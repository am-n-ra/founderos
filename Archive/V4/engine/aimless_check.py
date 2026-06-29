"""
Aimless state detection. Checks idle time, plan completeness, turn loops.
Returns verdict with recommended action.

Usage:
    from aimless_check import run_check
    verdict = run_check()
"""
from datetime import datetime, timezone
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE_DIR / "State"


def _now():
    return datetime.now(timezone.utc)


def _rp(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""


def _ef(text, pattern, default=""):
    m = re.search(pattern, text)
    return m.group(1).strip() if m else default


def run_check() -> dict:
    """Run aimless detection. Returns verdict dict."""
    now = _now()
    verdict = {"aimless": False, "type": "", "recommendation": "", "idle_minutes": 0, "unchecked_items": 0}
    
    # 1. Check idle time from CADENCE.md
    cad = _rp(STATE_DIR / "CADENCE.md")
    last_fhq = _ef(cad, r"\*\*Last fhq:\*\*\s*(\S+)", "?")
    last_fhqa = _ef(cad, r"\*\*Last fhqa:\*\*\s*(\S+)", "?")
    
    def _parse_time(t):
        try:
            parts = t.split(":")
            return int(parts[0]) * 60 + int(parts[1])
        except:
            return None
    
    last_minutes = None
    for t in [last_fhqa, last_fhq]:
        m = _parse_time(t)
        if m is not None:
            last_minutes = m
            break
    
    if last_minutes is not None:
        now_minutes = now.hour * 60 + now.minute
        if now_minutes < last_minutes:
            now_minutes += 1440
        idle = now_minutes - last_minutes
        verdict["idle_minutes"] = idle
        if idle > 30:
            verdict["aimless"] = True
            verdict["type"] = "AIMLESS_IDLE"
            verdict["recommendation"] = f"Idle for {idle} minutes. Suggest next action from DAILY_PLAN or top priority."
    
    # 2. Check DAILY_PLAN for unchecked items
    plan = _rp(STATE_DIR / "DAILY_PLAN.md")
    unchecked = plan.count("- [ ]")
    checked = plan.count("- [x]")
    verdict["unchecked_items"] = unchecked
    
    if not verdict["aimless"] and unchecked > 0 and checked == 0:
        verdict["aimless"] = True
        verdict["type"] = "AIMLESS_PLAN_AVAILABLE"
        # Extract next unchecked action
        for line in plan.splitlines():
            if "- [ ]" in line:
                verdict["recommendation"] = line.strip().lstrip("- [ ]").strip()
                break
    
    # 3. Check turn loops (if session_log exists)
    try:
        from session_log import count_turns_since_last_completion
        turns = count_turns_since_last_completion()
        if turns >= 5:
            verdict["aimless"] = True
            verdict["type"] = "AIMLESS_LOOP"
            verdict["recommendation"] = f"{turns} turns without completion. Force-propose next concrete action."
    except ImportError:
        pass
    
    # 4. No plan at all
    if not STATE_DIR.exists() or not (STATE_DIR / "DAILY_PLAN.md").exists():
        verdict["aimless"] = True
        verdict["type"] = "AIMLESS_NO_PLAN"
        verdict["recommendation"] = "No daily plan found. Run kickoff to generate one."
    
    return verdict
