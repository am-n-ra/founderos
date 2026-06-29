# V4 Module Migration — Design Spec

**Date:** 2026-06-20
**Status:** Approved
**Owner:** System

---

## Goal

Migrate all remaining FounderOS V3 modules and unlabeled root files to V4. No functional changes — only version headers, broken reference fixes, and footer standardization.

---

## Scope (27 files)

### 19 V3 modules → V4 header + template

| File | Lines | Notes |
|------|-------|-------|
| MOS.md | 51 | Mission Orchestrator |
| DAOS.md | 50 | Daily Autonomous OS |
| CEOS.md | 34 | Content Engineering OS |
| VEAOS.md | 41 | Strategic Vision Engine |
| ASTRA.md | 44 | Astro-Reflective Assistant |
| KMOS.md | 44 | Knowledge Management OS |
| LEOS.md | 39 | Learning Engineering OS |
| RIOS.md | 43 | Research Intelligence OS |
| FAOS.md | 51 | Fundraising & Alliance OS |
| SOS.md | 42 | Self Operating System |
| AOS.md | 57 | Architecture OS |
| DECISION_ENGINE.md | 54 | Structured decisions |
| PATTERN_ENGINE.md | 52 | Pattern detection |
| PLAYBOOK_ENGINE.md | 51 | Playbook creation |
| KNOWLEDGE_EVOLUTION_ENGINE.md | 47 | Knowledge decay |
| CONTINUOUS_IMPROVEMENT.md | 58 | Meta-improvement |
| AI_VIDEO_MASTER_DOMAIN.md | 91 | Video production |
| GENESIS.md | 97 | First-time setup |
| INSTALL.md | 89 | Deployment guide |

### 6 unlabeled files → V4 tag + reference audit

| File | Lines | Fix needed |
|------|-------|------------|
| CONCEPT_AUDIT.md | 234 | 1 ref FOUNDEROS_PROTOCOL (historical context — keep if past tense, fix if active instruction) |
| CONCEPT_REGISTRY.md | 306 | 1 ref FOUNDEROS_PROTOCOL |
| FOUNDERHQ_MANIFEST.md | 253 | 1 ref FOUNDEROS_PROTOCOL |
| CONCEPT_BOUNDARIES.md | 263 | Clean |
| FOUNDERHQ_DESCRIPTION.md | 516 | Clean |
| README.md | 37 | Clean ("v1.0" in title → "V4") |

### 2 concept files → reference audit only

| File | Issue | Action |
|------|-------|--------|
| concepts/SYSTEM.md | Lists FOUNDEROS_PROTOCOL.md as active entry in concept table + dedicated section | Update to reference SYSTEM_PROMPT.md instead |
| concepts/WORKFLOW.md | May reference FOUNDEROS_PROTOCOL steps in WF-007 | Verify and update if needed |

### No-touch list

- `ARCHIVE/` (V1 and V4 archives)
- `Protocols/` (SOURCE_OF_TRUTH, DECISION_GATES, RELATIONSHIP_MODEL — references are contextual/diagrammatic)
- `Runtime/` (IDE integrations)
- `concepts/MEMORY.md`, `TIMELINE.md` (historical refs are correct — they describe past events)
- `State/` (state files, not modules)
- `Frameworks/`, `KnowledgeAssets/` (out of scope)

---

## Template

Every module receives this structure:

```markdown
# FounderOS V4 — [NAME] ([Description])

## Purpose
[When to load this module, what it does — 2-3 sentences]

## Core Protocol
[Existing content preserved verbatim unless it contains broken references]

## Footer
| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
```

### Rules
1. **Header:** `V3` → `V4` strictly
2. **"Concept" section** (when present, e.g., MOS.md): merged into Purpose or removed
3. **Broken refs:** `KERNEL.md`, `FOUNDEROS_PROTOCOL.md` replaced by `SYSTEM_PROMPT.md` or removed
4. **Content:** textually preserved except for broken references
5. **Footer:** standardized to the template above (currently, each module has its own footer format or none)

---

## Special Cases

### GENESIS.md
Most impacted. Fixes:
- Step 3: "Execute KERNEL Boot" → "Execute Boot Sequence (SYSTEM_PROMPT.md)"
- Step 4: Remove "Load Protocols/FOUNDEROS_PROTOCOL.md" (protocol absorbed into SYSTEM_PROMPT.md)
- Verification checklist: remove FOUNDEROS_PROTOCOL check
- Footer dependencies: KERNEL/FOUNDEROS_PROTOCOL → SYSTEM_PROMPT.md

### INSTALL.md
- Step 5.2: "Execute KERNEL boot" → "Execute Boot Sequence from SYSTEM_PROMPT.md"
- Section 3: "Protocols/FOUNDEROS_PROTOCOL.md is the boot sequence" → "SYSTEM_PROMPT.md is the boot sequence"
- Footer dependencies → SYSTEM_PROMPT.md

### concepts/SYSTEM.md
Replace the FOUNDEROS_PROTOCOL row in the concept table and the dedicated section with SYSTEM_PROMPT.md references.

### concepts/WORKFLOW.md
WF-007 line 328: "TRIGGER: Every session start, after loading FOUNDEROS_PROTOCOL Step 1-2" → redirect to SYSTEM_PROMPT.md boot sequence. Content: "TRIGGER: Every session start, after Boot Sequence (SYSTEM_PROMPT.md)".

### README.md
Line 1: "# FounderOS v1.0" → "# FounderOS V4"

### CONCEPT_AUDIT.md
Line 222 references FOUNDEROS_PROTOCOL in past tense ("added to WORKFLOW.md. Enforced via...") — describes historical fix. No change needed. Preserve as-is.

---

## Verification

After migration:
1. No file in `FounderOS/` (root) has "V3" in its first line
2. No file in `FounderOS/` (root) references `KERNEL.md` or `FOUNDEROS_PROTOCOL.md` as active instructions
3. All module footers follow the V4 template
4. All unlabeled files have V4 headers
5. `grep -r "V3" FounderOS/ --include="*.md"` returns only archive/concept/historical files
6. `grep -r "FOUNDEROS_PROTOCOL" FounderOS/ --include="*.md"` returns only archive/historical/contextual references

---

## Success Criteria

- SYSTEM_PROMPT.md correctly lists all V4 modules (already correct — it says "12 specialist modules" without naming each)
- An agent reading any module sees "FounderOS V4" in the first line
- An agent following GENESIS.md or INSTALL.md will not attempt to load KERNEL.md or FOUNDEROS_PROTOCOL.md
- All module footers are consistent
- Zero functional changes to module protocols — content preserved verbatim

---

## Out of Scope

- Adding new capabilities to any module
- Rewriting module content (DIOS-style expansion)
- Architectural changes to how modules are loaded
- Migration of `Runtime/`, `Protocols/`, `State/`, `Frameworks/`, `KnowledgeAssets/`
- Migration of archive files
