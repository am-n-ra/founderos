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
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
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


def cmd_pull(env: dict) -> str:
    url = env.get("FHQ_GIST_URL", "")
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
            if fname.endswith(".json") or "snapshot" in fname:
                snap_file = finfo
                break
        if not snap_file:
            snap_file = list(files.values())[0]
        content = snap_file.get("content", "")
        if not content:
            return "ERROR: Empty snapshot file"
        inbox_path = STATE_DIR / "_SYNC_INBOX.md"
        inbox_path.write_text(
            f"# SYNC INBOX\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n```json\n{content}\n```\n",
            encoding="utf-8",
        )
        return f"OK: Snapshot pulled ({len(content)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_push(env: dict) -> str:
    url = env.get("FHQ_GIST_URL", "")
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
