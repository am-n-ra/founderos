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

SW_FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

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

J2000 = 2451545

YOGA_NAMES = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana",
    "Atiganda", "Sukarman", "Dhriti", "Shula", "Ganda",
    "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
    "Siddhi", "Vyatipata", "Variyan", "Parigha", "Shiva",
    "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
    "Indra", "Vaidhriti",
]

YOGA_FAVORABLE = {i for i in [0, 1, 6, 7, 10, 11, 13, 14, 15, 16,
                               19, 20, 21, 22, 23, 24, 25, 26]}

HOUSE_LORD_MAP = {
    0: "Mangala", 1: "Shukra", 2: "Budha", 3: "Chandra",
    4: "Surya", 5: "Budha", 6: "Shukra", 7: "Mangala",
    8: "Guru", 9: "Shani", 10: "Shani", 11: "Guru",
}

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
        dt = datetime(2000, 1, 1, 12) + timedelta(days=jd - J2000)
        return dt.strftime("%H:%M")

    def jd_to_date(self, jd: float) -> str:
        dt = datetime(2000, 1, 1, 12) + timedelta(days=jd - J2000)
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
        yoga_name = YOGA_NAMES[yoga_i]
        yoga_favorable = yoga_i in YOGA_FAVORABLE

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
                    timedelta(days=jd - J2000 + 1))
        jd_next = (next_day - datetime(2000, 1, 1, 12)).total_seconds() / 86400 + J2000
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
            house_lords[f"H{i}"] = HOUSE_LORD_MAP[sign]

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
