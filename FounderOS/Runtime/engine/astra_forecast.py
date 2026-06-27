"""astra_forecast.py — On-demand forecast command.

Usage:
    python Runtime/engine/astra_forecast.py --base-dir . today
    python Runtime/engine/astra_forecast.py --base-dir . week
    python Runtime/engine/astra_forecast.py --base-dir . month
    python Runtime/engine/astra_forecast.py --base-dir . year
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure workspace root is on sys.path for direct script execution
_this_dir = Path(__file__).resolve().parent
_workspace_root = _this_dir.parent.parent
if str(_workspace_root) not in sys.path:
    sys.path.insert(0, str(_workspace_root))

from Runtime.engine.astra_core import AstraEngine


def forecast_today(engine, jd, birth_chart=None):
    """Print today's full forecast to stdout and return markdown."""
    panch = engine.compute_panchanga(jd)
    horas = engine.compute_horas(jd)
    emotion = engine.emotional_forecast(jd)
    rahu = engine.rahu_kaal(jd)
    sun = engine.sunrise_sunset(jd)
    sade = engine.compute_sade_sati(birth_chart) if birth_chart else None
    reds = engine.detect_red_zones(jd)

    out = []
    out.append(f"ASTRA Forecast — {engine.jd_to_date(jd)}")
    out.append("=" * 60)
    out.append(f"  Vara: {panch['vara']['name']} ({panch['vara']['graha']})")
    out.append(f"  Tithi: {panch['tithi']['name']} ({panch['tithi']['paksha']})")
    out.append(f"  Nakshatra: {panch['nakshatra']['name']} Pada {panch['nakshatra']['pada']}")
    out.append(f"  Lever: {sun['sunrise']} | Coucher: {sun['sunset']}")
    out.append("")
    out.append(f"  Energie: {emotion['energy']}/100 | Focus: {emotion['focus']}/100")
    out.append(f"  Humeur: {emotion['mood']}/100 | Sociabilite: {emotion['sociability']}/100")
    out.append(f"  -> {emotion['mood_advice']}")
    out.append("")
    if horas['active']:
        out.append(f"  Hora: {horas['active']['lord']} ({horas['active']['start']}-{horas['active']['end']})")
        out.append(f"  -> {horas['active']['guide']}")
    if rahu:
        tag = " [ACTIF]" if rahu['active'] else ""
        out.append(f"  Rahu Kaal: {rahu['start']}-{rahu['end']}{tag}")
    if reds:
        for r in reds:
            now_tag = " ⚠" if r.get("now") else ""
            out.append(f"  [{r['severity']}{now_tag}] {r['reason']}")
    if sade and sade['active']:
        out.append(f"  [SADE SATI] {sade['phase']}: {sade['guidance']}")
    out.append("")
    types = ["signature", "negotiation", "launch", "deep_work", "content"]
    scores = [(t, engine.score_muhurta(jd, t)) for t in types]
    best = max(scores, key=lambda x: x[1])
    out.append(f"  Meilleur pour: {best[0]} ({best[1]}/100)")
    for t, s in sorted(scores, key=lambda x: -x[1]):
        out.append(f"    {t}: {s}/100")

    for line in out:
        print(line)

    md = f"## Today ({engine.jd_to_date(jd)})\n\n" + "\n".join(out)
    return md


def forecast_week(engine, jd):
    """Print 7-day forecast table and return markdown."""
    out = []
    out.append(f"ASTRA Weekly Forecast — starting {engine.jd_to_date(jd)}")
    out.append("=" * 68)
    out.append(f"{'Date':<14} {'Score':<8} {'Tithi':<14} {'Nakshatra':<14} {'Best Hora':<12}")
    out.append("-" * 68)
    for offset in range(7):
        d = jd + offset
        panch = engine.compute_panchanga(d)
        hrs = engine.compute_horas(d)
        score = 70
        if panch['tithi']['rikta']: score -= 10
        if panch['yoga']['favorable']: score += 10
        active_hora = hrs['active']['lord'] if hrs['active'] else '?'
        out.append(f"{engine.jd_to_date(d):<14} {score:<8} {panch['tithi']['name']:<14} {panch['nakshatra']['name']:<14} {active_hora:<12}")
    out.append("")
    out.append("Top recommendations:")
    out.append("- Verrouiller les contrats avant Mercure Rx")
    out.append("- Meilleurs jours pour negociations: jeudi, vendredi")
    out.append("- Eviter les tithis Rikta")

    for line in out:
        print(line)

    md = f"## Week ({engine.jd_to_date(jd)} to {engine.jd_to_date(jd + 6)})\n\n" + "\n".join(out)
    return md


def forecast_month(engine, jd):
    """Print 30-day landscape and return markdown."""
    out = []
    out.append(f"ASTRA 30-Day Landscape — {engine.jd_to_date(jd)} onward")
    out.append("=" * 70)
    for week_offset in range(4):
        week_start = jd + week_offset * 7
        out.append(f"\nSemaine {week_offset + 1} ({engine.jd_to_date(week_start)}):")
        for day_offset in range(7):
            d = week_start + day_offset
            panch = engine.compute_panchanga(d)
            score = 70
            if panch['tithi']['rikta']: score -= 10
            if panch['yoga']['favorable']: score += 10
            out.append(f"  {engine.jd_to_date(d):<12} {score:>3}/100 {panch['vara']['name']:<10} {panch['tithi']['name']:<12} {panch['nakshatra']['name']:<12}")

    for line in out:
        print(line)

    md = f"## Month ({engine.jd_to_date(jd)} onward)\n\n" + "\n".join(out)
    return md


def forecast_year(engine, jd):
    """Print 12-month transit scan to stdout and return markdown."""
    out = []
    out.append(f"ASTRA Yearly Forecast — {engine.jd_to_date(jd)} to {engine.jd_to_date(jd + 365)}")
    out.append("=" * 70)
    for month_offset in range(12):
        month_start = jd + month_offset * 30
        out.append("")
        out.append(f"Mois {month_offset + 1} ({engine.jd_to_date(month_start)}):")
        for day_offset in range(0, 30, 7):
            d = month_start + day_offset
            panch = engine.compute_panchanga(d)
            score = 70
            if panch['tithi']['rikta']: score -= 10
            if panch['yoga']['favorable']: score += 10
            out.append(f"  {engine.jd_to_date(d):<12} {score:>3}/100 {panch['vara']['name']:<10} {panch['tithi']['name']:<12}")
    out.append("")
    out.append("Year overview:")
    out.append("- 12-month transit scan")

    for line in out:
        print(line)

    md = f"## Year ({engine.jd_to_date(jd)} to {engine.jd_to_date(jd + 365)})\n\n" + "\n".join(out)
    return md


def forecast_dasha(engine, jd, birth_chart):
    """Print Vimshottari Dasha info to stdout and return markdown."""
    out = []
    d = birth_chart["dasha"]
    if d["current_md"]:
        out.append(f"Current MD: {d['current_md']['lord']} ({d['current_md']['start']} - {d['current_md']['end']})")
    if d["current_ad"]:
        out.append(f"Current AD: {d['current_ad']['lord']} ({d['current_ad'].get('start', '?')} - {d['current_ad'].get('end', '?')})")
    out.append("All MDs:")
    for m in d["dashas"]:
        out.append(f"  {m['lord']:<10} {m['start']} - {m['end']}  ({m['years']}yrs)")

    for line in out:
        print(line)

    md = f"## Dasha Timeline\n\n" + "\n".join(out)
    return md


def main():
    parser = argparse.ArgumentParser(description="ASTRA Forecast")
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("scope", nargs="?", default="today",
                        choices=["today", "week", "month", "year", "dasha"])
    args = parser.parse_args()

    engine = AstraEngine()
    jd = engine.jd_now()

    # Load birth chart if available
    birth_chart = None
    birth_path = Path(args.base_dir) / "State" / "ASTRA_BIRTH.md"
    try:
        if birth_path.exists():
            import re
            text = birth_path.read_text(encoding="utf-8")
            date_m = re.search(r"\*\*Birth date:\*\*\s*(\S+)", text)
            time_m = re.search(r"\*\*Birth time:\*\*\s*(\S+)", text)
            if date_m:
                parts = date_m.group(1).split("-")
                y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
                h, mi = 0, 0
                if time_m:
                    tparts = time_m.group(1).split(":")
                    h, mi = int(tparts[0]), int(tparts[1])
                chart = engine.compute_birth_chart(y, m, d, h, mi)
                chart["dasha"] = engine.compute_vimshottari(chart["jd"])
                birth_chart = chart
    except Exception as e:
        print(f"(no birth chart: {e})")

    md_content = None
    if args.scope == "today":
        md_content = forecast_today(engine, jd, birth_chart)
    elif args.scope == "week":
        md_content = forecast_week(engine, jd)
    elif args.scope == "month":
        md_content = forecast_month(engine, jd)
    elif args.scope == "year":
        md_content = forecast_year(engine, jd)
    elif args.scope == "dasha":
        if birth_chart:
            md_content = forecast_dasha(engine, jd, birth_chart)
        else:
            print("No birth chart found. Run astra_birth.py first.")
            md_content = "## Dasha Timeline\n\nNo birth chart found."

    if md_content:
        fore_path = Path(args.base_dir) / "State" / "ASTRA_FORECAST.md"
        fore_path.parent.mkdir(parents=True, exist_ok=True)
        full_md = f"# ASTRA FORECAST\n\n{md_content}\n\n---\n*Generated by astra_forecast.py at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}*"
        fore_path.write_text(full_md, encoding="utf-8")
        print(f"Written: {fore_path}")


if __name__ == "__main__":
    main()
