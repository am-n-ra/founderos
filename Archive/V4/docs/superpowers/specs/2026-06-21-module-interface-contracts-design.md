# Module Interface Contracts — Design Spec

**Date:** 2026-06-21
**Status:** Approved
**Owner:** System

---

## Goal

Add Interface Contracts (Position, Inputs, Outputs, Relations, Workflow) to all 14 V4 modules that lack them, following DIOS.md's structural pattern but scaled to each module's complexity. No DIOS-style domains or KPIs — just the interface contract + existing content reformatted into Workflow.

---

## Scope (14 modules)

| Module | Lines | Current Structure | Target Sections |
|--------|-------|-------------------|-----------------|
| MOS.md | 51 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| DAOS.md | 50 | Purpose, Daily Outputs, Operating Rhythm, Action Module Format, Integration | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| CEOS.md | 34 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| VEAOS.md | 41 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| ASTRA.md | 44 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| RIOS.md | 43 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| LEOS.md | 39 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| FAOS.md | 51 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| SOS.md | 42 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| AOS.md | 57 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| DIOS.md | 285 | Already has full structure | Skip — already complete |
| DECISION_ENGINE.md | 54 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| PATTERN_ENGINE.md | 52 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| PLAYBOOK_ENGINE.md | 51 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| KNOWLEDGE_EVOLUTION_ENGINE.md | 47 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| CONTINUOUS_IMPROVEMENT.md | 58 | Purpose, Core Protocol | Purpose, Position, Inputs, Outputs, Relations, Workflow |
| AI_VIDEO_MASTER_DOMAIN.md | 91 | Purpose, Core Protocol, Style & Voice, Hook Patterns | Purpose, Position, Inputs, Outputs, Relations, Workflow |

---

## Template

Each module restructured into this template:

```markdown
# FounderOS V4 — [NAME] ([Description])

## Purpose
[2-3 sentences — existing content, preserved]

## Position in FounderHQ
[Where this module sits in the architecture. What triggers it. What it feeds.]

## Inputs
- [Concept/Module X] — [what it provides]
- [Concept/Module Y] — [what it provides]

## Outputs
- [Artifact A] — [produced when, used by whom]
- [Artifact B] — [produced when, used by whom]

## Relations
- **[Module X]** — [how they interact]
- **[Module Y]** — [how they interact]

## Workflow
[Existing Core Protocol content, reformatted as numbered steps. Preserve all existing content verbatim.]

## Footer
...
```

### Content Rules
1. **Existing content preserved verbatim** — move existing text into Workflow section, reformat as steps if not already
2. **Position/Inputs/Outputs/Relations** — new content, 1-3 lines each, specific to the module's actual role
3. **No DIOS-style domains or KPIs** — those are distribution-specific, not needed here
4. **Footer unchanged** — already V4 standard

---

## Verification

After changes:
1. All 14 modules have Position, Inputs, Outputs, Relations, Workflow sections
2. Existing content is preserved in Workflow section
3. No content loss — diff shows additions only, not replacements
4. FACTOR: average module length increases from ~50 to ~80 lines

---

## Success Criteria

- An agent reading any module can answer: what triggers it, what does it receive, what does it produce, what depends on it
- Interface contracts are consistent across all modules
- DIOS.md remains the richest module (285 lines) but all others have at least the contract structure
