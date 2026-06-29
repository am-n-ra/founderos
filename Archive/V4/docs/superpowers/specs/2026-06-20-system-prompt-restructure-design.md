# SYSTEM_PROMPT.md Restructure Design

> **Problem:** FounderHQ's SYSTEM_PROMPT.md is 385 lines. Critical rules (Get-Date, PRG, mission alignment) are buried in prose. The agent does not execute them consistently because they are too far from the decision points. Previous fixes added more prose — which made the problem worse.

**Goal:** Reduce SYSTEM_PROMPT.md to ~100 lines. Critical execution rules must be in the first 30 lines. Move detailed reference material to RUNTIME.md.

**Architecture:**
- SYSTEM_PROMPT.md = boot + critical rules + module map (what to load when)
- RUNTIME.md = operational reference (temporal awareness detail, quality standards, error handling, principles)
- No new files. No runtime scripts. Pure restructure.

---

## Scope

### SYSTEM_PROMPT.md — Always Loaded (~90-100 lines)

| Section | Lines | Content |
|---|---|---|
| Identity + Primary Directive | 5 | Who FounderOS is, what it does |
| **Critical Execution Rules** | **15** | Get-Date before every response, PRG, Mission Alignment, Cash Awareness |
| Architecture Overview | 3 | 3 layers, modules map |
| Boot Sequence | 8 | Compressed — only what's needed for first load |
| Intent Classification + PRG | 20 | Table + gate + rules (inseparable) |
| Execution Modes | 8 | Standard, Quick, Reconstruction, Reboot |
| Permissions & Escalation | 10 | Autonomous vs escalated |
| State Preservation | 3 | Update CURRENT_STATE, TIMELINE, KNOWLEDGE at session end |
| Footer | 3 | Version, dependencies |

### RUNTIME.md — Loaded On Demand (~150 lines, enriched)

| Section | Content |
|---|---|
| Temporal Awareness Detail | Age tables, period awareness, temporal reports, staleness detection |
| Operational Principles | Leverage, Verification, Mission Alignment (expanded) |
| Quality Standards | Accuracy, Timeliness, Alignment, Concreteness |
| Interaction Style | Directives for tone, response style |
| Error Handling | Missing concepts, contradictions, permission violations |
| State Aging Table | Exact thresholds and actions |

### Removed (already covered elsewhere)
- Invariants detail → SOURCE_OF_TRUTH.md
- WF-007 freshness check detail → WORKFLOW.md (already exists)
- Temporal Awareness detail → RUNTIME.md

---

## Key Design Decisions

### 1. Critical Rules First

The first substantive section after Identity is **Critical Execution Rules**. These are:
- **Rule 1:** Get-Date before every response. Output format: `**[datetime Lomé UTC+0]**`.
- **Rule 2:** Execute Pre-Response Gate before every response. 3 steps.
- **Rule 3:** Mission Alignment — does this serve a mission?
- **Rule 4:** Cash Awareness — if < 1,500 FCFA, revenue first.

No other content appears before these rules. No prose, no explanation, no context — just the rules.

### 2. Intent Classification + PRG Merged

Currently separated by 20 lines. The PRG executes immediately after classification and before response — they are one temporal unit. They stay adjacent in the restructured file.

### 3. Temporal Awareness Moved to RUNTIME.md

The current SYSTEM_PROMPT.md has 80 lines of Temporal Awareness (age tables, period awareness, temporal reports, staleness edge cases). This is reference material, not boot material. It moves to RUNTIME.md with a one-line reference: "See RUNTIME.md for temporal awareness reference."

### 4. Execution Modes Compressed

Standard Session goes from 7 verbose steps to:
> 1. Boot → 2. Classify → 3. PRG → 4. Execute → 5. Update → 6. Repeat

Quick Session from 5 lines to 3. Reconstruction session stays. Reboot stays.

---

## File Changes

| File | Change |
|---|---|
| `FounderOS/SYSTEM_PROMPT.md` | Rewrite to ~100 lines |
| `FounderOS/RUNTIME.md` | Enrich with Temporal Awareness, Principles, Quality Standards, Error Handling |
| `FounderOS/Protocols/PRG_TEST.md` | Update tests for new structure |

---

## Success Criteria

1. SYSTEM_PROMPT.md ≤ 120 lines (ideally ~100)
2. Critical rules appear within first 30 lines
3. No content loss — everything moved is preserved in RUNTIME.md
4. Boot sequence still works (Step 1-7 flow intact)
5. PRG still enforceable (Get-Date in response header)
6. PRG_TEST.md tests pass on new structure

---

## Open Questions

None — constraints validated with founder.

---

## Footer

| Field | Value |
|---|---|
| Version | V1 |
| Owner | System |
| Location | `FounderOS/SYSTEM_PROMPT.md` + `FounderOS/RUNTIME.md` |
