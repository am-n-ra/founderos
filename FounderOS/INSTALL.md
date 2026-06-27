# FounderOS V4 — INSTALL

## Purpose

INSTALL is the deployment guide for setting up FounderOS in a new environment (new machine, new LLM, new IDE).

## Requirements

- Any LLM that supports reading and writing files (ChatGPT, Claude, Gemini, DeepSeek, LM Arena, local models)
- Any IDE or file system that supports markdown files
- Git (optional — for version tracking and reboot delta detection)
- Python 3.10+ (required for ASTRA engine)
- Operating System: Windows, macOS, Linux (any)

## Quick Install (Gist-based GENESIS)

FounderOS is distributed via a public Gist. On a fresh machine, the LLM fetches and runs the installer.

### What the LLM does

1. **Fetch the Gist**
   ```
   https://api.github.com/gists/5b7b5c36610cc1076c798c716c7560e6
   ```
   The LLM downloads the ZIP and extracts it into a new `FounderOS` directory.

2. **Verify files** — 12 bootstrap scripts should be present:
   `BOOTSTRAP.md`, `FOUNDER_SEED.md`, `installer.py`, `opencode.json`, `sync.py`, `watchtower.py`, `timekeeper.py`, `astra_core.py`, `astra_daily.py`, `astra_birth.py`, `astra_forecast.py`, `astra_reading.py`

3. **Run installer.py**
   ```bash
   python Runtime/engine/installer.py
   ```
   This creates a `.venv`, installs dependencies (requests, python-dotenv, pysweph), and sets up the directory structure.

4. **GENESIS conversation** — The LLM asks the user for:
   - **Business profile** (role, industry, tech stack, strategic needs, constraints)
   - **Birth data** (date, time, location) — for ASTRA Jyotish engine

5. **Build Profile** — The LLM writes:
   - `concepts/PROFILE.md` (business profile from user answers)
   - Runs `astra_birth.py` to generate `State/ASTRA_BIRTH.md` (birth chart, Dasha, Yogas)
   - Runs `astra_daily.py` to generate `State/ASTRA_DAILY.md` (today's guidance)
   - Runs `astra_reading.py` to generate `State/ASTRA_READING_RAW.md` (personalized narrative)
   - Creates `State/ASTRA_MODE.md` (default: `fhqa` mode)

6. **Boot** — The LLM loads `SYSTEM_PROMPT.md` and begins the session with full ASTRA awareness.

### For the user

If you're not an LLM, the manual steps are:
```bash
# Download and extract the Gist ZIP
curl -L -o founderos.zip https://api.github.com/gists/5b7b5c36610cc1076c798c716c7560e6.zip
# Extract into FounderOS/
# Run installer
python Runtime/engine/installer.py
# Then open a session with any LLM and provide SYSTEM_PROMPT.md
```

## What the LLM Does in Each Session

When you open `fhqa` mode:
1. Read `SYSTEM_PROMPT.md` (boot sequence)
2. Load all ASTRA state files (birth profile, daily, shadow, reading)
3. Report current Panchanga, Muhurta scores, Red Zones
4. Guide you proactively — "What should I do about this?"

`fhq` mode runs without ASTRA (standard FounderHQ).

## Troubleshooting

| Problem | Solution |
|---------|----------|
| LLM cannot find files | Check file paths in SYSTEM_PROMPT.md. Use absolute paths if needed. |
| Contradictions on first boot | Load SOURCE_OF_TRUTH.md. Resolve conflicts manually. |
| Freshness errors on first boot | Update concept footers. WF-007 threshold is 48h by default. |
| Git not found | Reboot system will work without git but with reduced delta detection. |
| LLM ignores protocol | Re-state SYSTEM_PROMPT.md. Emphasize "you are not an assistant." |
| swisseph import fails | Run `pip install pysweph` in the `.venv` |
| ASTRA scripts fail | Verify birth data was collected correctly in GENESIS step |

## Model Compatibility

FounderOS has been tested with:
- Claude (Opus, Sonnet)
- ChatGPT (GPT-4, GPT-4o)
- DeepSeek
- Gemini
- LM Arena

It should work with any model that can:
- Read and write files
- Follow multi-step procedures
- Maintain context across file operations

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-23 |
| Owner | System |
| Dependencies | GENESIS.md, SYSTEM_PROMPT.md, public Gist 5b7b5c36610cc1076c798c716c7560e6 |
