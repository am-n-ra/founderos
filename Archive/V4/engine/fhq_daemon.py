"""FounderHQ Daemon — MCP stdio + Streamable HTTP + REST.

Single binary that enforces cycle counter server-side.
Run modes:
  python fhq_daemon.py --mode stdio    (local MCP subprocess)
  python fhq_daemon.py --mode http     (remote MCP via FastAPI)
  python fhq_daemon.py --mode rest     (bare HTTP for sandboxes)
"""

import asyncio, json, subprocess, sys, time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Optional

FOUNDERHQ_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CYCLE_SCRIPT = FOUNDERHQ_ROOT / "FounderOS/Runtime/engine/cycle.py"
SYNC_SCRIPT = FOUNDERHQ_ROOT / "FounderOS/Runtime/engine/sync.py"
MAX_CYCLE_AGE = 60  # seconds


@dataclass
class CycleState:
    counter: int = 0
    timestamp: float = 0.0
    header: str = ""
    dx_command: str = ""
    diagnosis: str = ""
    lock: Lock = field(default_factory=Lock)

    @property
    def is_stale(self) -> bool:
        return (time.time() - self.timestamp) > MAX_CYCLE_AGE

    @property
    def age_seconds(self) -> float:
        return time.time() - self.timestamp

    def to_dict(self) -> dict:
        return {
            "counter": self.counter,
            "header": self.header,
            "dx": self.dx_command,
            "age_s": round(self.age_seconds, 1),
            "is_stale": self.is_stale,
        }


class FHQDaemon:
    def __init__(self):
        self.state = CycleState()
        self._stop = False
        self._mode = "unknown"

    def log(self, msg: str):
        ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", file=sys.stderr, flush=True)

    # ── Cycle ──────────────────────────────────────────

    def run_cycle(self) -> dict:
        if self._stop:
            return {"error": "SHUTDOWN"}

        try:
            result = subprocess.run(
                [sys.executable, str(CYCLE_SCRIPT), "--mode", "boot"],
                capture_output=True, text=True, cwd=str(FOUNDERHQ_ROOT),
                timeout=30,
            )
            if result.returncode != 0:
                self.log(f"cycle.py returned {result.returncode}: {result.stderr.strip()}")
        except subprocess.TimeoutExpired:
            self.log("cycle.py timed out after 30s")
            return {"error": "CYCLE_TIMEOUT"}

        cycle_required = FOUNDERHQ_ROOT / "FounderOS/State/_CYCLE_REQUIRED_HEADER.md"
        counter_file = FOUNDERHQ_ROOT / "FounderOS/State/_CYCLE_COUNTER.md"
        diagnosis_file = FOUNDERHQ_ROOT / "FounderOS/State/_DIAGNOSIS.md"

        with self.state.lock:
            if cycle_required.exists():
                lines = cycle_required.read_text().strip().split("\n")
                self.state.header = lines[0] if len(lines) >= 1 else ""
                self.state.dx_command = lines[1] if len(lines) >= 2 else ""
                counter_raw = lines[2].replace("CYCLE=", "").strip() if len(lines) >= 3 else "0"
                if counter_file.exists():
                    self.state.counter = int(counter_file.read_text().strip())
                elif counter_raw.isdigit():
                    self.state.counter = int(counter_raw)
                self.state.timestamp = time.time()
            if diagnosis_file.exists():
                self.state.diagnosis = diagnosis_file.read_text().strip()

        self.log(f"Cycle {self.state.counter} complete. DX: {self.state.dx_command}")
        return self.state.to_dict()

    def require_fresh_cycle(self) -> Optional[dict]:
        """Return state dict if fresh, None if stale."""
        with self.state.lock:
            if self.state.is_stale:
                return None
            return self.state.to_dict()

    # ── File access (gated) ────────────────────────────

    def _resolve_path(self, rel_path: str) -> Path:
        p = (FOUNDERHQ_ROOT / rel_path).resolve()
        if not str(p).startswith(str(FOUNDERHQ_ROOT)):
            raise PermissionError(f"Path outside FounderHQ root: {rel_path}")
        return p

    def read_file(self, rel_path: str) -> dict:
        gate = self.require_fresh_cycle()
        if gate is None:
            with self.state.lock:
                age = self.state.age_seconds
            return {"error": "CYCLE_STALE", "age_s": age}
        full = self._resolve_path(rel_path)
        if not full.exists():
            return {"error": "NOT_FOUND", "path": rel_path}
        return {"content": full.read_text(encoding="utf-8"), "path": rel_path}

    def write_file(self, rel_path: str, content: str) -> dict:
        gate = self.require_fresh_cycle()
        if gate is None:
            with self.state.lock:
                age = self.state.age_seconds
            return {"error": "CYCLE_STALE", "age_s": age}
        full = self._resolve_path(rel_path)
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")
        self.log(f"Wrote {rel_path}")
        return {"status": "written", "path": rel_path}

    # ── Gist sync ──────────────────────────────────────

    def sync_pull(self) -> dict:
        try:
            result = subprocess.run(
                [sys.executable, str(SYNC_SCRIPT), "pull"],
                capture_output=True, text=True, cwd=str(FOUNDERHQ_ROOT),
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            return {"error": "SYNC_TIMEOUT"}
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}

    def sync_push(self) -> dict:
        try:
            result = subprocess.run(
                [sys.executable, str(SYNC_SCRIPT), "push"],
                capture_output=True, text=True, cwd=str(FOUNDERHQ_ROOT),
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            return {"error": "SYNC_TIMEOUT"}
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}

    def status(self) -> dict:
        s = self.state.to_dict()
        s["mode"] = self._mode
        return s

    # ── Lifecycle ──────────────────────────────────────

    async def cycle_loop(self):
        """Background loop: run cycle every MAX_CYCLE_AGE seconds."""
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.run_cycle)
        while not self._stop:
            await asyncio.sleep(MAX_CYCLE_AGE)
            await loop.run_in_executor(None, self.run_cycle)

    def stop(self):
        self._stop = True


# === Shared tool definitions ===

TOOL_DEFINITIONS = [
    {
        "name": "fhq_cycle",
        "description": "Run cycle.py and refresh state. MUST be called first. Returns header + DX command + counter.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "fhq_status",
        "description": "Get daemon status: cycle counter, age, staleness, mode.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "fhq_read",
        "description": "Read a FounderHQ file. Fails with CYCLE_STALE if cycle >60s old.",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "fhq_write",
        "description": "Write content to a FounderHQ file. Fails if cycle stale.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "fhq_sync_pull",
        "description": "Pull latest state from private Gist.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "fhq_sync_push",
        "description": "Push current state to private Gist.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "fhq_run",
        "description": "Run a cycle mode (fhq, fhqa, boot). Returns cycle output.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "mode": {
                    "type": "string",
                    "enum": ["fhq", "fhqa", "boot"],
                    "description": "Cycle mode to run",
                }
            },
            "required": ["mode"],
        },
    },
]

# === MCP stdio transport ===

try:
    import mcp.server.stdio
    import mcp.types as types
    from mcp.server import Server
    from mcp.server.models import InitializationOptions
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False


def create_mcp_server(daemon: FHQDaemon) -> Server:
    """Create MCP server with FounderHQ tools.

    The daemon enforces all cycle requirements server-side:
    - fhq_cycle: always available (refreshes state)
    - fhq_status: always available
    - fhq_sync_pull/push: always available
    - fhq_read/fhq_write: return CYCLE_STALE error if cycle >60s old
    - fhq_run: returns CYCLE_STALE error if cycle >60s old
    """
    server = Server("founderhq")

    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [types.Tool(**t) for t in TOOL_DEFINITIONS]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        """Handle tool call. Enforce cycle freshness server-side."""
        result = await _handle_tool_call(daemon, name, arguments)
        return [types.TextContent(type="text", text=json.dumps(result, indent=2))]

    return server


async def _handle_tool_call(daemon: FHQDaemon, name: str, args: dict) -> dict:
    """Dispatch tool call with cycle enforcement gate.

    Tools that require fresh cycle (fhq_read, fhq_write, fhq_run)
    check daemon.require_fresh_cycle() first and return CYCLE_STALE error.
    Tools that are always available (fhq_cycle, fhq_status, sync) bypass the gate.
    """
    if name == "fhq_cycle":
        return daemon.run_cycle()
    if name == "fhq_status":
        return daemon.status()
    if name == "fhq_sync_pull":
        return daemon.sync_pull()
    if name == "fhq_sync_push":
        return daemon.sync_push()

    # Tools below require fresh cycle
    gate = daemon.require_fresh_cycle()
    if gate is None:
        return {
            "error": "CYCLE_STALE",
            "age_s": daemon.state.age_seconds,
            "message": "Run fhq_cycle first. Cycle is stale (>60s).",
        }

    if name == "fhq_read":
        return daemon.read_file(args["path"])
    if name == "fhq_write":
        return daemon.write_file(args["path"], args["content"])
    if name == "fhq_run":
        mode = args.get("mode", "fhq")
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None,
            lambda: subprocess.run(
                [sys.executable, str(CYCLE_SCRIPT), "--mode", mode],
                capture_output=True, text=True, cwd=str(FOUNDERHQ_ROOT),
                timeout=30,
            ),
        )
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}

    return {"error": f"Unknown tool: {name}"}


async def run_stdio(daemon: FHQDaemon):
    """Run daemon in MCP stdio mode.

    The LLM client launches this as a subprocess and communicates via stdin/stdout.
    First cycle runs immediately, then the event loop waits for MCP messages.
    """
    daemon._mode = "stdio"
    await asyncio.get_running_loop().run_in_executor(None, daemon.run_cycle)
    server = create_mcp_server(daemon)
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="founderhq",
                server_version="1.0.0",
                capabilities=types.ServerCapabilities(tools=types.ToolsCapability()),
            ),
        )


# === Streamable HTTP transport ===

try:
    from fastapi import FastAPI, HTTPException, Request
    from pydantic import BaseModel
    import uvicorn
    HTTP_AVAILABLE = True
except ImportError:
    HTTP_AVAILABLE = False


if HTTP_AVAILABLE:
    class _WriteBody(BaseModel):
        content: str


    def create_http_app(daemon: FHQDaemon) -> FastAPI:
        """Create FastAPI application serving MCP Streamable HTTP + REST endpoints.

        Two interfaces on the same server:
        1. /mcp endpoint: JSON-RPC 2.0 MCP protocol
        2. /api/* endpoints: Simple REST for sandbox clients (LM Arena, Manus)
        """
        app = FastAPI(title="FounderHQ")

        @app.get("/health")
        async def health():
            return {"status": "alive", "cycle": daemon.state.counter, "age_s": daemon.state.age_seconds}

        @app.get("/.well-known/mcp.json")
        async def mcp_well_known(request: Request):
            """MCP server metadata for auto-discovery (Claude Connectors)."""
            base = f"{request.url.scheme}://{request.url.hostname}"
            return {
                "name": "FounderHQ",
                "description": "Personal OS for solo entrepreneurs — cycle enforcement, state management, Gist sync",
                "url": f"{base}/mcp",
                "tools": [{"name": t["name"], "description": t["description"]} for t in TOOL_DEFINITIONS],
                "transport": "streamable-http",
            }

        # ── MCP Streamable HTTP endpoint ──

        @app.post("/mcp")
        async def mcp_endpoint(body: dict):
            """MCP JSON-RPC 2.0 endpoint.

            Accepts tools/list and tools/call methods.
            Delegates to the same _handle_tool_call as stdio mode.
            """
            method = body.get("method", "")
            params = body.get("params", {})
            msg_id = body.get("id", 1)

            if method == "tools/list":
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"tools": TOOL_DEFINITIONS},
                }

            if method == "tools/call":
                tool_name = params.get("name", "")
                tool_args = params.get("arguments", {})
                result = await _handle_tool_call(daemon, tool_name, tool_args)
                if "error" in result:
                    return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32000, "message": result["error"]}}
                return {"jsonrpc": "2.0", "id": msg_id, "result": result}

            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }

        # ── REST API for sandbox clients (LM Arena, Manus) ──

        @app.get("/api/cycle")
        async def api_cycle():
            return daemon.run_cycle()

        @app.get("/api/status")
        async def api_status():
            return daemon.status()

        @app.get("/api/read/{path:path}")
        async def api_read(path: str):
            result = await _handle_tool_call(daemon, "fhq_read", {"path": path})
            if "error" in result:
                status_code = 412 if result["error"] == "CYCLE_STALE" else 404
                raise HTTPException(status_code=status_code, detail=result)
            return result

        @app.post("/api/write/{path:path}")
        async def api_write(path: str, body: _WriteBody):
            result = await _handle_tool_call(daemon, "fhq_write", {"path": path, "content": body.content})
            if "error" in result:
                raise HTTPException(status_code=412, detail=result)
            return result

        return app


    async def run_http(daemon: FHQDaemon, host: str = "127.0.0.1", port: int = 8742):
        """Run daemon in HTTP mode (Streamable HTTP + REST API).

        Also starts the background cycle loop so state stays fresh.
        """
        daemon._mode = "http"
        await asyncio.get_running_loop().run_in_executor(None, daemon.run_cycle)
        app = create_http_app(daemon)
        config = uvicorn.Config(app, host=host, port=port, log_level="info")
        server = uvicorn.Server(config)
        await server.serve()


# === Main entry point ===


async def main():
    """Parse CLI args and start daemon in requested mode.

    Modes:
      stdio  - MCP stdio transport (local subprocess, default)
      http   - MCP Streamable HTTP + REST API (local or remote server)
      rest   - REST API only (lightweight, no MCP tools/list)
    """
    import argparse

    parser = argparse.ArgumentParser(description="FounderHQ MCP Daemon")
    parser.add_argument(
        "--mode", choices=["stdio", "http", "rest"], default="stdio",
        help="Transport mode (default: stdio)",
    )
    parser.add_argument(
        "--port", type=int, default=8742,
        help="HTTP port (default: 8742, http/rest modes only)",
    )
    parser.add_argument(
        "--host", default="127.0.0.1",
        help="HTTP bind address (default: 127.0.0.1, http/rest modes only)",
    )
    args = parser.parse_args()

    daemon = FHQDaemon()
    daemon.log(f"Starting daemon in {args.mode} mode...")

    try:
        if args.mode == "stdio":
            if not MCP_AVAILABLE:
                print("ERROR: mcp package not installed.", file=sys.stderr)
                print("Install: pip install -r FounderOS/Runtime/engine/requirements-daemon.txt", file=sys.stderr)
                sys.exit(1)
            await run_stdio(daemon)
        elif args.mode in ("http", "rest"):
            if not HTTP_AVAILABLE:
                print("ERROR: fastapi/uvicorn not installed.", file=sys.stderr)
                print("Install: pip install -r FounderOS/Runtime/engine/requirements-daemon.txt", file=sys.stderr)
                sys.exit(1)
            if args.mode == "rest":
                daemon._mode = "rest"
                await asyncio.get_running_loop().run_in_executor(None, daemon.run_cycle)
                # For REST mode, we use the same HTTP app but only
                # use /api/* endpoints, ignoring /mcp.
                app = create_http_app(daemon)
                import uvicorn
                config = uvicorn.Config(app, host=args.host, port=args.port, log_level="info")
                server = uvicorn.Server(config)
                await server.serve()
            else:
                await run_http(daemon, host=args.host, port=args.port)
    except KeyboardInterrupt:
        daemon.log("Shutting down...")
    finally:
        daemon.stop()
        daemon.log("Daemon stopped.")


if __name__ == "__main__":
    asyncio.run(main())
