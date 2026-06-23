import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    requests = None


ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"
STATE_DIR = Path(__file__).resolve().parent.parent.parent / "State"


class Snapshot:
    def __init__(
        self,
        state: dict,
        cadence: Optional[dict] = None,
        timeline: Optional[list] = None,
        projects: Optional[dict] = None,
        version: int = 1,
        timestamp: Optional[str] = None,
    ):
        self.version = version
        self.timestamp = timestamp or datetime.now(timezone.utc).isoformat()
        self.state = state
        self.cadence = cadence or {}
        self.timeline = timeline or []
        self.projects = projects or {}

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "timestamp": self.timestamp,
            "state": self.state,
            "cadence": self.cadence,
            "timeline": self.timeline,
            "projects": self.projects,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Snapshot":
        return cls(
            version=data.get("version", 1),
            timestamp=data.get("timestamp", ""),
            state=data.get("state", {}),
            cadence=data.get("cadence", {}),
            timeline=data.get("timeline", []),
            projects=data.get("projects", {}),
        )


def read_env() -> dict:
    if not ENV_PATH.exists():
        return {}
    env = {}
    raw = ENV_PATH.read_text(encoding="utf-8-sig")
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip()
    return env


def read_state_file(name: str) -> str:
    path = STATE_DIR / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_snapshot() -> Snapshot:
    current_state = read_state_file("CURRENT_STATE.md")
    cadence = read_state_file("CADENCE.md")
    tl_path = STATE_DIR.parent / "concepts" / "TIMELINE.md"
    timeline = tl_path.read_text(encoding="utf-8") if tl_path.exists() else ""

    state = {
        "date": _extract_field(current_state, r"\*\*Date:\*\*\s*(.*)"),
        "mode": _extract_field(current_state, r"\*\*Operating Mode:\*\*\s*(.*)"),
        "cash": _extract_field(current_state, r"\*\*Cash.*:\*\*\s*(.*)"),
        "top_priority": _extract_field(current_state, r"\*\*Top Priority:\*\*\s*(.*)"),
        "bottleneck": _extract_field(current_state, r"\*\*Current Bottleneck:\*\*\s*(.*)"),
    }

    c = {
        "session_start": _extract_field(cadence, r"\*\*Session start:\*\*\s*(.*)"),
        "session_end": _extract_field(cadence, r"\*\*Session end:\*\*\s*(.*)"),
    }

    events = []
    for line in timeline.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] not in ("Date", ""):
                events.append({
                    "date": cols[0],
                    "event": cols[1],
                    "decision": cols[2],
                    "outcome": cols[3],
                })

    lifecycle = read_state_file("LIFECYCLE.md")
    projects = {}
    in_table = False
    for line in lifecycle.splitlines():
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if in_table and line.startswith("|") and not line.startswith("|---"):
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 2:
                projects[cols[0]] = {"phase": cols[1] if len(cols) > 1 else ""}

    return Snapshot(state=state, cadence=c, timeline=events, projects=projects)


def _extract_field(text: str, pattern: str) -> str:
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def _gist_api_url(url: str) -> str:
    m = re.search(r"gist\.github\.com/[^/]+/([a-f0-9]+)", url)
    if m:
        return f"https://api.github.com/gists/{m.group(1)}"
    if "api.github.com/gists/" in url:
        return url
    return url


ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def _get_public_gist_files(base_dir: Path) -> dict:
    engine_dir = base_dir / "Runtime" / "engine"
    seed_path = base_dir / "FOUNDER_SEED.md"
    opencode_path = base_dir / "opencode.json"

    files = {}

    if seed_path.exists():
        files["FOUNDER_SEED.md"] = {"content": seed_path.read_text(encoding="utf-8")}

    engine_scripts = ["installer.py", "sync.py", "watchtower.py", "timekeeper.py"]
    for name in engine_scripts:
        path = engine_dir / name
        if path.exists():
            files[name] = {"content": path.read_text(encoding="utf-8")}

    if opencode_path.exists():
        files["opencode.json"] = {"content": opencode_path.read_text(encoding="utf-8")}

    return files


def cmd_pull(env: dict) -> str:
    url = _gist_api_url(env.get("FHQ_GIST_URL", ""))
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Gist GET returned {resp.status_code}"
        data = resp.json()
        files = data.get("files", {})
        if not files:
            return "ERROR: No files found in Gist"
        snap_file = None
        for fname, finfo in files.items():
            if "snapshot" in fname.lower():
                snap_file = finfo
                break
        if not snap_file:
            for fname, finfo in files.items():
                if fname.endswith(".json") and finfo.get("size", 0) > 10:
                    snap_file = finfo
                    break
        if not snap_file:
            return "ERROR: No valid snapshot file found (all files are empty or <10 bytes)"
        content = snap_file.get("content", "")
        if not content or len(content) < 10:
            return "ERROR: Empty or near-empty snapshot file"
        inbox_path = STATE_DIR / "_SYNC_INBOX.md"
        inbox_path.write_text(
            f"# SYNC INBOX\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n```json\n{content}\n```\n",
            encoding="utf-8",
        )
        return f"OK: Snapshot pulled ({len(content)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_push(env: dict) -> str:
    url = _gist_api_url(env.get("FHQ_GIST_URL", ""))
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    snap = build_snapshot()
    payload = json.dumps(snap.to_dict(), indent=2)
    try:
        resp = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": {"snapshot.json": {"content": payload}}},
            timeout=15,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist PATCH returned {resp.status_code}"
        return f"OK: Snapshot pushed ({len(payload)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_merge() -> str:
    inbox_path = STATE_DIR / "_SYNC_INBOX.md"
    if not inbox_path.exists():
        return "ERROR: No staged snapshot found (run pull first)"
    text = inbox_path.read_text(encoding="utf-8")
    m = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not m:
        return "ERROR: No JSON found in _SYNC_INBOX.md"
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return f"ERROR: Invalid JSON: {e}"
    snap = Snapshot.from_dict(data)

    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if cs_path.exists() and snap.state:
        cs_text = cs_path.read_text(encoding="utf-8")
        field_map = {
            "mode": "Operating Mode",
            "cash": "Cash",
            "top_priority": "Top Priority",
            "bottleneck": "Current Bottleneck",
            "date": "Date",
        }
        for key, val in snap.state.items():
            if val:
                field = field_map.get(key, key)
                cs_text = re.sub(r"(\*\*" + re.escape(field) + r":\*\*).*", r"\1 " + val, cs_text)
        cs_path.write_text(cs_text, encoding="utf-8")

    cad_path = STATE_DIR / "CADENCE.md"
    if cad_path.exists() and snap.cadence:
        cad_text = cad_path.read_text(encoding="utf-8")
        c_map = {"session_start": "Session start", "session_end": "Session end"}
        for key, val in snap.cadence.items():
            if val:
                field = c_map.get(key, key)
                cad_text = re.sub(r"(\*\*" + re.escape(field) + r":\*\*\s*).*", r"\1 " + val, cad_text)
        cad_path.write_text(cad_text, encoding="utf-8")

    if snap.timeline:
        tl_path = STATE_DIR.parent / "concepts" / "TIMELINE.md"
        if tl_path.exists():
            tl_text = tl_path.read_text(encoding="utf-8")
            for event in snap.timeline:
                new_row = f"\n| {event.get('date', '?')} | {event.get('event', '')} | {event.get('decision', '')} | {event.get('outcome', '')} |"
                if new_row not in tl_text:
                    tl_text += new_row
            tl_path.write_text(tl_text, encoding="utf-8")

    if snap.projects:
        lc_path = STATE_DIR / "LIFECYCLE.md"
        if lc_path.exists():
            lc_text = lc_path.read_text(encoding="utf-8")
            for proj_name, proj_state in snap.projects.items():
                phase = proj_state.get("phase", "")
                if phase and proj_name in lc_text:
                    lines = lc_text.splitlines()
                    new_lines = []
                    for line in lines:
                        if line.startswith(f"| {proj_name} |") and "|" in line:
                            cols = line.split("|")
                            if len(cols) >= 3:
                                cols[2] = f" {phase} "
                                line = "|".join(cols)
                        new_lines.append(line)
                    lc_text = "\n".join(new_lines)
            lc_path.write_text(lc_text, encoding="utf-8")

    inbox_path.unlink(missing_ok=True)
    return "OK: Merge complete"


def cmd_create_public_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"

    files = _get_public_gist_files(ROOT_DIR)
    if "FOUNDER_SEED.md" not in files:
        return "ERROR: FOUNDER_SEED.md not found"
    if "installer.py" not in files:
        return "ERROR: installer.py not found"

    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={
                "description": "FounderHQ V4 — Bootstrap Seed. Clone to install FHQ on any machine.",
                "public": True,
                "files": files,
            },
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist POST returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        gist_url = data.get("html_url", "")
        return f"OK: Public Gist created at {gist_url} ({len(files)} files)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_recreate_private_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"

    # 1. Delete existing Gist if URL is configured
    old_url = env.get("FHQ_GIST_URL", "")
    if old_url:
        api_url = _gist_api_url(old_url)
        try:
            resp = requests.delete(api_url, headers={"Authorization": f"token {token}"}, timeout=15)
            if resp.status_code not in (200, 204):
                return f"ERROR: Delete existing Gist returned {resp.status_code}"
        except Exception as e:
            return f"ERROR: Failed to delete existing Gist: {e}"

    # 2. Build snapshot from current state
    snap = build_snapshot()
    payload = json.dumps(snap.to_dict(), indent=2)

    # 3. Create new private Gist
    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={
                "description": "FounderHQ V4 — Private State Sync (auto-generated)",
                "public": False,
                "files": {"snapshot.json": {"content": payload}},
            },
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Create Gist returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        new_url = data.get("html_url", "")
        new_id = data.get("id", "")
        output = f"OK: Private Gist recreated.\nURL={new_url}\nID={new_id}\n"
        output += f"Update your .env: FHQ_GIST_URL={new_url}"
        return output
    except Exception as e:
        return f"ERROR: {e}"


def cmd_create_private_gist(env: dict) -> str:
    """Create a new private Gist for a first-time user. Auto-writes URL to .env."""
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={
                "description": "FounderHQ V4 — Private State Sync (auto-generated)",
                "public": False,
                "files": {"snapshot.json": {"content": "{}"}},
            },
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Create Gist returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        new_url = data.get("html_url", "")
        # Auto-write URL to .env
        env_path = ROOT_DIR / ".env"
        if env_path.exists():
            content = env_path.read_text("utf-8-sig", errors="replace")
            if "FHQ_GIST_URL=" in content:
                lines = []
                for line in content.splitlines():
                    if line.startswith("FHQ_GIST_URL="):
                        continue
                    lines.append(line)
                content = "\n".join(lines) + "\n"
            content += f"FHQ_GIST_URL={new_url}\n"
            env_path.write_text(content, encoding="utf-8")
            try:
                os.chmod(env_path, 0o600)
            except (OSError, NotImplementedError):
                pass
            return f"OK: Private Gist created at {new_url} (saved to .env)"
        return f"OK: Private Gist created at {new_url}\nUpdate your .env: FHQ_GIST_URL={new_url}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_clean_private_gist(env: dict) -> str:
    url = _gist_api_url(env.get("FHQ_GIST_URL", ""))
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Gist GET returned {resp.status_code}"
        data = resp.json()
        files = data.get("files", {})
        keep = {"snapshot.json"}
        delete_files = {name for name in files if name not in keep}
        remove_map = {}
        for name in delete_files:
            remove_map[name] = None
        if not remove_map:
            return "OK: No orphan files to clean"
        resp2 = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": remove_map},
            timeout=15,
        )
        if resp2.status_code not in (200, 201):
            return f"ERROR: Clean PATCH returned {resp2.status_code}"
        return f"OK: Removed {len(delete_files)} orphan file(s): {', '.join(sorted(delete_files))}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_pull_public(env: dict) -> str:
    url = env.get("FHQ_GIST_PUBLIC_URL", "")
    if not url:
        return "OK: No public Gist configured (FHQ_GIST_PUBLIC_URL not set)"
    api_url = _gist_api_url(url)
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(api_url, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Public Gist GET returned {resp.status_code}"
        data = resp.json()
        files = data.get("files", {})
        if not files:
            return "ERROR: No files in public Gist"
        version_file = None
        for fname, finfo in files.items():
            if "seed" in fname.lower() or "version" in fname.lower():
                version_file = finfo
                break
        if not version_file:
            version_file = list(files.values())[0]
        out_path = STATE_DIR / "_PUBLIC_VERSION.md"
        out_path.write_text(
            f"# PUBLIC BOOTSTRAP VERSION\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n"
            f"**Latest version:** {version_file.get('filename', 'unknown')}\n"
            f"**Size:** {version_file.get('size', 0)} bytes\n"
            f"**URL:** {url}\n",
            encoding="utf-8",
        )
        return f"OK: Public bootstrap version checked ({len(files)} files, latest {version_file.get('size', 0)} bytes)"
    except Exception as e:
        return f"OK: Public Gist not reachable ({e}) — skipping bootstrap check"


PUBLIC_GIST_ID = "5b7b5c36610cc1076c798c716c7560e6"

def cmd_update_public_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"

    files = _get_public_gist_files(ROOT_DIR)
    if not files:
        return "ERROR: No files to upload"

    url = f"https://api.github.com/gists/{PUBLIC_GIST_ID}"
    try:
        resp = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": files},
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: PATCH returned {resp.status_code}: {resp.text[:200]}"
        return f"OK: Public Gist updated ({len(files)} files)"
    except Exception as e:
        return f"ERROR: {e}"


def main():
    parser = argparse.ArgumentParser(description="FHQ state sync via Gist")
    parser.add_argument("command", choices=["pull", "push", "merge", "create-public-gist", "create-private-gist", "clean-private-gist", "pull-public", "recreate-private-gist", "update-public-gist"], help="Sync command")
    args = parser.parse_args()
    env = read_env()
    if args.command == "pull":
        result = cmd_pull(env)
    elif args.command == "push":
        result = cmd_push(env)
    elif args.command == "merge":
        result = cmd_merge(env)
    elif args.command == "create-public-gist":
        result = cmd_create_public_gist(env)
    elif args.command == "create-private-gist":
        result = cmd_create_private_gist(env)
    elif args.command == "clean-private-gist":
        result = cmd_clean_private_gist(env)
    elif args.command == "recreate-private-gist":
        result = cmd_recreate_private_gist(env)
    elif args.command == "pull-public":
        result = cmd_pull_public(env)
    elif args.command == "update-public-gist":
        result = cmd_update_public_gist(env)
    else:
        result = "ERROR: Unknown command"
    print(result)


if __name__ == "__main__":
    main()
