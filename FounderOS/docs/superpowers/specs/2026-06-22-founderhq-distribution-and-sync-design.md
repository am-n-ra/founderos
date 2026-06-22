# FounderHQ Distribution & Sync — Design Spec

> **Status:** Draft
> **Date:** 2026-06-22
> **Owner:** System

---

## 1. Problem

FounderHQ has ~50 files (markdown + Python scripts). Distributing it means copying the entire folder. Syncing state between devices (PC ↔ mobile) requires manual work.

**Requirements:**
- Zero-dependency distribution: one URL or one file → full FHQ environment
- Automatic state sync between devices
- No LLM exposure of secrets (GitHub token)
- Works on any LLM (OpenCode, Claude Code, LM Arena, ChatGPT web)

---

## 2. Distribution: FOUNDER_SEED.md

A single markdown file containing all core FHQ files delimited by `--- FILE:` markers. Hosted on a public GitHub Gist.

### Format

```markdown
# FOUNDER SEED — FounderHQ Bootstrap

Instructions for the LLM: read this file, create every `--- FILE:` block as a file.

---

--- FILE: FounderOS/SYSTEM_PROMPT.md ---
[full content]
--- END ---

--- FILE: FounderOS/Runtime/RUNTIME_KERNEL.md ---
[full content]
--- END ---

... (30-40 files, ~50K tokens total)
```

### Usage

```
User: fhq https://gist.github.com/user/abc123/founder-seed.md
```

LLM webfetches the URL, parses `--- FILE:` blocks, creates all files in 3-5 responses.

### Not included in seed

User-generated content: `projects/`, `State/CURRENT_STATE.md` values, `TIMELINE.md` entries, `KNOWLEDGE.md` entries, `concepts/MEMORY.md` content. These are created by the user through normal FHQ operation.

---

## 3. Secrets: `.env` File

A single `.env` file at the root of `FounderHQ/` containing environment variables. **Never read by the LLM.** Only read by Python scripts.

### Content

```
FHQ_GIST_URL=https://gist.github.com/tonuser/abc123
FHQ_GIST_TOKEN=ghp_xxxxxxxxxxxx
```

### Security rules

1. File permissions: `600` (owner read/write only)
2. Never included in any `.md` file
3. Never passed to the LLM in any prompt
4. Only read by `Runtime/engine/sync.py` via `python-dotenv`
5. Token scoped to `gist:write, gist:read` (GitHub fine-grained token)

---

## 4. State Sync: `sync.py`

Script that handles push/pull to a private GitHub Gist. The LLM **calls the script** (`run engine/sync.py pull`) and sees the result — never the token.

### Commands

```
sync.py pull
  → GET Gist API (with token from .env)
  → Downloads snapshot.json
  → Validates structure
  → Writes to State/_SYNC_INBOX.md (staging, not merged)
  → Returns: "New snapshot [date]" or "No changes"

sync.py push
  → Reads CURRENT_STATE.md + CADENCE.md + TIMELINE.md
  → Compacts into snapshot.json
  → POST to Gist API (with token from .env)
  → Returns: "Synced [timestamp]" or error message

sync.py merge
  → Reads State/_SYNC_INBOX.md
  → Applies changes to CURRENT_STATE.md, CADENCE.md, TIMELINE.md
  → Returns: changelog of what was merged
```

### Snapshot format (snapshot.json)

```json
{
  "version": 1,
  "timestamp": "2026-06-22T14:30:00Z",
  "state": {
    "date": "2026-06-22 14:30 Lome UTC+0",
    "mode": "SURVIVAL",
    "cash": 2679,
    "top_priority": "Find client for maize",
    "bottleneck": "Cash insuffisant"
  },
  "cadence": {
    "session_start": "08:15",
    "session_end": "14:30",
    "day_objective": "Valider SOJACO"
  },
  "timeline": [
    {
      "date": "2026-06-22 08:15",
      "event": "Boot",
      "decision": "Start day",
      "outcome": "Session started"
    }
  ],
  "projects": {
    "SOJACO": {"phase": "VALIDATION", "next_action": "Find client"},
    "OMNI": {"phase": "LAUNCH", "next_action": "Pitch Day prep"}
  }
}
```

---

## 5. Fallback Sync: `snapshot.py`

Alternative for environments without HTTP auth capability (basic LM Arena, ChatGPT web).

### Commands

```
snapshot.py generate
  → Reads state files
  → Produces compact markdown summary (~2K tokens)
  → Writes to State/EXPORT_SNAPSHOT.md

snapshot.py merge
  → Reads State/IMPORT_SNAPSHOT.md
  → Patches local files
  → Returns changelog
```

### Flow (token-less)

```
PC: fhq shutdown --export
  → LLM: run engine/snapshot.py generate
  → Output: short snapshot text

  User copies text, switches device.

Mobile: "fhq [paste snapshot]"
  → LLM reads snapshot, continues work.
  → "fhq shutdown --export"
  → New snapshot produced.

  User copies back, switches device.

PC: "fhq resume [paste snapshot]"
  → LLM: run engine/snapshot.py merge
  → Session continues with updated state.
```

---

## 6. First-Run: GENESIS

When `.founderhq_installed` does not exist at boot, the LLM executes GENESIS:

### Step-by-step

1. **Ask for token proactively** — LLM detects `.founderhq_installed` missing, asks user for GitHub token (scope gist)
   - User can type `skip` to do it later
   - Token is stored to `.env` immediately
   - LLM never reads the token value back

2. **Create all core files** — Parse `FOUNDER_SEED.md` (from context or webfetch), create every file

3. **Create `.venv`** — `python -m venv .venv` (install Python first if missing)

4. **Install dependencies** — `.venv\Scripts\pip install requests python-dotenv`

5. **Install scripts** — `run engine/installer.py --base-dir .`

6. **Test sync** — `run engine/sync.py push` with the new token, then `pull`

7. **Create `.founderhq_installed`** — empty marker file

8. **Create `State/SYNC_CONFIG.md`** — configuration readable by LLM

9. **Continue normal session** — ORIENT → DECIDE → ACT

---

## 7. Boot Sequence Changes

### SYSTEM_PROMPT.md Boot Sequence (updated)

```
0. First-run check → .founderhq_installed exists?
   NO → execute GENESIS (ask token, create files, .venv, scripts)
1-13. (existing steps)

After step 13 (Daily Kickoff):
  → run engine/sync.py pull (if SYNC_CONFIG.md exists)
```

### SYSTEM_PROMPT.md Intent Classification (updated)

```
| Message starts with **"boot"** | BOOT | Full initialization. GENESIS if first run. |
| Message starts with **"shutdown"** | SHUTDOWN | End session. Save state. Sync push. |
| Message starts with **"fhq"** | FHQ_MODE | Full kernel cycle. Sync pull if first fhq today. |
```

### RUNTIME_KERNEL.md Phase 1: BOOT (updated)

Add before existing operations:
```
0. Check .founderhq_installed
   - If absent → execute GENESIS procedure
```

### RUNTIME_KERNEL.md Phase 7: UPDATE (updated)

Add after existing operations:
```
6. Run engine/sync.py push (if SYNC_CONFIG.md exists)
```

---

## 8. File Inventory

### New files

| File | Purpose | Access |
|------|---------|--------|
| `FOUNDER_SEED.md` | Distribution: all core files in one file | Public Gist |
| `.env` | Secrets (token, Gist URL) | 600, scripts only |
| `.founderhq_installed` | Marker: installation complete | LLM reads |
| `.venv/` | Isolated Python environment | Scripts only |
| `State/SYNC_CONFIG.md` | Sync configuration (no token) | LLM reads |
| `State/_SYNC_INBOX.md` | Staging area for incoming sync | LLM reads |
| `State/EXPORT_SNAPSHOT.md` | Generated portable snapshot | LLM reads |
| `State/IMPORT_SNAPSHOT.md` | Snapshot to merge (user pastes) | LLM reads |
| `Runtime/engine/sync.py` | Gist push/pull/merge (reads .env) | Called by LLM |
| `Runtime/engine/snapshot.py` | Portable snapshot gen/merge | Called by LLM |

### Modified files

| File | Change |
|------|--------|
| `SYSTEM_PROMPT.md` | Boot sequence: first-run check + sync pull. Intent: GENESIS mode. Shutdown: sync push. |
| `RUNTIME_KERNEL.md` | Phase 1: GENESIS branch. Phase 7: sync push. |
| `Runtime/engine/installer.py` | Create .venv, write .env, create marker |
| `Runtime/engine/__init__.py` | Document sync.py, snapshot.py |
| `State/CADENCE.md` | Add Sync section to Day |
| `Protocols/SOURCE_OF_TRUTH.md` | Register all new files |
| `Runtime/engine/watchtower.py` | Read .env if needed (future) |
| `Runtime/engine/timekeeper.py` | Read .env if needed (future) |

---

## 9. Security Model

1. **GitHub token** stored in `.env` with `600` permissions
2. **Only `sync.py`** reads `.env` — LLM never sees the token value
3. LLM **calls** `sync.py` as a subprocess — input is "push" or "pull", output is "OK" or error
4. Snapshot contains **operational data only** (CURRENT_STATE fields, project phases, timeline events) — no passwords, no secrets
5. Snapshot is pushed to a **private Gist** — invisible to search, requires token to read
6. Fallback snapshots are copied between contexts by the user — no third party

---

## 10. Error Handling

| Error | Behavior |
|-------|----------|
| Token not configured | LLM asks proactively at boot. Sync skipped if absent. |
| Sync push fails (no network) | LLM logs error, continues. Retry on next shutdown. |
| Sync pull fails | LLM continues with local state. Marks "Sync failed" in response. |
| Merge conflict | LLM presents diff to user: "Remote changed X, local changed X. Which wins?" |
| Python not found | LLM installs Python via winget/choco/apt/brew depending on OS. |
| `.venv` missing | LLM re-creates it on next `fhq boot`. |
