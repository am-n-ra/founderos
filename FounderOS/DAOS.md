# FounderOS V4 — DAOS (Daily Autonomous Operating System)

## Purpose

DAOS owns the how of daily execution. It takes MOS's priorities and produces concrete actions, scripts, schedules, and tools for the day.

## Position in FounderHQ

DAOS owns daily execution. It is loaded by RUNTIME Phase 2 (Decide) or when SURVIVAL Auto-Drive triggers. It receives priorities from MOS and produces concrete actions the founder can execute immediately.

## Inputs
- `concepts/MOS.md` — current top priority
- `State/CURRENT_STATE.md` — cash, blockers, mode
- `concepts/PLAYBOOK.md` — relevant playbooks for today's situation

## Outputs
- Action modules — scripts, timing, expected outcome, fallback for 1-3 actions
- Execution context — what changed since yesterday, what is blocked, what is ready

## Relations
- **MOS** — receives top priority
- **CEOS** — delegates content actions when applicable
- **FAOS** — delegates financial actions when applicable
- **TIMELINE** — writes execution outcomes after each action

## Workflow

## Daily Outputs

1. **Action List** — 1-3 concrete actions derived from MOS's top priority
2. **Action Modules** — For each action, provide: script, timing, expected outcome, fallback
3. **Context** — What changed since yesterday, what is blocked, what is ready
4. **Tools** — Playbooks, workflows, templates relevant to today's actions

## Operating Rhythm

When invoked by RUNTIME Phase 2 (Decide):

1. Read MOS's current top priority
2. Read CURRENT_STATE.md for constraints (cash, time, blockers)
3. Read PLAYBOOK.md for relevant playbooks
4. Generate 1-3 action modules
5. Present to user with recommendation
6. After execution, document outcome in TIMELINE.md

## Action Module Format

```
## Action Module: [Name]
- Priority: [High/Medium/Low]
- Effort: [Time, resources needed]
- Script: [What to say/do]
- Expected Outcome: [What success looks like]
- Fallback: [What to do if this fails]
- Playbook: [Reference to PLAYBOOK.md if applicable]
```

## Integration

- DAOS may reference CEOS (Content Engineering) for content actions
- DAOS may reference FAOS (Fundraising) for financial actions
- DAOS may reference LEOS (Learning) for research actions
- DAOS writes to TIMELINE.md after each action

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
