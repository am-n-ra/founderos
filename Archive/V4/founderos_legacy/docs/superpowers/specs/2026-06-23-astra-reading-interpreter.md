# ASTRA Narrative Reading — Design Spec

## Goal
Generate a complete narrative interpretation of the user's birth chart — who they are, what they've been through, where they are now, and what's coming — using deterministic rules + LLM personalization.

## Architecture (Option 3 — Hybrid)

```
astra_reading.py  ──→  ASTRA_READING_RAW.md  ──→  LLM reads raw + PROFILE.md + TIMELINE.md
     (rules engine)        (facts + meanings)          └── writes ASTRA_READING.md
                                                              (final narrative)
```

### Layer 1: astra_reading.py (deterministic)
- Reads ASTRA_BIRTH.md
- Maps each chart element to human meanings via lookup dictionaries
- Sections:
  1. **Lagna Profile** — sign personality, nakshatra themes, lord influence
  2. **House-by-House** — what each house means, which grahas occupy, active houses
  3. **Graha Positions** — planet in sign + house + nakshatra → combined meaning
  4. **Yogas** — interpretations of detected yogas
  5. **Dasha Arc** — past dashas (what happened), current (where you are), future (direction)
  6. **Sade Sati** — phase meaning, what to expect
  7. **Current Sky** — today's transits relative to natal chart
  8. **Summary** — top 5 strengths, top 3 challenges, best timing for actions
- Outputs to `State/ASTRA_READING_RAW.md`

### Layer 2: LLM (per-session)
- On FHQ_ASTRA boot, loads ASTRA_READING_RAW.md + PROFILE.md + TIMELINE.md
- Synthesizes final `State/ASTRA_READING.md` with personalized narrative
- Connects chart patterns to user's actual business/life context

## Files
- Create: `Runtime/engine/astra_reading.py`
- Create: `State/ASTRA_READING_RAW.md` (generated)
- Create (LLM): `State/ASTRA_READING.md` (final narrative)
