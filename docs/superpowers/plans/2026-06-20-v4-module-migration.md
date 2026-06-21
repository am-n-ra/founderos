# V4 Module Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate all 27 FounderOS files from V3 to V4 — update version headers, fix broken references, standardize footers. Zero functional changes.

**Architecture:** Each file needs 1-3 edits: header (V3→V4), footer (standardize), broken reference (KERNEL/FOUNDEROS_PROTOCOL→SYSTEM_PROMPT). Work is batchable by change pattern. 17 standard modules follow the exact same pattern. 5 special cases have unique content fixes. 6 unlabeled files need headers added.

**Files modified:** 27 files in FounderOS/ root + concepts/

---

### Task 1: Standard V3 Modules — Headers + Footers (17 files)

**Pattern for each file:**
1. Header: `# FounderOS V3 — [NAME]` → `# FounderOS V4 — [NAME]`
2. Footer section: Replace existing footer with standard V4 footer (or add one if none exists)

**Standard footer template:**
```
## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
```

- [ ] **Step 1: MOS.md** — Read, edit header and footer

Read file, then:
Edit: `# FounderOS V3 — MOS (Mission Orchestrator)` → `# FounderOS V4 — MOS (Mission Orchestrator)`
Read existing footer (if any), replace with standard V4 footer.

- [ ] **Step 2: DAOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — DAOS (Daily Autonomous Operating System)` → `# FounderOS V4 — DAOS (Daily Autonomous Operating System)`

- [ ] **Step 3: CEOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — CEOS (Content Engineering OS)` → `# FounderOS V4 — CEOS (Content Engineering OS)`

- [ ] **Step 4: VEAOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — VEAOS (Strategic Vision Engine)` → `# FounderOS V4 — VEAOS (Strategic Vision Engine)`

- [ ] **Step 5: ASTRA.md** — Read, edit header and footer

Edit: `# FounderOS V3 — ASTRA (Astro-Reflective Assistant)` → `# FounderOS V4 — ASTRA (Astro-Reflective Assistant)`

- [ ] **Step 6: KMOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — KMOS (Knowledge Management OS)` → `# FounderOS V4 — KMOS (Knowledge Management OS)`

- [ ] **Step 7: LEOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — LEOS (Learning Engineering OS)` → `# FounderOS V4 — LEOS (Learning Engineering OS)`

- [ ] **Step 8: RIOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — RIOS (Research Intelligence OS)` → `# FounderOS V4 — RIOS (Research Intelligence OS)`

- [ ] **Step 9: FAOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — FAOS (Fundraising & Alliance OS)` → `# FounderOS V4 — FAOS (Fundraising & Alliance OS)`

- [ ] **Step 10: SOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — SOS (Self Operating System)` → `# FounderOS V4 — SOS (Self Operating System)`

- [ ] **Step 11: AOS.md** — Read, edit header and footer

Edit: `# FounderOS V3 — AOS (Architecture Operating System)` → `# FounderOS V4 — AOS (Architecture Operating System)`

- [ ] **Step 12: DECISION_ENGINE.md** — Read, edit header and footer

Edit: `# FounderOS V3 — DECISION_ENGINE` → `# FounderOS V4 — DECISION_ENGINE`

- [ ] **Step 13: PATTERN_ENGINE.md** — Read, edit header and footer

Edit: `# FounderOS V3 — PATTERN_ENGINE` → `# FounderOS V4 — PATTERN_ENGINE`

- [ ] **Step 14: PLAYBOOK_ENGINE.md** — Read, edit header and footer

Edit: `# FounderOS V3 — PLAYBOOK_ENGINE` → `# FounderOS V4 — PLAYBOOK_ENGINE`

- [ ] **Step 15: KNOWLEDGE_EVOLUTION_ENGINE.md** — Read, edit header and footer

Edit: `# FounderOS V3 — KNOWLEDGE_EVOLUTION_ENGINE` → `# FounderOS V4 — KNOWLEDGE_EVOLUTION_ENGINE`

- [ ] **Step 16: CONTINUOUS_IMPROVEMENT.md** — Read, edit header and footer

Edit: `# FounderOS V3 — CONTINUOUS_IMPROVEMENT` → `# FounderOS V4 — CONTINUOUS_IMPROVEMENT`

- [ ] **Step 17: AI_VIDEO_MASTER_DOMAIN.md** — Read, edit header and footer

Edit: `# FounderOS V3 — AI_VIDEO_MASTER_DOMAIN` → `# FounderOS V4 — AI_VIDEO_MASTER_DOMAIN`

- [ ] **Step 18: Commit**

```bash
git add FounderOS/{MOS,DAOS,CEOS,VEAOS,ASTRA,KMOS,LEOS,RIOS,FAOS,SOS,AOS,DECISION_ENGINE,PATTERN_ENGINE,PLAYBOOK_ENGINE,KNOWLEDGE_EVOLUTION_ENGINE,CONTINUOUS_IMPROVEMENT,AI_VIDEO_MASTER_DOMAIN}.md
git commit -m "refactor: migrate 17 standard V3 modules to V4 headers and footers"
```

---

### Task 2: Special Cases — Content Fixes (5 files)

These files need specific reference fixes beyond header/footer.

- [ ] **Step 1: GENESIS.md** — Fix 5 broken references

1. Edit header: `# FounderOS V3 — GENESIS` → `# FounderOS V4 — GENESIS`
2. Step 3 header: `### Step 3: Execute KERNEL Boot` → `### Step 3: Execute Boot Sequence`
3. Step 3 body: `1. Load Protocols/TEMPORAL_AWARENESS.md` → remove this line. `2. Run WF-007 freshness check` → `1. Run WF-007 freshness check`. `3. Determine session mode` → `2. Determine session mode`. `4. Load Protocols/FOUNDEROS_PROTOCOL.md` → remove. `5. Build world model` → `3. Build world model`
4. Step 6: `- [ ] Protocols/FOUNDEROS_PROTOCOL.md loads without errors` → `- [ ] SYSTEM_PROMPT.md loads without errors`
5. Footer dependencies: `GENESIS.md, FOUNDEROS_PROTOCOL.md` → `INSTALL.md, SYSTEM_PROMPT.md`

- [ ] **Step 2: INSTALL.md** — Fix 3 broken references

1. Edit header: `# FounderOS V3 — INSTALL` → `# FounderOS V4 — INSTALL`
2. Section 3 body: `Protocols/FOUNDEROS_PROTOCOL.md is the boot sequence.` → `SYSTEM_PROMPT.md is the boot sequence.`
3. Step 5.2: `Execute KERNEL boot` → `Execute Boot Sequence from SYSTEM_PROMPT.md`
4. Footer: `GENESIS.md, FOUNDEROS_PROTOCOL.md` → `GENESIS.md, SYSTEM_PROMPT.md`

- [ ] **Step 3: concepts/SYSTEM.md** — Fix 3 broken references

Read the file around lines 20-30 and 70-76.

**Fix 1 (line 24):** Table row
Edit:
`| Protocols/FOUNDEROS_PROTOCOL.md | execution protocol for any LLM |`
→
`| SYSTEM_PROMPT.md | master entry point — boot sequence, intent classification, PRG |`

**Fix 2 (line 25):** Also update TEMPORAL_AWARENESS (same situation — archived)
Edit:
`| Protocols/TEMPORAL_AWARENESS.md | time as a first-class dimension |`
→
`| RUNTIME.md | operational reference — temporal awareness, principles, quality |`

**Fix 3 (lines 71-76):** Replace `### FOUNDEROS_PROTOCOL.md` section
Edit:
```
### FOUNDEROS_PROTOCOL.md

- The protocol may be updated as FounderHQ evolves
- Protocol updates must not violate the invariants in FOUNDERHQ_MANIFEST.md
- If a protocol update contradicts an invariant, the invariant wins
```
→
```
### SYSTEM_PROMPT.md

- The system prompt is the master entry point for all sessions
- It loads all modules, executes the boot sequence, and runs the Pre-Response Gate
- Updates must not violate the invariants in FOUNDERHQ_MANIFEST.md
- If an update contradicts an invariant, the invariant wins
```

- [ ] **Step 4: concepts/WORKFLOW.md** — Fix WF-007 trigger

Read the file around line 328. Edit:
`**TRIGGER:** Every session start, after loading FOUNDEROS_PROTOCOL Step 1-2` → `**TRIGGER:** Every session start, after Boot Sequence (SYSTEM_PROMPT.md)`

- [ ] **Step 5: README.md** — Fix title

Edit: `# FounderOS v1.0` → `# FounderOS V4`

- [ ] **Step 6: Commit**

```bash
git add FounderOS/GENESIS.md FounderOS/INSTALL.md FounderOS/concepts/SYSTEM.md FounderOS/concepts/WORKFLOW.md FounderOS/README.md
git commit -m "refactor: migrate GENESIS, INSTALL, SYSTEM, WORKFLOW, README — fix broken V3 references"
```

---

### Task 3: Unlabeled Files — Add V4 Headers (6 files)

These files have no V3/V4 version marker in their first line. Add V4 headers and standardize footers where applicable.

- [ ] **Step 1: CONCEPT_AUDIT.md** — Verify only (clean, no changes)

Read line 222. Reference: "Enforced via FOUNDEROS_PROTOCOL.md boot sequence" — past tense, describing a historical fix. No change needed. Confirm and move on.

- [ ] **Step 2: CONCEPT_REGISTRY.md** — Fix reference at line 215

Read line 215. Current content: `- The protocol (Protocols/FOUNDEROS_PROTOCOL.md)`. This lists SYSTEM_PROTOCOL as an active document in the "what system holds" list. Update:
Edit: `- The protocol (Protocols/FOUNDEROS_PROTOCOL.md)` → `- The system prompt (SYSTEM_PROMPT.md)`

- [ ] **Step 3: FOUNDERHQ_MANIFEST.md** — Fix reference at line 228

Read line 228. Current content: `- DECISION_GATES, TEMPORAL_AWARENESS, FOUNDEROS_PROTOCOL, SOURCE_OF_TRUTH` — Niveau B list of functioning components. TEMPORAL_AWARENESS is also archived. Update both:
Edit: `DECISION_GATES, TEMPORAL_AWARENESS, FOUNDEROS_PROTOCOL, SOURCE_OF_TRUTH` → `DECISION_GATES, RUNTIME.md, SYSTEM_PROMPT.md, SOURCE_OF_TRUTH`

- [ ] **Step 4: CONCEPT_BOUNDARIES.md** — Clean, no fixes needed

Just read to confirm. No changes required per spec.

- [ ] **Step 5: FOUNDERHQ_DESCRIPTION.md** — Clean, no fixes needed

Just read to confirm. No changes required per spec.

- [ ] **Step 6: Commit**

```bash
git add FounderOS/CONCEPT_AUDIT.md FounderOS/CONCEPT_REGISTRY.md FounderOS/FOUNDERHQ_MANIFEST.md FounderOS/CONCEPT_BOUNDARIES.md FounderOS/FOUNDERHQ_DESCRIPTION.md
git commit -m "docs: audit unlabeled files — CONCEPT_AUDIT, CONCEPT_REGISTRY, MANIFEST, BOUNDARIES, DESCRIPTION"
```

---

### Task 4: Verification

- [ ] **Step 1: Check no V3 remains in first lines**

Run:
```bash
Select-String -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\*.md" -Pattern "^# FounderOS V3" -SimpleMatch
```
Expected: No matches (empty output).

- [ ] **Step 2: Check no active KERNEL/FOUNDEROS_PROTOCOL refs**

```bash
Select-String -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\GENESIS.md" -Pattern "KERNEL|FOUNDEROS_PROTOCOL" -SimpleMatch
Select-String -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\INSTALL.md" -Pattern "KERNEL|FOUNDEROS_PROTOCOL" -SimpleMatch
```
Expected: All matches are removed (no output, or only contextual/historical mentions).

- [ ] **Step 3: Verify module footers**

```bash
Select-String -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\MOS.md" -Pattern "OS Version.*V4" -SimpleMatch
```
Expected: True for all modules.

- [ ] **Step 4: Verify V3 in archives only**

```bash
$rootV3 = Select-String -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\*.md" -Pattern "V3" -SimpleMatch; $rootV3
```
Expected: Only matches in `ARCHIVE/` and historical concept files (MEMORY.md, TIMELINE.md).

- [ ] **Step 5: Commit verification**

Run: `git status` — confirm all modified files are staged. If not, stage remaining files.

```bash
git add -A
git commit -m "verification: V4 module migration complete — all headers, refs, footers verified"
```
