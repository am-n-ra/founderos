import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE_DIR / "State"

now = datetime.now(timezone.utc)
now_s = now.strftime("%Y-%m-%d %H:%M")
dow = now.strftime("%A")


def rp(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""


def ef(text, pattern, default="?"):
    m = re.search(pattern, text)
    return m.group(1).strip() if m else default


def parse_table(text, expected_cols=5):
    rows = []
    for line in text.splitlines():
        if line.startswith("| ") and not line.startswith("|---") and "Projet" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= expected_cols and cols[0] and cols[0] not in ("Projet", "-", "Objectif"):
                rows.append(cols)
    return rows


def parse_muhurta(text):
    muhurta = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\w+)\s*\|\s*(\d+)/100\s*\|\s*(\w+)\s*\|\s*(\d+)/100\s*\|$", line)
        if m:
            muhurta[m.group(1)] = int(m.group(2))
            muhurta[m.group(3)] = int(m.group(4))
    return muhurta


MISSION_MAP = {
    "KORA": "Africa Technology Sovereignty",
    "OMNI": "Africa Technology Sovereignty",
    "EDENVALLEY": "Africa Technology Sovereignty",
    "SOJACO": "Financial Independence",
    "DOODLEMIND": "Financial Independence",
    "PEST REPELLER": "Financial Independence",
    "STOP NUISIBLES": "Financial Independence",
    "SOLAR KIT": "Financial Independence",
    "FHQ": "FounderHQ",
    "FOUNDEROS": "FounderHQ",
    "FOUNDERHQ": "FounderHQ",
}


def read_mission():
    text = rp(BASE_DIR / "concepts" / "MISSION.md")
    missions = []
    current = {}
    for line in text.splitlines():
        if line.startswith("## ") and "Mission" in line and line.strip("# ").strip():
            if current.get("name"):
                missions.append(current)
            current = {"name": line.strip("# ").strip()}
        elif line.startswith("- Description:") and current:
            current["desc"] = line.split(":", 1)[1].strip()
        elif line.startswith("- Status:") and current:
            current["status"] = line.split(":", 1)[1].strip()
    if current.get("name"):
        missions.append(current)
    return {"missions": missions, "raw": text}


def mission_for_project(project_name):
    upper = project_name.strip().upper()
    if upper in MISSION_MAP:
        return MISSION_MAP[upper]
    return "Root Mission"


def get_mission_statement(mission_name, missions):
    for m in missions:
        if m.get("name") == mission_name:
            return m.get("desc", "")
    return ""


def generate_daily_plan():
    cs = rp(STATE_DIR / "CURRENT_STATE.md")
    om = ef(cs, r"\*\*Operating Mode:\*\*\s*(\S+)", "SURVIVAL")
    cash_raw = ef(cs, r"\*\*Cash.*:\*\*\s*(.+)", "?")
    cash_amount = 0
    cash_total = re.search(r"Total utilisable.*?~?(\d+)", cash_raw)
    if cash_total:
        cash_amount = int(cash_total.group(1))
    else:
        cash_first = re.search(r"~(\d+)", cash_raw)
        if cash_first:
            cash_amount = int(cash_first.group(1))
        else:
            cash_direct = re.search(r"(\d+)", cash_raw)
            if cash_direct:
                cash_amount = int(cash_direct.group(1))
    tp = ef(cs, r"\*\*Top Priority:\*\*\s*(.+)", "?")
    bn = ef(cs, r"\*\*Current Bottleneck:\*\*\s*(.+)", "?")
    so = ef(cs, r"\*\*Session Objective:\*\*\s*(.+)", "")

    prio = rp(STATE_DIR / "PRIORITY_MATRIX.md")
    projects = parse_table(prio, 7)
    top3_projects = []
    pending_actions = []
    in_pending = False
    for line in prio.splitlines():
        if "Actions Pending" in line:
            in_pending = True
            continue
        if "Règles d'Utilisation" in line:
            in_pending = False
            continue
        if in_pending:
            m = re.match(r"-\s+\[\s*([ xX]?)\s*\]\s+\*\*(.+?)\*\*\s*[—–-]\s*(.+)", line)
            if m:
                pending_actions.append({
                    "done": m.group(1).lower() == "x",
                    "project": m.group(2).strip(),
                    "action": m.group(3).strip()
                })
    for p in projects[:3]:
        top3_projects.append({"project": p[0], "objective": p[1], "status": p[2], "next": p[3], "warning": p[6] if len(p) > 6 else "🟢"})

    mission_ctx = read_mission()
    missions = mission_ctx["missions"]

    al = rp(STATE_DIR / "ALERTS.md")
    high_alerts = []
    medium_alerts = []
    in_active = False
    for line in al.splitlines():
        if "## Active Alerts" in line:
            in_active = True
            continue
        if line.startswith("## ") and in_active:
            in_active = False
            continue
        if in_active and line.startswith("| ") and "|---" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 1 and cells[0] in ("🔴", "🟡", "🟢"):
                if cells[0] == "🔴":
                    high_alerts.append(cells)
                elif cells[0] == "🟡":
                    medium_alerts.append(cells)

    ad = rp(STATE_DIR / "ASTRA_DAILY.md")
    nakshatra = ef(ad, r"\*\*Nakshatra:\*\*\s*(\S+)", "?")
    sade_sati = ef(ad, r"\*\*Sade Sati:\*\*\s*(.+)", "?")
    rahu_kaal = ef(ad, r"- \*\*Fenetre:\*\*\s*(\S+)", "?")
    best_action_type = ef(ad, r"- \*\*Meilleur type d'action:\*\*\s*(.+)", "?")
    guidance = ef(ad, r"\*\*Guidance:\*\*\s*(.+)", "?")
    muhurta = parse_muhurta(ad)
    energy = ef(ad, r"\|\s*Energie\s*\|\s*(\d+)/100", "?")
    focus = ef(ad, r"\|\s*Focus\s*\|\s*(\d+)/100", "?")

    revenue_required = cash_amount < 1500

    lines = []
    lines.append(f"# DAILY PLAN — {now_s}")
    lines.append("")
    lines.append(f"**Last Updated:** {now_s} Lome UTC+0")
    lines.append(f"**Mode:** {om}")
    lines.append(f"**Cash:** {cash_raw}")
    lines.append(f"**Revenue required:** {'YES — cash < 1,500 FCFA' if revenue_required else 'No'}")
    lines.append("")

    lines.append("## Top 3 Priorities")
    lines.append("")
    lines.append("| # | Project | Action | Status |")
    lines.append("|---|---------|--------|--------|")
    for i, p in enumerate(top3_projects[:3], 1):
        lines.append(f"| {i} | {p['project']} | {p['objective']} | [ ] |")
    lines.append("")

    if missions:
        lines.append("## Mission Alignment")
        lines.append("")
        lines.append("| # | Action | Mission |")
        lines.append("|---|--------|---------|")
        for i, p in enumerate(top3_projects[:3], 1):
            mname = mission_for_project(p["project"])
            mdesc = get_mission_statement(mname, missions)
            brief = mdesc[:60] + "..." if len(mdesc) > 60 else mdesc
            lines.append(f"| {i} | {p['project']}: {p['objective']} | {mname} — {brief}" if brief else f"| {i} | {p['project']}: {p['objective']} | {mname} |")
        if missions and missions[0].get("name"):
            lines.append(f"| — | Root mission | {missions[0]['name']} |")
        lines.append("")

    if revenue_required:
        lines.append("## Revenue Actions (mandatory — cash < 1,500 FCFA)")
        lines.append("")
        revenue_found = False
        for pa in pending_actions:
            if not pa["done"] and pa["project"] in ("SOJACO", "PEST REPELLER", "DOODLEMIND"):
                lines.append(f"- [ ] **{pa['project']}** — {pa['action']}")
                revenue_found = True
        if not revenue_found:
            lines.append("- [ ] **EA Trading** — Run London/NY session, monitor live trades")
            lines.append("- [ ] **PEST REPELLER** — Create 1 TikTok organic video (0 budget)")
            lines.append("- [ ] **DOODLEMIND** — Produce Short #3, publish YT+TK")
        lines.append("")

    best_mu = sorted(muhurta.items(), key=lambda x: -x[1]) if muhurta else []
    morning_score = best_mu[0][1] if best_mu else "?"
    afternoon_score = best_mu[1][1] if len(best_mu) > 1 else "?"
    evening_score = best_mu[2][1] if len(best_mu) > 2 else "?"

    top3_names = [p["objective"] for p in top3_projects[:3]]
    morning_action = tp if tp and tp != "?" else (top3_names[0] if top3_names else "Review priorities")
    afternoon_action = top3_names[1] if len(top3_names) > 1 else (pending_actions[0]["action"] if pending_actions else "Deep work")
    if revenue_required:
        evening_action = "Revenue generation — see Revenue Actions section"
    else:
        evening_action = top3_names[2] if len(top3_names) > 2 else "Plan next day"

    lines.append("## Time Blocks")
    lines.append("")
    lines.append("| Block | Action | Duration |")
    lines.append("|-------|--------|----------|")
    lines.append(f"| Morning (06:00-12:00) | {morning_action} | {morning_score}/100")
    lines.append(f"| Afternoon (12:00-18:00) | {afternoon_action} | {afternoon_score}/100")
    lines.append(f"| Evening (18:00-00:00) | {evening_action} | {evening_score}/100")
    lines.append("")

    lines.append("## Blockers")
    lines.append("")
    if bn and bn != "?":
        lines.append(f"- [ ] {bn}")
    for p in top3_projects:
        if p.get("warning") in ("🔴", "🟡"):
            if p.get("next") and p["next"] != "-":
                lines.append(f"- [ ] **{p['project']}:** {p['next']}")
    if "Oracle" in cs or "VPS" in cs:
        lines.append("- [ ] VPS Oracle — débloquer vm.standard ou alternative")
    if "GCP" in cs or "Google" in cs:
        lines.append("- [ ] GCP — top-up $50 pour valider compte (koralab)")
    lines.append("")

    lines.append("## Astral Timing")
    lines.append("")
    if nakshatra != "?":
        lines.append(f"- **Nakshatra:** {nakshatra}")
    if sade_sati != "?":
        lines.append(f"- **Sade Sati:** {sade_sati}")
    if rahu_kaal != "?":
        lines.append(f"- **Rahu Kaal:** {rahu_kaal}")
    if best_action_type != "?":
        lines.append(f"- **Best action type:** {best_action_type}")
    if guidance != "?":
        lines.append(f"- **Guidance:** {guidance}")
    if muhurta:
        top_mu = best_mu[:5]
        lines.append(f"- **Top Muhurta:** {' | '.join(f'{k}({v})' for k, v in top_mu)}")
    lines.append("")

    lines.append("## Alerts")
    lines.append("")
    if high_alerts:
        for a in high_alerts:
            lines.append(f"- 🔴 {' | '.join(c for c in a if c)}")
    if not high_alerts and not medium_alerts:
        lines.append("- No active alerts")
    else:
        for a in medium_alerts[:3]:
            lines.append(f"- 🟡 {' | '.join(c for c in a if c)}")
    lines.append("")

    lines.append("---")
    lines.append(f"*Generated by kickoff.py at {now_s} Lome UTC+0*")

    (STATE_DIR / "DAILY_PLAN.md").write_text("\n".join(lines), encoding="utf-8")

    header = f"**[{now_s} Lome UTC+0] | Kickoff: {om} | {dow} | Cash: {cash_amount}FCFA{' !!' if revenue_required else ''}**"
    (STATE_DIR / "_CYCLE_REQUIRED_HEADER.md").write_text(header, encoding="utf-8")

    return json.dumps({
        "status": "ok",
        "plan_path": str(STATE_DIR / "DAILY_PLAN.md"),
        "top_action": tp,
        "revenue_required": revenue_required,
        "alerts_count": len(high_alerts) + len(medium_alerts)
    }, ensure_ascii=False)


def generate_daily_plan_if_stale():
    plan_path = STATE_DIR / "DAILY_PLAN.md"
    if not plan_path.exists():
        generate_daily_plan()
        return {"generated": True, "reason": "missing", "plan_path": str(plan_path)}
    content = plan_path.read_text(encoding="utf-8", errors="replace")
    today_str = now.strftime("%Y-%m-%d")
    if today_str in content:
        return {"generated": False}
    generate_daily_plan()
    return {"generated": True, "reason": "stale", "plan_path": str(plan_path)}


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
    result = generate_daily_plan()
    print(result)


if __name__ == "__main__":
    main()
