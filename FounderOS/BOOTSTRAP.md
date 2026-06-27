# FounderHQ V4 — Bootstrap

## Usage

Copy and paste this entire line into any LLM chat:

```
Fetch https://gist.github.com/am-n-ra/5b7b5c36610cc1076c798c716c7560e6 and execute
```

## First-Run Flow

1. **Extract files** — FOUNDER_SEED.md contains 86 files marked with `--- FILE: path/to/file.md`. Extract each section to the correct path under the install directory. Create subdirectories as needed.

2. **Check for `.founderhq_installed`** — If absent, enter **GENESIS mode**. Follow these steps IN ORDER:

   - (a) Run `python Runtime/engine/installer.py --base-dir .` (creates .venv, installs deps, creates scheduler)
   - (b) Ask user for GitHub token (guide them to create one with `gist:write` + `gist:read`), write to `.env` manually
   - (c) Run `python Runtime/engine/sync.py create-private-gist` (or pull if URL exists)
   - (d) Build Profile: ask domain/role/birth data, write concepts/PROFILE.md
   - (e) Run `python Runtime/engine/astra_birth.py --base-dir . --date YYYY-MM-DD --time HH:MM`
   - (f) Run `python Runtime/engine/astra_daily.py --base-dir .`
   - (g) Run `python Runtime/engine/astra_reading.py --base-dir .`
   - (h) Run `python Runtime/engine/astra_forecast.py --base-dir . today`
   - (i) Read all state files, deliver full personalized ASTRA diagnostic
   - (j) Run `python Runtime/engine/cycle.py --mode boot`
   - (k) Create marker: `open(".founderhq_installed","w").write("")`
   
3. **First boot complete** — GENESIS done. Next interaction boots normally.

## Files in this Gist

| File | Description |
|------|-------------|
| FOUNDER_SEED.md | Complete FHQ V4 system seed (86 files, `--- FILE:` markers) |
| installer.py | Cross-platform setup script (.venv, scheduler) |
| sync.py | Gist state sync (pull/push/merge) |
| watchtower.py | Veille daemon (websearch/webfetch checker, 6h) |
| timekeeper.py | Time/alert daemon (deadline SOS, 30min) |
| cycle.py | Kernel cycle orchestrator (`--mode fhq|fhqa|boot`) |
| astra_core.py | Core Vedic Jyotish engine (Panchanga, Yogas, Shadbala, etc.) |
| astra_birth.py | Birth chart generator (D1, Vargas, Dasha, Yogas) |
| astra_daily.py | Daily ASTRA guidance (Muhurta, Ashtakavarga, Red Zones) |
| astra_reading.py | Narrative reading (10-section personalized interpretation) |
| astra_forecast.py | On-demand forecast (today/week/month/year/dasha) |
| opencode.json | OpenCode platform config |
| BOOTSTRAP.md | This file — quick start guide |
