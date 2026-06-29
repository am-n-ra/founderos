"""
Session conversation journal. Records every interaction turn during a session.
Auto-pruned at session end (significant entries → TIMELINE.md, rest discarded).

Usage:
    from session_log import log_turn, init_session, prune_session, count_turns_since_last_completion
"""
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE_DIR / "State"
CONCEPTS_DIR = BASE_DIR / "concepts"
LOG_PATH = STATE_DIR / "_SESSION_LOG.md"


def _now_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M Lome UTC+0")


def init_session():
    """Create fresh _SESSION_LOG.md with header."""
    LOG_PATH.write_text(
        f"# SESSION LOG — {_now_str()}\n\n"
        f"| Timestamp | User | Action | Outcome |\n"
        f"|-----------|------|--------|---------|\n",
        encoding="utf-8"
    )


def log_turn(user_message: str = "", system_action: str = "", outcome: str = ""):
    """Append one interaction turn to the session log."""
    if not LOG_PATH.exists():
        init_session()
    msg = user_message.strip().replace("\n", " ")[:80] if user_message else "(auto)"
    action = system_action.strip()[:80] if system_action else "(cycle)"
    outcome_str = outcome.strip()[:60] if outcome else ""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    line = f"| {timestamp} | {msg} | {action} | {outcome_str} |\n"
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line)


def prune_session():
    """Move significant entries to TIMELINE.md, delete log."""
    if not LOG_PATH.exists():
        return
    text = LOG_PATH.read_text(encoding="utf-8", errors="replace")
    significant = []
    for line in text.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4:
                action = cols[2].lower()
                outcome = cols[3].lower()
                if any(kw in action or kw in outcome for kw in ["completed", "decid", "launch", "deploy", "sign", "commit", "push", "merge", "change", "creat", "✅"]):
                    significant.append(cols)
    if significant:
        tl_path = CONCEPTS_DIR / "TIMELINE.md"
        if tl_path.exists():
            tl_text = tl_path.read_text(encoding="utf-8")
            for cols in significant:
                event = cols[2][:60]
                decision = cols[3][:60] if len(cols) > 3 else ""
                row = f"\n| {cols[0]} | Session event: {event} | {decision} | Automated |"
                if row not in tl_text:
                    tl_text += row
            tl_path.write_text(tl_text, encoding="utf-8")
    LOG_PATH.unlink(missing_ok=True)


def count_turns_since_last_completion() -> int:
    """Count log entries since last completed action."""
    if not LOG_PATH.exists():
        return 0
    text = LOG_PATH.read_text(encoding="utf-8", errors="replace")
    lines = [l for l in text.splitlines() if l.startswith("| ") and "|" in l[2:]]
    count = 0
    for line in reversed(lines):
        if "✅" in line or "completed" in line.lower() or "done" in line.lower():
            return count
        count += 1
    return count
