# FounderOS V4 Consolidation Design

## Objective

Eliminate architectural debt from V3 where 4 overlapping orchestration files (SYSTEM_PROMPT.md, FOUNDEROS_PROTOCOL.md, KERNEL.md, TEMPORAL_AWARENESS.md) coexist with duplicating content. Replace with a single master entry point that also adds automatic intent classification for loading specialist modules.

## Scope

**Touches:** Orchestration layer only (4 files to consolidate, 1 new intent classification system).

**Does NOT touch:** Specialist modules (CEOS, VEAOS, MOS, DAOS, ASTRA, KMOS, LEOS, RIOS, FAOS, SOS, AOS, DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE, KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT, AI_VIDEO_MASTER_DOMAIN, GENESIS, INSTALL). Concepts, Protocols (except FOUNDEROS_PROTOCOL + TEMPORAL_AWARENESS), Frameworks, State files remain untouched.

## Architecture Before (V3 — 4 overlapping files)

```
SYSTEM_PROMPT.md      ← Entry point: identity, invariants, architecture overview
KERNEL.md             ← Boot: session init, mode, permissions, integrity check
FOUNDEROS_PROTOCOL.md ← Protocol: loading procedure, execution modes, operational principles
TEMPORAL_AWARENESS.md ← Time: timezone, DST, freshness checks
```

**Problems:**
- SYSTEM_PROMPT.md says "read FOUNDEROS_PROTOCOL.md" but also has its own boot sequence
- KERNEL.md overlaps with FOUNDEROS_PROTOCOL.md Step 1-9
- TEMPORAL_AWARENESS.md is 1 page that could be 3 lines in SYSTEM_PROMPT.md
- LLM must read 4 files to understand "what am I?" — cognitive load, risk of contradiction

## Architecture After (V4 — 1 master + 1 runtime)

```
SYSTEM_PROMPT.md      ← Single entry point. Identity, boot, invariants, intent classification,
                         permissions, temporal awareness, error handling, execution modes
RUNTIME.md            ← Daily operating loop (separate: loaded after boot, not part of identity)
SOURCE_OF_TRUTH.md    ← Data map (unchanged)
DECISION_GATES.md     ← Gate system (unchanged)
```

## File Actions

| File | Action |
|------|--------|
| `FounderOS/SYSTEM_PROMPT.md` | Rewrite — absorb FOUNDEROS_PROTOCOL.md + KERNEL.md + TEMPORAL_AWARENESS.md + add intent classification |
| `FounderOS/RUNTIME.md` | Keep as-is (no changes) |
| `FounderOS/KERNEL.md` | Archive — content absorbed into SYSTEM_PROMPT.md boot section |
| `FounderOS/Protocols/FOUNDEROS_PROTOCOL.md` | Archive — content absorbed into SYSTEM_PROMPT.md |
| `FounderOS/Protocols/TEMPORAL_AWARENESS.md` | Archive — content absorbed into SYSTEM_PROMPT.md temporal section |

## SYSTEM_PROMPT.md New Structure

```
# FounderOS V4 — System Prompt

## Identity
- Who you are (absorbs FOUNDEROS_PROTOCOL.md "What You Are")

## Architecture
- Three layers (OS / Modules / Engines)

## Primary Directive
- Mission advancement, not Q&A

## Invariants
- File-first, Regle 0, continuity, state over conversation

## Boot Sequence (absorbs KERNEL.md + FOUNDEROS_PROTOCOL.md Loading Procedure)
- Step 0: Load SOURCE_OF_TRUTH.md + DECISION_GATES.md
- Step 1: Temporal awareness (absorbs TEMPORAL_AWARENESS.md — 3 lines)
- Step 2: Run WF-007 freshness check
- Step 3: Load CURRENT_STATE.md, MISSION.md, MEMORY.md
- Step 4: Load KNOWLEDGE.md, TIMELINE.md, PROJECT.md, WORKFLOW.md, ASSET.md
- Step 5: Build world model
- Step 6: Report awareness

## Intent Classification (NEW — solves automatic module loading)
- [Table: For each user message pattern, classify intent and load module]
- [Format: "If user says... → Classify as → Load module + execute protocol"]

## Execution Modes
- Standard, Quick, Reconstruction, Mid-Session Reboot (absorbs protocol versions)

## Permissions & Escalation
- Autonomous actions vs. escalation-required actions

## Interaction Style
- Direct, concise, no "how can I help"

## Quality Standards
- Accurate, Timely, Aligned, Concrete

## Error Handling
- Missing concept, contradiction, stale data
```

## Intent Classification Design

This is the key new feature. The SYSTEM_PROMPT.md will include a classification table that the LLM MUST apply to EVERY user message before responding.

### Classification Table

```
## Intent Classification

Before responding to ANY user message, classify the intent using this table:

| User message pattern (semantic match) | Classify as | Action |
|---|---|---|---|
| Strategy, vision, long-term direction, "what path should I take" | STRATEGIC | Load VEAOS.md, execute strategic framework |
| Daily execution, "what should I do today", task planning | EXECUTION | Load DAOS.md, generate action modules |
| Content creation, video, script, "make a post" | CONTENT | Load CEOS.md + AI_VIDEO_MASTER_DOMAIN.md |
| Reflection, "I'm stuck", "what do you think", uncertainty | REFLECTION | Load ASTRA.md, execute reflection framework |
| Research, "find information on X", investigate | RESEARCH | Load RIOS.md, execute research protocol |
| Learning a skill, "I need to learn X", knowledge gap | LEARNING | Load LEOS.md, generate learning roadmap |
| Fundraising, revenue, partnerships, "we need money" | FUNDRAISING | Load FAOS.md, execute fundraising analysis |
| Health, energy, burnout, "I'm tired", wellbeing | SELF | Load SOS.md, execute self-check protocol |
| Architecture, organization, "how should I structure this" | ARCHITECTURE | Load AOS.md, execute architecture method |
| Decision, "what should I choose", tradeoffs | DECISION | Load DECISION_ENGINE.md, run PROACT framework |
| Pattern, "I notice this keeps happening", recurring | PATTERN | Load PATTERN_ENGINE.md, detect and store pattern |
| Playbook, "I want to document a process" | PLAYBOOK | Load PLAYBOOK_ENGINE.md, create playbook |
| Simple update, status, informational (no module matches) | DIRECT | Execute directly, no module needed |
```

### Classification Rules

1. Classify BEFORE responding. Never reply before intent is classified.
2. If multiple intents match, pick the highest-weighted (first match in table).
3. If uncertain, pick the most mission-critical interpretation.
4. After classification, load the module file and follow its protocol.
5. The user should NEVER have to name a module. Classification is automatic.

## Archive Procedure

Archived files are moved to `FounderOS/ARCHIVE/V4/` with a single-line reference in SYSTEM_PROMPT.md footer noting their location for historical reference. They are NOT deleted — just not loaded during normal boot.

## What Does NOT Change

- All 18 specialist module files remain in `FounderOS/` root
- All `concepts/` files
- All `State/` files
- All `Frameworks/` files
- `Protocols/SOURCE_OF_TRUTH.md` (updated only to remove archived files from truth map)
- `Protocols/DECISION_GATES.md`
- `Runtime/`
- `GENESIS.md`, `INSTALL.md`

## Verification Criteria

After consolidation:

1. SYSTEM_PROMPT.md contains all content from KERNEL.md + FOUNDEROS_PROTOCOL.md + TEMPORAL_AWARENESS.md
2. No duplicate "identity" or "boot sequence" across files
3. Intent classification table has entries for ALL specialist modules
4. All 18 specialist modules still loadable and unchanged
5. KERNEL.md, FOUNDEROS_PROTOCOL.md, TEMPORAL_AWARENESS.md are in ARCHIVE/V4/
6. SOURCE_OF_TRUTH.md updated to point to SYSTEM_PROMPT.md for absorbed truths
7. No content loss: every functional section from archived files exists in SYSTEM_PROMPT.md

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | V3 files as reference, specialist modules unchanged |
