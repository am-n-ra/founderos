# FounderOS V4 — RIOS (Research Intelligence OS)

## Purpose

RIOS owns external research — gathering, analyzing, and synthesizing information from outside FounderHQ.

## Position in FounderHQ

RIOS conducts structured research and information gathering. It is loaded when the founder needs to investigate a problem, market, competitor, or opportunity. It feeds research findings into KNOWLEDGE_EVOLUTION_ENGINE and decision support into DECISION_ENGINE.

## Inputs
- Research questions — what needs to be investigated
- `State/CURRENT_STATE.md` — constraints on research time and scope
- `concepts/MEMORY.md` — existing knowledge to avoid redundant research

## Outputs
- Research briefs — topic, scope, methodology, key questions
- Findings — structured information with sources and confidence levels
- Analysis — synthesis of findings with implications
- Recommendations — what to do based on research

## Relations
- **DECISION_ENGINE** — research findings inform decisions
- **KNOWLEDGE_EVOLUTION_ENGINE** — verified findings stored for future reference
- **CEOS** — research for content creation when applicable
- **TIMELINE** — research milestones recorded

## Workflow

### Research Types

1. **Market Research** — Pricing, competitors, trends, demand signals
2. **Supplier Research** — Soya suppliers, pricing, quality, reliability
3. **Platform Research** — YouTube algorithm, TikTok distribution, Shopify
4. **Tool Research** — AI tools, production tools, automation
5. **Content Research** — What works in our niche, audience preferences

### Research Protocol

1. **Define question** — What exactly do we need to know?
2. **Select sources** — Web, databases, expert consultation, experiments
3. **Gather data** — Structured collection
4. **Synthesize** — What does this mean for FounderHQ?
5. **Store** — KNOWLEDGE.md with source, date, confidence level
6. **Action** — What should we do with this knowledge?

### Research Quality

- Triangulate: at least 2 independent sources for any decision-grade fact
- Timestamp: every research output is dated
- Confidence label: High / Medium / Low / Speculative
- Bias check: what might this source be incentivized to say?

### Integration

- RIOS feeds LEOS for learning integration
- RIOS feeds VEAOS for strategic decisions
- RIOS feeds CEOS for content research

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
