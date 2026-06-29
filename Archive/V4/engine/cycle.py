import argparse
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    import kickoff
except ImportError:
    kickoff = None

try:
    import persona_detect
except ImportError:
    persona_detect = None

try:
    import session_log
except ImportError:
    session_log = None

try:
    import aimless_check
except ImportError:
    aimless_check = None

try:
    import diagnose
except ImportError:
    diagnose = None

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE_DIR / "State"
CONCEPTS_DIR = BASE_DIR / "concepts"


def rp(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""


def ef(text, pattern, default=""):
    m = re.search(pattern, text)
    return m.group(1).strip() if m else default


def now_lome():
    return datetime.now(timezone.utc)


def pt(s):
    m = re.match(r"(\d{1,2}):(\d{2})", s.strip())
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    return None


def elapsed(start_str, end_dt):
    start_m = pt(start_str)
    if start_m is None:
        return "?"
    end_m = end_dt.hour * 60 + end_dt.minute
    if end_m < start_m:
        end_m += 1440
    delta = end_m - start_m
    return f"{delta // 60}h{delta % 60:02d}m"


def fresh(path, max_h=48):
    if not path.exists():
        return "MISSING"
    mt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    age = (datetime.now(timezone.utc) - mt).total_seconds() / 3600
    return "FRESH" if age <= max_h else "STALE"


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
    ap = argparse.ArgumentParser(description="FounderOS Kernel Cycle")
    ap.add_argument("--mode", choices=["fhq", "fhqa", "boot", "shutdown"], default="fhqa")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    mode = args.mode
    now = now_lome()
    now_s = now.strftime("%Y-%m-%d %H:%M")
    now_hhmm = now.strftime("%H:%M")
    dow = now.strftime("%A")

    cad = rp(STATE_DIR / "CADENCE.md")
    ss = ef(cad, r"\*\*Session start:\*\*\s*(\S+)", "?")
    lf = ef(cad, r"\*\*Last fhq:\*\*\s*(\S+)", "?")
    lfa = ef(cad, r"\*\*Last fhqa:\*\*\s*(\S+)", lf if mode == "fhqa" else "?")
    last_key = "Last fhqa" if mode == "fhqa" else "Last fhq"
    last_val = lfa if mode == "fhqa" else lf
    wi = ef(cad, r"## Week\s+(.+)")
    if not wi:
        import datetime as dt_m
        curr_wk = dt_m.date.today().isocalendar().week
        for ln in cad.splitlines():
            if f"S{curr_wk}" in ln and ln.strip().startswith("-"):
                wi = ln.strip().lstrip("- ")[:60]
                break
    wi = wi.strip()[:60]
    do = ef(cad, r"\*\*Objectif:\*\*\s*(.+)")

    ss_orig = ss
    if mode == "boot":
        ss_orig = ss
        ss = now_hhmm
    se = elapsed(ss, now)
    fe = elapsed(last_val, now)
    auto_fhq = False
    lv_num = pt(last_val)
    if lv_num is not None:
        n = now.hour * 60 + now.minute
        if n < lv_num:
            n += 1440
        auto_fhq = (n - lv_num) >= 30

    cs = rp(STATE_DIR / "CURRENT_STATE.md")
    om = ef(cs, r"\*\*Operating Mode:\*\*\s*(\S+)", "?")
    cash = ef(cs, r"\*\*Cash.*:\*\*\s*(.+)", "?")
    tp = ef(cs, r"\*\*Top Priority:\*\*\s*(.+)", "?")
    bn = ef(cs, r"\*\*Current Bottleneck:\*\*\s*(.+)", "?")
    so = ef(cs, r"\*\*Session Objective:\*\*\s*(.+)", "")

    lc = rp(STATE_DIR / "LIFECYCLE.md")
    proj_phases = []
    phases_defs = {"IDEA","VALIDATION","LAUNCH","GROWTH","SCALE","MATURE"}
    for line in lc.splitlines():
        if line.startswith("| ") and not line.startswith("|---") and "Projet" not in line and "Phase" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 2 and cols[0] and cols[0] not in ("-", "Field", "OS Version", "Created", "Owner", "Purpose", *phases_defs):
                proj_phases.append({"project": cols[0], "phase": cols[1]})

    prio = rp(STATE_DIR / "PRIORITY_MATRIX.md")
    top3 = []
    nx_action = ""
    for line in prio.splitlines():
        if line.startswith("| ") and not line.startswith("|---") and "Projet" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 3 and cols[0] and cols[0] not in ("Projet", "-", "Objectif"):
                w = cols[4] if len(cols) > 4 else ""
                top3.append({"project": cols[0], "objective": cols[1], "warning": w})
        if "[ ]" in line and line.strip().startswith("- [ ]"):
            if not nx_action:
                nx_action = line.strip().lstrip("- [ ]").strip()

    top3 = top3[:3]
    top3_str = ", ".join([f"{p['project']}({p['warning']})" for p in top3]) if top3 else "N/A"

    al = rp(STATE_DIR / "ALERTS.md")
    wr = rp(STATE_DIR / "WATCH_REPORT.md")
    has_high_alerts = "HIGH" in al
    watch_alerts = []
    registry_text = rp(STATE_DIR / "WATCH_REGISTRY.md")
    for line in registry_text.splitlines():
        if line.startswith("|") and "|---" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            # cols[0]=WatchItem [1]=Project [2]=Query [3]=Freq [4]=Priority [5]=NextCheck [6]=LastResult [7]=Status
            if len(cols) >= 8 and cols[4] in ("🔴", "🟡"):
                watch_alerts.append({"item": cols[0], "priority": cols[4], "status": cols[7], "last": cols[5]})
    watch_entries_raw = [e.strip() for e in wr.split("\n### ") if e.strip()]
    watch_entry_count = len(watch_entries_raw)

    astra = {}
    astra_prefix = ""
    if mode == "fhqa":
        ad = rp(STATE_DIR / "ASTRA_DAILY.md")
        nak = ef(ad, r"\*\*Nakshatra:\*\*\s*(\S+)", "?")
        tithi = ef(ad, r"\*\*Tithi:\*\*\s*(.+)", "?")
        ss_phase = ef(ad, r"\*\*Sade Sati:\*\*\s*(.+)", "?")
        guidance = ef(ad, r"\*\*Guidance:\*\*\s*(.+)", "?")
        energy = ef(ad, r"\|\s*Energie\s*\|\s*(\d+)/100", "?")
        focus = ef(ad, r"\|\s*Focus\s*\|\s*(\d+)/100", "?")
        mood = ef(ad, r"\|\s*Humeur\s*\|\s*(\d+)/100", "?")
        sociability = ef(ad, r"\|\s*Sociabilite\s*\|\s*(\d+)/100", "?")
        emotion_advice = ef(ad, r"- \*\*Conseil:\*\*\s*(.+)", "?")
        md_ctx = ef(ad, r"\*\*MD:\*\*\s*(.+)", "?")
        ad_ctx = ef(ad, r"\*\*AD:\*\*\s*(.+)", "?")
        rahu_kaal = ef(ad, r"- \*\*Fenetre:\*\*\s*(\S+)", "?")
        best_action_type = ef(ad, r"- \*\*Meilleur type d'action:\*\*\s*(.+)", "?")
        muhurta = {}
        for line in ad.splitlines():
            m = re.match(r"^\|\s*(\w+)\s*\|\s*(\d+)/100\s*\|\s*(\w+)\s*\|\s*(\d+)/100\s*\|$", line)
            if m:
                muhurta[m.group(1)] = int(m.group(2))
                muhurta[m.group(3)] = int(m.group(4))
        ashtakavarga_text = ""
        ash_section = re.search(r"## Ashtakavarga Transits\n(.+?)(?:\n## |\Z)", ad, re.DOTALL)
        if ash_section:
            ashtakavarga_text = ash_section.group(1).strip()
        astra_prefix = f" | {nak}"
        astra = {
            "nakshatra": nak, "tithi": tithi,
            "sade_sati": ss_phase, "guidance": guidance,
            "energy": energy, "focus": focus, "mood": mood, "sociability": sociability,
            "emotion_advice": emotion_advice,
            "md": md_ctx, "ad": ad_ctx,
            "rahu_kaal": rahu_kaal,
            "best_action_type": best_action_type,
            "muhurta": muhurta,
            "ashtakavarga": ashtakavarga_text,
        }
        ab = rp(STATE_DIR / "ASTRA_BIRTH.md")
        astra["lagna"] = ef(ab, r"\*\*Sign:\*\*\s*(\S+)", "?")
        astra["md_lord"] = ef(ab, r"\*\*Mahadasha:\*\*\s*(.+)", "?")
        astra["md_start"] = ef(ab, r"\*\*Start:\*\*\s*(\S+)", "?")
        astra["md_end"] = ef(ab, r"\*\*End:\*\*\s*(\S+)", "?")
        astra["md_years"] = ef(ab, r"\*\*Years:\*\*\s*(\S+)", "?")
        astra["antar_dasha"] = ef(ab, r"\*\*Antar Dasha:\*\*\s*(.+)", "?")
        yogas = []
        in_yoga_section = False
        for line in ab.splitlines():
            if "## Yogas" in line:
                in_yoga_section = True
                continue
            if line.startswith("## ") and in_yoga_section:
                in_yoga_section = False
                continue
            if in_yoga_section:
                ym = re.match(r"^- \*\*(.+?)\*\*", line)
                if ym:
                    yogas.append(ym.group(1))
        astra["yogas"] = yogas[:5]
        astra["yoga_count"] = len(yogas)
        shadbala = {}
        for line in ab.splitlines():
            sm = re.match(r"^\|\s*(\w+)\s*\|\s*(\d+)/100\s*\|\s*(\S+)", line)
            if sm and sm.group(1) not in ("Graha",):
                shadbala[sm.group(1)] = {"score": int(sm.group(2)), "quality": sm.group(3)}
        if shadbala:
            sorted_shadbala = sorted(shadbala.items(), key=lambda x: -x[1]["score"])
            astra["shadbala_top3"] = [f"{g}({v['score']})" for g, v in sorted_shadbala[:3]]
            astra["shadbala_bottom3"] = [f"{g}({v['score']})" for g, v in sorted_shadbala[-3:]]
        d9_m = re.search(r"### D9[^\n]*\n[^\n]*\n- \*\*Lagna:\*\*\s*(\S+)", ab)
        astra["d9_lagna"] = d9_m.group(1) if d9_m else "?"
        d10_m = re.search(r"### D10[^\n]*\n[^\n]*\n- \*\*Lagna:\*\*\s*(\S+)", ab)
        astra["d10_lagna"] = d10_m.group(1) if d10_m else "?"
        d60_m = re.search(r"### D60[^\n]*\n[^\n]*\n- \*\*Lagna:\*\*\s*(\S+)", ab)
        astra["d60_lagna"] = d60_m.group(1) if d60_m else "?"
        ash = rp(STATE_DIR / "ASTRA_SHADOW.md")
        warnings = []
        for line in ash.splitlines():
            if line.startswith("| ") and "WARN" in line:
                cols = [c.strip() for c in line.strip("|").split("|")]
                if len(cols) >= 4:
                    warnings.append(f"{cols[0]} {cols[1]} — {cols[2]}")
        astra["warnings"] = warnings

    mission_fresh = fresh(CONCEPTS_DIR / "MISSION.md")
    plan_fresh = fresh(STATE_DIR / "DAILY_PLAN.md")

    stale = []
    for f in sorted(CONCEPTS_DIR.glob("*.md")):
        st = fresh(f)
        if st != "FRESH":
            stale.append({"file": f.name, "status": st})

    header = f"**[{now_s} Lome UTC+0] | Session: {se} | {dow}{astra_prefix}**"
    sade_s = f" + Sade Sati {astra.get('sade_sati', '?')}" if mode == "fhqa" and astra.get("sade_sati") else ""
    lc_str = f"{om}{sade_s}"

    active_persona = ""
    persona_confidence = 0.0
    trigger_venture = False
    um = STATE_DIR / "_USER_MESSAGE.txt"
    if persona_detect and um.exists():
        txt = um.read_text(encoding="utf-8", errors="replace")
        try:
            pd = persona_detect.detect_persona(txt)
            active_persona = pd["persona"]
            persona_confidence = pd["confidence"]
            trigger_venture = pd["trigger_venture"]
            if active_persona and active_persona != "?":
                persona_detect.update_active_persona(active_persona)
                persona_detect.write_persona_state(active_persona, persona_confidence, trigger_venture, persona_detect.check_novice_mode())
        except Exception:
            pass
        um.unlink(missing_ok=True)

    lines = [
        f"# CYCLE OUTPUT — {now_s} Lome UTC+0",
        f"**Mode:** {mode}",
        "",
        "## HEADER",
        header,
        "",
    ]
    if has_high_alerts:
        lines.append("!! **HIGH ALERTS ACTIVE** — check ALERTS.md")
        lines.append("")
    lines += [
        "## CONTEXT",
        f"- **Operating Mode:** {om}",
        f"- **Session:** {se} (started {ss})",
        f"- **{last_key}:** {last_val} ({fe} ago)" + (" !! Auto-FHQ due!" if auto_fhq else ""),
        f"- **Week:** {wi}",
        f"- **Cash:** {cash}",
        f"- **Active Persona:** {active_persona} ({persona_confidence})",
        f"- **Top Priority:** {tp}",
        f"- **Bottleneck:** {bn}",
    ]
    if so:
        lines.append(f"- **Session Objective:** {so}")
    else:
        lines.append(f"- **Objective:** {do}")
    lines.append(f"- **Mission Status:** {mission_fresh}")
    lines.append(f"- **Daily Plan:** {plan_fresh}")
    try:
        av = aimless_verdict
        if av and av.get("aimless"):
            lines.append(f"- **Aimless:** {av['type']} — {av.get('recommendation', '')[:60]}")
    except Exception:
        pass
    lines.append("")

    if mode == "fhqa":
        lines += [
            "## ASTRA",
            f"- **Nakshatra:** {astra.get('nakshatra', '?')}",
            f"- **Tithi:** {astra.get('tithi', '?')}",
            f"- **Sade Sati:** {astra.get('sade_sati', '?')}",
            f"- **Guidance:** {astra.get('guidance', '?')}",
            f"- **Energy/Focus/Mood/Sociability:** {astra.get('energy', '?')}/{astra.get('focus', '?')}/{astra.get('mood', '?')}/{astra.get('sociability', '?')}",
            f"- **Emotion Advice:** {astra.get('emotion_advice', '?')}",
            f"- **Rahu Kaal:** {astra.get('rahu_kaal', '?')}",
            f"- **Best Action:** {astra.get('best_action_type', '?')}",
            f"- **Lagna:** {astra.get('lagna', '?')}",
            f"- **Mahadasha:** {astra.get('md_lord', astra.get('md', '?'))} ({astra.get('md_start', '?')} - {astra.get('md_end', '?')}, {astra.get('md_years', '?')}yr) | AD: {astra.get('antar_dasha', '?')}",
        ]
        mu = astra.get("muhurta", {})
        if mu:
            top_mu = sorted(mu.items(), key=lambda x: -x[1])[:3]
            lines.append(f"- **Top Muhurta:** {' | '.join(f'{k}({v})' for k, v in top_mu)}")
        yogas = astra.get("yogas", [])
        if yogas:
            lines.append(f"- **Top Yogas:** {'; '.join(yogas)}")
        st3 = astra.get("shadbala_top3", [])
        sb3 = astra.get("shadbala_bottom3", [])
        if st3 or sb3:
            lines.append(f"- **Shadbala:** top={', '.join(st3)} / bottom={', '.join(sb3)}")
        d9 = astra.get("d9_lagna", "?")
        d10 = astra.get("d10_lagna", "?")
        d60 = astra.get("d60_lagna", "?")
        lines.append(f"- **Vargas:** D9={d9} D10={d10} D60={d60}")
        ashtaka = astra.get("ashtakavarga", "")
        if ashtaka:
            lines.append(f"- **Ashtakavarga:**")
            for ash_line in ashtaka.splitlines():
                if ash_line.strip():
                    lines.append(f"  {ash_line.strip()}")
        lines.append("")
        for w in astra.get("warnings", []):
            lines.append(f"- !! {w}")
        if astra.get("warnings"):
            lines.append("")

    ph_str = ", ".join([f'{p["project"]}={p["phase"]}' for p in proj_phases])
    lines += [
        "## PROJECTS",
        f"- **Top 3:** {top3_str}",
        f"- **Phases:** {ph_str}",
        "",
    ]

    if stale:
        lines.append("## STALE CONCEPTS")
        for sc in stale:
            lines.append(f"- **{sc['file']}** — {sc['status']}")
        lines.append("")

    if nx_action:
        lines += [
            "## NEXT ACTION",
            f"- {nx_action}",
            "",
        ]

    lines += ["## Alerts"]
    alert_lines_found = False
    in_active_section = False
    for al_line in al.splitlines():
        if "## Active Alerts" in al_line:
            in_active_section = True
            continue
        if al_line.startswith("## ") and in_active_section:
            in_active_section = False
            continue
        if in_active_section and al_line.startswith("| ") and "|---" not in al_line:
            cells = [c.strip() for c in al_line.strip("|").split("|")]
            if len(cells) >= 1 and cells[0] == "Priority":
                continue  # skip table header row
            if len(cells) >= 1 and cells[0] in ("🔴", "🟡", "🟢"):
                lines.append(f"- {' | '.join(c for c in cells if c)}")
                alert_lines_found = True
    if not alert_lines_found:
        lines.append("- No active alerts")
    lines.append("")

    lines += ["## Watch Reports (🔥 priority only)"]
    if watch_alerts:
        for wa in watch_alerts:
            lines.append(f"- {wa['priority']} **{wa['item']}** | {wa['status']} | last: {wa['last']}")
        lines.append(f"- *{watch_entry_count} total items in WATCH_REPORT.md; 🟢/⚪ suppressed*")
    elif watch_entry_count > 0:
        lines.append(f"- No 🔴/🟡 alerts. {watch_entry_count} items tracked.")
    else:
        lines.append("- No recent reports")
    lines.append("")

    lines += [
        "---",
        f"*Cycle executed at {now_s} by cycle.py | Mode: {mode}*",
    ]

    (STATE_DIR / "_CYCLE_OUTPUT.md").write_text("\n".join(lines), encoding="utf-8")

    if kickoff:
        try:
            if mode == "boot":
                kickoff.generate_daily_plan()
            elif mode in ("fhq", "fhqa"):
                result = kickoff.generate_daily_plan_if_stale()
                if result.get("generated"):
                    print(f"!! DAILY_PLAN regenerated ({result.get('reason')})")
        except Exception as e:
            print(f"!! Kickoff error: {e}")

    if mode in ("fhq", "fhqa", "boot", "shutdown"):
        new_cad = cad
        def _uf(text, field, value, anchor):
            pat = rf"(\*\*{field}:\*\*)\s*\S*"
            if re.search(pat, text):
                return re.sub(pat, f"\\1 {value}", text)
            ap = rf"(\*\*{anchor}:\*\*.*)"
            m = re.search(ap, text)
            if m:
                return re.sub(ap, f"\\1\n**{field}:** {value}", text)
            return text + f"\n**{field}:** {value}"
        if mode == "boot":
            new_cad = _uf(new_cad, "Session start", now_hhmm, "Session end")
        elif mode == "shutdown":
            new_cad = _uf(new_cad, "Session end", now_hhmm, "Last fhqa")
            new_cad = _uf(new_cad, "Session end", now_hhmm, "Last fhq")
            new_cad = _uf(new_cad, "Session end", now_hhmm, "Session start")
        elif mode == "fhq":
            new_cad = _uf(new_cad, "Last fhq", now_hhmm, "Last fhqa")
            new_cad = _uf(new_cad, "Last fhq", now_hhmm, "Session start")
        else:
            if re.search(r"\*\*Last fhqa:\*\*", new_cad):
                new_cad = _uf(new_cad, "Last fhqa", now_hhmm, "Last fhq")
            else:
                new_cad = _uf(new_cad, "Last fhq", lf if lf != "?" else now_hhmm, "Session start")
                new_cad = _uf(new_cad, "Last fhqa", now_hhmm, "Last fhq")
        (STATE_DIR / "CADENCE.md").write_text(new_cad, encoding="utf-8")

    new_al = re.sub(r"(\*\*Cleared at:\*\*)\s*.*", f"\\1 {now_s} — Lome UTC+0", al)
    in_active = False
    has_header = False
    active_lines = []
    for line in new_al.splitlines():
        if "## Active Alerts" in line:
            in_active = True
            active_lines.append(line)
            continue
        if in_active and re.match(r"^\| .+ \| .+ \| .+ \| .+ \|$", line):
            if not has_header:
                has_header = True
                active_lines.append(line)
            continue
        if line.startswith("## ") and in_active:
            in_active = False
            has_header = False
        active_lines.append(line)
    new_al = "\n".join(active_lines)
    (STATE_DIR / "ALERTS.md").write_text(new_al, encoding="utf-8")

    if session_log:
        try:
            if mode == "boot":
                session_log.init_session()
            user_msg = ""
            um_path = STATE_DIR / "_USER_MESSAGE.txt"
            if um_path.exists():
                user_msg = um_path.read_text(encoding="utf-8", errors="replace")[:80]
                um_path.unlink(missing_ok=True)
            session_log.log_turn(user_message=user_msg, system_action=f"cycle_{mode}")
        except Exception:
            pass

    aimless_verdict = {}
    if aimless_check:
        try:
            aimless_verdict = aimless_check.run_check()
        except Exception:
            aimless_verdict = {}

    diagnosis = {}
    if diagnose and mode in ("fhq", "fhqa", "boot"):
        try:
            diagnosis = diagnose.run_diagnosis()
        except Exception as e:
            print(f"!! Diagnosis error: {e}")
            diagnosis = {}

    # Cycle counter — monotonic, never repeats
    counter_file = STATE_DIR / "_CYCLE_COUNTER.md"
    try:
        prev_count = int(counter_file.read_text(encoding="utf-8").strip())
    except (FileNotFoundError, ValueError):
        prev_count = 0
    cycle_num = prev_count + 1
    counter_file.write_text(str(cycle_num), encoding="utf-8")

    # Write _CYCLE_REQUIRED_HEADER.md with mechanical DX command + cycle counter
    if mode in ("fhq", "fhqa", "boot", "shutdown"):
        dx_rec = diagnosis.get("recommended_action", {}) if diagnosis else {}
        dx_approval = diagnosis.get("requires_approval", True) if diagnosis else True
        dx_cat = dx_rec.get("category", "?")
        dx_sa = dx_rec.get("subagent_type", "?")
        dx_line = f"DX={dx_cat} SUBAGENT={dx_sa} APPROVAL={'REQUIRED' if dx_approval else 'AUTO'}"
        (STATE_DIR / "_CYCLE_REQUIRED_HEADER.md").write_text(f"{header}\n{dx_line}\nCYCLE={cycle_num}", encoding="utf-8")

    if mode == "shutdown" and session_log:
        try:
            session_log.prune_session()
        except Exception:
            pass

    result = {
        "mode": mode, "datetime": now_s, "header": header,
        "session_elapsed": se, f"last_{mode}": last_val,
        f"{mode}_elapsed": fe, "auto_fhq_due": auto_fhq,
        "operating_mode": om, "cash": cash, "top_priority": tp,
        "bottleneck": bn, "active_persona": active_persona,
        "persona_confidence": persona_confidence, "trigger_venture": trigger_venture,
        "week_info": wi,
        "top3": [p["project"] for p in top3],
        "stale_concepts": [sc["file"] for sc in stale],
        "next_action": nx_action,
        "mission_status": mission_fresh,
        "daily_plan_status": plan_fresh,
        "kickoff_triggered": mode in ("boot", "fhq", "fhqa") and kickoff is not None,
        "aimless": aimless_verdict,
        "diagnosis": {
            "issues": len(diagnosis.get("issues", [])),
            "recommended": diagnosis.get("recommended_action", {}),
            "revenue_actions": len(diagnosis.get("revenue_actions", [])),
            "partner_actions": len(diagnosis.get("partner_actions", [])),
        } if diagnosis else {},
        "session_log_active": session_log is not None,
    }
    if mode == "fhqa":
        result["astra"] = astra

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"OK: Cycle {mode} executed at {now_s}")
        print(f"Header: {header}")
        print(f"Written: State/_CYCLE_OUTPUT.md")
        print(f"Written: State/_DIAGNOSIS.md")
        if diagnosis:
            dx_rec = diagnosis.get("recommended_action", {})
            dx_issues = len(diagnosis.get("issues", []))
            dx_rev = len(diagnosis.get("revenue_actions", []))
            dx_part = len(diagnosis.get("partner_actions", []))
            dx_approval = diagnosis.get("requires_approval", True)
            print(f"DX: {dx_issues} issues | {dx_rev} revenue | {dx_part} partner | action: {dx_rec.get('category','?')} | subagent: {dx_rec.get('subagent_type','?')} | approval: {'yes' if dx_approval else 'no'}")
        if auto_fhq:
            print(f"!!  Auto-FHQ due: {fe} since last {mode}")
        if stale:
            print(f"Stale concepts: {len(stale)}")


if __name__ == "__main__":
    main()
