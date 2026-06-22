"""timekeeper.py - Scheduled time and alert script. Run every 30min via Windows Task Scheduler.

Checks:
1. Deadlines in PRIORITY_MATRIX.md - alerts for any deadline <= 48h
2. SOS timer - checks CADENCE.md for session start timestamp, alerts if session > 90min
3. ALERTS.md - appends any triggered alerts

Usage:
    python Runtime/engine/timekeeper.py --base-dir /path/to/FounderHQ
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


def send_toast(title: str, message: str) -> bool:
    """Send Windows toast notification using BurntToast PowerShell module.

    Returns True if sent, False if BurntToast not available.
    """
    ps_script = (
        f'New-BurntToastNotification -Text "{title}", "{message}"'
    )
    try:
        result = subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=15,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def parse_deadlines(base_path: Path) -> list[dict]:
    """Parse PRIORITY_MATRIX.md for rows with deadlines within 48h."""
    matrix_path = base_path / "State" / "PRIORITY_MATRIX.md"
    if not matrix_path.exists():
        return []

    text = matrix_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    deadlines = []
    in_table = False

    for line in lines:
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            in_table = False
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 6:
            continue

        project = cols[0]
        deadline_str = cols[4]
        if not deadline_str or deadline_str == "-":
            continue

        deadline = None
        if deadline_str.lower() == "today":
            deadline = datetime.now().date()
        elif deadline_str.lower() == "tomorrow":
            deadline = datetime.now().date() + timedelta(days=1)
        else:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            except ValueError:
                continue

        if deadline is not None:
            days_until = (deadline - datetime.now().date()).days
            if 0 <= days_until <= 2:
                deadlines.append({
                    "project": project,
                    "deadline": deadline_str,
                    "days_until": days_until,
                    "action": cols[2],
                })

    return deadlines


def check_sos_timer(base_path: Path) -> Optional[str]:
    """Check SOS timer. If session > 90min, return alert message.

    Reads Session start timestamp from CADENCE.md Day section.
    """
    cadence_path = base_path / "State" / "CADENCE.md"
    if not cadence_path.exists():
        return None

    text = cadence_path.read_text(encoding="utf-8")
    match = re.search(r"\*\*Session start:\*\*\s*([\d:]+)", text, re.IGNORECASE)
    if not match:
        return None

    session_start_str = match.group(1)
    try:
        now = datetime.now()
        session_start = datetime.strptime(session_start_str, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
    except ValueError:
        return None

    elapsed_minutes = (now - session_start).total_seconds() / 60
    if elapsed_minutes > 90:
        return f"Session active depuis {elapsed_minutes:.0f} min. Pause recommandee (SOS)."

    return None


def append_alert(base_path: Path, severity: str, message: str) -> None:
    """Append alert to ALERTS.md."""
    alerts_path = base_path / "State" / "ALERTS.md"
    if not alerts_path.exists():
        alerts_path.write_text(
            "# ALERTS\n\n## Active Alerts\n\n"
            "| Timestamp | Source | Severity | Message |\n"
            "|-----------|--------|----------|---------|\n",
            encoding="utf-8",
        )

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M UTC+0")
    entry = f"| {now_str} | timekeeper | {severity} | {message} |\n"

    with open(alerts_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Timekeeper - time and alert script for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--no-toast", action="store_true", help="Skip toast notifications")
    args = parser.parse_args()

    base_path = Path(args.base_dir)

    deadlines = parse_deadlines(base_path)
    for d in deadlines:
        msg = f"{d['project']}: deadline {d['deadline']} dans {d['days_until']} jour(s)"
        print(f"[ALERT] {msg}")
        append_alert(base_path, "HIGH", msg)
        if not args.no_toast:
            sent = send_toast("FounderHQ Deadline", f"{d['project']} - {d['deadline']}")
            if sent:
                print("  Toast sent.")

    sos_msg = check_sos_timer(base_path)
    if sos_msg:
        print(f"[SOS] {sos_msg}")
        append_alert(base_path, "MEDIUM", sos_msg)
        if not args.no_toast:
            sent = send_toast("FounderHQ SOS", "Pause recommandee - session > 90 min")
            if sent:
                print("  Toast sent.")

    print("Timekeeper run complete.")


if __name__ == "__main__":
    main()
