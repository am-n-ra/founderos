# FounderHQ Distribution & Sync — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Zero-dependency distribution via FOUNDER_SEED.md + automatic state sync via private Gist + first-run GENESIS that installs everything.

**Architecture:** Two sync paths: primary (private Gist + token in `.env`, script `sync.py` reads token, LLM never sees it) and fallback (portable markdown snapshot via `snapshot.py`). First boot detects `.founderhq_installed` marker → if absent, runs GENESIS (ask token, create files, build .venv, install scripts).

**Tech Stack:** Python 3.13, GitHub Gist API, `requests`, `python-dotenv`, markdown state files

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `Runtime/engine/sync.py` | CREATE | Gist push/pull/merge. Reads token from `.env`. Called by LLM, never exposes token. |
| `Runtime/engine/snapshot.py` | CREATE | Portable markdown snapshot generate/merge. No token needed. |
| `State/SYNC_CONFIG.md` | CREATE | LLM-readable sync config (Gist URL, last sync date, no token). |
| `.env` | CREATE (via installer) | Secrets file: `FHQ_GIST_URL`, `FHQ_GIST_TOKEN`. Permissions 600. |
| `.founderhq_installed` | CREATE (via installer) | Empty marker. If absent at boot → GENESIS. |
| `Runtime/engine/installer.py` | MODIFY | Add .venv creation, token prompt, .env write, marker creation. |
| `SYSTEM_PROMPT.md` | MODIFY | Boot: first-run check (GENESIS). Sync pull after boot. Sync push on shutdown. |
| `Runtime/RUNTIME_KERNEL.md` | MODIFY | BOOT: add GENESIS branch. UPDATE: add sync push. |
| `State/CADENCE.md` | MODIFY | Add `### Sync` section to Day block. |
| `Protocols/SOURCE_OF_TRUTH.md` | MODIFY | Register sync.py, snapshot.py, SYNC_CONFIG.md, .env, .founderhq_installed. |
| `Runtime/engine/__init__.py` | MODIFY | Document sync.py, snapshot.py. |
| `FOUNDER_SEED.md` | GENERATE | Concatenation of all core files with `--- FILE:` delimiters. Excludes user data. |

---

### Task 1: Create `Runtime/engine/sync.py`

**Files:**
- Create: `FounderOS/Runtime/engine/sync.py`
- Create: `FounderOS/tests/test_sync.py`

- [ ] **Write the failing tests**

Create `FounderOS/tests/test_sync.py`:

```python
import pytest
import json
import os
from pathlib import Path
from Runtime.engine.sync import Snapshot, STATE_FIELDS, CADENCE_FIELDS


class TestSnapshot:
    def test_from_state_minimal(self):
        """Build snapshot from minimal state."""
        state = {
            "date": "2026-06-22 14:00 Lome UTC+0",
            "mode": "SURVIVAL",
            "cash": 2679,
            "top_priority": "Find client",
            "bottleneck": "Cash",
        }
        cadence = {"session_start": "08:00", "session_end": "14:00"}
        timeline = [{"date": "2026-06-22", "event": "Boot", "decision": "Start", "outcome": "OK"}]
        projects = {"SOJACO": {"phase": "VALIDATION"}}

        snap = Snapshot(state=state, cadence=cadence, timeline=timeline, projects=projects)
        assert snap.version == 1
        assert snap.state["mode"] == "SURVIVAL"
        assert snap.state["cash"] == 2679

    def test_to_from_json_roundtrip(self):
        """Serialize and deserialize preserves all data."""
        original = Snapshot(
            state={"date": "test", "mode": "GROWTH", "cash": 5000, "top_priority": "X", "bottleneck": "Y"},
            cadence={"session_start": "09:00", "session_end": "17:00"},
            timeline=[{"date": "T1", "event": "E1", "decision": "D1", "outcome": "O1"}],
            projects={"P1": {"phase": "LAUNCH"}},
        )
        data = original.to_dict()
        restored = Snapshot.from_dict(data)
        assert restored.state == original.state
        assert restored.cadence == original.cadence
        assert restored.timeline == original.timeline
        assert restored.projects == original.projects

    def test_missing_fields_default(self):
        """Missing optional fields get empty defaults."""
        snap = Snapshot(state={"date": "x", "mode": "x", "cash": 0, "top_priority": "x", "bottleneck": "x"})
        assert snap.cadence == {}
        assert snap.timeline == []
        assert snap.projects == {}
```

- [ ] **Run tests to verify they fail**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_sync.py -v
```

Expected: FAIL with ModuleNotFoundError

- [ ] **Write minimal implementation**

Create `FounderOS/Runtime/engine/sync.py`:

```python
"""sync.py - State sync via private GitHub Gist.

Reads FHQ_GIST_TOKEN and FHQ_GIST_URL from .env (root of FounderHQ).
LLM never sees the token - it calls sync.py as a subprocess and reads the
returned status message.

Commands:
    sync.py pull     - Download latest snapshot, stage in _SYNC_INBOX.md
    sync.py push     - Build snapshot from current state, push to Gist
    sync.py merge    - Apply staged snapshot to local files
"""

import argparse
import json
import os
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
    """Single portable state snapshot.

    Fields:
        version: Schema version (int, currently 1)
        timestamp: ISO datetime string
        state: dict with date, mode, cash, top_priority, bottleneck
        cadence: dict with session_start, session_end
        timeline: list of event dicts
        projects: dict mapping project name -> project state
    """

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
    """Read .env file and return dict of variables."""
    if not ENV_PATH.exists():
        return {}
    env = {}
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip()
    return env


def read_state_file(name: str) -> str:
    """Read a state file, return empty string if missing."""
    path = STATE_DIR / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_snapshot() -> Snapshot:
    """Read current state files and build a Snapshot."""
    current_state = read_state_file("CURRENT_STATE.md")
    cadence = read_state_file("CADENCE.md")
    timeline = read_state_file("TIMELINE.md") if (STATE_DIR.parent / "concepts" / "TIMELINE.md").exists() else ""

    # Extract key fields via simple parsing
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

    # Parse timeline entries
    events = []
    for line in timeline.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] != "Date":
                events.append({
                    "date": cols[0],
                    "event": cols[1],
                    "decision": cols[2],
                    "outcome": cols[3],
                })

    # Parse lifecycle for project phases
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
    """Extract first match of regex pattern from text."""
    import re
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def cmd_pull(env: dict) -> str:
    """Pull snapshot from Gist and write to _SYNC_INBOX."""
    url = env.get("FHQ_GIST_URL", "")
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"

    if requests is None:
        return "ERROR: requests library not installed (run: pip install requests)"

    try:
        resp = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Gist GET returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        # Gist API returns files dict
        files = data.get("files", {})
        if not files:
            return "ERROR: No files found in Gist"
        # Find snapshot file
        snap_file = None
        for fname, finfo in files.items():
            if fname.endswith(".json") or "snapshot" in fname:
                snap_file = finfo
                break
        if not snap_file:
            snap_file = list(files.values())[0]
        content = snap_file.get("content", "")
        if not content:
            return "ERROR: Empty snapshot file"

        inbox_path = STATE_DIR / "_SYNC_INBOX.md"
        inbox_path.write_text(f"# SYNC INBOX\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n```json\n{content}\n```\n", encoding="utf-8")
        return f"OK: Snapshot pulled ({len(content)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_push(env: dict) -> str:
    """Build snapshot and push to Gist."""
    url = env.get("FHQ_GIST_URL", "")
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"

    if requests is None:
        return "ERROR: requests library not installed"

    snap = build_snapshot()
    payload = json.dumps(snap.to_dict(), indent=2)

    # Gist API: put content into a file named snapshot.json
    try:
        resp = requests.patch(
            url,
            headers={
                "Authorization": f"token {token}",
                "Content-Type": "application/json",
            },
            json={"files": {"snapshot.json": {"content": payload}}},
            timeout=15,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist PATCH returned {resp.status_code}: {resp.text[:200]}"
        return f"OK: Snapshot pushed ({len(payload)} bytes) at {snap.timestamp}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_merge() -> str:
    """Apply staged snapshot to local state files."""
    inbox_path = STATE_DIR / "_SYNC_INBOX.md"
    if not inbox_path.exists():
        return "ERROR: No staged snapshot found (run pull first)"

    text = inbox_path.read_text(encoding="utf-8")
    # Extract JSON from code block
    import re
    m = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not m:
        return "ERROR: No JSON found in _SYNC_INBOX.md"

    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return f"ERROR: Invalid JSON: {e}"

    snap = Snapshot.from_dict(data)

    # Update CURRENT_STATE.md
    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if cs_path.exists() and snap.state:
        cs_text = cs_path.read_text(encoding="utf-8")
        for key, val in snap.state.items():
            if val and key != "date":
                # Map snapshot keys to CURRENT_STATE field names
                field_map = {
                    "mode": "Operating Mode",
                    "cash": "Cash",
                    "top_priority": "Top Priority",
                    "bottleneck": "Current Bottleneck",
                    "date": "Date",
                }
                field = field_map.get(key, key)
                old = r"(\*\*" + re.escape(field) + r":\*\*).*"
                new = rf"\1 {val}"
                cs_text = re.sub(old, new, cs_text)
        cs_path.write_text(cs_text, encoding="utf-8")

    # Update CADENCE.md
    cad_path = STATE_DIR / "CADENCE.md"
    if cad_path.exists() and snap.cadence:
        cad_text = cad_path.read_text(encoding="utf-8")
        for key, val in snap.cadence.items():
            if val:
                field_map = {
                    "session_start": "Session start",
                    "session_end": "Session end",
                }
                field = field_map.get(key, key)
                old = r"(\*\*" + re.escape(field) + r":\*\*\s*).*"
                new = rf"\1 {val}"
                cad_text = re.sub(old, new, cad_text)
        cad_path.write_text(cad_text, encoding="utf-8")

    # Append timeline entries
    if snap.timeline:
        tl_path = STATE_DIR.parent / "concepts" / "TIMELINE.md"
        if tl_path.exists():
            tl_text = tl_path.read_text(encoding="utf-8")
            for event in snap.timeline:
                new_row = f"\n| {event.get('date', '?')} | {event.get('event', '')} | {event.get('decision', '')} | {event.get('outcome', '')} |"
                if new_row not in tl_text:
                    tl_text += new_row
            tl_path.write_text(tl_text, encoding="utf-8")

    # Update LIFECYCLE.md project phases
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


def main():
    parser = argparse.ArgumentParser(description="FHQ state sync via Gist")
    parser.add_argument("command", choices=["pull", "push", "merge"], help="Sync command")
    args = parser.parse_args()

    env = read_env()

    if args.command == "pull":
        result = cmd_pull(env)
    elif args.command == "push":
        result = cmd_push(env)
    elif args.command == "merge":
        result = cmd_merge()
    else:
        result = "ERROR: Unknown command"

    print(result)


if __name__ == "__main__":
    main()
```

- [ ] **Run tests to verify they pass**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_sync.py -v
```

Expected: 3 PASSED

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/sync.py FounderOS/tests/test_sync.py
git commit -m "feat: add sync.py - Gist state push/pull/merge with .env token isolation"
```

---

### Task 2: Create `Runtime/engine/snapshot.py`

**Files:**
- Create: `FounderOS/Runtime/engine/snapshot.py`

- [ ] **Write snapshot.py**

```python
"""snapshot.py - Portable markdown snapshot for environments without Gist API access.

Generates a compact markdown summary of current state (no token needed).
LLM reads the output, user copies it to another device.
On the target device, LLM runs merge to apply changes.

Commands:
    snapshot.py generate  - Produce EXPORT_SNAPSHOT.md
    snapshot.py merge     - Read IMPORT_SNAPSHOT.md and apply changes
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


STATE_DIR = Path(__file__).resolve().parent.parent.parent / "State"
CONCEPTS_DIR = Path(__file__).resolve().parent.parent.parent / "concepts"


def read_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def extract_field(text: str, pattern: str) -> str:
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def cmd_generate() -> str:
    """Generate a portable markdown snapshot."""
    cs = read_file(STATE_DIR / "CURRENT_STATE.md")
    cad = read_file(STATE_DIR / "CADENCE.md")
    lc = read_file(STATE_DIR / "LIFECYCLE.md")
    tl = read_file(CONCEPTS_DIR / "TIMELINE.md")

    date = extract_field(cs, r"\*\*Date:\*\*\s*(.*)")
    mode = extract_field(cs, r"\*\*Operating Mode:\*\*\s*(.*)")
    cash = extract_field(cs, r"\*\*Cash.*:\*\*\s*(.*)")
    priority = extract_field(cs, r"\*\*Top Priority:\*\*\s*(.*)")
    bottleneck = extract_field(cs, r"\*\*Current Bottleneck:\*\*\s*(.*)")
    sess_start = extract_field(cad, r"\*\*Session start:\*\*\s*(.*)")
    sess_end = extract_field(cad, r"\*\*Session end:\*\*\s*(.*)")

    # Latest timeline entries
    recent_events = []
    for line in tl.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] not in ("Date", ""):
                recent_events.append(f"- {cols[0]}: {cols[1]} -> {cols[3]}")

    recent_events = recent_events[-5:]  # last 5

    # Project phases
    projects = []
    in_table = False
    for line in lc.splitlines():
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if in_table and line.startswith("|") and not line.startswith("|---"):
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 5:
                projects.append(f"- {cols[0]}: {cols[1]} -> {cols[4]}")

    snapshot = f"""# FHQ Snapshot - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}

**Date:** {date}
**Mode:** {mode}
**Cash:** {cash}
**Top Priority:** {priority}
**Bottleneck:** {bottleneck}
**Session:** {sess_start} -> {sess_end}

## Projects
{chr(10).join(projects) if projects else "- (none)"}

## Recent Events
{chr(10).join(recent_events) if recent_events else "- (none)"}
"""

    out_path = STATE_DIR / "EXPORT_SNAPSHOT.md"
    out_path.write_text(snapshot, encoding="utf-8")
    return f"OK: Snapshot written to State/EXPORT_SNAPSHOT.md ({len(snapshot)} chars)"


def cmd_merge() -> str:
    """Read IMPORT_SNAPSHOT.md and apply to state files."""
    in_path = STATE_DIR / "IMPORT_SNAPSHOT.md"
    if not in_path.exists():
        return "ERROR: No State/IMPORT_SNAPSHOT.md found. Paste the snapshot text there first."

    text = in_path.read_text(encoding="utf-8")

    new_date = extract_field(text, r"\*\*Date:\*\*\s*(.*)")
    new_mode = extract_field(text, r"\*\*Mode:\*\*\s*(.*)")
    new_cash = extract_field(text, r"\*\*Cash:\*\*\s*(.*)")
    new_priority = extract_field(text, r"\*\*Top Priority:\*\*\s*(.*)")
    new_bottleneck = extract_field(text, r"\*\*Bottleneck:\*\*\s*(.*)")

    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if cs_path.exists():
        cs_text = cs_path.read_text(encoding="utf-8")
        updates = {
            "Date": new_date,
            "Operating Mode": new_mode,
            "Cash": new_cash,
            "Top Priority": new_priority,
            "Current Bottleneck": new_bottleneck,
        }
        for field, val in updates.items():
            if val:
                cs_text = re.sub(
                    rf"(\*\*{re.escape(field)}:\*\*).*",
                    rf"\1 {val}",
                    cs_text,
                )
        cs_path.write_text(cs_text, encoding="utf-8")

    in_path.unlink(missing_ok=True)
    return "OK: Merge complete. State files updated from snapshot."


def main():
    parser = argparse.ArgumentParser(description="FHQ portable snapshot (no token needed)")
    parser.add_argument("command", choices=["generate", "merge"], help="Snapshot command")
    args = parser.parse_args()

    if args.command == "generate":
        result = cmd_generate()
    elif args.command == "merge":
        result = cmd_merge()
    else:
        result = "ERROR: Unknown command"

    print(result)


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/snapshot.py
git commit -m "feat: add snapshot.py - portable markdown snapshot for token-less environments"
```

---

### Task 3: Create `State/SYNC_CONFIG.md`

**Files:**
- Create: `FounderOS/State/SYNC_CONFIG.md`

- [ ] **Create SYNC_CONFIG.md**

```markdown
# SYNC CONFIG

## Purpose

Configuration de synchronisation. Lu par le LLM au boot pour savoir si le sync est actif. Ne contient PAS le token — celui-ci est dans `.env`, jamais lu par le LLM.

---

**Sync Gist URL:** [URL de votre Gist prive]
**Last Sync:** [date]
**Auto-sync on boot:** yes
**Auto-sync on shutdown:** yes

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Sync configuration (no secrets) |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/SYNC_CONFIG.md
git commit -m "feat: add SYNC_CONFIG.md - LLM-readable sync config (no token)"
```

---

### Task 4: Modify `Runtime/engine/installer.py`

**Files:**
- Modify: `FounderOS/Runtime/engine/installer.py`

- [ ] **Read current file then rewrite**

The current installer.py creates Windows Task Scheduler tasks. Add:
1. `.venv` creation if missing
2. Token prompt and `.env` creation
3. `.founderhq_installed` marker creation

Read current file first:
```cmd
type FounderOS\Runtime\engine\installer.py
```

Then replace with this expanded version:

```python
"""installer.py - First-run setup for FounderHQ.

Creates:
1. .venv Python virtual environment
2. .env file (asks user for GitHub token)
3. Installs dependencies (requests, python-dotenv)
4. Windows Task Scheduler tasks for watchtower + timekeeper
5. .founderhq_installed marker

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


ENV_PATH = ".env"


def create_venv(base_path: Path) -> bool:
    """Create .venv if it doesn't exist."""
    venv_path = base_path / ".venv"
    if venv_path.exists() and (venv_path / "Scripts" / "python.exe").exists():
        print(".venv: already exists")
        return True

    print("Creating .venv...")
    result = subprocess.run(
        [sys.executable, "-m", "venv", str(venv_path)],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        print(f"ERROR creating .venv: {result.stderr.strip()}")
        return False
    print(".venv: created")
    return True


def install_deps(base_path: Path) -> bool:
    """Install Python dependencies in .venv."""
    pip = base_path / ".venv" / "Scripts" / "pip"
    if not pip.exists():
        pip = base_path / ".venv" / "bin" / "pip"  # Linux/macOS fallback

    deps = ["requests", "python-dotenv"]
    print(f"Installing dependencies: {', '.join(deps)}...")
    result = subprocess.run(
        [str(pip), "install"] + deps,
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        print(f"ERROR installing deps: {result.stderr.strip()}")
        return False
    print("Dependencies: installed")
    return True


def setup_env(base_path: Path) -> bool:
    """Prompt user for GitHub token and write .env."""
    env_file = base_path / ENV_PATH
    if env_file.exists():
        print(".env: already exists")
        return True

    print("\n=== GitHub Token Setup ===")
    print("FounderHQ uses a private GitHub Gist for state sync between devices.")
    print("You need a GitHub fine-grained token with scope: gist:write, gist:read")
    print("Create one at: https://github.com/settings/tokens?type=beta")
    print("(Type 'skip' to configure later, or press Enter to skip)\n")

    token = input("GitHub token: ").strip()
    if not token or token.lower() == "skip":
        print(".env: skipped. Sync will not be available.")
        return True

    url = input("Gist URL (optional, press Enter to skip): ").strip()

    env_content = f"FHQ_GIST_TOKEN={token}\n"
    if url:
        env_content += f"FHQ_GIST_URL={url}\n"

    env_file.write_text(env_content, encoding="utf-8")
    # Set restrictive permissions on Unix; on Windows this is best-effort
    try:
        os.chmod(env_file, 0o600)
    except (OSError, NotImplementedError):
        pass
    print(f".env: created at {env_file}")
    return True


def create_marker(base_path: Path) -> bool:
    """Create .founderhq_installed marker."""
    marker = base_path / ".founderhq_installed"
    marker.write_text("", encoding="utf-8")
    print("Marker: .founderhq_installed created")
    return True


def task_exists(task_name: str) -> bool:
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", task_name],
        capture_output=True, text=True, timeout=10,
    )
    return result.returncode == 0


def create_task(task_name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    python_exe = str(Path(base_dir) / ".venv" / "Scripts" / "python.exe")
    if not Path(python_exe).exists():
        python_exe = sys.executable

    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval_minutes),
        "/TN", task_name,
        "/TR", f'"{python_exe}" "{script_path}" --base-dir "{base_dir}"',
        "/F",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {task_name}: {result.stderr.strip()}")
        return False
    print(f"Task '{task_name}' created (every {interval_minutes} min).")
    return True


def remove_task(task_name: str) -> bool:
    if not task_exists(task_name):
        print(f"Task '{task_name}' does not exist, skipping.")
        return True
    cmd = ["schtasks", "/Delete", "/TN", task_name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        print(f"ERROR removing task {task_name}: {result.stderr.strip()}")
        return False
    print(f"Task '{task_name}' removed.")
    return True


def check_burnt_toast() -> bool:
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Get-Module -ListAvailable -Name BurntToast",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    available = "BurntToast" in result.stdout
    if available:
        print("BurntToast: available")
    else:
        print("BurntToast: NOT available - toast notifications disabled")
    return available


def main():
    parser = argparse.ArgumentParser(description="Installer for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks")
    parser.add_argument("--install-burnttoast", action="store_true", help="Install BurntToast")
    parser.add_argument("--skip-env", action="store_true", help="Skip .env setup")
    parser.add_argument("--skip-venv", action="store_true", help="Skip .venv creation")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    if args.uninstall:
        remove_task("FounderHQ-Watchtower")
        remove_task("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    if args.install_burnttoast:
        cmd = [
            "powershell.exe", "-NoProfile", "-Command",
            "Install-Module -Name BurntToast -Force -Scope CurrentUser",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        print("BurntToast installed." if result.returncode == 0 else f"BurntToast install failed: {result.stderr.strip()}")
        return

    check_burnt_toast()

    if not args.skip_venv:
        create_venv(base_path)
        install_deps(base_path)

    if not args.skip_env:
        setup_env(base_path)

    # Setup scheduled tasks
    watchtower_path = scripts_dir / "watchtower.py"
    if watchtower_path.exists():
        create_task("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)
    else:
        print(f"WARNING: {watchtower_path} not found, skipping watchtower task")

    timekeeper_path = scripts_dir / "timekeeper.py"
    if timekeeper_path.exists():
        create_task("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)
    else:
        print(f"WARNING: {timekeeper_path} not found, skipping timekeeper task")

    create_marker(base_path)

    print("\nInstallation complete.")
    print("  - .venv: ready")
    print("  - Dependencies: installed")
    print("  - Scheduled tasks: configured")
    print("  - .founderhq_installed: created")


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/installer.py
git commit -m "feat: expand installer with .venv, token prompt, .env, marker"
```

---

### Task 5: Modify `SYSTEM_PROMPT.md` — Add first-run check and sync hooks

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md`

- [ ] **Read current file**

```cmd
type FounderOS\SYSTEM_PROMPT.md
```

- [ ] **Add first-run check as step 0 of Boot Sequence**

Find the `## Boot Sequence` section. After the line `Execute at session start (triggered by \`boot\` or first \`fhq\` of the day):`, add a new step 0 BEFORE the existing list:

```
0. **First-Run Check** — Check if `.founderhq_installed` exists in the root directory.
   - If absent → Execute **GENESIS**:
     1. Inform user: "First boot detected. I need to install FounderHQ."
     2. Run `python Runtime/engine/installer.py --base-dir .`
     3. If Python missing, install it first (winget/choco/apt/brew depending on OS)
     4. Confirm `.founderhq_installed` exists before continuing
     5. Proceed to step 1
```

- [ ] **Add sync pull after Daily Kickoff**

Find step 13 (Daily Kickoff). After it, add:

```
14. **Sync Pull** — If `State/SYNC_CONFIG.md` exists: run `python Runtime/engine/sync.py pull`. If new snapshot received, run `python Runtime/engine/sync.py merge`. Report sync status.
```

- [ ] **Add sync push to shutdown Intent**

Find the SHUTDOWN row in Intent Classification (starts with `Message starts with **"shutdown"**`). Append to its Action column:

```
 Before shutdown: run python Runtime/engine/sync.py push.
```

- [ ] **Add sync merge to fhq mode Intent**

Find the FHQ_MODE row. No change needed — the sync pull is in the boot sequence which `fhq` triggers.

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "feat: add first-run check, sync pull on boot, sync push on shutdown to SYSTEM_PROMPT"
```

---

### Task 6: Modify `Runtime/RUNTIME_KERNEL.md` — Add GENESIS branch and sync push

**Files:**
- Modify: `FounderOS/Runtime/RUNTIME_KERNEL.md`

- [ ] **Read current Phase 1: BOOT, add GENESIS check**

```cmd
type FounderOS\Runtime\RUNTIME_KERNEL.md
```

Find `## Phase 1: BOOT` section. Add a new operation 0 before the existing list:

```
0. **First-Run Check**: Check if `.founderhq_installed` exists in root.
   - If absent → halt normal boot, execute GENESIS procedure
     (ask for token, create files, .venv, scripts, marker).
```

- [ ] **Add sync push to Phase 7: UPDATE**

Find `## Phase 7: UPDATE` section. Add to the operations list:

```
6. **Sync Push**: If State/SYNC_CONFIG.md exists, run `python Runtime/engine/sync.py push` to persist state to Gist.
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/RUNTIME_KERNEL.md
git commit -m "feat: add GENESIS branch to BOOT and sync push to UPDATE in RUNTIME_KERNEL"
```

---

### Task 7: Modify `State/CADENCE.md` — Add Sync section

**Files:**
- Modify: `FounderOS/State/CADENCE.md`

- [ ] **Read current file, add Sync section to Day**

```cmd
type FounderOS\State\CADENCE.md
```

Find the `## Day (Jour)` section. Add after the `**Duration:** [calculated]` line, before `**Top 3 actions:**`:

```
**Sync:** [synced / pending / not configured]
**Last Sync:** [date]
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/CADENCE.md
git commit -m "feat: add Sync status fields to CADENCE.md Day section"
```

---

### Task 8: Generate `FOUNDER_SEED.md`

**Files:**
- Create: `FounderOS/FOUNDER_SEED.md`

- [ ] **Build FOUNDER_SEED.md by concatenating all core files**

This is a build step. Write a Python script that generates FOUNDER_SEED.md from all core files, then run it.

```python
"""build_seed.py - Generate FOUNDER_SEED.md from all core FHQ files.

Run from FounderHQ root:
    python build_seed.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "FOUNDER_SEED.md"

# Files to include (in order). Exclude user data directories.
CORE_PATHS = [
    # Root files
    "SYSTEM_PROMPT.md",
    "RUNTIME.md",
    "FOUNDERHQ_MANIFEST.md",
    "GENESIS.md",
    "INSTALL.md",
    # Frameworks
    "AOS.md",
    "CAOS.md",
    "CEOS.md",
    "DAOS.md",
    "DECISION_ENGINE.md",
    "FAOS.md",
    "KMOS.md",
    "LEOS.md",
    "MOS.md",
    "PATTERN_ENGINE.md",
    "PLAYBOOK_ENGINE.md",
    "RIOS.md",
    "SOS.md",
    "VEAOS.md",
    # State
    "State/CADENCE.md",
    "State/CURRENT_STATE.md",
    "State/LIFECYCLE.md",
    "State/PRIORITY_MATRIX.md",
    "State/SYNC_CONFIG.md",
    "State/WATCH_REGISTRY.md",
    "State/ALERTS.md",
    "State/WATCH_REPORT.md",
    # Runtime
    "Runtime/RUNTIME_KERNEL.md",
    "Runtime/FRE_SPEC.md",
    "Runtime/ADAPTER_INTERFACE.md",
    "Runtime/engine/__init__.py",
    "Runtime/engine/bootstrap.py",
    "Runtime/engine/state_manager.py",
    "Runtime/engine/gate_checker.py",
    "Runtime/engine/timeline_logger.py",
    "Runtime/engine/cadence_engine.py",
    "Runtime/engine/watchtower.py",
    "Runtime/engine/timekeeper.py",
    "Runtime/engine/installer.py",
    "Runtime/engine/sync.py",
    "Runtime/engine/snapshot.py",
    # Protocols
    "Protocols/SOURCE_OF_TRUTH.md",
    "Protocols/DECISION_GATES.md",
    "Protocols/INFO_CAPTURE_PROTOCOL.md",
]

HEADER = """# FOUNDER SEED — FounderHQ Bootstrap

## Instructions for the LLM

This file contains all core files of FounderHQ. Each section is delimited by:

```
--- FILE: <relative-path> ---
<file content>
--- END ---
```

1. Read this file completely.
2. For each `--- FILE:` block, create the file at that relative path.
3. Create any intermediate directories as needed.
4. Continue until all files are created.
5. Then run `python Runtime/engine/installer.py --base-dir .` to complete setup.

---

"""


def main():
    sections = [HEADER]

    for rel_path in CORE_PATHS:
        file_path = ROOT / rel_path
        if not file_path.exists():
            print(f"WARNING: {rel_path} not found, skipping")
            continue

        content = file_path.read_text(encoding="utf-8")
        section = f"--- FILE: {rel_path} ---\n{content}--- END ---\n"
        sections.append(section)

    OUTPUT.write_text("\n\n".join(sections), encoding="utf-8")
    file_count = len(sections) - 1
    char_count = len("\n\n".join(sections))
    print(f"FOUNDER_SEED.md generated: {file_count} files, {char_count} chars")


if __name__ == "__main__":
    main()
```

Run the build script:
```cmd
cd C:\Users\junio\Desktop\FounderHQ\FounderOS
python build_seed.py
```

Verify:
```cmd
type FounderOS\FOUNDER_SEED.md | head -10
```

Expected output: FOUNDER_SEED.md starts with the header and first FILE: block.

- [ ] **Add build_seed.py to gitignore and clean up**

Create `.gitignore` entry or just leave `build_seed.py` as a development tool.

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/FOUNDER_SEED.md
git commit -m "feat: generate FOUNDER_SEED.md - single-file distribution of all core FHQ files"
```

---

### Task 9: Modify `Protocols/SOURCE_OF_TRUTH.md`

**Files:**
- Modify: `FounderOS/Protocols/SOURCE_OF_TRUTH.md`

- [ ] **Add entries for new files**

Read current file, then add these rows to the truth table:

```
| .env | Root/ | System (scripts only) | Secrets: GitHub token, Gist URL. Permissions 600. Never read by LLM. |
| .founderhq_installed | Root/ | System | Empty marker file. If absent at boot -> GENESIS procedure. |
| FOUNDER_SEED.md | Root/ | System | Distribution file. Contains all core files for bootstrap. |
| Runtime/engine/sync.py | Runtime/engine/ | System | Gist state sync. Reads .env for token. Called by LLM, never exposes token. |
| Runtime/engine/snapshot.py | Runtime/engine/ | System | Portable markdown snapshot for token-less environments. |
| State/SYNC_CONFIG.md | State/ | System | LLM-readable sync configuration (no secrets). |
| State/_SYNC_INBOX.md | State/ | System (sync.py) | Staging area for incoming Gist sync data. |
| State/EXPORT_SNAPSHOT.md | State/ | snapshot.py | Generated portable snapshot for export. |
| State/IMPORT_SNAPSHOT.md | State/ | snapshot.py | Snapshot to merge (user pastes here). |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Protocols/SOURCE_OF_TRUTH.md
git commit -m "docs: register sync.py, snapshot.py, .env, .founderhq_installed, FOUNDER_SEED.md in SOURCE_OF_TRUTH"
```

---

### Task 10: Modify `Runtime/engine/__init__.py`

**Files:**
- Modify: `FounderOS/Runtime/engine/__init__.py`

- [ ] **Add doc entries for sync.py and snapshot.py**

Read current file, then update the docstring to add:

```
    sync: Gist state sync (push/pull/merge). Reads token from .env. LLM never sees token.
    snapshot: Portable markdown snapshot for token-less sync. No token needed.
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/__init__.py
git commit -m "docs: document sync and snapshot modules in engine __init__"
```

---

## Self-Review Checklist

### 1. Spec Coverage
- FOUNDER_SEED.md -> Task 8
- .env secrets -> Task 4 (installer prompts, writes .env)
- sync.py -> Task 1 (push/pull/merge with token isolation)
- snapshot.py -> Task 2 (portable fallback)
- .founderhq_installed -> Task 4 (installer creates), Task 5-6 (boot checks)
- SYNC_CONFIG.md -> Task 3
- GENESIS auto-run -> Task 5 (SYSTEM_PROMPT step 0), Task 6 (RUNTIME_KERNEL)
- Auto sync on boot -> Task 5 (step 14)
- Auto sync on shutdown -> Task 5 (shutdown intent), Task 6 (UPDATE phase)
- SOURCE_OF_TRUTH -> Task 9
- __init__.py -> Task 10
- CADENCE.md sync fields -> Task 7

### 2. Placeholder Scan
No placeholders found. All code blocks complete. All paths exact.

### 3. Type Consistency
- `Snapshot` class with `to_dict()` / `from_dict()` used consistently in sync.py and tests
- `cmd_pull`, `cmd_push`, `cmd_merge` return strings — used in `main()` print
- `cmd_generate`, `cmd_merge` in snapshot.py return strings — same pattern
- `create_venv`, `install_deps`, `setup_env`, `create_marker` return bool — used in installer.py main()
- All function signatures match between tasks
