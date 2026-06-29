# FRE — RUNTIME KERNEL

## Purpose

Define the universal execution cycle that every FounderHQ runtime implements. The kernel is platform-independent and LLM-independent.

## Identity

The kernel is the decision cycle. It transforms observation into action and action into learning. It is the heartbeat of FounderHQ.

## The Kernel Cycle

```
BOOT
  ↓
OBSERVE
  ↓
ORIENT
  ↓
DIAGNOSE ◄── auto-subagent loop
  ↓
DECIDE
  ↓
ACT
  ↓
LEARN
  ↓
UPDATE
  ↓
(repeat from OBSERVE)
```

## Phase 1: BOOT

Execute at session start - triggered by user message starting with `boot` or first `fhq` of the day. If the session is already active (a prior `fhq` or `boot` was processed today), BOOT is skipped and the cycle starts at OBSERVE.

### Full Boot (triggered by `boot` or first daily `fhq`):

Operations:
0. **GENESIS Check** - Check if `.founderhq_installed` exists. If absent, execute GENESIS: ask user for GitHub token, create .venv, install dependencies, create .env, run installer, create `.founderhq_installed` marker.
1. Load State/CURRENT_STATE.md
2. Load State/PRIORITY_MATRIX.md
3. Load State/CADENCE.md
4. Load State/LIFECYCLE.md
5. Load State/WATCH_REGISTRY.md
6. Load State/ALERTS.md - read and clear
7. Load State/WATCH_REPORT.md
8. Compute datetime in Lome UTC+0
9. Set Session Start timestamp in CADENCE.md (Day -> Session Start)
10. Scan all concept footers for staleness (>48h)
11. Report: datetime, mode (SURVIVAL/GROWTH/SCALE), cadence context, lifecycle phases, top priority, stale concepts, active alerts
12. **Sync Pull** - If `.env` exists with FHQ_GIST_TOKEN, run `sync.py pull` to fetch remote state. On failure, continue with local state.

Output: Session awareness established.

### Quick Boot (triggered by subsequent `fhq` same day):

Operations:
1. Re-read CURRENT_STATE.md (may have changed since last cycle)
2. Re-read LIFECYCLE.md (project phases may have shifted)
3. Compute current datetime, update CADENCE.md Hour section
4. Check ALERTS.md for new entries from background scripts

Output: Updated temporal awareness, skipping full initialization.

## Phase 2: OBSERVE

Receive and process input from the founder or the environment.

Operations:
1. Receive raw input (message, file change, time trigger)
2. Scan input against INFO_CAPTURE_PROTOCOL mapping
3. Capture any operational data found into appropriate files
4. Classify input into an action type (DECISION_GATES)

Output: Cleaned, classified input ready for orientation.

## Phase 3: ORIENT

Understand what the input means in the current context. Cross-reference cadence, lifecycle, and active frameworks.

Operations:
1. Load relevant concepts for the classified action type
2. Verify freshness of loaded concepts
3. **Cross CADENCE x LIFECYCLE**: Determine current temporal position (week, month, quarter) and active project phases. Select frameworks matching lifecycle phase from LIFECYCLE.md phase-to-framework mapping.
4. Scan all active projects in PRIORITY_MATRIX for data room completeness
5. Flag any contradictions between files
6. Check current constraints: cash, energy, time, blockers
7. **Check ALERTS.md** for any background script notifications since last cycle
8. **Check WATCH_REPORT.md** for any new veille findings

Output: Situational awareness with flagged risks, cadence context, lifecycle-informed framework selection.

## Phase 4: DIAGNOSE

Automatically detect what needs to be fixed and determine the highest-leverage action. On `fhqa`/`fhq`, this phase runs automatically via cycle.py → diagnose.py. The diagnosis output (`_DIAGNOSE.md`) prescribes the action; the LLM spawns a subagent to research/plan/execute.

### Diagnosis Sources:
1. **Revenue check** — if cash < 1,500 FCFA, REVENUE_CRITICAL flag → activate EA or micro-revenue action
2. **Opportunity windows** — WATCH_REGISTRY 🔴 items expiring or partner responses pending
3. **Stale concepts** — any concept > 48h without update
4. **Project health** — missing README.md / strategic docs in active projects
5. **Aimless state** — idle time > 30min, unchecked plan items, turn loops
6. **Research gaps** — missing information needed for key decisions (compute, grants, data)

### Subagent Loop (automatic):
After diagnosis, the LLM MUST:
1. If **research_needed** exists → spawn a `research` subagent with the query
2. If **action_ready** (no research needed) → spawn an `execution` subagent with the action payload
3. If both exist → spawn research first, then plan from findings
4. The subagent MUST write its output to `_SUBAGENT_PLAN.md` before executing. Format: Goal → Steps → Evidence → Fallback.
5. Present the plan + action payload for approval before irreversible steps

### Escalation Rule:
- If the recommended action involves spending money, external commitment, or public posting → present for approval with full payload
- If purely internal (file updates, concept refresh, state read) → execute directly
- Check `requires_approval` field in _DIAGNOSIS.md: if False, execute directly without asking

Output: Diagnosis with prescribed action and subagent type. Subagent output written to _SUBAGENT_PLAN.md.

## Phase 5: DECIDE

Choose the single highest-leverage action.

Operations:
1. Apply DECISION_GATES: is this financial, legal, external?
2. Apply PRIORITIZATION_PROTOCOL: is this the right action NOW?
3. If SURVIVAL mode and DIRECT classification: auto-generate action module
4. If escalation required: present options with recommendation, await decision
5. Select one action

Output: A clear, constrained decision.

## Phase 6: ACT

Execute the selected action.

Operations:
1. Load the relevant module (DIOS, VAOS, CEOS, etc.)
2. Load the relevant workflow if applicable
3. Execute the action
4. Document the execution

Output: Action completed.

## Phase 7: LEARN

Extract lessons from the action and its outcome.

Operations:
1. What worked?
2. What didn't?
3. What surprised us?
4. Is there a pattern?
5. Is there a new playbook?

Output: Knowledge captured.

## Phase 8: UPDATE

Persist all changes to files.

Operations:
1. Update CURRENT_STATE.md with new operational state
2. Update TIMELINE.md (Event → Decision → Outcome)
3. Update KNOWLEDGE.md with validated lessons
4. Update affected concept files
5. Save session objective and next-session priority
6. **Sync Push** - If `.env` exists with FHQ_GIST_TOKEN, run `sync.py push` to persist state to remote Gist. On failure, state remains local.

Output: State preserved for next session.

## Kernel Principles

1. **LLM is a component** — the kernel cycles regardless of which LLM executes it
2. **Pass by reference** — can skip phases if input demands immediate action (e.g., "stop")
3. **No phase skipping without flag** — if a phase is skipped, it must be declared
4. **Cash-aware** — if cash < 1,500 FCFA, DECIDE must prioritize revenue generation
5. **File-based** — all outputs are persisted to files before the next cycle

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | FRE |
| Purpose | Universal execution cycle for FounderHQ. Platform-independent decision loop. |
| Dependencies | FRE_SPEC.md, ADAPTER_INTERFACE.md, SYSTEM_PROMPT.md |
