"""installer.py - Cross-platform first-run setup for FounderHQ.

Creates:
1. .venv Python virtual environment
2. .env file (asks user for GitHub token)
3. Installs dependencies (requests, python-dotenv)
4. Scheduler tasks for watchtower + timekeeper (schtasks / cron / launchd)
5. .founderhq_installed marker

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


IS_WINDOWS = sys.platform.startswith("win")
IS_LINUX = sys.platform.startswith("linux")
IS_MAC = sys.platform == "darwin"

ENV_PATH = ".env"


def get_platform_label() -> str:
    if IS_WINDOWS:
        return "Windows"
    if IS_LINUX:
        return "Linux"
    if IS_MAC:
        return "macOS"
    return sys.platform


def get_venv_python(base_path: Path) -> str:
    if IS_WINDOWS:
        pip = base_path / ".venv" / "Scripts" / "python.exe"
    else:
        pip = base_path / ".venv" / "bin" / "python3"
        if not pip.exists():
            pip = base_path / ".venv" / "bin" / "python"
    return str(pip) if pip.exists() else sys.executable


def get_venv_pip(base_path: Path) -> str:
    for name in ("pip.exe", "pip", "pip3"):
        if IS_WINDOWS:
            pip = base_path / ".venv" / "Scripts" / name
        else:
            pip = base_path / ".venv" / "bin" / name
        if pip.exists():
            return str(pip)
    return ""


def create_venv(base_path: Path) -> bool:
    """Create .venv if it doesn't exist."""
    venv_path = base_path / ".venv"
    marker = get_venv_python(base_path)
    if marker and Path(marker).exists():
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
    pip = get_venv_pip(base_path)
    if not pip:
        print("ERROR: pip not found in .venv")
        return False

    deps = ["requests", "python-dotenv"]
    print(f"Installing dependencies: {', '.join(deps)}...")
    result = subprocess.run(
        [pip, "install"] + deps,
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


# ── Scheduler (OS-agnostic) ──


def _remove_schtasks(name: str) -> bool:
    if not _task_exists_schtasks(name):
        return True
    cmd = ["schtasks", "/Delete", "/TN", name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    return result.returncode in (0, 1)


def _task_exists_schtasks(name: str) -> bool:
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", name],
        capture_output=True, text=True, timeout=10,
    )
    return result.returncode == 0


def _create_schtasks(name: str, script: str, base_dir: str, interval: int) -> bool:
    python_exe = get_venv_python(Path(base_dir))
    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval),
        "/TN", name,
        "/TR", f'"{python_exe}" "{script}" --base-dir "{base_dir}"',
        "/F",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {name}: {result.stderr.strip()}")
        return False
    print(f"Task '{name}' created (every {interval} min).")
    return True


def _remove_cron(name: str) -> bool:
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            return True
        lines = [l for l in result.stdout.splitlines() if name not in l]
        new_cron = "\n".join(lines) + "\n"
        proc = subprocess.run(
            ["crontab", "-"],
            input=new_cron, text=True, capture_output=True, timeout=10,
        )
        return proc.returncode == 0
    except Exception:
        return True


def _create_cron(name: str, script: str, base_dir: str, interval: int) -> bool:
    python_exe = get_venv_python(Path(base_dir))
    comment = f"# FounderHQ: {name}"
    cron_line = f"*/{interval} * * * * {python_exe} {script} --base-dir {base_dir}"
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            capture_output=True, text=True, timeout=10,
        )
        existing = result.stdout if result.returncode == 0 else ""
        if name in existing:
            print(f"Cron '{name}': already exists")
            return True
        new_cron = existing.strip() + "\n" + comment + "\n" + cron_line + "\n"
        proc = subprocess.run(
            ["crontab", "-"],
            input=new_cron, text=True, capture_output=True, timeout=10,
        )
        if proc.returncode != 0:
            print(f"ERROR creating cron '{name}': {proc.stderr.strip()}")
            return False
        print(f"Cron '{name}' created (every {interval} min).")
        return True
    except FileNotFoundError:
        print("WARNING: crontab not available, skipping scheduler")
        return False


def _remove_launchd(name: str) -> bool:
    plist = Path.home() / "Library" / "LaunchAgents" / f"{name}.plist"
    if not plist.exists():
        return True
    subprocess.run(["launchctl", "unload", str(plist)], capture_output=True, timeout=10)
    plist.unlink(missing_ok=True)
    return True


def _create_launchd(name: str, script: str, base_dir: str, interval: int) -> bool:
    python_exe = get_venv_python(Path(base_dir))
    label = f"com.founderhq.{name.lower().replace(' ', '-')}"
    plist_dir = Path.home() / "Library" / "LaunchAgents"
    plist_dir.mkdir(parents=True, exist_ok=True)
    plist_path = plist_dir / f"{label}.plist"

    start_interval = interval * 60  # launchd uses seconds
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{label}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_exe}</string>
        <string>{script}</string>
        <string>--base-dir</string>
        <string>{base_dir}</string>
    </array>
    <key>StartInterval</key>
    <integer>{start_interval}</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""
    plist_path.write_text(plist_content, encoding="utf-8")
    result = subprocess.run(
        ["launchctl", "load", str(plist_path)],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != 0:
        print(f"ERROR loading launchd job '{label}': {result.stderr.strip()}")
        return False
    print(f"Launchd job '{label}' created (every {interval} min).")
    return True


def setup_scheduler(name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    if IS_WINDOWS:
        return _create_schtasks(name, script_path, base_dir, interval_minutes)
    if IS_LINUX:
        return _create_cron(name, script_path, base_dir, interval_minutes)
    if IS_MAC:
        return _create_launchd(name, script_path, base_dir, interval_minutes)
    print(f"WARNING: Unknown platform '{sys.platform}', skipping scheduler")
    return False


def remove_scheduler(name: str) -> bool:
    if IS_WINDOWS:
        return _remove_schtasks(name)
    if IS_LINUX:
        return _remove_cron(name)
    if IS_MAC:
        return _remove_launchd(name)
    return True


# ── Notifications ──


def check_notifications() -> bool:
    if IS_WINDOWS:
        cmd = [
            "powershell.exe", "-NoProfile", "-Command",
            "Get-Module -ListAvailable -Name BurntToast",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        available = "BurntToast" in result.stdout
        if available:
            print("Notifications: BurntToast available (Windows)")
        else:
            print("Notifications: BurntToast NOT available")
        return available
    if IS_LINUX:
        result = subprocess.run(
            ["which", "notify-send"],
            capture_output=True, text=True, timeout=5,
        )
        available = result.returncode == 0
        print(f"Notifications: notify-send {'available' if available else 'NOT available'} (Linux)")
        return available
    if IS_MAC:
        print("Notifications: osascript available (macOS)")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Cross-platform installer for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks/jobs")
    parser.add_argument("--skip-env", action="store_true", help="Skip .env setup")
    parser.add_argument("--skip-venv", action="store_true", help="Skip .venv creation")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    print(f"Platform: {get_platform_label()}")

    if args.uninstall:
        remove_scheduler("FounderHQ-Watchtower")
        remove_scheduler("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    check_notifications()

    if not args.skip_venv:
        create_venv(base_path)
        install_deps(base_path)

    if not args.skip_env:
        setup_env(base_path)

    watchtower_path = scripts_dir / "watchtower.py"
    if watchtower_path.exists():
        setup_scheduler("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)
    else:
        print(f"WARNING: {watchtower_path} not found, skipping watchtower")

    timekeeper_path = scripts_dir / "timekeeper.py"
    if timekeeper_path.exists():
        setup_scheduler("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)
    else:
        print(f"WARNING: {timekeeper_path} not found, skipping timekeeper")

    create_marker(base_path)

    print("\nInstallation complete.")
    print(f"  Platform: {get_platform_label()}")
    print("  - .venv: ready")
    print("  - Dependencies: installed")
    print("  - Scheduler: configured")
    print("  - .founderhq_installed: created")


if __name__ == "__main__":
    main()
