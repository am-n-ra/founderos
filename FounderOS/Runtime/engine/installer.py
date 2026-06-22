"""installer.py - First-run setup for FounderHQ background scripts.

Creates Windows Task Scheduler tasks for:
1. watchtower - runs every 6 hours
2. timekeeper - runs every 30 minutes

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ --uninstall
"""

import argparse
import subprocess
import sys
from pathlib import Path


def task_exists(task_name: str) -> bool:
    """Check if a Windows Scheduled Task exists."""
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", task_name],
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.returncode == 0


def create_task(task_name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    """Create a Windows Scheduled Task."""
    python_exe = sys.executable
    if not python_exe:
        python_exe = "python"

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
    """Remove a Windows Scheduled Task."""
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
    """Check if BurntToast PowerShell module is available."""
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


def install_burnt_toast() -> bool:
    """Install BurntToast PowerShell module."""
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Install-Module -Name BurntToast -Force -Scope CurrentUser",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"BurntToast install failed: {result.stderr.strip()}")
        return False
    print("BurntToast installed.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Installer for FounderHQ background scripts")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks")
    parser.add_argument("--install-burnttoast", action="store_true", help="Install BurntToast PowerShell module")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    if args.uninstall:
        remove_task("FounderHQ-Watchtower")
        remove_task("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    if args.install_burnttoast:
        install_burnt_toast()
        return

    check_burnt_toast()

    watchtower_path = scripts_dir / "watchtower.py"
    if not watchtower_path.exists():
        print(f"ERROR: {watchtower_path} not found")
        sys.exit(1)

    create_task("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)

    timekeeper_path = scripts_dir / "timekeeper.py"
    if not timekeeper_path.exists():
        print(f"ERROR: {timekeeper_path} not found")
        sys.exit(1)

    create_task("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)

    print("\nInstallation complete.")
    print("  FounderHQ-Watchtower: runs every 6 hours (veille)")
    print("  FounderHQ-Timekeeper: runs every 30 minutes (deadlines + SOS)")


if __name__ == "__main__":
    main()
