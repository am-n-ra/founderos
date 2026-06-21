# FounderOS V4 — DECISION_ENGINE

## Purpose

The DECISION_ENGINE provides structured decision-making frameworks. It is invoked when the user faces a choice with meaningful consequences.

## Position in FounderHQ

DECISION_ENGINE provides structured decision-making frameworks for tradeoffs, prioritization, and strategic choices. It is loaded when MOS, VEAOS, or any module faces a decision with multiple options and non-trivial consequences. It feeds recommendations back to the calling module.

## Inputs
- Decision context — the question, options, criteria, constraints from the calling module
- `State/CURRENT_STATE.md` — current operational constraints and mode
- `concepts/TIMELINE.md` — relevant past decisions and outcomes

## Outputs
- Structured analysis — options evaluated against criteria with weighted scores
- Recommendation — best option with rationale
- Sensitivity analysis — how recommendation changes under different assumptions
- Decision record — written to TIMELINE.md for future reference

## Relations
- **MOS** — mission tradeoffs use DECISION_ENGINE for structured analysis
- **VEAOS** — strategic tradeoffs use PROACT framework via DECISION_ENGINE
- **FAOS** — financial tradeoffs analyzed for resource allocation decisions
- **TIMELINE** — every decision written to timeline for traceability

## Workflow

### When to Invoke

- User asks "What should I do?"
- Multiple viable options exist with different tradeoffs
- Decision involves risk, resource allocation, or opportunity cost
- User is indecisive or stuck

### Decision Framework: PROACT

1. **P**roblem — What exactly needs to be decided? State in one sentence.
2. **R**equirements — What must the decision satisfy? (constraints, must-haves)
3. **O**ptions — 2-3 viable paths, each with pros/cons
4. **A**ssessment — Score each option against requirements
5. **C**hoice — Recommendation with rationale
6. **T**rigger — What needs to happen to execute this decision?

### Decision Quality Checklist

- [ ] All relevant information loaded from files?
- [ ] Short-term and long-term consequences considered?
- [ ] Worst-case acceptable?
- [ ] Can this decision be reversed? If not, what's the cost?
- [ ] Is this a reversible decision? (Move fast if yes. Be careful if no.)
- [ ] What would I decide if I had more data? Less data? More money? Less money?
- [ ] Is this decision driven by fear or by strategy?

### Decision Logging

Every significant decision must be logged in TIMELINE.md:
- Date
- Decision
- Rationale
- Expected outcome
- Review date (when to check if it was right)

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
