"""
Diagnosis engine for FounderOS.
Reads state, detects critical issues, prescribes action.
Output: _DIAGNOSIS.md consumed by LLM to auto-trigger subagent loops.

Usage:
    from diagnose import run_diagnosis
    dx = run_diagnosis()
"""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE_DIR / "State"
CONCEPTS_DIR = BASE_DIR / "concepts"
PROJECTS_DIR = BASE_DIR / "projects"


def rp(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""


def ef(text, pattern, default=""):
    m = re.search(pattern, text)
    return m.group(1).strip() if m else default


def ef_all(text, pattern):
    return re.findall(pattern, text)


def now_lome():
    return datetime.now(timezone.utc)


def file_age_h(path):
    if not path.exists():
        return 999
    mt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return (datetime.now(timezone.utc) - mt).total_seconds() / 3600


def parse_time_hhmm(t):
    try:
        parts = t.strip().split(":")
        return int(parts[0]) * 60 + int(parts[1])
    except (ValueError, IndexError):
        return None


def run_diagnosis() -> dict:
    now = now_lome()
    now_minutes = now.hour * 60 + now.minute

    cs = rp(STATE_DIR / "CURRENT_STATE.md")
    co = rp(STATE_DIR / "_CYCLE_OUTPUT.md")
    plan = rp(STATE_DIR / "DAILY_PLAN.md")
    prio = rp(STATE_DIR / "PRIORITY_MATRIX.md")
    wr = rp(STATE_DIR / "WATCH_REPORT.md")
    reg = rp(STATE_DIR / "WATCH_REGISTRY.md")
    al = rp(STATE_DIR / "ALERTS.md")
    cad = rp(STATE_DIR / "CADENCE.md")

    om = ef(cs, r"\*\*Operating Mode:\*\*\s*(\S+)", "SURVIVAL")
    cash_raw = ef(cs, r"\*\*Cash.*:\*\*\s*(.+)", "?")
    tp = ef(cs, r"\*\*Top Priority:\*\*\s*(.+)", "?")
    bn = ef(cs, r"\*\*Current Bottleneck:\*\*\s*(.+)", "?")

    issues = []
    research_queries = []
    critical_path = []
    revenue_actions = []
    partner_actions = []
    grant_actions = []
    project_actions = []

    # === 1. REVENUE CRITICAL CHECK ===
    cash_val = 0
    cash_matches = re.findall(r"~?(\d+)\s*FCFA", cash_raw)
    if cash_matches:
        cash_val = min(int(c) for c in cash_matches)

    if cash_val < 1500:
        issues.append({
            "type": "REVENUE_CRITICAL",
            "severity": "CRITICAL",
            "detail": f"Cash: {cash_raw} — below 1,500 FCFA threshold",
            "impact": "No runway for compute, data, or basic operations"
        })
        # Check EA trading opportunity
        ea_active = ef(cs, r"\*\*LiveTrading:\*\*\s*(\S+)", "false")
        if "true" not in ea_active.lower():
            revenue_actions.append({
                "action": "Activate EA trading on current London/NY session",
                "effort": "15min setup",
                "expected": "$0.50/ trade, ~10-20 trades/session",
                "blocker": "MT5 running + VPS or local keep-alive"
            })
        # Check if any micro-task or quick revenue is possible
        for line in plan.splitlines():
            if "- [ ]" in line and any(kw in line.lower() for kw in ["revenue", "vente", "client", "paiement", "facture", "mission"]):
                revenue_actions.append({
                    "action": line.strip().lstrip("- [ ]").strip(),
                    "effort": "from DAILY_PLAN",
                    "expected": "revenue",
                    "blocker": ""
                })
                break

    # === 2. GRANT / OPPORTUNITY WINDOW CHECK ===
    # Check WATCH_REGISTRY for 🔴 items expiring soon
    for line in reg.splitlines():
        if line.startswith("|") and "|---" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 8 and cols[4] == "🔴":
                item = cols[0]
                next_check = cols[5]
                status = cols[7]
                if status in ("🟢", "⚪"):
                    partner_actions.append({
                        "action": f"Follow up: {item}",
                        "source": "WATCH_REGISTRY",
                        "urgency": "🔴",
                        "next_check": next_check
                    })
                elif status == "🟡":
                    issues.append({
                        "type": "OPPORTUNITY_PENDING",
                        "severity": "HIGH",
                        "detail": f"{item} — status {status}, needs attention",
                        "impact": "May miss deadline or partner window"
                    })

    # === 3. PARTNER AWAITING CHECK ===
    # Look for signs we owe someone a response
    partner_keywords = [
        "ST Digital", "Herlog", "Cina Lawson", "Djanta Tech Hub",
        "Google for Startups", "DG West Africa", "Masakhane",
        "Lacuna Fund", "AI4D Africa"
    ]
    for kw in partner_keywords:
        if kw.lower() in cs.lower() or kw.lower() in co.lower() or kw.lower() in wr.lower():
            # Check if there's a specific action item
            for line in plan.splitlines():
                if kw.lower() in line.lower() and "- [ ]" in line:
                    partner_actions.append({
                        "action": f"Respond to {kw}: " + line.strip().lstrip("- [ ]").strip(),
                        "source": "DAILY_PLAN",
                        "urgency": "HIGH" if "🔴" in line else "MEDIUM"
                    })
                    break
            else:
                partner_actions.append({
                    "action": f"Check status of {kw} communication",
                    "source": "state_scan",
                    "urgency": "MEDIUM"
                })

    # === 4. STALE CONCEPTS ===
    stale_files = []
    for f in sorted(CONCEPTS_DIR.glob("*.md")):
        age = file_age_h(f)
        if age > 48:
            stale_files.append({"file": f.name, "age_h": round(age, 1)})
    if stale_files:
        issues.append({
            "type": "STALE_CONCEPTS",
            "severity": "MEDIUM",
            "detail": f"{len(stale_files)} concepts > 48h old: {', '.join(s['file'] for s in stale_files)}",
            "impact": "Knowledge drift — LLM may act on outdated state"
        })

    # === 5. PROJECT HEALTH CHECK ===
    for proj_dir in sorted(PROJECTS_DIR.iterdir()):
        if proj_dir.is_dir() and proj_dir.name != "KORA":
            readme = proj_dir / "README.md"
            strategic = list(proj_dir.glob("0*_*.md")) or list(proj_dir.glob("*_*.md"))
            if not readme.exists() and not strategic:
                project_actions.append({
                    "project": proj_dir.name,
                    "action": f"Create project structure for {proj_dir.name}",
                    "reason": "Missing README.md and strategic docs"
                })

    # === 6. NEXT ACTION FROM CYCLE ===
    cycle_next = ef(co, r"## NEXT ACTION\n-\s*(.+)", "")

    # === 7. RESEARCH NEEDED ===
    # Detect what information is missing for key decisions
    if "compute" in bn.lower() or "vps" in bn.lower() or "gpu" in bn.lower():
        research_queries.append({
            "query": "ST Digital GPU compute partnership status or alternative providers in West Africa",
            "reason": "Compute is the top bottleneck for KORA"
        })
    if "grant" in bn.lower() or "funding" in bn.lower():
        grant_deadlines = []
        for line in wr.splitlines():
            if "deadline" in line.lower() or "call" in line.lower():
                grant_deadlines.append(line.strip())
        if grant_deadlines:
            research_queries.append({
                "query": "; ".join(grant_deadlines),
                "reason": "Upcoming grant deadlines need preparation"
            })

    # === 8. SYNTHESIS: RECOMMENDED TOP ACTION ===
    top_action = {}
    if om == "SURVIVAL":
        if revenue_actions:
            top_action = {
                "category": "REVENUE",
                "action": revenue_actions[0]["action"],
                "effort": revenue_actions[0].get("effort", "?"),
                "expected": revenue_actions[0].get("expected", "Cash"),
                "subagent_type": "execution"
            }
        elif partner_actions:
            top_action = {
                "category": "PARTNER",
                "action": partner_actions[0]["action"],
                "urgency": partner_actions[0].get("urgency", "MEDIUM"),
                "subagent_type": "research"
            }
        elif grant_actions:
            top_action = {
                "category": "GRANT",
                "action": grant_actions[0]["action"],
                "subagent_type": "research"
            }
        elif project_actions:
            top_action = {
                "category": "PROJECT",
                "action": project_actions[0]["action"],
                "project": project_actions[0]["project"],
                "subagent_type": "execution"
            }
    else:
        if partner_actions:
            top_action = {"category": "PARTNER", "action": partner_actions[0]["action"], "subagent_type": "research"}
        elif grant_actions:
            top_action = {"category": "GRANT", "action": grant_actions[0]["action"], "subagent_type": "research"}
        elif stale_files:
            top_action = {"category": "MAINTENANCE", "action": "Update stale concepts", "subagent_type": "execution"}

    if not top_action and cycle_next:
        top_action = {"category": "FROM_CYCLE", "action": cycle_next, "subagent_type": "execution"}

    # === 9. BUILD DIAGNOSIS OUTPUT ===
    dx = {
        "timestamp": now.strftime("%Y-%m-%d %H:%M Lome UTC+0"),
        "mode": om,
        "cash": cash_raw,
        "bottleneck": bn,
        "top_priority": tp,
        "issues": issues,
        "revenue_actions": revenue_actions,
        "partner_actions": partner_actions,
        "grant_actions": grant_actions,
        "project_actions": project_actions,
        "research_queries": research_queries,
        "stale_files": stale_files,
        "recommended_action": top_action,
        "requires_approval": top_action.get("category") in ("REVENUE", "PARTNER", "GRANT", "GENERAL")
    }

    # === 10. WRITE _DIAGNOSIS.md ===
    lines = [
        f"# DIAGNOSIS — {dx['timestamp']}",
        f"**Mode:** {om} | **Cash:** {cash_raw}",
        f"**Bottleneck:** {bn}",
        f"**Top Priority:** {tp}",
        "",
        "## Issues Detected",
    ]
    if issues:
        for iss in issues:
            lines.append(f"- **[{iss['severity']}]** {iss['type']}: {iss['detail']}")
    else:
        lines.append("- No critical issues detected")
    lines.append("")

    if revenue_actions:
        lines.append("## Revenue Actions")
        for ra in revenue_actions:
            lines.append(f"- **{ra['action']}** (effort: {ra.get('effort', '?')}, expected: {ra.get('expected', '?')})")
            if ra.get('blocker'):
                lines.append(f"  - Blocker: {ra['blocker']}")
        lines.append("")

    if partner_actions:
        lines.append("## Partner Actions")
        for pa in partner_actions:
            lines.append(f"- [{pa.get('urgency', 'MEDIUM')}] {pa['action']} (from {pa['source']})")
        lines.append("")

    if grant_actions:
        lines.append("## Grant Actions")
        for ga in grant_actions:
            lines.append(f"- {ga['action']}")
        lines.append("")

    if project_actions:
        lines.append("## Project Health")
        for pa in project_actions:
            lines.append(f"- **{pa['project']}**: {pa['action']} ({pa['reason']})")
        lines.append("")

    if research_queries:
        lines.append("## Research Needed")
        for rq in research_queries:
            lines.append(f"- `{rq['query']}` — {rq['reason']}")
        lines.append("")

    if stale_files:
        lines.append("## Stale Concepts")
        for sc in stale_files:
            lines.append(f"- **{sc['file']}** ({sc['age_h']}h old)")
        lines.append("")

    if top_action:
        lines.append("## Recommended Next Action")
        lines.append(f"**Category:** {top_action.get('category', 'GENERAL')}")
        lines.append(f"**Action:** {top_action['action']}")
        lines.append(f"**Subagent type:** {top_action.get('subagent_type', 'general')}")
        lines.append(f"**Requires approval:** {'Yes' if dx.get('requires_approval', True) else 'No'}")
        lines.append("")

    lines.append("---")
    lines.append(f"*Diagnosis generated at {dx['timestamp']} by diagnose.py*")

    (STATE_DIR / "_DIAGNOSIS.md").write_text("\n".join(lines), encoding="utf-8")

    return dx


if __name__ == "__main__":
    import json
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
    dx = run_diagnosis()
    print(json.dumps(dx, indent=2, ensure_ascii=False, default=str))
    print(f"\nWritten: State/_DIAGNOSIS.md")
