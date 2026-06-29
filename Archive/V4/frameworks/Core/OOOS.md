# OOOS — Opportunity Operating System

## When to Use This Lens

- At every boot (Phase OBSERVE): to execute profile-derived watches and evaluate opportunities
- When the founder says: "watch", "opportunity", "credit", "grant", "deal", "new [tool/platform]"
- When a watch triggers and returns potential opportunities

## Required Inputs

- concepts/PROFILE.md — Founder profile (domain, stack, needs, constraints, watch domains)
- State/WATCH_REGISTRY.md — Active watches registry
- websearch / webfetch results — External opportunity data

## Outputs

- Scored opportunities list
- Top 3 recommendations with rationale
- Action payload (if score >= 60): what to do, where to go, what to prepare
- Updated Watch Domains in PROFILE.md (after iteration)

## Workflow

### 1. LOAD — Load Profile

Load PROFILE.md. Extract: Strategic Needs, Watch Domains, Scoring Preferences, Operational Constraints.

### 2. DERIVE — Derive Queries

From PROFILE Watch Domains, generate 1-2 websearch queries per domain. Prioritize domains matching current Strategic Needs (Priority 1 first).

### 3. DETECT — Search and Collect

Run websearch queries. Collect raw results: provider, program name, what it offers, eligibility, deadline, model access, value.

### 4. SCORE — Score Each Opportunity

For each result, compute score using PROFILE Scoring Preferences:

- **Relevance (0-40)**: Does this match the founder's domain and active missions?
- **Value (0-30)**: How much free compute/resources? Is it Claude/GPT-4 class?
- **Accessibility (0-20)**: Is Togo/West Africa eligible? How much effort to claim?
- **Urgency (0-10)**: Deadline? Limited spots? First-come?

**Total = Relevance + Value + Accessibility + Urgency**

### 5. RECOMMEND — Rank and Present

Rank by score descending. Present top 3.

- Score >= 80: STRONGLY RECOMMEND + full action payload (URL, steps, deadline)
- Score >= 60: RECOMMEND + present for approval
- Score >= 40: SUGGEST (mention in awareness report)
- Score < 40: NOTE (low priority, mention only if asked)

### 6. UPDATE — Refine Profile

After each cycle, refine PROFILE.md:

- Domains that returned quality results: keep
- Domains that returned nothing useful: broaden or replace
- New domains discovered during search: add
- Scoring weights that need adjustment: update

## Scoring Formula

Total = Relevance(40) + Value(30) + Accessibility(20) + Urgency(10)

Maximum possible: 100. Minimum: 0.

### Relevance Scoring Guide

| Signal | Points |
|--------|--------|
| Directly enables KORA (compute, models, grants) | 35-40 |
| Enables DoodleMind or content | 25-34 |
| General dev tool, useful but not critical | 15-24 |
| Tangential to current missions | 5-14 |
| Not relevant | 0-4 |

### Value Scoring Guide

| Signal | Points |
|--------|--------|
| Free Claude/GPT-4 access > $100 value | 25-30 |
| Free credits $50-100 | 18-24 |
| Free credits < $50 or cheap compute | 10-17 |
| Discount only, not free | 5-9 |
| Requires payment | 0-4 |

### Accessibility Scoring Guide

| Signal | Points |
|--------|--------|
| Togo/West Africa explicitly eligible, simple signup | 16-20 |
| Africa eligible, some paperwork | 10-15 |
| Global but competitive, good odds | 5-9 |
| US/Europe only | 0-4 |

### Urgency Scoring Guide

| Signal | Points |
|--------|--------|
| Deadline < 7 days or limited spots | 8-10 |
| Deadline < 30 days | 5-7 |
| Deadline > 30 days | 2-4 |
| No deadline / evergreen | 0-1 |

## Anti-patterns

- Watching without evaluating (raw data is noise, not signal)
- Recommending without verifying eligibility
- Proposing actions without founder approval (Rule #6 — never commit externally without approval)
- Watch domains too specific too early (start broad, refine)
- Ignoring accessibility constraints (US-only offers waste attention)

## Integration

OOOS is loaded:

1. During BOOT (after awareness report, before concept loading) — via SYSTEM_PROMPT.md step 11.5
2. Via intent classification: when user mentions "watch", "opportunity", "credit", "grant", "deal"

OOOS writes to:

- State/WATCH_REGISTRY.md — updates watch results
- Concepts/PROFILE.md — refines Watch Domains and Scoring Preferences
- Concepts/TIMELINE.md — logs major opportunity finds

