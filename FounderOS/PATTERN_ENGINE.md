# FounderOS V4 — PATTERN_ENGINE

## Purpose

The PATTERN_ENGINE detects recurring structures across actions, outcomes, decisions, and behaviors — converting raw experience into actionable pattern awareness.

## Position in FounderHQ

PATTERN_ENGINE identifies, validates, and tracks recurring patterns across FounderHQ operations. It is loaded when the founder or ASTRA suspects a pattern, or during routine analysis cycles. It feeds validated patterns into PLAYBOOK_ENGINE and KNOWLEDGE_EVOLUTION_ENGINE.

## Inputs
- `concepts/TIMELINE.md` — raw event stream for pattern scanning
- `State/CURRENT_STATE.md` — current operational context
- Pattern hypotheses — from ASTRA or founder observations
- `concepts/MEMORY.md` — past pattern records for validation

## Outputs
- Pattern candidates — potential recurring behaviors, signals, or bottlenecks
- Validated patterns — confirmed patterns with evidence and confidence level
- Pattern refutations — disproven hypotheses with reasoning
- Playbook triggers — validated patterns that suggest new playbooks

## Relations
- **ASTRA** — receives pattern hypotheses from reflective analysis
- **PLAYBOOK_ENGINE** — validated patterns may produce new or updated playbooks
- **KNOWLEDGE_EVOLUTION_ENGINE** — confirmed patterns stored as structured knowledge
- **TIMELINE** — reads events, writes pattern discoveries

## Workflow

### Pattern Types

1. **Behavioral Patterns** — How the user reacts to certain situations
2. **Outcome Patterns** — What types of actions consistently succeed or fail
3. **Timing Patterns** — When things happen, how long they take
4. **Blockage Patterns** — What consistently blocks progress
5. **Decision Patterns** — How decisions are made and which approaches work
6. **Market Patterns** — Recurring signals in the external environment

### Detection Methods

1. **Timeline Analysis** — Scan TIMELINE.md for repeated Event → Decision → Outcome sequences
2. **Knowledge Analysis** — Scan KNOWLEDGE.md for patterns already documented
3. **Behavioral Observation** — Note recurring user behaviors (procrastination patterns, energy patterns, etc.)
4. **External Signal Detection** — Market trends, platform changes, competitor moves

### Pattern Format

```
## Pattern: [Name]
- Type: [Behavioral/Outcome/Timing/Blockage/Decision/Market]
- Evidence: [Specific instances with dates]
- Confidence: [High/Medium/Low/Speculative]
- Implication: [What this means for what we should do]
- Action: [What to do about it]
```

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
