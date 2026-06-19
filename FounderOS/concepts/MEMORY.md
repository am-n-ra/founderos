# MEMORY

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 3.

## Role

Store temporary operational context.

Memory changes frequently.

If something has been true for more than 30 days, it belongs in KNOWLEDGE.

---

## Current Priorities

1. Monitor Variation #2 analytics — wait for >100 views before SN-003 decision
2. Engage any WhatsApp inquiries from Variation #2
3. Update State/CURRENT_STATE.md after each action

---

## Current Operating Mode

SURVIVAL — generate revenue before cash runs out.

---

## Recent Decisions

- 2026-06-18: FounderOS architecture audited. Result: 42 specs replaced by concept-based system.
- 2026-06-18: Four foundation documents written (MANIFEST, CONCEPT_REGISTRY, PROTOCOL, TEMPORAL_AWARENESS).
- 2026-06-18: CONCEPT_BOUNDARIES.md written.
- 2026-06-18: Global deep fix — 107 legacy files archived, DECISION_GATES + CURRENT_SESSION created, patterns migrated, TEMPORAL_AWARENESS operationalized.
- 2026-06-18: Variation #2 posted by founder with "PEST" giveaway + price anchoring (8,500 vs 5,900).
- 2026-06-17: Video 1 posted on TikTok @stopnuisibles228.
- 2026-06-17: Zoclo Livraison mission archived.

---

## Open Questions

None — all current decisions made.

---

## Active Concerns

- 5 TikTok followers — zero social proof, low conversion probability without incentive.
- Video 1 analytics: 380 views, 98.8% For You, 11.69s avg, 12.2% full watch, 13 likes, 0 comments, 2 shares, 6 saves, 4 new followers, drop at 0:03
- Facebook: 227 views, 4s avg, 0 interactions, 0 link clicks
- Cash position: see State/CURRENT_STATE.md (single source of truth)

---

## Blockers

- None — waiting on Variation #2 analytics to determine next action.

---

## Scope Notice

MEMORY stores cross-session context, durable reflections, and long-term concerns.

State/CURRENT_STATE.md stores what is happening RIGHT NOW (cash, bottleneck, priority, objective).

If it is a current operational fact → State/CURRENT_STATE.md.
If it is a pattern observed over multiple sessions → MEMORY.md.
If it is a validated truth → KNOWLEDGE.md.

Do not duplicate. If it belongs in CURRENT_STATE, put it there. MEMORY is for what persists across sessions, not what is transient.

---

## State Synchronization

State is stored in multiple concept files. To prevent divergence:

1. **State categories:** Mission State, Project State, Knowledge State, Learning State, Asset State
2. **Sync cycle:** Detect Changes → Validate → Update State → Notify Dependencies → Log Changes
3. **Conflict rule:** If two states disagree (e.g., MEMORY says cash=1,118 but CURRENT_STATE says cash=1,500), generate STATE_CONFLICT_REPORT.md
4. **State snapshot:** State/CURRENT_STATE.md is the daily snapshot. It is the single source of truth for session-level state.

---

## Review Cadence

| Cadence | Focus | Questions |
|---------|-------|-----------|
| Daily | Tasks completed / blocked / lessons / next priorities | What worked? What failed? What surprised us? |
| Weekly | Progress / patterns / workflow issues / opportunities | What repeated? What should change? |
| Monthly | Strategic alignment / system performance / knowledge growth | Are the right projects active? |
| Quarterly | Major milestones / direction correction | Are we still on the right mission? |

Metrics to track: Lessons Count, Patterns Count, Playbooks Count, Workflow Success Rate, Execution Speed, Goal Completion Rate

---

## Footer

Last updated: 2026-06-18 (added: scope notice, state synchronization, review cadence)

Memory should be reviewed and pruned at the start of each session.

Stale entries (older than 14 days without update) should be flagged.

If an entry becomes a validated truth, move it to KNOWLEDGE.
