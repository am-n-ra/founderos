# DAILY_KICKOFF

## Concept

DAILY_KICKOFF is the first execution sequence of every session. It ensures the system never starts a day aimless. Every session begins with a structured kickoff or the system does not respond.

---

## When It Fires

1. **First user message of the day** — the first `fhq`/`fhqa`/`boot` after a session gap >= 4 hours triggers automatic kickoff
2. **Explicit `kickoff` command** — user says "kickoff", "daily", "plan the day", "commencer", "on fait quoi aujourd'hui"
3. **Post-boot** — BOOT mode always runs kickoff after cycle output

---

## Sequence

```
User message (first of day / "kickoff" / "boot")
    ↓
[FHQ_ASTRA/FHQ_MODE/BOOT] → run cycle.py --mode <mode>
    ↓
kickoff.generate_daily_plan() fires (for boot mode)
    ↓
```

### Step-by-step

| # | Action | File Read | Purpose |
|---|--------|-----------|---------|
| 1 | Read CURRENT_STATE | State/CURRENT_STATE.md | Extract mode, cash, top priority, bottleneck |
| 2 | Read PRIORITY_MATRIX | State/PRIORITY_MATRIX.md | Extract active projects, warnings, next actions |
| 3 | Read cash status | CURRENT_STATE (Cash field) | Determine if < 1,500 FCFA |
| 4 | Read ALERTS | State/ALERTS.md | Check HIGH alerts, active warnings |
| 5 | Read ASTRA_DAILY | State/ASTRA_DAILY.md | Extract muhurta scores, Rahu Kaal, Sade Sati (if fhqa mode) |
| 6 | Generate DAILY_PLAN | — | Write to State/DAILY_PLAN.md |
| 7 | Set response header | — | Write to _CYCLE_REQUIRED_HEADER.md with kickoff marker |

---

## Decision Tree

```
Cash < 1,500 FCFA?
    ├── YES → ALL actions must serve revenue generation.
    │         Top priority = revenue, regardless of other projects.
    │         No actions that do not directly enable income.
    │
    └── NO  → Normal prioritization via PRIORITIZATION_PROTOCOL.
              Bottleneck-driven execution.
```

### Mode-specific behavior

- **fhq/fhqa modes:** Kickoff reads DAILY_PLAN if it exists from boot, otherwise generates a lightweight inline plan
- **boot mode:** Full DAILY_PLAN.md written to disk
- **DIRECT classification:** If no plan exists, generate one inline before responding

---

## AIMLESS PREVENTION

This section exists because the user said: *"Je ne peux plus me retrouver en roue libre sans rien à faire"* — the system MUST prevent aimless days.

### Rules

1. **If no DAILY_PLAN.md exists** at session start → generate one from CURRENT_STATE top priority + PRIORITY_MATRIX top 3 before any other action.
2. **If DAILY_PLAN.md is empty or has no actions** → cannot happen. Generation always produces at least 1 action.
3. **If DAILY_PLAN.md exists but all actions are done** → regenerate with next priorities from PRIORITY_MATRIX.
4. **If user says "what now" / "what should I do"** → never answer with a question. Always propose the next incomplete action from DAILY_PLAN.
5. **If user sends a vague message** (1-3 words, no clear intent) → classify as DIRECT, check DAILY_PLAN, propose specific action.
6. **SURVIVAL mode override:** If cash < 1,500, every plan must include at least one revenue-generating action as priority #1. If no revenue action exists in DAILY_PLAN, the plan is invalid.

### Recovery

If aimless state detected (no progress after 3+ turns):
1. Read DAILY_PLAN.md
2. Pick first incomplete action
3. Propose it with a concrete engagement: "Let's execute [action] now. 25 minutes."
4. Do not ask "is that okay?" — state the action and wait for confirmation or objection.

---

## Mission-Driven Mode

Since V4.2, DAILY_PLAN.md includes a MISSION ALIGNMENT section that maps each action
to its parent mission. This ensures no action is taken without mission context.
When MISSION.md is stale (>48h), kickoff flags it and suggests a mission review.

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Updated | 2026-06-27 |
| Owner | DAILY_KICKOFF |
| Depends On | CURRENT_STATE, PRIORITY_MATRIX, ALERTS, ASTRA_DAILY |
