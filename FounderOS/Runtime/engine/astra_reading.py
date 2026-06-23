"""astra_reading.py — Generate ASTRA_READING_RAW.md narrative interpretation.

Reads ASTRA_BIRTH.md and produces a 7-section narrative reading.

Usage:
    python Runtime/engine/astra_reading.py --base-dir .
"""

import argparse
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


# ── Interpretation Dictionaries ──────────────────────────────────────────

RASHI_MEANING = {
    "Belier": "Aries — impulsif, leader, pioneer. Maison de Mangala.",
    "Taureau": "Taurus — stable, patient, materiel. Maison de Shukra.",
    "Gemeaux": "Gemini — adaptable, communicatif, curieux. Maison de Budha.",
    "Cancer": "Cancer — sensible, protecteur, intuitif. Maison de Chandra.",
    "Lion": "Leo — creatif, autoritaire, genereux. Maison de Surya.",
    "Vierge": "Virgo — analytique, precis, serviable. Maison de Budha.",
    "Balance": "Libra — equilibre, diplomate, esthetique. Maison de Shukra.",
    "Scorpion": "Scorpio — intense, transformateur, puissant. Maison de Mangala.",
    "Sagittaire": "Sagittarius — expansif, philosophe, aventureux. Maison de Guru.",
    "Capricorne": "Capricorn — discipline, ambitieux, perseverant. Maison de Shani.",
    "Verseau": "Aquarius — original, humanitaire, independant. Maison de Shani.",
    "Poissons": "Pisces — spirituel, artiste, compatissant. Maison de Guru.",
}

NAKSHATRA_MEANING = {
    "Ashwini": ("Les cavaliers", "Vitesse, guerison, initiative"),
    "Bharani": ("Le porteur", "Transformation, naissance, karma"),
    "Krittika": ("Le couteau", "Precision, courage, discernement"),
    "Rohini": ("La rouge", "Creativite, beaute, abondance"),
    "Mrigashira": ("La tête de cerf", "Recherche, curiosite, douceur"),
    "Ardra": ("La larme", "Tempete, transformation, verite"),
    "Punarvasu": ("Le retour de la lumiere", "Renouveau, compassion, foi"),
    "Pushya": ("La nourriture", "Nourrir, protege, stabilite"),
    "Ashlesha": ("L'enlacement", "Intuition, pouvoir cache, kundalini"),
    "Magha": ("Le puissant", "Autorite, ancetres, noblesse"),
    "Purva Phalguni": ("Le figuier", "Plaisir, jeunesse, romance"),
    "Uttara Phalguni": ("Le figuier tardif", "Mariage, partenariat, prosperite"),
    "Hasta": ("La main", "Adresse, artisanat, precision"),
    "Chitra": ("La perle brillante", "Esthetique, design, opportunites"),
    "Swati": ("Le corail", "Independance, equilibre, autonomie"),
    "Vishakha": ("La branche fourchue", "Determination, rayonnement, competition"),
    "Anuradha": ("La disciple", "Devotion, succes, resilience"),
    "Jyeshtha": ("L'ainee", "Protection, autorite, ego"),
    "Mula": ("La racine", "Destruction, transformation, enquete"),
    "Purva Ashadha": ("La victorieuse", "Victoire, resurgence, pouvoir"),
    "Uttara Ashadha": ("La tardive victorieuse", "Perseverance, stabilite, triomphe"),
    "Shravana": ("L'ecoute", "Apprentissage, ecoute, sagesse"),
    "Dhanishta": ("La plus riche", "Musique, richesse, prosperite"),
    "Shatabhisha": ("Les cent guerisseurs", "Guerison, mystere, recherche"),
    "Purva Bhadrapada": ("Le feu purifiant", "Transformation, spiritualite, dualite"),
    "Uttara Bhadrapada": ("Le guerisseur tardif", "Profondeur, fermeture, guerison"),
    "Revati": ("L'abondante", "Voyage, protection, fin de cycle"),
}

HOUSE_MEANING = {
    1: ("Soi-meme, personnalite, debut de vie", "La maison de l'identite. Si activee: forte volonte, leadership."),
    2: ("Finances, famille, parole", "Ressources materielles et securite."),
    3: ("Communication, courage, fratrie", "Expression, initiatives, deplacement."),
    4: ("Foyer, mere, emotions", "Racines, bonheur interieur, immobilier."),
    5: ("Creativite, enfants, intelligence", "Expression personnelle, education, romance."),
    6: ("Sante, service, conflits", "Defis, routines quotidiennes, guerison."),
    7: ("Partenariat, mariage, contrats", "Relations, affaires, associations."),
    8: ("Transformation, heritages, mysteres", "Crise, regeneration, recherche."),
    9: ("Fortune, spiritualite, voyages", "Guru, chance, etudes superieures."),
    10: ("Carriere, reputation, autorite", "Karma professionnel, statut social."),
    11: ("Revenus, reseau, aspirations", "Gains, cercles sociaux, amities."),
    12: ("Solitude, spiritualite, pertes", "Retraite, karma, liberation."),
}

GRAHA_THEMES = {
    "Surya": "Soleil — identite, autorite, vitalite, pere",
    "Chandra": "Lune — emotions, intuition, mere, mental",
    "Mangala": "Mars — action, courage, competition, conflits",
    "Budha": "Mercure — communication, commerce, intelligence, jeunesse",
    "Guru": "Jupiter — sagesse, expansion, richesse, spiritualite",
    "Shukra": "Venus — amour, beaute, confort, arts",
    "Shani": "Saturne — discipline, karma, limitations, temps",
    "Rahu": "Rahu Nord — ambition, desir, materiel, illusions",
    "Ketu": "Ketu Sud — spiritualite, detachement, karma passe",
}

YOGA_INTERPRETATIONS = {
    "Budha-Aditya Yoga": "Soleil et Mercure conjoints dans le meme signe. Intelligence aigue, eloquence, succes en communication.",
    "Gaja-Kesari Yoga": "Jupiter en Kendra de la Lune. Sagesse, autorite, respect, chance.",
    "Chandra-Mangala Yoga": "Lune et Mars conjoints. Passion, courage, leadership, mais impulsivite.",
}

SADE_SATI_GUIDE = {
    "rising": "Saturne s'approche de ta Lune natale. Periode de retrait, d'epuration. Elimine ce qui ne te sert plus. N'entreprends pas de nouvelles expansions.",
    "peak": "Saturne sur ta Lune. Periode intense de karma et de transformations. Lecons.",
    "declining": "Saturne s'eloigne. Reconstruction. Les fruits des efforts commencent a montrer.",
}

RASHI_LIST = [
    "Belier", "Taureau", "Gemeaux", "Cancer", "Lion", "Vierge",
    "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons",
]

DASHA_NARRATIVE = {
    "Rahu": "Ambition, desirs materiels, percées, mais illusions.",
    "Guru": "Croissance, sagesse, expansion, spiritualite.",
    "Shani": "Discipline, karma, patience, lecons de vie.",
    "Surya": "Identite, vitalite, leadership, reconnaissance.",
    "Chandra": "Emotions, famille, intuition, nourriture.",
    "Mangala": "Action, courage, conflits, initiatives.",
    "Budha": "Communication, affaires, reseau, apprentissage.",
    "Shukra": "Amour, beaute, confort, arts, relations.",
    "Ketu": "Spiritualite, detachement, karma passe, retrait.",
}

GRAHA_ORDER = [
    "Surya", "Chandra", "Mangala", "Budha", "Guru", "Shukra", "Shani", "Rahu", "Ketu",
]


def parse_birth_md(path) -> dict:
    """Parse ASTRA_BIRTH.md and return structured birth chart dict."""
    text = Path(path).read_text(encoding="utf-8")

    birth_data = {}
    date_m = re.search(r"\*\*Birth date:\*\*\s*(\S+)", text)
    time_m = re.search(r"\*\*Birth time:\*\*\s*(\S+)", text)
    loc_m = re.search(r"\*\*Location:\*\*\s*(\S+)", text)
    if date_m:
        birth_data["date"] = date_m.group(1)
    if time_m:
        birth_data["time"] = time_m.group(1)
    if loc_m:
        birth_data["location"] = loc_m.group(1)

    lagna = {}
    sign_m = re.search(r"\*\*Sign:\*\*\s*(\w+)\s*\(([\d.]+)deg\)", text)
    if sign_m:
        lagna["rashi"] = sign_m.group(1)
        lagna["deg"] = float(sign_m.group(2))
    nak_m = re.search(r"\*\*Nakshatra:\*\*\s*(.+?)\s*[—\-]\s*Pada\s*(\d+)", text)
    if nak_m:
        lagna["nakshatra"] = nak_m.group(1).strip()
        lagna["nakshatra_pada"] = int(nak_m.group(2))
    lord_m = re.search(r"\*\*Nakshatra Lord:\*\*\s*(\w+)", text)
    if lord_m:
        lagna["nakshatra_lord"] = lord_m.group(1)

    grahas = {}
    in_graha = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("| Graha |"):
            in_graha = True
            continue
        if stripped.startswith("|---"):
            continue
        if in_graha and stripped.startswith("|"):
            parts = [p.strip() for p in stripped.split("|")]
            if len(parts) >= 9:
                name = parts[1]
                rashi = parts[2]
                deg = float(parts[3])
                nak = parts[4]
                pada = int(parts[5])
                nak_lord = parts[6]
                house = int(parts[7])
                retro = parts[8] == "R"
                rashi_i = RASHI_LIST.index(rashi) if rashi in RASHI_LIST else 0
                lon_approx = rashi_i * 30 + deg
                grahas[name] = {
                    "rashi": rashi, "rashi_deg": deg, "lon": lon_approx,
                    "nakshatra": nak, "nakshatra_pada": pada,
                    "nakshatra_lord": nak_lord, "house": house,
                    "retrograde": retro,
                }
        elif in_graha and not stripped.startswith("|"):
            in_graha = False

    house_lords = {}
    in_hl = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("| House |"):
            in_hl = True
            continue
        if stripped.startswith("|---"):
            continue
        if in_hl and stripped.startswith("|"):
            parts = [p.strip() for p in stripped.split("|")]
            if len(parts) >= 3:
                house_lords[parts[1]] = parts[2]
        elif in_hl and not stripped.startswith("|"):
            in_hl = False

    dasha = {"dashas": []}
    md_m = re.search(r"\*\*Mahadasha:\*\*\s*(\w+)", text)
    if md_m:
        dasha["current_md"] = {"lord": md_m.group(1)}
    start_m = re.search(r"\*\*Start:\*\*\s*(\S+)", text)
    if start_m:
        dasha.setdefault("current_md", {})["start"] = start_m.group(1)
    end_m = re.search(r"\*\*End:\*\*\s*(\S+)", text)
    if end_m:
        dasha.setdefault("current_md", {})["end"] = end_m.group(1)
    ad_m = re.search(r"\*\*Antar Dasha:\*\*\s*(\w+)", text)
    if ad_m:
        dasha["current_ad"] = {"lord": ad_m.group(1)}

    in_dt = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("| Lord | Level |"):
            in_dt = True
            continue
        if stripped.startswith("|---"):
            continue
        if in_dt and stripped.startswith("|"):
            parts = [p.strip() for p in stripped.split("|")]
            if len(parts) >= 6:
                dasha["dashas"].append({
                    "lord": parts[1], "start": parts[3],
                    "end": parts[4], "years": float(parts[5]),
                })
        elif in_dt and not stripped.startswith("|"):
            in_dt = False

    sade_sati = {"active": False, "phase": "none", "guidance": ""}
    sade_status_m = re.search(r"\*\*Status:\*\*\s*(.+)", text)
    sade_guide_m = re.search(r"\*\*Guidance:\*\*\s*(.+)", text)
    if sade_status_m:
        sade_sati["active"] = True
        sade_sati["phase"] = sade_status_m.group(1).strip()
    if sade_guide_m:
        sade_sati["guidance"] = sade_guide_m.group(1).strip()

    yogas = []
    yogas_section = re.search(
        r"## Yogas \(Auto-Detected\)\n(.+?)(?=\n##|\Z)", text, re.DOTALL
    )
    if yogas_section:
        for ym in re.finditer(r"\*\*(.+?):\*\*\s*(.+)", yogas_section.group(1)):
            yogas.append([ym.group(1), ym.group(2).strip()])

    return {
        "birth_data": birth_data,
        "lagna": lagna,
        "grahas": grahas,
        "house_lords": house_lords,
        "dasha": dasha,
        "sade_sati": sade_sati,
        "yogas": yogas,
    }


def generate_reading(engine, chart) -> str:
    """Generate 7-section narrative reading markdown."""
    lagna = chart["lagna"]
    grahas = chart["grahas"]
    house_lords = chart["house_lords"]
    dasha = chart["dasha"]
    sade_sati = chart["sade_sati"]
    yogas = chart["yogas"]
    birth_data = chart["birth_data"]
    now = datetime.now(timezone.utc)
    current_md = dasha.get("current_md", {})
    current_md_lord = current_md.get("lord", "?")
    dashas = dasha.get("dashas", [])

    md = f"""# ASTRA Reading — Narrative Interpretation

> Generated from ASTRA_BIRTH.md at {now.strftime('%Y-%m-%d %H:%M')} UTC
> Birth: {birth_data.get('date', '?')} at {birth_data.get('time', '?')}, {birth_data.get('location', '?')}

"""

    # ── Section 1: Lagna Profile ──────────────────────────────────────
    rashi_name = lagna.get("rashi", "?")
    nak_name = lagna.get("nakshatra", "?")
    nak_lord = lagna.get("nakshatra_lord", "?")
    rashi_desc = RASHI_MEANING.get(rashi_name, "")
    nak_info = NAKSHATRA_MEANING.get(nak_name, ("", ""))

    md += f"""## Section 1 : Lagna Profile

**{rashi_name}** — {rashi_desc}

Le Lagna (Ascendant) est le signe qui se levait a l'Est au moment de ta naissance.
Il definit le filtre a travers lequel tu vis le monde — ton corps, ton approche, ton debut de vie.

**Nakshatra:** {nak_name} — {nak_info[0]}
**Themes:** {nak_info[1]}
**Seigneur du Nakshatra:** {nak_lord} — {GRAHA_THEMES.get(nak_lord, '')}

"""
    if grahas.get("Guru", {}).get("house") == 1:
        md += ":star: **Guru (Jupiter) en Lagna** — Sagesse, optimisme, protection naturelle. Presence benefique qui attire la chance et la confiance des autres.\n\n"

    # ── Section 2: House-by-House ─────────────────────────────────────
    md += "## Section 2 : Maison par Maison\n\n"
    for h_num in range(1, 13):
        h_key = f"H{h_num}"
        domain, desc = HOUSE_MEANING[h_num]
        lord = house_lords.get(h_key, "?")
        lord_desc = GRAHA_THEMES.get(lord, "")
        planets_in_house = [
            name for name in GRAHA_ORDER
            if grahas.get(name, {}).get("house") == h_num
        ]
        if planets_in_house:
            parts = []
            for p in planets_in_house:
                pdesc = GRAHA_THEMES.get(p, "")
                parts.append(f"{p} ({pdesc})")
            planets_text = " **Grahas presentes:** " + ", ".join(parts) + "."
        else:
            planets_text = " Aucun graha en residence."

        md += f"""**Maison {h_num}:** {domain}
{desc}
**Seigneur:** {lord} — {lord_desc}.{planets_text}

"""

    # ── Section 3: Yogas ──────────────────────────────────────────────
    md += "## Section 3 : Yogas\n\n"
    if yogas:
        for yoga_name, yoga_brief in yogas:
            interpretation = YOGA_INTERPRETATIONS.get(yoga_name, yoga_brief)
            md += f"""**{yoga_name}**
{interpretation}

"""
    else:
        md += "Aucun yoga majeur detecte dans le D1 (chart natal). Cela signifie que les energies sont relativement independantes — chaque graha opere sans combinaison exceptionnelle.\n\n"

    # ── Section 4: Dasha Arc ──────────────────────────────────────────
    md += "## Section 4 : Arc Dasha\n\nLa Vimshottari Dasha est le cycle planetaire de 120 ans. Chaque Mahadasha (MD) est gouvernee par un graha qui imprime son theme sur une periode de ta vie.\n\n### Dashas passes\n"
    found_current = False
    for d in dashas:
        if d.get("lord") == current_md_lord and not found_current:
            found_current = True
            continue
        if not found_current:
            theme = GRAHA_THEMES.get(d["lord"], d["lord"])
            md += f"- **{d['lord']}** ({d.get('start', '?')} - {d.get('end', '?')}): {theme}\n"

    md += f"""
### Dasha actuelle
**{current_md_lord}** ({current_md.get('start', '?')} - {current_md.get('end', '?')})
{GRAHA_THEMES.get(current_md_lord, '')}

Le Mahadasha de {current_md_lord} est la toile de fond de ta vie actuelle. {DASHA_NARRATIVE.get(current_md_lord, '')}

"""
    current_ad = dasha.get("current_ad", {})
    if current_ad:
        md += f"""### Antar Dasha actuel
**{current_ad.get('lord', '?')}** (sous-periode)
{GRAHA_THEMES.get(current_ad.get('lord', ''), '')}

L'Antar Dasha affine le theme du Mahadasha. {current_ad.get('lord', '?')} apporte ses energies specifiques dans le cadre general de {current_md_lord}.

"""
    next_lord = None
    found_current = False
    for d in dashas:
        if d.get("lord") == current_md_lord:
            found_current = True
            continue
        if found_current:
            next_lord = d
            break
    if next_lord:
        md += f"""### Prochaine Dasha
**{next_lord['lord']}** (a partir de {next_lord.get('start', '?')})
{GRAHA_THEMES.get(next_lord['lord'], '')}

"""

    # ── Section 5: Sade Sati ──────────────────────────────────────────
    md += "## Section 5 : Sade Sati\n\nSade Sati est la phase de 7.5 ans ou Saturne transite les 12e, 1re et 2e maisons depuis la Lune natale. C'est un cycle de karma, discipline et transformation.\n\n"
    if sade_sati.get("active", False):
        phase_raw = sade_sati.get("phase", "")
        if "rising" in phase_raw or "12e" in phase_raw:
            phase_key = "rising"
        elif "peak" in phase_raw or "sur la" in phase_raw:
            phase_key = "peak"
        elif "declining" in phase_raw or "2e" in phase_raw:
            phase_key = "declining"
        else:
            phase_key = None
        if phase_key:
            md += f"""**Phase active:** {sade_sati.get('phase', '?')}

{SADE_SATI_GUIDE.get(phase_key, sade_sati.get('guidance', ''))}
"""
        else:
            md += f"{sade_sati.get('guidance', 'Sade Sati active.')}\n"
    else:
        md += "Sade Sati n'est pas active actuellement.\n"
    md += "\n"

    # ── Section 6: Current Sky ────────────────────────────────────────
    md += "## Section 6 : Ciel Actuel\n\nTransits du jour compares a ton chart natal.\n\n"
    now_jd = engine.jd_now()
    current_positions = engine.all_grahas(now_jd)

    for graha_name in GRAHA_ORDER:
        natal = grahas.get(graha_name)
        current = current_positions.get(graha_name)
        if not natal or not current:
            continue
        natal_rashi = natal.get("rashi", "?")
        curr_rashi = current.get("rashi", "?")
        aspects = ""
        if natal_rashi == curr_rashi:
            aspects += " [CONJONCTION NATALE — energie natal activee]"
        if natal_rashi in RASHI_LIST and curr_rashi in RASHI_LIST:
            natal_i = RASHI_LIST.index(natal_rashi)
            curr_i = RASHI_LIST.index(curr_rashi)
            dist = (curr_i - natal_i) % 12
            if dist == 6:
                aspects += " [OPPOSITION — tension, prise de conscience]"
            elif dist in (4, 8):
                aspects += " [TRIGONE — soutien harmonieux]"
            elif dist in (3, 9):
                aspects += " [QUADRATURE — defi, friction]"
        retro = " (R)" if current.get("retrograde") else ""
        md += f"- **{graha_name}**: {natal_rashi} natal -> {curr_rashi} actuel{retro}{aspects}\n"
    md += "\n"

    # ── Section 7: Summary ────────────────────────────────────────────
    md += "## Section 7 : Resume\n\n### Forces principales\n"
    strengths = []
    if grahas.get("Guru", {}).get("house") == 1:
        strengths.append("Jupiter en Lagna — sagesse naturelle, protection, chance")
    tenth_planets = [n for n in GRAHA_ORDER if grahas.get(n, {}).get("house") == 10]
    if tenth_planets:
        strengths.append(f"Grahas en Maison 10 ({', '.join(tenth_planets)}) — forte carriere, visibilite")
    sun_rashi = grahas.get("Surya", {}).get("rashi")
    mer_rashi = grahas.get("Budha", {}).get("rashi")
    if sun_rashi and mer_rashi and sun_rashi == mer_rashi:
        strengths.append("Budha-Aditya Yoga — intelligence aigue, eloquence, communication puissante")
    guru_house = grahas.get("Guru", {}).get("house")
    chandra_house = grahas.get("Chandra", {}).get("house")
    if guru_house and chandra_house:
        dist = abs(guru_house - chandra_house) % 12
        if dist in (0, 4, 8):
            strengths.append("Gaja-Kesari Yoga — sagesse, autorite, respect, chance protegee")
    if grahas.get("Mangala", {}).get("rashi") == grahas.get("Chandra", {}).get("rashi"):
        strengths.append("Chandra-Mangala Yoga — passion, courage, leadership equilibre")
    if not strengths:
        strengths.append("Resilience et capacite d'adaptation")

    for s in strengths:
        md += f"- {s}\n"

    md += "\n### Defis principaux\n"
    challenges = []
    for h in (6, 8, 12):
        shani_house = grahas.get("Shani", {}).get("house")
        if shani_house == h:
            challenges.append(f"Shani en maison {h} — discipline forcee, detachement, isolement")
        rahu_house = grahas.get("Rahu", {}).get("house")
        if rahu_house == h:
            challenges.append(f"Rahu en maison {h} — illusions, confusions, karmas non resolus")
    rx_names = [n for n in GRAHA_ORDER if grahas.get(n, {}).get("retrograde")]
    if rx_names:
        challenges.append(f"Retrogrades ({', '.join(rx_names)}) — energies interiorisees, karma en revision")
    if not challenges:
        challenges.append("Vigilance sur les periodes de Mercure retrograde et Rahu Kaal")

    for c in challenges:
        md += f"- {c}\n"

    md += f"""
### Meilleur timing
- **Dasha actuelle:** {current_md_lord} — le moment est aligne avec ce theme
- **Sade Sati:** {'Active — periode de transformation profonde' if sade_sati.get('active') else 'Inactive — cycle neutre'}
- **Check quotidien:** `python Runtime/engine/astra_daily.py --base-dir .` pour le muhurta du jour

---
*ASTRA Reading — Generated by astra_reading.py at {now.strftime('%Y-%m-%d %H:%M')} UTC*
"""

    return md


def main():
    parser = argparse.ArgumentParser(description="ASTRA Narrative Reading Generator")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    args = parser.parse_args()

    base = Path(args.base_dir)
    engine = AstraEngine()

    birth_path = base / "State" / "ASTRA_BIRTH.md"
    if not birth_path.exists():
        print(f"Error: {birth_path} not found. Run astra_birth.py first.")
        sys.exit(1)

    chart = parse_birth_md(str(birth_path))
    print("Birth chart parsed.")

    md = generate_reading(engine, chart)

    output_path = base / "State" / "ASTRA_READING_RAW.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md, encoding="utf-8")
    print(f"Written: {output_path}")
    print("ASTRA reading complete.")


if __name__ == "__main__":
    main()
