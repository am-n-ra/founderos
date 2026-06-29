# FounderOS V4 — KNOWLEDGE_EVOLUTION_ENGINE

## Purpose

The KNOWLEDGE_EVOLUTION_ENGINE owns the long-term evolution of FounderHQ's knowledge base — ensuring knowledge stays accurate, relevant, and well-structured as the system grows.

## Position in FounderHQ

KNOWLEDGE_EVOLUTION_ENGINE manages the FounderHQ knowledge base — storing structured facts, validating new information, identifying gaps, and surfacing relevant knowledge when needed. It is the durable memory layer that persists across sessions. It is loaded when any module needs to store or retrieve structured knowledge.

## Inputs
- New knowledge — facts, insights, patterns from any module (ASTRA, RIOS, PATTERN_ENGINE, etc.)
- `concepts/MEMORY.md` — existing knowledge base
- Knowledge queries — what does the system need to know?
- `concepts/TIMELINE.md` — context for temporal knowledge

## Outputs
- Verified knowledge — facts validated and stored in canonical form
- Knowledge gaps — what the system needs to know but doesn't yet
- Relevance-ranked knowledge — information surfaced in response to queries
- Knowledge versioning — what changed, when, and why

## Relations
- **ASTRA** — reflective insights stored as verified knowledge
- **RIOS** — research findings stored as structured facts
- **PATTERN_ENGINE** — validated patterns stored in knowledge base
- **ALL MODULES** — any module may query knowledge for contextual awareness
- **TIMELINE** — knowledge versioning recorded as timeline events

## Workflow

### Evolution Cycle

#### Monthly (Light)
1. Check KNOWLEDGE.md for entries older than 30 days
2. Flag entries without recent verification
3. Check for duplicate or contradictory entries
4. Report findings to user

#### Quarterly (Deep)
1. Full knowledge audit: every entry in KNOWLEDGE.md reviewed
2. Ontology check: does the knowledge structure still fit reality?
3. Deprecation sweep: mark entries no longer relevant
4. Synthesis: identify meta-patterns across knowledge entries
5. Reorganization: restructure if current categories no longer fit
6. Report: what changed, what was deprecated, what was synthesized

#### Triggers
- New knowledge contradicts old knowledge → reconcile immediately
- A pattern is detected 5+ times → synthesize into a principle
- A knowledge entry has 0 references in 60 days → flag for deprecation

### Knowledge Decay

- Time-sensitive knowledge (prices, contacts, platform rules) decays in 30 days
- Principle-level knowledge (what works, patterns) decays in 90 days
- Identity-level knowledge (mission, values) does not decay but should be reviewed annually
- Decayed knowledge is flagged, not deleted

### Integration

- KNOWLEDGE_EVOLUTION_ENGINE receives patterns from PATTERN_ENGINE
- KNOWLEDGE_EVOLUTION_ENGINE receives new learning from LEOS
- KNOWLEDGE_EVOLUTION_ENGINE reports results to CONTINUOUS_IMPROVEMENT

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
