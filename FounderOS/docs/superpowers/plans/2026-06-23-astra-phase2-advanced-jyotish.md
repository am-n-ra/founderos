# ASTRA Phase 2 — Advanced Jyotish Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Upgrade ASTRA from basic Jyotish to an advanced engine with full Yogas detection (Dhana/Raja/Viparita), Ashtakavarga, extended Muhurta (15+ event types), Vargas D9/D10/D60, and Shadbala (sixfold strength).

**Architecture:** Add computation methods to `astra_core.py` as stateless functions on `AstraEngine`. Update `astra_birth.py` to include new birth chart data (Yogas, Vargas). Update `astra_daily.py` for new Muhurta types + Ashtakavarga transit check. Update `astra_reading.py` for new narrative sections. All state files remain pure Markdown.

**Tech Stack:** Python 3.13, pysweph v2.10.3.6 (Moshier ephemeris, Lahiri ayanamsa), no new dependencies.

**Plan location:** `docs/superpowers/plans/2026-06-23-astra-phase2-advanced-jyotish.md`

---
## File Structure

### Modified files:
- `Runtime/engine/astra_core.py` — Add ~20 new methods (Yogas, Ashtakavarga, Vargas, Shadbala) + extended EVENT_MUHURTA
- `Runtime/engine/astra_birth.py` — Expand birth Markdown with Yogas section (detailed), Vargas tables, Shadbala summary
- `Runtime/engine/astra_daily.py` — Include Ashtakavarga transit guidance in daily, new Muhurta event types
- `Runtime/engine/astra_reading.py` — Add 3 new narrative sections (Ashtakavarga, Vargas, Shadbala)

### New files:
- (none — all additions go into existing files)

---

### Task 1: Extended Yogas Detection (Dhana, Raja, Viparita, Sankha, Kalpadruma, etc.)

**Files:**
- Modify: `Runtime/engine/astra_core.py` (add `detect_d1_yogas()` method)
- Modify: `Runtime/engine/astra_birth.py` (expand Yogas section in Markdown)
- Modify: `Runtime/engine/astra_reading.py` (richer Yogas interpretation)

- [ ] **Step 1: Add YOGA_DEFINITIONS constant + detect_d1_yogas() to astra_core.py**

After line 75 (HOUSE_LORD_MAP), add yoga category constants:

```python
# ── Yoga Definitions ──────────────────────────────────────────────────

# Raja Yogas: Lords of Kendra (1,4,7,10) + Kona (1,5,9) in mutual Kendra/Kona
# Dhana Yogas: Lords of 2nd, 11th, 5th, 9th in mutual connection
# Viparita Raja Yoga: Lords of 6th, 8th, 12th in own/trine houses

RAJA_YOGA_KENDRA = {1, 4, 7, 10}
RAJA_YOGA_KONA = {1, 5, 9}
DHANA_HOUSES = {2, 5, 9, 11}
VIPARITA_HOUSES = {6, 8, 12}
TRIKONA_HOUSES = {1, 5, 9}
KENDRA_HOUSES = {1, 4, 7, 10}
TRIK_HOUSES = {6, 8, 12}
```

- [ ] **Step 2: Add the detect_d1_yogas() method to AstraEngine class**

After the `compute_birth_chart` method, add:

```python
    # ── Yoga Detection ────────────────────────────────────────────────

    def detect_d1_yogas(self, birth_chart: dict) -> list:
        """Detect all major Yogas from D1 birth chart. Returns list of (name, description, strength)."""
        grahas = birth_chart["grahas"]
        house_lords = birth_chart["house_lords"]
        asc_lon = birth_chart["lagna"]["lon"]
        asc_sign = int(asc_lon / 30)
        yogas = []

        # Helper: get lord of a house number
        def lord_of(h_num):
            sign = (asc_sign + h_num - 1) % 12
            return HOUSE_LORD_MAP[sign]

        # Helper: which house is a graha in
        def house_of(graha_name):
            g = grahas.get(graha_name)
            return g["house"] if g else None

        # Helper: rashi index of a graha
        def rashi_of(graha_name):
            g = grahas.get(graha_name)
            return int(g["lon"] / 30) if g else None

        # ── 1. Budha-Aditya Yoga (Sun + Mercury in same sign) ──
        if grahas.get("Surya") and grahas.get("Budha"):
            if rashi_of("Surya") == rashi_of("Budha"):
                yogas.append(("Budha-Aditya Yoga",
                    "Soleil et Mercure conjoints. Intelligence aigue, eloquence, succes en communication, commerce.",
                    "strong"))

        # ── 2. Gaja-Kesari Yoga (Jupiter in Kendra from Moon) ──
        if grahas.get("Chandra") and grahas.get("Guru"):
            moon_h = house_of("Chandra")
            guru_h = house_of("Guru")
            if moon_h and guru_h:
                dist = (guru_h - moon_h) % 12
                if dist == 0 or dist == 4 or dist == 8:
                    yogas.append(("Gaja-Kesari Yoga",
                        "Jupiter en Kendra de la Lune. Sagesse, autorite, respect, chance protegee, reconnaissance.",
                        "strong"))

        # ── 3. Chandra-Mangala Yoga (Moon + Mars in same sign) ──
        if grahas.get("Chandra") and grahas.get("Mangala"):
            if rashi_of("Chandra") == rashi_of("Mangala"):
                yogas.append(("Chandra-Mangala Yoga",
                    "Lune et Mars conjoints. Passion, courage, leadership, energie combative. Attention a l'impulsivite.",
                    "medium"))

        # ── 4. Raja Yoga: Kendra Lord + Kona Lord in Kendra/Kona ──
        for h1 in KENDRA_HOUSES:
            for h2 in TRIKONA_HOUSES:
                l1_name = lord_of(h1)
                l2_name = lord_of(h2)
                if l1_name == l2_name:
                    continue
                l1_h = house_of(l1_name)
                l2_h = house_of(l2_name)
                # Mutual connection: lord of h1 is in h2's house, or lord of h2 is in h1's house
                # Or both occupy a Kendra/Kona
                if l1_h and l2_h:
                    condition = False
                    # Lord of Kendra in Kona
                    if l1_h in TRIKONA_HOUSES:
                        condition = True
                    # Lord of Kona in Kendra
                    if l2_h in KENDRA_HOUSES:
                        condition = True
                    # Both in same Kendra/Kona
                    if l1_h in KENDRA_HOUSES and l2_h in KENDRA_HOUSES:
                        condition = True
                    if l1_h in TRIKONA_HOUSES and l2_h in TRIKONA_HOUSES:
                        condition = True
                    if condition:
                        yogas.append((f"Raja Yoga ({l1_name}+{l2_name})",
                            f"Seigneurs du Kendra ({h1}) et du Kona ({h2}) en connexion mutuelle. Pouvoir, autorite, succes, statut eleve.",
                            "strong"))

        # ── 5. Dhana Yoga: Lords of 2/5/9/11 in mutual connection ──
        for h1 in DHANA_HOUSES:
            for h2 in DHANA_HOUSES:
                if h1 >= h2:
                    continue
                l1_name = lord_of(h1)
                l2_name = lord_of(h2)
                if l1_name == l2_name:
                    continue
                l1_h = house_of(l1_name)
                l2_h = house_of(l2_name)
                if l1_h and l2_h:
                    # Conjunction or mutual aspect
                    if l1_h == l2_h:
                        yogas.append((f"Dhana Yoga ({l1_name}+{l2_name})",
                            f"Seigneurs des maisons de richesse ({h1}, {h2}) conjoints. Prosperite financiere, gains, opportunites materielles.",
                            "medium"))

        # ── 6. Viparita Raja Yoga: Lords of 6/8/12 in own/tri/kona houses ──
        trik_lords = []
        for h in TRIK_HOUSES:
            l_name = lord_of(h)
            l_h = house_of(l_name)
            if l_h and l_h in TRIK_HOUSES:
                trik_lords.append(l_name)
        if len(trik_lords) >= 2:
            yogas.append(("Viparita Raja Yoga",
                f"Seigneurs des maisons de defi ({', '.join(trik_lords)}) en maisons 6/8/12. Succes a travers les obstacles, renaissance apres les crises.",
                "strong"))
        elif len(trik_lords) == 1:
            yogas.append((f"Viparita Raja Yoga ({trik_lords[0]})",
                f"Seigneur de maison 6/8/12 en maison 6/8/12. Transformation positive a travers les defis.",
                "medium"))

        # ── 7. Sankha Yoga (auspicious planets in 4 corners) ──
        benefics_in_kendra = 0
        for g_name in ["Guru", "Shukra", "Budha"]:
            gh = house_of(g_name)
            if gh and gh in KENDRA_HOUSES:
                benefics_in_kendra += 1
        if benefics_in_kendra >= 3:
            yogas.append(("Sankha Yoga (conque)",
                f"{benefics_in_kendra} benefiques en Kendra. Grande chance, charisme, succes social.",
                "strong"))

        # ── 8. Kalpadruma Yoga: All grahas in 7+ houses ──
        occupied = set()
        for g_name in grahas:
            gh = house_of(g_name)
            if gh:
                occupied.add(gh)
        if len(occupied) >= 8:
            yogas.append(("Kalpadruma Yoga (arbre celeste)",
                f"Grahas repartis dans {len(occupied)} maisons differentes. Versatilite, diversite de talents, potentiel multidisciplinaire.",
                "medium"))

        # ── 9. Kemadruma Yoga: No planets on either side of Moon ──
        if grahas.get("Chandra"):
            moon_h = house_of("Chandra")
            adjacent_occupied = False
            for g_name in grahas:
                if g_name == "Chandra":
                    continue
                gh = house_of(g_name)
                if gh and (gh == (moon_h - 1) % 12 or gh == (moon_h + 1) % 12):
                    adjacent_occupied = True
                    break
            if not adjacent_occupied and moon_h:
                # Check if Shukra or Guru aspect Moon
                yogas.append(("Kemadruma Yoga",
                    "Aucun graha a cote de la Lune. Isolement emotionnel, mais peut etre compense par la force de la Lune elle-meme.",
                    "weak"))

        # ── 10. Sunapha Yoga: Planets in 2nd from Moon ──
        if grahas.get("Chandra"):
            moon_h = house_of("Chandra")
            if moon_h:
                h2_from_moon = (moon_h + 1) % 12
                planets_in_2nd = [n for n in grahas if house_of(n) == h2_from_moon]
                if planets_in_2nd:
                    yogas.append(("Sunapha Yoga",
                        f"Grahas en 2e depuis la Lune ({', '.join(planets_in_2nd)}). Richesse, prosperite, confort materiel.",
                        "medium"))

        # ── 11. Anapha Yoga: Planets in 12th from Moon ──
        if grahas.get("Chandra"):
            moon_h = house_of("Chandra")
            if moon_h:
                h12_from_moon = (moon_h - 1) % 12
                planets_in_12th = [n for n in grahas if house_of(n) == h12_from_moon]
                if planets_in_12th:
                    yogas.append(("Anapha Yoga",
                        f"Grahas en 12e depuis la Lune ({', '.join(planets_in_12th)}). Charme personnalite, influence, bonnes relations.",
                        "medium"))

        # ── 12. Durudhara Yoga: Planets in 2nd AND 12th from Moon ──
        if grahas.get("Chandra"):
            moon_h = house_of("Chandra")
            if moon_h:
                h2 = (moon_h + 1) % 12
                h12 = (moon_h - 1) % 12
                p2 = [n for n in grahas if house_of(n) == h2]
                p12 = [n for n in grahas if house_of(n) == h12]
                if p2 and p12:
                    yogas.append(("Durudhara Yoga",
                        f"Grahas des deux cotes de la Lune ({', '.join(p2)} + {', '.join(p12)}). Richesse, popularite, equilibre materiel-spirituel.",
                        "strong"))

        # ── 13. Neecha Bhanga Raja Yoga: Debilitated planet gets cancellation ──
        # Check if any planet is in debilitation but has cancellation
        deb_house = {"Surya": 9, "Chandra": 2, "Mangala": 3, "Budha": 5,
                     "Guru": 3, "Shukra": 5, "Shani": 0}
        for g_name, deb_sign in deb_house.items():
            g = grahas.get(g_name)
            if not g:
                continue
            g_rashi = rashi_of(g_name)
            if g_rashi == deb_sign:
                # Check cancellation: lord of deb sign is in Kendra/Kona
                deb_lord = HOUSE_LORD_MAP[deb_sign]
                dl_h = house_of(deb_lord)
                if dl_h and dl_h in KENDRA_HOUSES | TRIKONA_HOUSES:
                    yogas.append((f"Neecha Bhanga Raja Yoga ({g_name})",
                        f"{g_name} est en debilite mais annulee. Grand succes apres des difficultes initiales. Transformation puissante.",
                        "strong"))

        return yogas
```

- [ ] **Step 3: Update astra_birth.py to use detect_d1_yogas()**

Replace the basic yoga detection block (lines 96-123) with:

```python
    # Detect Yogas using core engine
    engine = AstraEngine()
    yogas = engine.detect_d1_yogas(chart)

    if yogas:
        # Sort by strength
        strength_order = {"strong": 0, "medium": 1, "weak": 2}
        yogas.sort(key=lambda y: strength_order.get(y[2], 3))
        
        for name, desc, strength in yogas:
            icon = {"strong": ":star:", "medium": "", "weak": "-"}.get(strength, "")
            md += f"- **{name}** {icon}: {desc}\n"
    else:
        md += "- Aucun yoga majeur detecte\n"
```

Note: Need to pass engine to generate_birth_md. Add `engine` parameter.

- [ ] **Step 4: Update astra_reading.py Yogas section to use new strength data**

Replace Section 3 Yogas content (lines 336-346) with interpretation that includes strength:

```python
    md += "## Section 3 : Yogas\n\n"
    if chart.get("yogas"):
        for yoga_name, yoga_desc, yoga_strength in chart.get("yogas", []):
            strength_label = {"strong": "Puissant", "medium": "Modere", "weak": "Faible"}.get(yoga_strength, "Modere")
            md += f"""**{yoga_name}** — {strength_label}
{yoga_desc}

"""
        # Count strong Yogas for summary
        strong_count = sum(1 for y in chart.get("yogas", []) if len(y) >= 3 and y[2] == "strong")
        if strong_count >= 3:
            md += f"**{strong_count} yogas puissants** — charte natale exceptionnellement favorable.\n\n"
        elif strong_count >= 1:
            md += f"**{strong_count} yoga(s) puissant(s)** — points d'appui solides dans le theme.\n\n"
        else:
            md += "Aucun yoga majeur — les energies sont distribuees sans combinaison exceptionnelle.\n\n"
    else:
        md += "Aucun yoga majeur detecte dans le D1.\n\n"
```

Also update parse_birth_md to extract yogas with strength:

Update yoga section parsing (lines 248-254) to capture strength:

```python
    yogas = []
    yogas_section = re.search(
        r"## Yogas \(Auto-Detected\)\n(.+?)(?=\n##|\Z)", text, re.DOTALL
    )
    if yogas_section:
        for ym in re.finditer(r"\*\*(.+?):\*\*\s*(.+)", yogas_section.group(1)):
            full_text = ym.group(2).strip()
            strength = "medium"
            entry = [ym.group(1), full_text, strength]
            yogas.append(entry)
```

---

### Task 2: Extended Muhurta (15+ Event Types)

**Files:**
- Modify: `Runtime/engine/astra_core.py` (extend EVENT_MUHURTA)

- [ ] **Step 1: Extend EVENT_MUHURTA dict**

Replace the EVENT_MUHURTA block (lines 117-154) with:

```python
EVENT_MUHURTA = {
    "signature": {
        "best_tithi": [2, 3, 5, 7, 10, 11, 13],
        "best_vara": [4, 5],
        "best_hora": ["Guru", "Shukra", "Budha"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True, "avoid_eclipse": True,
    },
    "negotiation": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [3, 4],
        "best_hora": ["Budha", "Guru"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "launch": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [0, 4, 5],
        "best_hora": ["Guru", "Surya", "Shukra"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True, "avoid_eclipse": True,
    },
    "deep_work": {
        "best_tithi": [5, 6, 7, 8, 10, 11],
        "best_vara": [6, 3],
        "best_hora": ["Shani", "Budha"],
        "avoid_rikta": False, "avoid_mercury_rx": False, "avoid_rahu": False,
    },
    "fundraising": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [4, 0],
        "best_hora": ["Guru", "Surya"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True, "avoid_eclipse": True,
    },
    "content": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [1, 3, 4],
        "best_hora": ["Budha", "Shukra", "Chandra"],
        "avoid_rikta": True, "avoid_mercury_rx": False, "avoid_rahu": False,
    },
    "medical": {
        "best_tithi": [2, 5, 7, 9, 10, 11, 13],
        "best_vara": [1, 4, 5],
        "best_hora": ["Chandra", "Guru"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "travel": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [4, 0, 3],
        "best_hora": ["Guru", "Budha", "Surya"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "education": {
        "best_tithi": [2, 5, 7, 10, 11],
        "best_vara": [4, 3, 5],
        "best_hora": ["Guru", "Budha"],
        "avoid_rikta": True, "avoid_mercury_rx": False, "avoid_rahu": False,
    },
    "investment": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [4, 5],
        "best_hora": ["Guru", "Shukra", "Budha"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True, "avoid_eclipse": True,
    },
    "partnership": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [4, 5, 0],
        "best_hora": ["Shukra", "Guru"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "legal": {
        "best_tithi": [5, 7, 10, 11, 13],
        "best_vara": [4, 0, 2],
        "best_hora": ["Guru", "Surya", "Mangala"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "renovation": {
        "best_tithi": [4, 7, 9, 10, 14],
        "best_vara": [6, 2, 4],
        "best_hora": ["Mangala", "Shani", "Surya"],
        "avoid_rikta": False, "avoid_mercury_rx": False, "avoid_rahu": False,
    },
    "moving": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [1, 4, 5, 0],
        "best_hora": ["Guru", "Shukra"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "vehicle": {
        "best_tithi": [2, 3, 5, 7, 10, 11, 13],
        "best_vara": [1, 4, 0],
        "best_hora": ["Budha", "Surya", "Shukra"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "interview": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [0, 4, 3],
        "best_hora": ["Budha", "Guru", "Shukra"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
    },
    "networking": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_vara": [4, 0, 5, 3],
        "best_hora": ["Budha", "Shukra"],
        "avoid_rikta": True, "avoid_mercury_rx": False, "avoid_rahu": False,
    },
}
```

- [ ] **Step 2: Update astra_daily.py to include new muhurta types**

Update the Muhurta Scores table and best_type determination in render_daily_md (lines 106-124):

```python
    # Muhurta scores listing - show all event types
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
```

---

### Task 3: Vargas D9/Navamsa + D10/Dasamsa + D60/Shashtiamsa

**Files:**
- Modify: `Runtime/engine/astra_core.py` (add `compute_varga()` method)
- Modify: `Runtime/engine/astra_birth.py` (add Vargas tables to birth MD)
- Modify: `Runtime/engine/astra_reading.py` (add Section for Vargas interpretation)

- [ ] **Step 1: Add compute_varga() method to AstraEngine**

After the compute_birth_chart method, add:

```python
    # ── Vargas (Divisional Charts) ─────────────────────────────────────

    VARGA_DEFS = {
        "D1": {"name": "Rashi (Natal)", "divisor": 1, "description": "Corps physique, personnalite globale"},
        "D9": {"name": "Navamsa", "divisor": 9, "description": "Conjoint, mariage, spiritualite, potentiel cache"},
        "D10": {"name": "Dasamsa", "divisor": 10, "description": "Carriere, profession, autorite, karma social"},
        "D60": {"name": "Shashtiamsa", "divisor": 60, "description": "Karma profond, destin, tendances passees"},
    }

    def compute_varga_positions(self, jd: float, divisor: int) -> dict:
        """Compute graha positions in a divisional chart.
        
        For each graha, the divisional sign = floor(sidereal_lon / (30/divisor)) % divisor
        then mapped back to a sign from the varga's starting sign.
        """
        grahas = self.all_grahas(jd)
        varga_positions = {}
        
        for name, g in grahas.items():
            lon = g["lon"]
            # Each divisional sign is 30/divisor degrees
            seg_size = 30.0 / divisor
            # Which segment within the rashi
            deg_in_rashi = lon % 30
            seg_i = int(deg_in_rashi / seg_size)
            # The varga sign = rashi_start_sign + seg_i (mod 12)
            rashi_i = int(lon / 30) % 12
            varga_sign_i = (rashi_i * divisor + seg_i) % 12
            varga_positions[name] = {
                "rashi": RASHI_FR[varga_sign_i],
                "rashi_en": RASHI[varga_sign_i],
                "rashi_i": varga_sign_i,
                "lon": lon,
                "varga_degree_offset": round(deg_in_rashi % seg_size, 2),
                "retrograde": g["retrograde"],
            }
        
        return varga_positions

    def compute_vargas(self, birth_jd: float) -> dict:
        """Compute D9, D10, D60 positions."""
        result = {}
        for key, vdef in self.VARGA_DEFS.items():
            if key == "D1":
                # D1 is just the birth chart
                continue
            result[key] = {
                "name": vdef["name"],
                "description": vdef["description"],
                "positions": self.compute_varga_positions(birth_jd, vdef["divisor"]),
            }
        return result

    def compute_varga_lagna(self, birth_chart: dict, divisor: int) -> dict:
        """Compute lagna in a divisional chart."""
        asc_lon = birth_chart["lagna"]["lon"]
        seg_size = 30.0 / divisor
        deg_in_rashi = asc_lon % 30
        seg_i = int(deg_in_rashi / seg_size)
        rashi_i = int(asc_lon / 30) % 12
        varga_sign_i = (rashi_i * divisor + seg_i) % 12
        return {
            "rashi": RASHI_FR[varga_sign_i],
            "rashi_i": varga_sign_i,
            "varga_degree_offset": round(deg_in_rashi % seg_size, 2),
        }
```

- [ ] **Step 2: Update astra_birth.py to include Vargas**

In generate_birth_md, after the Yogas section, add:

```python
    # Compute Vargas
    vargas = engine.compute_vargas(chart["jd"])
    
    md += f"""
## Vargas (Divisional Charts)
"""
    for vkey in ["D9", "D10", "D60"]:
        vdata = vargas.get(vkey, {})
        vpos = vdata.get("positions", {})
        vlagna = engine.compute_varga_lagna(chart, {"D9": 9, "D10": 10, "D60": 60}[vkey])
        
        md += f"""
### {vkey} — {vdata.get('name', '')}
{vdata.get('description', '')}
- **Lagna:** {vlagna['rashi']}
- **Grahas:**
| Graha | Rashi |
|-------|-------|
"""
        for g_name in GRAHA_ORDER:
            pg = vpos.get(g_name)
            if pg:
                retro = " R" if pg["retrograde"] else ""
                md += f"| {g_name}{retro} | {pg['rashi']} |\n"
```

Note: Import GRAHA_ORDER at the top of astra_birth.py or use the tuple from astra_core.

- [ ] **Step 3: Update astra_reading.py to add Vargas interpretation section**

Add a new Section 8 (renumbering if needed) after Section 7:

```python
    # ── Section 8: Vargas Summary ─────────────────────────────────────
    md += "## Section 8 : Analyse des Vargas\n\nLes divisionales (Vargas) revelent des couches plus profondes du destin. Chaque varga eclaire un domaine specifique.\n\n"
    
    if chart.get("vargas"):
        for vkey in ["D9", "D10", "D60"]:
            vdata = chart["vargas"].get(vkey, {})
            if not vdata:
                continue
            positions = vdata.get("positions", {})
            md += f"""### {vkey} — {vdata.get('name', '')}
{vdata.get('description', '')}

"""
            # Highlight notable placements in varga
            for g_name in GRAHA_ORDER:
                pg = positions.get(g_name)
                if pg:
                    rashi = pg.get("rashi", "")
                    # Check if graha is in own/exaltation sign in this varga
                    # (simplified: just list key placements)
                    md += f"- {g_name}: {rashi}\n"
            md += "\n"
    else:
        md += "Donnees Vargas non disponibles.\n\n"
```

---

### Task 4: Ashtakavarga System

**Files:**
- Modify: `Runtime/engine/astra_core.py` (add Ashtakavarga computation methods)
- Modify: `Runtime/engine/astra_daily.py` (add Ashtakavarga transit guidance)
- Modify: `Runtime/engine/astra_birth.py` (add Sarvashtakavarga table)
- Modify: `Runtime/engine/astra_reading.py` (add Ashtakavarga narrative section)

- [ ] **Step 1: Add Ashtakavarga constants and computation to astra_core.py**

Add before the AstraEngine class (or in a new section):

```python
# ── Ashtakavarga ──────────────────────────────────────────────────────

# Ashtakavarga bindus per planet per house (1-based)
# Each planet gives 0-8 bindus in each house based on transit position
# Simplified: standard Ashtakavarga tables

# Bhinnashtakavarga bindus for each planet's transit through each sign (1-based)
# Standard Parashari Ashtakavarga bindu counts
ASHTAKAVARGA_TABLE = {
    "Surya":  [5, 4, 5, 3, 6, 5, 4, 5, 6, 4, 3, 2],
    "Chandra":[3, 4, 4, 6, 6, 4, 5, 4, 4, 5, 5, 4],
    "Mangala":[5, 3, 4, 5, 4, 3, 5, 4, 5, 5, 3, 4],
    "Budha":  [5, 5, 3, 6, 4, 5, 5, 5, 4, 5, 5, 4],
    "Guru":   [5, 4, 4, 5, 5, 5, 4, 3, 5, 5, 4, 5],
    "Shukra": [4, 4, 5, 6, 5, 4, 4, 4, 5, 5, 5, 5],
    "Shani":  [3, 4, 4, 5, 5, 4, 4, 5, 4, 4, 5, 5],
}

# Houses for which each planet contributes bindus (Parashari)
# For transit analysis
ASHTAKA_RECEPTACLES = {
    "Surya":  [1, 2, 4, 7, 8, 9, 10, 11],
    "Chandra":[3, 6, 7, 8, 10, 11, 12],
    "Mangala":[3, 5, 6, 8, 9, 10, 11, 12],
    "Budha":  [1, 3, 4, 5, 7, 8, 10, 11],
    "Guru":   [1, 2, 4, 5, 6, 9, 10, 11],
    "Shukra": [1, 2, 3, 4, 5, 8, 9, 11],
    "Shani":  [1, 2, 4, 7, 8, 9, 10, 11],
}

# Standard benefic/unbenefic houses for each planet (1-based)
ASHTAKA_BENEFIC = {
    "Surya":  [1, 2, 4, 7, 8, 9, 10, 11],
    "Chandra":[3, 6, 7, 8, 10, 11, 12],
    "Mangala":[3, 5, 6, 8, 9, 10, 11, 12],
    "Budha":  [1, 3, 4, 5, 7, 8, 10, 11],
    "Guru":   [1, 2, 4, 5, 6, 9, 10, 11],
    "Shukra": [1, 2, 3, 4, 5, 8, 9, 11],
    "Shani":  [1, 2, 4, 7, 8, 9, 10, 11],
}
```

- [ ] **Step 2: Add compute_ashtakavarga() method to AstraEngine**

```python
    # ── Ashtakavarga ───────────────────────────────────────────────────

    def compute_ashtakavarga(self, jd: float) -> dict:
        """Compute Bhinnashtakavarga and Sarvashtakavarga for a given date."""
        grahas = self.all_grahas(jd)
        
        # Bhinnashtakavarga: per-planet bindus (house-based from lagna)
        bhinnas = {}
        sarva = [0] * 12
        
        for planet_name, bindus in ASHTAKAVARGA_TABLE.items():
            if planet_name not in grahas:
                continue
            # Position of the planet (which sign it's in, 0-11)
            p_lon = grahas[planet_name]["lon"]
            p_sign = int(p_lon / 30) % 12
            
            # Bindus per house: the sign the planet is in determines which
            # houses get how many bindus via the table
            house_bindus = [0] * 12
            for house_i in range(12):
                # The bindu value for this planet in this house position
                # The table is indexed by transit sign
                transit_sign = (p_sign + house_i) % 12
                bindu = bindus[transit_sign]
                house_bindus[house_i] = bindu
                sarva[house_i] += bindu
            
            bhinnas[planet_name] = house_bindus
        
        # Add Ketu's ashtakavarga (same as Jupiter)
        if "Rahu" in grahas:
            bhinnas["Ketu"] = list(bhinnas.get("Guru", [0]*12))
        
        total_possible = len(ASHTAKAVARGA_TABLE) * 8  # Max bindus possible
        sarva_total = sum(sarva)
        
        # Strong houses: above average bindus
        avg = sarva_total / 12 if sarva_total > 0 else 0
        strong_houses = [i + 1 for i, b in enumerate(sarva) if b > avg]
        weak_houses = [i + 1 for i, b in enumerate(sarva) if b < avg - 2]
        
        return {
            "bhinnashtakavarga": bhinnas,
            "sarvashtakavarga": sarva,
            "total_bindus": sarva_total,
            "average_bindus": round(avg, 1),
            "strong_houses": strong_houses,
            "weak_houses": weak_houses,
        }
```

- [ ] **Step 3: Add compute_ashtaka_transit() method**

```python
    def compute_ashtaka_transit(self, jd: float, birth_jd: float) -> dict:
        """Analyse transiting planets through natal Ashtakavarga houses."""
        natal_ashta = self.compute_ashtakavarga(birth_jd)
        transit_grahas = self.all_grahas(jd)
        
        transit_effects = []
        for g_name, g_data in transit_grahas.items():
            if g_name not in ASHTAKAVARGA_TABLE:
                continue
            t_sign = int(g_data["lon"] / 30) % 12
            
            # Check transit through Ashtakavarga benefic houses
            benefic_houses = ASHTAKA_BENEFIC.get(g_name, [])
            # Current transit house (1-based relative to natal chart)
            # Need asc from birth chart
            # Simplified: just check transit sign vs natal ashtaka houses
            
            # Bindu count at transit position in Sarvashtakavarga
            transit_bindu = natal_ashta["sarvashtakavarga"][t_sign]
            strong = transit_bindu > natal_ashta["average_bindus"]
            
            transit_effects.append({
                "graha": g_name,
                "transit_sign": t_sign,
                "transit_rashi": RASHI_FR[t_sign],
                "transit_bindu": transit_bindu,
                "above_average": strong,
            })
        
        return {
            "transits": transit_effects,
            "sarva": natal_ashta,
        }
```

- [ ] **Step 4: Update astra_daily.py to include Ashtakavarga transit guidance**

In render_daily_md, after the Muhurta section, add:

```python
    # Ashtakavarga transit analysis
    if birth_chart:
        try:
            ashta_transit = engine.compute_ashtaka_transit(jd, birth_chart["jd"])
            strong_transits = [t for t in ashta_transit["transits"] if t.get("above_average")]
            if strong_transits:
                md += "\n## Ashtakavarga Transits\n"
                md += "| Graha | Transit | Bindus |\n"
                md += "|-------|---------|--------|\n"
                for t in strong_transits:
                    md += f"| {t['graha']} | {t['transit_rashi']} | {t['transit_bindu']} |\n"
                md += "\n"
        except Exception:
            pass
```

---

### Task 5: Shadbala (Sixfold Strength)

**Files:**
- Modify: `Runtime/engine/astra_core.py` (add Shadbala computation)
- Modify: `Runtime/engine/astra_reading.py` (add Shadbala section)

- [ ] **Step 1: Add Shadbala computation to astra_core.py**

Add after the compute_vargas method:

```python
    # ── Shadbala (Sixfold Strength) ─────────────────────────────────────

    SHADBALA_RUPS = {
        "Surya": 5, "Chandra": 5, "Mangala": 5, "Budha": 5,
        "Guru": 5, "Shukra": 5, "Shani": 5,
    }

    GRAHA_EXALTATION = {
        "Surya": 0, "Chandra": 2, "Mangala": 9, "Budha": 5,
        "Guru": 3, "Shukra": 5, "Shani": 9,
    }

    GRAHA_DEBILITATION = {
        "Surya": 9, "Chandra": 8, "Mangala": 3, "Budha": 5,
        "Guru": 3, "Shukra": 5, "Shani": 0,
    }

    GRAHA_MOOLATRIKONA = {
        "Surya": 0, "Chandra": 2, "Mangala": 0, "Budha": 5,
        "Guru": 9, "Shukra": 5, "Shani": 10,
    }

    def compute_shadbala(self, jd: float, birth_chart: dict) -> dict:
        """Compute simplified Shadbala (sixfold strength) for each graha.
        
        Returns normalized strength 0-100 for each graha.
        Full Shadbala requires extensive computation; this is a practical
        approximation based on key factors.
        """
        grahas = self.all_grahas(jd)
        asc_lon = birth_chart["lagna"]["lon"]
        asc_sign = int(asc_lon / 30) % 12
        
        result = {}
        for name, g in grahas.items():
            if name == "Ketu" or name == "Rahu":
                # Nodes get simplified strength
                continue
            
            lon = g["lon"]
            sign_i = int(lon / 30) % 12
            deg = lon % 30
            speed = g["speed"]
            
            score = 50  # Baseline
            
            # 1. Sthana Bala (Positional): exaltation + moolatrikona + own sign + friend sign
            ex_sign = self.GRAHA_EXALTATION.get(name, -1)
            de_sign = self.GRAHA_DEBILITATION.get(name, -1)
            mt_sign = self.GRAHA_MOOLATRIKONA.get(name, -1)
            
            if sign_i == ex_sign:
                score += 30  # Exalted
            elif sign_i == de_sign:
                score -= 20  # Debilitated
            elif sign_i == mt_sign:
                score += 20  # Moolatrikona
            
            # Own sign: check rashi lord
            own_lord = HOUSE_LORD_MAP.get(sign_i)
            if own_lord == name:
                score += 15
            
            # 2. Chesta Bala (Motional): retrograde strength
            if speed < 0:
                score += 10  # Retrograde planets gain strength
            elif abs(speed) < 0.5:
                score -= 5   # Slow planets lose some
            
            # 3. Dig Bala (Directional): planets in directional signs
            # Surya: 10th house, Shukra/Budha: 1st, etc.
            house_i = (sign_i - asc_sign) % 12
            dig_bala_houses = {
                "Surya": 9, "Chandra": 3, "Mangala": 9,
                "Budha": 0, "Guru": 0, "Shukra": 0, "Shani": 9,
            }
            dig_house = dig_bala_houses.get(name, -1)
            if house_i == dig_house:
                score += 15
            elif (house_i - dig_house) % 12 == 6:
                score -= 10  # Opposite direction
            
            # 4. Naisargika Bala (Natural): natural strength hierarchy
            natural_strength = {
                "Surya": 10, "Chandra": 8, "Guru": 7, "Shukra": 6,
                "Budha": 5, "Mangala": 4, "Shani": 3,
            }
            score += natural_strength.get(name, 5)
            
            # 5. Drik Bala (Aspectual): simplified
            # Benefic aspects add, malefic subtract
            benefic_aspects = 0
            malefic_aspects = 0
            for other_name, other_g in grahas.items():
                if other_name == name or other_name == "Rahu" or other_name == "Ketu":
                    continue
                o_sign = int(other_g["lon"] / 30) % 12
                o_house = (o_sign - asc_sign) % 12
                
                # Check opposition (7th house)
                if (o_house - house_i) % 12 == 6:
                    if other_name in ["Guru", "Shukra"]:
                        benefic_aspects += 1
                    elif other_name in ["Mangala", "Shani"]:
                        malefic_aspects += 1
            
            score += benefic_aspects * 5
            score -= malefic_aspects * 3
            
            # Normalize
            score = max(0, min(100, score))
            
            # Qualitative
            if score >= 75:
                quality = "tres fort"
            elif score >= 60:
                quality = "fort"
            elif score >= 40:
                quality = "moyen"
            elif score >= 25:
                quality = "faible"
            else:
                quality = "tres faible"
            
            result[name] = {
                "score": score,
                "quality": quality,
                "exalted": sign_i == ex_sign,
                "debilitated": sign_i == de_sign,
            }
        
        return result
```

---

### Task 6: Update astra_birth.py for Phase 2

**Files:**
- Modify: `Runtime/engine/astra_birth.py`

- [ ] **Step 1: Import GRAHA_ORDER at top**

Add:
```python
from Runtime.engine.astra_core import AstraEngine, GRAHA_ORDER
```

- [ ] **Step 2: Pass engine to generate_birth_md + integrate all new features**

Refactor generate_birth_md signature: `def generate_birth_md(engine, year, month, day, hour, minute, place="Lome") -> str:`

Inside function, after computing chart and dasha:
1. Call `engine.detect_d1_yogas(chart)` — replace old yoga block
2. Call `engine.compute_vargas(chart["jd"])` — add after Yogas
3. Call `engine.compute_ashtakavarga(chart["jd"])` — add basic summary
4. Call `engine.compute_shadbala(chart["jd"], chart)` — add basic summary

- [ ] **Step 3: Update main() to pass engine**

Change main() to create engine before calling generate_birth_md and pass it:
```python
    engine = AstraEngine()
    md = generate_birth_md(engine, year, month, day, hour, minute, args.place)
```

---

### Task 7: Update astra_reading.py for Phase 2

**Files:**
- Modify: `Runtime/engine/astra_reading.py`

- [ ] **Step 1: Parse new birth MD sections (Vargas, Ashtakavarga, Shadbala)**

In parse_birth_md, add parsing for:
- Vargas tables (regex per D9/D10/D60 section)
- Ashtakavarga summary
- Shadbala scores (if present)

Store as `chart["vargas"]`, `chart["ashtakavarga"]`, `chart["shadbala"]`.

- [ ] **Step 2: Add Section 8 (Vargas analysis) — see Task 3 Step 3**

- [ ] **Step 3: Add Section 9 (Ashtakavarga analysis)**

```python
    # ── Section 9: Ashtakavarga ────────────────────────────────────────
    md += "## Section 9 : Ashtakavarga\n\nAshtakavarga est un systeme de points (bindus) qui mesure la force des maisons. Plus une maison a de bindus, plus elle est favorable.\n\n"
    
    ashta = chart.get("ashtakavarga", {})
    if ashta:
        sarva = ashta.get("sarvashtakavarga", [])
        if sarva:
            md += "### Sarvashtakavarga (total bindus par maison)\n| Maison | Bindus | Force |\n|--------|--------|-------|\n"
            avg = sum(sarva) / len(sarva) if sarva else 0
            for i, b in enumerate(sarva):
                if b > avg: force = ":star: Forte"
                elif b < avg - 2: force = "Faible"
                else: force = "Moyenne"
                md += f"| {i+1} | {b} | {force} |\n"
            md += f"\n**Total:** {sum(sarva)} bindus (moyenne: {avg:.1f})\n\n"
            
            # Highlight
            strong = ashta.get("strong_houses", [])
            weak = ashta.get("weak_houses", [])
            if strong:
                md += f"**Maisons fortes:** {', '.join(str(h) for h in strong)} — opportunites dans ces domaines.\n"
            if weak:
                md += f"**Maisons faibles:** {', '.join(str(h) for h in weak)} — vigilance requise.\n"
    else:
        md += "Donnees Ashtakavarga non disponibles.\n\n"
```

- [ ] **Step 4: Add Section 10 (Shadbala analysis)**

```python
    # ── Section 10: Shadbala (Sixfold Strength) ────────────────────────
    md += "## Section 10 : Shadbala — Force des Grahas\n\nLe Shadbala mesure la force globale de chaque graha dans le theme. Score sur 100.\n\n"
    
    shadbala = chart.get("shadbala", {})
    if shadbala:
        md += "| Graha | Score | Qualite | Note |\n|-------|-------|---------|------|\n"
        for g_name in GRAHA_ORDER:
            s = shadbala.get(g_name)
            if s:
                notes = []
                if s.get("exalted"):
                    notes.append("Exalte")
                if s.get("debilitated"):
                    notes.append("Debile")
                note_str = ", ".join(notes) if notes else "-"
                md += f"| {g_name} | {s['score']}/100 | {s['quality']} | {note_str} |\n"
        
        # Identify strongest and weakest
        valid = {k: v for k, v in shadbala.items() if v and v.get("score") is not None}
        if valid:
            strongest = max(valid, key=lambda k: valid[k]["score"])
            weakest = min(valid, key=lambda k: valid[k]["score"])
            md += f"\n**Graha le plus fort:** {strongest} ({valid[strongest]['score']}/100)\n"
            md += f"**Graha le plus faible:** {weakest} ({valid[weakest]['score']}/100)\n"
    else:
        md += "Donnees Shadbala non disponibles.\n\n"
```

---

### Task 8: Update astra_daily.py for Phase 2

**Files:**
- Modify: `Runtime/engine/astra_daily.py`

- [ ] **Step 1: Integrate new Muhurta types (Task 2 Step 2)**

- [ ] **Step 2: Integrate Ashtakavarga transit (Task 4 Step 4)**

- [ ] **Step 3: Run and verify all outputs**

---

### Task 9: Integration Test — Full GENESIS flow with Phase 2

**Files:**
- `State/ASTRA_BIRTH.md` (regenerated)
- `State/ASTRA_DAILY.md` (regenerated)
- `State/ASTRA_READING_RAW.md` (regenerated)

- [ ] **Step 1: Regenerate birth profile**
```bash
python Runtime/engine/astra_birth.py --base-dir . --date 2003-05-29 --time 09:49
```

- [ ] **Step 2: Regenerate daily**
```bash
python Runtime/engine/astra_daily.py --base-dir . --force
```

- [ ] **Step 3: Regenerate reading**
```bash
python Runtime/engine/astra_reading.py --base-dir .
```

- [ ] **Step 4: Run forecast test**
```bash
python Runtime/engine/astra_forecast.py --base-dir . today
```

- [ ] **Step 5: Verify all files exist and contain new sections**
```
State/ASTRA_BIRTH.md — should have Yogas (10+ types), Vargas tables, Shadbala
State/ASTRA_DAILY.md — should have new muhurta types, Ashtakavarga transits
State/ASTRA_READING_RAW.md — should have Sections 8-10 (Vargas, Ashtakavarga, Shadbala)
```
