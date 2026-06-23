import pytest
import subprocess
from pathlib import Path


def test_installer_reports_scheduler_accuracy(tmp_path: Path):
    """Installer must report whether scheduler tasks were actually created."""
    (tmp_path / "Runtime" / "engine").mkdir(parents=True)
    (tmp_path / "Runtime" / "engine" / "watchtower.py").write_text("")
    (tmp_path / "Runtime" / "engine" / "timekeeper.py").write_text("")

    result = subprocess.run(
        ["python", "-m", "Runtime.engine.installer",
         "--base-dir", str(tmp_path),
         "--skip-venv", "--skip-env"],
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0
    assert "watchtower" in result.stdout.lower()
    assert "timekeeper" in result.stdout.lower()
    assert "Scheduler: configured" not in result.stdout
