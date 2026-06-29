"""Validates LLM responses against FRE_SPEC PRG contracts.

Checks datetime format, stale concepts, response structure.
Returns PASS/FAIL for each gate.

Usage:
    from engine.gate_checker import GateChecker
    checker = GateChecker("/path/to/founderhq")
    results = checker.check_all(response_text)
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional


class GateChecker:
    """Validates LLM responses against PRG (Pre-Response Gate) contracts."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    def _read_file(self, *parts: str) -> Optional[str]:
        path = self.base_dir.joinpath(*parts)
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8")

    def check_temporal(self, response: str) -> tuple[bool, str]:
        """Gate 1: Verify response starts with a valid datetime.

        Expected format: **[YYYY-MM-DD HH:MM Lomé UTC+0]**
        """
        if not response:
            return False, "Empty response"

        first_line = response.strip().split("\n")[0]
        pattern = r"^\*\*\[\d{4}-\d{2}-\d{2} \d{2}:\d{2} Lomé UTC\+0\]\*\*"
        if re.match(pattern, first_line):
            return True, "Datetime header present and valid"
        return False, f"Missing or invalid datetime header. Got: '{first_line[:60]}'"

    def check_concept_freshness(self, max_age_hours: int = 48) -> list[str]:
        """Gate 5: Find concepts that haven't been updated within max_age_hours.

        Checks footers of concept files for 'Last Updated' or 'Last Verified' timestamps.
        """
        stale_files = []
        concept_dir = self.base_dir / "concepts"
        if not concept_dir.exists():
            return ["concepts/ directory not found"]

        now = datetime.utcnow()

        for f in sorted(concept_dir.iterdir()):
            if f.suffix != ".md" or not f.is_file():
                continue
            text = f.read_text(encoding="utf-8")

            # Look for Last Updated or Last Verified in footer
            ts_match = re.search(
                r"(?:Last\s+Updated|Last\s+Verified)[^\d]*(\d{4}-\d{2}-\d{2})",
                text,
            )
            if not ts_match:
                stale_files.append(f"{f.name}: no timestamp found")
                continue

            date_str = ts_match.group(1)
            try:
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                age_hours = (now - file_date).total_seconds() / 3600
                if age_hours > max_age_hours:
                    stale_files.append(
                        f"{f.name}: {age_hours:.0f}h old "
                        f"(max {max_age_hours}h)"
                    )
            except ValueError:
                stale_files.append(f"{f.name}: unparseable date '{date_str}'")

        return stale_files

    def check_projects_cascade(self) -> list[str]:
        """Gate 4: Verify active projects have strategic cascade files.

        Checks projects/<PROJECT>/ for 01_VISION.md through 10_PITCH_DECK.md + annexes/.
        """
        missing = []
        projects_dir = self.base_dir / "projects"
        if not projects_dir.exists():
            return ["projects/ directory not found"]

        required = [
            "01_VISION.md",
            "02_MISSION.md",
            "03_THEORY_OF_CHANGE.md",
            "04_STRATEGIC_ASSETS_MAP.md",
            "05_MASTER_PLAN.md",
            "06_STRATEGIC_ROADMAP.md",
            "07_CAPITAL_ROADMAP.md",
            "08_EXECUTIVE_SUMMARY.md",
            "09_BUSINESS_PLAN.md",
            "10_PITCH_DECK.md",
        ]

        for proj_dir in sorted(projects_dir.iterdir()):
            if not proj_dir.is_dir():
                continue
            proj_missing = []
            for req in required:
                if not (proj_dir / req).exists():
                    proj_missing.append(req)
            if proj_missing:
                missing.append(
                    f"{proj_dir.name}: missing {', '.join(proj_missing)}"
                )

        return missing

    def check_all(self, response: str) -> dict:
        """Run all applicable checks and return results."""
        results = {}

        # Gate 1: Temporal
        temporal_ok, temporal_msg = self.check_temporal(response)
        results["gate_1_temporal"] = {
            "status": "PASS" if temporal_ok else "FAIL",
            "message": temporal_msg,
        }

        # Gate 5: Freshness
        stale = self.check_concept_freshness()
        results["gate_5_freshness"] = {
            "status": "PASS" if not stale else "FLAG",
            "message": f"{len(stale)} stale concept(s)" if stale else "All fresh",
            "stale_files": stale,
        }

        # Gate 4: Project Data Room (informational)
        missing_cascade = self.check_projects_cascade()
        results["gate_4_project_scan"] = {
            "status": "PASS" if not missing_cascade else "FLAG",
            "message": (
                f"{len(missing_cascade)} project(s) incomplete"
                if missing_cascade
                else "All complete"
            ),
            "details": missing_cascade,
        }

        return results

    def report(self, response: str) -> str:
        """Return a formatted gate check report."""
        results = self.check_all(response)
        lines = ["## PRG Gate Check Report", ""]

        for gate, data in results.items():
            status = data["status"]
            icon = {"PASS": "✅", "FAIL": "❌", "FLAG": "⚠️"}.get(status, "❓")
            lines.append(f"{icon} {gate}: {data['message']}")

        return "\n".join(lines)
