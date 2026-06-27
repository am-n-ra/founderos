"""timekeeper.py - Scheduled time and alert script. Run every 30min via Windows Task Scheduler.

Checks:
1. Deadlines in PRIORITY_MATRIX.md - alerts for any deadline <= 48h
2. SOS timer - checks CADENCE.md for session start timestamp, alerts if session > 90min
3. ALERTS.md - appends any triggered alerts

Usage:
    python Runtime/engine/timekeeper.py --base-dir /path/to/FounderHQ
"""

import argparse
import importlib.util
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

_this_dir = Path(__file__).resolve().parent
_workspace_root = _this_dir.parent.parent


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
            deadline = datetime.now(timezone.utc).date()
        elif deadline_str.lower() == "tomorrow":
            deadline = datetime.now(timezone.utc).date() + timedelta(days=1)
        else:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            except ValueError:
                continue

        if deadline is not None:
            days_until = (deadline - datetime.now(timezone.utc).date()).days
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
    match = re.search(r"\*\*Session start:\*\*\s*([\d:]+)", text)
    if not match:
        return None

    session_start_str = match.group(1)
    try:
        now = datetime.now(timezone.utc)
        session_start = datetime.strptime(session_start_str, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day, tzinfo=timezone.utc
        )
        if session_start > now:
            session_start -= timedelta(days=1)
    except ValueError:
        return None

    elapsed_minutes = (now - session_start).total_seconds() / 60
    if elapsed_minutes > 90:
        return f"Session active depuis {elapsed_minutes:.0f} min. Pause recommandée (SOS)."

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

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC+0")
    entry = f"| {now_str} | timekeeper | {severity} | {message} |\n"

    with open(alerts_path, "a", encoding="utf-8") as f:
        f.write(entry)


def write_heartbeat(base_path: Path, task_name: str, interval_minutes: int) -> None:
    hb_path = base_path / "State" / "_HEARTBEAT.md"
    now_utc = datetime.now(timezone.utc)
    now_str = now_utc.strftime("%Y-%m-%d %H:%M")
    next_str = (now_utc + timedelta(minutes=interval_minutes)).strftime("%Y-%m-%d %H:%M")
    if not hb_path.exists():
        hb_path.write_text(
            "# HEARTBEAT\n\n"
            "| Task | Last Run (UTC) | Status | Next Expected (UTC) |\n"
            "|------|---------------|--------|---------------------|\n",
            encoding="utf-8",
        )
    lines = hb_path.read_text(encoding="utf-8").splitlines()
    new_lines = []
    found = False
    for line in lines:
        if line.startswith(f"| {task_name} |"):
            new_lines.append(f"| {task_name} | {now_str} | OK | {next_str} |")
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f"| {task_name} | {now_str} | OK | {next_str} |")
    hb_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def check_watchtower_heartbeat(base_path: Path) -> None:
    hb_path = base_path / "State" / "_HEARTBEAT.md"
    if not hb_path.exists():
        append_alert(base_path, "HIGH", "No heartbeat file found - watchtower may not be running")
        return
    text = hb_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("| FounderHQ-Watchtower |"):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 4:
                last_str = parts[1]
                status = parts[2]
                try:
                    last_dt = datetime.strptime(last_str, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
                    elapsed = (datetime.now(timezone.utc) - last_dt).total_seconds() / 3600
                    if status != "OK":
                        append_alert(base_path, "HIGH", f"Watchtower status: {status} (last run {last_str})")
                    elif elapsed > 7:
                        append_alert(base_path, "HIGH", f"Watchtower heartbeat stale - {elapsed:.0f}h since last run")
                except ValueError:
                    pass
            return


def main():
    parser = argparse.ArgumentParser(description="Timekeeper - time and alert script for FounderHQ")
    parser.add_argument("--base-dir", default=str(_workspace_root), help="FounderOS root directory")
    parser.add_argument("--no-toast", action="store_true", help="Skip toast notifications")
    parser.add_argument("--astra", action="store_true", help="Run ASTRA daily update")
    args = parser.parse_args()

    base_path = Path(args.base_dir)

    if args.astra:
        astra_daily_path = _workspace_root / "Runtime" / "engine" / "astra_daily.py"
        if not astra_daily_path.exists():
            msg = "astra_daily.py not found"
            print(f"[ASTRA] {msg}")
            append_alert(base_path, "HIGH", msg)
        else:
            daily_state = base_path / "State" / "ASTRA_DAILY.md"
            today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            if daily_state.exists() and today_str in daily_state.read_text(encoding="utf-8"):
                print(f"[ASTRA] Daily already up to date ({today_str}), skipping.")
            else:
                try:
                    spec = importlib.util.spec_from_file_location("astra_daily", astra_daily_path)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    mod.main()
                    print(f"[ASTRA] Daily update complete ({today_str}).")
                except Exception as e:
                    msg = f"Astra daily failed: {e}"
                    print(f"[ASTRA] Error: {msg}")
                    append_alert(base_path, "HIGH", msg)

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

    check_watchtower_heartbeat(base_path)
    write_heartbeat(base_path, "FounderHQ-Timekeeper", interval_minutes=30)

    print("Timekeeper run complete.")


if __name__ == "__main__":
    main()
