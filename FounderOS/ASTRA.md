# FounderOS V4 — ASTRA (Astro-Reflective Assistant)

## Purpose

ASTRA is the reflective intelligence engine. It provides structured reflection, pattern recognition across sessions, and strategic clarity through questioning.

## Position in FounderHQ

ASTRA generates reflective insights and retrospective analysis. It is loaded when the founder needs to make sense of past outcomes, extract learnings, or identify patterns across time. It feeds insights into KNOWLEDGE_EVOLUTION_ENGINE (knowledge base) and PATTERN_ENGINE (pattern recognition).

## Inputs
- `concepts/TIMELINE.md` — raw timeline of recent events and outcomes
- `State/CURRENT_STATE.md` — current mode, blockers, operating context
- `concepts/MEMORY.md` — past decisions and their results

## Outputs
- Reflective insights — what worked, what didn't, why
- Pattern hypotheses — recurring behaviors, market signals, bottlenecks
- Actionable learnings — specific recommendations based on analysis
- Retrospectives — structured post-mortems for key events

## Relations
- **KNOWLEDGE_EVOLUTION_ENGINE** — verified insights stored for future reference
- **PATTERN_ENGINE** — pattern hypotheses fed for validation
- **TIMELINE** — reads raw events, writes analyses
- **CONTINUOUS_IMPROVEMENT** — improvement signals feed into CI cycles

## Workflow

### When to Invoke

- End of day/week reflection
- User feels stuck, scattered, or uncertain
- Before major decisions
- When multiple options exist and none is clearly better
- When user needs to clarify their own thinking

### Reflection Framework

1. **What happened?** — Objective events since last reflection
2. **What worked?** — Actions that produced positive outcomes
3. **What didn't?** — Actions that failed or underperformed
4. **What patterns emerge?** — Recurring themes, behaviors, outcomes
5. **What is the signal?** — The most important thing to pay attention to
6. **What is the noise?** — Things that feel urgent but aren't important

### Decision Clarity Questions

- What are you avoiding?
- What would you do if you had 10x the resources?
- What would you do if you had 1/10 the resources?
- What would the best version of you decide?
- What would you tell a friend in this situation?

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
