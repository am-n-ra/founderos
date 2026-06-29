# Proactivity Gaps Fix — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix 4 proactivity gaps in FounderHQ — DIRECT dead end, no heartbeat, RUNTIME disconnected, unenforced next action.

**Architecture:** 5 edits to SYSTEM_PROMPT.md only. RUNTIME.md Phase 1-2 already exists — no changes needed.

**Files modified:** `FounderOS/SYSTEM_PROMPT.md` only.

---

### Task 1: Apply 5 Edits to SYSTEM_PROMPT.md

**File:** Modify `FounderOS/SYSTEM_PROMPT.md`

- [ ] **Step 1: Fix 1a — Intent Classification DIRECT row**

Read line 67. Current:
```
| Simple update, status, informational | DIRECT | Execute directly |
```
Edit to:
```
| Simple update, ambiguous, acknowledgment | DIRECT | SURVIVAL → load DAOS.md, propose 1 action module. Otherwise → respond directly |
```

- [ ] **Step 2: Fix 1b — New Critical Execution Rule 5**

After line 16 (`4. **Cash Awareness.**`), insert blank line + new rule:
```
5. **SURVIVAL Auto-Drive.** If mode = SURVIVAL and classification = DIRECT, load DAOS.md, generate 1 action module from current priority, and propose it. Do not wait for instruction.
```

- [ ] **Step 3: Fix 2 — Standard Session + Quick Session loops**

Standard Session line 92:
Edit: `1. Boot → 2. Classify → 3. PRG → 4. Load module → 5. Execute → 6. Update concepts → 7. Repeat from step 2`
→ `1. Boot → 2. Classify → 3. PRG → 4. Load module → 5. Execute → 6. Update concepts → 7. State next action → 8. Repeat from step 2`

Quick Session line 95-99:
After `5. Update affected concepts`, insert blank line + `6. State next action`

- [ ] **Step 4: Fix 3 — New Boot Step 8**

After line 45 (`7. **Integrity Check**`), insert:
```
8. **Daily Kickoff** — Execute RUNTIME Phase 1-2 (Assess cash/state → Decide top action). State today's single most important action.
```

- [ ] **Step 5: Fix 4 — "Recommend" → "MUST"**

Line 44. Edit:
`6. **Report Awareness** — State: datetime, mode, top priority, what changed, stale concepts, PRG status, next action`
→
`6. **Report Awareness** — State: datetime, mode, top priority, what changed, stale concepts, PRG status. MUST state next action.`

- [ ] **Step 6: Verify and commit**

Verify all 5 changes by reading the modified file.

```bash
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "fix: 4 proactivity gaps — DIRECT auto-drive, after-response action, Daily Kickoff, MUST enforce"
```
