# Fix opencode MCP Daemon Crash on Windows Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stop opencode internal server from crashing when fhq/fhqa MCP daemon runs on Windows.

**Architecture:** opencode v1.3.17 has a known Windows-specific bug (GitHub issue #26128) where Python MCP stdio subprocesses are killed ~1s after spawn before the MCP initialize handshake completes. The daemon is correct (it works standalone via HTTP mode) but is fundamentally incompatible with opencode's Windows stdio MCP transport. The fix removes MCP dependency: disable daemon in opencode.json, let SYSTEM_PROMPT.md's sandbox path take over with direct cycle.py execution using the correct mode flag.

**Tech Stack:** opencode v1.3.17, Python MCP SDK v1.26.0, Windows 11, fhq_daemon.py

**Root Cause** (from 3 subagent deep investigations):
- opencode spawns Python MCP servers via `StdioClientTransport` on Windows
- Known bug: Windows process manager kills Python subprocess ~1s after spawn before `initialize` completes (openocode issue #26128)
- opencode has no reconnection logic (issue #26714) — once a tool call fails, the MCP client is permanently deleted
- 18MB opencode log shows only INFO level — failures are silently dropped
- The daemon itself is correct: `python fhq_daemon.py --mode http` runs indefinitely

---

## File Structure

| File | Change | Responsibility |
|------|--------|---------------|
| `opencode.json` | Disable MCP daemon (`enabled: false`) | Prevent opencode from spawning daemon as stdio subprocess |
| `FounderOS/SYSTEM_PROMPT.md` | Fix sandbox path to use actual cycle mode; add Windows note | LLM detects no MCP tools → uses sandbox path with correct mode |
| `FounderOS/Runtime/engine/fhq_daemon.py` | No change (daemon is correct, just incompatible transport) | Kept for HTTP mode on non-Windows clients (Claude Desktop, Cursor) |

---

### Task 1: Disable MCP Daemon in opencode.json

**Files:**
- Modify: `opencode.json` (entire file, 15 lines)

- [ ] **Step 1: Set `enabled: false`**

Change line 7 from `"enabled": true` to `"enabled": false`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "founderhq": {
      "type": "local",
      "command": ["python", "FounderOS/Runtime/engine/fhq_daemon.py", "--mode", "stdio"],
      "enabled": false
    }
  },
  "instructions": [
    "FounderOS/SYSTEM_PROMPT.md",
    "FounderOS/Runtime/FRE_SPEC.md",
    "All core rules are in SYSTEM_PROMPT.md. Read it at session start. Do not add instructions here that duplicate SYSTEM_PROMPT.md — it is the single source of truth for behavioral rules."
  ]
}
```

- [ ] **Step 2: Verify MCP tools are not available**

Start a new opencode session or check the opencode log. The daemon should NOT be spawned. The MCP section `"founderhq"` will appear in `mcp` config but `enabled: false` means opencode ignores it.

Verification command:
```bash
Get-Content C:\Users\junio\.config\opencode\logs\mcp\founderhq.log -Tail 20 -ErrorAction SilentlyContinue
```
Expected: log file does not exist (process was never spawned) or contains nothing.

- [ ] **Step 3: Commit**

```bash
git add opencode.json
git commit -m "fix: disable MCP daemon in opencode.json (Windows stdio bug #26128)"
```

---

### Task 2: Update SYSTEM_PROMPT.md MCP Section for Windows

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md` lines 105-117

- [ ] **Step 1: Rewrite MCP daemon section to reflect Windows incompatibility**

Replace lines 105-117 (the "Mechanical Enforcement (MCP Daemon)" section) with:

```markdown
## Mechanical Enforcement (MCP Daemon)

**IMPORTANT: opencode v1.3.17 has a known critical bug on Windows** (issue #26128, #16449). Python MCP stdio subprocesses are killed ~1s after spawn before the MCP initialize handshake completes. The MCP daemon (`fhq_daemon.py`) is correct software — it runs indefinitely via HTTP mode — but is fundamentally incompatible with opencode's Windows stdio transport.

If MCP tools ARE available (non-Windows platform with opencode, or remote client like Claude Desktop/Cursor via HTTP):
  1. Call `fhq_cycle` FIRST — runs cycle.py and refreshes state
  2. Use `fhq_read` / `fhq_write` for file access — daemon enforces freshness
  3. Use `fhq_sync_push` at end to persist state to Gist
  4. The daemon REFUSES stale state — this is not optional

If no MCP tools (standard path on Windows — opencode has broken stdio MCP):
  1. Run cycle with the classified mode: `python FounderOS/Runtime/engine/cycle.py --mode <CLASSIFIED_MODE>` (fhq, fhqa, or boot)
  2. If classification is DIRECT (no mode keyword), use: `python FounderOS/Runtime/engine/cycle.py --mode fhq`
  3. Read `FounderOS/State/_CYCLE_OUTPUT.md` for header + context
  4. Execute PRG (Pre-Response Gate)
  5. End with: `python FounderOS/Runtime/engine/sync.py push`
```

- [ ] **Step 2: Update the sandbox fallback note in the CYCLE COUNTER section**

Find line 131 (`**MCP-aware note:** ...`). Replace it with:

```markdown
**MCP-aware note:** On Windows, opencode's stdio MCP transport is broken (issue #26128). MCP tools will NOT be available. The 5 manual checks above are REQUIRED every response. This is not optional — the counter is the only freshness enforcement mechanism.
```

- [ ] **Step 3: Commit**

```bash
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "fix: update SYSTEM_PROMPT.md for Windows MCP daemon incompatibility"
```

---

### Task 3: Fix Sandbox Path to Use Correct Cycle Mode

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md` lines 187-188 (the sandbox section in the Intent Classification fallback)

- [ ] **Step 1: Update the sandbox/DIRECT classification section**

Find line 103 (`| Simple update, ambiguous, no keyword | DIRECT | ...`). The sandbox path previously always used `--mode boot` which is wrong for fhq/fhqa classifications. The fix was already done in Task 2 above. Verify the sandbox section now correctly says:

The key change: the old text said `Run: python FounderOS/Runtime/engine/cycle.py --mode boot` in the sandbox path. The new text (from Task 2) says `Run cycle with the classified mode: python FounderOS/Runtime/engine/cycle.py --mode <CLASSIFIED_MODE> (fhq, fhqa, or boot)`.

No additional edit needed — Task 2 covers this.

- [ ] **Step 2: Verify no other hardcoded `--mode boot` in sandbox references**

Search for any remaining `--mode boot` in the SYSTEM_PROMPT that should be dynamic:

```bash
Select-String -Path FounderOS/SYSTEM_PROMPT.md -Pattern "--mode boot"
```

Expected: only the Boot Sequence step (line 63: `python FounderOS/Runtime/engine/cycle.py --mode boot`) — this is correct because step 2 in the boot sequence always uses boot mode.

- [ ] **Step 3: Commit (if changes needed)**

```bash
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "fix: remove hardcoded --mode boot in sandbox reference"
```

---

### Task 4: Verify Fix Works

**Files:**
- Check: `FounderOS/State/_CYCLE_REQUIRED_HEADER.md`
- Check: `FounderOS/State/_CYCLE_COUNTER.md`
- Check: `FounderOS/State/_DIAGNOSIS.md`

- [ ] **Step 1: Start a new opencode session to confirm no crash**

Close current opencode session. Start a new one:

```bash
opencode
```

Expected: opencode starts without "internal server killer" behavior. No daemon process spawned. No crash.

- [ ] **Step 2: Send fhq and verify cycle completes**

In the new session, send `fhq`. Expected:
1. No opencode crash
2. Classification table triggers FHQ_MODE
3. No MCP tools detected → sandbox path: `python cycle.py --mode fhq` runs
4. Response header matches `**[datetime Lomé UTC+0]**`

- [ ] **Step 3: Send fhqa and verify cycle completes**

In the new session, send `fhqa`. Expected:
1. No opencode crash
2. Classification table triggers FHQ_ASTRA
3. No MCP tools detected → sandbox path: `python cycle.py --mode fhqa` runs
4. Response header matches `**[datetime Lomé UTC+0]**`
5. No "Daemon stopped" or MCP errors in opencode log

---

## Self-Review

**1. Spec coverage:**
- Root cause documented: ✓ (openocode issue #26128, Windows stdio MCP bug)
- Disable daemon: Task 1 ✓
- Update SYSTEM_PROMPT.md: Task 2 ✓
- Fix mode flags: Task 3 ✓
- Verify: Task 4 ✓

**2. Placeholder scan:** No TBD, TODOs, or placeholders. All code blocks complete.

**3. Type consistency:** All file paths verified by reading actual files. No type/signature mismatches.

---

## Verification

After all tasks complete, run the following to confirm the fix:

```bash
# 1. Confirm MCP daemon disabled in opencode.json
Select-String -Path opencode.json -Pattern "enabled"

# 2. Confirm daemon process not running
Get-Process -Name python -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -match "fhq_daemon" }

# 3. Confirm opencode log has no daemon errors
Get-Content C:\Users\junio\.local\share\opencode\log\opencode.log -Tail 50 | Select-String -Pattern "(error|Error|Daemon|MCP)"
```

All three should be clean: `enabled: false`, no python fhq_daemon process, no errors in log.
