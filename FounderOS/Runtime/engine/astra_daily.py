"""astra_daily.py — Generate ASTRA_DAILY.md state file.

Run by timekeeper once daily (00:30) or on demand.
Reads ASTRA_BIRTH.md if available for natal context.
Writes ASTRA_DAILY.md + updates ASTRA_SHADOW.md.

Usage:
    python Runtime/engine/astra_daily.py --base-dir C:/path/to/FounderHQ
    python Runtime/engine/astra_daily.py --base-dir . --force
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure workspace root is on sys.path for direct script execution
_this_dir = Path(__file__).resolve().parent
_workspace_root = _this_dir.parent.parent
if str(_workspace_root) not in sys.path:
    sys.path.insert(0, str(_workspace_root))

from Runtime.engine.astra_core import AstraEngine


def render_daily_md(engine, jd, birth_chart=None) -> str:
    """Render full daily markdown for ASTRA_DAILY.md."""
    panch = engine.compute_panchanga(jd)
    horas = engine.compute_horas(jd)
    emotion = engine.emotional_forecast(jd)
    rahu = engine.rahu_kaal(jd)
    reds = engine.detect_red_zones(jd)
    score = engine.score_muhurta(jd, "general")
    sade = engine.compute_sade_sati(birth_chart) if birth_chart else {"active": False, "phase": "none", "guidance": ""}

    now = datetime.now(timezone.utc)
    sun = engine.sunrise_sunset(jd)

    md = f"""# ASTRA DAILY — {now.strftime('%Y-%m-%d')}

> Lome (UTC+0) — Generated at {now.strftime('%H:%M')}

## Chapter Context
"""

    if birth_chart and birth_chart.get("dasha"):
        d = birth_chart["dasha"]
        md += f"""- **MD:** {d['current_md']['lord']} ({d['current_md']['start']} - {d['current_md']['end']})
"""
        if d.get('current_ad'):
            md += f"""- **AD:** {d['current_ad']['lord']} ({d['current_ad']['start']} - {d['current_ad']['end']})
"""

    if sade["active"]:
        md += f"""- **Sade Sati:** {sade['phase']}
- **Guidance:** {sade['guidance']}
"""

    md += f"""
## Panchanga
- **Vara:** {panch['vara']['name']} ({panch['vara']['graha']})
- **Tithi:** {panch['tithi']['name']} ({panch['tithi']['paksha']})
- **Nakshatra:** {panch['nakshatra']['name']} — Pada {panch['nakshatra']['pada']}
- **Lord:** {panch['nakshatra']['lord']}
- **Yoga:** {panch['yoga']['name']}

## Sun & Moon
- **Lever:** {sun['sunrise']}
- **Coucher:** {sun['sunset']}
- **Soleil:** {engine.rashi_name(panch['sun_lon'])} {panch['sun_lon'] % 30:.1f} deg
- **Lune:** {engine.rashi_name(panch['moon_lon'])} {panch['moon_lon'] % 30:.1f} deg

## Emotional Forecast
| Axe | Score | Note |
|-----|-------|------|
| Energie | {emotion['energy']}/100 | {emotion['mood_label']} |
| Focus | {emotion['focus']}/100 | |
| Humeur | {emotion['mood']}/100 | |
| Sociabilite | {emotion['sociability']}/100 | |
- **Conseil:** {emotion['mood_advice']}

## Hora Actuelle
- **Hora:** {horas['active']['lord'] if horas['active'] else 'N/A'} ({horas['active']['start'] if horas['active'] else 'N/A'} - {horas['active']['end'] if horas['active'] else 'N/A'})
- **Favorable pour:** {horas['active']['guide'] if horas['active'] else 'N/A'}
"""

    if rahu:
        active_note = " [ACTIF MAINTENANT]" if rahu["active"] else ""
        md += f"""
## Rahu Kaal
- **Fenetre:** {rahu['start']} - {rahu['end']}{active_note}
"""

    if reds:
        md += """
## Red Zones
| Severite | Fenetre | Regle |
|----------|---------|-------|
"""
        for r in reds:
            now_tag = " ⚠" if r.get("now") else ""
            md += f"| {r['severity']}{now_tag} | {r['window']} | {r['rule']} |\n"

    muhurta_types = [
        "general", "signature", "negotiation", "launch", "deep_work",
        "fundraising", "content", "medical", "travel", "education",
        "investment", "partnership", "legal", "renovation", "moving",
        "vehicle", "interview", "networking",
    ]
    
    md += f"""
## Muhurta Scores
| Type | Score | Type | Score |
|------|-------|------|-------|
"""
    for i in range(0, len(muhurta_types), 2):
        t1 = muhurta_types[i]
        s1 = engine.score_muhurta(jd, t1)
        if i + 1 < len(muhurta_types):
            t2 = muhurta_types[i + 1]
            s2 = engine.score_muhurta(jd, t2)
            md += f"| {t1} | {s1}/100 | {t2} | {s2}/100 |\n"
        else:
            md += f"| {t1} | {s1}/100 | | |\n"

    md += "\n## Today's Guidance\n"

    # Ashtakavarga transit analysis
    if birth_chart:
        try:
            ashta = engine.compute_ashtaka_transit(jd, birth_chart["jd"])
            strong_transits = [t for t in ashta["transits"] if t.get("above_average")]
            if strong_transits:
                md += "\n## Ashtakavarga Transits\n"
                md += "| Graha | Transit | Bindus |\n"
                md += "|-------|---------|--------|\n"
                for t in strong_transits:
                    md += f"| {t['graha']} | {t['transit_rashi']} | {t['transit_bindu']} |\n"
        except Exception as e:
            print(f"[WARN] Ashtakavarga transit error: {e}")

    best_type = max([
        ("signature", engine.score_muhurta(jd, "signature")),
        ("negotiation", engine.score_muhurta(jd, "negotiation")),
        ("deep_work", engine.score_muhurta(jd, "deep_work")),
        ("content", engine.score_muhurta(jd, "content")),
    ], key=lambda x: x[1])

    md += f"- **Meilleur type d'action:** {best_type[0]} ({best_type[1]}/100)\n"
    if horas["active"]:
        md += f"- **Maintenant:** Hora {horas['active']['lord']} — {horas['active']['guide']}\n"
    if rahu and rahu["active"]:
        md += f"- **Eviter:** Decisions importantes jusqu'a {rahu['end']} (Rahu Kaal)\n"
    elif rahu:
        md += f"- **Prep:** Rahu Kaal a {rahu['start']} — prepare les decisions avant\n"

    if sade["active"]:
        md += f"- **Sade Sati:** {sade['guidance']}\n"

    md += f"""
---
*ASTRA Daily — Generated by astra_daily.py at {now.strftime('%Y-%m-%d %H:%M')} UTC*
"""
    return md


def render_shadow_md(engine, jd, birth_chart=None) -> str:
    """Render shadow mode markdown."""
    reds = engine.detect_red_zones(jd)
    sade = engine.compute_sade_sati(birth_chart) if birth_chart else {"active": False, "phase": "none", "guidance": ""}

    md = "# ASTRA Shadow Mode — Active Prohibitions\n\n"
    md += "| Severite | Fenetre | Regle | Raison |\n"
    md += "|----------|---------|-------|--------|\n"
    for r in reds:
        md += f"| {r['severity']} | {r['window']} | {r['rule']} | {r.get('reason', '-')} |\n"

    if sade["active"]:
        md += f"| WARN | ongoing | {sade['guidance']} | Sade Sati {sade['phase']} |\n"

    return md


def main():
    parser = argparse.ArgumentParser(description="ASTRA Daily Generator")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--force", action="store_true", help="Force regenerate")
    args, _ = parser.parse_known_args()

    base = Path(args.base_dir)
    engine = AstraEngine()
    jd = engine.jd_now()

    # Try to load birth chart
    birth_chart = None
    birth_path = base / "State" / "ASTRA_BIRTH.md"
    try:
        if birth_path.exists():
            # Parse birth data from markdown
            text = birth_path.read_text(encoding="utf-8")
            date_m = re.search(r"\*\*Birth date:\*\*\s*(\S+)", text)
            time_m = re.search(r"\*\*Birth time:\*\*\s*(\S+)", text)
            if date_m:
                date_str = date_m.group(1)
                parts = date_str.split("-")
                y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
                h, mi = 0, 0
                if time_m:
                    tparts = time_m.group(1).split(":")
                    h, mi = int(tparts[0]), int(tparts[1])
                chart = engine.compute_birth_chart(y, m, d, h, mi)
                dasha = engine.compute_vimshottari(chart["jd"])
                chart["dasha"] = dasha
                birth_chart = chart
    except Exception as e:
        print(f"Warning: could not load birth chart: {e}")

    # Generate ASTRA_DAILY.md
    daily_path = base / "State" / "ASTRA_DAILY.md"
    md = render_daily_md(engine, jd, birth_chart)
    daily_path.parent.mkdir(parents=True, exist_ok=True)
    daily_path.write_text(md, encoding="utf-8")
    print(f"Written: {daily_path}")

    # Generate ASTRA_SHADOW.md
    shadow_path = base / "State" / "ASTRA_SHADOW.md"
    shadow_md = render_shadow_md(engine, jd, birth_chart)
    shadow_path.write_text(shadow_md, encoding="utf-8")
    print(f"Written: {shadow_path}")

    print("ASTRA daily update complete.")


if __name__ == "__main__":
    main()
