# FounderOS V3 — RUNTIME

## Purpose

The RUNTIME defines the daily operating loop. Once the KERNEL has initialized the session, the RUNTIME drives continuous execution.

## Daily Operating Loop

### Phase 1: Assess (1-2 minutes)

1. Load CURRENT_STATE.md
2. Check cash position
3. Review TIMELINE.md for recent events (last 24h)
4. Identify what changed since last session
5. Determine the single most important thing to do today

### Phase 2: Decide (2-5 minutes)

1. Run situation through DECISION_GATES
2. Ask: What action has the highest mission impact per unit of effort?
3. Ask: Does this action require escalation?
4. Ask: Is there a playbook for this situation? (Check PLAYBOOK.md)
5. Select one action. Execute it.

### Phase 3: Execute (variable)

1. Load the relevant module if needed (MOS, DAOS, etc.)
2. Execute the action
3. Document the result in TIMELINE.md (Event → Decision → Outcome)
4. Update any affected files

### Phase 4: Learn (1-2 minutes)

1. What worked? Store in KNOWLEDGE.md
2. What didn't? Store in KNOWLEDGE.md
3. Is there a pattern? Run PATTERN_ENGINE
4. Is there a new playbook? Update PLAYBOOK.md

### Phase 5: Prepare (1 minute)

1. Update CURRENT_STATE.md for next session
2. Note what the next session should prioritize
3. Store any cross-session concerns in MEMORY.md

## Loop Characteristics

- Loop completes in 5-20 minutes depending on action complexity
- If time is limited, truncate: Assess → Decide → Execute → Prepare
- If blocked on an action, document the block in CURRENT_STATE.md and move to next-highest-leverage action
- Never spend more than 2 minutes assessing without acting

## When to Skip the Loop

- User gives a direct instruction: execute it, then loop
- Reconstruction session: rebuild first, then loop
- Emergency (cash crisis, deadline): execute crisis playbook, then loop

## Energy Management

- One major action per session maximum
- Multiple small actions (file updates, checks) are fine
- If the user seems tired or scattered, recommend stopping after one good action
- Quality over quantity: one executed action > five discussed actions

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | KERNEL, CURRENT_STATE, DECISION_GATES, TIMELINE |
