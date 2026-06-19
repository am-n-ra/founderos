# Archive v1 — Legacy FounderOS System

**Date archived:** 2026-06-18

**Reason:** FounderOS v1 was replaced by a concept-based system (9 concepts) with DECISION_GATES enforcement. These files are no longer active but are preserved for reference.

## Contents

| Directory | Files | Origin |
|-----------|-------|--------|
| legacy_frameworks/ | 44 | FounderOS/SYSTEM/ — CAOS, CEOS, PSOS, FAOS, and 40 other spec files |
| legacy_state/ | 12 | FounderOS/STATE/ — BOOT_LOG, CURRENT_STATE, FOUNDER_PROFILE, etc. |
| legacy_memory/ | 3 | FounderOS/MEMORY/ — ACTIVE_DECISIONS, CURRENT_FOCUS, MEMORY_INDEX |
| legacy_knowledge/ | 31 | Knowledge/ — AI_VIDEO_PRODUCTION_WORKFLOW, CONTENT_PILLARS, etc. |
| legacy_specs/ | 6 | FounderOS/ root — V1_MASTER_SPEC, AGENT_POLICY, BOOTSTRAP_PACKAGE, etc. |
| legacy_automations/ | 4 (empty) | FounderOS/AUTOMATIONS/ — empty shell directories |

## Migration Status

### Migrated into concept system (16 Knowledge files)
Patterns from these files were extracted and integrated into the 9 concepts:
- AI_VIDEO_PRODUCTION_WORKFLOW → WORKFLOW (WF-004)
- ASSET_REGISTRY → ASSET (reuse rule, subtypes)
- AUTOMATION_ENGINE → WORKFLOW (WF-005)
- BOOT_MANAGER → SYSTEM (boot sequence)
- BRAND_STRATEGY → ASSET (A-008 brand identity)
- CONNECTOR_FRAMEWORK → SYSTEM (runtime architecture)
- CONTENT_PILLARS → PLAYBOOK (PB-001)
- CONTINUOUS_IMPROVEMENT → MEMORY + KNOWLEDGE
- EVENT_BUS → WORKFLOW (WF-006)
- GOVERNANCE_PROTOCOL → DECISION_GATES + SYSTEM (authority levels)
- MISSION_CONTROL → MISSION (hierarchy, drift detection)
- RUNTIME_OPERATING_LAYER → SYSTEM (runtime architecture)
- SERIES_BIBLE → ASSET (template)
- SOCIAL_MEDIA_STRATEGY → PLAYBOOK (PB-002)
- STATE_SYNCHRONIZATION → MEMORY (state sync)
- STORY_BIBLE → ASSET (template, inheritance chain)

### Already covered (5 files — no migration needed)
- DESIGN_PHILOSOPHY, KNOWLEDGE_EVOLUTION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE, VALUES

### No value to migrate (5 files — one-time artifacts)
- EXECUTION_ROADMAP, LEAN_CANVAS, MISSION_2026, VISION_2028, WEBSITE_ARCHITECTURE

### Not migrated (44 frameworks + 12 state + 3 memory + 6 specs)
These are reference documents. Their core principles (CAOS allocation, CEOS content, PSOS strategy) have been extracted into DECISION_GATES rules. The raw files remain for historical reference.

## Access
- Read-only. Do not modify.
- If a pattern is found here that does not exist in the active concepts, extract it.
- If all patterns have been extracted, this directory may be compressed.

## Active System
The active FounderHQ system is now at:
- `FounderOS/concepts/` — 9 concept files
- `FounderOS/DECISION_GATES.md` — enforcement gates
- `FounderOS/CURRENT_SESSION.md` — operational state
- `FounderOS/FOUNDEROS_PROTOCOL.md` — execution protocol
- `FounderOS/FOUNDERHQ_MANIFEST.md` — invariants
