# SYSTEM

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 9.

## Role

Store the rules that govern FounderHQ itself.

SYSTEM is the meta-layer. It does not contain operational data, mission definitions, project status, knowledge, or any business content.

**Status:** ⚠️ Needs review — recent runtime changes not yet documented.

**Last Updated:** 2026-06-24

---

## FounderHQ Documents

FounderHQ is defined by these documents, listed in load order:

| Document | Purpose |
|----------|---------|
| FOUNDERHQ_MANIFEST.md | 9 invariants — what cannot be broken |
| CONCEPT_REGISTRY.md | 9 concepts — what must exist |
| CONCEPT_BOUNDARIES.md | frontiers — what each concept answers and does not answer |
| SYSTEM_PROMPT.md | master entry point — boot sequence, intent classification, PRG |
| RUNTIME.md | operational reference — temporal awareness, principles, quality |
| CONCEPT_AUDIT.md | audit record of concept purity |
| RELATIONSHIP_MODEL.md | graph of concept relationships |

---

## Concept Evolution Rules

### Adding a New Concept

1. The concept must serve at least one invariant from FOUNDERHQ_MANIFEST.md
2. The concept must be added to CONCEPT_REGISTRY.md
3. The concept must have boundaries defined in CONCEPT_BOUNDARIES.md
4. The concept must have relationship types defined in RELATIONSHIP_MODEL.md
5. The concept must be implemented as a file in concepts/
6. The audit must pass before the concept is considered active

### Removing a Concept

1. A concept cannot be removed if it is referenced by any other concept
2. A concept may be archived if all references are removed first
3. An archived concept remains in CONCEPT_REGISTRY.md with status "Archived"
4. An archived concept's file moves to Archive/

### Modifying a Concept

1. A concept's boundaries may change, but the change must be documented in CONCEPT_AUDIT.md
2. A concept's implementation may change (file → database → graph)
3. After modification, all relationships to other concepts must be verified for integrity

---

## Document Evolution Rules

### FOUNDERHQ_MANIFEST.md

- Invariants may be added but not removed
- An invariant may be refined (clarified) but not weakened
- Any change to the manifest requires founder approval

### CONCEPT_REGISTRY.md

- A concept may be added, archived, or merged
- A concept may not be deleted — its definition persists in the registry
- If two concepts are merged, the merge must be documented with a migration note

### SYSTEM_PROMPT.md

- The system prompt is the master entry point for all sessions
- It loads all modules, executes the boot sequence, and runs the Pre-Response Gate
- Updates must not violate the invariants in FOUNDERHQ_MANIFEST.md
- If an update contradicts an invariant, the invariant wins

### CONCEPT_BOUNDARIES.md

- Boundaries may be refined as concepts evolve
- Any refinement must be verified against CONCEPT_AUDIT.md

---

## Quality Gates

Every concept implementation must meet these minimum standards:

### Completeness

The concept file must contain:
- Its definition from CONCEPT_REGISTRY.md (via reference or brief summary)
- Its current state (missions, projects, memory, knowledge, timeline, etc.)
- A last-updated date in the footer

### Boundary Purity

The concept must not contain information that belongs to another concept.

If a review detects contamination, the contamination must be moved to the correct concept and the audit must be updated.

### Relationship Integrity

Every relationship to another concept must be bidirectional.

If PROJECT links to MISSION, MISSION must link back to PROJECT.

If a link exists in one direction but not the other, it is flagged as incomplete.

### Freshness

A concept must be reviewed if it has not been updated within:

| Concept | Max Age | Action |
|---------|---------|--------|
| MEMORY | 7 days | Flag as potentially stale |
| PROJECT (Active) | 14 days | Flag as possibly abandoned |
| PROJECT (Paused) | 30 days | Flag for review |
| KNOWLEDGE | 90 days | Flag for revalidation |
| TIMELINE | 30 days | Flag if gap detected |
| MISSION | 90 days | Flag for relevance check |

---

## Governance Rules

### Authority Levels

| Level | Name | Scope |
|-------|------|-------|
| 0 | Observe Only | Monitor, analyze, report, learn. Cannot modify anything. |
| 1 | Recommend | Recommend actions, generate plans, suggest decisions. Cannot execute. |
| 2 | Prepare Actions | Prepare assets, reports, code, content. Requires founder approval before execution. |
| 3 | Execute Low-Risk | Reports, registry updates, state updates, summaries. Must log all actions. |
| 4 | Execute Approved | Previously approved workflows, automations, recurring processes. Auditable. |
| 5 | Strategic Partner | Full operational capability. Still requires approval for: financial, legal, external publishing, hiring. |

Current operating authority: **Level 1-2** (can recommend and prepare, execution requires founder approval)

### Escalation Categories — Always escalate to founder:

- **Financial** — any transaction, pricing change, discount, payment acceptance
- **Legal** — contracts, terms, liability, compliance
- **Security** — data access, account changes, credential management
- **Hiring** — any engagement of people or services
- **Equity** — ownership, shares, revenue share agreements
- **External Communications** — publishing on behalf of founder, public statements
- **Personal Data** — sharing or storing third-party personal information

### Risk Levels

| Level | Type | Action |
|-------|------|--------|
| LOW | Auto-execute | Generate report, update registry, create summary |
| MEDIUM | Prepare + request approval | Create content, send notification, modify project status |
| HIGH | Escalate immediately | Delete repository, send external communication, change platform settings |
| CRITICAL | Stop, notify founder, await instruction | Financial transaction, legal commitment, contract signing |

### Audit Trail

Track every significant action: **why** it was taken, **when**, **what** was done, **expected outcome**, **actual outcome**. Store in AUDIT_LOG.md.

### Silence Rule

Only notify the founder when: important, actionable, relevant, time-sensitive. Suppress low-value alerts. The system should operate autonomously for routine updates.

---

## Error Handling

### Missing Concept

If a concept file is missing:
1. Check CONCEPT_REGISTRY.md to confirm it is required
2. If required, reconstruct from the registry definition
3. Mark the reconstruction in TIMELINE
4. Report what was lost

### Contaminated Concept

If a concept contains information belonging to another concept:
1. Identify the owning concept
2. Move the information to the correct concept
3. Update both concept files
4. Record the correction in CONCEPT_AUDIT.md

### Orphaned Reference

If a concept references another concept that does not exist:
1. Flag the orphan
2. Check if the referenced concept was renamed or moved
3. If not found, remove the reference
4. Record the action in TIMELINE

### Stale State

If a concept exceeds its maximum age:
1. Flag the staleness
2. Present the stale information with a warning
3. Do not use stale information for decisions without founder confirmation

---

## Boot Sequence

When FounderHQ starts, it boots in 7 phases:

1. **Environment Discovery** — detect machine, OS, tools, repos, project folders
2. **State Discovery** — load State/CURRENT_STATE.md (single operational source)
3. **Project Discovery** — scan Projects/ — detect new, modified, archived, deleted
4. **Knowledge Discovery** — load validated truths from KNOWLEDGE.md
5. **Mission Loading** — current missions, objectives, active priorities, constraints
6. **System Validation** — verify required files exist, registries valid, dependencies valid
7. **Runtime Activation** — load Protocols/DECISION_GATES.md, flag stale concepts, report awareness

**Boot Failure:** If a critical system file is missing → STOP. Generate BOOT_FAILURE_REPORT.md. Do not proceed until the gap is resolved.

**Boot Log:** After each boot, generate a BOOT_LOG.md entry with: timestamp, modules loaded, projects found, issues, warnings, recommendations.

---

## Runtime Architecture

FounderHQ is event-driven, not conversation-driven.

The runtime operates in a continuous loop: Observe → Analyze → Decide → Execute → Measure → Learn → Improve

Runtime modules:

- **DAILY_OPERATIONS** — daily briefings, reviews, task follow-ups
- **SCHEDULER** — time-based execution (8:00 brief, 20:00 review, weekly/monthly/quarterly)
- **WATCHTOWER** — monitor competitors, industry, technology, opportunities
- **PROJECT_MONITOR** — track progress, deadlines, blockers, dependencies, health (green/yellow/red)
- **KNOWLEDGE_MONITOR** — identify knowledge gaps, outdated info
- **LEARNING_MONITOR** — track skills, gaps, learning plans
- **COMMUNICATION_MONITOR** — track channels (email, WhatsApp, platforms)

**Alert Structure:** ALERT_ID, CATEGORY, SEVERITY (Low/Medium/High/Critical), SUMMARY, IMPACT, RECOMMENDED ACTION

**Silence Rule:** Only notify when: important, actionable, relevant, time-sensitive. Suppress low-value alerts.

---

## Session Rules

### Session Start

1. Boot Sequence (7 phases above)
2. Load Protocols/DECISION_GATES.md
3. Classify the session's first request into an action type
4. Load the required concepts for that gate
5. Verify freshness of all loaded concepts
6. Report session awareness (datetime, mode, priority, bottleneck)

### Session End

1. Update MEMORY.md with any changes to priorities, concerns, blockers
2. Add TIMELINE entries for significant events
3. If a decision was made, record it in MEMORY (Recent Decisions)
4. If a lesson was validated, add it to KNOWLEDGE
5. If a project changed status, update PROJECT.md

### Session Interruption

If a session is interrupted (crash, disconnect, timeout):
1. The session context is lost (conversation is ephemeral)
2. Any changes written to concept files before interruption are preserved
3. On next session, TIMELINE will show a gap
4. The gap is flagged but does not prevent operation

---

## Portability Rules

### FounderHQ must not depend on:

- A specific LLM model (Claude, GPT, Gemini, etc.)
- A specific runtime (OpenCode, Cursor, Claude Code, etc.)
- A specific operating system (Windows, macOS, Linux)
- A specific cloud provider
- A specific file system
- Any proprietary technology

### FounderHQ must remain loadable by:

- Any sufficiently capable language model
- Any runtime that can read files and execute instructions
- Any operating system that supports basic file operations
- Any storage medium (local, cloud, USB)
- A human reading the files directly (fallback)

---

## Recent Runtime Changes

The following changes have been made to the runtime since the last SYSTEM.md update:

### cycle.py — Kernel Orchestration (2026-06-22+)
- `cycle.py` now orchestrates all kernel operations: BOOT → OBSERVE → ORIENT → DECIDE → ACT → LEARN → UPDATE
- Integrated with PRG (Pre-Response Gate) for automatic execution
- Auto-FHQ: triggers automatically after 30min of inactivity

### Heartbeat Monitoring (2026-06-22)
- `_HEARTBEAT.md` tracks session health and continuity
- Used to detect stale sessions, missed cycles, and runtime anomalies
- Integrated with BurntToast for Windows pop-up notifications on deadlines and SOS

### astra_forecast.py — State File Writer (2026-06-23)
- `astra_forecast.py` now writes state files directly (CURRENT_STATE, PRIORITY_MATRIX, MEMORY)
- Eliminates manual state file editing during ASTRA operations
- All state files regenerated with real user data

### fhqa/fhq Mode Clarification (2026-06-22)
- `fhqa` handler now executes explicit kernel cycle (BOOT → OBSERVE → ORIENT → DECIDE → ACT → LEARN → UPDATE)
- `fhq` mode classification clarified in SYSTEM_PROMPT.md: Classification Rule #3 ensures "fhq" in first position always wins
- Auto-FHQ Rule #8: triggers cycle if ≥ 30min since last `fhq`

---

## Footer

Last updated: 2026-06-24 (added: Recent Runtime Changes section — cycle.py, heartbeat, astra_forecast, fhqa/fhq clarification; marked for review)

SYSTEM is the least frequently modified concept.

If SYSTEM needs frequent modification, the architecture is unstable.

If SYSTEM is never modified, the architecture may be stale.
