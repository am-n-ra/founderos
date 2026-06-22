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
        pip = base_path / ".venv" / "bin" / "pip"

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
