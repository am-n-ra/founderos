"""Reads/writes FounderHQ state files programmatically.

Provides typed access to CURRENT_STATE.md, PRIORITY_MATRIX.md, TIMELINE.md.

Usage:
    from engine.state_manager import StateManager
    sm = StateManager("/path/to/founderhq")
    cash = sm.get_cash()
    sm.set_top_priority("Find client for corn")
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional


class StateManager:
    """Manages FounderHQ state files."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    # --- CURRENT_STATE.md ---

    def _current_state_path(self) -> Path:
        return self.base_dir / "State" / "CURRENT_STATE.md"

    def get_field(self, field_name: str) -> Optional[str]:
        """Extract a field value from CURRENT_STATE.md.

        Looks for '**Field Name:** value' pattern.
        """
        path = self._current_state_path()
        if not path.exists():
            return None
        text = path.read_text(encoding="utf-8")
        # Match both **Field:** value and **Field:** multiline value
        pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.*?)(?=\n\*\*|\Z)"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    def get_cash(self) -> Optional[str]:
        """Get current cash position."""
        return self.get_field("Cash")

    def get_top_priority(self) -> Optional[str]:
        """Get current top priority."""
        return self.get_field("Top Priority")

    def get_mode(self) -> Optional[str]:
        """Get operating mode."""
        return self.get_field("Operating Mode")

    def update_field(self, field_name: str, value: str) -> bool:
        """Update a field in CURRENT_STATE.md.

        Returns True if updated, False if field not found.
        """
        path = self._current_state_path()
        if not path.exists():
            return False

        text = path.read_text(encoding="utf-8")
        pattern = rf"(\*\*{re.escape(field_name)}:\*\*).*"
        replacement = rf"\1 {value}"

        if not re.search(pattern, text):
            return False

        new_text = re.sub(pattern, replacement, text)
        path.write_text(new_text, encoding="utf-8")
        return True

    def update_last_updated(self) -> bool:
        """Set Last Updated to current datetime in Lomé UTC+0."""
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M — Lomé UTC+0")
        return self.update_field("Last Updated", now)

    # --- PRIORITY_MATRIX.md ---

    def _priority_matrix_path(self) -> Path:
        return self.base_dir / "State" / "PRIORITY_MATRIX.md"

    def add_pending_action(self, project: str, action: str) -> bool:
        """Add a pending action to PRIORITY_MATRIX.md."""
        path = self._priority_matrix_path()
        if not path.exists():
            return False

        text = path.read_text(encoding="utf-8")
        # Find the Actions Pending section
        marker = "### Actions Pending"
        if marker not in text:
            return False

        new_item = f"- [ ] **{project}** — {action}"
        # Insert after the marker line
        text = text.replace(marker, f"{marker}\n{new_item}")
        path.write_text(text, encoding="utf-8")
        return True

    # --- TIMELINE.md ---

    def _timeline_path(self) -> Path:
        return self.base_dir / "concepts" / "TIMELINE.md"

    def append_timeline(self, event: str, decision: str, outcome: str) -> bool:
        """Append an event to TIMELINE.md."""
        path = self._timeline_path()
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

        entry = f"\n| {now} | {event} | {decision} | {outcome} |"

        # Ensure the Timeline table header exists
        if not path.exists():
            path.write_text(
                "# TIMELINE\n\n"
                "| Date | Event | Decision | Outcome |\n"
                "|------|-------|----------|---------|\n",
                encoding="utf-8",
            )

        text = path.read_text(encoding="utf-8")
        text += entry
        path.write_text(text, encoding="utf-8")
        return True
