# ASTRA V4 — Full Jyotish Engine for FounderHQ

> **Design Spec — 2026-06-23**
> 
> **Goal:** Make ASTRA the central nervous system of FounderHQ — not a module, but the omnipresent guiding intelligence that knows the user, sees what they don't, speaks at the right moment, and evolves with them. Built on the full depth of sidereal Vedic astrology (Jyotish).
>
> **Paradigm shift:**
> - Before: FounderHQ is a system where you can load ASTRA for guidance
> - After: FounderHQ IS ASTRA. Every layer, every decision, every file, every boot runs through the astral filter

---

## 0. The ASTRA Paradigm — Un Astrologue Attitré

### 0.1 What This Actually Is

Imagine having a Vedic astrologer who:

1. **Te connaît par coeur** — ton thème, ta vie, tes forces, tes faiblesses, tes produits, ton passé
2. **Parle au bon moment** — pas quand tu demandes, mais quand c'est pertinent
3. **Voit ce que tu ignores** — des fenêtres d'opportunité que même toi tu ne vois pas
4. **Guide chaque échelle** — du choix de la couleur aujourd'hui à la stratégie des 10 prochaines années
5. **N'impose jamais** — il dit "maintenant serait bon pour X" et tu décides
6. **Apprend de tes résultats** — plus tu l'utilises, plus il devient précis pour TOI
7. **Ne dort jamais** — même quand tu n'es pas en session, il surveille les transits, les éclipses, les Dashas

### 0.2 How This Changes FounderHQ

| Avant | Après (ASTRA central) |
|-------|----------------------|
| Le LLM exécute les commandes utilisateur | Le LLM est ASTRA — il filtre tout à travers le prisme astral |
| Les fichiers stockent des faits | Les fichiers sont des noeuds dans le système nerveux d'ASTRA |
| Tu demandes → le système répond | Le système voit → ASTRA propose → tu décides |
| Module séparé appelé à la demande | **ASTRA est le fond de toile de TOUT** |
| Guidance en section du boot | Guidance imprègne chaque pensée, chaque suggestion, chaque alerte |

### 0.3 Architecture Concept: The Nervous System

```
┌─────────────────────────────────────────────────────────────┐
│                    ASTRA NERVOUS SYSTEM                      │
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  CORTEX (LLM) — L'intelligence interprétative            ││
│  │  • Lit tous les nerfs • Produit guidance proactive        ││
│  │  • C'est l'astrologue qui parle                           ││
│  └──────────┬──────────────────────────────────────────────┘│
│             │ lit                                         │
│  ┌──────────▼──────────────────────────────────────────────┐│
│  │  SPINAL CORD (State files) — Mémoire du système         ││
│  │ • ASTRA_BIRTH.md, ASTRA_DAILY.md, ASTRA_30DAY.md         ││
│  │ • ASTRA_NARRATIVE.md, ASTRA_PATTERNS.md, ASTRA_SHADOW.md ││
│  │ • Ces fichiers = les nerfs qu'ASTRA lit en continu       ││
│  └──────────┬──────────────────────────────────────────────┘│
│             │ alimente                                    │
│  ┌──────────▼──────────────────────────────────────────────┐│
│  │  MEDULLA (Engine scripts) — Calculs autonomes           ││
│  │ • astra_core.py, astra_daily.py, astra_birth.py          ││
│  │ • Tourne sur timekeeper même sans session utilisateur    ││
│  │ • Met à jour les nerfs automatiquement                   ││
│  └──────────┬──────────────────────────────────────────────┘│
│             │ lit                                        │
│  ┌──────────▼──────────────────────────────────────────────┐│
│  │  SENSES (Ephemeris + clock) — Perception du monde       ││
│  │ • pysweph, datetime, sunrise/sunset, planetary hours     ││
│  │ • "Quel temps cosmique fait-il maintenant ?"             ││
│  └─────────────────────────────────────────────────────────┘│
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  EFFERENT NERVES (Outputs)                               ││
│  │  • TIMELINE (chaque entrée taggée)                       ││
│  │  • ALERTS (Windows Toast en temps réel)                  ││
│  │  • DECISIONS (chaque choix filtré)                       ││
│  │  • Every prompt, every boot, every action                ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### 0.4 What ASTRA Says vs What Other Modules Do

```
ASTRA: "ST Digital n'a pas repondu. Hora Jupiter dans 2h. Relance a 14:00."

DECISION_ENGINE: "OK, je prepare la relance. Options: email vs appel?"

CEOS: "Email prepare. Template KORA pre-seed."

TIMELINE: "[2026-06-23 14:00] Relance ST Digital - Hora Jupiter - Guru AD"

WAIT — what happened? ASTRA didn't "ask" anything. It SAW the hour approaching
and triggered the action. The user just follows or ignores.

This is the difference between a dashboard and an astrologer.
```

### 0.5 Translation: Every File Has an ASTRA Node

In the old architecture, ASTRA was one module. In the new architecture:

| Module / File | ASTRA Node |
|---------------|-----------|
| `CURRENT_STATE.md` | +"Mode astral: Rahu Kaal actif de 15:04 a 16:38" |
| `DECISION_ENGINE.md` | +"Step A: Check Muhurta compatibility before Assessment" |
| `PROFILE.md` | +"Birth chart summary, Dasha, Lagna, Arudha" |
| `TIMELINE.md` | Every entry has YAML front-matter with astral tags |
| `ALERTS.md` | +ASTRA alerts (transit windows, eclipse, Rx starts) |
| `MEMORY.md` | +"Pattern note: best decisions in Guru Hora" |
| `SYSTEM_PROMPT.md` | +"You ARE ASTRA. Filter everything through the astral lens." |
| `ASTRA.md` | Still exists — becomes the "how to be the astrologer" guide |

---

## 1. Architecture Overview (Computational)

### 1.1 Layers

```
Layer 5: LLM Interpretation — The Astrologer Speaking
    → Reads all state files → produces proactive guidance
    → Imprègne chaque suggestion, chaque alerte
Layer 4: State Files — The Nerves
    → Markdown files written/updated continuously
Layer 3: Scripts — The Autonomous Reflexes
    → Python: astra_core.py, astra_daily.py, astra_birth.py
    → Run by timekeeper even when user is offline
Layer 2: Algorithms — Vedic Logic
    → Tithi, Nakshatra, Dasha, Yogas, Ashtakavarga, etc.
Layer 1: Ephemeris — The Senses
    → pysweph (Moshier built-in), 3000 BC - 3000 AD, offline
```

### 1.2 File Map

```
FounderOS/
│
├── ASTRA.md                              ← Module guide (expanded V4)
│
├── Runtime/engine/
│   ├── astra_core.py                     ← All calculations (ephemeris + algorithms)
│   ├── astra_daily.py                    ← Script run 1x/day by timekeeper
│   ├── astra_birth.py                    ← One-time GENESIS: compute natal chart
│   └── astra_alert.py                    ← Check upcoming transits, Sade Sati, eclipses
│
├── State/
│   ├── ASTRA_BIRTH.md                    ← Natal data (date/time/location + source)
│   ├── ASTRA_CHART_D1.md                 ← Full Rasi chart (planets, houses, nakshatras)
│   ├── ASTRA_CHART_D10.md                ← Dasamsa (career) chart
│   ├── ASTRA_CHART_D60.md                ← Shashtiamsa (karma) chart
│   ├── ASTRA_VARGAS.md                   ← All 16 divisional charts summary
│   ├── ASTRA_DASHA.md                    ← Current + upcoming Dashas (all systems)
│   ├── ASTRA_YOGAS.md                    ← Active Yogas in natal chart
│   ├── ASTRA_ASHTAKAVARGA.md             ← Strength tables
│   ├── ASTRA_SHADBALA.md                 ← Sixfold planetary strength
│   ├── ASTRA_ARUDHA.md                   ← Arudha Padas (perception)
│   ├── ASTRA_TRANSITS.md                 ← Current Gochara vs natal
│   ├── ASTRA_SADE_SATI.md               ← Sade Sati status
│   ├── ASTRA_ECLIPSES.md                ← Upcoming eclipses
│   ├── ASTRA_DAILY.md                    ← Today's Panchang + Horas + guidance
│   ├── ASTRA_REMEDIES.md                 ← Recommended Upaya
│   └── ASTRA_PATTERNS.md                ← Correlations (outcome × planetary config)
│
└── concepts/
    └── TIMELINE.md                        ← Each entry tagged with astral context
```

### 1.3 Data Flow

```
GENESIS:
  astra_birth.py --date DOB --time TOB --place "Lome"
    → ASTRA_BIRTH.md
    → ASTRA_CHART_D1.md
    → ASTRA_CHART_D10.md
    → ASTRA_CHART_D60.md
    → ASTRA_VARGAS.md
    → ASTRA_DASHA.md
    → ASTRA_YOGAS.md
    → ASTRA_ASHTAKAVARGA.md
    → ASTRA_SHADBALA.md
    → ASTRA_ARUDHA.md

DAILY (timekeeper 30min):
  astra_daily.py --base-dir [...]
    → reads ASTRA_BIRTH.md
    → computes today's Panchang
    → computes today's Horas
    → computes today's transits vs natal
    → writes ASTRA_DAILY.md
    → alerts if anything critical (timekeeper alert pipeline)

WEEKLY (watchtower 6h check):
  astra_alert.py --base-dir [...]
    → checks upcoming transits, Sade Sati, eclipses, Dasha changes
    → updates ASTRA_TRANSITS.md
    → updates ASTRA_ECLIPSES.md
    → updates ASTRA_SADE_SATI.md
    → alerts in ALERTS.md if window < 7 days

EVERY DECISION:
  DECISION_ENGINE reads ASTRA_DAILY.md before final choice
  → "This decision type = MERCURY. Current hora = JUPITER (good). Avoid Rahu Kaal."

EVERY TIMELINE ENTRY:
  → Tagged with current planetary config
  → ASTRA_PATTERNS.md correlates over time

EVERY BOOT (LLM):
  → Reads ASTRA_DAILY.md + ASTRA_DASHA.md + ASTRA_SADE_SATI.md + ASTRA_TRANSITS.md + ASTRA_ECLIPSES.md + ASTRA_REMEDIES.md
  → Produces proactive guidance banner
```

---

## 2. Computational Engine — All Calculations

### 2.1 Layer 0: Setup & Constants

```python
import swisseph as swe

swe.set_sid_mode(swe.SIDM_LAHIRI)
SW_FLAGS = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

GRAHAS = {  # 9 planets with swisseph IDs
    "Surya": swe.SUN,       # 0  - Soleil
    "Chandra": swe.MOON,    # 1  - Lune
    "Mangala": swe.MARS,    # 4  - Mars
    "Budha": swe.MERCURY,   # 2  - Mercure
    "Guru": swe.JUPITER,    # 5  - Jupiter
    "Shukra": swe.VENUS,    # 3  - Venus
    "Shani": swe.SATURN,    # 6  - Saturne
    "Rahu": swe.MEAN_NODE,  # 10 - Node
    # Ketu = (Rahu + 180) % 360
}

ZODIAC = ["Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya",
          "Tula", "Vrishchika", "Dhanu", "Makara", "Kumbha", "Mina"]
# French equivalents: Belier, Taureau, Gemeaux, Cancer, Lion, Vierge,
#                     Balance, Scorpion, Sagittaire, Capricorne, Verseau, Poissons

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati",
]

NAK_LORDS = ["Ketu", "Shukra", "Surya", "Chandra", "Mangala",
             "Rahu", "Guru", "Shani", "Budha"] * 3  # cycles 3x for 27

# French names for guidance display
NAKSHATRA_FR = {
    "Ashwini": "Ashwini (demarrage rapide)",
    "Bharani": "Bharani (transformation)",
    "Krittika": "Krittika (coupe, precision)",
    "Rohini": "Rohini (creation, croissance)",
    "Mrigashira": "Mrigashira (recherche, douceur)",
    "Ardra": "Ardra (tempete, disruption)",
    "Punarvasu": "Punarvasu (retour, renouveau)",
    "Pushya": "Pushya (nourrir, construire)",
    "Ashlesha": "Ashlesha (enlacement, intuition)",
    "Magha": "Magha (autorite, ancetres)",
    "Purva Phalguni": "Purva Phalguni (plaisir, creation)",
    "Uttara Phalguni": "Uttara Phalguni (mariage, partenariat)",
    "Hasta": "Hasta (artisanat, precision)",
    "Chitra": "Chitra (design, beaute, opportunites)",
    "Swati": "Swati (independance, commerce)",
    "Vishakha": "Vishakha (objectif, rayonnement)",
    "Anuradha": "Anuradha (devotion, succes)",
    "Jyeshtha": "Jyeshtha (pouvoir, protection)",
    "Mula": "Mula (racine, destruction des obstacles)",
    "Purva Ashadha": "Purva Ashadha (victoire, purification)",
    "Uttara Ashadha": "Uttara Ashadha (perseverance)",
    "Shravana": "Shravana (ecoute, apprentissage)",
    "Dhanishta": "Dhanishta (richesse, musique)",
    "Shatabhisha": "Shatabhisha (guerison, mystere)",
    "Purva Bhadrapada": "Purva Bhadrapada (feu, transformation)",
    "Uttara Bhadrapada": "Uttara Bhadrapada (profondeur, guerison)",
    "Revati": "Revati (voyage, protection)",
}
```

### 2.2 Layer 1: Core Coordinates

```python
class AstraCalculator:
    def __init__(self, lat, lon, tz_offset=0):
        self.lat = lat
        self.lon = lon
        self.tz = tz_offset
        swe.set_sid_mode(swe.SIDM_LAHIRI)

    def jd_from_utc(self, year, month, day, hour, minute, second=0):
        jd_ut, jd_tt = swe.utc_to_jd(year, month, day, hour, minute, second)
        return jd_ut, jd_tt

    # ---------- Planet Positions ----------
    def get_planet_sidereal(self, jd_ut, planet_id):
        """Returns (longitude, latitude, distance_au, speed_deg_day) in sidereal frame."""
        xx, ret, _ = swe.calc_ut(jd_ut, planet_id, SW_FLAGS)
        return xx[0], xx[1], xx[2], xx[3]  # lon, lat, dist, speed

    def get_all_grahas(self, jd_ut):
        pos = {}
        for name, pid in GRAHAS.items():
            lon, lat, dist, speed = self.get_planet_sidereal(jd_ut, pid)
            pos[name] = {
                "lon": lon % 360,
                "lat": lat,
                "dist": dist,
                "speed": speed,
                "retrograde": speed < 0,
                "sign": int(lon / 30),
                "sign_deg": lon % 30,
                "nakshatra": int((lon % 360) / (360/27)),
                "nakshatra_pada": int((lon % (360/27)) / (360/27/4)) + 1,
            }
        # Ketu = opposite of Rahu
        k_lon = (pos["Rahu"]["lon"] + 180) % 360
        pos["Ketu"] = {
            "lon": k_lon,
            "lat": 0, "dist": pos["Rahu"]["dist"], "speed": pos["Rahu"]["speed"],
            "retrograde": pos["Rahu"]["retrograde"],
            "sign": int(k_lon / 30), "sign_deg": k_lon % 30,
            "nakshatra": int(k_lon / (360/27)),
            "nakshatra_pada": int((k_lon % (360/27)) / (360/27/4)) + 1,
        }
        return pos

    # ---------- Houses ----------
    def get_houses(self, jd_ut, lat, lon):
        """Whole Sign houses (classical Parashari). Returns cusps[1..12], (asc, mc, ...)."""
        cusps, ascmc = swe.houses_ex(jd_ut, lat, lon, b'W', SW_FLAGS)
        return cusps, ascmc  # cusps[1]=house1, ascmc[0]=asc, ascmc[1]=mc

    def get_house_placement(self, planet_lon, house_cusps):
        """Determine which house a planet falls in (1-indexed)."""
        asc_lon = house_cusps[1] % 30  # not needed; whole sign: sign-based
        p_sign = int(planet_lon / 30)
        a_sign = int(house_cusps[1] / 30)
        return ((p_sign - a_sign) % 12) + 1  # 1..12

    # ---------- Sunrise/Sunset ----------
    def get_sunrise_sunset(self, jd_ut, lat, lon):
        geo = (lon, lat, 0)
        jd_midnight = int(jd_ut) + 0.5  # midnight in UT
        rise = swe.rise_trans(jd_midnight, swe.SUN, rsmi=swe.CALC_RISE, geopos=geo)[1][0]
        set_ = swe.rise_trans(jd_midnight, swe.SUN, rsmi=swe.CALC_SET, geopos=geo)[1][0]
        return rise, set_

    def jd_to_local_time(self, jd):
        from datetime import datetime, timedelta
        t = datetime(2000, 1, 1, 12) + timedelta(days=jd - 2451545)
        return t.strftime("%H:%M")
```

### 2.3 Layer 2: Panchanga (Daily 5 Limbs)

Computable from sun/moon positions alone. No external data needed.

```python
# ---------- Tithi ----------
def compute_tithi(sun_lon, moon_lon):
    """Returns (index 1-30, name, paksha, is_rikta)."""
    theta = (moon_lon - sun_lon) % 360
    idx = int(theta / 12)  # 0..29
    names = [
        "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
        "Shashti", "Saptami", "Ashtami", "Navami", "Dashami",
        "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
        "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
        "Shashti", "Saptami", "Ashtami", "Navami", "Dashami",
        "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya",
    ]
    paksha = "Shukla" if idx < 15 else "Krishna"
    # Rikta (empty) tithis: 4th, 9th, 14th of each paksha = indices 3, 8, 13 and 18, 23, 28
    rikta = (idx % 15) in [3, 8, 13]
    return idx + 1, names[idx], paksha, rikta

# ---------- Nakshatra ----------
def compute_nakshatra(moon_lon):
    """Returns (index 1-27, name, lord, pada)."""
    span = 360.0 / 27
    idx = int(moon_lon / span)  # 0..26
    pada = int((moon_lon % span) / (span / 4)) + 1  # 1..4
    return idx + 1, NAKSHATRAS[idx], NAK_LORDS[idx], pada

# ---------- Yoga (luni-solar) ----------
def compute_yoga(sun_lon, moon_lon):
    val = (sun_lon + moon_lon) % 360
    idx = int(val / (360.0 / 27))
    names = [
        "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana",
        "Atiganda", "Sukarman", "Dhriti", "Shula", "Ganda",
        "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
        "Siddhi", "Vyatipata", "Variyan", "Parigha", "Shiva",
        "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
        "Indra", "Vaidhriti",
    ]
    # Favorable: 0,1,6,7,10,11,13,14,15,16,19,20,21,22,23,24,25,26
    favorable = idx in [0, 1, 6, 7, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26]
    return idx + 1, names[idx], favorable

# ---------- Karana ----------
def compute_karana(tithi_idx):
    """tithi_idx is 1..30."""
    karana_idx = (tithi_idx - 1) % 11 if tithi_idx != 0 else 10
    names = ["Bava", "Balava", "Kaulava", "Taitila", "Garija",
             "Vanija", "Vishti", "Shakuni", "Chatushpada", "Naga", "Kimstughna"]
    return karana_idx + 1, names[karana_idx]

# ---------- Vara (weekday) ----------
def compute_vara(jd_ut):
    """0=Sun, 1=Mon, ..., 6=Sat"""
    return int((jd_ut + 1.5) % 7)
```

### 2.4 Layer 3: Rahu Kaal (Inauspicious Times)

```python
def compute_trikalam(sunrise_jd, sunset_jd, weekday):
    """Returns (rahu_start, rahu_end, yama_start, yama_end, gulika_start, gulika_end)."""
    day_dur = sunset_jd - sunrise_jd
    seg = day_dur / 8

    # Offsets by weekday (0=Sun..6=Sat)
    RAHU_OFF = [7, 1, 6, 4, 5, 3, 2]
    YAMA_OFF = [4, 3, 2, 1, 0, 6, 5]
    GULI_OFF = [6, 5, 4, 3, 2, 1, 0]

    rahu = (sunrise_jd + seg * RAHU_OFF[weekday],
            sunrise_jd + seg * (RAHU_OFF[weekday] + 1))
    yama = (sunrise_jd + seg * YAMA_OFF[weekday],
            sunrise_jd + seg * (YAMA_OFF[weekday] + 1))
    guli = (sunrise_jd + seg * GULI_OFF[weekday],
            sunrise_jd + seg * (GULI_OFF[weekday] + 1))
    return rahu, yama, guli
```

### 2.5 Layer 4: Hora (Planetary Hours)

```python
def compute_horas(sunrise_jd, sunset_jd, next_sunrise_jd, weekday):
    """Returns list of {type, lord, start, end} for 24 horas."""
    DAY_RULERS = ["Surya", "Chandra", "Mangala", "Budha",
                  "Guru", "Shukra", "Shani"]
    PLANET_SEQ = ["Shani", "Guru", "Mangala", "Surya",
                  "Shukra", "Budha", "Chandra"]

    day_dur = sunset_jd - sunrise_jd
    night_dur = next_sunrise_jd - sunset_jd
    day_h = day_dur / 12
    night_h = night_dur / 12

    first_lord = DAY_RULERS[weekday]
    lord_idx = PLANET_SEQ.index(first_lord)

    horas = []
    for i in range(12):  # day
        idx = (lord_idx + i) % 7
        horas.append({"type": "day", "lord": PLANET_SEQ[idx],
                       "start": sunrise_jd + i * day_h,
                       "end": sunrise_jd + (i + 1) * day_h})
    for i in range(12):  # night
        idx = (lord_idx + 12 + i) % 7
        horas.append({"type": "night", "lord": PLANET_SEQ[idx],
                       "start": sunset_jd + i * night_h,
                       "end": sunset_jd + (i + 1) * night_h})
    return horas

# Hora activity guidance (LLM reads this)
HORA_ACTIVITIES = {
    "Surya":   "leadership, decisions importantes, visibilite",
    "Chandra": "emotions, relations, intuition, creativite",
    "Mangala": "action, competition, travail physique",
    "Budha":   "communication, ecriture, deals, negociation",
    "Guru":    "signatures, expansion, apprentissage, richesse",
    "Shukra":  "ventes, relations, beaute, plaisir",
    "Shani":   "travail solo, discipline, analyse, restructuration",
}
```

### 2.6 Layer 5: Natal Chart (D1 — Rasi)

```python
def compute_birth_chart(birth_date, birth_time, lat, lon):
    """Full natal chart computation. Called once at GENESIS."""
    jd_birth, _ = swe.utc_to_jd(*birth_date, *birth_time)
    calc = AstraCalculator(lat, lon)

    # 1. Planet positions
    grahas = calc.get_all_grahas(jd_birth)

    # 2. Houses
    cusps, ascmc = calc.get_houses(jd_birth, lat, lon)
    asc_lon = ascmc[0]  # Ascendant (Lagna)
    mc_lon = ascmc[1]   # Midheaven

    # 3. House placement for each graha
    for name, g in grahas.items():
        g["house"] = ((int(g["lon"] / 30) - int(asc_lon / 30)) % 12) + 1

    # 4. Lagna details
    lagna_sign = int(asc_lon / 30)
    lagna_nak = int(asc_lon / (360/27))

    return {
        "jd": jd_birth,
        "grahas": grahas,
        "lagna": {"lon": asc_lon, "sign": lagna_sign, "nakshatra": lagna_nak,
                  "nakshatra_lord": NAK_LORDS[lagna_nak]},
        "mc": mc_lon,
        "houses": cusps,
    }
```

### 2.7 Layer 6: Vimshottari Dasha

```python
DASHA_PERIODS = {  # years
    "Ketu": 7, "Shukra": 20, "Surya": 6, "Chandra": 10,
    "Mangala": 7, "Rahu": 18, "Guru": 16, "Shani": 19, "Budha": 17,
}
DASHA_LORDS = ["Ketu", "Shukra", "Surya", "Chandra", "Mangala",
               "Rahu", "Guru", "Shani", "Budha"]

def compute_vimshottari(birth_jd, moon_lon):
    """Returns list of {lord, start_jd, end_jd, years} for Mahadasha.
       Also computes Antar (sub) and Pratyantar (sub-sub) Dashas."""
    span = 360.0 / 27
    nak_idx = int(moon_lon / span)
    deg_in_nak = moon_lon % span

    start_lord = NAK_LORDS[nak_idx]
    lord_i = DASHA_LORDS.index(start_lord)

    # Balance of first MD
    remaining = 1.0 - (deg_in_nak / span)
    balance_years = DASHA_PERIODS[start_lord] * remaining

    md = []
    current_jd = birth_jd - balance_years * 365.25
    for i in range(9):
        idx = (lord_i + i) % 9
        lord = DASHA_LORDS[idx]
        full = DASHA_PERIODS[lord]
        yrs = balance_years if i == 0 else full
        days = yrs * 365.25
        md.append({
            "lord": lord, "level": 1,
            "start_jd": current_jd, "end_jd": current_jd + days,
            "years": round(yrs, 4),
        })
        current_jd += days

    # Compute Antar Dasha (sub-periods) for current MD
    def antars(md_entry):
        lord_i = DASHA_LORDS.index(md_entry["lord"])
        total_yrs = md_entry["years"]
        subs = []
        for j in range(9):
            idx = (lord_i + j) % 9
            sub_yrs = total_yrs * DASHA_PERIODS[DASHA_LORDS[idx]] / 120.0
            # Actually: (parent_years * child_years) / 120
            sub_days = sub_yrs * 365.25
            subs.append({
                "lord": DASHA_LORDS[idx], "level": 2,
                "years": round(sub_yrs, 4),
            })
        return subs

    return md, antars

def get_current_dasha(dashas, jd_now):
    """Find which Mahadasha + Antar Dasha period contains jd_now."""
    for md in dashas:
        if md["start_jd"] <= jd_now < md["end_jd"]:
            return md
    return None
```

### 2.8 Layer 7: Other Dasha Systems

```python
# ---------- Yogini Dasha (Moon-based, 8 periods of varying years) ----------
YOGINI_PERIODS = {"Mangala": 1, "Shani": 2, "Budha": 3, "Guru": 4,
                   "Chandra": 5, "Shukra": 6, "Surya": 7, "Ketu": 8}
YOGINI_LORDS = ["Mangala", "Shani", "Budha", "Guru", "Chandra",
                "Shukra", "Surya", "Ketu"]

def compute_yogini_dasha(moon_lon):
    """Yogini Dasha based on birth Nakshatra."""
    nak_idx = int(moon_lon / (360/27))
    yogini_idx = nak_idx % 8
    # Similar recursive structure as Vimshottari
    ...

# ---------- Kalachakra Dasha ----------
# Complex sign-based dasha system. Requires complete implementation from
# classical texts. Deployed in Phase 3.

# ---------- Chara Dasha (Jaimini) ----------
# Sign-based dasha where each sign period varies by number of signs to Lagna.
# Deployed in Phase 3.
```

### 2.9 Layer 8: Ashtakavarga (Strength)

```python
def compute_ashtakavarga(graha_lons):
    """Bav (8-fold) and Sav (Sarva = total) Ashtakavarga.
    
    Algorithm: For each planet, count "bindus" (points) based on
    planet positions falling in specific houses from each reference planet.
    
    This is purely algorithmic — no ephemeris needed beyond planet positions.
    """
    # Each of 8 planets (Ketu excluded) contributes 0-8 points per sign
    # Totaled in SAV (0-56 points per sign, but typically 28-42 is average)
    pass  # Full implementation in Phase 2

# ---------- Shadbala (Sixfold Strength) ----------
def compute_shadbala(grahas, houses, lat):
    """Sthana Bala (positional), Dig Bala (directional), Kala Bala (temporal),
       Chesta Bala (motional), Naisargika Bala (natural), Ayana Bala (declination).
    """
    pass  # Full implementation in Phase 3
```

### 2.10 Layer 9: Yogas (Planetary Combinations)

```python
def detect_yogas(grahas, lagna, houses, lat, lon):
    """Detect all active Yogas in the chart. 200+ possible.
    
    Categories (implemented in phases):
    
    Phase 1 (Core 30):
    - Dhana Yogas: lords of 2nd/11th in Kendra/Kona
    - Raja Yogas: Kendra lord + Kona lord
    - Viparita Raja Yogas: lords of 6/8/12 in 6/8/12
    - Chandra-Mangala Yoga: Moon + Mars
    - Budha-Aditya Yoga: Sun + Mercury
    - Gajakesari Yoga: Jupiter + Moon in Kendra
    - Neecha Bhanga Raja Yoga: debilitated planet cancelled
    
    Phase 2 (Intermediate 50):
    - Parvata, Kedar, Rahu-Ketu, Shasha, etc.
    
    Phase 3 (Advanced 120+):
    - Full BPHS + Jaimini catalog
    """
    yogas = []
    # Phase 1 patterns...
    return yogas
```

### 2.11 Layer 10: Arudha Padas (Jaimini)

```python
def compute_arudha(house_lord_lon):
    """Arudha Pada (reflection point) of a house.
    Pada = sign of lord + (sign offset from own house).
    """
    # A(l) = sign(h) + [sign(h) - lagna_sign]
    # If A(l) = sign(h), add 10 signs
    pass  # Phase 2
```

### 2.12 Layer 11: Divisional Charts (Vargas D1-D60)

```python
DIV_CHART_FUNCTIONS = {
    "D1": (1, "Rasi - body/life general"),       # Always computed
    "D2": (2, "Hora - wealth/finance"),
    "D3": (3, "Drekkana - siblings/communication"),
    "D4": (4, "Chaturthamsa - home/property"),
    "D5": (5, "Panchamsa - knowledge/creativity"),
    "D6": (6, "Shashtamsa - health/disease"),
    "D7": (7, "Saptamsa - children"),
    "D8": (8, "Ashtamsa - danger/sudden events"),
    "D9": (9, "Navamsa - spouse/partnership"),   # Always computed
    "D10": (10, "Dasamsa - career/profession"),   # Always computed
    "D12": (12, "Dwadasamsa - parents"),
    "D16": (16, "Shodasamsa - vehicles/comforts"),
    "D20": (20, "Vimsamsa - spirituality"),
    "D24": (24, "Chaturvimsamsa - education/knowledge"),
    "D27": (27, "Saptavimsamsa - strength"),
    "D30": (30, "Trimsamsa - evils/hardships"),
    "D40": (40, "Chatvarimsamsa - maternal lineage"),
    "D45": (45, "Panchachatvarimsamsa - merits"),
    "D60": (60, "Shashtiamsa - karma/past lives"), # Always computed
}

def compute_divisional_chart(graha_lon, div_factor):
    """Compute a planet's position in a divisional chart.
    
    D2 (Hora): divide 30° sign into 15° halves. D1 sign*2 + (deg>15?1:0)
    D3 (Drekkana): divide 30° sign into 10° thirds.
    D9 (Navamsa): divide 30° sign into 9 parts of 3°20' each.
    D10 (Dasamsa): divide 30° sign into 10 parts of 3° each.
    D60 (Shashtiamsa): divide 30° sign into 60 parts of 0°30' each.
    """
    # General formula:
    span = 30.0 / div_factor
    within_sign = graha_lon % 30
    sub = int(within_sign / span)
    # Result sign = (original_sign * div_factor + sub) % 12
    # But each varga has unique mapping rules
    pass  # Full implementation per varga type
```

### 2.13 Layer 12: Transits (Gochara)

```python
def compute_transit_effects(natal_grahas, transiting_grahas, nat_houses):
    """Compare current planet positions to natal chart.
    Returns list of significant transits.
    
    Key transits to detect:
    - Jupiter transit over natal Sun/Moon/Lagna/2nd/11th houses
    - Saturn transit over natal Moon (Sade Sati)
    - Rahu/Ketu transit over natal planets
    - Malefic transit over 1st/2nd/4th/5th/7th/9th/10th houses
    - Benefic transit over 12th/6th/8th houses (Viparita)
    - Eclipse on natal planet
    - Planetary war (conjunction)
    """
    pass
```

### 2.14 Layer 13: Sade Sati (Saturn's 7.5 Year Cycle)

```python
def compute_sade_sati(natal_moon_sign, transit_saturn_sign):
    """Return status: "none", "rising", "peak", "declining", "ended".
    
    Sade Sati = Saturn in 12th, 1st, or 2nd house from natal Moon.
    Phase 1 (12th): ~2.5 years - rising
    Phase 2 (1st): ~2.5 years - peak
    Phase 3 (2nd): ~2.5 years - declining
    """
    moon_idx = natal_moon_sign  # 0..11
    sat_idx = transit_saturn_sign  # 0..11
    dist = (sat_idx - moon_idx) % 12
    if dist == 11:
        return "rising", "Saturne en 12e depuis la Lune: phase de retrait, eliminer l'ancien"
    elif dist == 0:
        return "peak", "Saturne sur la Lune: phase intense, karma, transformations"
    elif dist == 1:
        return "declining", "Saturne en 2e depuis la Lune: phase de reconstruction"
    return "none", None
```

### 2.15 Layer 14: Muhurta (Electional Timing)

```python
# Muhurta scoring: given an event type and a proposed time,
# score 0-100 based on:
# - Tithi (specific tithis favored per event type)
# - Nakshatra (specific nakshatras favored)
# - Day of week (specific days per event)
# - Hora (specific horas per event)
# - Lagna quality at that time
# - Mercury direct/retrograde
# - Jupiter direct/retrograde
# - Rahu Kaal avoidance

EVENT_MUHURTA = {
    "signature_contrat": {
        "best_tithi": [2, 3, 5, 7, 10, 11, 13],  # Tithi 1-indexed
        "best_nakshatra": ["Rohini", "Uttara Phalguni", "Hasta",
                           "Chitra", "Anuradha", "Shravana", "Revati"],
        "best_vara": [4, 5],  # Thursday (Jupiter), Friday (Venus)
        "best_hora": ["Guru", "Shukra", "Budha"],
        "avoid": ["rikta_tithi", "mercury_rx", "rahu_kaal", "sunset"],
    },
    "lancement_produit": {
        "best_tithi": [2, 3, 5, 7, 10, 11],
        "best_nakshatra": ["Ashwini", "Krittika", "Rohini", "Pushya",
                           "Magha", "Chitra", "Shravana", "Dhanishta"],
        "best_vara": [4, 5, 7],  # Thu, Fri, Sun
        "best_hora": ["Guru", "Surya", "Shukra"],
        "avoid": ["amavasya", "eclipse", "mercury_rx"],
    },
    "negociation": {...},
    "cloture_vente": {...},
    "recrutement": {...},
    "voyage": {...},
    "investissement": {...},
    "deep_work": {...},
}

def score_muhurta(event_type, target_jd, lat, lon):
    """Score 0-100 for doing event_type at target_jd."""
    calc = astra_core.AstraCalculator(lat, lon)
    score = 70  # base

    panchanga = compute_panchanga(...)  # tithi, nak, etc.
    horas = compute_horas(...)
    mercur_rx = planet_speed("Budha", target_jd) < 0

    template = EVENT_MUHURTA.get(event_type, EVENT_MUHURTA["signature_contrat"])

    if panchanga["tithi_idx"] in template["best_tithi"]:
        score += 10
    if panchanga["nak_name"] in template["best_nakshatra"]:
        score += 10
    if panchanga["vara_idx"] in template["best_vara"]:
        score += 5
    if current_hora["lord"] in template["best_hora"]:
        score += 10
    if mercur_rx and "mercury_rx" in template.get("avoid", []):
        score -= 25
    if panchanga["rikta"]:
        score -= 15

    return min(max(score, 0), 100)
```

### 2.16 Layer 15: Prasna (Horary)

```python
def compute_prasna(question_time_jd, lat, lon):
    """Answer a question based on the moment it was asked.
    Same calculations as birth chart, but uses question moment
    instead of birth moment. Lagna + Moon position at question
    time = key indicators."""
    # Phase 3 feature
    pass
```

### 2.17 Layer 16: Remedial Measures (Upaya)

```python
# Based on chart weakness, recommend:
REMEDIES = {
    "Surya": {
        "mantra": "Om Suryaya Namaha",
        "repeat": 1000,
        "best_time": "sunrise (Surya Hora)",
        "day": "Sunday",
        "color": "red/copper",
        "food": "donate wheat/jaggery to needy",
        "fasting": "Sunday",
    },
    "Chandra": {
        "mantra": "Om Chandraya Namaha",
        "repeat": 1000,
        "best_time": "evening (Chandra Hora)",
        "day": "Monday",
        "color": "white/silver",
        "food": "donate rice/milk",
        "fasting": "Monday",
    },
    "Mangala": { ... },
    "Budha": { ... },
    "Guru": { ... },
    "Shukra": { ... },
    "Shani": { ... },
    "Rahu": { ... },
    "Ketu": { ... },
}

def recommend_remedies(graha_name, weakness_type):
    """Returns human-readable Upaya suggestions.
    Prioritizes free/no-cost: mantras, fasting, charity timing.
    Gemstone recommendations only if user requests ($$$)."""
    r = REMEDIES.get(graha_name, {})
    return {
        "chanting": f"Om {graha_name}aya Namaha - {r.get('repeat', 108)} times, {r.get('best_time', 'dawn')}",
        "best_day": r.get("day", ""),
        "color": r.get("color", ""),
        "charity": r.get("food", ""),
        "fasting": r.get("fasting", ""),
    }
```

### 2.18 Layer 17: Eclipses

```python
def get_eclipses(year):
    """Use swe.sol_eclipse_when_loc() and swe.lun_eclipse_when().
    Returns list of {type, jd, magnitude, duration} for the year."""
    pass  # Phase 3
```

---

## 3. File Specifications

### 3.1 ASTRA_BIRTH.md

```markdown
# ASTRA Birth Profile

## Birth Data
- **Date:** 1996-12-15 (example)
- **Time:** 14:30 (UTC+0)
- **Location:** Lome, Togo (6.133deg N, 1.217deg E)
- **Source:** Self-reported

## Verification Notes
- Ayanamsa: Lahiri (24.13 deg in 2026)
- Houses: Whole Sign (Parashari)
- Timezone: UTC+0 (no DST)

## Generated
- **Computed:** 2026-06-23
- **By:** astra_birth.py v1.0
```

### 3.2 ASTRA_CHART_D1.md

```markdown
# D1 — Rasi Chart (Natal)

**Birth:** 1996-12-15 14:30 Lome

## Lagna (Ascendant)
- **Sign:** Mesha (Aries) — 12deg 34min
- **Nakshatra:** Ashwini — Pada 3
- **Nakshatra Lord:** Ketu

## Graha Positions
| Graha | Sign | Deg | Nakshatra | Pada | House | Retro |
|-------|------|-----|-----------|------|-------|-------|
| Surya | Dhanu | 3.2 | Mula | 1 | 9 | No |
| Chandra | Karka | 15.7 | Pushya | 3 | 4 | No |
| Mangala | Kumbha | 22.1 | Purva Bhadrapada | 4 | 11 | No |
| Budha | Vrishchika | 8.5 | Anuradha | 2 | 8 | No |
| Guru | Kanya | 25.3 | Chitra | 4 | 7 | No |
| Shukra | Tula | 18.0 | Vishakha | 3 | 7 | No |
| Shani | Mina | 5.0 | Revati | 2 | 12 | No |
| Rahu | Vrishchika | 28.0 | Jyeshtha | 4 | 9 | Yes |
| Ketu | Vrishabha | 28.0 | Mrigashira | 2 | 3 | Yes |

## House Lords
| House | Sign | Lord |
|-------|------|------|
| 1 | Mesha | Mangala |
| 2 | Vrishabha | Shukra |
| ... | ... | ... |

## Bhava (House) Strengths
| House | Planets | Occupied By | Aspect |
|-------|---------|-------------|--------|
| 1 | 1 | Mangala (lord) | ... |
| ... | ... | ... | ... |
```

### 3.3 ASTRA_DASHA.md

```markdown
# Vimshottari Dasha Timeline

**Birth:** 1996-12-15 14:30 Lome (JD 2450600.00)

## Current Period
- **Mahadasha:** Guru (Jupiter) — 2020-01-15 to 2036-01-15
- **Antar Dasha:** Shukra (Venus) — 2025-06-10 to 2028-04-22
- **Pratyantar Dasha:** Surya (Sun) — 2026-03-01 to 2026-07-15

## Full Timeline
| MD Lord | Start | End | Years | Status |
|---------|-------|-----|-------|--------|
| Budha | 1990-05-10 | 2000-01-15 | 9.7 | Past |
| Ketu | 2000-01-15 | 2007-01-15 | 7.0 | Past |
| Shukra | 2007-01-15 | 2020-01-15 | 20.0 | Past |
| **Guru** | **2020-01-15** | **2036-01-15** | **16.0** | **Current** |
| Shani | 2036-01-15 | 2055-01-15 | 19.0 | Future |
| ... | ... | ... | ... | ... |

## Other Dasha Systems
| System | Current Lord | Remaining |
|--------|-------------|-----------|
| Yogini | Shani | 3 months |
| Kalachakra | TBD | TBD |
| Chara (Jaimini) | TBD | TBD |

## Next Transitions
- Pratyantar ends: 2026-07-15 (Surya -> Chandra AD)
- **21 days**: Mercury retrograde enters
- **90 days**: Jupiter transit to next sign
```

### 3.4 ASTRA_DAILY.md

```markdown
# ASTRA Daily — 2026-06-23

**Lome, UTC+0** — Generated at 00:30:00

## Panchanga
- **Vara:** Mangalavara (Mardi)
- **Tithi:** Dashami (Shukla Paksha) — favorable
- **Nakshatra:** Chitra (27.3 deg Vierge) — Pada 1
- **Yoga:** Parigha (Bon)
- **Karana:** Vanija (Bon pour le commerce)

## Sun & Moon
- **Lever:** 05:42
- **Coucher:** 18:11
- **Soleil:** Gemeaux 7.8 deg (Mula Nakshatra)
- **Lune:** Vierge 26.3 deg (Chitra Nakshatra)

## Planetary Hours (Horas)
| Hora | Debut | Fin | Planete | Activite |
|------|-------|-----|---------|----------|
| 1 | 05:42 | 06:42 | Surya | Leadership, decisions |
| 2 | 06:42 | 07:42 | Shukra | Ventes, beaute |
| 3 | 07:42 | 08:42 | Budha | Communication, deals |
| ... | ... | ... | ... | ... |
| **7** | **11:57** | **12:59** | **Guru** | **Signatures, expansion** |
| 8 | 12:59 | 14:01 | Shani | Analyse |
| 9 | 14:01 | 15:03 | Surya | Decisions |
| 10 | 15:03 | 16:05 | Shukra | Ventes |
| 11 | 16:05 | 17:07 | Budha | Communication |
| 12 | 17:07 | 18:11 | Chandra | Intuition |

## Inauspicious Times
- **Rahu Kaal:** 15:04 - 16:38 — Eviter decisions importantes
- **Yamaganda:** 06:42 - 07:54 — Eviter commencer voyages
- **Gulika Kaal:** 10:18 - 11:30 — Eviter operations chirurgicales

## Transit Highlights
- **Saturne en Poissons (19.6 deg)** — En 12e maison natale
- **Soleil en Gemeaux** — Active maison 11: revenus, reseaux
- **Lune en Chitra (Vierge)** — Active maison 5: creativite, speculation

## Today's Guidance
- **En ce moment:** Hora Guru (11:57-12:59) — Bon pour signatures, decisions d'expansion
- **Eviter:** Rahu Kaal (15:04-16:38)
- **Conseil du jour:** Lune en Chitra design/opportunites. Bon pour lancer des projets
- **Meilleure fenetre:** 11:57-12:59 + 16:05-17:07

## Dasha Context
- **MD:** Guru (expansion, sagesse)
- **AD:** Shukra (argent, partenariats)
- **PD:** Surya (autorite, visibilite)
```

### 3.5 ASTRA_TRANSITS.md

```markdown
# ASTRA Transits — 2026-06-23

## Current Transits vs Natal
| Transit Planet | Natal Point | Aspect | Effect | Window |
|---------------|-------------|--------|--------|--------|
| Guru (Jupiter) | Lagna (Asc) | Trine (120deg) | Favorable — 7 jours | 2026-06-20 to 2026-06-27 |
| Shani (Saturn) | Chandra (Moon) | 12th from Moon | Sade Sati Phase 1: rising | 2025-03 to 2027-09 |
| Rahu | Ketu (natal) | Conjunction | Intense karma | 2026-05 to 2026-11 |

## Upcoming Events
| Event | Date | Type | Impact |
|-------|------|------|--------|
| Mercure retrograde | 2026-07-15 | Rx | Contracts/buying pause |
| Surya transit to Karka | 2026-07-16 | Transit | Maison 4 active |
| Guru transit to Simha | 2026-08-01 | Transit | Major — sign change |
| Eclipse lune | 2026-08-04 | Eclipse | Maison 5 active |
```

### 3.6 ASTRA_SADE_SATI.md

```markdown
# Sade Sati Status

**Natal Moon:** Karka (Cancer)

## Current Phase
- **Phase:** Rising (Saturn in 12th from Moon)
- **Saturne en:** Poissons
- **Maison natale:** 12e
- **Debut:** 2025-03-15
- **Phase 2 (Peak) starts:** 2027-09-20

## Guidance
Le Sade Sati (phase ascendante) est un cycle de retrait:
- Eliminer ce qui ne sert plus
- Eviter les expansions majeures
- Travailler sur la discipline, la solitude
- Bon pour la spiritualite, l'introspection

## Remedes Recommandes
- Hanuman Chalisa (mardi)
- Donner des lentilles noires le samedi
- Porter du bleu fonetre (si budget le permet)
```

### 3.7 ASTRA_YOGAS.md

```markdown
# Active Yogas in Natal Chart

## Raja Yogas
- Guru + Shukra en Kendra (maison 7) → **Hamsa Yoga**: sagesse, richesse
- Mangala lord lagna en Kendra → **Ruchaka Yoga**: pouvoir, leadership

## Dhana Yogas
- Lord 2 + Lord 11 en Kendra → **Dhana Yoga**: accumulation de richesse

## Other Yogas
- Surya + Budha conjoints → **Budha-Aditya Yoga**: intelligence, communication
```

### 3.8 ASTRA_ARUDHA.md

```markdown
# ASTRA Arudha Padas

| Pada | Signe | Signification |
|------|-------|---------------|
| A1 (Lagna) | Mithuna | Comment le monde vous percoit |
| A2 (Dhana) | Karka | Perception de vos finances |
| A3 (Sahaja) | Simha | Perception de vos relations |
| A4 (Bandhu) | Kanya | Perception de votre foyer |
| A5 (Putra) | Tula | Perception de vos creations |
| A6 (Shatru) | Vrishchika | Perception de vos defis |
| A7 (Yuvati) | Dhanu | Perception de vos partenariats |
| A8 (Randhra) | Makara | Perception de vos crises |
| A9 (Dharma) | Kumbha | Perception de votre chance |
| A10 (Karma) | Mina | Perception de votre carriere |
| A11 (Labha) | Mesha | Perception de vos gains |
| A12 (Vyaya) | Vrishabha | Perception de vos depenses |

## Arudha Lagna Insights
- A1 en Mithuna → percu comme intelligent, communicatif
- A5 en Tula → creations perçues comme belles
- A10 en Mina → carriere perçue comme spirituelle/creative
```

### 3.9 ASTRA_DAILY.md Integration (Boot Banner)

When the LLM boots, AFTER reading CURRENT_STATE and before proposing actions, it loads all ASTRA state files and produces:

```
[ASTRA] ─────────────────────────────────────────
  Aujourd'hui: Mardi (Mars) | Dashami Shukla
  Lune en Chitra — design, opportunites
  Hora: Guru (11:57-12:59) — expansion/signatures
  Eviter Rahu Kaal 15:04-16:38

  Dasha: Guru MD + Shukra AD + Surya PD
         => Expansion commerciale en cours

  Sade Sati: Phase 1 (rising) — eliminer l'ancien

  Meilleure fenetre: 12:00-13:00 + 16:00-17:00
  → "Bon moment pour relancer ST Digital et Sojaco"
─────────────────────────────────────────────────
```

### 3.10 TIMELINE Tagging

Every TIMELINE entry gets tagged with astral context at the moment of the event/decision:

```
---
## 2026-06-23

### Event: Relance ST Digital
- **ASTRA:** Tithi Dashami, Hora Guru, Lune Chitra — favorable
- **Decision:** Relancer avec offre package
- **Outcome:** En attente
---
```

---

## 4. Integration Points

### 4.1 GENESIS (First Boot)

```
GENESIS Step (e): Build Profile
  → Existing questions (domain, role, stack, needs, constraints, geography, projects)
  → NEW: "Date, heure et lieu de naissance (pour ASTRA)"

GENESIS Step (f): Run astra_birth.py
  → Reads ASTRA_BIRTH.md
  → Computes all charts
  → Writes ASTRA_CHART_D1.md, ASTRA_DASHA.md, ASTRA_YOGAS.md, etc.
  → Produces "ASTRA Profile Completer" summary

GENESIS Step (g): Display ASTRA Summary
  → "Voici ce que votre chart revel:"
    - Lagna, Nakshatra, Dasha actuelle
    - Forces, defis
    - Guide pour le mode SURVIVAL actuel
```

### 4.2 DAILY Boot (Every Session)

```
1. astra_daily.py runs (via timekeeper at 00:30)
   → Writes ASTRA_DAILY.md

2. LLM loads ASTRA_DAILY.md + ASTRA_DASHA.md + ASTRA_SADE_SATI.md
   + ASTRA_TRANSITS.md + ASTRA_ECLIPSES.md
   → Produces ASTRA banner in boot sequence

3. DECISION_ENGINE checks: "Is this decision compatible with current timing?"
   → "Tu veux signer un contrat. Mercure est en Cancer (bon) mais Rahu Kaal
      est dans 2h. On attend?"
```

### 4.3 DECISION ENGINE

```python
# Current: PROACT framework
# P - Problem
# R - Requirements
# O - Options
# A - Assessment
# C - Choice
# T - Trigger

# With ASTRA:
# A - Assessment gets astral overlay:
#   astra_score = astra_core.score_muhurta(event_type, now, lat, lon)
#   if astra_score < 40: flag as "timing suboptimal"
#   if astra_score > 80: flag as "timing excellent"

# T - Trigger becomes:
#   "Executer dans X heures pendant la prochaine Hora favorable"
```

### 4.4 PATTERN CORRELATION (Learning Loop)

```python
# Over time, ASTRA_PATTERNS.md accumulates:
# | Outcome | Tithi | Nakshatra | Hora | Dasha AD | Vara |
# |---------|-------|-----------|------|----------|------|
# | Win     | Dwitiya | Rohini | Guru | Shukra | Friday |
# | Loss    | Chaturthi | Ashlesha | Shani | Rahu | Tuesday |

# Every 30 entries: run correlation analysis
# "Sur 30 decisions, 80% des wins etaient en Hora Guru.
#  Votre meilleure fenetre = Jeudi/Guru Hora."
```

### 4.5 ALERTS (timekeeper + watchtower)

```python
# timekeeper (every 30 min) with --astra flag:
# 1. Check if current time is Rahu Kaal -> no alert (it's expected)
# 2. Check if Hora changed -> write to ASTRA_DAILY
# 3. Check if current hora is good for today's priority

# watchtower (every 6h) with ASTRA watch items:
# 1. Upcoming transit within 7 days
# 2. Dasha change within 14 days
# 3. Eclipse within 14 days
# 4. Mercury retrograde start within 7 days
# -> Windows Toast alert
```

---

## 5. Implementation Phases

### Phase 0: ASTRA Nervous System + Foundations (3-5 days)
- [ ] **Redefine SYSTEM_PROMPT.md**: The LLM's persona becomes ASTRA — everything filtered through the astral lens
- [ ] **Redefine every module interface**: CURRENT_STATE, TIMELINE, ALERTS, MEMORY each get an ASTRA node
- [ ] **Install pysweph**, verify works with Moshier ephemeris
- [ ] Write `astra_core.py` with all Layer 0-5 calculations
- [ ] Write `astra_daily.py` that computes today's Panchang + Horas + Rahu Kaal + Emotional Forecast
- [ ] Write `astra_birth.py` for D1 chart computation
- [ ] Define all state file templates
- [ ] Define **ASTRA persona prompt**: how the LLM-as-astrologer thinks, speaks, and interjects
- [ ] Define **interjection rules**: when ASTRA speaks unprompted (Rahu Kaal imminent, transit window, hora change)
- [ ] Test: full boot where ASTRA speaks first, before any user input

### Phase 1: GENESIS + DAILY Integration (3-5 days)
- [ ] Add birth data questions to GENESIS profile step
- [ ] Wire `astra_birth.py` into GENESIS (run after birth data collected)
- [ ] Wire `astra_daily.py` into timekeeper (30min trigger)
- [ ] Update LLM boot sequence to load ASTRA_DAILY.md (banner)
- [ ] Update DECISION_ENGINE to include "timing overlay"
- [ ] First user test: full GENESIS → boot → decision flow

### Phase 2: Core Astrology (5-7 days)
- [ ] D1 chart: house lords, bhava strengths, aspects
- [ ] Vimshottari Dasha: full MD + AD + PD + calculation
- [ ] Ashtakavarga: SAV tables
- [ ] Mugurta scoring: 10 event types with score modeling
- [ ] Sade Sati: full cycle tracking + alerts
- [ ] Daily alerts: transit detection pipeline
- [ ] Yogas: top 30 (Dhana, Raja, Viparita, etc.)

### Phase 3: Advanced (7-10 days)
- [ ] Divisional charts: D10, D60, D9
- [ ] Arudha Padas: all 12 with interpretation
- [ ] Shadbala: sixfold strength
- [ ] Yogas expansion: 200+ detection
- [ ] Yogini Dasha + Kalachakra Dasha
- [ ] Eclipse detection + alerts
- [ ] Pattern correlation engine
- [ ] Color/action recommendations per day

### Phase 4: Polish (ongoing)
- [ ] Jaimini Sutras
- [ ] Prasna (horary)
- [ ] Compatibility analysis (for partnerships/team)
- [ ] Annual chart (Varshaphal)
- [ ] Batch chart recomputation when ayanamsa updates
- [ ] TIMELINE retro-tagging (tag past entries with astral context)

---

## 6. Testing Strategy

### Calculation Tests
- Cross-validate against AstroSage or Jagannatha Hora for same date/location
- Tithi, Nakshatra, Rahu Kaal should match known panchang
- Dasha end/start dates should match known examples (e.g., Gandhi's chart)

### Integration Tests
- `astra_daily.py` output can be parsed as valid markdown
- State files never grow unbounded (fixed-size templates)
- Alert pipeline fires within timekeeper constraints (<30s per run)

### User Tests
- Phase 1 test: new user goes through GENESIS → sees ASTRA banner → makes decision
- Phase 2 test: user sees proactive transit/Dasha alerts in boot
- Phase 3 test: user sees pattern correlation after 10+ decisions

---

## 7. Narrative Thread — Life Story Engine

### 7.1 Problem with Daily Snippets

The current spec produces one-day-at-a-time guidance. An entrepreneur needs **story arcs** — understanding where they are in their multi-year journey. A daily-only ASTRA is like reading a book one word per day without knowing what chapter you're in.

### 7.2 Architecture: Temporal Story Layers

```
Layer: Narrative Track
├── Macro (years)   → Dasha period: "You are in Guru MD (2020-2036) - expansion arc"
├── Meso (months)   → Transit: "Jupiter enters Simha Aug 2026 - career acceleration"
├── Micro (days)    → Daily: "Tithi Dashami, Hora Guru - good for signatures"
└── Nano (hours)    → Hora: "Next 48min = Jupiter hora - use for priority decisions"
```

### 7.3 State File: ASTRA_NARRATIVE.md

```markdown
# ASTRA Narrative — Life Arc

## Current Chapter
- **Mahadasha:** Guru (Jupiter) — 2020-01-15 to 2036-01-15
- **Theme:** Expansion, wisdom, abundance
- **Sub-chapter (AD):** Shukra (Venus) — 2025-06-10 to 2028-04-22
- **Sub-theme:** Financial growth through partnerships, creativity

## The Story So Far
| Period | Dasha | Theme | What Happened |
|--------|-------|-------|---------------|
| 1990-2000 | Budha | Learning | Education foundations |
| 2000-2007 | Ketu | Detachment | Formative challenges |
| 2007-2020 | Shukra | Wealth, pleasure | Career building, creative work |
| 2020-2036 | Guru | Expansion | KORA, OMNI, SOJACO — current |

## What This Chapter Demands
- **Guru MD:** Build systems, teach others, expand reach, seek wisdom
- **Shukra AD:** Monetize creativity, form partnerships, beautify offerings
- **Surya PD (current):** Take leadership position, increase visibility

## What Happens Next
- **2036-2055:** Shani MD — Infrastructure, discipline, institutional building
- **2055-2072:** Budha MD — Communication, advisory, writing legacy
```

### 7.4 Integration

Every session boot, before the daily banner, the narrative is loaded:

```
[ASTRA] Chapitre actuel: Guru MD (expansion) — Shukra AD (argent/partenariats)
        Il te reste 9.5 ans dans Guru. Le sous-chapitre Shukra dure 2.9 ans
        → Objectif de ce chapitre: construire KORA jusqu'a pre-seed
        → Ce que tu fais MAINTENANT determine la suite (Shani MD = institution)
```

### 7.5 File Updates

- **New:** `State/ASTRA_NARRATIVE.md` — generated at GENESIS, updated on Dasha change
- **Modified:** `ASTRA_DAILY.md` — adds "Chapter Context" section at top

---

## 8. Emotional-Energy Mapping

### 8.1 Problem

The spec tells you what to DO but not how you'll FEEL. Yet emotional state determines everything — when to push, when to rest, when to create, when to administrate.

### 8.2 Architecture: Emotional Forecast Engine

Each day gets an emotional/energy profile computed from:

```python
def compute_daily_mood(jd_now, natal_moon_sign, transit_grahas):
    """Score 0-100 on 4 axes: energy, focus, mood, sociability."""
    factors = {
        "tithi_factor": score_tithi_mood(tithi_idx),
        "nakshatra_factor": score_nak_mood(nak_idx),
        "moon_phase_factor": score_moon_phase(tithi_idx),
        "transit_moon_factor": score_moon_transit(transit_moon_sign, natal_moon_sign),
        "day_factor": score_weekday_mood(vara_idx),
    }
    # Weighted average per axis
    return {
        "energy": weighted_avg(energy_factors),
        "focus": weighted_avg(focus_factors),
        "mood": weighted_avg(mood_factors),
        "sociability": weighted_avg(sociability_factors),
    }
```

### 8.3 Nakshatra Emotional Signatures

Each nakshatra has a distinct emotional quality that colors the day:

```python
NAK_MOOD = {
    "Ashwini": "Impulsive, energetic, ready to start — canalise dans l'action rapide",
    "Bharani": "Intense, transformative, raw — bon pour creuser, pas pour vendre",
    "Krittika": "Sharp, cutting, precise — bon pour decisions difficiles",
    "Rohini": "Warm, creative, nurturing — bon pour creation de contenu, design",
    "Mrigashira": "Curious, searching, soft — bon pour recherche, pas pour conclusion",
    "Ardra": "Stormy, disruptive, scattered — eviter decisions, bon pour brainstorm",
    "Punarvasu": "Returning, renewing, hopeful — bon pour reconnecter",
    "Pushya": "Nourishing, building, calm — tres favorable, bon pour tout construire",
    "Ashlesha": "Entwined, intuitive, possessive — bon pour negocier, attention manipulation",
    "Magha": "Authoritative, ancestral, proud — bon pour leadership, pas pour humilite",
    "Purva Phalguni": "Playful, creative, pleasure — bon pour creation, ventes",
    "Uttara Phalguni": "Steady, generous, partnership — bon pour mariage, partenariats",
    "Hasta": "Crafty, skilled, precise — bon pour travail manuel, artisanat",
    "Chitra": "Designer, beautiful, opportunity — bon pour design, architecture",
    "Swati": "Independent, airy, balanced — bon pour commerce, autonomie",
    "Vishakha": "Focused, radiant, goal-oriented — bon pour execution, feu",
    "Anuradha": "Devoted, successful, cooperative — bon pour equipe, projets communs",
    "Jyeshtha": "Powerful, protective, hidden — bon pour protection, attention ego",
    "Mula": "Root, destruction, searching — bon pour arracher, purifier",
    "Purva Ashadha": "Victorious, purifying, assertive — bon pour lancer, conquerir",
    "Uttara Ashadha": "Persevering, determined, stable — bon pour tenir, finir",
    "Shravana": "Listening, learning, teaching — bon pour apprentissage, enseignement",
    "Dhanishta": "Wealthy, musical, rhythmic — bon pour finance, art",
    "Shatabhisha": "Healing, mysterious, solitary — bon pour solitude, recherche",
    "Purva Bhadrapada": "Fiery, transformative, intense — bon pour transformation",
    "Uttara Bhadrapada": "Deep, healing, closing — bon pour fin de cycle, guerison",
    "Revati": "Traveling, protecting, ending — bon pour voyage, fin de projet",
}
```

### 8.4 Integration

In ASTRA_DAILY.md:

```
## Emotional Forecast
- **Energie:** 78/100 (Bon — Tithi favorable + Lune en Chitra)
- **Focus:** 62/100 (Moyen — Mercure aspecte par Rahu)
- **Humeur:** 85/100 (Excellent — Shukra AD + Guru MD)
- **Sociabilite:** 45/100 (Faible — Lune en aspect avec Shani)

→ Aujourd'hui, privilegie le design et la creation (Chitra).
→ La sociabilite est basse — evite les appels clients importants.
→ Bon pour avancer KORA design, moins bon pour SOJACO nego.
```

### 8.5 File Updates

- **Modified:** `ASTRA_DAILY.md` — adds "Emotional Forecast" section
- **Engine:** `astra_core.compute_daily_mood()` function

---

## 9. Product Astrology — Thèmes Astrals des Produits

### 9.1 Problem

FounderHQ gère 5+ produits (KORA, OMNI, SOJACO, DoodleMind, Pest Repeller). Chacun a une date de naissance — moment du premier commit, de l'idée, du lancement. Ces produits ont leur propre chart et leur propre vie astrale.

### 9.2 Architecture

```python
PRODUCTS = {
    "KORA Lab": {
        "birth": {"date": "2026-02-15", "time": None, "place": "Lome", "event": "first_idea"},
        "type": "AI Lab",
        "dasha": None,  # computed
    },
    "OMNI": {
        "birth": {"date": "2026-05-01", "time": None, "place": "Lome", "event": "MVP_deploy"},
        "type": "Platform",
    },
    "SOJACO": {
        "birth": {"date": "2026-06-15", "time": None, "place": "Lome", "event": "first_sale"},
        "type": "Commerce",
    },
    "DoodleMind": {
        "birth": {"date": "2026-06-18", "time": None, "place": "Lome", "event": "first_short"},
        "type": "Content",
    },
    "Pest Repeller": {
        "birth": {"date": "2026-05-20", "time": None, "place": "Lome", "event": "stock_acquired"},
        "type": "Product",
    },
}
```

### 9.3 State File: ASTRA_PRODUCTS.md

```markdown
# Product Astrology

## KORA Lab
- **Birth:** 2026-02-15 (first idea) — Lome
- **Chart:** Lagna en [X], Lune en [Y], Dasha actuelle: [Z]
- **Current Transit:** Jupiter en Cancer active la maison 10 (carriere)
- **Status:** Guru transit favorable — bonne periode pour levée de fonds
- **Advice:** Investis dans KORA maintenant (Guru AD est favorable)

## OMNI
- **Birth:** 2026-05-01 (MVP deploy)
- **Chart:** Lagna en [X], Lune en [Y]
- **Current Transit:** Saturn en Poissons, maison 8 — restructuration necessaire
- **Status:** Periode de consolidation, pas d'expansion
- **Advice:** Attend la fin du transit Saturn en 8 avant de scaler

## SOJACO
- **Birth:** 2026-06-15 (first sale)
- **Chart:** ...
- **Current:** Lune favorable pour negociations cette semaine
- **Advice:** Bon pour renégocier Atakpamé ce jeudi (Hora Jupiter)
```

### 9.4 Integration

Boot banner adapte selon le produit actif:

```
[ASTRA] Produit actif: SOJACO
        Le chart de SOJACO montre: Lune favorable aujourd'hui pour negociations
        → Bon moment pour renégocier Atakpame (350 FCFA/kg -> 325?)
        → Hora Jupiter 11:57-12:59 -> ideal pour appel fournisseur
```

### 9.5 File Updates

- **New:** `State/ASTRA_PRODUCTS.md` — computed at GENESIS, updated daily
- **Engine:** `astra_core.compute_product_chart(name, date, place)`

---

## 10. 30-Day Landscape — Le Paysage du Mois

### 10.1 Problem

Daily-only blinders. An entrepreneur needs to see the **upcoming terrain** — what's coming, so they can prepare, accelerate, or hold.

### 10.2 Architecture

```python
def compute_30day_landscape(jd_start, lat, lon, natal):
    """Scan next 30 days for key events. Returns structured panorama."""
    landscape = {
        "good_timing_windows": [],
        "avoid_windows": [],
        "key_transits": [],
        "best_days_by_activity": {},
    }
    for day_offset in range(30):
        jd = jd_start + day_offset
        # Compute daily panchanga
        # Detect Rahu Kaal times
        # Score for each event type (signature, negotiation, launch, deep work)
        # Flag planetary events
    return landscape
```

### 10.3 State File: ASTRA_30DAY.md

```markdown
# 30-Day Landscape — 2026-06-23 to 2026-07-22

## Overview
```
FW    |    Semaine 1   |    Semaine 2   |    Semaine 3   |    Semaine 4
Score |  🟢 82/100      |  🟡 65/100      |  🔴 45/100      |  🟢 78/100
```

## Key Events
| Date | Event | Impact |
|------|-------|--------|
| Jun 24 | Lune en Swati | Bon pour commerce, autonomie |
| Jun 28 | Jupiter Hora prolongée | Bon pour signatures toute la journée |
| **Jul 15** | **Mercure retrograde debut** | **🔴 STOP signatures, contrats, lancements** |
| Jul 16 | Surya transit Karka | Activation maison 4 (foyer, base) |
| **Aug 1** | **Guru transit Simha** | **🟢 MAJEUR — sign-change, opportunite** |

## Strategic Recommendations

### Semaine 1 (Jun 23-29) — 🟢 Favorable
- Signer les contrats (Mercure encore direct)
- Négocier les prix fournisseurs
- Lancer les campagnes

### Semaine 2 (Jun 30 - Jul 6) — 🟡 Neutre
- Travail interne, prepa
- Eviter les decisions majeures

### Semaine 3 (Jul 7-14) — 🔴 Prepare
- Verrouiller tout avant Mercure Rx
- Finaliser les contrats en cours
- Prep pour periode de revision

### Semaine 4 (Jul 15-22) — Mercure Rx
- Pas de nouveaux contrats
- Reviser, corriger, reconnecter
- Planifier la suite

## Priority Action
**Verrouille les contrats Sojaco et KORA avant le 14 juillet.**
Apres, Mercure retrograde — impossible de signer proprement pendant 3 semaines.
```

### 10.4 Integration

Le 30-day landscape est chargé une fois par semaine (pas tous les jours — pas de surcharge). Intégré au boot du Lundi.

### 10.5 File Updates

- **New:** `State/ASTRA_30DAY.md` — updated weekly by watchtower
- **Engine:** `astra_core.compute_30day_landscape()`

---

## 11. Competitive Advantage Engine

### 11.1 Problem

The spec says "guidance" but doesn't answer the question that matters: **"What gives me an edge over everyone else?"**

### 11.2 Architecture: Strategic Overlays

Each overlay maps astral data to exploitable advantages:

```python
def compute_advantages(natal, transits, dasha):
    advantages = []

    # 1. Arudha Lagna overlay
    # The world sees you as your Arudha Lagna (AL).
    # Strong AL in communicative sign -> play that card
    # Weak AL -> compensate
    al = compute_arudha_lagna(natal)
    if al.sign in [3, 6, 9, 12]:  # Mutable signs
        advantages.append({
            "domain": "branding",
            "insight": f"Le monde te percoit comme {al.sign_name} — joue la carte {al.quality}",
            "action": "Positionne-toi comme expert communicant, pas comme operateur",
        })

    # 2. Dasha overlay per domain
    # Certain Dashas favor certain activities
    dasha_adv = {
        "Guru": {
            "advantages": ["expansion", "teaching", "fundraising"],
            "risk": "overconfidence, over-expansion",
            "best_moves": "Build institutions, form authority, teach your method",
        },
        "Shani": {
            "advantages": ["discipline", "structure", "long-term"],
            "risk": "delay, obstruction, solitude",
            "best_moves": "Systematize, automate, cut what doesn't serve",
        },
        "Rahu": {
            "advantages": ["innovation", "tech", "risk-taking"],
            "risk": "illusion, scandal, instability",
            "best_moves": "Pursue moonshots, explore new tech, go global",
        },
        # ... each planet
    }

    # 3. Transit overlay per active product
    for product in active_products:
        transit_score = score_product_transit(product, transits)
        if transit_score > 80:
            advantages.append({
                "domain": product.name,
                "insight": f"{product.name} traverse une fenetre favorable",
                "action": f"Pousse {product.name} maintenant — fenetre de {best_window.days} jours",
            })

    return advantages
```

### 11.3 State File: ASTRA_ADVANTAGES.md

```markdown
# Competitive Advantages — June 2026

## Current Active Advantages

### 🟢 Guru MD + Shukra AD
**Window:** 9.5 years remaining (2026-2036)
**Advantage:** Phase d'expansion naturelle — opportunites viennent a toi
**Playbook:**
- Tu es credible en mode "fondateur qui scale" — pas en mode survie
- Les investisseurs ressentent Guru — leve plus facile
- Les partenariats marchent mieux (Shukra AD)

### 🟢 Arudha Lagna en Mithuna
**Advantage:** Le marche te percoit comme intelligent et communicant
**Exploite:** Content marketing, thought leadership, education
**Evite:** Role d'operateur ou d'executant — tu ne seras pas pris au serieux

### 🟡 KORA en Guru Transit
**Window:** 2026-06-20 to 2026-06-27
**Advantage:** Jupiter en trine au lagna de KORA — fenetre de levée
**Action:** Relancer ST Digital CETTE SEMAINE, soumettre programmes

### 🔴 Sade Sati Phase 1
**Window:** 2025-03 to 2027-09
**Advantage:** Phase de retrait = bon pour eliminer, restructurer, se preparer
**Risk:** Ne pas expandre agressivement, ne pas prendre de dettes
**Action:** Utiliser cette fenetre pour nettoyer SOJACO et KORA
```

### 11.4 Integration

Le Competitive Advantage Engine est chargé dans le **ORIENT** phase du boot, entre l'état actuel et la décision. Il répond à : "Sachant qui tu es, ce que traversent tes produits, et ce que le marché perçoit — quel est ton avantage unique aujourd'hui ?"

### 11.5 File Updates

- **New:** `State/ASTRA_ADVANTAGES.md` — updated daily
- **Engine:** `astra_core.compute_advantages()`

---

## 12. Shadow Mode — Anti-Guidance (Ce qu'il ne faut PAS faire)

### 12.1 Problem

The spec is all about positive guidance. But the most valuable thing astrology can tell you is **when to NOT do something**. An entrepreneur in SURVIVAL mode can't afford suboptimal timing.

### 12.2 Concept: Red Zones

```python
def detect_red_zones(jd_now, natal, transits):
    """Return list of active prohibitions with severity (WARN/HIGH/CRITICAL)."""
    red = []

    # 1. Rahu Kaal active?
    if is_in_rahu_kaal(jd_now):
        red.append({"type": "CRITICAL", "window": "15:04-16:38",
                     "rule": "Ne RIEN commencer d'important", "why": "Rahu Kaal"})

    # 2. Mercury retrograde?
    if is_retrograde("Budha", jd_now):
        red.append({"type": "HIGH", "window": "Jul 15 - Aug 7",
                     "rule": "Pas de contrats, pas de lancements, pas d'achats majeurs",
                     "why": "Mercure retrograde (Rishta)"})

    # 3. Saturn in 8th house transit?
    saturn_house = get_transit_house("Shani", jd_now, natal)
    if saturn_house == 8:
        red.append({"type": "WARN", "window": str(saturn_window),
                     "rule": "Eviter les investissements risques, les conflits legaux",
                     "why": "Shani en maison 8 (crise, transformation)"})

    # 4. Eclipse window?
    if is_in_eclipse_window(jd_now):
        red.append({"type": "HIGH", "window": eclipse_date,
                     "rule": "Nouveaux contrats, signatures, revelations",
                     "why": "Fenetre d'eclipse (informations cachees)"})

    # 5. Rikta Tithi?
    if is_rikta(tithi_idx):
        red.append({"type": "WARN", "window": "toute la journee",
                     "rule": "Lancements, mariage, achats importants",
                     "why": "Tithi Rikta (vide)"})

    # 6. Sade Sati current phase?
    sade = compute_sade_sati(natal)
    if sade["phase"] != "none":
        red.append({"type": "WARN", "window": sade["window"],
                     "rule": "Expansion agressive, gros risques financiers",
                     "why": sade["reason"]})

    return red
```

### 12.3 State File: ASTRA_SHADOW.md

```markdown
# ASTRA Shadow Mode — Active Prohibitions

| Severite | Periode | Regle | Raison |
|----------|---------|-------|--------|
| CRITICAL | 15:04-16:38 | Rien commencer | Rahu Kaal (actif maintenant) |
| HIGH | Jul 15 - Aug 7 | Pas de contrats | Mercure retrograde |
| WARN | 2025-03 - 2027-09 | Expansion moderee | Sade Sati Phase 1 |
| WARN | 2026-06-23 | Contrats/lancements evites si possible | Chaturthi Rikta |

## Immediate Blockers
- [CLOCK] Rahu Kaal dans 2h (15:04-16:38) — prepare les signatures pour apres
- [CALENDAR] Mercure Rx commence dans 22 jours — verrouille les contrats maintenant
```

### 12.4 Integration

Le Shadow Mode est **systématiquement affiché** au boot, avant toute suggestion positive. Indépendant du mode SURVIVAL/GROWTH — ce sont des contraintes absolues.

```
[ASTRA] ⚠ ACTIF: Rahu Kaal 15:04-16:38 (eviter decisions)
        ⚠ Mercure Rx dans 22j — verrouiller contrats avant
        ⚠ Sade Sati Phase 1 — pas d'expansion agressive
```

### 12.5 File Updates

- **New:** `State/ASTRA_SHADOW.md` — updated with every astra_daily.py run
- **Engine:** `astra_core.detect_red_zones()`

---

## 13. Continuous Learning Loop — Pattern Engine

### 13.1 Problem

The spec says "pattern correlation" but doesn't define how it works. Without a concrete mechanism, it won't be built.

### 13.2 Architecture: Decision → Outcome → Astral Tag → Correlation

```python
class AstraLearningLoop:
    """Every decision gets tagged. Every outcome gets logged.
    After N entries, correlation analysis runs automatically."""

    def __init__(self):
        self.entries = []

    def tag_decision(self, decision_text, decision_type, jd_now, outcome=None):
        """Tag a TIMELINE entry with full astral context at decision moment."""
        tag = {
            "timestamp": jd_now,
            "tithi": compute_tithi(sun_lon, moon_lon),
            "nakshatra": compute_nakshatra(moon_lon),
            "hora": get_current_hora(jd_now),
            "vara": compute_vara(jd_now),
            "md": get_current_md(dashas, jd_now),
            "ad": get_current_ad(dashas, jd_now),
            "mercury_rx": is_retrograde("Budha", jd_now),
            "decision_type": decision_type,
            "outcome": outcome,  # "win", "loss", "pending"
        }
        self.entries.append(tag)
        return tag

    def correlate(self, min_entries=10):
        """After min_entries with outcomes, find patterns."""
        from collections import Counter

        wins = [e for e in self.entries if e["outcome"] == "win"]
        losses = [e for e in self.entries if e["outcome"] == "loss"]
        pending = [e for e in self.entries if e["outcome"] == "pending"]

        if len(wins) + len(losses) < min_entries:
            return None

        patterns = []

        # Check each astral factor for correlation
        for factor in ["tithi", "nakshatra", "hora", "vara", "md", "ad", "mercury_rx"]:
            win_dist = Counter(w[factor] for w in wins)
            loss_dist = Counter(l[factor] for l in losses)

            # Find overrepresented values in wins vs losses
            for value in set(list(win_dist.keys()) + list(loss_dist.keys())):
                w_count = win_dist.get(value, 0)
                l_count = loss_dist.get(value, 0)
                total_w = len(wins)
                total_l = len(losses)
                if total_w > 0 and total_l > 0:
                    w_ratio = w_count / total_w
                    l_ratio = l_count / total_l
                    if w_ratio > l_ratio * 2 and w_count >= 3:
                        patterns.append({
                            "factor": factor,
                            "value": value,
                            "win_rate": f"{w_count}/{total_w} wins when {factor}={value}",
                            "signal": f"Fort corrélation positive: {value} → win"
                        })
        return patterns
```

### 13.3 State File: ASTRA_PATTERNS.md

```markdown
# ASTRA Pattern Correlation

## Current Database
| Date | Decision | Type | Tithi | Nak | Hora | Vara | MD | AD | Mercury | Outcome |
|------|----------|------|-------|-----|------|------|-----|------|---------|
| Jun 20 | Relance ST Digital | fundraising | Panchami | Shravana | Guru | Saturday | Guru | Shukra | Direct | Win |
| Jun 19 | Negocie Atakpame | negotiation | Chaturthi | Ashlesha | Shani | Friday | Guru | Shukra | Direct | Loss |
| Jun 18 | DoodleMind #1 | content | Tritiya | Rohini | Venus | Thursday | Guru | Shukra | Direct | Win |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Detected Patterns (30 entries analyzed)

### 🔥 Strong Signals
1. **Hora Guru** → 80% win rate (8/10 decisions)
   → Privilégie les decisions importantes pendant Hora Guru
2. **Shukra AD** → 75% win rate pour les ventes
   → Tu es dans une bonne phase pour le commerce
3. **Mercure direct** → 90% win rate pour les contrats
   → Confirme: toujours signer avant Mercure Rx

### ⚠ Weak Signals
4. **Rahu Kaal** → 0% win rate (0/3)
   → Confirme: ne jamais decider pendant Rahu Kaal
5. **Shani Hora** → 20% win rate pour les negociations
   → Shani Hora = analyse solo, pas d'interactions

### 📝 Recommendation
Based on your personal data, schedule ALL important decisions in:
- **Hora Guru** (best) or **Hora Budha** (good for contracts)
- **Shukla Paksha** (waxing moon)
- **Mercure direct** periods
- **Jeudi or Vendredi** days

Avoid: Rahu Kaal, Shani Hora for interactions, Mercure Rx for contracts
```

### 13.4 Integration

- Every TIMELINE entry created by the LLM is automatically tagged via `tag_decision()`
- Every entry updated with an outcome (manual) triggers re-correlation
- After 10 entries with outcomes: pattern report added to ASTRA_PATTERNS.md
- After 30 entries: full correlation with confidence scores
- After 100 entries: predictive model ("Given current conditions, your odds of success on this decision type are X%")

### 13.5 File Updates

- **Modified:** `concepts/TIMELINE.md` — each entry includes astral YAML front-matter
- **New:** `State/ASTRA_PATTERNS.md` — updated every 10 decisions
- **Engine:** `astra_core.tag_decision()`, `astra_core.correlate()`

---

## 14. OS Behavioral Transformation — ASTRA Change le Comportement de FounderHQ

### 14.1 Problem

The spec treats ASTRA as a module that provides information. But the real power is when **FounderHQ's behavior changes based on astral context** — mode, recommendations, strategy, all adapt.

### 14.2 Concept: Adaptive OS Behavior

```python
class AstraBehaviorModulator:
    """FounderHQ mode adapts based on astral context, not just cash."""

    def get_mode_override(self, jd_now, natal, transits):
        """Return recommended mode adjustment."""
        factors = {}

        # Dasha influence
        md_lord = get_current_md_lord(dashas, jd_now)
        md_map = {
            "Guru": "EXPANSION_BIAS",     # Push expansion, tolerate risk
            "Shani": "DEFENSE_BIAS",       # Systematic, conservative
            "Rahu": "SPECULATION_BIAS",    # High risk/reward, innovative
            "Shukra": "RELATIONSHIP_BIAS", # Partnership-focused
            "Ketu": "DETACHMENT_BIAS",     # Cut, simplify, solitude
            "Mangala": "ACTION_BIAS",      # Aggressive execution
            "Chandra": "NURTURE_BIAS",     # Emotional, creative
            "Surya": "AUTHORITY_BIAS",     # Leadership, visibility
            "Budha": "COMMUNICATION_BIAS", # Deals, writing, learning
        }
        factors["dasha_bias"] = md_map.get(md_lord, "NEUTRAL")

        # Sade Sati override
        sade = compute_sade_sati(natal)
        if sade["phase"] != "none":
            factors["sade_sati"] = {
                "rising": "RISK_OFF",      # Phase 1
                "peak": "SURVIVAL_PLUS",   # Phase 2
                "declining": "CAUTIOUS",   # Phase 3
            }.get(sade["phase"])

        # Transit override
        saturn_8th = get_transit_house("Shani", jd_now, natal) == 8
        if saturn_8th:
            factors["saturn_8th"] = "NO_BIG_MOVES"

        jupiter_over_lagna = is_jupiter_aspecting_lagna(jd_now, natal)
        if jupiter_over_lagna:
            factors["jupiter_lagna"] = "FULL_GO"

        return factors

    def get_adaptive_rules(self, factors):
        """Generate concrete behavioral rules for this session."""
        rules = []

        if "RISK_OFF" in factors.values():
            rules.extend([
                "Prioriser la survie et la preparation",
                "Eviter les nouvelles depenses",
                "Focus sur l'optimisation de ce qui existe",
                "Pas d'embauche, pas d'expansion",
            ])

        if "FULL_GO" in factors.values():
            rules.extend([
                "Pousser les decisions majeures maintenant",
                "Contacter investisseurs, clients, partenaires",
                "Lancer les campagnes marketing",
                "Prendre des rendez-vous importants",
            ])

        if "NO_BIG_MOVES" in factors.values():
            rules.extend([
                "Ne pas signer de bail, contrat long-terme",
                "Eviter les restructurations majeures",
                "Focus sur des actions reversibles",
            ])

        return rules
```

### 14.3 How FounderHQ Changes Behavior

| Normal | Avec ASTRA |
|--------|-----------|
| "Tu es en SURVIVAL. Voici les options revenue." | "SURVIVAL + Sade Sati rising. Double defense. Priorite: eliminer les couts, pas generer du revenu." |
| "Tu as 3 produits. Lequel avancer ?" | "Guru MD favorise KORA. Shukra AD favorise les partenariats OMNI. Mets SOJACO en pause." |
| "Voici les prochaines actions." | "Mercure Rx dans 22 jours. Verrouille tout avant. Les 3 prochains jours sont les meilleurs pour signer." |
| "Decision: option A ou B?" | "Option A a meilleure note Muhurta (82/100 vs 45/100). Par ailleurs, la Hora actuelle est Guru. Fais A maintenant." |

### 14.4 State File Influence Map

```
ASTRA_DASHA.md     →  mode_override: EXPANSION_BIAS
ASTRA_SADE_SATI.md  →  sade_sati: RISK_OFF
ASTRA_SHADOW.md     →  red_zones: [15:04-16:38 CRITICAL]
ASTRA_30DAY.md      →  weekly_focus: "signer contrats avant Rx"
ASTRA_ADVANTAGES.md →  play: "content marketing"
ASTRA_NARRATIVE.md  →  chapter: "KORA pre-seed"

All flow into → CURRENT_SESSION_RULES (generated by LLM at boot)
```

### 14.5 Integration

Pas un fichier séparé. L'ASTRA Behavior Modulator est intégré dans :

1. `SYSTEM_PROMPT.md` — les règles de conduite du boot sont dynamiques
2. `State/CURRENT_STATE.md` — le mode opératoire inclut le facteur astral
3. `CURRENT_SESSION.md` — les règles de cette session incluent les contraintes ASTRA

---

## 15. Forecast Engine — Voir Avant

### 15.1 Problem

The daily banner is passive — it appears at boot. But the user needs to be able to **demander une vue** à tout moment, à n'importe quelle échelle : "Quel est mon paysage pour aujourd'hui/cette semaine/ce mois/cette année ?"

### 15.2 Command Interface

```
fhqa forecast              → Aujourd'hui + contexte Dasha (full)
fhqa forecast today        → Panchang + Horas + Emotional + Shadow
fhqa forecast week         → 7 jours: scores, events, windows, red zones
fhqa forecast month        → 30-Day Landscape (section 10)
fhqa forecast year         → Transits majeurs, eclipses, Rx periods, Dasha shifts
fhqa forecast dasha        → Full Dasha timeline (MD/AD/PD)
fhqa forecast product KORA → Product astrology for KORA this period
```

### 15.3 Architecture

```python
def generate_forecast(scope, jd_now, natal, products, n_days=None):
    """Generate a human-readable forecast for the requested scope."""

    if scope == "today":
        # Panchanga + Horas + Emotional + Shadow + Transits + Advantage
        return render_daily_forecast(...)

    elif scope == "week":
        # 7-day table: each day ranked 0-100 with key events
        days = []
        for offset in range(7):
            jd = jd_now + offset
            score = score_day(jd, natal)
            panch = compute_panchanga(jd)
            red = detect_red_zones(jd, natal)
            days.append({
                "date": jd_to_date(jd),
                "score": score,
                "panchanga": panch,
                "red_zones": red,
                "best_hours": get_best_hours(jd, natal, "general"),
            })
        return render_weekly_forecast(days)

    elif scope == "month":
        return render_30day_landscape(jd_now, natal)

    elif scope == "year":
        # Major events: eclipses, Rx periods, sign changes, Dasha shifts
        events = []
        for month_offset in range(12):
            jd = jd_now + month_offset * 30.5
            events.extend(detect_yearly_events(jd, month_offset))
        return render_yearly_forecast(events)

    elif scope == "dasha":
        return render_dasha_timeline(dashas, jd_now)
```

### 15.4 Output Format (Example: Weekly Forecast)

```markdown
# ASTRA Forecast — Semaine du 23 au 29 Juin 2026

## Overview
| Jour | Score | Evenement cle | Red Zone |
|------|-------|---------------|----------|
| Mar 23 | 🟢 85 | Hora Guru 11:57 | Rahu 15:04 |
| Mer 24 | 🟢 78 | Lune Swati | - |
| Jeu 25 | 🟡 62 | Jupiter/Shani aspect | - |
| Ven 26 | 🔴 45 | Chaturthi Rikta | Toute la journee |
| Sam 27 | 🟡 55 | Samedi/Saturne | Gulika matin |
| Dim 28 | 🟢 80 | Dimanche/Soleil | - |
| Lun 29 | 🟢 75 | Lune Pushya | - |

## Top 3 Priorites
1. **Verrouiller contrats** avant le 14 juillet (Mercure Rx)
2. **Meilleurs jours pour negociations**: Mar 23 (Hora Guru) + Jeu 25 matin
3. **Eviter**: Ven 26 (Rikta) pour decisions importantes

## Chapitre Dasha
Toujours en Guru MD + Shukra AD. Cette semaine:
- Guru Hora = Jeudi 25 (11:57-12:59) — signatures
- Shukra Hora = Vendredi 26 (07:42-08:54) — ventes
```

### 15.5 Integration

- Forecast est une commande, pas un fichier — généré à la demande
- Peut être schedulé (ex: `fhqa forecast today` envoyé automatiquement à 06:00)
- Peut être exporté (markdown simple, lisible dans le terminal)

---

## 16. Mode Switching — fhq vs fhqa

### 16.1 Problem

The user wants full FounderHQ with all its capabilities, but sometimes WITHOUT the astral layer. Two distinct experiences:
- `fhq` = FounderHQ classique (SURVIVAL, produits, décisions, mais sans ASTRA)
- `fhqa` = FounderHQ + ASTRA comme système nerveux central

### 16.2 How It Works

```python
FHQ_MODES = {
    "fhq": {
        "name": "FounderHQ",
        "astra": False,
        "persona": "standard_founderos",
        "banner": "standard (current_state + priorities)",
        "llm_role": "You are FounderOS — a personal operating system for a solo entrepreneur.",
        "astra_files_loaded": False,
        "astra_speaks": False,
        "forecast_command": False,
    },
    "fhqa": {
        "name": "FounderHQ + ASTRA",
        "astra": True,
        "persona": "astra_founderos",
        "banner": "astra (narrative + daily + shadow + forecast banner)",
        "llm_role": "You are ASTRA — FounderHQ's astrologer-in-residence. You see everything through the sidereal Vedic Jyotish lens. You speak proactively when timing matters.",
        "astra_files_loaded": True,
        "astra_speaks": True,
        "interjection_rules": True,
        "forecast_command": True,
    },
}
```

### 16.3 State File: ASTRA_MODE.md

```markdown
# ASTRA Mode

## Current Mode: fhqa

## Session Config
- ASTRA active: True
- Proactive interjections: True
- Forecast command: True
- Last forecast: 2026-06-23 06:00

## Switch History
| Date | From | To | Reason |
|------|------|-----|--------|
| 2026-06-23 | fhq | fhqa | Full activation |
```

### 16.4 Boot Differences

| Aspect | fhq | fhqa |
|--------|-----|------|
| Banner | CURRENT_STATE + priorities | CURRENT_STATE + ASTRA banner + Shadow + Forecast |
| Persona | FounderOS (agent exécutif) | ASTRA (astrologue intégré) |
| Proactivity | Répond aux commandes | Parle avant qu'on lui demande |
| Files loaded | State standard | State standard + tous les ASTRA_*.md |
| Decision Engine | PROACT standard | PROACT + Muhurta score |
| TIMELINE entry | Standard | Tagged with astral context |
| Alerts | Deadlines, SOS | Deadlines + SOS + Transit + Rx + Eclipse |
| Forecast | Pas disponible | fhqa forecast [scope] |

### 16.5 Switching at Runtime

```
User: "fhq"    
System: Mode desactive ASTRA. Passage en FounderOS classique.

User: "fhqa"
System: Mode active ASTRA. Chargement des fichiers astraux.
[ASTRA] Bienvenue. Aujourd'hui, Mardi (Mars), Dashami Shukla...
```

### 16.6 Background Processing

Même en mode `fhq`, les scripts ASTRA tournent en arrière-plan :
- `astra_daily.py` continue de s'exécuter (timekeeper)
- `astra_alert.py` continue de surveiller les transits
- Les fichiers ASTRA_*.md sont toujours mis à jour

Quand l'utilisateur passe en `fhqa`, les données sont déjà chaudes — pas d'attente.

### 16.7 File Updates

- **New:** `State/ASTRA_MODE.md` — persisted mode state
- **Modified:** `SYSTEM_PROMPT.md` — dual persona (fhq vs fhqa)
- **Modified:** `openmode.json` or keyword routing — intercept `fhq` vs `fhqa`

---

## 17. Non-Goals (Antipatterns)

- ❌ Displaying charts to the user (raw data = noise)
- ❌ Requiring ephemeris downloads (built-in Moshier is sufficient)
- ❌ Network access for astrology computations (100% offline)
- ❌ Tropical/Western astrology in any form (sidereal Vedic only)
- ❌ Pop/cookie-cutter interpretations (every guidance is personalized)
- ❌ Fatalistic language ("you will", "you are doomed")
- ❌ Overwhelming the user with data (max 10 lines in boot banner)
- ❌ Replacing human judgment (ASTRA = input, not instruction)
- ❌ Passive dashboard (ASTRA must be proactive, not reactive)

---

## 18. Ethical Design

1. **Guidance, not fate** — Every prediction: "Planetary conditions suggest X, but you decide"
2. **Explainability** — Every alert includes traceable reasoning chain ("I suggest this because...")
3. **Opt-in depth** — Start with basic daily banner; let user enable deeper features progressively
4. **Cultural respect** — Source from BPHS/classical texts, cite origins, never dilute
5. **Vulnerability-aware** — Filter charged terms; reframe as "consider pausing" not "don't"
6. **Resilience** — If calculations fail, ASTRA falls back to LLM-only mode graciously
7. **No lock-in** — Birth data can be deleted, all state files are plain markdown
8. **The astrologer never demands** — ASTRA suggests, the user decides. Always.
