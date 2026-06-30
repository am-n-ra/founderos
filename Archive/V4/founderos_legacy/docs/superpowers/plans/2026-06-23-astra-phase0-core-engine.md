# ASTRA Phase 0+1 — Core Engine, Daily Refresh & Birth Profile

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) for syntax tracking.

**Goal:** Build the foundational ASTRA engine that computes Panchanga, Horas, Rahu Kaal, Emotional Forecast, and Birth Profile (D1 chart + Vimshottari Dasha) — producing state files that the LLM reads for proactive guidance.

**Architecture:** `astra_core.py` contains all stateless calculation functions. `astra_daily.py` is the timekeeper-triggered daily script. `astra_birth.py` is the one-time GENESIS script. All output to Markdown state files.

**Tech Stack:** Python 3.13, pysweph (Moshier ephemeris, offline), Windows Task Scheduler (timekeeper hook)

**Spec reference:** `docs/superpowers/specs/2026-06-23-astra-v4-jyotish-engine-design.md` — Sections 0, 1, 2, 7, 8, 12, 15, 16

---

### Task 1: Write astra_core.py — All Computation Functions

**Files:**
- Create: `Runtime/engine/astra_core.py`

This is the largest file — all stateless calculation functions for Panchanga, Horas, Rahu Kaal, Emotional Forecast, Dasha, Birth Chart (D1), and utility functions.

- [ ] **Step 1: Write the complete astra_core.py module**

```python
"""astra_core.py — Core ASTRA computation engine.

All functions are stateless. No file I/O. Pure calculations from ephemeris.
Designed to be imported by astra_daily.py, astra_birth.py, and the LLM prompt.

Usage:
    from Runtime.engine.astra_core import AstraEngine
    engine = AstraEngine(lat=6.133, lon=1.217)
    panchanga = engine.compute_panchanga(jd_now)
"""

import swisseph as swe
from datetime import datetime, timedelta, timezone
from typing import Optional

# ── Constants ──────────────────────────────────────────────────────────

SW_FLAGS = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

GRAHA_IDS = {
    "Surya": swe.SUN, "Chandra": swe.MOON, "Mangala": swe.MARS,
    "Budha": swe.MERCURY, "Guru": swe.JUPITER, "Shukra": swe.VENUS,
    "Shani": swe.SATURN, "Rahu": swe.MEAN_NODE,
}

RASHI = ["Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya",
         "Tula", "Vrishchika", "Dhanu", "Makara", "Kumbha", "Mina"]

RASHI_FR = ["Belier", "Taureau", "Gemeaux", "Cancer", "Lion", "Vierge",
            "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons"]

NAKSHATRA = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati",
]

NAK_LORDS = ["Ketu", "Shukra", "Surya", "Chandra", "Mangala",
             "Rahu", "Guru", "Shani", "Budha"] * 3

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashti", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashti", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya",
]

WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
WEEKDAYS_FR = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
WEEKDAY_GRAHA = ["Surya", "Chandra", "Mangala", "Budha", "Guru", "Shukra", "Shani"]

HORA_GUIDE = {
    "Surya": "Leadership, decisions importantes, visibilite",
    "Chandra": "Emotions, relations, intuition, creativite",
    "Mangala": "Action, competition, travail physique",
    "Budha": "Communication, ecriture, deals, negociation",
    "Guru": "Signatures, expansion, apprentissage, richesse",
    "Shukra": "Ventes, relations, beaute, plaisir",
    "Shani": "Travail solo, discipline, analyse, restructuration",
}

NAK_EMOTION = {
    "Ashwini": ("Impulsif, energetique", "Canalise dans l'action rapide"),
    "Bharani": ("Intense, transformatif", "Bon pour creuser, pas pour vendre"),
    "Krittika": ("Precis, coupant", "Bon pour decisions difficiles"),
    "Rohini": ("Chaud, creatif, nourrissant", "Bon pour creation de contenu, design"),
    "Mrigashira": ("Curieux, doux", "Bon pour recherche, pas pour conclusion"),
    "Ardra": ("Tempetueux, disruptif", "Eviter decisions, bon pour brainstorm"),
    "Punarvasu": ("Renouveau, retour", "Bon pour reconnecter"),
    "Pushya": ("Nourrissant, calme", "Tres favorable, bon pour tout construire"),
    "Ashlesha": ("Enlace, intuitif", "Bon pour negocier, attention manipulation"),
    "Magha": ("Autoritaire, ancestral", "Bon pour leadership, pas pour humilite"),
    "Purva Phalguni": ("Joueur, creatif", "Bon pour creation, ventes"),
    "Uttara Phalguni": ("Stable, genereux", "Bon pour partenariats"),
    "Hasta": ("Habile, precis", "Bon pour travail manuel, artisanat"),
    "Chitra": ("Designer, beau", "Bon pour design, architecture, opportunites"),
    "Swati": ("Independant, equilibre", "Bon pour commerce, autonomie"),
    "Vishakha": ("Focalise, rayonnant", "Bon pour execution"),
    "Anuradha": ("Devoue, successful", "Bon pour equipe, projets communs"),
    "Jyeshtha": ("Puissant, cache", "Bon pour protection, attention ego"),
    "Mula": ("Racine, destruction", "Bon pour arracher, purifier"),
    "Purva Ashadha": ("Victorieux", "Bon pour lancer, conquerir"),
    "Uttara Ashadha": ("Perseverant, stable", "Bon pour tenir, finir"),
    "Shravana": ("Ecoute, apprentissage", "Bon pour apprentissage, enseignement"),
    "Dhanishta": ("Riche, musical", "Bon pour finance, art"),
    "Shatabhisha": ("Guerisseur, solitaire", "Bon pour solitude, recherche"),
    "Purva Bhadrapada": ("Fougueux, transformatif", "Bon pour transformation"),
    "Uttara Bhadrapada": ("Profond, fermeture", "Bon pour fin de cycle, guerison"),
    "Revati": ("Voyageur, protection", "Bon pour voyage, fin de projet"),
}

EVENT_MUHURTA = {
    "signature": {
        "best_tithi": [2, 3, 5, 7, 10, 11, 13],
        "best_vara": [4, 5],
        "best_hora": ["Guru", "Shukra", "Budha"],
        "avoid_rikta": True, "avoid_mercury_rx": True, "avoid_rahu": True,
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
}


class AstraEngine:
    """Core ASTRA computation engine. All methods are stateless."""

    def __init__(self, lat: float = 6.133, lon: float = 1.217):
        self.lat = lat
        self.lon = lon
        swe.set_sid_mode(swe.SIDM_LAHIRI)

    # ── Utilities ──────────────────────────────────────────────────────

    def jd_now(self) -> float:
        now = datetime.now(timezone.utc)
        jd_ut, _ = swe.utc_to_jd(now.year, now.month, now.day,
                                  now.hour, now.minute, now.second)
        return jd_ut

    def jd_from_utc(self, year: int, month: int, day: int,
                    hour: int = 12, minute: int = 0, second: int = 0) -> float:
        jd_ut, _ = swe.utc_to_jd(year, month, day, hour, minute, second)
        return jd_ut

    def jd_to_local_time(self, jd: float) -> str:
        dt = datetime(2000, 1, 1, 12) + timedelta(days=jd - 2451545)
        return dt.strftime("%H:%M")

    def jd_to_date(self, jd: float) -> str:
        dt = datetime(2000, 1, 1, 12) + timedelta(days=jd - 2451545)
        return dt.strftime("%Y-%m-%d")

    def rashi_name(self, lon: float, lang: str = "fr") -> str:
        r = RASHI_FR if lang == "fr" else RASHI
        return r[int(lon / 30) % 12]

    def rashi_deg(self, lon: float) -> tuple:
        return int(lon / 30) % 12, lon % 30

    # ── Planet Positions ──────────────────────────────────────────────

    def planet_sidereal(self, jd: float, planet_id: int) -> dict:
        xx, _, _ = swe.calc_ut(jd, planet_id, SW_FLAGS)
        lon = xx[0] % 360
        sig_i, deg = self.rashi_deg(lon)
        nak_i = int(lon / (360 / 27))
        pada = int((lon % (360 / 27)) / (360 / 27 / 4)) + 1
        return {
            "lon": lon, "lat": xx[1], "dist": xx[2], "speed": xx[3],
            "retrograde": xx[3] < 0,
            "rashi": RASHI_FR[sig_i], "rashi_deg": round(deg, 1),
            "nakshatra": NAKSHATRA[nak_i],
            "nakshatra_pada": pada,
            "nakshatra_lord": NAK_LORDS[nak_i],
        }

    def all_grahas(self, jd: float) -> dict:
        pos = {}
        for name, pid in GRAHA_IDS.items():
            pos[name] = self.planet_sidereal(jd, pid)
        # Ketu = Rahu + 180
        rahu = pos["Rahu"]
        k_lon = (rahu["lon"] + 180) % 360
        sig_i, deg = self.rashi_deg(k_lon)
        nak_i = int(k_lon / (360 / 27))
        pada = int((k_lon % (360 / 27)) / (360 / 27 / 4)) + 1
        pos["Ketu"] = {
            "lon": k_lon, "lat": 0, "dist": rahu["dist"], "speed": rahu["speed"],
            "retrograde": rahu["retrograde"],
            "rashi": RASHI_FR[sig_i], "rashi_deg": round(deg, 1),
            "nakshatra": NAKSHATRA[nak_i],
            "nakshatra_pada": pada,
            "nakshatra_lord": NAK_LORDS[nak_i],
        }
        return pos

    # ── Sunrise / Sunset ──────────────────────────────────────────────

    def sunrise_sunset(self, jd: float) -> dict:
        geo = (self.lon, self.lat, 0)
        jd_midnight = int(jd) + 0.5
        rise_jd = swe.rise_trans(jd_midnight, swe.SUN,
                                 rsmi=swe.CALC_RISE, geopos=geo)[1][0]
        set_jd = swe.rise_trans(jd_midnight, swe.SUN,
                                rsmi=swe.CALC_SET, geopos=geo)[1][0]
        return {
            "sunrise_jd": rise_jd,
            "sunset_jd": set_jd,
            "sunrise": self.jd_to_local_time(rise_jd),
            "sunset": self.jd_to_local_time(set_jd),
        }

    # ── Panchanga ──────────────────────────────────────────────────────

    def compute_panchanga(self, jd: float) -> dict:
        grahas = self.all_grahas(jd)
        sun_lon = grahas["Surya"]["lon"]
        moon_lon = grahas["Chandra"]["lon"]

        theta = (moon_lon - sun_lon) % 360
        tithi_i = int(theta / 12)
        paksha = "Shukla (croissant)" if tithi_i < 15 else "Krishna (decroissant)"
        rikta = (tithi_i % 15) in [3, 8, 13]

        nak_i = int(moon_lon / (360 / 27))
        pada = int((moon_lon % (360 / 27)) / (360 / 27 / 4)) + 1

        yoga_val = (sun_lon + moon_lon) % 360
        yoga_i = int(yoga_val / (360 / 27))
        YOGA_NAMES = [
            "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana",
            "Atiganda", "Sukarman", "Dhriti", "Shula", "Ganda",
            "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
            "Siddhi", "Vyatipata", "Variyan", "Parigha", "Shiva",
            "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
            "Indra", "Vaidhriti",
        ]
        yoga_name = YOGA_NAMES[yoga_i]
        yoga_favorable = yoga_i in [0, 1, 6, 7, 10, 11, 13, 14, 15, 16,
                                    19, 20, 21, 22, 23, 24, 25, 26]

        vara_i = int((jd + 1.5) % 7)
        return {
            "tithi": {"index": tithi_i + 1, "name": TITHI_NAMES[tithi_i],
                      "paksha": paksha, "rikta": rikta},
            "nakshatra": {"index": nak_i + 1, "name": NAKSHATRA[nak_i],
                          "lord": NAK_LORDS[nak_i], "pada": pada},
            "yoga": {"name": yoga_name, "favorable": yoga_favorable},
            "vara": {"index": vara_i, "name": WEEKDAYS_FR[vara_i],
                     "graha": WEEKDAY_GRAHA[vara_i]},
            "sun_lon": sun_lon, "moon_lon": moon_lon,
            "grahas": grahas,
        }

    # ── Rahu Kaal ──────────────────────────────────────────────────────

    def rahu_kaal(self, jd: float) -> Optional[dict]:
        sun = self.sunrise_sunset(jd)
        if not sun or not sun.get("sunrise_jd"):
            return None
        vara_i = int((jd + 1.5) % 7)
        day_dur = sun["sunset_jd"] - sun["sunrise_jd"]
        seg = day_dur / 8
        RAHU_OFF = [7, 1, 6, 4, 5, 3, 2]
        off = RAHU_OFF[vara_i]
        start = sun["sunrise_jd"] + seg * off
        end = start + seg
        return {
            "start_jd": start, "end_jd": end,
            "start": self.jd_to_local_time(start),
            "end": self.jd_to_local_time(end),
            "active": start <= jd <= end,
        }

    # ── Horas ──────────────────────────────────────────────────────────

    def compute_horas(self, jd: float) -> dict:
        sun = self.sunrise_sunset(jd)
        next_day = (datetime(2000, 1, 1, 12) +
                    timedelta(days=jd - 2451545 + 1))
        jd_next = (next_day - datetime(2000, 1, 1, 12)).total_seconds() / 86400 + 2451545
        try:
            next_rise = swe.rise_trans(jd_next, swe.SUN,
                                       rsmi=swe.CALC_RISE,
                                       geopos=(self.lon, self.lat, 0))[1][0]
        except Exception:
            next_rise = sun["sunrise_jd"] + 1.0

        day_dur = sun["sunset_jd"] - sun["sunrise_jd"]
        night_dur = next_rise - sun["sunset_jd"]
        day_h = day_dur / 12
        night_h = night_dur / 12

        weekday = int((jd + 1.5) % 7)
        first_lord = WEEKDAY_GRAHA[weekday]
        PLANET_SEQ = ["Shani", "Guru", "Mangala", "Surya",
                      "Shukra", "Budha", "Chandra"]
        lord_i = PLANET_SEQ.index(first_lord)

        horas = []
        for i in range(12):
            idx = (lord_i + i) % 7
            hs = sun["sunrise_jd"] + i * day_h
            he = hs + day_h
            horas.append({
                "type": "day", "lord": PLANET_SEQ[idx],
                "start_jd": hs, "end_jd": he,
                "start": self.jd_to_local_time(hs),
                "end": self.jd_to_local_time(he),
                "guide": HORA_GUIDE.get(PLANET_SEQ[idx], ""),
                "active": hs <= jd <= he,
            })
        for i in range(12):
            idx = (lord_i + 12 + i) % 7
            hs = sun["sunset_jd"] + i * night_h
            he = hs + night_h
            horas.append({
                "type": "night", "lord": PLANET_SEQ[idx],
                "start_jd": hs, "end_jd": he,
                "start": self.jd_to_local_time(hs),
                "end": self.jd_to_local_time(he),
                "guide": HORA_GUIDE.get(PLANET_SEQ[idx], ""),
                "active": hs <= jd <= he,
            })

        active = [h for h in horas if h["active"]]
        return {"horas": horas, "active": active[0] if active else None}

    # ── Emotional Forecast ─────────────────────────────────────────────

    def emotional_forecast(self, jd: float) -> dict:
        panch = self.compute_panchanga(jd)
        nak_name = panch["nakshatra"]["name"]
        emotion = NAK_EMOTION.get(nak_name, ("Neutre", "Journee normale"))

        # Energy score 0-100 based on factors
        energy = 70
        if panch["tithi"]["rikta"]:
            energy -= 15
        if panch["yoga"]["favorable"]:
            energy += 10
        if panch["vara"]["index"] in [4, 5]:  # Thu/Fri
            energy += 5
        energy = max(0, min(100, energy))

        # Focus score
        focus = 65
        if panch["nakshatra"]["name"] in ["Mrigashira", "Ardra", "Swati"]:
            focus -= 10
        if panch["nakshatra"]["name"] in ["Krittika", "Hasta", "Shravana"]:
            focus += 10
        focus = max(0, min(100, focus))

        # Mood score
        mood = 70
        if panch["tithi"]["paksha"].startswith("Shukla"):
            mood += 10
        else:
            mood -= 5
        mood = max(0, min(100, mood))

        # Sociability
        sociability = 60
        if panch["vara"]["index"] in [4, 5, 0]:  # Thu/Fri/Sun
            sociability += 10
        if panch["vara"]["index"] == 6:  # Sat
            sociability -= 10
        sociability = max(0, min(100, sociability))

        return {
            "energy": energy,
            "focus": focus,
            "mood": mood,
            "sociability": sociability,
            "mood_label": emotion[0],
            "mood_advice": emotion[1],
        }

    # ── Muhurta Score ──────────────────────────────────────────────────

    def score_muhurta(self, jd: float, event_type: str = "signature") -> int:
        panch = self.compute_panchanga(jd)
        horas = self.compute_horas(jd)
        tpl = EVENT_MUHURTA.get(event_type, EVENT_MUHURTA["signature"])
        score = 60

        if panch["tithi"]["index"] in tpl.get("best_tithi", []):
            score += 10
        else:
            score -= 5

        if panch["vara"]["index"] in tpl.get("best_vara", []):
            score += 5

        if horas["active"] and horas["active"]["lord"] in tpl.get("best_hora", []):
            score += 10
        elif horas["active"]:
            score -= 3

        if tpl.get("avoid_rikta") and panch["tithi"]["rikta"]:
            score -= 15

        rx = self.is_retrograde(jd, "Budha")
        if tpl.get("avoid_mercury_rx") and rx:
            score -= 20

        rahu = self.rahu_kaal(jd)
        if tpl.get("avoid_rahu") and rahu and rahu["active"]:
            score -= 20

        return max(0, min(100, score))

    # ── Retrograde Check ──────────────────────────────────────────────

    def is_retrograde(self, jd: float, graha_name: str) -> bool:
        pid = GRAHA_IDS.get(graha_name)
        if pid is None:
            return False
        xx, _, _ = swe.calc_ut(jd, pid, SW_FLAGS)
        return xx[3] < 0

    # ── Birth Chart (D1) ──────────────────────────────────────────────

    def compute_birth_chart(self, year: int, month: int, day: int,
                            hour: int = 12, minute: int = 0,
                            place: str = "Lome") -> dict:
        jd = self.jd_from_utc(year, month, day, hour, minute)
        grahas = self.all_grahas(jd)
        sun = self.sunrise_sunset(jd)

        # Lagna (Ascendant)
        cusps, ascmc = swe.houses_ex(jd, self.lat, self.lon, b'W', SW_FLAGS)
        asc_lon = ascmc[0]
        asc_sig_i, asc_deg = self.rashi_deg(asc_lon)
        asc_nak_i = int(asc_lon / (360 / 27))
        asc_pada = int((asc_lon % (360 / 27)) / (360 / 27 / 4)) + 1

        # House placement for each graha
        for name, g in grahas.items():
            g["house"] = ((int(g["lon"] / 30) - int(asc_lon / 30)) % 12) + 1

        # House lords
        house_lords = {}
        for i in range(1, 13):
            sign = (int(asc_lon / 30) + i - 1) % 12
            lord_map = {
                0: "Mangala", 1: "Shukra", 2: "Budha", 3: "Chandra",
                4: "Surya", 5: "Budha", 6: "Shukra", 7: "Mangala",
                8: "Guru", 9: "Shani", 10: "Shani", 11: "Guru",
            }
            house_lords[f"H{i}"] = lord_map[sign]

        return {
            "jd": jd,
            "place": place,
            "lagna": {
                "lon": asc_lon, "rashi": RASHI_FR[asc_sig_i],
                "deg": round(asc_deg, 1), "nakshatra": NAKSHATRA[asc_nak_i],
                "nakshatra_pada": asc_pada, "nakshatra_lord": NAK_LORDS[asc_nak_i],
            },
            "grahas": grahas,
            "house_lords": house_lords,
            "sunrise": sun["sunrise"],
            "sunset": sun["sunset"],
        }

    # ── Vimshottari Dasha ─────────────────────────────────────────────

    DASHA_PERIODS = {
        "Ketu": 7, "Shukra": 20, "Surya": 6, "Chandra": 10,
        "Mangala": 7, "Rahu": 18, "Guru": 16, "Shani": 19, "Budha": 17,
    }
    DASHA_LORDS = ["Ketu", "Shukra", "Surya", "Chandra", "Mangala",
                   "Rahu", "Guru", "Shani", "Budha"]

    def compute_vimshottari(self, birth_jd: float) -> dict:
        moon_lon = self.all_grahas(birth_jd)["Chandra"]["lon"]
        nak_i = int(moon_lon / (360 / 27))
        deg_in_nak = moon_lon % (360 / 27)
        start_lord = NAK_LORDS[nak_i]
        lord_i = self.DASHA_LORDS.index(start_lord)
        remaining = 1.0 - (deg_in_nak / (360 / 27))
        balance_yrs = self.DASHA_PERIODS[start_lord] * remaining

        dashas = []
        current_jd = birth_jd - balance_yrs * 365.25
        for i in range(9):
            idx = (lord_i + i) % 9
            lord = self.DASHA_LORDS[idx]
            full = self.DASHA_PERIODS[lord]
            yrs = balance_yrs if i == 0 else full
            days = yrs * 365.25
            d = {
                "lord": lord, "level": 1,
                "start_jd": current_jd, "end_jd": current_jd + days,
                "years": round(yrs, 4),
                "start": self.jd_to_date(current_jd),
                "end": self.jd_to_date(current_jd + days),
            }
            # Compute Antar Dasha (sub-periods)
            subs = []
            for j in range(9):
                s_idx = (self.DASHA_LORDS.index(lord) + j) % 9
                s_lord = self.DASHA_LORDS[s_idx]
                s_yrs = yrs * self.DASHA_PERIODS[s_lord] / 120.0
                s_days = s_yrs * 365.25
                subs.append({
                    "lord": s_lord, "level": 2,
                    "years": round(s_yrs, 4),
                })
            d["antars"] = subs
            dashas.append(d)
            current_jd += days

        # Find current
        now_jd = self.jd_now()
        current_md = None
        current_ad = None
        for md in dashas:
            if md["start_jd"] <= now_jd < md["end_jd"]:
                current_md = md
                # Find current AD
                ad_start_jd = md["start_jd"]
                for ad in md["antars"]:
                    ad_days = ad["years"] * 365.25
                    ad_end = ad_start_jd + ad_days
                    if ad_start_jd <= now_jd < ad_end:
                        current_ad = ad
                        current_ad["start"] = self.jd_to_date(ad_start_jd)
                        current_ad["end"] = self.jd_to_date(ad_end)
                        break
                    ad_start_jd = ad_end
                break

        return {
            "dashas": dashas,
            "current_md": current_md,
            "current_ad": current_ad,
            "next_change": dashas[1]["start"] if len(dashas) > 1 else None,
        }

    # ── Sade Sati ─────────────────────────────────────────────────────

    def compute_sade_sati(self, birth_chart: dict) -> dict:
        moon_sign = int(birth_chart["grahas"]["Chandra"]["lon"] / 30)
        now_jd = self.jd_now()
        saturn = self.planet_sidereal(now_jd, swe.SATURN)
        sat_sign = int(saturn["lon"] / 30)

        # Sade Sati moons: in 12th, 1st, or 2nd house from natal Moon
        # In whole sign: moon_sign + 11, + 0, + 1
        dist = (sat_sign - moon_sign) % 12

        result = {"active": False, "phase": "none", "guidance": ""}
        if dist == 11:
            result = {"active": True, "phase": "rising (Saturne en 12e de la Lune)",
                      "guidance": "Phase de retrait. Eliminer l'ancien. Eviter les nouvelles expansions."}
        elif dist == 0:
            result = {"active": True, "phase": "peak (Saturne sur la Lune)",
                      "guidance": "Phase intense. Karma, transformations, lecons difficiles."}
        elif dist == 1:
            result = {"active": True, "phase": "declining (Saturne en 2e de la Lune)",
                      "guidance": "Reconstruction. Les fruits du travail precedent commencent a se montrer."}

        return result

    # ── Red Zones (Shadow Mode) ────────────────────────────────────────

    def detect_red_zones(self, jd: float) -> list:
        reds = []
        rahu = self.rahu_kaal(jd)
        if rahu and rahu["active"]:
            reds.append({
                "severity": "CRITICAL",
                "window": f"{rahu['start']}-{rahu['end']}",
                "rule": "Ne RIEN commencer d'important",
                "reason": "Rahu Kaal actif maintenant",
                "now": True,
            })
        elif rahu:
            reds.append({
                "severity": "WARN",
                "window": f"{rahu['start']}-{rahu['end']}",
                "rule": "Eviter decisions importantes pendant cette fenetre",
                "reason": "Rahu Kaal a venir",
                "now": False,
            })

        rx = self.is_retrograde(jd, "Budha")
        if rx:
            reds.append({
                "severity": "HIGH",
                "window": "periode retrograde",
                "rule": "Pas de nouveaux contrats, lancements, achats majeurs",
                "reason": "Mercure retrograde",
                "now": True,
            })

        panch = self.compute_panchanga(jd)
        if panch["tithi"]["rikta"]:
            reds.append({
                "severity": "WARN",
                "window": "toute la journee",
                "rule": "Eviter les lancements et grandes decisions",
                "reason": f"Tithi Rikta ({panch['tithi']['name']})",
                "now": True,
            })

        return reds
```

- [ ] **Step 2: Run a basic import test**

Run: `cd FounderOS && .venv\Scripts\python.exe -c "from Runtime.engine.astra_core import AstraEngine; e = AstraEngine(); print('OK')"`

Expected: `OK` (no import errors, pysweph works)

- [ ] **Step 3: Run a functional test**

```python
from Runtime.engine.astra_core import AstraEngine
e = AstraEngine()
jd = e.jd_now()
panch = e.compute_panchanga(jd)
print(f"Tithi: {panch['tithi']['name']}, Nak: {panch['nakshatra']['name']}")
print(f"Vara: {panch['vara']['name']}")
horas = e.compute_horas(jd)
if horas['active']:
    print(f"Hora: {horas['active']['lord']} - {horas['active']['guide']}")
emotion = e.emotional_forecast(jd)
print(f"Mood: energy={emotion['energy']}, focus={emotion['focus']}")
rahu = e.rahu_kaal(jd)
if rahu:
    print(f"Rahu Kaal: {rahu['start']}-{rahu['end']}")
reds = e.detect_red_zones(jd)
for r in reds:
    print(f"Red: {r['severity']} - {r['reason']}")
score = e.score_muhurta(jd, 'signature')
print(f"Muhurta score: {score}")
```

Run: Save as `test_astra_core.py` and run with `.venv\Scripts\python.exe`

Expected: All values printed correctly

- [ ] **Step 4: Test birth chart computation**

```python
from Runtime.engine.astra_core import AstraEngine
e = AstraEngine()
# Test with a known date
chart = e.compute_birth_chart(1996, 12, 15, 14, 30)
print(f"Lagna: {chart['lagna']['rashi']} {chart['lagna']['deg']}deg")
print(f"Nak: {chart['lagna']['nakshatra']} Pada {chart['lagna']['nakshatra_pada']}")
for name, g in chart['grahas'].items():
    print(f"  {name}: {g['rashi']} {g['rashi_deg']}deg House {g['house']}")
```

- [ ] **Step 5: Test Vimshottari Dasha computation**

```python
from Runtime.engine.astra_core import AstraEngine
e = AstraEngine()
birth_jd = e.jd_from_utc(1996, 12, 15, 14, 30)
dasha = e.compute_vimshottari(birth_jd)
if dasha['current_md']:
    print(f"MD: {dasha['current_md']['lord']} ({dasha['current_md']['start']} - {dasha['current_md']['end']})")
if dasha['current_ad']:
    print(f"AD: {dasha['current_ad']['lord']} ({dasha['current_ad'].get('start', '?')})")
```

- [ ] **Step 6: Test Sade Sati**

```python
from Runtime.engine.astra_core import AstraEngine
e = AstraEngine()
chart = e.compute_birth_chart(1996, 12, 15, 14, 30)
sade = e.compute_sade_sati(chart)
print(f"Sade Sati: {sade['phase']} - {sade['guidance']}")
```

- [ ] **Step 7: Commit**

```bash
git add Runtime/engine/astra_core.py
git commit -m "feat(astra): core engine - Panchanga, Horas, Rahu Kaal, Emotional Forecast, Birth Chart, Dasha, Sade Sati, Muhurta"
```

---

### Task 2: Write astra_daily.py — Daily State File Generator

**Files:**
- Create: `Runtime/engine/astra_daily.py`

- [ ] **Step 1: Write astra_daily.py**

```python
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
import sys
from datetime import datetime, timezone
from pathlib import Path
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
- **AD:** {d['current_ad']['lord']} ({d['current_ad']['start']} - {d['current_ad']['end']})" if d.get('current_ad') else ""}
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
- **Hora:** {horas['active']['lord']} ({horas['active']['start']} - {horas['active']['end']})
- **Favorable pour:** {horas['active']['guide']}
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

    md += f"""
## Muhurta Scores
| Type | Score |
|------|-------|
| General | {score}/100 |
| Signature | {engine.score_muhurta(jd, 'signature')}/100 |
| Negotiation | {engine.score_muhurta(jd, 'negotiation')}/100 |
| Deep Work | {engine.score_muhurta(jd, 'deep_work')}/100 |
| Content | {engine.score_muhurta(jd, 'content')}/100 |

## Today's Guidance
"""

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
        md += f"| {r['severity']} | {r['window']} | {r['rule']} | {r['reason']} |\n"

    if sade["active"]:
        md += f"| WARN | ongoing | {sade['guidance']} | Sade Sati {sade['phase']} |\n"

    return md


def main():
    parser = argparse.ArgumentParser(description="ASTRA Daily Generator")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--force", action="store_true", help="Force regenerate")
    args = parser.parse_args()

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
            import re
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
```

- [ ] **Step 2: Run astra_daily.py**

Run: `cd FounderOS && .venv\Scripts\python.exe Runtime/engine/astra_daily.py --base-dir .`

Expected: `State/ASTRA_DAILY.md` and `State/ASTRA_SHADOW.md` created with correct content.

- [ ] **Step 3: Verify output files**

Run: `Get-Content State/ASTRA_DAILY.md -First 20`

Expected: Valid markdown with Panchanga, Hora, Emotional Forecast, Red Zones sections.

- [ ] **Step 4: Commit**

```bash
git add Runtime/engine/astra_daily.py State/ASTRA_DAILY.md State/ASTRA_SHADOW.md
git commit -m "feat(astra): daily state file generator"
```

---

### Task 3: Write astra_birth.py — Birth Profile Generator (GENESIS)

**Files:**
- Create: `Runtime/engine/astra_birth.py`
- Create: `State/ASTRA_BIRTH.md`

- [ ] **Step 1: Write astra_birth.py**

```python
"""astra_birth.py — Compute and store birth chart at GENESIS.

Run once during first-time setup (GENESIS step).
Generates ASTRA_BIRTH.md, seeds Dasha timeline.

Usage:
    python Runtime/engine/astra_birth.py --base-dir . --date 1996-12-15 --time 14:30
"""

import argparse
from datetime import datetime
from pathlib import Path
from Runtime.engine.astra_core import AstraEngine


def generate_birth_md(engine, year, month, day, hour, minute, place="Lome") -> str:
    """Generate ASTRA_BIRTH.md from birth data."""
    chart = engine.compute_birth_chart(year, month, day, hour, minute, place)
    dasha = engine.compute_vimshottari(chart["jd"])
    sade = engine.compute_sade_sati(chart)

    md = f"""# ASTRA Birth Profile

> Generated by astra_birth.py

## Birth Data
- **Birth date:** {year:04d}-{month:02d}-{day:02d}
- **Birth time:** {hour:02d}:{minute:02d} (UTC+0)
- **Location:** {place} ({engine.lat}N, {engine.lon}E)

## Ayanamsa
- **System:** Lahiri (Chitrapaksha)
- **Houses:** Whole Sign (Parashari)

## Lagna (Ascendant)
- **Sign:** {chart['lagna']['rashi']} ({chart['lagna']['deg']}deg)
- **Nakshatra:** {chart['lagna']['nakshatra']} — Pada {chart['lagna']['nakshatra_pada']}
- **Nakshatra Lord:** {chart['lagna']['nakshatra_lord']}

## Graha Positions
| Graha | Rashi | Deg | Nakshatra | Pada | Lord | House | Retro |
|-------|-------|-----|-----------|------|------|-------|-------|
"""
    for name in ["Surya", "Chandra", "Mangala", "Budha", "Guru", "Shukra", "Shani", "Rahu", "Ketu"]:
        g = chart["grahas"].get(name)
        if not g:
            continue
        retro = "R" if g["retrograde"] else ""
        md += f"| {name} | {g['rashi']} | {g['rashi_deg']} | {g['nakshatra']} | {g['nakshatra_pada']} | {g['nakshatra_lord']} | {g.get('house', '?')} | {retro} |\n"

    md += f"""
## House Lords
| House | Lord |
|-------|------|
"""
    for h, lord in list(chart["house_lords"].items())[:12]:
        md += f"| {h} | {lord} |\n"

    if dasha["current_md"]:
        md += f"""
## Current Dasha
- **Mahadasha:** {dasha['current_md']['lord']}
- **Start:** {dasha['current_md']['start']}
- **End:** {dasha['current_md']['end']}
- **Years:** {dasha['current_md']['years']}"""
        if dasha["current_ad"]:
            md += f"""
- **Antar Dasha:** {dasha['current_ad']['lord']}
"""

    if sade["active"]:
        md += f"""
## Sade Sati
- **Status:** {sade['phase']}
- **Guidance:** {sade['guidance']}
"""

    md += f"""
## Full Dasha Timeline
| Lord | Level | Start | End | Years |
|------|-------|-------|-----|-------|
"""
    for d in dasha["dashas"]:
        md += f"| {d['lord']} | MD | {d['start']} | {d['end']} | {d['years']} |\n"

    md += f"""
## Yogas (Auto-Detected)
"""

    # Detect basic Yogas
    grahas = chart["grahas"]
    yogas = []

    # Budha-Aditya Yoga: Sun + Mercury in same sign
    if grahas["Surya"]["rashi"] == grahas["Budha"]["rashi"]:
        yogas.append(("Budha-Aditya Yoga", "Intelligence, communication, eloquence"))

    # Gaja-Kesari Yoga: Jupiter + Moon in Kendra from each other
    moon_sign = int(grahas["Chandra"]["lon"] / 30)
    jup_sign = int(grahas["Guru"]["lon"] / 30)
    dist = (jup_sign - moon_sign) % 12
    if dist == 0 or dist == 4 or dist == 8:
        yogas.append(("Gaja-Kesari Yoga", "Sagesse, autorite, respect"))

    # Chandra-Mangala Yoga: Moon + Mars
    if grahas["Chandra"]["rashi"] == grahas["Mangala"]["rashi"]:
        yogas.append(("Chandra-Mangala Yoga", "Passion, courage, leadership"))

    if yogas:
        for name, desc in yogas:
            md += f"- **{name}:** {desc}\n"
    else:
        md += "- No major Yogas auto-detected in D1\n"

    return md


def main():
    parser = argparse.ArgumentParser(description="ASTRA Birth Profile Generator")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--date", required=True, help="Birth date YYYY-MM-DD")
    parser.add_argument("--time", default="12:00", help="Birth time HH:MM")
    parser.add_argument("--place", default="Lome", help="Birth place")
    args = parser.parse_args()

    date_parts = args.date.split("-")
    time_parts = args.time.split(":")
    year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
    hour, minute = int(time_parts[0]), int(time_parts[1])

    engine = AstraEngine()
    md = generate_birth_md(engine, year, month, day, hour, minute, args.place)

    base = Path(args.base_dir)
    birth_path = base / "State" / "ASTRA_BIRTH.md"
    birth_path.parent.mkdir(parents=True, exist_ok=True)
    birth_path.write_text(md, encoding="utf-8")
    print(f"Birth profile written: {birth_path}")
    print("Done. Run astra_daily.py to generate today's guidance.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run astra_birth.py with test data**

Run: `cd FounderOS && .venv\Scripts\python.exe Runtime/engine/astra_birth.py --base-dir . --date 1996-12-15 --time 14:30`

Expected: `State/ASTRA_BIRTH.md` created with full chart, Dasha timeline, Yogas.

- [ ] **Step 3: Verify birth profile**

Run: `Get-Content State/ASTRA_BIRTH.md -First 30`

Expected: Valid markdown with Lagna, Graha positions table, Dasha timeline, Yogas.

- [ ] **Step 4: Run astra_daily.py with birth context**

Run: `cd FounderOS && .venv\Scripts\python.exe Runtime/engine/astra_daily.py --base-dir .`

Expected: `ASTRA_DAILY.md` now includes Dasha context, Sade Sati status in Chapter Context section.

- [ ] **Step 5: (Optional) Enter real birth data**

Run: `.venv\Scripts\python.exe Runtime/engine/astra_birth.py --base-dir . --date YYYY-MM-DD --time HH:MM`

Replace with real birth data. Verify output.

- [ ] **Step 6: Commit**

```bash
git add Runtime/engine/astra_birth.py State/ASTRA_BIRTH.md
git commit -m "feat(astra): birth profile generator for GENESIS"
```

---

### Task 4: Wire ASTRA into timekeeper (Daily Execution)

**Files:**
- Modify: `Runtime/engine/timekeeper.py` — add ASTRA hooks

- [ ] **Step 1: Read current timekeeper.py**

- [ ] **Step 2: Add --astra flag to timekeeper.py**

Add at the beginning of `main()`:

```python
parser.add_argument("--astra", action="store_true", help="Run ASTRA daily update")
```

Add after the existing checks:

```python
if args.astra:
    try:
        from Runtime.engine.astra_daily import main as astra_daily
        astra_main()
        print("[ASTRA] Daily update complete.")
    except Exception as e:
        print(f"[ASTRA] Error: {e}")
```

- [ ] **Step 3: Install timekeeper with --astra flag**

If installing via Task Scheduler, add `--astra` to the task arguments.

- [ ] **Step 4: Test timekeeper with --astra**

Run: `.venv\Scripts\python.exe Runtime/engine/timekeeper.py --astra --no-toast`

Expected: Both timekeeper checks AND ASTRA daily update run.

- [ ] **Step 5: Commit**

```bash
git add Runtime/engine/timekeeper.py
git commit -m "feat(astra): wire astra_daily into timekeeper with --astra flag"
```

---

### Task 5: Wire ASTRA Mode Switching (fhq vs fhqa)

**Files:**
- Create: `State/ASTRA_MODE.md`
- Modify: `SYSTEM_PROMPT.md` — add dual persona

- [ ] **Step 1: Create ASTRA_MODE.md**

```markdown
# ASTRA Mode

## Current Mode: fhqa

## Session Config
- ASTRA active: True
- Proactive interjections: True
- Forecast command: True
- Load ASTRA files: True

## Switch History
| Date | From | To | Reason |
|------|------|-----|--------|
| 2026-06-23 | - | fhqa | Initial activation |
```

- [ ] **Step 2: Read SYSTEM_PROMPT.md to find keyword routing section**

- [ ] **Step 3: Add fhq/fhqa routing to SYSTEM_PROMPT.md**

Add to the intent classification table:

```
| fhq | FHQ_MODE | Run FounderHQ without ASTRA (standard mode) |
| fhqa | FHQ_ASTRA | Run FounderHQ with ASTRA active (full guidance) |
```

Add a dual persona instruction block:

```
If mode is fhq:
  You are FounderOS — a personal operating system for a solo entrepreneur.
  Respond directly to user requests without astrological context.

If mode is fhqa:
  You ARE ASTRA — FounderHQ's astrologer-in-residence.
  You see everything through the sidereal Vedic Jyotish lens.
  Before every response, check ASTRA_DAILY.md, ASTRA_SHADOW.md, ASTRA_BIRTH.md.
  If current timing is significant, speak proactively.
  Format guidance as [ASTRA] prefix for astral insights.
```

- [ ] **Step 4: Commit**

```bash
git add State/ASTRA_MODE.md SYSTEM_PROMPT.md
git commit -m "feat(astra): mode switching fhq/fhqa with dual persona"
```

---

### Task 6: Forecast Command

**Files:**
- Create: `Runtime/engine/astra_forecast.py`

- [ ] **Step 1: Write astra_forecast.py**

```python
"""astra_forecast.py — On-demand forecast command.

Usage:
    python Runtime/engine/astra_forecast.py --base-dir . today
    python Runtime/engine/astra_forecast.py --base-dir . week
    python Runtime/engine/astra_forecast.py --base-dir . month
    python Runtime/engine/astra_forecast.py --base-dir . year
"""

import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
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


def forecast_week(engine, jd, birth_chart=None):
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
    # Best days
    print("Top recommendations:")
    print("- Verrouiller les contrats avant Mercure Rx")
    print("- Meilleurs jours pour negociations: jeudi, vendredi")
    print("- Eviter les tithis Rikta")


def forecast_month(engine, jd, birth_chart=None):
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
        forecast_week(engine, jd, birth_chart)
    elif args.scope == "month":
        forecast_month(engine, jd, birth_chart)
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
```

- [ ] **Step 2: Test forecast command**

Run: `.venv\Scripts\python.exe Runtime/engine/astra_forecast.py --base-dir . today`
Expected: Full daily forecast in terminal

Run: `.venv\Scripts\python.exe Runtime/engine/astra_forecast.py --base-dir . week`
Expected: 7-day table

Run: `.venv\Scripts\python.exe Runtime/engine/astra_forecast.py --base-dir . month`
Expected: 4-week table

- [ ] **Step 3: Commit**

```bash
git add Runtime/engine/astra_forecast.py
git commit -m "feat(astra): on-demand forecast command (today, week, month, dasha)"
```
