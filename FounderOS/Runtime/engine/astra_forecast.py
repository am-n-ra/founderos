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
    """Print today's full forecast to stdout."""
    panch = engine.compute_panchanga(jd)
    horas = engine.compute_horas(jd)
    emotion = engine.emotional_forecast(jd)
    rahu = engine.rahu_kaal(jd)
    sun = engine.sunrise_sunset(jd)
    sade = engine.compute_sade_sati(birth_chart) if birth_chart else None
    reds = engine.detect_red_zones(jd)

    print(f"ASTRA Forecast — {engine.jd_to_date(jd)}")
    print("=" * 60)
    print(f"  Vara: {panch['vara']['name']} ({panch['vara']['graha']})")
    print(f"  Tithi: {panch['tithi']['name']} ({panch['tithi']['paksha']})")
    print(f"  Nakshatra: {panch['nakshatra']['name']} Pada {panch['nakshatra']['pada']}")
    print(f"  Lever: {sun['sunrise']} | Coucher: {sun['sunset']}")
    print()
    print(f"  Energie: {emotion['energy']}/100 | Focus: {emotion['focus']}/100")
    print(f"  Humeur: {emotion['mood']}/100 | Sociabilite: {emotion['sociability']}/100")
    print(f"  -> {emotion['mood_advice']}")
    print()
    if horas['active']:
        print(f"  Hora: {horas['active']['lord']} ({horas['active']['start']}-{horas['active']['end']})")
        print(f"  -> {horas['active']['guide']}")
    if rahu:
        tag = " [ACTIF]" if rahu['active'] else ""
        print(f"  Rahu Kaal: {rahu['start']}-{rahu['end']}{tag}")
    if reds:
        for r in reds:
            now_tag = " ⚠" if r.get("now") else ""
            print(f"  [{r['severity']}{now_tag}] {r['reason']}")
    if sade and sade['active']:
        print(f"  [SADE SATI] {sade['phase']}: {sade['guidance']}")
    print()
    types = ["signature", "negotiation", "launch", "deep_work", "content"]
    scores = [(t, engine.score_muhurta(jd, t)) for t in types]
    best = max(scores, key=lambda x: x[1])
    print(f"  Meilleur pour: {best[0]} ({best[1]}/100)")
    for t, s in sorted(scores, key=lambda x: -x[1]):
        print(f"    {t}: {s}/100")


def forecast_week(engine, jd):
    """Print 7-day forecast table."""
    print(f"ASTRA Weekly Forecast — starting {engine.jd_to_date(jd)}")
    print("=" * 68)
    print(f"{'Date':<14} {'Score':<8} {'Tithi':<14} {'Nakshatra':<14} {'Best Hora':<12}")
    print("-" * 68)
    for offset in range(7):
        d = jd + offset
        panch = engine.compute_panchanga(d)
        hrs = engine.compute_horas(d)
        score = 70
        if panch['tithi']['rikta']: score -= 10
        if panch['yoga']['favorable']: score += 10
        active_hora = hrs['active']['lord'] if hrs['active'] else '?'
        print(f"{engine.jd_to_date(d):<14} {score:<8} {panch['tithi']['name']:<14} {panch['nakshatra']['name']:<14} {active_hora:<12}")
    print()
    print("Top recommendations:")
    print("- Verrouiller les contrats avant Mercure Rx")
    print("- Meilleurs jours pour negociations: jeudi, vendredi")
    print("- Eviter les tithis Rikta")


def forecast_month(engine, jd):
    """Print 30-day landscape."""
    print(f"ASTRA 30-Day Landscape — {engine.jd_to_date(jd)} onward")
    print("=" * 70)
    for week_offset in range(4):
        week_start = jd + week_offset * 7
        print(f"\nSemaine {week_offset + 1} ({engine.jd_to_date(week_start)}):")
        for day_offset in range(7):
            d = week_start + day_offset
            panch = engine.compute_panchanga(d)
            score = 70
            if panch['tithi']['rikta']: score -= 10
            if panch['yoga']['favorable']: score += 10
            print(f"  {engine.jd_to_date(d):<12} {score:>3}/100 {panch['vara']['name']:<10} {panch['tithi']['name']:<12} {panch['nakshatra']['name']:<12}")


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

    if args.scope == "today":
        forecast_today(engine, jd, birth_chart)
    elif args.scope == "week":
        forecast_week(engine, jd)
    elif args.scope == "month":
        forecast_month(engine, jd)
    elif args.scope == "year":
        print("Year forecast: 12-month transit scan (Phase 3)")
    elif args.scope == "dasha":
        if birth_chart:
            d = birth_chart["dasha"]
            if d["current_md"]:
                print(f"Current MD: {d['current_md']['lord']} ({d['current_md']['start']} - {d['current_md']['end']})")
            if d["current_ad"]:
                print(f"Current AD: {d['current_ad']['lord']} ({d['current_ad'].get('start', '?')} - {d['current_ad'].get('end', '?')})")
            print(f"All MDs:")
            for md in d["dashas"]:
                print(f"  {md['lord']:<10} {md['start']} - {md['end']}  ({md['years']}yrs)")
        else:
            print("No birth chart found. Run astra_birth.py first.")


if __name__ == "__main__":
    main()
