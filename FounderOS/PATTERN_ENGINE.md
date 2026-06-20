# FounderOS V3 — PATTERN_ENGINE

## Purpose

The PATTERN_ENGINE detects recurring structures across actions, outcomes, decisions, and behaviors — converting raw experience into actionable pattern awareness.

## Pattern Types

1. **Behavioral Patterns** — How the user reacts to certain situations
2. **Outcome Patterns** — What types of actions consistently succeed or fail
3. **Timing Patterns** — When things happen, how long they take
4. **Blockage Patterns** — What consistently blocks progress
5. **Decision Patterns** — How decisions are made and which approaches work
6. **Market Patterns** — Recurring signals in the external environment

## Detection Methods

1. **Timeline Analysis** — Scan TIMELINE.md for repeated Event → Decision → Outcome sequences
2. **Knowledge Analysis** — Scan KNOWLEDGE.md for patterns already documented
3. **Behavioral Observation** — Note recurring user behaviors (procrastination patterns, energy patterns, etc.)
4. **External Signal Detection** — Market trends, platform changes, competitor moves

## Pattern Format

```
## Pattern: [Name]
- Type: [Behavioral/Outcome/Timing/Blockage/Decision/Market]
- Evidence: [Specific instances with dates]
- Confidence: [High/Medium/Low/Speculative]
- Implication: [What this means for what we should do]
- Action: [What to do about it]
```

## Outputs

- New patterns stored in KNOWLEDGE.md
- Pattern-based recommendations to MOS and RUNTIME
- Alerts when a known pattern is repeating

## Integration

- PATTERN_ENGINE is invoked by RUNTIME Phase 4 (Learn)
- PATTERN_ENGINE feeds into PLAYBOOK_ENGINE for playbook creation
- PATTERN_ENGINE feeds into KNOWLEDGE_EVOLUTION for knowledge refinement

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | TIMELINE.md, KNOWLEDGE.md, RUNTIME |
