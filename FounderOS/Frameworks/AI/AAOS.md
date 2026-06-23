# AAOS — Automation & Agents Operating System

## When to Use This Lens

Agent design, workflow automation, reduction of repetitive manual tasks.

## Required Questions

1. Is this task repetitive? (frequency, duration, human cost)
2. Can it be standardized into deterministic steps?
3. What is the error tolerance of the automation?
4. Is the automation effort less than the cost of manual repetition?
5. What level of oversight is required (auto / approved / supervised)?
6. Does the automation create leverage or technical debt?

## Principles

- Automate only what is standardized and understood.
- Hierarchy: Documentation → Standardization → Automation → Delegation.
- Do not automate what changes every week.
- Automation without oversight generates noise.
- A poorly defined agent is worse than no agent at all.

## Antipatterns

- Automating before standardizing
- Automating a process you don't understand
- Creating an agent without clear boundaries (scope, authority, escalation)
- Confusing automation with human delegation
