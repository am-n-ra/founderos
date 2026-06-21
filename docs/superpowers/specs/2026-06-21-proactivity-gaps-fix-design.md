# Proactivity Gaps Fix — Design Spec

**Date:** 2026-06-21
**Status:** Approved
**Owner:** System

---

## Goal

Fix 4 proactivity gaps identified in FounderHQ review. All changes are in SYSTEM_PROMPT.md and RUNTIME.md only. Minimal edits, maximum impact.

---

## Fix 1: DIRECT → Auto-Drive (SURVIVAL mode)

**File:** SYSTEM_PROMPT.md

**Change 1a — Intent Classification table (line 67):**
```
| Simple update, status, informational | DIRECT | Execute directly |
```
→
```
| Simple update, ambiguous, acknowledgment | DIRECT | SURVIVAL → load DAOS.md, propose 1 action module. Otherwise → respond directly |
```

**Change 1b — Critical Execution Rules (new rule 5, after line 16):**
```
3. **Mission Alignment.** Before any action: what mission does this serve? If none, don't do it.
4. **Cash Awareness.** If cash < 1,500 FCFA, every action must generate or enable revenue.
```
→
```
3. **Mission Alignment.** Before any action: what mission does this serve? If none, don't do it.
4. **Cash Awareness.** If cash < 1,500 FCFA, every action must generate or enable revenue.
5. **SURVIVAL Auto-Drive.** If mode = SURVIVAL and classification = DIRECT, load DAOS.md, generate 1 action module from current priority, and propose it. Do not wait for instruction.
```

---

## Fix 2: After-Response Recommendation

**File:** SYSTEM_PROMPT.md

**Change 2 — Standard Session (line 92):**
```
### Standard Session
1. Boot → 2. Classify → 3. PRG → 4. Load module → 5. Execute → 6. Update concepts → 7. Repeat from step 2
```
→
```
### Standard Session
1. Boot → 2. Classify → 3. PRG → 4. Load module → 5. Execute → 6. Update concepts → 7. State next action → 8. Repeat from step 2
```

Also update Quick Session:
```
1. Load SOURCE_OF_TRUTH + CURRENT_STATE + MISSION + PROJECT
2. Freshness check (quick scan)
3. Classify and execute one high-leverage action
4. Execute PRG before responding
5. Update affected concepts
```
→
```
1. Load SOURCE_OF_TRUTH + CURRENT_STATE + MISSION + PROJECT
2. Freshness check (quick scan)
3. Classify and execute one high-leverage action
4. Execute PRG before responding
5. Update affected concepts
6. State next action
```

---

## Fix 3: RUNTIME Connected to Boot

**File:** SYSTEM_PROMPT.md

**Change 3 — Boot Sequence (new step 8 after line 45):**
```
7. **Integrity Check** — All critical files loaded? Temporal context established? No contradictions?
```
→
```
7. **Integrity Check** — All critical files loaded? Temporal context established? No contradictions?
8. **Daily Kickoff** — Execute RUNTIME Phase 1-2 (Assess cash/state → Decide top action). State today's single most important action.
```

---

## Fix 4: "Recommend" → "MUST"

**File:** SYSTEM_PROMPT.md

**Change 4 — Boot Step 6 (line 44):**
```
6. **Report Awareness** — State: datetime, mode, top priority, what changed, stale concepts, PRG status, next action
```
→
```
6. **Report Awareness** — State: datetime, mode, top priority, what changed, stale concepts, PRG status. MUST state next action.
```

---

## Verification

After changes:
1. SYSTEM_PROMPT.md line 67 shows DAOS fallback for SURVIVAL+DIRECT
2. SYSTEM_PROMPT.md has rule 5 in Critical Execution Rules
3. Standard Session includes "7. State next action"
4. Quick Session includes "6. State next action"
5. Boot Sequence has step 8 (Daily Kickoff referencing RUNTIME Phase 1-2)
6. Boot Step 6 says "MUST" not "recommend"
7. RUNTIME.md has Phase 1-2 defined (already exists — no change needed)

---

## Success Criteria

- User says "ok" in SURVIVAL mode → system proposes action from DAOS
- Every response ends with a next-action statement
- Boot always includes a "today's action" recommendation
- No ambiguity in whether to state next action (MUST vs recommend)
