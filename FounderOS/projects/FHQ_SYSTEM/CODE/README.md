# FHQ_SYSTEM — Code

## GitHub Repository

The FHQ SYSTEM code lives directly in `FounderOS/Runtime/engine/` as Python scripts. These are not submodules — they are the system itself.

## Submodule Status
- **Status:** ✅ monolithic (code is part of the main founderos repo)

## Engine Scripts

| Script | Purpose |
|--------|---------|
| cycle.py | Boot/fhq/fhqa cycle runner |
| sync.py | Gist-based pull/push sync |
| installer.py | First-run installation |
| watchtower.py | Scheduled veille automation |
| timekeeper.py | Scheduled temporal awareness |
| astra_birth.py | Birth chart calculation |
| astra_daily.py | Daily muhurta calculation |
| astra_reading.py | Narrative reading generation |
| astra_forecast.py | Forecast generation |
