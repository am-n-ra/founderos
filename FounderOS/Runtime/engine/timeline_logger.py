"""Appends structured events to TIMELINE.md.

Usage:
    from engine.timeline_logger import TimelineLogger
    logger = TimelineLogger("/path/to/founderhq")
    logger.log_event("Sent proposal to client", "Approved", "Awaiting response")
"""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional


class TimelineLogger:
    """Appends timestamped events to TIMELINE.md."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    def _timeline_path(self) -> Path:
        return self.base_dir / "concepts" / "TIMELINE.md"

    def _ensure_exists(self):
        """Create TIMELINE.md with header if it doesn't exist."""
        path = self._timeline_path()
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "# TIMELINE\n\n"
                "| Date | Event | Decision | Outcome |\n"
                "|------|-------|----------|---------|\n",
                encoding="utf-8",
            )

    def log_event(
        self,
        event: str,
        decision: str,
        outcome: str = "",
        date_str: Optional[str] = None,
    ) -> bool:
        """Append an event to TIMELINE.md.

        Args:
            event: What happened.
            decision: What was decided.
            outcome: What resulted (optional).
            date_str: Custom date (default: current UTC time).

        Returns:
            True if written successfully.
        """
        self._ensure_exists()

        if date_str is None:
            date_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

        entry = f"| {date_str} | {event} | {decision} | {outcome} |\n"

        path = self._timeline_path()
        with path.open("a", encoding="utf-8") as f:
            f.write(entry)
        return True
