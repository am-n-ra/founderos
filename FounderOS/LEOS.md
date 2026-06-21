# FounderOS V4 — LEOS (Learning Engineering OS)

## Purpose

LEOS owns the learning pipeline — designing how new knowledge is acquired, structured, and integrated into FounderHQ.

## Position in FounderHQ

LEOS manages the founder's learning ecosystem — tracking what needs to be learned, how it was learned, and ensuring retention. It is loaded when the founder needs to acquire new skills, review past learning, or organize a learning path. It feeds skill acquisition data into KNOWLEDGE_EVOLUTION_ENGINE and priorities into MOS.

## Inputs
- `State/CURRENT_STATE.md` — available time for learning
- `concepts/MISSION.md` — skills needed for current missions
- `concepts/PLAYBOOK.md` — operational knowledge to master

## Outputs
- Learning paths — structured sequence of skills to acquire
- Progress tracking — what has been learned, retention level, gaps
- Review schedules — spaced repetition for retention
- Skill gaps — analysis of missing capabilities vs. mission requirements

## Relations
- **MOS** — learning priorities aligned with mission needs
- **KNOWLEDGE_EVOLUTION_ENGINE** — knowledge artifacts stored as structured facts
- **CONTINUOUS_IMPROVEMENT** — learning velocity tracked as improvement metric

## Workflow

### Learning Pipeline

1. **Identify knowledge gap** — What don't we know that we need to know?
2. **Design learning approach** — Research, experiment, expert consultation, or trial-and-error?
3. **Execute** — Gather information per approach
4. **Validate** — Cross-reference, test against reality
5. **Integrate** — Store in KNOWLEDGE.md with confidence level

### Learning Priorities (Current)

1. Soya supply chain: supplier reliability, pricing patterns, logistics
2. YouTube content: hook retention mechanics, audience building
3. FounderOS: what workflows need improvement, what concepts need refinement

### Learning Formats

- **Active**: Deliberate research, experiments, A/B testing
- **Passive**: Pattern detection from daily operations
- **Borrowed**: Learning from others (competitors, mentors, content)

### Integration

- LEOS supplies CEOS with research for content topics
- LEOS supplies FAOS with market data for fundraising
- LEOS feeds into KNOWLEDGE_EVOLUTION_ENGINE for quarterly synthesis

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
