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

    recent_events = []
    for line in tl.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] not in ("Date", ""):
                recent_events.append(f"- {cols[0]}: {cols[1]} -> {cols[3]}")

    recent_events = recent_events[-5:]

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
        return "ERROR: No State/IMPORT_SNAPSHOT.md found."

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
