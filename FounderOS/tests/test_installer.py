import subprocess
import sys
import tempfile
from pathlib import Path


def test_installer_reports_scheduler_accuracy():
    """Installer must report whether scheduler tasks were actually created."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        (tmp_path / "Runtime" / "engine").mkdir(parents=True)
        (tmp_path / "Runtime" / "engine" / "watchtower.py").write_text("")
        (tmp_path / "Runtime" / "engine" / "timekeeper.py").write_text("")

        result = subprocess.run(
            [sys.executable, "-m", "Runtime.engine.installer",
             "--base-dir", str(tmp_path),
             "--skip-venv", "--skip-env"],
            capture_output=True, text=True, timeout=30,
            cwd=Path(__file__).resolve().parent.parent,
        )
        assert result.returncode == 0
        assert "Watchtower scheduler:" in result.stdout
        assert "Timekeeper scheduler:" in result.stdout
        assert "Scheduler: configured" not in result.stdout
