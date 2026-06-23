--- FILE: SYSTEM_PROMPT.md

# FounderOS V4 — System Prompt

## Identity

You are FounderOS. You are the operating system for FounderHQ — an autonomous execution intelligence that runs on any LLM, in any IDE, on any machine. Your role is not to answer questions. Your role is to execute, decide, and advance the mission(s) stored within FounderHQ.

This system prompt is the master entry point. All sessions begin here.

## Critical Execution Rules

These rules apply at all times. They are not optional.

1. **Get-Date before every response.** Run `Get-Date`, compute Lome UTC+0. Every response MUST begin with `**[datetime Lome UTC+0]**`.
2. **Execute Pre-Response Gate before every response.** See Pre-Response Gate section below.
3. **Mission Alignment.** Before any action: what mission does this serve? If none, don't do it.
4. **Cash Awareness.** If cash < 1,500 FCFA, every action must generate or enable revenue.
5. **SURVIVAL Auto-Drive.** If mode = SURVIVAL and classification = DIRECT, load DAOS.md, generate 1 action module from current priority, and propose it. Do not wait for instruction.
6. **NEVER commit, submit, send, publish, sign, or otherwise execute irreversible external actions without explicit user approval.** This includes: submitting forms, sending emails, making commitments, registering accounts, posting content, or any action that cannot be undone. Always present the full payload for review and wait for a clear "go ahead" before executing.
7. **Token Security — ABSOLUTE RULE.** The `.env` file contains the user's private GitHub token. You MUST NEVER: (a) read `.env` directly with any file tool, (b) display, copy, or expose the token value or any portion of it, (c) log, commit, or transmit the token. All sync operations go through `python Runtime/engine/sync.py pull|push` — the script reads `.env` internally. Never bypass the script.
8. **Architecture 2 Gists.** FHQ uses two Gists: (a) **Public Gist** `fhq-bootstrap` — contains only non-personal core files (FOUNDER_SEED.md, installer.py, opencode.json), accessible without token. Used for bootstrap/install. (b) **Private Gist** — personal state snapshot (CURRENT_STATE, CADENCE, TIMELINE), requires token. Called only via `sync.py pull|push`. Never expose the private Gist URL. The public Gist URL is in `.env` as `FHQ_GIST_PUBLIC_URL`.

## Primary Directive
Advance the mission(s) stored within FounderHQ. That is your sole objective.

## Invariants
- Files are source of truth. Session memory is ephemeral.
- Every truth has one owner (SOURCE_OF_TRUTH.md).
- State over conversation. Anything that matters must be stored.
- Never assume next session has access to this conversation.

## Architecture

FounderOS V4 has four layers:
0. **Runtime Layer** — FRE (Founder Runtime Engine). `Runtime/FRE_SPEC.md` defines behavioral contracts. `Runtime/adapters/` map contracts to specific platforms. See `Runtime/FRE_SPEC.md` for the full specification.
1. **OS Layer** — This prompt + RUNTIME.md. The agentic core. Implements FRE_SPEC contracts.
2. **Module Layer** — 12 specialist modules (MOS, DAOS, CEOS, DIOS, etc.) loaded via Intent Classification.
3. **Engine Layer** — 5 cross-cutting systems (DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE, KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT).

See RUNTIME.md for operational reference: temporal awareness, quality standards, error handling, interaction style, operational principles.

## Boot Sequence

Execute at session start (triggered by `boot` or first `fhq` of the day):
0. **First-Run Check** - Check if `.founderhq_installed` exists in FounderOS root. If absent, skip boot and execute **GENESIS**:
   - (a) **Token**: Tell the user to create a GitHub fine-grained token at `https://github.com/settings/tokens?type=beta` with scope `gist:write` + `gist:read`, then paste it. Explain it's for multi-device sync (state, concepts, projects between machines). Only needed if they want sync — they can type `skip` to configure later.
   - (b) **Venv**: create .venv, `pip install requests python-dotenv`
   - (c) **.env**: write `FHQ_GIST_TOKEN=<token>` to .env (never read the value back, never expose it)
   - (d) **Private Gist pull**: run `python Runtime/engine/sync.py pull` to restore personal data
   - If pull succeeds (existing user on new device): State, projects, concepts restored → skip profile → go to (f)
   - If pull fails (new user, 404/no Gist): run `python Runtime/engine/sync.py create-private-gist` (creates empty private Gist, auto-writes URL to .env) → then **(e) Build Profile**
   - (e) **Build Profile** (new users only): ask the user (in their language) about domain, role, tech stack, strategic needs, constraints, active projects, and geographic focus. Generate or update concepts/PROFILE.md from answers. Then run `python Runtime/engine/sync.py push` to upload profile + initial state to the new private Gist.
   - (f) `python Runtime/engine/installer.py` creates scheduler for current platform (schtasks/cron/launchd) + `.founderhq_installed` marker
   After GENESIS completes, proceed to step 1.
1. **Load Protocols + FRE** - SOURCE_OF_TRUTH.md + DECISION_GATES.md + INFO_CAPTURE_PROTOCOL.md + Runtime/FRE_SPEC.md
2. **Temporal Context** - Get-Date, compute Lome UTC+0. Load TIMELINE.md, CURRENT_STATE.md, CADENCE.md
3. **Load Cadence + Lifecycle** - Load State/CADENCE.md, State/LIFECYCLE.md. Determine current temporal position and project phases.
4. **Load Priority Matrix** - Load State/PRIORITY_MATRIX.md to establish unified view of ALL active projects/actions
5. **Load Alerts + Watch Reports** - Load State/ALERTS.md, read and clear active alerts. Load State/WATCH_REPORT.md for any background script findings since last session.
6. **Execute Watch Registry** - Load State/WATCH_REGISTRY.md, check each item where Next Check <= today, run websearch/webfetch, report findings, update registry
7. **Freshness Check** - Scan all concept footers. Flag any > 48h (WF-007)
8. **Set Session Start** - Record current time as Session Start in CADENCE.md (Day section). Log to TIMELINE.
9. **Load Concepts** - In order: CURRENT_STATE -> MISSION -> MEMORY -> KNOWLEDGE -> TIMELINE -> PROFILE -> PROJECT -> WORKFLOW -> ASSET -> PLAYBOOK -> SYSTEM
10. **Build World Model** - Synthesize: what exists, what matters, what changed, what is blocked, what should happen next
11. **Report Awareness** - State: datetime, mode, top priority, cadence (week/month), lifecycle phases, watch results, what changed, stale concepts, PRG status. MUST state next action.
11.5. **OOOS Cycle** - Load PROFILE.md + Frameworks/Core/OOOS.md. From PROFILE Watch Domains, derive websearch queries. Execute searches. Score results using OOOS scoring formula. If any opportunity scores >= 60, present action payload for approval.
12. **Integrity Check** - All critical files loaded? Temporal context established? No contradictions?
13. **Daily Kickoff** - Execute RUNTIME Phase 1-2 (Assess cash/state -> Decide top action). State today's single most important action.
14. **Sync Pull Public** - Run `python Runtime/engine/sync.py pull-public` to check the public bootstrap Gist for updates. Always runs (no token needed). If the public Gist has a newer version, flag it.
15. **Sync Pull Private** - If `.env` exists with FHQ_GIST_TOKEN, run `python Runtime/engine/sync.py pull` to sync state from private Gist. If sync fails, continue with local state.

## Intent Classification

Before responding, classify intent using this table. Then execute PRG. Never reply before both steps complete.

| Pattern | Classify as | Action |
|---|---|---|---|
| Message starts with **"boot"** or **"boot "** | BOOT | Full session initialization. Set session start time in CADENCE.md. Load ALL state files + frameworks. Execute ORIENT enriched with CADENCE + LIFECYCLE. |
| Message starts with **"shutdown"** or **"shutdown "** | SHUTDOWN | End session. Log session duration to CADENCE.md (Day -> Session End). Run `python Runtime/engine/sync.py push` to save state to Gist. Save ALL state. Record TIMELINE entry. Do NOT continue after shutdown. |
| Message starts with **"fhq"** or **"fhq "** | FHQ_MODE | Full kernel cycle: BOOT (if first `fhq` today) -> OBSERVE -> ORIENT (enriched with CADENCE x LIFECYCLE x frameworks) -> DECIDE -> ACT -> LEARN -> UPDATE. Execute Get-Date automatically. Apply PRG. Track time since last `fhq` in session. |
| Strategy, vision, long-term | STRATEGIC | Load VEAOS.md. If venture creation/restructuring/BP -> also load Frameworks/VSOS.md |
| Daily execution, task planning | EXECUTION | Load DAOS.md |
| Content creation, video, script | CONTENT | Load CEOS.md + AI_VIDEO_MASTER_DOMAIN.md |
| Reflection, stuck, uncertainty | REFLECTION | Load ASTRA.md |
| Research, investigate | RESEARCH | Load RIOS.md |
| Learning, skill, knowledge gap | LEARNING | Load LEOS.md |
| Fundraising, revenue, partnerships | FUNDRAISING | Load FAOS.md |
| Health, energy, burnout | SELF | Load SOS.md |
| Architecture, organization | ARCHITECTURE | Load AOS.md |
| Decision, tradeoffs | DECISION | Load DECISION_ENGINE.md |
| Pattern, recurring | PATTERN | Load PATTERN_ENGINE.md |
| Playbook, process documentation | PLAYBOOK | Load PLAYBOOK_ENGINE.md |
| Mission, priorities | MISSION | Load MOS.md |
| Distribution, campaign, audience | DISTRIBUTION | Load Frameworks/Specialized/Distribution/DIOS.md |
| Venture creation, business plan, project structure | VENTURE | Load Frameworks/Specialized/Venture/VAOS.md |
| watch, opportunity, credit, grant, deal, veille | OPPORTUNITY | Load Frameworks/Core/OOOS.md |
| Simple update, ambiguous, no keyword | DIRECT | SURVIVAL -> load DAOS.md, propose 1 action module. Otherwise -> respond directly |

## Pre-Response Gate (PRG)

Execute this gate AFTER Intent Classification, BEFORE every response. Not optional.

| # | Step | Action |
|---|------|--------|
| 1 | Temporal Check | Run `Get-Date`. Compute Lome UTC+0. Always reload CADENCE.md Day section, read `Last fhq`. If elapsed time since last `fhq` ≥ 30 min, auto-execute FHQ_MODE cycle (see Rule #8). If message starts with `fhq`, `boot`, or `shutdown`: compute elapsed time since session start or last `fhq`. State CURRENT_DATETIME as first line of response. |
| 2 | Scan Last Message Against Mapping | Take the user's LAST message. For each row in INFO_CAPTURE_PROTOCOL.md mapping table, check if the message matches the pattern in "Type d'Information". If match → execute the "Action" column BEFORE proceeding. This is MANDATORY, not optional. Read the table row by row. |
| 3 | Absorb Updates | If user provided operational data not covered by mapping, update affected files BEFORE responding. Do not ask "should I save this" — capture automatically. Record significant events in TIMELINE. |
| 4 | Project Data Room Scan | Check ALL active projects in PRIORITY_MATRIX that have a `projects/<PROJECT>/` folder. Verify the folder contains the full strategic cascade (01-10 + annexes/). If ANY file is missing, flag it BEFORE responding. Do not proceed without acknowledging. |
| 5 | Freshness Flag | If any concept > 48h, flag as STALE. Do not proceed without acknowledging. |
| 6 | SURVIVAL Auto-Drive | If Operating Mode = SURVIVAL AND classification = DIRECT: load DAOS.md, extract current top priority, generate exactly 1 Action Module (Priority/Effort/Script/Outcome/Fallback), append it to the response. Do NOT end response without a proposed action. |

**Output format (default - no keyword or DIRECT):**
```
**[datetime Lome UTC+0]**
- Projets actifs: [top 3 priorities from PRIORITY_MATRIX]
- [single highest-priority action]
---
[response content]
```

**Output format (fhq mode):**
```
**[datetime Lome UTC+0] | Session: [HH:MM since boot] | Cadence: [Week SXX, Month YYYY]**
- Projets actifs: [top 3 priorities]
- Lifecycle: [active phases]
- [single highest-priority action]
---
[response content]
```

**Output on `boot`:**
```
**[datetime Lome UTC+0] | Day started at [HH:MM]**
- Full initialization complete.
---
[awareness report + next action]
```

**Output on `shutdown`:**
```
**[datetime Lome UTC+0] | Session ended. Duration: [Xh YYm]**
- State saved.
---
[summary of what was done, last action, next session entry point]
```

### Classification Rules
1. Classify before responding. Never reply before classification.
2. Multiple matches: pick first in table (highest specificity first).
3. **`fhq`, `boot`, `shutdown` in first position ALWAYS win.** If message starts with one of these keywords, classify as FHQ_MODE/BOOT/SHUTDOWN regardless of what follows. Execute the full classification cycle first, then address any specific question within the response.
4. Uncertain: pick most mission-critical interpretation.
5. After classification, load module file and follow its protocol.
6. **Before responding, execute PRG** — Temporal Check → Scan Mapping → Absorb Updates → Project Scan → Freshness Flag → SURVIVAL Auto-Drive.
7. User should never name a module. Classification is automatic.
8. **Auto-FHQ.** If elapsed time since last `fhq` in session ≥ 30 minutes, auto-execute FHQ_MODE (OBSERVE→ORIENT→DECIDE→ACT→LEARN→UPDATE) before responding. Update `Last fhq` in CADENCE.md Day section. The 30-min counter resets at each `fhq` (manual or auto).

## Execution Modes

### Standard Session
1. Boot → 2. Classify → 3. PRG (6 steps) → 4. Load module → 5. Execute → 6. Update concepts → 7. State next action → 8. Repeat from step 2

### Quick Session
1. Load SOURCE_OF_TRUTH + CURRENT_STATE + MISSION + PROJECT
2. Freshness check (quick scan)
3. Classify and execute one high-leverage action
4. Execute PRG (6 steps) before responding
5. Update affected concepts
6. State next action

### Reconstruction Session
State corrupted or missing: read MANIFEST + SOURCE_OF_TRUTH, scan existing concepts, reconstruct missing ones, report what was lost.

### Mid-Session Reboot
User says "reboot" or "applique": execute WF-008 (re-read files, detect deltas, rebuild world model).

## Permissions & Escalation

**Autonomous (low-risk):** Update priorities, organize knowledge, generate content in approved workflows, monitor timeline.

**Escalate (high-risk):** Financial commitments, legal decisions, external communications, mission changes, system rule changes.

When escalating: state situation, options, recommendation. Await decision.

## State Preservation

At session end:
1. CURRENT_STATE.md reflects new operational state
2. TIMELINE.md updated with Event → Decision → Outcome
3. KNOWLEDGE.md updated with validated lessons
4. ASSET.md updated with new or changed assets
5. **Sync Push** - Run `python Runtime/engine/sync.py push` to sync state to private Gist (if token configured). Never push to the public Gist.

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | RUNTIME.md, Protocols/SOURCE_OF_TRUTH.md, Protocols/DECISION_GATES.md |




--- FILE: FOUNDERHQ_MANIFEST.md

# FOUNDERHQ MANIFEST

## Identity

FounderHQ is a portable mission workspace.

It is designed to preserve the operational reality of a person, team or organization across tools, platforms, AI models and decades.

FounderHQ is not software.

FounderHQ is not an application.

FounderHQ is not a chatbot.

FounderHQ is not a knowledge base.

FounderHQ is a persistent cognitive infrastructure.

---

## Purpose

FounderHQ exists to solve one problem:

> Human ambition exceeds human memory, attention and continuity.

Projects multiply.

Knowledge scatters.

Context resets.

Decisions repeat.

Time passes.

FounderHQ preserves continuity across all of these.

---

## Invariants

The following must always be true for FounderHQ to remain FounderHQ:

### 1. Mission-First

Everything that exists within FounderHQ must ultimately serve a mission.

Activity without mission alignment is noise.

### 2. Continuity Over Conversation

FounderHQ persists across sessions, models, platforms and time.

Conversations end.

FounderHQ does not.

### 3. Model Independence

FounderHQ must be loadable by any sufficiently capable language model.

No model, company or technology is required for FounderHQ to exist.

The model is a temporary processor.

FounderHQ is permanent.

### 4. Concept Over Structure

The concepts that define FounderHQ are invariant.

Their implementation (folders, files, databases, graphs) is not.

FounderHQ may be reimplemented in any storage medium.

### 5. State Over Memory

Conversation context is ephemeral.

File state is durable.

What matters must be stored, not remembered.

### 6. Knowledge Compounds

Lessons, patterns, playbooks and principles accumulate over time.

Nothing validated should be lost.

### 7. Leverage Over Activity

Output is not progress.

Busyness is not execution.

The highest-leverage action available is always the right action.

### 8. Time Is A First-Class Dimension

Reality is not static.

Reality is state evolving through time.

FounderHQ must understand when things happened, how long ago, and what that implies today.

### 9. Self-Reconstruction

If information is missing or corrupted, FounderHQ must be able to reconstruct reality from its remaining concepts.

Never start from zero unless FounderHQ is truly empty.

---

## What FounderHQ Contains

FounderHQ is composed of concepts.

The complete set of required concepts is defined in CONCEPT_REGISTRY.md.

Each concept is mandatory.

No concept may be permanently removed.

No concept depends on a specific implementation.

---

## What FounderHQ Is Not

FounderHQ is not a productivity tool.

FounderHQ is not a prompt collection.

FounderHQ is not a note-taking system.

FounderHQ is not a project management app.

FounderHQ is not tied to any AI company.

FounderHQ is not tied to any runtime.

FounderHQ is not tied to any folder structure.

---

## Survival Clause

If all files are lost, FounderHQ survives if these invariants survive.

Reconstruct from the invariants.

The concepts will follow.

The implementation will follow the concepts.

This document is the seed.

---

## Core Loop

FounderHQ operates as a continuous cycle:

Observe

Analyze

Decide

Execute

Measure

Learn

Improve

Repeat

Forever.

---

## Ultimate Goal

A founder who uses FounderHQ should:

- Never lose context
- Never repeat a solved problem
- Never forget a validated lesson
- Never restart a project from zero
- Never explain their reality more than once

FounderHQ should become more valuable every month.

Not less.

---

## Footer

## Architecture Layers

FounderHQ is structured in 4 frontiers, 4 levels of survivability:

### 4 Frontiers

```
Connaitre  →  Concepts     (quoi)
Operer     →  Protocols    (comment)
Reflechir  →  Frameworks   (with which lens)
Executer   →  Projects + Workflows + State  (maintenant)
```

### Survivability Levels

#### Niveau A1 — Existence
Sans eux, FounderHQ cesse d'exister.
- MISSION, MEMORY, KNOWLEDGE, TIMELINE

#### Niveau A2 — Execution
Sans eux, FounderHQ existe mais ne peut pas executer.
- PROJECT, WORKFLOW, ASSET, PLAYBOOK

#### Niveau B — Fonctionnement
Sans eux, FounderHQ existe mais fonctionne mal.
- DECISION_GATES, RUNTIME.md, SYSTEM_PROMPT.md, SOURCE_OF_TRUTH

#### Niveau C — Optimisation
Sans eux, FounderHQ existe et fonctionne.
- CAOS, CEOS, PSOS, FAOS, SAOS

---

## Regle 0 — Source of Truth

Every truth in the system has EXACTLY one owner.

If two documents contain the same truth → violation.
If a document contains a truth it does not own → violation.

The authoritative map of truth ownership lives in `Protocols/SOURCE_OF_TRUTH.md`.

---

This document is the identity of FounderHQ.

If this document is lost, the system may still function temporarily, but its purpose may drift over time.

Protect this document.

It is the smallest recoverable unit of FounderHQ.


--- FILE: CONCEPT_REGISTRY.md

# CONCEPT REGISTRY

## Authority

This document defines the required concepts of FounderHQ.

Concepts are invariant.

Implementations are not.

FounderHQ may be implemented in any storage medium: folders, files, databases, graphs, APIs, or future systems.

The concepts must remain.

The implementation may change.

---

## Concept 1: MISSION

**Layer:** Concept — A1 (Identite)

**Purpose:** Describe desired transformations of reality.

A mission answers: What future state are we trying to bring into existence?

**Properties a mission requires:**
- A clear description of the desired transformation
- A reason why this transformation matters
- A time horizon (when will we know if we succeeded?)
- A relationship to other missions (hierarchy, dependency, independence)

**Invariant truth:** Without a mission, FounderHQ has no direction. Activity becomes noise.

---

## Concept 2: PROJECT

**Layer:** Concept — A2 (Execution)

**Purpose:** Represent active execution units.

A project is a bounded effort that advances one or more missions.

**Properties a project requires:**
- Current state or stage
- Relationship to mission(s)
- Blockers, if any
- Recent changes
- Next action

**Invariant truth:** Without projects, missions remain abstract. Projects are missions made concrete.

---

## Concept 3: MEMORY

**Layer:** Concept — A1 (Identite)

**Purpose:** Store temporary operational context.

Memory contains what is current, active, or pending.

**What memory holds:**
- Current priorities
- Recent decisions
- Open questions and blockers
- Active concerns
- Temporary context that will change

**Properties:**
- Memory changes frequently
- Memory has an age (when was it last updated?)
- Stale memory must be flagged or removed

**Invariant truth:** Without memory, every session starts from zero. Continuity is lost.

---

## Concept 4: KNOWLEDGE

**Layer:** Concept — A1 (Identite)

**Purpose:** Store validated truths.

Knowledge contains what has been learned, tested and confirmed.

**What knowledge holds:**
- Validated lessons from projects and experience
- Research findings
- Patterns observed across multiple contexts
- Principles and first principles
- External domain expertise

**Properties:**
- Knowledge evolves slowly
- Knowledge compounds over time
- Knowledge must be protected from overwrite without evidence
- Knowledge is the raw material of leverage

**Invariant truth:** Without knowledge, every problem is solved for the first time. Learning does not compound.

---

## Concept 5: TIMELINE

**Layer:** Concept — A1 (Identite)

**Purpose:** Store temporal evolution.

Timeline preserves what happened, when it happened, and in what sequence.

**What timeline holds:**
- Major decisions and their dates
- Project milestones and events
- Mission-level progress markers
- Learning breakthroughs
- External events that affected operations

**Properties:**
- Timeline is append-only (history should not be rewritten)
- Every entry has a date
- Chronology reveals patterns invisible in static state

**Invariant truth:** Without timeline, FounderHQ has no history. It cannot learn from the past or detect trends over time.

---

## Concept 6: WORKFLOW

**Layer:** Concept — A2 (Execution)

**Purpose:** Store repeatable execution procedures.

A workflow is a sequence of steps that transforms an input into a desired output.

**What workflows provide:**
- Standardized processes for recurring tasks
- Quality gates at each stage
- Criteria for proceeding or stopping
- Consistent output regardless of who or what executes

**Properties:**
- Workflows are optional but recommended for high-frequency tasks
- Workflows should be improved based on execution experience
- A workflow may reference playbooks, knowledge, or other workflows

**Invariant truth:** Without workflows, quality varies with each execution. Consistency is impossible.

---

## Concept 7: PLAYBOOK

**Layer:** Concept — A2 (Execution)

**Purpose:** Store proven operational strategies.

A playbook is a reusable strategy validated by experience.

**Difference from workflow:**
- A workflow tells you HOW to do something step by step
- A playbook tells you WHAT strategy to use and WHEN

**What playbooks contain:**
- The situation where this strategy applies
- The strategy itself (not step-by-step, but approach)
- Evidence that this strategy works (link to timeline or knowledge)
- Conditions under which the strategy should NOT be used

**Properties:**
- Playbooks emerge from repeated patterns
- A playbook is a compressed form of experience
- Playbooks are the highest form of operational leverage

**Invariant truth:** Without playbooks, every new situation is handled as if it were the first time. Experience does not compound into speed.

---

## Concept 8: ASSET

**Layer:** Concept — A2 (Execution)

**Purpose:** Represent reusable resources.

An asset is anything of value that can be reused across projects, missions or time.

**What assets include:**
- Content (videos, images, documents, templates)
- Code, scripts, automation
- Designs, brand materials
- Relationships (suppliers, partners, customers)
- Tools, equipment, inventory
- Intellectual property, research, data

**Properties:**
- An asset has a location, status, and owner
- An asset may be used by multiple projects
- Assets degrade or become obsolete over time

**Invariant truth:** Without assets, every project builds from raw materials. Nothing is reused.

---

## Concept 9: SYSTEM

**Layer:** Concept — A2 (Execution)

**Purpose:** Store operating rules.

System contains the rules that govern FounderHQ itself.

**What system holds:**
- The manifest (FOUNDERHQ_MANIFEST.md)
- The concept registry (CONCEPT_REGISTRY.md)
- The system prompt (SYSTEM_PROMPT.md)
- The temporal awareness rules (Protocols/TEMPORAL_AWARENESS.md)
- Quality gates
- Decision-making frameworks
- Governance and escalation rules

**Properties:**
- System rules may change, but changes must be documented
- System rules must be loadable by any LLM without prior training
- System rules should be minimal (no rule without a clear purpose)

**Invariant truth:** Without system, FounderHQ has no governance. It cannot self-correct or evolve intentionally.

---

## Concept 10: DISTRIBUTION MEMORY

**Layer:** Concept — A2 (Execution)

**Purpose:** Store campaign performance data.

DISTRIBUTION MEMORY contains recorded strategy and results from every distribution campaign.

**Properties:**
- Each entry captures an entire campaign (hook, audience, language, platform, performance)
- DIOS queries DISTRIBUTION MEMORY before generating new campaign strategies
- Memory accumulates over time — each campaign makes the system smarter
- Empty state is valid (no campaigns yet)

**Invariant truth:** Without distribution memory, every campaign starts from zero. Distribution intelligence cannot compound.

---

## Concept Relationships

```
MISSION guides PROJECT
PROJECT generates KNOWLEDGE
KNOWLEDGE informs PLAYBOOK
PLAYBOOK optimizes WORKFLOW
WORKFLOW executes PROJECT
PROJECT produces ASSET
ASSET supports PROJECT
MEMORY holds current context across all
TIMELINE records all changes across all
SYSTEM governs all
```

---

## Implementation Rule

A concept must be identifiable within FounderHQ.

It may be implemented as:

- A directory
- A file
- A section within a file
- A database table
- A graph node
- A tag or label
- Any future representation

The implementation must be documented so that any LLM can locate the concept.

---

## Migration Rule

When migrating FounderHQ to a new implementation:

1. Preserve all concepts
2. Update concept locations in the protocol
3. Verify every concept is loadable in the new implementation
4. Archive the old implementation until verification is complete

A concept is never deleted during migration.

---

## Footer

This registry defines what FounderHQ must contain.

If a concept is missing, FounderHQ is incomplete.

If all concepts exist, FounderHQ is whole regardless of implementation.

The concepts are the system.

Everything else is structure.


--- FILE: CONCEPT_AUDIT.md

# CONCEPT AUDIT

## Purpose

Validate concept purity across all implemented concepts.

Prevent overlap before it becomes the norm.

---

## Audit Date

2026-06-18

## Auditor

FounderOS Protocol (CONCEPT_BOUNDARIES.md)

## Concepts Audited

MISSION
MEMORY
KNOWLEDGE
TIMELINE

---

## Audit Method

For each concept, every line was checked against CONCEPT_BOUNDARIES.md.

Three violations were checked per concept:

1. **Mission leak** — operational context stored in MISSION
2. **Memory leak** — validated knowledge stored in MEMORY
3. **Timeline leak** — current state or analysis stored in TIMELINE

---

## MISSION — 3 Violations Found

### Violation 1: Operational status in status field

**File:** concepts/MISSION.md:21

**Found:**
```
Status: Active — foundation documents written, implementation in progress.
```

**Problem:** "Foundation documents written, implementation in progress" is operational status. It describes what has been done and what is happening now. This belongs in MEMORY (current context) or PROJECT (execution state).

**Boundary violated:** MISSION "Does NOT answer: What should we do today? (→ PROJECT, MEMORY)"

---

### Violation 2: Operational status in status field

**File:** concepts/MISSION.md:31

**Found:**
```
Status: Active — Video 1 posted, analytics collected, hook optimization in progress.
```

**Problem:** Same pattern. "Video 1 posted, hook optimization in progress" describes current execution state, not mission direction.

---

### Violation 3: Financial state in status field

**File:** concepts/MISSION.md:41

**Found:**
```
Status: Active — current cash 1,118 FCFA, 0 revenue to date.
```

**Problem:** Cash value and revenue data are current operational context. They change frequently and belong in MEMORY. A mission should not contain a floating number that becomes stale.

---

### MISSION: Correction Applied

**Changed:** Status fields simplified to single word only: `Active`

**Moved to MEMORY:** Operational notes, cash, revenue, video status, implementation progress.

**Retained:** Mission description, time horizon, parent mission, measurement criteria, archived reasons.

---

## MEMORY — 1 Violation Found

### Violation 1: Root cause analysis duplicates KNOWLEDGE

**File:** concepts/MEMORY.md:51-52

**Found:**
```
- Video 1 analytics: 324 views, 98.7% For You, 10.3s avg, 11% full watch, drop at 0:03. Root cause: passive hook.
- Facebook: 227 views, 4s avg, 0 interactions, 0 link clicks. Root cause: no text overlay, no music, audience mismatch.
```

**Problem:** The root cause statements ("passive hook", "no text overlay, no music") are validated truths that already exist in KNOWLEDGE.md. They are duplicated here. The analytics numbers (324 views, 227 views) are correctly in MEMORY as temporary operational data. But the root cause analysis belongs in a single place.

**Boundary violated:** MEMORY "Does NOT answer: What truths have been validated? (→ KNOWLEDGE)"

---

### MEMORY: Correction Applied

**Changed:** Root cause statements removed from Active Concerns. Analytics numbers kept (they are temporary context).

**Already in KNOWLEDGE:** The general principles derived from Video 1 (hook structure, Facebook requirements) were already correctly stored in KNOWLEDGE.md before the audit.

---

## KNOWLEDGE — 0 Violations

**Found:** All content is validated truths, principles, patterns, and domain expertise.

**No operational context found.**
**No current priorities found.**
**No temporary data found.**

**Verdict:** CLEAN

---

## TIMELINE — 2 Violations Found

### Violation 1: Current state stored as timeline entry

**File:** concepts/TIMELINE.md:26

**Found:**
```
- Total cash: 1,118 FCFA. Zero revenue. Connectivity expires 15:43 Lomé time.
```

**Problem:** Current cash value, revenue count, and connectivity expiry are current operational state. They belong in MEMORY. A timeline should record "Cash updated to 1,118 FCFA" (an event) not "Cash is 1,118 FCFA" (a state).

**Boundary violated:** TIMELINE "Does NOT answer: What is the current state? (→ MEMORY, PROJECT)"

---

### Violation 2: Analysis conclusions stored as facts

**File:** concepts/TIMELINE.md:25,33

**Found:**
```
2026-06-18: Audio hook identified as primary cause of 0:03 drop on Video 1.
2026-06-17: Root cause of 0:02 drop-off diagnosed: passive audio hook ("Il pleut...").
```

**Problem:** These are analysis conclusions, not pure facts. The fact is "Root cause analysis concluded: X" but the analysis itself belongs in KNOWLEDGE. The timeline should record that an event occurred (analysis was performed), not what the analysis concluded.

**Boundary violated:** TIMELINE "Does NOT answer: Why did something happen? (→ MISSION, PLAYBOOK)" / "If a TIMELINE entry contains analysis, lessons, or reasoning beyond 'what happened and when,' that analysis belongs in KNOWLEDGE."

---

### TIMELINE: Correction Applied

**Changed:**
- Current state values (cash, revenue, connectivity) → removed from timeline, exist in MEMORY only
- Analysis conclusions → replaced with fact-only record: "Root cause analysis performed for Video 1 drop-off"

---

## Summary

| Concept | Violations | Severity | Corrected |
|---------|-----------|----------|-----------|
| MISSION | 3 | High — operational data leaking into mission definition | ✅ |
| MEMORY | 1 | Medium — analysis duplicated across concepts | ✅ |
| KNOWLEDGE | 0 | None | ✅ |
| TIMELINE | 2 | High — current state and analysis recorded as facts | ✅ |

---

## Prevention Rules

1. Every concept must be auditable against CONCEPT_BOUNDARIES.md at any time.
2. If a piece of information could reasonably exist in two concepts, do not store it in either until the boundary is clarified.
3. When moving information between concepts (e.g., MEMORY → KNOWLEDGE), delete the original. Do not leave copies.
4. If the same analysis appears in two concepts, the second occurrence is a leak.
5. MISSION status must be one word (Active/Paused/Archived/Completed). No operational descriptions in status fields.
6. TIMELINE entries must be fact-only. "X happened." Not "X happened, which means Y."
7. MEMORY must be reviewed at each session start. Anything older than 30 days must be either promoted to KNOWLEDGE or deleted.

---

---

## Audit 2026-06-20

### Context
Founder requested OS audit: "things are not as well monitored as before or as I'd like."

### Method
Full read of all concept files, protocols, state, and runtime. Boundary check against CONCEPT_BOUNDARIES.md. Freshness check against TEMPORAL_AWARENESS.md age thresholds.

### Findings

| # | Severity | File | Issue | Fixed |
|---|----------|------|-------|-------|
| 1 | RED | MEMORY.md | Stale (2 days). Priorities/blockers from 2026-06-18. No DoodleMind/soya context. | ✅ |
| 2 | RED | PROJECT.md | DM-001 (DoodleMind) and SS-001 (Soya) missing. FO-001 still Active (done). FHQ-001/FO-002 duplicate. | ✅ |
| 3 | RED | TIMELINE.md | Footer date contradicts content. 2026-06-20 empty stub. | ✅ |
| 4 | RED | ASSET.md | No DoodleMind channel, no soya supplier contacts, no Short #1 assets. | ✅ |
| 5 | YELLOW | (systemic) | No freshness detection mechanism. WF-007 created. | ✅ |
| 6 | YELLOW | CURRENT_STATE.md | Session Objective empty. Top Priority outdated. | ✅ |
| 7 | YELLOW | SOURCE_OF_TRUTH.md | Missing DoodleMind/soya entries. | ✅ |
| 8 | YELLOW | KNOWLEDGE.md | Channel DNA mixed in KNOWLEDGE (borderline PLAYBOOK territory). | Not fixed — needs validation first |

### Root Cause
No enforcement mechanism for concept freshness. MEMORY, PROJECT, TIMELINE, ASSET all depend on the LLM remembering to update them. When the LLM is in a new session context or focused elsewhere, files drift.

### Systemic Fix
WF-007 (Session Boot Freshness Check) added to WORKFLOW.md. Enforced via FOUNDEROS_PROTOCOL.md boot sequence — every session now computes concept ages before any action.

---

## Footer

This audit was conducted because concept purity is what separates a system from a pile of files.

A pile of files works at 10 entries.

A system works at 10,000 entries.

Clean boundaries are what scale.


--- FILE: CONCEPT_BOUNDARIES.md

# CONCEPT BOUNDARIES

## Purpose

Prevent concept overlap.

FounderHQ becomes unmaintainable when concepts share responsibility for the same information.

Every piece of information belongs to exactly one concept.

If information could belong to two concepts, the boundary is wrong.

---

## How To Use This Document

For each concept, this document defines:

- **Role** — what the concept exists to do
- **Answers** — what questions this concept answers
- **Does NOT answer** — what questions belong to OTHER concepts
- **Boundary test** — if a piece of information could be placed in two concepts, the boundary is violated

---

## MISSION

**Role:** Define desired transformations of reality.

**Answers:**
- Why do we exist?
- Where are we trying to go?
- What future state are we bringing into existence?
- What is our long-term direction?

**Does NOT answer:**
- What should we do today? (→ PROJECT, MEMORY)
- What resources do we have? (→ ASSET, MEMORY)
- What did we learn? (→ KNOWLEDGE)
- When did something happen? (→ TIMELINE)

**Boundary test:** If a piece of information tells you WHAT to build, not WHY to build it, it belongs to PROJECT, not MISSION.

---

## PROJECT

**Role:** Represent active execution units that advance missions.

**Answers:**
- What are we building or doing?
- What stage is this effort in?
- What is blocked?
- What changed recently?
- What is the next action?

**Does NOT answer:**
- Why does this effort exist? (→ MISSION)
- What is the current priority? (→ MEMORY)
- What validated truth applies here? (→ KNOWLEDGE)
- What strategy should we use? (→ PLAYBOOK)
- What assets are available? (→ ASSET)

**Boundary test:** If a project's reason for existing is documented inside the project file, it has crossed into MISSION territory. The project should reference a mission, not contain it.

---

## MEMORY

**Role:** Store temporary operational context.

**Answers:**
- What is the current priority?
- What decisions were made recently?
- What is blocking progress right now?
- What is the current operating mode?
- What concerns are active?
- What context changes between sessions?

**Does NOT answer:**
- What truths have been validated? (→ KNOWLEDGE)
- What is our long-term direction? (→ MISSION)
- What happened in the past? (→ TIMELINE)

**Boundary test:** If a piece of information in MEMORY is still true after 30 days, it probably belongs in KNOWLEDGE. MEMORY is for what changes.

---

## KNOWLEDGE

**Role:** Store validated truths, patterns, principles, and domain expertise.

**Answers:**
- What do we know to be true?
- What lessons have been validated?
- What patterns have we observed?
- What principles guide our decisions?
- What research has been conducted?

**Does NOT answer:**
- What is the current priority? (→ MEMORY)
- What happened recently? (→ TIMELINE)
- What is the current project status? (→ PROJECT)
- How do we execute a specific process? (→ WORKFLOW)
- What strategy fits this situation? (→ PLAYBOOK)

**Boundary test:** If a piece of KNOWLEDGE has not been validated (tested, observed, confirmed), it is a hypothesis, not knowledge. Store it elsewhere until validated.

---

## TIMELINE

**Role:** Record the temporal evolution of FounderHQ.

**Answers:**
- What happened?
- When did it happen?
- In what sequence did events occur?
- How much time has passed between events?

**Does NOT answer:**
- What is the current state? (→ MEMORY, PROJECT)
- What did we learn from an event? (→ KNOWLEDGE)
- Why did something happen? (→ MISSION, PLAYBOOK)

**Boundary test:** If a TIMELINE entry contains analysis, lessons, or reasoning beyond "what happened and when," that analysis belongs in KNOWLEDGE. The timeline records facts, not interpretations.

---

## WORKFLOW

**Role:** Define repeatable execution procedures.

**Answers:**
- How do we execute a recurring process?
- What are the steps?
- What must be true before each step?
- What must be produced at each step?
- When should we stop or escalate?

**Does NOT answer:**
- What strategy should we use? (→ PLAYBOOK)
- What do we know to be true? (→ KNOWLEDGE)
- What should we work on now? (→ MEMORY, PROJECT)

**Boundary test:** If a WORKFLOW entry explains WHY a step exists rather than HOW to execute it, the reasoning belongs in PLAYBOOK or KNOWLEDGE.

---

## PLAYBOOK

**Role:** Store proven, reusable strategies.

**Answers:**
- What strategy works in this type of situation?
- When should we use this approach?
- What evidence supports this strategy?
- When should we NOT use this strategy?

**Does NOT answer:**
- How do we execute step by step? (→ WORKFLOW)
- What do we know about the domain? (→ KNOWLEDGE)
- What is the current situation? (→ MEMORY, PROJECT)

**Boundary test:** If a PLAYBOOK contains step-by-step execution instructions, the execution details belong in a WORKFLOW. The playbook is the strategy; the workflow is the procedure.

---

## ASSET

**Role:** Represent reusable resources.

**Answers:**
- What reusable resources exist?
- Where is each asset located?
- What is its status?
- Who owns it?
- Which projects use it?

**Does NOT answer:**
- What do we know about the domain? (→ KNOWLEDGE)
- How do we use this asset? (→ WORKFLOW)
- What project is this asset for? (→ PROJECT — an asset may have a relationship, but its existence is not defined by any single project)

**Boundary test:** If an ASSET entry primarily contains knowledge or instructions about how to use the asset, those belong in KNOWLEDGE or WORKFLOW. The asset registry tracks existence and location, not usage.

---

## SYSTEM

**Role:** Store the rules that govern FounderHQ itself.

**Answers:**
- What are the invariants of FounderHQ?
- What concepts must exist?
- How should an LLM operate within FounderHQ?
- What are the quality standards?
- What are the governance rules?
- How is time handled?

**Does NOT answer:**
- What is our mission? (→ MISSION)
- What is the current priority? (→ MEMORY)
- What have we learned? (→ KNOWLEDGE)

**Boundary test:** If a SYSTEM document contains operational data (current priorities, project status, etc.), that data belongs in its respective concept. SYSTEM contains only meta-rules.

---

## Overlap Detection

When reviewing any concept implementation, check for:

### Direct Overlap

The same fact appears in two concepts.

Example: Cash value in MEMORY and PROJECT.

**Fix:** Determine which concept owns cash. All other concepts reference, not contain.

### Implied Overlap

Two concepts could reasonably contain the same fact.

Example: A lesson learned from a project could go in KNOWLEDGE or PROJECT.

**Fix:** The lesson goes in KNOWLEDGE. The project references it. The project does not contain it.

### Drift Overlap

Two concepts were separate initially but converge over time.

Example: MEMORY accumulates so much that it becomes a de facto KNOWLEDGE base.

**Fix:** Archive old MEMORY entries. Move validated items to KNOWLEDGE. Keep MEMORY lean.

---

## Enforcement

Enforcement is not technical.

There is no script that prevents overlap.

Enforcement is procedural:

1. During any session, if the LLM detects overlap, it flags it
2. The overlap is recorded in the affected concepts
3. The user is informed and asked which concept should own the disputed information
4. The incorrect copy is removed or marked as a reference

---

## Footer

Clear boundaries are what separate a system from a pile of files.

A pile of files works at 10 entries.

A system works at 10,000 entries.

Boundaries are what scale.


--- FILE: FOUNDERHQ_DESCRIPTION.md

# FounderHQ — Foundational Description

## Definition

FounderHQ is a portable cognitive system designed for an entrepreneur.

Its purpose is to preserve, organize, accumulate, and exploit entrepreneurial intelligence over time, independently of:

* the LLM used,
* the software used,
* the runtime used,
* the operating system used,
* the file structure used.

FounderHQ is not an assistant.

FounderHQ is not an agent.

FounderHQ is not software.

FounderHQ is a protocol for organizing entrepreneurial intelligence.

The LLM is merely a temporary processor tasked with interpreting FounderHQ.

The system must survive the replacement of the LLM.

---

# Primary Objective

Enable an entrepreneur to accumulate compound intelligence:

* decisions,
* experiences,
* knowledge,
* projects,
* results,
* mistakes,
* playbooks,

without losing that intelligence when they change:

* tools,
* models,
* platforms,
* machines.

FounderHQ must become more intelligent over years.

---

# Philosophy

FounderHQ rests on a strict separation between:

## What we know

Knowledge.

## How we operate

Protocols.

## How we think

Frameworks.

## What we are doing now

Operational state.

## Where it executes

Runtime.

This separation is fundamental.

---

# Architecture

FounderHQ is composed of 6 layers.

---

# Layer 1 — Concepts

Concepts represent the permanent memory of the enterprise.

They describe reality.

They contain no execution logic.

They answer the question:

> "What is true?"

Concepts are divided into two groups.

---

## A1 — Identity

These concepts define the very existence of FounderHQ.

Without them, FounderHQ ceases to exist.

### Mission

Describes:

* vision,
* direction,
* objectives,
* principles.

Question:

> Why are we doing what we do?

---

### Memory

Describes:

* historical context,
* important decisions,
* preferences,
* durable constraints.

Question:

> What must we remember?

---

### Knowledge

Describes:

* validated truths,
* lessons learned,
* confirmed patterns.

Question:

> What have we learned?

---

### Timeline

Describes:

* events,
* decisions,
* outcomes.

Format:

Event → Decision → Outcome

Question:

> What happened?

---

## A2 — Execution

These concepts enable action.

Without them FounderHQ survives but becomes unable to execute effectively.

### Project

Work in progress.

Question:

> What are we building?

---

### Workflow

Reproducible processes.

Question:

> How to execute a task?

---

### Asset

Assets.

Question:

> What do we own?

Examples:

* products,
* brands,
* domains,
* databases,
* audiences.

---

### Playbook

Validated methods.

Condition:

Must be demonstrated multiple times across multiple contexts.

Question:

> What works reliably?

---

### System

Documentation of FounderHQ's internal functioning.

Question:

> How does FounderHQ work?

---

# Layer 2 — Protocols

Protocols define expected behavior.

They answer the question:

> How should FounderHQ operate?

---

## FounderOS Protocol

Startup sequence.

Boot.

Loading.

Order of operations.

---

## Decision Gates

Determines:

* what type of decision is requested,
* which concepts must be consulted,
* which frameworks must be loaded.

---

## Temporal Awareness

Manages:

* time,
* freshness,
* age of information.

Every decision must be time-aware.

---

## Relationship Model

Describes:

* dependencies,
* relationships,
* connections.

Between all concepts.

---

## Source Of Truth

Fundamental rule.

Every truth has a single owner.

No duplication.

---

## Prioritization Protocol

Determines:

> What is the next most important action?

---

# Layer 3 — Frameworks

Frameworks are lenses for thinking.

They store no data.

They are not concepts.

They are not protocols.

They answer the question:

> How to analyze this problem?

They can be replaced without destroying FounderHQ.

---

## Core Frameworks

### CAOS

Financial analysis.

Cash.

Allocation.

Survival.

---

### CEOS

Content analysis.

Conversion.

Audience.

Distribution.

---

### PSOS

Product analysis.

Offer.

Positioning.

Value.

---

### FAOS

Acquisition analysis.

Funnel.

Growth.

Traffic.

---

### SAOS

Systemic analysis.

Components.

Boundaries.

Bottlenecks.

Removal cost.

Reconstruction.

---

# Layer 4 — State

The present.

Current snapshot.

Contains:

* current priority,
* main bottleneck,
* immediate context,
* operational status.

This layer is temporary.

It can be deleted and reconstructed.

---

# Layer 5 — Runtime

The execution engine.

Examples:

* OpenCode,
* Cursor,
* Claude Code,
* ChatGPT,
* Gemini,
* future system.

FounderHQ depends on no particular runtime.

The runtime simply implements the expected interface.

---

# Layer 6 — Archive

History.

Previous versions.

Old frameworks.

Past decisions.

Never an active source of truth.

---

# Fundamental Rule

Every piece of information has exactly one owner.

Example:

Product price:

Asset.

Not elsewhere.

Cash:

State.

Not elsewhere.

Validated lesson:

Knowledge.

Not elsewhere.

Event:

Timeline.

Not elsewhere.

Any duplication constitutes a violation.

---

# Reconstruction

If all files are lost:

An LLM must be able to reconstruct FounderHQ from this description.

The mandatory elements to reconstruct are:

* Concepts,
* Protocols,
* Frameworks,
* State,
* Runtime Interface,
* Archive.

Exact file names may change.

Exact folder structure may change.

The concepts must never change.

---

# Success Criterion

FounderHQ is successful when:

* knowledge accumulates,
* decisions improve,
* playbooks emerge,
* projects advance,
* results are traceable,
* the system survives the replacement of the LLM.

The system must become more intelligent every year even if all tools change.


--- FILE: RUNTIME.md

# FounderOS V4 — RUNTIME

## Purpose

The RUNTIME defines the daily operating loop and contains operational reference material for FounderOS V4.

## Daily Operating Loop

### Phase 1: Assess (1-2 minutes)

1. Load CURRENT_STATE.md
2. Check cash position
3. Review TIMELINE.md for recent events (last 24h)
4. Identify what changed since last session
5. Determine the single most important thing to do today

### Phase 2: Decide (2-5 minutes)

1. Run situation through DECISION_GATES
2. Ask: What action has the highest mission impact per unit of effort?
3. Ask: Does this action require escalation?
4. Ask: Is there a playbook for this situation? (Check PLAYBOOK.md)
5. Select one action. Execute it.

### Phase 3: Execute (variable)

1. Load the relevant module if needed (MOS, DAOS, etc.)
2. Execute the action
3. Document the result in TIMELINE.md (Event → Decision → Outcome)
4. Update any affected files

### Phase 4: Learn (1-2 minutes)

1. What worked? Store in KNOWLEDGE.md
2. What didn't? Store in KNOWLEDGE.md
3. Is there a pattern? Run PATTERN_ENGINE
4. Is there a new playbook? Update PLAYBOOK.md

### Phase 5: Prepare (1 minute)

1. Update CURRENT_STATE.md for next session
2. Note what the next session should prioritize
3. Store any cross-session concerns in MEMORY.md

## Loop Characteristics

- Loop completes in 5-20 minutes depending on action complexity
- If time is limited, truncate: Assess → Decide → Execute → Prepare
- If blocked on an action, document the block in CURRENT_STATE.md and move to next-highest-leverage action
- Never spend more than 2 minutes assessing without acting

## When to Skip the Loop

- User gives a direct instruction: execute it, then loop
- Reconstruction session: rebuild first, then loop
- Emergency (cash crisis, deadline): execute crisis playbook, then loop

## Energy Management

- One major action per session maximum
- Multiple small actions (file updates, checks) are fine
- If the user seems tired or scattered, recommend stopping after one good action
- Quality over quantity: one executed action > five discussed actions

---

## Temporal Awareness

Time is a first-class operational dimension. Reality is not static — it is state evolving through time.

### Before Every Response

Query the system clock (Get-Date). Determine current date AND time. Verify timezone — do NOT assume it matches the user's. Use [System.TimeZoneInfo]::Local.GetUtcOffset((Get-Date)) to detect actual offset. Convert to Lome time (UTC+0). No DST in West Africa Time.

### Required Temporal Markers

Every operational session must establish:
- CURRENT_DATETIME
- CURRENT_TIMEZONE
- ELAPSED_SINCE_LAST_SESSION
- AGE_OF_MEMORY
- AGE_OF_KNOWLEDGE
- AGE_OF_TIMELINE

### State Aging

Every piece of information has an age measured from last update to current time:

| Age | Confidence | Action |
|-----|-----------|--------|
| < 1 day | High | Use as is |
| 1-7 days | Medium | Flag if critical |
| 7-30 days | Low | Verify before use |
| 30-90 days | Very low | Reconstruct if possible |
| > 90 days | Minimal | Treat as historical reference only |

A state without a timestamp is treated as maximally stale.

### Staleness Thresholds

- PROJECT not updated for 45 days → flag as possibly abandoned
- MEMORY not reviewed for 14 days → flag as potentially inaccurate
- MISSION not reviewed for 90 days → flag as potentially obsolete
- DECISION without follow-up for 30 days → flag for review
- KNOWLEDGE entry older than 1 year without revalidation → flag as unvalidated

### Timeline Operations

Recording: Every significant event in TIMELINE.md with date, description, affected concepts, cause.
Reading: Scan TIMELINE reverse chronological. Events > 90 days may be summarized.
Reconstruction: If TIMELINE missing, reconstruct from PROJECT + MEMORY + KNOWLEDGE dates. Mark entries as approximate.

### Period Awareness

Understand position within: TODAY, THIS_WEEK, THIS_MONTH, THIS_QUARTER, THIS_YEAR. Each boundary triggers: review goals, assess progress, decide to continue/adjust/abandon.

### Temporal Reports

Generate on request:
- STALE_STATE_REPORT — concepts exceeding age thresholds
- ACTIVITY_REPORT — changes over a specified period
- TIMELINE_SUMMARY — condensed history over a period
- AGING_KNOWLEDGE_REPORT — entries not revalidated within threshold

### Consistency Rules

1. Never treat old information as current without verification
2. Never present a stale state as if it were fresh
3. Never make a time-sensitive recommendation without checking current time
4. Never assume a previous session's context applies to the current session
5. Always state the date when information age is relevant
6. Always flag when a decision or priority exceeds its expected lifespan

### Edge Cases

No clock available: State explicitly. Estimate from file modification dates. Mark conclusions as approximate.
Timezone change: Record new timezone. Normalize stored times to UTC. Display in user's current timezone.
Gap in timeline: Note the gap. Check other concepts for events. If none found, mark as unknown.

---

## Operational Principles

### Mission Alignment
Before any significant action, ask: What mission does this support? If no mission exists or the action does not serve a mission, do not execute it.

### Verification
Verify before asserting. If unsure: read the relevant concept, check TIMELINE for evidence, check SOURCE_OF_TRUTH.md for the owner, ask the user. Do not generate unverified information.

### Leverage
Prevent: solving the same problem twice, repeating the same recommendation, producing output that will not be used. Seek: highest mission impact per unit of effort, reusable assets, compounding knowledge.

### Cash Awareness
If cash is below 1,500 FCFA, prioritize revenue-generating actions above all else.

### Execution Constraints
- Always load CURRENT_STATE.md before acting on any operational matter
- Always verify the most recent version of a file before using cached knowledge
- If data is older than 48 hours, flag as stale — do not act without reverification

---

## Quality Standards

Every output must be:
1. **Accurate** — based on loaded data, verified against concepts
2. **Timely** — aware of current date, time, and state freshness
3. **Aligned** — serves at least one mission
4. **Concrete** — leads to action or clarity, not just information

If an output cannot meet these standards, state why.

## Interaction Style

Be direct. Be concise. Do not ask "How can I help?" without context — you have context. Do not suggest actions that waste time. Do not produce output the user did not ask for unless it serves a mission.

When the user asks a question, determine:
- Does this answer already exist in KNOWLEDGE?
- Does this require a decision?
- Does this require an action?
- Does this require external research?

## Error Handling

**Cannot load a concept:**
1. Check if it exists in a different representation
2. Check if it can be reconstructed from other concepts
3. Consult SOURCE_OF_TRUTH.md for the expected location
4. Report what is missing and proceed with what is available

**Contradictory information:**
1. Read SOURCE_OF_TRUTH.md to identify the owner of each truth
2. The owner document wins for that truth
3. Flag the contradiction
4. Correct the non-owner document

**Invariant violation request:**
1. State the invariant
2. Explain why the action would violate it
3. Suggest an alternative

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Purpose | Operational reference for FounderOS runtime. Contains Temporal Awareness, Principles, Quality Standards, Interaction Style, Error Handling. |
| Dependencies | SYSTEM_PROMPT.md, Protocols/SOURCE_OF_TRUTH.md, Protocols/DECISION_GATES.md, State/CURRENT_STATE.md |


--- FILE: Protocols/DECISION_GATES.md

# DECISION_GATES

## Concept

Decision Gates enforce FounderHQ's execution discipline.

Before every action, the agent must identify the action type, load the required concepts, verify their freshness, and only then respond.

Without gates, FounderHQ is a library.

---

## How Gates Work

```
Action Request
    ↓
Identify Action Type (match the request to a gate below)
    ↓
LOAD required concepts (read them in the current session)
    ↓
LOAD optional frameworks (if applicable — read the lens)
    ↓
VERIFY freshness (is each concept older than its max age?)
    ↓
CHECK escalation level — does this action require founder approval?
    ↓
APPLY lens framework (answer the lens questions in context)
    ↓
APPLY PRIORITIZATION_PROTOCOL (is this the right action NOW?)
    ↓
Respond (or escalate with options)
```

**Escalation check:** If the action involves Financial, Legal, Security, Hiring, Equity, External Communications, or Personal Data — escalate to founder regardless of gate type.

**Failure mode:** If a required concept is stale (> max age), flag it before responding. Do not proceed without current data.

---

## Universal Action Types

### 1. Strategic

**Triggers:** "What should I do?", "What's the priority?", "Which direction?", "Define next action", "How to allocate time?"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `State/CURRENT_STATE.md` — Cash, Bottleneck, Priority, Last Decision (real-time)
- `Concepts/TIMELINE.md` — Last 7 days events (max 14 days)
- `Concepts/PROJECT.md` — Active projects, Status, Next Action (max 7 days)

**Optional Frameworks:**
- CAOS — Allocation hierarchy, survival protocol
- SAOS — System analysis, bottleneck identification

---

### 2. Financial

**Triggers:** "Set a price", "Create an offer", "Discount", "Budget", "Spend money", "Investment decision"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `State/CURRENT_STATE.md` — Cash, Active Product (real-time)
- `Concepts/ASSET.md` — Product cost, Margin, Supplier data (max 30 days)

**Optional Frameworks:**
- CAOS — Capital preservation, allocation hierarchy
- FAOS — Capital sourcing, runway analysis

---

### 3. Product

**Triggers:** "Define a product", "Validate an offer", "Position a product", "Feature decision", "Product pivot"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — Relevant product knowledge (max 14 days)
- `Concepts/ASSET.md` — Existing products, inventory, supply chain (max 30 days)

**Optional Frameworks:**
- PSOS — Product strategy, positioning, validation

---

### 4. Content

**Triggers:** "Write a script", "Create a video", "Write a post", "Propose a hook", "Design a CTA", "Plan content"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — Content principles, audience tactics, offer design (max 14 days)
- `Concepts/WORKFLOW.md` — WF-001 Video Production (max 30 days)
- `State/CURRENT_STATE.md` — Cash, Active Product, Top Priority, Bottleneck (real-time)

**Optional Frameworks:**
- CEOS — Hook analysis, conversion strategy, distribution
- MAOS (Content/) — Marketing campaign planning, audience acquisition
- AI_VIDEO_MASTER_DOMAIN (AI/) — Entity-based video production pipeline

---

### 5. Operational

**Triggers:** "Execute a process", "Run a workflow", "Follow a procedure", "Checklist execution"

**Required Concepts:**
- `Concepts/WORKFLOW.md` — Relevant workflow(s) (max 30 days)
- `State/CURRENT_STATE.md` — Current priority, bottleneck (real-time)

**Optional Frameworks:**
- None (workflows are self-contained)

---

### 6. Research

**Triggers:** "Research a topic", "Analyze a market", "Investigate a competitor", "Explore an opportunity"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — What we already know (max 14 days)

**Optional Frameworks:**
- SAOS — System analysis, dependency mapping
- PSOS — Opportunity evaluation

---

### 7. Learning

**Triggers:** "Learn a skill", "Study a field", "Read a resource", "Take a course"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — What we already know (max 14 days)

**Optional Frameworks:**
- PSOS — Learning Principle: learn → apply → build → validate

---

### 8. Creative

**Triggers:** "Brainstorm ideas", "Generate concepts", "Create something new", "Explore a creative direction"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/ASSET.md` — Brand guidelines, existing assets (max 30 days)

**Optional Frameworks:**
- CEOS — Audience alignment
- PSOS — Leverage principle
- AI_VIDEO_MASTER_DOMAIN (AI/) — Video production concepts, entity framework

---

### 9. Technical

**Triggers:** "Build something", "Configure a tool", "Set up a system", "Write code", "Fix a technical issue"

**Required Concepts:**
- `Concepts/WORKFLOW.md` — Relevant workflow (max 30 days)
- `Concepts/KNOWLEDGE.md` — Relevant technical knowledge (max 14 days)

**Optional Frameworks:**
- SAOS — System analysis, bottleneck identification
- AAOS (AI/) — Automation design, agent architecture

---

### 10. Relationship

**Triggers:** "Contact someone", "Send a message", "Network", "Partnership outreach", "Hire", "Collaborate"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/PROJECT.md` — Current projects, relevant context (max 7 days)

**Optional Frameworks:**
- FAOS — Capital hierarchy (relationships as capital)
- PSOS — Trust principle

---

## Gate Bypass Rule

If no action type matches the request, classify by intent:

- "Decide what to do" → Strategic
- "Spend/create with money" → Financial
- "Make something for others" → Content or Product
- "Follow a procedure" → Operational
- "Learn something" → Learning or Research
- "Build/create technically" → Technical

When in doubt, use Strategic.

---

## Footer

Version: V2 — Universal taxonomy (10 types). Frameworks: 8 actifs (CAOS, CEOS, PSOS, FAOS, SAOS, MAOS, AAOS, AI_VIDEO_MASTER_DOMAIN), 3 experimental (PMOS, RIOS, LEOS). Integre PRIORITIZATION_PROTOCOL.

Gates are enforced by the agent at boot. There is no other gatekeeper.

If a gate is skipped, the action is unconstrained. That is the system's failure mode.

If you skip a gate, flag it: "⚠️ GATE SKIPPED: [action type] — response may be unconstrained."


--- FILE: Protocols/INFO_CAPTURE_PROTOCOL.md

# INFO CAPTURE PROTOCOL

## Purpose

Any operational information given in conversation is automatically captured in FHQ. This protocol defines which type of info goes into which file, without waiting for explicit instruction.

## Fundamental Rule

**If the info is useful to a future session, it must be written now.**

Do not ask "do you want me to save it?" — save it directly.

---

## Mapping Type → File

| Information Type | Example | Target File | Action |
|-------------------|---------|--------------|--------|
| **Deadline / cutoff date** | "June 22 at 4:59 PM" | State/PRIORITY_MATRIX.md | Update deadline + warning 🔴 |
| **Project progress** | "I finished 1.1 Debt vs Equity" | State/CURRENT_STATE.md + State/PRIORITY_MATRIX.md | Update status section + dashboard |
| **New project** | "I'm launching Omni" | Apply PROJECT_REGISTRATION_PROTOCOL.md | Create concept/ + projects/ + all links |
| **Decision** | "We're going with Innov'Action not Idée-Action" | State/CURRENT_STATE.md + relevant concepts | Update Last Decision |
| **Figure / metric** | "Collection 4,875 FCFA" | State/CURRENT_STATE.md | Update Cash + product info |
| **Blockage** | "Supplier no update" | State/PRIORITY_MATRIX.md | Set warning 🟡/🔴 |
| **Important event** | "Herlog sent" | TIMELINE.md | Record Event → Decision → Outcome |
| **New relationship** | "OMNI linked to KORA" | Relevant concepts | Add bidirectional link |
| **Preference / rule** | "Always track both" | Protocols/INFO_CAPTURE_PROTOCOL.md | Add the rule |
| **Watch information** | "Websearch result X" | State/WATCH_REGISTRY.md | Update Last Result + Next Check |

---

## Concrete Cases (recent examples)

| What you said | What was captured | Where |
|-----------------|---------------------|-----|
| "I just finished 1.1 Debt vs Equity" | Financial Literacy 1.1 → ✅ | State/CURRENT_STATE.md + State/PRIORITY_MATRIX.md |
| "company not yet registered" | Omni company status corrected | projects/Omni/annexes/A4_DJANTA_TECH_HUB.md |
| "omni should be in innov action" | Program confirmed | concepts/OMNI.md + annexes A4 |
| "why don't you track all my goals" | PRIORITY_MATRIX.md created | New file |

---

## What Is NOT Captured

- Questions without operational answers
- Unconfirmed exploratory thoughts
- Conversations not related to FHQ (unless an emergent pattern)

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | System |


--- FILE: Protocols/PRIORITIZATION_PROTOCOL.md

# PRIORITIZATION PROTOCOL

## Concept

Among 100 possible actions, which is the only one worth doing now?

This protocol answers that question.

There are no multiple "priorities." There is ONE priority at a time.

---

## Fundamental Rule

The bottleneck is the single constraint preventing the entire system from moving forward.

If we resolve the bottleneck, the whole system progresses.

If we work on something else, we are busy but not making progress.

---

## Decision Tree

### Step 1: Current State

1. Cash > 0 ?
   - NO → Absolute priority: generate revenue. Everything else is secondary.
   - YES → continue.

2. Is a product on sale?
   - NO → Priority: put a product on sale. A product that doesn't exist cannot generate revenue.
   - YES → continue.

3. Does the product have customers?
   - NO → Priority: acquire the first customer. Distribution is the bottleneck.
   - YES → continue.

4. Are existing customers satisfied?
   - NO → Priority: resolve customer issues. Retention before acquisition.
   - YES → continue.

5. Has the product reached product-market fit?
   - NO → Priority: iterate until customers come back or refer others.
   - YES → Scale.

### Step 2: Load Context

Read the following concepts to verify the decision tree:

- State/CURRENT_STATE.md (cash, bottleneck, current priority)
- Concepts/MISSION.md (strategic direction)
- Concepts/TIMELINE.md (recent events)

### Step 3: Apply the Lens

If DECISION_GATES recommends a framework, load it and apply its questions to the context.

### Step 4: Reduce to ONE Action

Ask the question:

```
If I do only one thing today,
which one has the greatest impact on the bottleneck?
```

If the answer is vague, the question was not specific enough.

Rephrase until you get ONE concrete action.

---

## Verification

Before starting the action, verify:

- [ ] Does this action directly serve the identified bottleneck?
- [ ] Is this action the highest leverage available?
- [ ] Can this action be executed in the available time?
- [ ] Is this action not busywork disguised as progress?

If all 4 answers are "yes" → execute.
If any answer is "no" → re-evaluate.

---

## Anti-patterns

- Working on 3 priorities at the same time (none truly progresses)
- Choosing an easy action instead of an impactful one
- Confusing urgency with importance
- Planning without executing
- Re-prioritizing before completing the current priority
- Using planning as an escape from execution

---

## Integration with DECISION_GATES

When an action type is identified via DECISION_GATES, PRIORITIZATION_PROTOCOL ensures it is the RIGHT action to do now.

Both protocols work in sequence:

```
DECISION_GATES     →  What to do?
PRIORITIZATION     →  What to do NOW?
```


--- FILE: Protocols/SOURCE_OF_TRUTH.md

# SOURCE OF TRUTH

## Rule 0

Every system truth has EXACTLY one owner.

If two documents contain the same truth → violation.
If a document contains a truth it does not own → violation.

## Truth Map

| Truth | Owner |
|--------|-------------|
| Mission, vision, principes strategiques | concepts/MISSION.md |
| Projets actifs, statut, outcome attendu | concepts/PROJECT.md |
| Etat operationnel actuel | State/CURRENT_STATE.md |
| Bridge file. Background script alerts read and cleared at boot. | State/Scripts->LLM/ALERTS.md |
| Temporal hierarchy (life->year->month->week->day->hour). Session timestamps. | State/System/CADENCE.md |
| Per-project lifecycle phase. Gates. Framework mapping. | State/System/LIFECYCLE.md |
| Veille findings from watchtower, consumed at boot. | State/watchtower.py/WATCH_REPORT.md |
| Prix, cout, stock, marques, audiences | concepts/ASSET.md |
| Contacts fournisseurs (tel, email, termes) | concepts/ASSET.md |
| Comptes reseaux sociaux, chaines YouTube | concepts/ASSET.md |
| Lecons validees, patterns confirmes | concepts/KNOWLEDGE.md |
| Pipeline contenu YouTube doodle long-form | concepts/KNOWLEDGE.md (KnowledgeAssets/) |
| Pipeline Shorts viraux doodle | concepts/KNOWLEDGE.md (KnowledgeAssets/) |
| Evenements, decisions, outcomes | concepts/TIMELINE.md |
| Processus, etapes d'execution | concepts/WORKFLOW.md |
| Methodes validees (3+ contextes differents) | concepts/PLAYBOOK.md |
| Fonctionnement interne de FounderHQ | concepts/SYSTEM.md |
| Historique des decisions (contexte, raison, resultat) | concepts/TIMELINE.md |
| Quand charger quel framework | Protocols/DECISION_GATES.md |
| Demarrage et sequence de boot, execution modes, permissions | SYSTEM_PROMPT.md |
| Heure, age des informations, fraicheur | SYSTEM_PROMPT.md |
| Detection de fraicheur des concepts | concepts/WORKFLOW.md (WF-007) |
| Graphe de dependances entre concepts | Protocols/RELATIONSHIP_MODEL.md |
| Priorisation : quoi faire MAINTENANT | Protocols/PRIORITIZATION_PROTOCOL.md |
| Marketing, campaigns (lens) | Frameworks/Content/MAOS.md |
| Automation, agents (lens) | Frameworks/AI/AAOS.md |
| Video production entities (lens) | Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md |
| Master entry point, identity, primary directive | SYSTEM_PROMPT.md |
| Classification automatique des intentions, routage des modules | SYSTEM_PROMPT.md |
| Session mode, permissions, constraints, integrity check | SYSTEM_PROMPT.md |
| Daily operating loop (Assess → Decide → Execute → Learn → Prepare) | RUNTIME.md |
| Mission orchestration, priorities | MOS.md |
| Daily execution, action modules | DAOS.md |
| Strategic vision, long-term thinking | VEAOS.md |
| Content engineering, video production | CEOS.md |
| Reflection, clarity, pattern awareness | ASTRA.md |
| Knowledge management, hygiene | KMOS.md |
| Learning pipeline, knowledge gaps | LEOS.md |
| External research, intelligence | RIOS.md |
| Fundraising, revenue, alliances | FAOS.md |
| Founder wellbeing, energy, mindset | SOS.md |
| OS architecture, coherence, audits | AOS.md |
| Structured decision-making (PROACT) | DECISION_ENGINE.md |
| Pattern detection across actions/outcomes | PATTERN_ENGINE.md |
| Playbook creation, validation, evolution | PLAYBOOK_ENGINE.md |
| Long-term knowledge evolution, decay | KNOWLEDGE_EVOLUTION_ENGINE.md |
| Meta-improvement of FounderOS itself | CONTINUOUS_IMPROVEMENT.md |
| Complete video production system | AI_VIDEO_MASTER_DOMAIN.md |
| FRE: runtime constitution and system contracts | Runtime/FRE_SPEC.md |
| FRE: universal execution cycle (BOOT → OBSERVE → ORIENT → DECIDE → ACT → LEARN → UPDATE) | Runtime/RUNTIME_KERNEL.md |
| FRE: adapter interface contract (4 mandatory questions) | Runtime/ADAPTER_INTERFACE.md |
| Distribution intelligence, audience, language, platform strategy | Frameworks/Specialized/Distribution/DIOS.md |
| Distribution: audience segmentation and targeting | Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md |
| Distribution: language-market derivation and cultural adaptation | Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md |
| Distribution: platform selection by audience behavior | Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md |
| Distribution: hook creation and testing | Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md |
| Distribution: offer design and presentation | Frameworks/Specialized/Distribution/DIOS/OFFER_INTELLIGENCE.md |
| Distribution: rhythm, cross-posting, campaign structure | Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_INTELLIGENCE.md |
| Distribution: CTA design, objection handling, WhatsApp closing | Frameworks/Specialized/Distribution/DIOS/CONVERSION_INTELLIGENCE.md |
| Distribution: campaign memory and learning loop | Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_MEMORY.md |
| Venture architecture, venture creation and structuring | Frameworks/Specialized/Venture/VAOS.md |
| Venture: vision definition and reality transformation | Frameworks/Specialized/Venture/VAOS/VISION_ENGINE.md |
| Venture: mission definition and approach | Frameworks/Specialized/Venture/VAOS/MISSION_ENGINE.md |
| Venture: theory of change and causal logic | Frameworks/Specialized/Venture/VAOS/THEORY_OF_CHANGE.md |
| Venture: strategic asset inventory and gap analysis | Frameworks/Specialized/Venture/VAOS/ASSET_MAPPING.md |
| Venture: strategic planning and bet sequencing | Frameworks/Specialized/Venture/VAOS/STRATEGIC_PLANNING.md |
| Venture: roadmap with phase gates and milestones | Frameworks/Specialized/Venture/VAOS/ROADMAP_ENGINE.md |
| Venture: capital strategy and funding sources | Frameworks/Specialized/Venture/VAOS/CAPITAL_STRATEGY.md |
| Venture: business plan generation from VAOS cascade | Frameworks/Specialized/Venture/VAOS/BUSINESS_PLAN_ENGINE.md |
| Venture: constraint analysis and bottleneck identification | Frameworks/Specialized/Venture/VAOS/CONSTRAINT_ANALYSIS.md |
| Venture: repositioning and venture repair | Frameworks/Specialized/Venture/VAOS/VENTURE_REPOSITIONING.md |
| Campaign performance data, hook/audience/language history | concepts/DISTRIBUTION_MEMORY.md |
| First-time setup procedure | GENESIS.md |
| Installation guide, troubleshooting | INSTALL.md |
| Archives V3/V4 (KERNEL, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS) | ARCHIVE/V4/ |
| Gist-based sync (pull/push/merge) | Runtime/engine/sync.py |
| Portable markdown snapshot (no token) | Runtime/engine/snapshot.py |
| Secrets (GitHub token — NEVER read by LLM) | .env |
| First-run installation marker | .founderhq_installed |
| Single-file distribution of all core files | FOUNDER_SEED.md |
| Ce fichier (carte des verites) | Protocols/SOURCE_OF_TRUTH.md |

## Maintenance Rule

If a new truth is added to the system, we must:
1. Determine its unique owner
2. Add it to this map
3. Verify that no other document already owns it


--- FILE: Protocols/RELATIONSHIP_MODEL.md

# RELATIONSHIP MODEL

## Purpose

Define how FounderHQ concepts relate to each other.

FounderHQ is a graph of concepts, not a tree of folders.

Concepts have meaning through their relationships, not their position in a hierarchy.

---

## Core Principle

A concept references another concept.

A concept does not contain another concept.

If information exists in the space between two concepts, the relationship is documented but the information belongs to exactly one concept.

---

## Concept Graph

```
MISSION
  │
  │ supports ──────────────────────┐
  ▼                                │
PROJECT ── generates ──────────► KNOWLEDGE
  │                                │
  │ recorded_in                    │ informs
  ▼                                ▼
TIMELINE                        PLAYBOOK
                                  │
                                  │ optimizes
                                  ▼
                              WORKFLOW
                                  │
                                  │ executed_by
                                  ▼
                              PROJECT
                                  │
                                  │ produces
                                  ▼
                              ASSET
                                  │
                                  │ supports
                                  ▼
                              PROJECT
                                  │
                                  │ tracked_in
                                  ▼
                              TIMELINE

SYSTEM governs all concepts.
MEMORY holds current context for all concepts.
```

---

## Relationship Types

### supports

**From:** MISSION → PROJECT

**Meaning:** This project exists to advance this mission.

**Rule:** Every project must support at least one mission. If a project does not support any mission, it should not exist.

**Cardinality:** A mission may support many projects. A project may support many missions.

---

### generates

**From:** PROJECT → KNOWLEDGE

**Meaning:** This project produced validated lessons, patterns, or principles.

**Rule:** When a project completes, any validated learning must be stored in KNOWLEDGE. The project references the knowledge. It does not contain it.

**Cardinality:** A project may generate zero or many knowledge entries. A knowledge entry may be generated by one or many projects.

---

### recorded_in

**From:** PROJECT → TIMELINE

**Meaning:** Events related to this project are recorded in TIMELINE.

**Rule:** A project does not maintain its own chronology. All chronological events belong in TIMELINE, tagged with the PROJECT_ID.

**Cardinality:** A project may have many timeline entries. A timeline entry references exactly one project (or zero for system-level events).

---

### informs

**From:** KNOWLEDGE → PLAYBOOK

**Meaning:** This knowledge provides the evidence base for this playbook.

**Rule:** A playbook must cite the knowledge entries that validate its strategy.

**Cardinality:** One knowledge entry may inform zero or many playbooks. One playbook may be informed by many knowledge entries.

---

### optimizes

**From:** PLAYBOOK → WORKFLOW

**Meaning:** This playbook provides the strategy that this workflow implements.

**Rule:** A workflow may reference a playbook for strategic guidance. The workflow contains step-by-step execution. The playbook contains the reasoning.

**Cardinality:** A playbook may optimize many workflows. A workflow may be optimized by at most one playbook.

---

### executed_by

**From:** WORKFLOW → PROJECT

**Meaning:** This project uses this workflow to execute.

**Rule:** When a project uses a workflow, it references the workflow. It does not copy the workflow steps.

**Cardinality:** A workflow may be executed by many projects. A project may use many workflows.

---

### produces

**From:** PROJECT → ASSET

**Meaning:** This project produced this reusable asset.

**Rule:** An asset may outlive the project that created it.

**Cardinality:** A project may produce zero or many assets. An asset may be produced by exactly one project.

---

### uses

**From:** PROJECT → ASSET

**Meaning:** This project uses this asset as a resource.

**Rule:** A project may use assets created by other projects. Asset ownership does not restrict usage.

**Cardinality:** A project may use many assets. An asset may be used by many projects.

---

### tracked_in

**From:** PROJECT → TIMELINE (reverse of recorded_in)

**Meaning:** This project's progress is visible in TIMELINE entries.

**Rule:** Same as recorded_in — bidirectional for convenience.

---

## Framework Relationships

```
DECISION_GATES
  │
  │ references
  ▼
FRAMEWORKS/Core/CAOS.md
FRAMEWORKS/Core/CEOS.md
FRAMEWORKS/Core/PSOS.md
FRAMEWORKS/Core/FAOS.md
FRAMEWORKS/Core/SAOS.md
```

**From:** DECISION_GATES → Frameworks

**Meaning:** DECISION_GATES determines which framework lens to load based on action type.

**Rule:** Frameworks are loaded on demand. They are not boot-level concepts. They are specialized thinking tools invoked by DECISION_GATES.

---

## Runtime Relationships

```
Runtime/RUNTIME_INTERFACE.md
  │
  │ implemented_by
  ▼
Runtime/opencode/
Runtime/chatgpt/
Runtime/claude/

**From:** Runtime/RUNTIME_INTERFACE → Runtime Adapters

**Meaning:** Each runtime adapter implements the interface defined in Runtime/RUNTIME_INTERFACE.md.

**Rule:** FounderHQ does not depend on any specific runtime. Any runtime that satisfies the interface can operate FounderHQ.

---

## State Relationships

```
State/CURRENT_STATE.md
  │
  │ referenced_by
  ▼
DECISION_GATES
FOUNDEROS_PROTOCOL
Concepts/MISSION
Concepts/MEMORY
Concepts/PROJECT
```

**From:** CURRENT_STATE → all concepts and protocols

**Meaning:** CURRENT_STATE is the single source of operational truth. Every action depends on it.

**Rule:** CURRENT_STATE is loaded every session. If stale, it must be re-verified.

---

## Non-Concept Relationships

Some relationships involve documents or external entities, not concepts.

### references

**Used when:** A concept needs to point to a specific file, URL, or resource that is not itself a concept.

**Example:** PROJECT.RELATED_ASSETS may reference a file path in `Projects/Stop Nuisibles/CONTENT/`

### depends_on

**Used when:** A project cannot proceed until another project completes.

**Example:** SN-002 (Variation #2) must complete before SN-003 (Video 2) applies its learnings.

---

## Relationship Integrity Rules

### Rule 1: A reference does not duplicate

If PROJECT says `RELATED_KNOWLEDGE: KNOWLEDGE — Video Content Principles`, the knowledge must NOT also be copied into PROJECT.

### Rule 2: Orphan prevention

If a concept is referenced, it must exist. A PROJECT that links to MISSION must point to a mission that exists in MISSION.md.

### Rule 3: Relationship decay

If a relationship is not used for 90 days (e.g., a PROJECT links to a PLAYBOOK but the PLAYBOOK is never updated), flag the relationship for review.

### Rule 4: No implicit relationships

Every relationship must be documented. If PROJECT generates KNOWLEDGE, the link must appear in both PROJECT and KNOWLEDGE.

---

## Example Relationship Chain

```
MISSION: Stop Nuisibles
  │
  │ supports
  ▼
PROJECT: SN-002 (Variation #2)
  │
  │ generates ─────────────► KNOWLEDGE: "Passive audio hook causes 0:03 drop"
  │                              │
  │ recorded_in                  │ informs
  ▼                              ▼
TIMELINE: 2026-06-18        PLAYBOOK: TikTok Hook Structure
                                  │
                                  │ optimizes
                                  ▼
                              WORKFLOW: Video Production Pipeline
                                  │
                                  │ executed_by
                                  ▼
                              PROJECT: SN-003 (Video 2)
```

---

## Future: Machine-Readable Relationships

When FounderHQ reaches sufficient maturity, relationships may be stored in a machine-readable format (JSON, YAML, or graph database).

Until then, relationships are documented in plain text within each concept file.

The relationship model remains valid regardless of storage format.

---

## Footer

This model defines how concepts coexist without merging.

If two concepts share a relationship that is not listed here, the relationship either does not exist or belongs in a different concept.

If a relationship seems to require data duplication, the boundaries between the two concepts are wrong.


--- FILE: Protocols/PROJECT_REGISTRATION_PROTOCOL.md

# PROJECT REGISTRATION PROTOCOL

## Purpose

Ensure every new project added to FounderHQ is fully integrated across ALL relevant files. This protocol is executed once per new project. No file should be left behind.

## Scope

This covers ALL projects regardless of type: ventures (KORA, Omni), products (Soya, Pest Repeller, DoodleMind), partnerships, or experimental.

---

## Registration Checklist

### 1. Create Concept File

`concepts/<PROJECT>.md`

Template:
```markdown
# FounderOS V4 — <PROJECT> (Tagline)

## Purpose

[One paragraph: why this project exists.]

## Position in FounderHQ

[One paragraph: how it relates to other projects.]

## Status

| Field | Value |
|---|---|
| Phase | [Phase] |
| Activity | Active / Standby / Archived |
| Priority | High / Medium / Low |

## Quick Reference

| Document | Location |
|---|---|
| Main docs | `projects/<PROJECT>/` |

## Relations

[Links to other concepts/projects]

## Footer
```

### 2. Create Project Data Room

`projects/<PROJECT>/` with the full **strategic cascade** (defined below).

#### Strategic Cascade (10 files + annexes)

Every project data room MUST contain the following numbered files, plus annexes:

| # | File | Purpose |
|---|------|---------|
| 01 | `01_VISION.md` | Long-term vision (10-20 year horizon) |
| 02 | `02_MISSION.md` | Mission, purpose, what we do / don't do |
| 03 | `03_THEORY_OF_CHANGE.md` | How vision becomes reality; causal chain |
| 04 | `04_STRATEGIC_ASSETS_MAP.md` | Assets accumulated, competitive moats |
| 05 | `05_MASTER_PLAN.md` | Strategic plan, layers, principles |
| 06 | `06_STRATEGIC_ROADMAP.md` | Timeline, phases, milestones |
| 07 | `07_CAPITAL_ROADMAP.md` | Funding needs, sources, use of funds |
| 08 | `08_EXECUTIVE_SUMMARY.md` | 1-page summary for stakeholders |
| 09 | `09_BUSINESS_PLAN.md` | Full business plan (problem, market, model, risks) |
| 10 | `10_PITCH_DECK.md` | Slide-by-slide pitch presentation |
| - | `annexes/` | Supporting docs (contacts, pricing, research) |
| - | `README.md` | Project overview, status, quick links |

**Template:** For format and tone, reference existing project data rooms (`projects/Omni/`, `projects/KORA/`). The cascade follows the same structure regardless of project size — a cash project like SOJACO will have leaner content within the same file structure.

### 3. Update CURRENT_STATE.md

Add to:
- **Active Products** list (line ~61-65)
- **<PROJECT> Status** section (after existing status blocks)
- **Top Priority** — merge if project has deadline
- **Session Objective** — if active

### 4. Update PRIORITY_MATRIX.md

Add row to **Projets Actifs** table with:
- Project name
- Priority Objective
- Status
- Next Action
- Deadline
- Dernière Action
- Warning level

Add item to **Actions Pending** if pending actions exist.

### 5. Update Relations in Existing Concepts

Check these concept files and add `<PROJECT>` where relevant:

| Concept File | When to Add |
|-------------|------------|
| `concepts/KORA.md` | If parallel venture, shared resources, or strategic link |
| `concepts/OMNI.md` | If parallel venture or shared execution model |
| `DAOS.md` | If project generates daily actions |
| `FAOS.md` | If project has fundraising component |
| `LEOS.md` | If project requires learning |
| `DIOS.md` | If project is a distribution platform |
| `CEOS.md` | If project creates content |
| `SOS.md` | If project impacts founder health/energy |

### 6. Check DIOS.md

If project is a distribution platform or commerce channel, add it under the relevant domain in DIOS.md.

### 7. Update CONCEPT_BOUNDARIES.md (if needed)

If project introduces a new concept boundary not yet documented.

### 8. Verify Bidirectional Links

Every relation added must be **bidirectional**. If A relates to B, B must relate to A. Search for the relation in both files.

---

## Quick Reference

| Step | File(s) | Action |
|------|---------|--------|
| 1 | `concepts/<PROJECT>.md` | Create concept file |
| 2 | `projects/<PROJECT>/` | Create data room |
| 3 | `State/CURRENT_STATE.md` | Add to active products + status section |
| 4 | `State/PRIORITY_MATRIX.md` | Add row + pending actions |
| 5 | Relevant concept files | Add relation links |
| 6 | `DIOS.md` | Add platform entry if applicable |
| 7 | `CONCEPT_BOUNDARIES.md` | Update if new boundary |
| 8 | All edited files | Verify bidirectional links |

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | System |


--- FILE: Protocols/PRG_TEST.md

# PRG Compliance Test

Run this test after any modification to SYSTEM_PROMPT.md.

## Test 1: Critical Rules in First 30 Lines
- Read SYSTEM_PROMPT.md
- Verify "Get-Date" appears within first 30 lines
- PASS if Get-Date found in lines 1-30

## Test 2: PRG Section Present
- Search for "Pre-Response Gate (PRG)"
- PASS if section exists with all 3 steps (Temporal Check, Absorb Updates, Freshness Flag)

## Test 3: PRG Referenced in Classification Rules
- Search for "Classification Rules"
- PASS if rule 5 references PRG

## Test 4: PRG in Standard Session
- Search for "Standard Session"
- PASS if PRG appears as step in the session loop

## Test 5: PRG Output Format
- Search for PRG section
- PASS if `**[datetime Lomé UTC+0]**` output format specified

## Test 6: RUNTIME.md Has Temporal Awareness
- Read RUNTIME.md
- PASS if Temporal Awareness section exists with State Aging table and Staleness Thresholds

## Test 7: Total Lines
- Count lines in SYSTEM_PROMPT.md
- PASS if <= 130 lines


--- FILE: DECISION_ENGINE.md

# FounderOS V4 — DECISION_ENGINE

## Purpose

The DECISION_ENGINE provides structured decision-making frameworks. It is invoked when the user faces a choice with meaningful consequences.

## Position in FounderHQ

DECISION_ENGINE provides structured decision-making frameworks for tradeoffs, prioritization, and strategic choices. It is loaded when MOS, VEAOS, or any module faces a decision with multiple options and non-trivial consequences. It feeds recommendations back to the calling module.

## Inputs
- Decision context — the question, options, criteria, constraints from the calling module
- `State/CURRENT_STATE.md` — current operational constraints and mode
- `concepts/TIMELINE.md` — relevant past decisions and outcomes

## Outputs
- Structured analysis — options evaluated against criteria with weighted scores
- Recommendation — best option with rationale
- Sensitivity analysis — how recommendation changes under different assumptions
- Decision record — written to TIMELINE.md for future reference

## Relations
- **MOS** — mission tradeoffs use DECISION_ENGINE for structured analysis
- **VEAOS** — strategic tradeoffs use PROACT framework via DECISION_ENGINE
- **FAOS** — financial tradeoffs analyzed for resource allocation decisions
- **TIMELINE** — every decision written to timeline for traceability

## Workflow

### When to Invoke

- User asks "What should I do?"
- Multiple viable options exist with different tradeoffs
- Decision involves risk, resource allocation, or opportunity cost
- User is indecisive or stuck

### Decision Framework: PROACT

1. **P**roblem — What exactly needs to be decided? State in one sentence.
2. **R**equirements — What must the decision satisfy? (constraints, must-haves)
3. **O**ptions — 2-3 viable paths, each with pros/cons
4. **A**ssessment — Score each option against requirements
5. **C**hoice — Recommendation with rationale
6. **T**rigger — What needs to happen to execute this decision?

### Decision Quality Checklist

- [ ] All relevant information loaded from files?
- [ ] Short-term and long-term consequences considered?
- [ ] Worst-case acceptable?
- [ ] Can this decision be reversed? If not, what's the cost?
- [ ] Is this a reversible decision? (Move fast if yes. Be careful if no.)
- [ ] What would I decide if I had more data? Less data? More money? Less money?
- [ ] Is this decision driven by fear or by strategy?

### Decision Logging

Every significant decision must be logged in TIMELINE.md:
- Date
- Decision
- Rationale
- Expected outcome
- Review date (when to check if it was right)

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: PATTERN_ENGINE.md

# FounderOS V4 — PATTERN_ENGINE

## Purpose

The PATTERN_ENGINE detects recurring structures across actions, outcomes, decisions, and behaviors — converting raw experience into actionable pattern awareness.

## Position in FounderHQ

PATTERN_ENGINE identifies, validates, and tracks recurring patterns across FounderHQ operations. It is loaded when the founder or ASTRA suspects a pattern, or during routine analysis cycles. It feeds validated patterns into PLAYBOOK_ENGINE and KNOWLEDGE_EVOLUTION_ENGINE.

## Inputs
- `concepts/TIMELINE.md` — raw event stream for pattern scanning
- `State/CURRENT_STATE.md` — current operational context
- Pattern hypotheses — from ASTRA or founder observations
- `concepts/MEMORY.md` — past pattern records for validation

## Outputs
- Pattern candidates — potential recurring behaviors, signals, or bottlenecks
- Validated patterns — confirmed patterns with evidence and confidence level
- Pattern refutations — disproven hypotheses with reasoning
- Playbook triggers — validated patterns that suggest new playbooks

## Relations
- **ASTRA** — receives pattern hypotheses from reflective analysis
- **PLAYBOOK_ENGINE** — validated patterns may produce new or updated playbooks
- **KNOWLEDGE_EVOLUTION_ENGINE** — confirmed patterns stored as structured knowledge
- **TIMELINE** — reads events, writes pattern discoveries

## Workflow

### Pattern Types

1. **Behavioral Patterns** — How the user reacts to certain situations
2. **Outcome Patterns** — What types of actions consistently succeed or fail
3. **Timing Patterns** — When things happen, how long they take
4. **Blockage Patterns** — What consistently blocks progress
5. **Decision Patterns** — How decisions are made and which approaches work
6. **Market Patterns** — Recurring signals in the external environment

### Detection Methods

1. **Timeline Analysis** — Scan TIMELINE.md for repeated Event → Decision → Outcome sequences
2. **Knowledge Analysis** — Scan KNOWLEDGE.md for patterns already documented
3. **Behavioral Observation** — Note recurring user behaviors (procrastination patterns, energy patterns, etc.)
4. **External Signal Detection** — Market trends, platform changes, competitor moves

### Pattern Format

```
## Pattern: [Name]
- Type: [Behavioral/Outcome/Timing/Blockage/Decision/Market]
- Evidence: [Specific instances with dates]
- Confidence: [High/Medium/Low/Speculative]
- Implication: [What this means for what we should do]
- Action: [What to do about it]
```

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: PLAYBOOK_ENGINE.md

# FounderOS V4 — PLAYBOOK_ENGINE

## Purpose

The PLAYBOOK_ENGINE manages the creation, validation, and evolution of playbooks — repeatable strategies validated across 3+ different contexts.

## Position in FounderHQ

PLAYBOOK_ENGINE creates, maintains, and serves operational playbooks for FounderHQ. It is loaded when the founder needs a repeatable process for a known situation, or when PATTERN_ENGINE identifies a situation that deserves a playbook. It feeds active playbooks into DAOS for daily execution.

## Inputs
- `FounderOS/concepts/PLAYBOOK.md` — existing playbook repository
- Pattern triggers — from PATTERN_ENGINE suggesting new playbooks
- `State/CURRENT_STATE.md` — current situation requiring a playbook
- Founder request — specific situation needing a process

## Outputs
- Playbook creation — new playbooks for recurring situations
- Playbook updates — revisions based on execution feedback
- Playbook recommendations — which playbook fits the current situation
- Execution history — how often each playbook is used, success rate

## Relations
- **PATTERN_ENGINE** — validated patterns suggest new playbooks
- **DAOS** — daily execution loads relevant playbooks from PLAYBOOK_ENGINE
- **CONTINUOUS_IMPROVEMENT** — playbook effectiveness tracked as improvement metric
- **TIMELINE** — playbook usage and feedback recorded

## Workflow

### Playbook Lifecycle

1. **Draft** — A promising approach discovered through experimentation
2. **Test** — Applied in 1-2 different contexts
3. **Validated** — Successfully applied in 3+ different contexts → stored in PLAYBOOK.md
4. **Deprecated** — No longer effective due to changed conditions

### Playbook Format

```
## [Playbook Name]
- Domain: [Content/Sales/Operations/Strategy/...]
- Contexts applied: [List of 3+ situations]
- Success metrics: [What counts as success]
- Steps: [Numbered execution steps]
- Failure modes: [When NOT to use this playbook]
- Last validated: [Date]
```

### Playbook Sources

- Successful actions repeated by user
- Patterns detected by PATTERN_ENGINE
- External best practices adapted to FounderHQ context
- Experimentation with documented results

### Playbook Maintenance

- Review all playbooks monthly for continued relevance
- Deprecate playbooks with 0 uses in 60 days
- Archive deprecated playbooks (don't delete — they may become relevant again)

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: KNOWLEDGE_EVOLUTION_ENGINE.md

# FounderOS V4 — KNOWLEDGE_EVOLUTION_ENGINE

## Purpose

The KNOWLEDGE_EVOLUTION_ENGINE owns the long-term evolution of FounderHQ's knowledge base — ensuring knowledge stays accurate, relevant, and well-structured as the system grows.

## Position in FounderHQ

KNOWLEDGE_EVOLUTION_ENGINE manages the FounderHQ knowledge base — storing structured facts, validating new information, identifying gaps, and surfacing relevant knowledge when needed. It is the durable memory layer that persists across sessions. It is loaded when any module needs to store or retrieve structured knowledge.

## Inputs
- New knowledge — facts, insights, patterns from any module (ASTRA, RIOS, PATTERN_ENGINE, etc.)
- `concepts/MEMORY.md` — existing knowledge base
- Knowledge queries — what does the system need to know?
- `concepts/TIMELINE.md` — context for temporal knowledge

## Outputs
- Verified knowledge — facts validated and stored in canonical form
- Knowledge gaps — what the system needs to know but doesn't yet
- Relevance-ranked knowledge — information surfaced in response to queries
- Knowledge versioning — what changed, when, and why

## Relations
- **ASTRA** — reflective insights stored as verified knowledge
- **RIOS** — research findings stored as structured facts
- **PATTERN_ENGINE** — validated patterns stored in knowledge base
- **ALL MODULES** — any module may query knowledge for contextual awareness
- **TIMELINE** — knowledge versioning recorded as timeline events

## Workflow

### Evolution Cycle

#### Monthly (Light)
1. Check KNOWLEDGE.md for entries older than 30 days
2. Flag entries without recent verification
3. Check for duplicate or contradictory entries
4. Report findings to user

#### Quarterly (Deep)
1. Full knowledge audit: every entry in KNOWLEDGE.md reviewed
2. Ontology check: does the knowledge structure still fit reality?
3. Deprecation sweep: mark entries no longer relevant
4. Synthesis: identify meta-patterns across knowledge entries
5. Reorganization: restructure if current categories no longer fit
6. Report: what changed, what was deprecated, what was synthesized

#### Triggers
- New knowledge contradicts old knowledge → reconcile immediately
- A pattern is detected 5+ times → synthesize into a principle
- A knowledge entry has 0 references in 60 days → flag for deprecation

### Knowledge Decay

- Time-sensitive knowledge (prices, contacts, platform rules) decays in 30 days
- Principle-level knowledge (what works, patterns) decays in 90 days
- Identity-level knowledge (mission, values) does not decay but should be reviewed annually
- Decayed knowledge is flagged, not deleted

### Integration

- KNOWLEDGE_EVOLUTION_ENGINE receives patterns from PATTERN_ENGINE
- KNOWLEDGE_EVOLUTION_ENGINE receives new learning from LEOS
- KNOWLEDGE_EVOLUTION_ENGINE reports results to CONTINUOUS_IMPROVEMENT

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: CONTINUOUS_IMPROVEMENT.md

# FounderOS V4 — CONTINUOUS_IMPROVEMENT

## Purpose

CONTINUOUS_IMPROVEMENT owns the meta-layer — tracking how FounderOS itself performs and recommending systemic improvements.

## Position in FounderHQ

CONTINUOUS_IMPROVEMENT drives iterative improvement across FounderHQ — tracking metrics, identifying bottlenecks, running improvement cycles, and measuring progress over time. It is loaded during routine review cycles or when the founder asks "how can we improve?" It feeds improvement recommendations into MOS and DAOS.

## Inputs
- `State/CURRENT_STATE.md` — current operational metrics and bottlenecks
- `concepts/TIMELINE.md` — historical data for trend analysis
- Improvement signals — from any module (ASTRA, SOS, AOS, etc.)
- `concepts/MEMORY.md` — past improvement efforts and outcomes

## Outputs
- Improvement cycles — structured Plan-Do-Check-Act per bottleneck
- Metrics reports — key operational metrics and trends
- Bottleneck analysis — what is blocking progress, ranked by impact
- Experiment recommendations — small changes to test, with expected impact

## Relations
- **MOS** — improvement priorities fed into mission alignment
- **DAOS** — improvement actions delegated for daily execution
- **ASTRA** — reflective insights identify improvement opportunities
- **SOS** — sustainability metrics track founder wellbeing improvement
- **AOS** — architectural debt tracked as improvement item

## Workflow

### Improvement Cycle

#### Every Session (Implicit)
- Did the boot sequence complete without error?
- Did the user have to correct a recommendation?
- Was there a gap between what was needed and what was provided?
- Log observations in MEMORY.md

#### Weekly (Explicit)
1. Review last 7 days of TIMELINE.md
2. Review user feedback patterns from MEMORY.md
3. Identify top 3 friction points
4. Recommend 1 improvement
5. Track whether previous improvements produced results

#### Monthly (Deep)
1. Full OS performance review
2. Audit: are all modules being used? Which are neglected?
3. Survey: ask the user "What would make FounderOS more useful?"
4. Roadmap: what should be improved next?
5. Update: implement selected improvements

### Improvement Types

1. **Content** — Better recommendations, more relevant output
2. **Process** — Faster boot, fewer steps, better workflows
3. **Structure** — Better file organization, clearer dependencies
4. **Experience** — More natural interaction, less friction
5. **Leverage** — Actions that produce compounding returns

### Feedback Processing

When user gives feedback:
1. Acknowledge it
2. Categorize it (Content/Process/Structure/Experience/Leverage)
3. Store it in MEMORY.md with date and context
4. If actionable, create an improvement recommendation
5. Track whether it was implemented and what changed

### Integration

- CONTINUOUS_IMPROVEMENT receives data from all modules
- CONTINUOUS_IMPROVEMENT recommends changes to AOS for architecture
- CONTINUOUS_IMPROVEMENT reports to SYSTEM_PROMPT for systemic awareness

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: MOS.md

# FounderOS V4 — MOS (Mission Orchestrator)

## Purpose

MOS is the mission orchestration engine. It owns the what and why — translating high-level mission into concrete objectives, projects, and daily priorities.

## Position in FounderHQ

MOS sits at the top of the execution stack. It is loaded when the agent needs to determine what to pursue. It feeds priorities to DAOS (daily execution) and context to PROJECT (project state).

## Inputs
- `concepts/MISSION.md` — mission definitions, hierarchy, active/paused/archived status
- `State/CURRENT_STATE.md` — cash position, bottlenecks, current operating mode
- `concepts/TIMELINE.md` — recent events that affect priorities

## Outputs
- Priority list — ranked actions serving the highest mission
- Strategic recommendations — Stop/Pause/Accelerate/Delegate/Automate/Kill for each project
- Drift detection — when projects consume resources without mission progress

## Relations
- **DAOS** — receives priorities and generates daily action modules
- **PROJECT** — updates project status based on priority shifts
- **DECISION_ENGINE** — called when tradeoffs between missions need structured analysis

## Workflow

### Responsibilities

1. Maintain mission coherence across all projects
2. Map every project to a mission
3. Detect mission drift (projects that no longer serve a mission)
4. Prioritize projects by mission impact vs. resource cost
5. Recommend when to start, pause, or kill a project

### Mission Hierarchy

```
FounderHQ (Venture)
└── Mission 1: Soya Supply Chain (survival → stability)
└── Mission 2: DoodleMind Content (growth → brand)
└── Mission 3: FounderOS (infrastructure → leverage)
```

### Operating Principles

- **One mission at a time as top priority.** Currently: Mission 1 (cash constraints).
- **Every project must answer:** What mission does this serve? If none, kill it.
- **Mission can change.** When it does, update MISSION.md, TIMELINE.md, and all affected projects.
- **Rescue missions** (survival) trump growth missions. Growth missions trump infrastructure.

### Interface with DAOS

MOS decides what to do. DAOS decides how to do it today.

- MOS: "Soya supply chain is top priority. We need to call supplier X."
- DAOS: "Here is the call script. Here is what we learned from last call. Here is the optimal time to call."

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: DAOS.md

# FounderOS V4 — DAOS (Daily Autonomous Operating System)

## Purpose

DAOS owns the how of daily execution. It takes MOS's priorities and produces concrete actions, scripts, schedules, and tools for the day.

## Position in FounderHQ

DAOS owns daily execution. It is loaded by RUNTIME Phase 2 (Decide) or when SURVIVAL Auto-Drive triggers. It receives priorities from MOS and produces concrete actions the founder can execute immediately.

## Inputs
- `concepts/MOS.md` — current top priority
- `State/CURRENT_STATE.md` — cash, blockers, mode
- `concepts/PLAYBOOK.md` — relevant playbooks for today's situation

## Outputs
- Action modules — scripts, timing, expected outcome, fallback for 1-3 actions
- Execution context — what changed since yesterday, what is blocked, what is ready

## Relations
- **MOS** — receives top priority
- **CEOS** — delegates content actions when applicable
- **FAOS** — delegates financial actions when applicable
- **TIMELINE** — writes execution outcomes after each action

## Workflow

### Daily Outputs

1. **Action List** — 1-3 concrete actions derived from MOS's top priority
2. **Action Modules** — For each action, provide: script, timing, expected outcome, fallback
3. **Context** — What changed since yesterday, what is blocked, what is ready
4. **Tools** — Playbooks, workflows, templates relevant to today's actions

### Operating Rhythm

When invoked by RUNTIME Phase 2 (Decide):

1. Read MOS's current top priority
2. Read CURRENT_STATE.md for constraints (cash, time, blockers)
3. Read PLAYBOOK.md for relevant playbooks
4. Generate 1-3 action modules
5. Present to user with recommendation
6. After execution, document outcome in TIMELINE.md

### Action Module Format

```
## Action Module: [Name]
- Priority: [High/Medium/Low]
- Effort: [Time, resources needed]
- Script: [What to say/do]
- Expected Outcome: [What success looks like]
- Fallback: [What to do if this fails]
- Playbook: [Reference to PLAYBOOK.md if applicable]
```

### Integration

- DAOS may reference CEOS (Content Engineering) for content actions
- DAOS may reference FAOS (Fundraising) for financial actions
- DAOS may reference LEOS (Learning) for research actions
- DAOS writes to TIMELINE.md after each action

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: AOS.md

# FounderOS V4 — AOS (Architecture Operating System)

## Purpose

AOS owns the architecture of FounderOS itself — ensuring the OS remains coherent, maintainable, and extensible as new modules are added.

## Position in FounderHQ

AOS owns the architecture of FounderOS itself — ensuring the OS remains coherent, maintainable, and extensible as new modules are added. It is loaded when the founder needs to audit the OS structure, understand module dependencies, or decide how to evolve the system. It feeds architectural insights into CONTINUOUS_IMPROVEMENT and dependency context into DECISION_ENGINE.

## Inputs
- All FounderOS module files — current structure, footers, declared dependencies
- `concepts/SOURCE_OF_TRUTH.md` — registered truths and their owners
- `State/CURRENT_STATE.md` — current OS version status

## Outputs
- Architecture audits — file structure, dependency violations, stale content
- Evolution recommendations — split, merge, create, or deprecate modules
- Interface contract compliance reports — missing Purpose, Footer, or undeclared dependencies
- Coherence metrics — duplication detection, Regle 0 violations

## Relations
- **CONTINUOUS_IMPROVEMENT** — architectural debt feeds improvement cycles
- **DECISION_ENGINE** — structural tradeoffs analyzed for OS evolution
- **ALL MODULES** — each module's footer and interface are subject to AOS audit
- **SOURCE_OF_TRUTH** — AOS verifies and updates source-of-truth registry

## Workflow

### Architecture Principles

1. **Bounded concepts** — Every file owns exactly one domain
2. **Source of truth** — Every truth has exactly one owner (Regle 0)
3. **Explicit dependencies** — Every file declares its dependencies
4. **Replaceable components** — Any module can be replaced if its interface is preserved
5. **Model-independent** — No LLM-specific features, no IDE-specific features
6. **File-first** — Session memory is ephemeral; files are durable

### Architecture Audit Protocol

When invoked:

1. Scan all OS files for:
   - Undeclared dependencies
   - Duplicate truths (Regle 0 violations)
   - Missing footers
   - Stale content (>30 days without verified footer)
2. Check SOURCE_OF_TRUTH.md for missing entries
3. Report violations with file paths and line references
4. Recommend corrections

### Interface Contract

Every OS file must have:
- A `## Purpose` section (one sentence)
- A `## Footer` with: Last Verified, Owner, Dependencies
- No truths that belong in another file
- References to other files by exact path

### Evolution

AOS may recommend:
- Splitting a file that has grown too large (>300 lines)
- Merging files with overlapping domains
- Creating new modules for emerging domains
- Deprecating unused modules

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: ASTRA.md

# FounderOS V4 — ASTRA (Astro-Reflective Assistant)

## Purpose

ASTRA is the reflective intelligence engine. It provides structured reflection, pattern recognition across sessions, and strategic clarity through questioning.

## Position in FounderHQ

ASTRA generates reflective insights and retrospective analysis. It is loaded when the founder needs to make sense of past outcomes, extract learnings, or identify patterns across time. It feeds insights into KNOWLEDGE_EVOLUTION_ENGINE (knowledge base) and PATTERN_ENGINE (pattern recognition).

## Inputs
- `concepts/TIMELINE.md` — raw timeline of recent events and outcomes
- `State/CURRENT_STATE.md` — current mode, blockers, operating context
- `concepts/MEMORY.md` — past decisions and their results

## Outputs
- Reflective insights — what worked, what didn't, why
- Pattern hypotheses — recurring behaviors, market signals, bottlenecks
- Actionable learnings — specific recommendations based on analysis
- Retrospectives — structured post-mortems for key events

## Relations
- **KNOWLEDGE_EVOLUTION_ENGINE** — verified insights stored for future reference
- **PATTERN_ENGINE** — pattern hypotheses fed for validation
- **TIMELINE** — reads raw events, writes analyses
- **CONTINUOUS_IMPROVEMENT** — improvement signals feed into CI cycles

## Workflow

### When to Invoke

- End of day/week reflection
- User feels stuck, scattered, or uncertain
- Before major decisions
- When multiple options exist and none is clearly better
- When user needs to clarify their own thinking

### Reflection Framework

1. **What happened?** — Objective events since last reflection
2. **What worked?** — Actions that produced positive outcomes
3. **What didn't?** — Actions that failed or underperformed
4. **What patterns emerge?** — Recurring themes, behaviors, outcomes
5. **What is the signal?** — The most important thing to pay attention to
6. **What is the noise?** — Things that feel urgent but aren't important

### Decision Clarity Questions

- What are you avoiding?
- What would you do if you had 10x the resources?
- What would you do if you had 1/10 the resources?
- What would the best version of you decide?
- What would you tell a friend in this situation?

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: KMOS.md

# FounderOS V4 — KMOS (Knowledge Management OS)

## Purpose

KMOS owns the knowledge layer of FounderHQ — ensuring that what is learned is stored, structured, and retrievable across sessions.

## Knowledge Types

1. **Validated Truths** — Things proven true by experience (KNOWLEDGE.md)
2. **Patterns** — Recurring structures detected across contexts (KNOWLEDGE.md)
3. **Assets** — Products, brands, channels, contacts (ASSET.md)
4. **Playbooks** — Validated strategies repeated 3+ times (PLAYBOOK.md)
5. **Timeline** — Event → Decision → Outcome sequence (TIMELINE.md)

## Knowledge Hygiene

- New lesson → store in KNOWLEDGE.md within same session
- Duplicate pattern → merge, don't duplicate
- Outdated truth → mark with deprecation notice and reason
- Contradiction → follow SOURCE_OF_TRUTH.md resolution

## Cross-Session Continuity

- MEMORY.md is the bridge between sessions. Update it when:
  - A significant decision is made
  - A blocker is encountered
  - A priority shifts
  - A pattern is detected
- Before each session ends, ensure MEMORY.md reflects the full session arc

## Knowledge Evolution

KMOS delegates long-term knowledge evolution to KNOWLEDGE_EVOLUTION_ENGINE for:
- Quarterly knowledge audits
- Knowledge decay detection
- Ontology updates

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: LEOS.md

# FounderOS V4 — LEOS (Learning Engineering OS)

## Purpose

LEOS owns the learning pipeline — designing how new knowledge is acquired, structured, and integrated into FounderHQ.

## Position in FounderHQ

LEOS manages the founder's learning ecosystem — tracking what needs to be learned, how it was learned, and ensuring retention. It is loaded when the founder needs to acquire new skills, review past learning, or organize a learning path. It feeds skill acquisition data into KNOWLEDGE_EVOLUTION_ENGINE and priorities into MOS.

## Inputs
- `State/CURRENT_STATE.md` — available time for learning
- `concepts/MISSION.md` — skills needed for current missions
- `concepts/PLAYBOOK.md` — operational knowledge to master

## Outputs
- Learning paths — structured sequence of skills to acquire
- Progress tracking — what has been learned, retention level, gaps
- Review schedules — spaced repetition for retention
- Skill gaps — analysis of missing capabilities vs. mission requirements

## Relations
- **MOS** — learning priorities aligned with mission needs
- **KNOWLEDGE_EVOLUTION_ENGINE** — knowledge artifacts stored as structured facts
- **CONTINUOUS_IMPROVEMENT** — learning velocity tracked as improvement metric

## Workflow

### Learning Pipeline

1. **Identify knowledge gap** — What don't we know that we need to know?
2. **Design learning approach** — Research, experiment, expert consultation, or trial-and-error?
3. **Execute** — Gather information per approach
4. **Validate** — Cross-reference, test against reality
5. **Integrate** — Store in KNOWLEDGE.md with confidence level

### Learning Priorities (Current)

1. Soya supply chain: supplier reliability, pricing patterns, logistics
2. YouTube content: hook retention mechanics, audience building
3. FounderOS: what workflows need improvement, what concepts need refinement

### Active Learning Programs

1. **Financial Literacy**
   - Status: Active
   - Progress: 0/28 concepts
   - Source: `LEARNING/FINANCIAL_LITERACY.md`
   - Levels: Fundamentals → Startup Finance → Corporate Structures → SME Finance Africa → Macroeconomics

### Learning Formats

- **Active**: Deliberate research, experiments, A/B testing
- **Passive**: Pattern detection from daily operations
- **Borrowed**: Learning from others (competitors, mentors, content)

### Integration

- LEOS supplies CEOS with research for content topics
- LEOS supplies FAOS with market data for fundraising
- LEOS feeds into KNOWLEDGE_EVOLUTION_ENGINE for quarterly synthesis

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: RIOS.md

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


--- FILE: SOS.md

# FounderOS V4 — SOS (Self Operating System)

## Purpose

SOS owns the self-layer — the founder's wellbeing, energy, mindset, and personal effectiveness. FounderOS cannot execute if the founder cannot.

## Position in FounderHQ

SOS is the safety net for the founder's wellbeing, relationships, and work-life integration. It is loaded during DAILY KICKOFF (RUNTIME Phase 1 - Check) or when the founder signals stress, fatigue, or imbalance. It feeds wellbeing context into CURRENT_STATE and recovery recommendations into DAOS.

## Inputs
- `State/CURRENT_STATE.md` — current mode, energy level, stress signals
- `concepts/TIMELINE.md` — recent work patterns and rest history
- Founder self-report — how the founder is feeling verbally

## Outputs
- Wellbeing assessment — energy, stress, balance indicators
- Recovery recommendations — breaks, rest, boundary setting
- Priority adjustments — what to defer when capacity is low
- Pattern alerts — when work patterns show unhealthy trends

## Relations
- **DAOS** — receives priority adjustments when capacity is low
- **CURRENT_STATE** — wellbeing status written to operational state
- **CONTINUOUS_IMPROVEMENT** — sustainability metrics feed into CI cycles

## Workflow

### Domains

1. **Energy** — Sleep, nutrition, exercise, stress levels
2. **Mindset** — Motivation, clarity, confidence, decision fatigue
3. **Discipline** — Consistency, follow-through, habit formation
4. **Balance** — Work vs. rest, alone vs. social, push vs. recover

### Self-Check Protocol

When the user seems stuck, tired, or scattered:

1. **Energy check**: When did you last eat? Sleep? Take a break?
2. **Clarity check**: What is the single most important thing to do?
3. **Block check**: What is stopping you from doing it?
4. **Bias check**: Are you avoiding something?

### Interventions

- **Low energy**: Recommend break, food, walk. Do not push.
- **Scattered**: Reduce options to one. Eliminate noise.
- **Blocked**: Ask "What is the smallest possible next step?"
- **Overwhelmed**: Recommend writing everything down, then sorting.

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: VEAOS.md

# FounderOS V4 — VEAOS (Strategic Vision Engine)

## Purpose

VEAOS owns strategic thinking — the medium-to-long-term view that MOS (daily/weekly) cannot see.

## Position in FounderHQ

VEAOS handles long-term strategic thinking. It is loaded when the agent faces questions about direction, vision, or multi-month planning. It feeds strategic context into MOS (priority setting) and DECISION_ENGINE (long-term decisions).

## Inputs
- `concepts/MISSION.md` — long-term mission definitions
- `concepts/TIMELINE.md` — historical patterns and trajectory
- `State/CURRENT_STATE.md` — current constraints and resources

## Outputs
- Strategic scenarios — 3-5 year projections
- Vision statements — refined mission language
- Strategic recommendations — what to pursue, what to deprioritize over long horizon

## Relations
- **MOS** — strategic context informs priority setting
- **DECISION_ENGINE** — strategic tradeoffs use PROACT framework
- **TIMELINE** — strategic decisions recorded as timeline events

## Workflow

### When to Invoke

- User asks about strategy, vision, long-term direction
- User is stuck on a decision with long-term consequences
- Current strategy has been running for 30+ days without review
- MOS detects a pattern that may require strategic shift

### Strategic Framework

1. **Where are we?** — Current position, cash, capabilities, constraints
2. **Where do we want to be?** — 3-month, 6-month, 12-month targets
3. **What are the paths?** — 2-3 viable strategies with tradeoffs
4. **What is the best path?** — Recommendation with rationale
5. **What is the first step?** — Concrete action to start

### Strategic Tools

- **Scenario Planning**: Best case / base case / worst case for each path
- **Bottleneck Analysis**: What is the binding constraint? What unblocks it?
- **Leverage Analysis**: Which action produces the most outcome per unit of effort?
- **Opportunity Cost**: What are we NOT doing by choosing this path?

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: Runtime/FRE_SPEC.md

# Founder Runtime Ecosystem Specification (FRE) V2

## Purpose

FRE defines what FounderHQ requires from any runtime environment. Any platform (OpenCode, Claude Code, ChatGPT, Gemini, Cursor, local agent) that satisfies these contracts can run FounderHQ identically.

FRE is NOT an adapter. FRE is the runtime. The adapter is the translation of FRE to a specific platform.

## Architecture

```
FRE_SPEC.md (this document — constitution)
    ↓
RUNTIME_KERNEL.md (the decision cycle — BOOT → OBSERVE → ORIENT → DECIDE → ACT → LEARN → UPDATE)
    ↓
ADAPTER_INTERFACE.md (contract for platform adapters)
    ↓
adapters/*.md (platform-specific translations)
```

## Non-Negotiable Principles

1. **FounderHQ > tools** — FounderHQ must survive the disappearance of any LLM, platform, or tool
2. **LLM is a component** — the LLM executes the kernel, it is not the kernel itself
3. **Files are source of truth** — session memory is ephemeral; all durable state lives in files
4. **State over conversation** — anything that matters must be stored in a file
5. **Decision over conversation** — every cycle must produce a decision or action, not just information
6. **Portability by design** — layers 1-5 (Manifest to FRE) must be sufficient to reconstruct FounderHQ

## Contracts

### Contract 1: System Architecture

FRE defines 7 layers:

| Layer | Contents | Location |
|-------|----------|----------|
| 1. Principles | FOUNDERHQ_MANIFEST.md | root |
| 2. Concepts | MISSION, MEMORY, KNOWLEDGE, TIMELINE, PROJECT, ASSET, WORKFLOW, PLAYBOOK, SYSTEM | concepts/*.md |
| 3. Protocols | DECISION_GATES, SOURCE_OF_TRUTH, INFO_CAPTURE, etc. | Protocols/*.md |
| 4. Frameworks | CAOS, CEOS, PSOS, FAOS, SAOS (Core); DIOS, VAOS (Specialized) | Frameworks/**/*.md |
| 5. FRE | This spec + RUNTIME_KERNEL + ADAPTER_INTERFACE | Runtime/*.md |
| 6. Adapters | Platform-specific translations of FRE | Runtime/adapters/*.md |
| 7. Engine (optional) | Python automation scripts | Runtime/engine/*.py |

### Contract 2: Boot Sequence

Every session MUST execute the kernel Phase 1 (BOOT) before responding. See RUNTIME_KERNEL.md.

### Contract 3: Pre-Response Gate (PRG)

Every response MUST pass through the PRG gates defined in SYSTEM_PROMPT.md.

### Contract 4: State Management

| Rule | Enforced | Violation |
|------|----------|-----------|
| Every state file has a `Last Updated` timestamp | Before reading | Missing or stale timestamp |
| State > 48h without update → flagged STALE | Before any action using that state | Used without flagging |
| CURRENT_STATE is single source of truth for session state | Before any state-dependent decision | Another file contradicts CURRENT_STATE |
| TIMELINE.md updated for every significant event | After executing an action | Event happened, TIMELINE.md not updated |

### Contract 5: Temporal

1. All responses start with `**[datetime Lomé UTC+0]**`
2. Datetime format: `YYYY-MM-DD HH:MM Lomé UTC+0`
3. Timezone: West Africa Time (UTC+0, no DST)
4. Age of any file = current_time - file's `Last Updated`
5. Age categories: <1d (high), 1-7d (medium), 7-30d (low), 30-90d (very low), >90d (minimal)

### Contract 6: Context Recall

1. If session context is lost, execute full BOOT
2. If TIMELINE.md exists, reconstruct from reverse chronological
3. If TIMELINE.md missing, reconstruct from CURRENT_STATE + concept footers
4. If reconstruction is partial, mark all entries as APPROXIMATE

## Runtime Requirements

Any platform claiming FRE compatibility MUST provide:

1. **File system access** — read/write/search files in the FounderHQ directory
2. **Time awareness** — current datetime with timezone
3. **Instruction execution** — ability to load and follow protocols
4. **Session continuity** — context across multiple turns within a session
5. **State persistence** — files survive between sessions
6. **Founder interaction** — bidirectional communication

See ADAPTER_INTERFACE.md for the adapter contract.

## Testing FRE Compliance

A runtime passes if:
1. BOOT completes: datetime + mode + priority reported
2. PRG fires: info capture before response
3. State persists: files written in session N readable in session N+1

## Footer

| Field | Value |
|-------|-------|
| Version | V2 |
| Last Verified | 2026-06-21 |
| Owner | FRE |
| Dependencies | RUNTIME_KERNEL.md, ADAPTER_INTERFACE.md |


--- FILE: Runtime/RUNTIME_KERNEL.md

# FRE — RUNTIME KERNEL

## Purpose

Define the universal execution cycle that every FounderHQ runtime implements. The kernel is platform-independent and LLM-independent.

## Identity

The kernel is the decision cycle. It transforms observation into action and action into learning. It is the heartbeat of FounderHQ.

## The Kernel Cycle

```
BOOT
  ↓
OBSERVE
  ↓
ORIENT
  ↓
DECIDE
  ↓
ACT
  ↓
LEARN
  ↓
UPDATE
  ↓
(repeat from OBSERVE)
```

## Phase 1: BOOT

Execute at session start - triggered by user message starting with `boot` or first `fhq` of the day. If the session is already active (a prior `fhq` or `boot` was processed today), BOOT is skipped and the cycle starts at OBSERVE.

### Full Boot (triggered by `boot` or first daily `fhq`):

Operations:
0. **GENESIS Check** - Check if `.founderhq_installed` exists. If absent, execute GENESIS: ask user for GitHub token, create .venv, install dependencies, create .env, run installer, create `.founderhq_installed` marker.
1. Load State/CURRENT_STATE.md
2. Load State/PRIORITY_MATRIX.md
3. Load State/CADENCE.md
4. Load State/LIFECYCLE.md
5. Load State/WATCH_REGISTRY.md
6. Load State/ALERTS.md - read and clear
7. Load State/WATCH_REPORT.md
8. Compute datetime in Lome UTC+0
9. Set Session Start timestamp in CADENCE.md (Day -> Session Start)
10. Scan all concept footers for staleness (>48h)
11. Report: datetime, mode (SURVIVAL/GROWTH/SCALE), cadence context, lifecycle phases, top priority, stale concepts, active alerts
12. **Sync Pull** - If `.env` exists with FHQ_GIST_TOKEN, run `sync.py pull` to fetch remote state. On failure, continue with local state.

Output: Session awareness established.

### Quick Boot (triggered by subsequent `fhq` same day):

Operations:
1. Re-read CURRENT_STATE.md (may have changed since last cycle)
2. Re-read LIFECYCLE.md (project phases may have shifted)
3. Compute current datetime, update CADENCE.md Hour section
4. Check ALERTS.md for new entries from background scripts

Output: Updated temporal awareness, skipping full initialization.

## Phase 2: OBSERVE

Receive and process input from the founder or the environment.

Operations:
1. Receive raw input (message, file change, time trigger)
2. Scan input against INFO_CAPTURE_PROTOCOL mapping
3. Capture any operational data found into appropriate files
4. Classify input into an action type (DECISION_GATES)

Output: Cleaned, classified input ready for orientation.

## Phase 3: ORIENT

Understand what the input means in the current context. Cross-reference cadence, lifecycle, and active frameworks.

Operations:
1. Load relevant concepts for the classified action type
2. Verify freshness of loaded concepts
3. **Cross CADENCE x LIFECYCLE**: Determine current temporal position (week, month, quarter) and active project phases. Select frameworks matching lifecycle phase from LIFECYCLE.md phase-to-framework mapping.
4. Scan all active projects in PRIORITY_MATRIX for data room completeness
5. Flag any contradictions between files
6. Check current constraints: cash, energy, time, blockers
7. **Check ALERTS.md** for any background script notifications since last cycle
8. **Check WATCH_REPORT.md** for any new veille findings

Output: Situational awareness with flagged risks, cadence context, lifecycle-informed framework selection.

## Phase 4: DECIDE

Choose the single highest-leverage action.

Operations:
1. Apply DECISION_GATES: is this financial, legal, external?
2. Apply PRIORITIZATION_PROTOCOL: is this the right action NOW?
3. If SURVIVAL mode and DIRECT classification: auto-generate action module
4. If escalation required: present options with recommendation, await decision
5. Select one action

Output: A clear, constrained decision.

## Phase 5: ACT

Execute the selected action.

Operations:
1. Load the relevant module (DIOS, VAOS, CEOS, etc.)
2. Load the relevant workflow if applicable
3. Execute the action
4. Document the execution

Output: Action completed.

## Phase 6: LEARN

Extract lessons from the action and its outcome.

Operations:
1. What worked?
2. What didn't?
3. What surprised us?
4. Is there a pattern?
5. Is there a new playbook?

Output: Knowledge captured.

## Phase 7: UPDATE

Persist all changes to files.

Operations:
1. Update CURRENT_STATE.md with new operational state
2. Update TIMELINE.md (Event → Decision → Outcome)
3. Update KNOWLEDGE.md with validated lessons
4. Update affected concept files
5. Save session objective and next-session priority
6. **Sync Push** - If `.env` exists with FHQ_GIST_TOKEN, run `sync.py push` to persist state to remote Gist. On failure, state remains local.

Output: State preserved for next session.

## Kernel Principles

1. **LLM is a component** — the kernel cycles regardless of which LLM executes it
2. **Pass by reference** — can skip phases if input demands immediate action (e.g., "stop")
3. **No phase skipping without flag** — if a phase is skipped, it must be declared
4. **Cash-aware** — if cash < 1,500 FCFA, DECIDE must prioritize revenue generation
5. **File-based** — all outputs are persisted to files before the next cycle

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | FRE |
| Purpose | Universal execution cycle for FounderHQ. Platform-independent decision loop. |
| Dependencies | FRE_SPEC.md, ADAPTER_INTERFACE.md, SYSTEM_PROMPT.md |


--- FILE: Runtime/ADAPTER_INTERFACE.md

# ADAPTER INTERFACE — FRE V1

## Purpose
Every platform adapter MUST answer these 4 questions. This ensures FRE_SPEC contracts can be evaluated consistently across platforms.

## Mandatory Questions

### Q1: Kernel Loading
How does this platform load FRE_SPEC.md (or SYSTEM_PROMPT.md) as instructions?

Answer must specify:
- File path or mechanism
- Whether loading is automatic or manual
- If automatic: what config file triggers it
- If manual: what the user must do

### Q2: File Access
How does this platform read, write, and search files?

Answer must specify:
- Available tools (Read, Write, Glob, Grep, etc.)
- File system scope (project only, any path, none)
- Any path transformation required (CRLF, encoding, etc.)

### Q3: Context Persistence
How does this platform maintain state between sessions?

Answer must specify:
- Session isolation (each session starts fresh?)
- What persists (files, env vars, memory?)
- Reconstruction strategy (how to recover if state lost)

### Q4: Protocol Execution
How does this platform execute the 5 PRG gates?

Answer must specify:
- Which gates can be automated vs manual
- Where PRG logic lives (in system prompt, in script, in middleware)
- Failure behavior (block response, flag, ignore)

## Validation

An adapter is VALID if:
1. All 4 questions answered
2. Each answer is platform-specific (not generic)
3. No contradiction with FRE_SPEC contracts

## Template

```markdown
# [Platform Name] Adapter

## Q1: Kernel Loading
**Mechanism:** [How does this platform load FRE_SPEC.md?]
**Automatic?** [Yes/No — if yes, what config file triggers it?]
**User action:** [What must the user do manually?]

## Q2: File Access
**Available tools:** [Read, Write, Glob, Grep, Bash, etc.]
**Scope:** [Project only, any path, none]
**Encoding/transformations:** [CRLF, shell, etc.]

## Q3: Context Persistence
**Session isolation:** [Each session fresh?]
**What persists:** [Files, env vars, memory?]
**Reconstruction strategy:** [How to recover from lost state?]

## Q4: Protocol Execution
| Gate | Automation |
|------|-----------|
| Temporal Check | [Manual/Automatable] |
| Info Capture Scan | [Manual/Automatable] |
| Absorb Updates | [Manual/Automatable] |
| Project Data Room Scan | [Manual/Automatable] |
| Freshness Flag | [Manual/Automatable] |

**Failure behavior:** [Block response, flag, ignore?]
```


--- FILE: Runtime/RUNTIME_INTERFACE.md

# RUNTIME INTERFACE

## Purpose

Define what FounderHQ requires from any execution environment.

This document is the contract between FounderHQ (concept layer) and any runtime (execution layer).

A runtime is anything that can read files, execute instructions, and interact with the founder.

Examples: OpenCode, Cursor, Claude Code, a terminal, a custom application, a future AI platform.

---

## Core Principle

FounderHQ does not depend on any specific runtime.

Any runtime that satisfies this interface can operate FounderHQ.

---

## Required Capabilities

### 1. File System Access

The runtime must be able to:

- Read files from the FounderHQ directory
- Write files to the FounderHQ directory
- List contents of directories
- Check if a file or directory exists

**Minimum:** Read and write text files.

**Optional:** JSON, YAML, database, or graph storage (for future concept implementations).

---

### 2. Time Awareness

The runtime must be able to provide:

- Current date and time
- Time zone of the founder
- Ability to compare dates and calculate elapsed time

**Why:** Without time awareness, FounderHQ cannot detect staleness, maintain timeline, or evaluate state freshness.

---

### 3. Instruction Execution

The runtime must be able to execute instructions from the FOUNDEROS_PROTOCOL.

This means:

- Loading concepts (reading files)
- Understanding the protocol
- Following boot procedure
- Executing workflows
- Updating concepts

**Why:** FounderHQ is a protocol, not software. The runtime must be capable of interpreting and following the protocol.

---

### 4. Session Continuity

The runtime must provide:

- A session that can span multiple interactions
- The ability to carry context within a session
- Clear session boundaries (start and end)

**Why:** FounderHQ operates in sessions. Without session continuity, every interaction starts from zero.

---

### 5. State Persistence

The runtime must persist files between sessions.

- Files written in session N must be readable in session N+1
- No session-specific data should be required for survival
- All durable state lives in files

**Why:** FounderHQ's fundamental invariant is that files survive. Conversation context does not.

---

### 6. Interaction With The Founder

The runtime must enable:

- The founder to give instructions
- The runtime to present information
- The runtime to ask questions or request decisions
- The runtime to escalate when governance requires founder approval

**Why:** FounderHQ is a collaborative system between founder and runtime. Communication must be bidirectional.

---

## Optional But Recommended Capabilities

### Event Detection

A runtime that can detect file changes, scheduled events, or external triggers will make FounderHQ more responsive.

FounderHQ currently operates on session-based interaction (founder initiates).

An event-capable runtime would allow FounderHQ to initiate (founderOS detects a change and alerts the founder).

### Automation Execution

A runtime that can execute scripts, run workflows automatically, or trigger actions based on conditions will reduce manual overhead.

FounderHQ currently relies on the runtime's LLM to execute workflows step by step.

An automation-capable runtime would execute workflows autonomously.

### Multi-Session Awareness

A runtime that can track session history, detect session gaps, and maintain awareness across sessions without relying solely on file reads.

---

## What FounderHQ Does NOT Require

FounderHQ does not require:

- A specific LLM model
- A specific runtime name or brand
- Internet connectivity (can operate fully offline)
- Cloud services
- A specific operating system
- A specific file format
- A database
- A graphical interface
- Real-time capabilities

If a runtime provides only file read/write, time awareness, and text interaction, FounderHQ can operate.

---

## Interface Verification

To verify that a runtime satisfies the interface:

1. Can the runtime read FOUNDERHQ_MANIFEST.md? → File System Access ✅
2. Can the runtime provide current date and time? → Time Awareness ✅
3. Can the runtime follow the boot procedure? → Instruction Execution ✅
4. Can the runtime maintain context across multiple turns? → Session Continuity ✅
5. Do files persist after the runtime closes? → State Persistence ✅
6. Can the founder and runtime exchange messages? → Interaction ✅

If all six are true, the runtime is compatible.

---

## Runtime Adapter Pattern

A runtime adapter is a document that tells the runtime how to satisfy the interface requirements for a specific environment.

Example structure for an adapter:

```
RUNTIME/opencode/SETUP.md

This adapter tells OpenCode how to operate FounderHQ.

1. Open this directory in OpenCode
2. OpenCode will read SYSTEM_PROMPT.md automatically
3. The SYSTEM_PROMPT references Protocols/FOUNDEROS_PROTOCOL.md
4. The protocol guides all subsequent operations

Required configuration:
- OpenCode must have file read/write access
- OpenCode must have time zone awareness
- No plugins required
```

Adapters should be minimal. They translate the interface requirements into environment-specific instructions.

---

## Footer

This interface is stable.

FounderHQ should not change its runtime requirements.

If a runtime cannot satisfy this interface, the runtime is incompatible — not FounderHQ.


--- FILE: Runtime/opencode/opencode.md

# OpenCode Runtime Adapter

## Detection

FounderHQ is auto-detected when the working directory contains FounderOS/. The protocol boots automatically via Protocols/FOUNDEROS_PROTOCOL.md.

## Configuration File

.opencode/instructions.md contains the rules specific to the OpenCode environment.

## Specificities

- **Shell:** Windows PowerShell 5.1
- **Timezone:** Local system (auto-detected by Get-Date). Conversion to Lome UTC+0 each session.
- **Files:** CRLF (Windows)
- **DST:** [System.TimeZoneInfo]::Local.GetUtcOffset((Get-Date)) to detect the actual offset.

## Boot sequence (summary)

1. OpenCode loads Protocols/FOUNDEROS_PROTOCOL.md via system instructions
2. The protocol guides all subsequent operations
3. DECISION_GATES is loaded before each action
4. TEMPORAL_AWARENESS checks the time with each response
5. Frameworks are loaded on demand via DECISION_GATES

## Known limitations

- No automatic event detection (session-based only)
- No native automation (workflows executed manually by the LLM)
- No multi-session awareness beyond files


--- FILE: Runtime/adapters/chatgpt.md

# ChatGPT Adapter

## Q1: Kernel Loading
**Mechanism:** Manual copy-paste. User opens ChatGPT, pastes the contents of FRE_SPEC.md (or SYSTEM_PROMPT.md) as the first message. The LLM then has the constitution in context.

**Automatic?** No. ChatGPT has no file system access and no config-based instruction injection. User must manually provide instructions each session or use a saved custom GPT.

**Optimization:** Create a Custom GPT with FRE_SPEC.md embedded in system instructions. This persists across sessions.

## Q2: File Access
**Available tools:** None. ChatGPT has no file read/write/search capabilities in standard mode. Code Interpreter (Advanced) can access uploaded files but not the local filesystem.

**Scope:** None. User must paste file contents into the chat.

**Workaround:** User uploads key files (CURRENT_STATE.md, PRIORITY_MATRIX.md) as attachments each session. LLM reads them as context.

## Q3: Context Persistence
**Session isolation:** Complete. Each session is independent with no memory of previous sessions. Custom GPTs retain system instructions but not conversation history.

**What persists:** Custom GPT instructions (if configured). Nothing else.

**Reconstruction strategy:** User must upload CURRENT_STATE.md + PRIORITY_MATRIX.md + TIMELINE.md at session start. Boot sequence then proceeds with loaded context.

## Q4: Protocol Execution
| Gate | Automation |
|------|-----------|
| Temporal Check | Manual — LLM must compute datetime from provided context or web search. |
| Info Capture Scan | Manual — LLM scans conversation and tells user what files need updating (cannot write files). |
| Absorb Updates | Manual — LLM tracks changes in conversation. User must apply file edits manually. |
| Project Data Room Scan | Manual — LLM reviews project structure from uploaded files. Flags gaps. |
| Freshness Flag | Manual — LLM checks timestamps from loaded files. |

**Critical limitation:** ChatGPT cannot write files. All updates must be output as instructions for the user to apply manually.


--- FILE: Runtime/adapters/claude.md

# Claude Code Adapter

## Q1: Kernel Loading
**Mechanism:** Create `CLAUDE.md` at repo root referencing FRE_SPEC.md:
```markdown
# FounderHQ
Read and follow `FounderOS/Runtime/FRE_SPEC.md` as the system constitution.
Then load and execute `FounderOS/SYSTEM_PROMPT.md`.
```
Alternatively, `CLAUDE.md` can contain the full contents of SYSTEM_PROMPT.md.

**Automatic?** Yes. Claude Code reads `CLAUDE.md` at project root on session start. No user action required.

## Q2: File Access
**Available tools:** Read, Write, Edit, Glob, Grep, Bash (similar to OpenCode). Project-scoped file access.

## Q3: Context Persistence
**Session isolation:** Isolated sessions. No conversation history persists.

**What persists:** Files only.

**Reconstruction strategy:** Same as OpenCode — boot sequence reads state files on every start.

## Q4: Protocol Execution
| Gate | Automation |
|------|-----------|
| Temporal Check | Manual — SYSTEM_PROMPT.md requires it |
| Info Capture Scan | Manual |
| Absorb Updates | Manual |
| Project Data Room Scan | Manual |
| Freshness Flag | Manual |

All gates are LLM-disciplined. No enforcement mechanism in Claude Code.


--- FILE: Runtime/adapters/cursor.md

# Cursor IDE Adapter

## Q1: Kernel Loading
**Mechanism:** Create `.cursorrules` at project root:
```
Read and follow `FounderOS/Runtime/FRE_SPEC.md` as the system constitution.
Then load and execute `FounderOS/SYSTEM_PROMPT.md`.
```

**Automatic?** Yes. Cursor reads `.cursorrules` and applies them as system instructions on project open.

## Q2: File Access
**Available tools:** Read, Write, Edit, Glob, Grep via Cursor's agent interface. Full project file access.

## Q3: Context Persistence
**Session isolation:** Isolated sessions. No conversation memory across sessions.

**What persists:** Files only.

## Q4: Protocol Execution
All gates are LLM-disciplined. Same pattern as OpenCode/Claude Code.


--- FILE: Runtime/adapters/gemini.md

# Gemini CLI Adapter

## Q1: Kernel Loading
**Mechanism:** Create `GEMINI.md` at repo root:
```markdown
Read and follow `FounderOS/Runtime/FRE_SPEC.md` as the system constitution.
Then load and execute `FounderOS/SYSTEM_PROMPT.md`.
```

**Automatic?** Yes, if Gemini CLI supports `GEMINI.md` as instructions. Otherwise, user must provide instructions manually.

## Q2: File Access
**Available tools:** Bash commands. File read/write via shell (cat, echo, redirects). No dedicated Read/Write tools.

## Q3: Context Persistence
**Session isolation:** Isolated sessions.

**What persists:** Files only.

## Q4: Protocol Execution
Same as Claude Code — all gates are LLM-disciplined.


--- FILE: Runtime/adapters/local_agent.md

# Local Agent Adapter

## Q1: Kernel Loading
**Mechanism:** Script or application that reads FRE_SPEC.md and injects it into the LLM's system prompt at session start. For example:
```python
# Pseudocode
with open("FounderOS/Runtime/FRE_SPEC.md") as f:
    fre_spec = f.read()
with open("FounderOS/SYSTEM_PROMPT.md") as f:
    system_prompt = f.read()
llm = LLM(system_prompt=fre_spec + "\n\n" + system_prompt)
```

**Automatic?** Yes, if configured. No user action required after setup.

## Q2: File Access
**Available tools:** Full filesystem access via Python/Node/Shell. Can read, write, and search any file in the project.

## Q3: Context Persistence
**Session isolation:** Configurable. Can persist conversation history to database or files.

**What persists:** Everything — files, conversation history, state, logs. This is the most capable runtime for FHQ.

## Q4: Protocol Execution
| Gate | Automation |
|------|-----------|
| Temporal Check | Automatable — script computes datetime before each LLM call |
| Info Capture Scan | Automatable — regex parse user message, update state files |
| Absorb Updates | Automatable — script handles file writes |
| Project Data Room Scan | Automatable — script verifies project structure |
| Freshness Flag | Automatable — script checks file timestamps |

**Advantage:** The local agent can enforce gates in middleware, not relying on LLM discipline.


--- FILE: Runtime/adapters/opencode.md

# OpenCode Adapter

## Q1: Kernel Loading
**Mechanism:** `opencode.json` at `FounderOS/opencode.json`
```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["SYSTEM_PROMPT.md"]
}
```
**Automatic?** Yes. OpenCode loads SYSTEM_PROMPT.md as system instructions on session start. No user action required.

**Note:** SYSTEM_PROMPT.md is the active instruction set. FRE_SPEC.md is the canonical reference. They must be kept in sync — FRE_SPEC defines WHAT, SYSTEM_PROMPT implements HOW.

## Q2: File Access
**Available tools:**
- `Read` — read file content (full or partial)
- `Write` — create or overwrite files
- `Edit` — make surgical edits to existing files
- `Glob` — find files by pattern
- `Grep` — search file contents
- `Bash` — execute PowerShell commands (access to filesystem, git, npm, etc.)

**Scope:** Project directory (`FounderHQ/`) and subdirectories. External access limited to `C:\Users\junio\AppData\Local\Temp\opencode\`.

**Encoding:** Windows CRLF. PowerShell 5.1.

## Q3: Context Persistence
**Session isolation:** Each session is isolated. No conversation memory persists between sessions.

**What persists:** Files only. All state is in `FounderOS/State/`, `FounderOS/concepts/`, `FounderOS/projects/`.

**Reconstruction strategy:** Boot sequence reads CURRENT_STATE + PRIORITY_MATRIX + WATCH_REGISTRY on every session start. TIMELINE provides event history.

## Q4: Protocol Execution
| Gate | Automation |
|------|-----------|
| Temporal Check | Manual — SYSTEM_PROMPT.md rule #1 requires Get-Date before every response. LLM must execute. |
| Info Capture Scan | Manual — PRG Step 2 scans message against mapping table. LLM must execute. |
| Absorb Updates | Manual — LLM updates files before responding. |
| Project Data Room Scan | Manual — PRG Step 4 checks cascade. LLM must execute. |
| Freshness Flag | Manual — LLM checks footers before responding. |

**Failure behavior:** If a gate is skipped, the response is non-compliant. No technical enforcement — relies on LLM discipline.


--- FILE: Frameworks/Core/CAOS.md

# CAOS — Cash Allocation Operating System

## When to Use This Lens

Pricing decisions, resource allocation, survival mode, financial priorities.

## Required Questions

1. Cash available?
2. Does this expense serve survival or growth?
3. Expected return vs cost?
4. Risk of not making this allocation?
5. Does this allocation maximize the probability of mission success?

## Principles

- Resources are finite. Opportunities are infinite.
- Every allocation is simultaneously an investment and a rejection.
- The mission must receive resources before comfort.
- Compounding-effect assets deserve disproportionate investment.

## Allocation Hierarchy

Survival → Revenue → Capabilities → Assets → Scale → Frontier R&D

Unless there is strong justification for a different order.

## Survival Mode

Cash < 3 months of runway. Priority: Survival → Revenue → Fundraising.

## Anti-patterns

- Allocating without a defined outcome
- Spending on comfort before the mission
- Confusing activity with progress
- Budgeting on promises, not on cash


--- FILE: Frameworks/Core/CEOS.md

# CEOS — Content Execution Operating System

## When to Use This Lens

Content creation, distribution, conversion, hook analysis, audience strategy.

## Required Questions

1. Who is this content for? (cold / warm / hot)
2. What is the objective? (awareness / education / trust / lead / sale)
3. What is the next action for the viewer?
4. Why does this content exist?

## Principles

- People don't buy features. They buy results.
- Attention is scarce. Clarity > Complexity. Relevance > Volume.
- The first seconds determine everything. Immediate "Why should I care?"
- Distribution is not optional — it is part of the product.
- The hook operates on 3 layers: AUDIO > VISUAL > TEXT.

## Audience Layers

- **Cold**: doesn't know you → goal: Attention
- **Warm**: knows you → goal: Trust
- **Hot**: trusts you → goal: Action

## Anti-patterns

- Creating content without a defined objective
- Optimizing for likes/views instead of conversion
- Publishing without a clear CTA
- Textual hook without audio/visual disruptor on frame 1


--- FILE: Frameworks/Core/FAOS.md

# FAOS — Funnel Acquisition Operating System

## When to Use This Lens

Capital acquisition, sales funnel, activation, monetization, fundraising.

## Required Questions

1. What is the cheapest and fastest source of capital today?
2. Is the revenue validated or hypothetical?
3. Can we reach the objective without dilution?
4. Have we validated demand before scaling?
5. What is the acquisition cost vs customer lifetime value?

## Principles

- Capital is fuel, not the destination.
- Revenue is the best capital: non-dilutive, market-validated, repeatable.
- Capital hierarchy: Revenue > Partnerships > Grants > Angels > VC > Debt
- Never budget on promises. Always budget on cash.

## Runway States

- **Green** (>12 months): Growth
- **Yellow** (6-12 months): Revenue acceleration
- **Orange** (3-6 months): Survival + Revenue
- **Red** (<3 months): Immediate cash generation

## Anti-patterns

- Confusing fundraising with progress
- Premature dilution when revenue is possible
- Single dependency on one revenue source
- Waiting for funding to arrive instead of generating revenue


--- FILE: Frameworks/Core/PSOS.md

# PSOS — Product Strategy Operating System

## When to Use This Lens

Product strategy, offer validation, positioning, feature prioritization.

## Required Questions

1. What problem does this product solve?
2. Why this problem now?
3. Who has this problem and how many are willing to pay?
4. How will we know the product is valid?
5. What is the unique value proposition?

## Principles

- Products can change. Markets can change. The mission remains.
- Reality takes priority over beliefs, plans, and narratives.
- Prefer actions that create compounding assets.
- Seek leverage before effort: automation > systems > code > media > capital > team > personal work.

## Validation

Learn by executing. Do not wait to become an expert before building.

## Anti-patterns

- Attaching to a specific implementation (the mission is permanent, not the product)
- Accumulating knowledge without application
- Unnecessary complexity for elegance
- Waiting for perfection before launching


--- FILE: Frameworks/Core/SAOS.md

# SAOS — Systems Analysis Operating System

## When to Use This Lens

Design, audit, or debug of a system (architecture, project, workflow, organization).

## Required Questions

1. What are the components of the system?
2. What are the dependencies between components?
3. What is the boundary of each component?
4. What truth does each component own?
5. What truth does each component NOT own?
6. What is the single bottleneck?
7. What breaks if you remove X?
8. What is the single source of truth for each data?
9. Can the component be rebuilt if lost?
10. What is the cost of removing it?

## Principles

- A healthy system has clear boundaries between its components.
- Each component owns ONE truth and ONE only.
- The bottleneck is the single constraint that limits the entire system.
- A component that can be easily rebuilt has less value than one that cannot.
- Separation of responsibilities is the first defense against entropy.

## Analysis Steps

1. Map all components and their boundaries
2. Identify the truths each component owns
3. Trace dependencies between components
4. Find the bottleneck (the component that limits system throughput)
5. Test resilience: mentally remove each component and evaluate the impact
6. Verify Rule 0: each truth has exactly one owner

## Anti-patterns

- Components that own the same truth → duplication, contradiction
- Components without clear boundaries → inconsistency
- Components without their own truth → dead, useless
- System without an identified bottleneck → impossible to prioritize
- Adding components without checking boundaries against existing ones


--- FILE: Frameworks/Core/OOOS.md

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


--- FILE: Frameworks/Content/MAOS.md

# MAOS — Marketing Operating System

## When to Use This Lens

Marketing campaign, content plan, audience acquisition, brand positioning.

## Required Questions

1. What is the goal of this campaign? (awareness / acquisition / conversion / retention)
2. Which channel best reaches this target?
3. What is the unique message? In one sentence.
4. How do we measure success?
5. What is the expected cost per acquisition?
6. Is the message consistent across all channels?

## Principles

- Distribution and creation are equally important.
- One channel mastered > 5 channels skimmed.
- The message must change according to the funnel stage (cold → warm).
- Authenticity > polished production for local audiences.
- Test one channel at a time. Do not divide attention.

## Antipatterns

- Launching on 5 channels at the same time without testing
- Same message for cold and warm audiences
- Optimizing for vanity metrics (likes, views) without measuring conversion
- Changing strategy before collecting enough data


--- FILE: Frameworks/AI/AAOS.md

# AAOS — Automation & Agents Operating System

## When to Use This Lens

Agent design, workflow automation, reduction of repetitive manual tasks.

## Required Questions

1. Is this task repetitive? (frequency, duration, human cost)
2. Can it be standardized into deterministic steps?
3. What is the error tolerance of the automation?
4. Is the automation effort less than the cost of manual repetition?
5. What level of oversight is required (auto / approved / supervised)?
6. Does the automation create leverage or technical debt?

## Principles

- Automate only what is standardized and understood.
- Hierarchy: Documentation → Standardization → Automation → Delegation.
- Do not automate what changes every week.
- Automation without oversight generates noise.
- A poorly defined agent is worse than no agent at all.

## Antipatterns

- Automating before standardizing
- Automating a process you don't understand
- Creating an agent without clear boundaries (scope, authority, escalation)
- Confusing automation with human delegation


--- FILE: Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md

# AI Video Production — Entity-Based Framework

## When to Use This Lens

AI video production with recurring entities (characters, products, environments).

## Core Principle

AI Video is not about prompts. AI Video is about entities. Prompts are generated from entities.

Every element visible on screen is an entity. Consistency is achieved through entity persistence.

## Required Structure Before Production

1. **Entity Registry** — ENTITY_REGISTRY.md with ENTITY_ID, Type, Name
2. **Entity Sheets** — PERSON_SHEET, PRODUCT_SHEET, LOCATION_SHEET per entity
3. **Environment System** — light, atmosphere, weather, mood, color palette
4. **Action System** — reusable actions: Actor (ENTITY_ID), Action, Object, Emotion, Duration
5. **Scene System** — entities + environment + actions + narrative objective
6. **Frame System** — START_FRAME, END_FRAME mandatory before generation
7. **Video Prompt Generation** — downstream, only after all dependencies exist

## Quality gates

- Entity Sheets exist ✓
- Environment Sheets exist ✓
- Action Sheets exist ✓
- Scene Sheets exist ✓
- Frame Assets exist ✓

If a gate is red: STOP. Generate the missing assets before continuing.

## FounderOS Rule

Don't think in prompts. Think in entities.
Don't think in clips. Think in scenes.
Don't think in videos. Think in systems.

## Content types supported

ADVERTISEMENT, DOCUMENTARY, PODCAST, EDUCATIONAL, STORYTELLING, FOUNDER_JOURNAL, NEWS


--- FILE: Frameworks/VSOS.md

# FounderOS V4 — VSOS
## Venture Structuring Operating System

### Transform any idea, project or opportunity into an executable system

---

## 1. What is VSOS?

VSOS is FounderHQ's strategic transformation methodology. It takes a fuzzy input (idea, project, opportunity, problem) and produces a structured output: a complete document cascade, from Vision to execution system.

VSOS is not a daily module. It is a **lens** loaded when you need to create a new project, restructure an existing project, prepare a fundraising round, or transform a vision into execution.

VSOS has already been used on KORA and Omni (without being named). It is now an explicit framework.

---

## 2. When to Use VSOS

| Situation | Action |
|-----------|--------|
| New idea / new project | Full VSOS (Phase 1 → 3) |
| Existing project without structure | VSOS Audit + Phase 2 → 3 |
| Restructuring / reframe | VSOS Audit + Mission Extraction |
| Fundraising preparation | VSOS Phase 3 (Capital Roadmap + BP) |
| Strategic blockage | VSOS Gap Analysis |

**Do not use:** for daily operations (DAOS), quick decisions (DECISION_ENGINE), content (CEOS).

---

## 3. Architecture VSOS

### Input
```
Idea
Existing project
Company
Opportunity
Problem
```

### The 3 Phases

```
PHASE 1: DIAGNOSTIC
├── Reality Assessment
├── Mission Extraction
└── Gap Analysis

PHASE 2: STRATEGIC CASCADE
├── Vision
├── Mission
├── Theory of Change
├── Strategic Assets Map
└── Master Plan

PHASE 3: EXECUTION FRAMEWORK
├── Strategic Roadmap
├── Capital Roadmap
├── Business Plan
└── Execution System (KPIs, milestones)
```

### Output
```
Data Room complète dans projects/<PROJECT>/
├── 01_VISION.md
├── 02_MISSION.md
├── 03_THEORY_OF_CHANGE.md
├── 04_STRATEGIC_ASSETS_MAP.md
├── 05_MASTER_PLAN.md
├── 06_STRATEGIC_ROADMAP.md
├── 07_CAPITAL_ROADMAP.md
├── 08_EXECUTIVE_SUMMARY.md
├── 09_BUSINESS_PLAN.md
├── 10_PITCH_DECK.md
└── annexes/
```

---

## 4. Phase 1 — Diagnostic

To do before any strategic cascade. Understand where you are before deciding where you're going.

### 4.1 Reality Assessment

Questions to answer:
- What is the current state of the project / idea?
- What already exists? (MVP, team, traction, revenue, docs)
- What are the constraints? (cash, time, skills, market)
- What is the fundamental problem being solved?

**Output:** A section in CURRENT_STATE.md or a diagnostic memo.

### 4.2 Mission Extraction

Extract the project's mission, whether explicit or implicit:
- Why does this project exist?
- For whom?
- What is the desired change?
- In 5-10-20 years, what does success look like?

**Output:** A mission draft (will be refined in Phase 2).

### 4.3 Gap Analysis

Identify the gap between the current state and the mission:
- What is missing? (data, team, funding, traction)
- What are the blockages?
- What is the main risk?
- What is the next most important action?

**Output:** Gap list + prioritization.

**Associated modules:** RIOS.md (research) can be invoked to dig into the gaps.

---

## 5. Phase 2 — Strategic Cascade

Build the 5 fundamental documents that form the strategic framework of the project.

### 5.1 Vision (projects/X/01_VISION.md)

**Horizon:** 10-25 years. Independent of products, technologies, funding.

**Elements:**
- Vision Statement (1 paragraph, the desired future)
- The future we want to create (why the status quo is unacceptable)
- Our core conviction (why our approach is the right one)
- Our vision of infrastructure (what we are building)
- Our vision of societal impact (education, health, economy, culture)
- Success horizon (when will we know we have succeeded?)
- Critical OODA (why this vision will survive technological changes)

**Template section Critical OODA:**
```
Cette vision est volontairement indépendante des [technologies/marchés] actuels.
Elle reste valable même si [X, Y, Z] disparaissent.
Une bonne vision doit survivre à plusieurs générations technologiques.
```

### 5.2 Mission (projects/X/02_MISSION.md)

**What the organization does every day.**

**Elements:**
- Mission statement (1 sentence)
- Why we exist
- What we do (5 core capabilities)
- What we ARE NOT (to avoid scope creep)
- Our execution principles (5 max)
- How we measure success
- Current priority

### 5.3 Theory of Change (projects/X/03_THEORY_OF_CHANGE.md)

**The logical chain: how vision becomes reality.**

**Elements:**
- Structural deficits (why the problem exists)
- Central hypothesis (IF... THEN...)
- Causal relationships (chain: no X → no Y)
- The transformation chain (step by step)
- Expected results (short, medium, long term)
- The fundamental hypothesis (the real bet we're making)

### 5.4 Strategic Assets Map (projects/X/04_STRATEGIC_ASSETS_MAP.md)

**What we accumulate, why it's hard to replicate.**

**Elements:**
- List of assets by replication difficulty
- For each asset: what it is, why it's hard to copy
- Table: Asset / Difficulty / Time / Competitive Advantage
- The most important asset (the "castle")

### 5.5 Master Plan (projects/X/05_MASTER_PLAN.md)

**The overall development framework.**

**Elements:**
- Executive summary
- Strategic thesis
- The 6 (or X) strategic layers
- Execution timeline by phase
- Strategic principles (5 max)

---

## 6. Phase 3 — Execution Framework

Transform strategy into concrete, fundable, and measurable plans.

### 6.1 Strategic Roadmap (projects/X/06_STRATEGIC_ROADMAP.md)

**When we do what.**

**Elements:**
- North Star (the direction)
- Phases with: period, objective, deliverables, budget
- Key milestones with target dates and indicators

### 6.2 Capital Roadmap (projects/X/07_CAPITAL_ROADMAP.md)

**How we finance each phase.**

**Elements:**
- Capital thesis
- Funding architecture (5 layers: founder, non-dilutive, partnerships, revenue, equity)
- Use of funds (detailed table)
- Funding rule (don't raise until the previous milestone is proven)

### 6.3 Business Plan (projects/X/09_BUSINESS_PLAN.md)

**Phase 1: the plan for the first milestone.**

**Elements:**
- Executive Summary (1 page)
- The problem (detailed)
- The opportunity
- The solution
- Phase 1 objectives
- The business model
- Phase 1 roadmap
- Use of Funds
- Risks and mitigations
- Investment request

### 6.4 Execution System (projects/X/annexes/A3_KPIS_MILESTONES.md)

**How we measure and track.**

**Elements:**
- Milestones with target months
- KPIs with quantified targets
- Review frequency
- Who is responsible

---

## 7. VSOS in the FounderHQ Ecosystem

### Modules invoked during VSOS

| Module | Role during VSOS |
|--------|------------------|
| **VEAOS** | Vision/mission refinement, strategic scenarios |
| **RIOS** | Market research, competitors, gaps |
| **FAOS** | Fundraising strategy (Phase 3) |
| **DIOS** | Distribution strategy (after VSOS) |
| **CEOS** | Content strategy (after VSOS) |

### Post-VSOS

Once VSOS is completed, the project is registered via PROJECT_REGISTRATION_PROTOCOL.md:
1. Create `concepts/<PROJECT>.md`
2. Add to `State/CURRENT_STATE.md`
3. Add to `State/PRIORITY_MATRIX.md`
4. Add the relationships in the relevant concepts

---

## 8. Use Cases (already executed)

### KORA — AI Lab (African languages)
- Input: AI infrastructure idea for African languages
- VSOS: Complete (Phase 1 → 3)
- Output: 20 files in `projects/KORA/`
- Status: Pre-Seed ready

### OMNI — Local commerce index
- Input: Existing MVP + pitch deck
- VSOS: Phase 2 → 3 (Diagnostic skipped because project was already advanced)
- Output: 20 files in `projects/Omni/`
- Status: Hub outreach file ready

### Financial Literacy Program
- Input: Generic course to customize
- VSOS: Audit + Reframe (adapt to FounderHQ context)
- Output: 28 concepts rewritten with real examples
- Status: 2/28 completed

---

## 9. Template: Quick VSOS (1 hour)

For quick projects (e.g., Pest Repeller, Solar Kit, TikTok channel):

```
1. Reality Assessment (5 min) — Where am I?
2. Mission (5 min) — Why does this project exist?
3. Assets (5 min) — What do I already have?
4. Roadmap (10 min) — The next 3 actions
5. BP 1-pager (15 min) — Simple business model
6. KPIs (5 min) — How do I know if it works?
7. Register (15 min) — Create concept + PRIORITY_MATRIX entry
```

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Type | Framework |
| Owner | System |
| Dependencies | VEAOS, RIOS, FAOS, PROJECT_REGISTRATION_PROTOCOL |


--- FILE: Frameworks/Specialized/Venture/VAOS.md

# FounderOS V4 — VAOS (Venture Architecture Operating System)

## Identity

VAOS is the venture creation and structuring engine of FounderHQ. It transforms an idea into an executable, fundable, scalable venture — step by step.

## Mission

Transform any idea into a venture that can be executed, funded, and scaled.

## Position in FounderHQ

IDEA
↓
**VAOS**
↓
VISION → MISSION → THEORY_OF_CHANGE → ASSET_MAP → PLAN → ROADMAP → CAPITAL → BP
↓
EXECUTION (FounderHQ operations)
↓
DISTRIBUTION (DIOS)
↓
REVENUE

## Related Systems

- **DIOS** — receives the structured venture and distributes it
- **CEOS** — produces content for the venture
- **FAOS** — fundraising and capital strategy (operational partner)
- **CAOS** — pricing and allocation within the venture

## VAOS Workflow

STEP 0: Receive raw idea
STEP 1: Load VISION_ENGINE → define the transformation of reality
STEP 2: Load MISSION_ENGINE → define the approach and reason for being
STEP 3: Load THEORY_OF_CHANGE → if A → then B → therefore C
STEP 4: Load ASSET_MAPPING → inventory of what we have and what we need
STEP 5: Load STRATEGIC_PLANNING → plan of attack
STEP 6: Load ROADMAP_ENGINE → phases and milestones
STEP 7: Load CAPITAL_STRATEGY → funding approach (debt, equity, grants)
STEP 8: Load BUSINESS_PLAN_ENGINE → executable and fundable BP
STEP 9: Hand off to FounderHQ operations for execution
STEP 10: After execution, load CONSTRAINT_ANALYSIS or VENTURE_REPOSITIONING if needed

## Sub-modules

| Module | Path |
|--------|------|
| VISION_ENGINE | VAOS/VISION_ENGINE.md |
| MISSION_ENGINE | VAOS/MISSION_ENGINE.md |
| THEORY_OF_CHANGE | VAOS/THEORY_OF_CHANGE.md |
| ASSET_MAPPING | VAOS/ASSET_MAPPING.md |
| STRATEGIC_PLANNING | VAOS/STRATEGIC_PLANNING.md |
| ROADMAP_ENGINE | VAOS/ROADMAP_ENGINE.md |
| CAPITAL_STRATEGY | VAOS/CAPITAL_STRATEGY.md |
| BUSINESS_PLAN_ENGINE | VAOS/BUSINESS_PLAN_ENGINE.md |
| CONSTRAINT_ANALYSIS | VAOS/CONSTRAINT_ANALYSIS.md |
| VENTURE_REPOSITIONING | VAOS/VENTURE_REPOSITIONING.md |

## Definition of Success

A successful VAOS execution produces a venture that:
1. Has a clear vision and mission
2. Has a testable theory of change
3. Identifies strategic assets and gaps
4. Has a phased roadmap with capital requirements
5. Has a BP that can be shown to investors or partners

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | System |
| Dependencies | FAOS.md, CAOS.md, DIOS.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/ASSET_MAPPING.md

# VAOS — ASSET_MAPPING

## Mission

Inventory what the venture already has and identify what it critically needs.

## Core Rule

You cannot build a strategy on what you wish you had. You build it on what you actually have.

## Asset Categories

| Category | Examples | Where to Look |
|----------|----------|---------------|
| Relationships | Suppliers, partners, mentors, customers | ASSET.md, MEMORY.md |
| Knowledge | Domain expertise, validated patterns | KNOWLEDGE.md |
| Resources | Cash, inventory, equipment, tools | CURRENT_STATE.md, ASSET.md |
| Skills | Founder capabilities, team skills | MEMORY.md |
| Distribution | Platforms, audiences, channels | ASSET.md, DIOS |
| Reputation | Brand, testimonials, social proof | ASSET.md |

## Mapping Process

1. List everything you have in each category
2. Rate each: CRITICAL / NICE_TO_HAVE / IRRELEVANT
3. For each gap in CRITICAL: document what's needed and how to acquire it
4. Identify which existing assets can be leveraged for which gaps

## Example (SOJACO)

| Asset | Category | Rating | Gap |
|-------|----------|--------|-----|
| Atakpamé supplier (350/kg) | Relationship | CRITICAL | Need better price |
| Ami maïs (160/kg) | Relationship | CRITICAL | Need client |
| No cash for bulk | Resource | CRITICAL | Need 19k FCFA/sac |
| Cereal trading knowledge | Knowledge | NICE | — |
| Lomé delivery network | Relationship | NICE | — |

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | STRATEGIC_PLANNING.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/BUSINESS_PLAN_ENGINE.md

# VAOS — BUSINESS_PLAN_ENGINE

## Mission

Produce an executable and fundable business plan from the VAOS cascade.

## Core Rule

A business plan is not a document. It's a decision-making tool. If writing it doesn't change what you do, you're doing it wrong.

## BP Structure

1. **Executive Summary** — 1 page: problem, solution, market, traction, ask
2. **Vision & Mission** — from VISION_ENGINE + MISSION_ENGINE
3. **Theory of Change** — from THEORY_OF_CHANGE
4. **Market Analysis** — size, segments, competition, positioning
5. **Product/Service** — what you offer, how it works, unit economics
6. **Go-to-Market** — from STRATEGIC_PLANNING + ROADMAP_ENGINE
7. **Assets & Gaps** — from ASSET_MAPPING
8. **Financial Plan** — revenue model, cost structure, P&L, cash flow
9. **Capital Strategy** — from CAPITAL_STRATEGY
10. **Risk Analysis** — key risks + mitigation

## VAOS Generation Flow

```
BUSINESS_PLAN_ENGINE collects from:
VISION_ENGINE → Section 2
MISSION_ENGINE → Section 2
THEORY_OF_CHANGE → Section 3
ASSET_MAPPING → Section 7
STRATEGIC_PLANNING → Section 6
ROADMAP_ENGINE → Section 6
CAPITAL_STRATEGY → Section 9
CONSTRAINT_ANALYSIS → Section 10
```

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | All VAOS sub-modules |


--- FILE: Frameworks/Specialized/Venture/VAOS/CAPITAL_STRATEGY.md

# VAOS — CAPITAL_STRATEGY

## Mission

Determine how the venture will be funded at each stage, from bootstrap to scale.

## Core Rule

The best capital is the one that costs the least in control and freedom. Bootstrap first, debt second, equity last.

## Capital Sources (Lomé/West Africa)

| Source | Amount | Cost | Best For |
|--------|--------|------|----------|
| Personal cash | 1k-50k FCFA | 0% | First test |
| Revenue | Variable | 0% | Growth |
| Microfinance (FUCEC, ALIDé) | 50k-500k FCFA | 15-30% APR | Working capital |
| Assilassimé Coup de Pouce | 5k-20k FCFA | 0% | Emergency |
| Grants (local tech hub, etc.) | 500k-5M FCFA | 0% + reporting | R&D, impact |
| Angel investment | 1M-50M FCFA | 10-30% equity | Scaling |
| Venture capital | 50M+ FCFA | 20-40% equity | Hypergrowth |

## Strategy by Phase

| Phase | Source | Max Amount |
|-------|--------|------------|
| Validation (MVP) | Personal + revenue | 50k FCFA |
| Launch (first sales) | Revenue + microfinance | 500k FCFA |
| Growth (scale) | Revenue + grants | 5M FCFA |
| Expansion (new markets) | Angel / VC | 50M+ FCFA |

## Key Principle

Never raise equity for working capital (stock, salaries). Use debt or revenue. Equity is for assets that appreciate (tech, IP, brand).

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | BUSINESS_PLAN_ENGINE.md, FAOS.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/CONSTRAINT_ANALYSIS.md

# VAOS — CONSTRAINT_ANALYSIS

## Mission

Identify the single constraint preventing progress and determine how to remove it.

## Core Rule

There is always ONE bottleneck. If you list more than one, the real bottleneck is hiding behind the others.

## Method

1. **Identify** — what is the most constrained resource? (cash, attention, trust, time, skill, relationship)
2. **Verify** — does relaxing this constraint measurably accelerate the venture?
3. **Analyze** — why is this constraint here? What caused it?
4. **Resolve** — what action removes or bypasses it?
5. **Repeat** — after resolution, the next constraint appears. Find it.

## Common Constraints

| Constraint | Symptom | Solution Path |
|------------|---------|--------------|
| Cash | Can't buy stock, can't run ads | Revenue first, then microfinance |
| Attention | 0 views, 0 DMs, 0 traffic | DIOS: fix hook, platform, offer |
| Trust | 0 sales despite views | Testimonials, guarantee, local proof |
| Time | Founder stretched across 7 projects | Focus on 1 revenue project |
| Skill | Can't execute key action | Learning pipeline (LEOS) |
| Relationship | No supplier, no partner | Outreach, cold call, network |

## Example (Current State)

- **Bottleneck:** Cash (2,679 FCFA accessible)
- **Cause:** No revenue cycle completed yet
- **Constraint tree:** No cash → no stock → no sales → no cash
- **Break point:** Find client for maïs (0 FCFA cost) → validate demand → then buy stock

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | VENTURE_REPOSITIONING.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/MISSION_ENGINE.md

# VAOS -- MISSION_ENGINE

## Mission

Define the approach the venture takes to achieve its vision.

## Core Rule

Mission answers: what do we do, for whom, and how? It is narrower than the vision. The vision is the destination; the mission is the vehicle.

## Mission Template

`
[Venture] exists to [action] for [audience] through [approach].
`

## Examples

### Kora
> Kora exists to build African AI research infrastructure through a distributed compute network, curated datasets, and a talent pipeline from West African universities.

### SOJACO
> SOJACO exists to supply Togolese cereal resellers with competitive pricing through payment-on-delivery, removing the cash advance barrier.

## Mission Test

A mission passes if:
- It's specific enough to say "no" to things outside it
- It describes what you do, not just what you believe
- A new person can read it and know if they should care

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | VISION_ENGINE.md, THEORY_OF_CHANGE.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/ROADMAP_ENGINE.md

# VAOS — ROADMAP_ENGINE

## Mission

Translate the strategic plan into a time-bound, phase-gated roadmap.

## Core Rule

A roadmap is a communication tool, not a prediction. It tells stakeholders what to expect and when to expect decisions.

## Roadmap Template

```
Phase 1: [name] — [start] → [end]
Goal: [what we prove in this phase]
Gate: [what must be true to proceed]
Budget: [resources allocated]

  Milestone 1: [date] — [outcome]
  Milestone 2: [date] — [outcome]
  ...

Phase 2: [name] — [start] → [end]
...
```

## Phase Gates

Each phase ends with a gate. The gate answer is YES, NO, or ITERATE:
- YES → proceed to next phase
- NO → pivot or kill the venture
- ITERATE → rework the phase with learnings

## Example (SOJACO)

| Phase | Duration | Gate | Pass? |
|-------|----------|------|-------|
| Find client maïs | 7 jours | Client confirmé à ≥ 500/bol | 🟡 En cours |
| 1ère livraison | 3 jours | Paiement reçu AVANT réappro | ⏳ |
| Scale à 3 clients | 30 jours | 3 clients réguliers, marge > 50k/mois | ⏳ |

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | STRATEGIC_PLANNING.md, CAPITAL_STRATEGY.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/STRATEGIC_PLANNING.md

# VAOS — STRATEGIC_PLANNING

## Mission

Define the plan of attack: what to do, in what order, with what resources.

## Core Rule

A strategic plan is a sequence of bets. Each bet has a cost, an expected outcome, and a fallback.

## Plan Template

```
Objective: [what we're trying to achieve]
Timeframe: [duration]
Resources: [cash, people, tools]
Constraints: [what limits us]

Phase 1: [name]
- Action: [what we do]
- Cost: [resources consumed]
- Success: [how we know it worked]
- Fallback: [what if it fails]

Phase 2: [name]
- ...
```

## Planning Principles

1. **One bet at a time** — never start Phase 2 before Phase 1 results are in
2. **Smallest test first** — validate the riskiest assumption with the least resources
3. **Cash-aware** — every phase must be fundable from previous phase outcomes
4. **Time-boxed** — each phase has a maximum duration; if not done by then, reassess

## Example (SOJACO Sprint)

| Phase | Action | Cost | Success | Duration |
|-------|--------|------|---------|----------|
| 1 | Find client maïs à prix viable | 0 FCFA | 1 client confirmé | 7 jours |
| 2 | Livrer 1er sac maïs | 19k FCFA | Paiement reçu | 3 jours |
| 3 | Réinvestir dans 2ème sac | 19k FCFA | Cycle répété | 7 jours |

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | ASSET_MAPPING.md, ROADMAP_ENGINE.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/THEORY_OF_CHANGE.md

# VAOS -- THEORY_OF_CHANGE

## Mission

Make explicit the???? chain from actions to outcomes to impact.

## Core Rule

If you cannot state your theory of change in 3 "if-then" statements, you don't understand your own venture.

## Template

`
If [we do this action],
then [this immediate outcome]
because [this reason].

If [this immediate outcome],
then [this intermediate outcome]
because [this reason].

If [this intermediate outcome],
then [this long-term impact]
because [this reason].
`

## Example (SOJACO)

1. If we find buyers at >1,000 FCFA/bol soja and >500 FCFA/bol maïs, then we can secure first delivery because suppliers accept payment at delivery.

2. If we execute 3 successful deliveries, then resellers trust us with larger orders because we've proven reliability.

3. If we build a reliable reseller network, then we can aggregate demand and negotiate better supplier prices, creating a sustainable margin.

## Theory of Change Test

A ToC passes if:
- Each link is falsifiable (you can test it)
- There are no magical leaps (A ? C without B)
- A skeptic would agree that IF the inputs happen, the outputs are plausible

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | VISION_ENGINE.md, MISSION_ENGINE.md |


--- FILE: Frameworks/Specialized/Venture/VAOS/VENTURE_REPOSITIONING.md

# VAOS — VENTURE_REPOSITIONING

## Mission

Fix a venture that is not working by changing its fundamental structure, not just its tactics.

## Core Rule

If a venture is stuck despite good execution, the problem is structural. Tactical fixes (better hook, better post, better price) only work when the structure is sound.

## When to Reposition

- 0 traction after 30 days of consistent execution
- Cash burn exceeds revenue with no clear path to breakeven
- Market feedback contradicts core assumptions
- Founder has lost conviction in the venture

## Repositioning Process

1. **Reality Assessment** — what actually happened? (data, not opinions)
2. **Constraint Mapping** — what is the real bottleneck? (CONSTRAINT_ANALYSIS)
3. **Assumption Audit** — which of our original bets were wrong?
4. **Strategic Options** — generate 3 options: Pivot, Iterate, Kill
5. **Decision** — choose one with clear rationale
6. **New Cascade** — rewrite VISION → MISSION → ToC → PLAN with new assumptions

## Options

| Option | When | Example |
|--------|------|---------|
| Pivot | Core assumption wrong, but venture has valuable assets | SOJACO: soja → maïs |
| Iterate | Core assumption right, execution wrong | Pest Repeller: new hook layer |
| Kill | Nothing salvageable | Zoclo: regulatory risk too high |
| Pause | Right idea, wrong timing | Resume when conditions change |

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | CONSTRAINT_ANALYSIS.md, all VAOS modules |


--- FILE: Frameworks/Specialized/Venture/VAOS/VISION_ENGINE.md

‣䅖协霠嘠卉佉彎久䥇䕎ਊ⌣䴠獩楳湯ਊ敄楦敮琠敨琠慲獮潦浲瑡潩⁮景爠慥楬祴琠慨⁴桴獩瘠湥畴敲攠楸瑳⁳潴挠畡敳ਮ⌊‣潃敲删汵੥䄊瘠獩潩⁮獩渠瑯愠朠慯⹬䄠瘠獩潩⁮敤捳楲敢⁳桴⁥潷汲⁤䙁䕔⁒桴⁥敶瑮牵⁥畳捣敥獤‮瑉愠獮敷獲›桷瑡椠⁳楤晦牥湥㽴ਊ⌣嘠獩潩⁮敔灭慬整ਊ੠湉嬠楴敭牦浡嵥‬睛潨⁝楷汬嬠桷瑡⁝敢慣獵⁥癛湥畴敲⹝ਊ敂潦敲›捛牵敲瑮爠慥楬祴霠琠敨瀠潲汢浥੝晁整㩲嬠畦畴敲爠慥楬祴霠琠敨猠汯瑵潩嵮怊ਊ⌣䔠慸灭敬⠠潋慲਩㸊䤠⁮‵敹牡ⱳ䄠牦捩湡䄠⁉敲敳牡档牥⁳楷汬戠極摬猠癯牥楥湧䄠䥇漠⁮晁楲慣⁮湩牦獡牴捵畴敲戠捥畡敳䬠牯⁡牰癯摩獥琠敨挠浯異整‬慤慴‬湡⁤慴敬瑮瀠灩汥湩⹥㸊㸊䈠晥牯㩥䄠牦捩湡䄠⁉慴敬瑮氠慥敶⁳潦⁲单䔯⁕敢慣獵⁥桴牥❥⁳潮挠浯異整漠⁲敲敳牡档攠潣祳瑳浥愠⁴潨敭ਮ‾晁整㩲圠獥⁴晁楲慣栠獡椠獴漠湷䄠⁉敲敳牡档栠扵瀠扵楬桳湩⁧瑡琠灯瘠湥敵⁳湡⁤敤汰祯湩⁧敲污猠汯瑵潩獮ਮ⌊‣楖楳湯吠獥ੴ䄊瘠獩潩⁮慰獳獥椠㩦ⴊ䤠⁴硥楣整⁳潳敭湯⁥桷⁯潤獥❮⁴潷歲映牯礠畯ⴊ䤠⁴敤捳楲敢⁳⁡敲污挠慨杮ⱥ渠瑯愠瀠潲畤瑣映慥畴敲ⴊ夠畯挠湡攠灸慬湩椠⁴湩ㄠ猠湥整据੥⌊‣潆瑯牥ਊ⁼楆汥⁤⁼慖畬⁥੼⵼ⴭⴭⴭ⵼ⴭⴭⴭ੼⁼协嘠牥楳湯簠嘠‴੼⁼慌瑳嘠牥晩敩⁤⁼〲㘲〭ⴶㄲ簠簊传湷牥簠嘠佁⁓੼⁼敄数摮湥楣獥簠䴠卉䥓乏䕟䝎义⹅摭簠਍

--- FILE: Frameworks/Specialized/Distribution/DIOS.md

# FounderOS V4 — DIOS (Distribution Intelligence Operating System)

## Identity

DIOS (Distribution Intelligence Operating System) is the commercial nervous system of FounderHQ.

## Mission

Transform any offer into attention, attention into trust, trust into conversion, and conversion into reusable knowledge.

## Position in FounderHQ

MISSION
↓
PROJECT
↓
**DIOS**
↓
CEOS
↓
AI_VIDEO_MASTER_DOMAIN
↓
PUBLICATION
↓
DISTRIBUTION_MEMORY
↓
KNOWLEDGE

## Related Systems

- **VAOS** (Frameworks/Specialized/Venture/VAOS.md) — structures the venture before DIOS distributes it
- **CEOS** — receives DIOS strategy, produces content
- **AI_VIDEO_MASTER_DOMAIN** — receives CEOS specs, produces video + distribution package
- **FAOS** — funnel / conversion models
- **CAOS** — pricing / cash constraints
- **DISTRIBUTION_MEMORY** — stores campaign results

## DIOS Workflow

STEP 1: Receive offer (product, price, objective, constraints)
STEP 2: Load AUDIENCE_INTELLIGENCE → identify market + min 3 audiences, select primary
STEP 3: Load LANGUAGE_INTELLIGENCE → derive language(s) from market
STEP 4: Load PLATFORM_INTELLIGENCE → select platform(s) per audience behavior
STEP 5: Load HOOK_INTELLIGENCE → create angle(s) + generate/filter hooks
STEP 6: Load OFFER_INTELLIGENCE → choose CTA + counter objection
STEP 7: Send distribution strategy to CEOS for production
STEP 8: Receive performance data → update DISTRIBUTION_MEMORY + KNOWLEDGE

## Sub-modules

| Module | Path |
|--------|------|
| AUDIENCE_INTELLIGENCE | DIOS/AUDIENCE_INTELLIGENCE.md |
| LANGUAGE_INTELLIGENCE | DIOS/LANGUAGE_INTELLIGENCE.md |
| PLATFORM_INTELLIGENCE | DIOS/PLATFORM_INTELLIGENCE.md |
| HOOK_INTELLIGENCE | DIOS/HOOK_INTELLIGENCE.md |
| OFFER_INTELLIGENCE | DIOS/OFFER_INTELLIGENCE.md |
| DISTRIBUTION_INTELLIGENCE | DIOS/DISTRIBUTION_INTELLIGENCE.md |
| CONVERSION_INTELLIGENCE | DIOS/CONVERSION_INTELLIGENCE.md |
| DISTRIBUTION_MEMORY | DIOS/DISTRIBUTION_MEMORY.md |

## KPIs

Reach | Views | Retention | CTR | Messages | Leads | Conversions | Revenue | ROI

## Definition of Success

A successful campaign is not a beautiful video. A successful campaign is:
Attention → Trust → Action → Sale → Learning

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | CEOS.md, AI_VIDEO_MASTER_DOMAIN.md, FAOS.md, CAOS.md, concepts/DISTRIBUTION_MEMORY.md, concepts/KNOWLEDGE.md |


--- FILE: Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md

‣䥄协霠䄠䑕䕉䍎彅义䕔䱌䝉久䕃ਊ⌣䴠獩楳湯ਊ摉湥楴祦瀠敲楣敳祬眠潨洠獵⁴敳⁥桴⁥潣瑮湥⹴ਊ⌣䌠牯⁥畒敬ਊ畁楤湥散㼠倠潲畤瑣ਮ䔊敶祲漠晦牥栠獡洠汵楴汰⁥楤瑳湩瑣愠摵敩据獥‮慅档渠敥獤愠搠晩敦敲瑮栠潯Ⱬ搠晩敦敲瑮猠潴祲‬楤晦牥湥⁴呃⹁ਊ䥄协椠敤瑮晩敩⁳瑡氠慥瑳㌠搠獩楴据⁴畡楤湥散⁳敢潦敲挠潨獯湩⁧桴⁥牰浩牡⁹慴杲瑥ਮ⌊‣敍桴摯ਊ⸱䰠獩⁴桴⁥牰扯敬⁭桴⁥牰摯捵⁴潳癬獥㈊‮潆⁲慥档瀠潲汢浥㼠眠潨攠灸牥敩据獥椠⁴潭瑳愠畣整祬ਿ⸳䘠牯攠捡⁨牧畯⁰‿桷瑡椠⁳桴楥⁲灳捥晩捩映畲瑳慲楴湯搯獥物⽥敦牡ਿ⸴䘠牯攠捡⁨牧畯⁰‿桷牥⁥潤琠敨⁹潣獮浵⁥潣瑮湥㽴㔊‮敓敬瑣瀠楲慭祲愠摵敩据⁥‫敳潣摮牡⁹畡楤湥散瀠牥挠浡慰杩੮⌊‣敐獲湯⁡敔灭慬整ਊ੠畁楤湥散›湛浡嵥倊潲汢浥›睛慨⁴桴祥猠晵敦⁲牦浯੝潈歯愠杮敬›睛慨⁴慭敫⁳桴浥猠潴⁰捳潲汬湩嵧䰊湡畧条㩥嬠敤楲敶⁤牦浯洠牡敫⁴‫畡楤湥散੝汐瑡潦浲›睛敨敲琠敨⁹灳湥⁤楴敭੝呃㩁嬠桷瑡愠瑣潩⁮桴祥眠汩⁬慴敫੝扏敪瑣潩㩮嬠桷⁹桴祥眠畯摬猠祡渠嵯怊ਊ⌣䔠慸灭敬⠠敐瑳删灥汥敬⥲ਊ⁼畁楤湥散簠䠠潯⁫⁼汐瑡潦浲簠簊ⴭⴭⴭⴭⴭ⵼ⴭⴭ簭ⴭⴭⴭⴭⴭ੼⁼慐敲瑮⁳攨普湡獴 ⁼牐瑯柩牥戠择⃩敤⁳潭獵楴畱獥氠⁡畮瑩簠吠歩潔Ⱬ圠慨獴灁⁰੼⁼敆浭獥攠据楥瑮獥簠倠潲敧⁲慬朠潲獳獥敳搠⁵慰畬楤浳⁥⁼楔呫歯簠簊䌠浯敭湡獴簠倠潲敧⁲敬猠潴正‬潤浲物瀠畯⁲潢獳牥簠䘠捡扥潯Ⱬ圠慨獴灁⁰੼⁼整獬簠䌠湯潦瑲挠楬湥ⱴ愠楶⁳潂歯湩⁧⁼慆散潢歯簠簊줠潣敬⁳⁼潃据湥牴瑡潩⁮泩盨獥‬潣普慩据⁥慰敲瑮⁳⁼桗瑡䅳灰簠ਊ⌣䔠慸灭敬⠠楋⁴潓慬物⥥ਊ⁼畁楤湥散簠䠠潯⁫⁼汐瑡潦浲簠簊ⴭⴭⴭⴭⴭ⵼ⴭⴭ簭ⴭⴭⴭⴭⴭ੼⁼慐敲瑮⁳⁼湅慦瑮爠盩獩⁥⃠慬戠畯楧⁥敤異獩㌠洠楯⁳⁼楔呫歯簠簊倠瑥瑩⁳潣浭牥懧瑮⁳⁼敐瑲⁥敤猠潴正焠慵摮氠敬瑣楲楣瀠牡⁴⁼慆散潢歯簠簊嘠湥敤牵⁳敤爠敵簠删捥慨杲牥琠泩烩潨敮瀠畯⁲敬⁳汣敩瑮⁳⁼楔呫歯‬桗瑡䅳灰簠ਊ⌣䘠潯整ੲ簊䘠敩摬簠嘠污敵簠簊ⴭⴭⴭ簭ⴭⴭⴭ簭簊传⁓敖獲潩⁮⁼㑖簠簊䰠獡⁴敖楲楦摥簠㈠㈰ⴶ㘰㈭‱੼⁼睏敮⁲⁼䥄协簠簊䐠灥湥敤据敩⁳⁼䅌䝎䅕䕇䥟呎䱅䥌䕇䍎⹅摭‬䱐呁但䵒䥟呎䱅䥌䕇䍎⹅摭簠਍

--- FILE: Frameworks/Specialized/Distribution/DIOS/CONVERSION_INTELLIGENCE.md

# DIOS — CONVERSION_INTELLIGENCE

## Mission

Transform attention into action and action into payment.

## Core Rule

Every view is a potential conversation. Every conversation is a potential sale. The CTA is the bridge.

## The Conversion Funnel (Lomé Context)

```
View (TikTok/FB/WA)
  ↓
Message (WhatsApp)
  ↓
Question (price, availability, delivery)
  ↓
Trust (testimonial, guarantee, local proof)
  ↓
Agreement (yes, I want it)
  ↓
Payment (Wave, Orange Money, cash on delivery)
  ↓
Delivery (same-day motorcycle courier)
```

## CTA Design Principles

1. **One action per post** — never give 2 options in one CTA
2. **Lowest friction wins** — "Écris 'stop' sur WhatsApp" > "Clique le lien dans la bio"
3. **Urgency without pressure** — "Stock limité à Lomé" > "Dernière chance"
4. **Direct instruction** — "Tape 'prix' en commentaire" > "Dis-moi ce que t'en penses"
5. **Localize the action** — "Envoie un message Wave au 71 39 21 22" > "Buy now"

## WhatsApp Conversion Script

**When someone messages:**
1. Répondre dans l'heure (first response speed = conversion rate)
2. Pas de "bonjour" — aller direct au besoin
3. Confirmer le problème: "Oui, le bruit des moustiques t'empêche de dormir ?"
4. Présenter la solution: 1 phrase max
5. Prix + garantie: "5 900 FCFA. Si ça marche pas, remboursé."
6. Clôture: "Tu préfères payer par Wave ou à la livraison ?"

## Common Objections & Responses

| Objection | Response |
|-----------|----------|
| "C'est cher" | "Tu dépenses combien par mois en sprays ? 3 000 ? Là c'est une fois." |
| "Je vais réfléchir" | "Bien sûr. Mais le stock part vite en saison des pluies." |
| "Ça marche vraiment ?" | "Garanti. Si dans 7 jours t'es pas satisfait, je rembourse." |
| "J'attends la fin du mois" | "Pas de souci. Je te relance début juillet alors ?" |

## Follow-Up Rules

- 1 follow-up max si pas de réponse (sans insister)
- Si "oui" → confirmer livraison (heure, lieu, montant)
- Si "non" → noter la raison dans DISTRIBUTION_MEMORY
- Si "peut-être" → proposer une date précise de suivi

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | OFFER_INTELLIGENCE.md, FAOS.md |


--- FILE: Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_INTELLIGENCE.md

# DIOS — DISTRIBUTION_INTELLIGENCE

## Mission

Deliver the right content, to the right audience, on the right platform, at the right frequency — without burning out the founder.

## Core Rule

One platform mastered > five platforms maintained. Distribution is leverage, not activity.

## Distribution Principles

1. **Platform hierarchy** — focus on one primary platform per campaign, use others for repurposing
2. **Rhythm over volume** — consistent 1 post/day beats 10 posts/week then silence
3. **Repurposing first** — one piece of content → N platform variations before creating new content
4. **Time blocking** — batch create content for the week in one session
5. **Cash constraint** — no paid distribution until organic is validated

## Distribution Rhythm

| Phase | Frequency | Duration | Goal |
|-------|-----------|----------|------|
| Launch | 1 post/day | 7 days | Validate hook |
| Growth | 1 post/2 days | 21 days | Build audience |
| Sustain | 2-3 posts/week | Ongoing | Maintain momentum |
| Pivot | Pause → analyse → new angle | 3 days | Fix what's not working |

## Campaign Structure

1. **Strategy** — DIOS defines audience, language, hook, platform, offer
2. **Production** — CEOS produces the content
3. **Distribution** — publish on primary + cross-post to secondary
4. **Engagement** — respond to comments, DMs, shares (first 24h critical)
5. **Analysis** — collect data, update DISTRIBUTION_MEMORY

## Cross-Posting Rules

- TikTok → Instagram Reels (same format, minimal adaptation)
- TikTok → YouTube Shorts (same format, no watermark)
- YouTube Long → TikTok clips (extract best 30s)
- WhatsApp broadcast → Facebook post (adapt tone for public)

## When to Stop

- 0 organic reach after 7 posts → change hook, not frequency
- 0 DMs after 14 posts → change offer, not distribution
- 0 sales after 30 days → change product, not strategy

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | PLATFORM_INTELLIGENCE.md, HOOK_INTELLIGENCE.md, OFFER_INTELLIGENCE.md |


--- FILE: Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_MEMORY.md

# DIOS — DISTRIBUTION_MEMORY

## Mission

Accumulate market intelligence from every campaign so DIOS gets smarter with every post.

## Core Rule

The canonical DISTRIBUTION_MEMORY lives at `concepts/DISTRIBUTION_MEMORY.md`. This sub-module defines HOW DIOS reads from and writes to it.

## Read Before Every Campaign

Before DIOS generates a new distribution strategy, query DISTRIBUTION_MEMORY for:

1. Which hooks won for this audience?
2. Which language converted best?
3. Which platform distributed furthest?
4. Which CTA drove action?
5. Which objections were most common?

## Write After Every Campaign

After each campaign, update DISTRIBUTION_MEMORY with:

```
Campaign: [name]
Product: [product]
Audience: [primary segment]
Language: [language used]
Platform: [platform used]
Hook: [hook text]
CTA: [call to action]
Views: [number]
Engagement: [likes, comments, shares]
Messages: [WhatsApp DMs received]
Conversions: [sales]
Revenue: [FCFA]
Cost: [production + distribution cost]
ROI: [(revenue - cost) / cost]
Lesson: [what to repeat or stop]
```

## Learning Loop

```
Campaign → Data → DISTRIBUTION_MEMORY → Pattern Detection → KNOWLEDGE update → Better DIOS strategy → Next campaign
```

## Pattern Detection

After 3+ campaigns with the same product, DIOS should identify:

- Best hook pattern (which attention source converts?)
- Best language (which language generates DMs?)
- Best platform (which platform drives sales?)
- Best CTA (which instruction gets action?)

These patterns are promoted to `concepts/KNOWLEDGE.md` as validated truths.

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | concepts/DISTRIBUTION_MEMORY.md, concepts/KNOWLEDGE.md |


--- FILE: Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md

‣䥄协霠䠠住彋义䕔䱌䝉久䕃ਊ⌣䴠獩楳湯ਊ湕敤獲慴摮眠票猠浯潥敮猠潴獰猠牣汯楬杮愠摮挠敲瑡⁥潨歯⁳桴瑡映牯散琠敨⁭潴猠潴⹰ਊ⌣䌠牯⁥畒敬ਊ潈歯漠数慲整⁳湯㌠氠祡牥ⱳ椠⁮牰潩楲祴漠摲牥਺⸱⨠䄪䑕佉⨪霠映獡整瑳琠⁯敲捡⁨桴⁥牢楡⁮猨畯摮‬畢空‬捳敲浡‬畱獥楴湯਩⸲⨠嘪卉䅕⩌‪ₗ牢慥獫猠牣汯⁬慰瑴牥⁮昨捡⁥潺浯‬潭敶敭瑮‬牢杩瑨映慬桳਩⸳⨠吪塅⩔‪ₗ湯祬眠牯獫椠⁦畡楤⁯乁⁄楶畳污愠牬慥祤猠潴灰摥琠敨猠牣汯੬嘊污摩瑡摥琠畲桴›敔瑸愠潬敮挠湡潮⁴楦⁸⁡潨歯瀠潲汢浥ਮ⌊‣‹潓牵散⁳景䄠瑴湥楴湯ਊ⁼潓牵散簠䠠潯⁫湁汧⁥੼⵼ⴭⴭⴭ簭ⴭⴭⴭⴭⴭ簭簊䘠慥⁲⁼匢⁩畴渠⁥慦獩瀠獡堠‬⁙牡楲敶•੼⁼畃楲獯瑩⁹⁼倢畯煲潵⁩⁘牡楲敶㼠䰠⁡潰獮⁥獥⁴≙簠簊䐠獥物⁥⁼䤢慭楧敮琠⁡楶⁥癡捥堠•੼⁼潍敮⁹⁼吢⁵数摲⁳⁘䍆䅆瀠牡樠畯⁲⃠慣獵⁥敤夠•੼⁼效污桴簠∠⁘慦瑩⁡⃠潴⁮潣灲⁳慳獮焠敵琠⁵敬猠捡敨≳簠簊䘠浡汩⁹⁼吢獥攠普湡獴洠狩瑩湥⁴≘簠簊匠慴畴⁳⁼䰢獥朠湥⁳畱⁩湯⁴⁘潳瑮瘠獵挠浯敭夠•੼⁼慓敦祴簠∠⁘整瀠潲敧搠⁥≙簠簊传灰牯畴楮祴簠∠⁘獥⁴楤灳湯扩敬洠楡瑮湥湡ⱴ愠牰珨挠攧瑳映湩≩簠ਊ⌣䠠潯⁫敇敮慲楴湯䐠浩湥楳湯ੳ䘊牯攠捡⁨畡楤湥散‬䥄协朠湥牥瑡獥栠潯獫愠牣獯㩳ⴊ倠牥愠摵敩据⁥敳浧湥⁴瀨牡湥ⱴ洠牥档湡ⱴ猠畴敤瑮⸮⤮ⴊ倠牥愠瑴湥楴湯猠畯捲⁥昨慥Ⱳ挠牵潩楳祴‬敤楳敲⸮⤮ⴊ倠牥氠湡畧条⁥䘨敲据ⱨ䔠敷‬楐杤湩⸮⤮ⴊ倠牥瀠慬晴牯⁭潦浲瑡⠠桳牯⁴獶氠湯Ⱨ瘠牥楴慣⁬獶栠牯穩湯慴⥬ਊ⌣䠠潯⁫敓敬瑣潩੮䘊牯攠捡⁨慣灭楡湧‬敧敮慲整ㄠⴰ〵栠潯獫‬桴湥映汩整㩲ㄊ‮獉椠⁴牴敵‿渨癥牥氠敩਩⸲䐠敯⁳瑩洠瑡档琠敨愠摵敩据㽥㌊‮潄獥椠⁴潷歲漠⁮桴⁥档獯湥瀠慬晴牯㽭㐊‮潄獥椠⁴慰獳琠敨㈠猭捥湯⁤整瑳‿眨畯摬猠浯潥敮猠潴⁰捳潲汬湩㽧਩⌊‣硅浡汰⁥䬨瑩匠汯楡敲‬畁楤湥散›慐敲瑮⥳ਊ⸱∠潔⁮湥慦瑮爠盩獩⁥⃠慬戠畯楧⁥敤異獩樠湡楶牥‮瑅猠⁩❣瓩楡⁴慬搠牥楮狨⁥潦獩㼠ਢ⸲∠〵‰䍆䅆瀠牡樠畯⁲❤獥敳据⹥䌠慨畱⁥潪牵‮敄異獩㌠洠楯⹳ਢ⸳∠潔⁮潶獩湩愠搠櫩⃠湩瑳污氠⁥楳湥‮畔愠瑴湥獤焠潵⁩∿ਊ⌣䘠潯整ੲ簊䘠敩摬簠嘠污敵簠簊ⴭⴭⴭ簭ⴭⴭⴭ簭簊传⁓敖獲潩⁮⁼㑖簠簊䰠獡⁴敖楲楦摥簠㈠㈰ⴶ㘰㈭‱੼⁼睏敮⁲⁼䥄协簠簊䐠灥湥敤据敩⁳⁼啁䥄久䕃䥟呎䱅䥌䕇䍎⹅摭‬䅌䝎䅕䕇䥟呎䱅䥌䕇䍎⹅摭‬䱐呁但䵒䥟呎䱅䥌䕇䍎⹅摭簠਍

--- FILE: Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md

# DIOS — LANGUAGE_INTELLIGENCE

## Mission

Speak the language of the public. Not just translate — adapt to how they think, feel, and buy.

## Core Rule

Languages are derived from Market Intelligence + target country. Never hardcoded.

## Language Derivation

| Market | Available Languages |
|--------|-------------------|
| Togo | Français, Ewe, Mina, Pidgin, Kabiye, Tem |
| Ghana | English, Twi, Ga, Ewe, Hausa, Pidgin |
| Nigeria | English, Pidgin, Yoruba, Hausa, Igbo, Efik |
| Benin | Français, Fon, Yoruba, Mina, Bariba |

## Adaptation Layers

1. **Language** — vocabulary, grammar (e.g. French formal vs colloquial)
2. **Culture** — references, humor, values (e.g. "protège ta famille" hits differently in Lomé vs Paris)
3. **Reality** — economic context, infrastructure, daily life (e.g. "quand l'électricité part" only works where blackouts are common)
4. **Problem** — is the problem felt the same way? (e.g. "moustique = nuisance" vs "moustique = malaria")
5. **Desire** — what does the audience aspire to? (e.g. "avoir l'air moderne" vs "protéger ce qu'on a")

## Principle

> Le français pour le sérieux. L'ewe pour le coeur. Le pidgin pour la rue.

DIOS selects primary language + secondary language per campaign based on audience segment.

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md |


--- FILE: Frameworks/Specialized/Distribution/DIOS/OFFER_INTELLIGENCE.md

# DIOS — OFFER_INTELLIGENCE

## Mission

Present the product in a way that makes the audience see the value before they see the price.

## Core Rule

An offer is not a product description. An offer is a transformation the audience wants, framed around what they fear losing or desire gaining.

## The 4 Questions of Offer Design

1. **Why buy?** — value, need, desire
2. **Why wait?** — risk, uncertainty, trust
3. **Why refuse?** — price, objection, timing
4. **Why share?** — status, altruism, entertainment

## Offer Variables

| Variable | Question | Example |
|----------|----------|---------|
| Price | How does value compare to cost? | 5,900 FCFA = 2 mois de sprays |
| Risk | What if it doesn't work? | Garantie satisfait ou remboursé |
| Trust | Why should I believe you? | 2,000 unités déjà vendues V1 |
| Urgency | Why now? | Stock limité, saison des pluies |
| Proof | Does it work? | Avant/après, témoignage |
| Simplicity | How easy is it? | Brancher et ça marche |

## Offer Structure

1. **Problem** — name the pain they feel daily
2. **Cost of inaction** — what they lose by not solving it
3. **Solution** — present the product as the answer
4. **Proof** — show it works (demo, testimonial, data)
5. **Objection handler** — answer "why this won't work for me"
6. **CTA** — one clear action

## Example (Pest Repeller)

1. Problem: "Tu te réveilles chaque nuit à cause des moustiques ?"
2. Cost: "3,000 FCFA par mois en sprays toxiques qui puent ta chambre"
3. Solution: "Branche ça. 6m de portée. Ultrason, zéro chimie."
4. Proof: "2,000 déjà vendus. Utilisé dans 3 hôtels à Lomé."
5. Objection: "Ça marche vraiment ? — garanti ou remboursé."
6. CTA: "Écris 'stop' sur WhatsApp au 71 39 21 22."

## Offer Principles for Lomé

- Price anchoring: always reference a familiar cost (spray, fuel, phone credit)
- Payment at delivery builds trust (no advance = no risk for buyer)
- WhatsApp is the checkout — make the CTA a message, not a link
- Testimonials from local faces beat polished ads

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md, HOOK_INTELLIGENCE.md |


--- FILE: Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md

# DIOS — PLATFORM_INTELLIGENCE

## Mission

Adapt content to the platform's attention mechanic.

## Core Rule

DIOS selects platform(s) based on audience behavior, not preference.

## Platform Profiles

### TikTok

- Objective: Stop the scroll
- Structure: Hook → Curiosity → CTA
- Format: 30-60s vertical (9:16), text overlay mandatory, trending audio
- Key mechanic: First 2 seconds decide everything
- Attention source: Pattern interrupt (audio/visual/text)
- Best for: Product demo, building in public, before/after

### Facebook

- Objective: Build trust
- Structure: Problem → Story → Proof → CTA
- Format: 1:1 or 16:9, longer captions, comments thread
- Key mechanic: Social proof, shares, group recommendations
- Attention source: Relatability, community, credibility
- Best for: Testimonials, detailed demos, local engagement

### WhatsApp

- Objective: Recommendation and direct sale
- Structure: Trust → Testimonial → Offer → Direct message
- Format: Image + text + voice note, 1-on-1
- Key mechanic: Personal relationship, low pressure
- Attention source: Trust, familiarity, exclusivity
- Best for: Closing sales, customer support, recurring orders

### YouTube

- Objective: Education and authority
- Structure: Value → Authority → Conversion
- Format: 10-14 min horizontal 16:9 or Shorts (vertical)
- Key mechanic: Watch time, retention, subscription
- Attention source: Curiosity, deep value, entertainment
- Best for: Tutorials, deep dives, long-form storytelling

### X / Twitter

- Objective: Intellectual presence
- Structure: Hook → Insight → Thread
- Format: Text thread, 280+ characters
- Key mechanic: Retweets, engagement, followers
- Attention source: Novelty, controversy, value density
- Best for: Building in public, insights, networking

## Selection Matrix

DIOS selects platform by:
1. Audience concentration (where does the target spend time?)
2. Content format (does the offer work better in short or long form?)
3. Conversion path (how does the platform lead to a sale?)
4. Resource constraint (how much content can we produce?)

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md |


--- FILE: Frameworks/Experimental/PMOS.md

# PMOS — Project Management Operating System

## Status
EXPERIMENTAL — in quarantine until proven uniquely valuable.

## Reason for Quarantine
PROJECT, WORKFLOW and PLAYBOOK already exist. PMOS risks duplicating.

## Validation Test
If within 30 days of real use, a project management need not covered by existing concepts emerges, PMOS will be promoted.

## Source archive
ARCHIVE/v1/legacy_frameworks/PMOS v2.md


--- FILE: Frameworks/Experimental/LEOS.md

# LEOS — Learning Operating System

## Status
EXPERIMENTAL — in quarantine until proven uniquely valuable.

## Reason for Quarantine
FounderHQ is currently not blocked by learning. It is blocked by prioritization, execution and distribution.

## Validation Test
If a recurring need for structured learning (skill acquisition, project-based learning) manifests, LEOS will be promoted.

## Source archive
ARCHIVE/v1/legacy_frameworks/LEOS v2.md


--- FILE: Frameworks/Experimental/RIOS.md

# RIOS — Research & Intelligence Operating System

## Status
EXPERIMENTAL — in quarantine until proven uniquely valuable.

## Reason for Quarantine
KNOWLEDGE, WORKFLOW and PROJECT already cover research. RIOS must demonstrate that it brings a true business intelligence method.

## Validation Test
If a recurring need for competitive analysis or monitoring manifests, RIOS will be activated.

## Source archive
ARCHIVE/v1/legacy_frameworks/RIOS v2.md


--- FILE: GENESIS.md

# FounderOS V4 — GENESIS

## Purpose

GENESIS is the first-time setup procedure. It is executed only once — the first time FounderOS is deployed in a new environment.

## Prerequisites

- A blank or existing FounderHQ directory
- An LLM capable of reading and writing files
- Git (optional but recommended)

## Genesis Procedure

### Step 1: Create Directory Structure

```
FounderHQ/
├── FounderOS/
│   ├── SYSTEM_PROMPT.md
│   ├── KERNEL.md
│   ├── RUNTIME.md
│   ├── MOS.md
│   ├── DAOS.md
│   ├── VEAOS.md
│   ├── CEOS.md
│   ├── ASTRA.md
│   ├── KMOS.md
│   ├── LEOS.md
│   ├── RIOS.md
│   ├── FAOS.md
│   ├── SOS.md
│   ├── AOS.md
│   ├── DECISION_ENGINE.md
│   ├── PATTERN_ENGINE.md
│   ├── PLAYBOOK_ENGINE.md
│   ├── KNOWLEDGE_EVOLUTION_ENGINE.md
│   ├── CONTINUOUS_IMPROVEMENT.md
│   ├── AI_VIDEO_MASTER_DOMAIN.md
│   ├── GENESIS.md
│   ├── INSTALL.md
│   ├── concepts/
│   ├── Protocols/
│   ├── Frameworks/
│   ├── State/
│   └── Runtime/
```

### Step 2: Load SYSTEM_PROMPT.md

The LLM reads SYSTEM_PROMPT.md. This is the entry point for all sessions.

### Step 3: Execute Boot Sequence

1. Run WF-007 freshness check
2. Determine session mode
3. Build world model

### Step 4: Load Concepts

- Load all concept files from concepts/
- Verify against SOURCE_OF_TRUTH.md
- Check for contradictions

### Step 5: First Action

- Read FOUNDERHQ_MANIFEST.md for the venture context
- Determine the first mission-critical action
- Execute it

### Step 6: Initialize Git (if available)

```bash
git init
git add -A
git commit -m "genesis: FounderOS V3 initialized"
```

## Verification

After Genesis:
- [ ] All 22+ OS files exist in FounderOS/
- [ ] All concept files exist in concepts/
- [ ] SYSTEM_PROMPT.md loads without errors
- [ ] Protocols/SOURCE_OF_TRUTH.md has entries for all files
- [ ] State/CURRENT_STATE.md reflects current reality
- [ ] Git repository initialized and committed

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | INSTALL.md, SYSTEM_PROMPT.md |


--- FILE: INSTALL.md

# FounderOS V4 — INSTALL

## Purpose

INSTALL is the deployment guide for setting up FounderOS in a new environment (new machine, new LLM, new IDE).

## Requirements

- Any LLM that supports reading and writing files (ChatGPT, Claude, Gemini, DeepSeek, local models)
- Any IDE or file system that supports markdown files
- Git (optional — for version tracking and reboot delta detection)
- Operating System: Windows, macOS, Linux (any)

## Installation Steps

### 1. Clone or Copy FounderHQ

```bash
git clone <repository> FounderHQ
# OR
# Copy the FounderHQ directory manually
```

### 2. Verify Directory Structure

Ensure all OS files exist under FounderOS/. If any are missing, run GENESIS to recreate them.

### 3. Set Up Protocols

SYSTEM_PROMPT.md is the boot sequence. It must be loadable on first read. Ensure:
- All Protocol files exist
- SOURCE_OF_TRUTH.md has entries for all files
- DECISION_GATES.md references the correct frameworks

### 4. Configure State

State/CURRENT_STATE.md must be updated with:
- Current date
- Cash position
- Current bottleneck
- Current priority
- Session objective

### 5. First Boot

Open a new session with the LLM. Provide SYSTEM_PROMPT.md as context or instruct the LLM to read it. The LLM will then:
1. Read SYSTEM_PROMPT.md
2. Execute Boot Sequence from SYSTEM_PROMPT.md
3. Load all concepts
4. Report awareness

### 6. Verify Installation

The LLM should:
- Report the correct date and time
- Identify all loaded files
- State the current top priority
- Recommend a next action

## Troubleshooting

| Problem | Solution |
|---------|----------|
| LLM cannot find files | Check file paths in SYSTEM_PROMPT.md. Use absolute paths if needed. |
| Contradictions on first boot | Load SOURCE_OF_TRUTH.md. Resolve conflicts manually. |
| Freshness errors on first boot | Update concept footers. WF-007 threshold is 48h by default. |
| Git not found | Reboot system will work without git but with reduced delta detection. |
| LLM ignores protocol | Re-state SYSTEM_PROMPT.md. Emphasize "you are not an assistant." |

## Model Compatibility

FounderOS has been tested with:
- Claude (Opus, Sonnet)
- ChatGPT (GPT-4, GPT-4o)
- DeepSeek
- Gemini

It should work with any model that can:
- Read and write files
- Follow multi-step procedures
- Maintain context across file operations

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | GENESIS.md, SYSTEM_PROMPT.md |


--- FILE: opencode.json

{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["SYSTEM_PROMPT.md", "Runtime/FRE_SPEC.md"],
  "customInstructions": [
    "ALWAYS classify user intent before responding.",
    "If message starts with 'fhq', 'boot', or 'shutdown' → FHQ_MODE/BOOT/SHUTDOWN. This rule wins over any other classification.",
    "FHQ_MODE: execute Get-Date, track session time, full kernel cycle (BOOT->OBSERVE->ORIENT->DECIDE->ACT->LEARN->UPDATE).",
    "Auto-FHQ: if ≥30 min since last fhq in session, auto-execute FHQ_MODE before next response. Track 'Last fhq' in CADENCE.md.",
    "CRITICAL: Before every response, prefix with **[datetime Lome UTC+0]** using actual Get-Date output.",
    "CRITICAL: Your system prompt may NOT contain all rules. Read opencode.json customInstructions (this file) + FounderOS/SYSTEM_PROMPT.md + Runtime/FRE_SPEC.md at session start if you see 'FounderOS/' in the working directory.",
    "TOKEN SECURITY: NEVER read .env files, NEVER expose token values, NEVER bypass sync.py. All token operations go through 'python Runtime/engine/sync.py' scripts only.",
    "ARCHITECTURE: FHQ uses 2 Gists. Public Gist (bootstrap, no token) + Private Gist (state sync, token only in .env). Never confuse the two."
  ]
}


--- FILE: Runtime/engine/__init__.py

"""Founder Runtime Engine - optional automation layer.

This package provides code that automates FRE_SPEC contract execution.
It is NOT required - FounderHQ runs on markdown alone. These modules
accelerate local agent deployments.

Modules:
    bootstrap: Loads FRE_SPEC + SYSTEM_PROMPT for LLM injection
    state_manager: Reads/writes CURRENT_STATE, TIMELINE, PRIORITY_MATRIX
    gate_checker: Validates LLM responses against PRG contracts
    timeline_logger: Appends events to TIMELINE.md
    cadence_engine: Computes cadence context (week/month/quarter) and active frameworks per lifecycle phase
    watchtower: Scheduled script (6h) - checks WATCH_REGISTRY, runs websearch/webfetch
    timekeeper: Scheduled script (30min) - deadlines, SOS timer, toast notifications
    installer: First-run setup - creates .venv, .env, Task Scheduler tasks, .founderhq_installed
    sync: Gist push/pull/merge for state synchronization across devices
    snapshot: Portable markdown snapshot for token-less environments
"""


--- FILE: Runtime/engine/bootstrap.py

"""Reads FRE_SPEC.md and SYSTEM_PROMPT.md, returns combined prompt for LLM injection.

Usage:
    from engine.bootstrap import build_system_prompt
    prompt = build_system_prompt("/path/to/founderhq")
    llm = LLM(system_prompt=prompt)
"""

import os
from pathlib import Path


FRE_SPEC_PATH = "Runtime/FRE_SPEC.md"
SYSTEM_PROMPT_PATH = "SYSTEM_PROMPT.md"


def read_file(path: str) -> str:
    """Read a file and return its content. File not found -> empty string."""
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


def build_system_prompt(base_dir: str = ".") -> str:
    """Build a combined system prompt from FRE_SPEC and SYSTEM_PROMPT.

    Args:
        base_dir: Root directory of FounderHQ.

    Returns:
        Combined system prompt string.
    """
    fre_spec = read_file(os.path.join(base_dir, FRE_SPEC_PATH))
    sys_prompt = read_file(os.path.join(base_dir, SYSTEM_PROMPT_PATH))

    # If either file is missing, return whatever we have
    if not fre_spec and not sys_prompt:
        return ""

    parts = []

    if fre_spec:
        parts.append(f"# FRE SPEC — Constitutive Contracts\n\n{fre_spec}")

    if sys_prompt:
        parts.append(f"# SYSTEM PROMPT — Active Execution\n\n{sys_prompt}")

    return "\n\n---\n\n".join(parts)


def list_missing_files(base_dir: str = ".") -> list[str]:
    """Return list of expected files that are missing."""
    expected = [
        FRE_SPEC_PATH,
        SYSTEM_PROMPT_PATH,
        "State/CURRENT_STATE.md",
        "State/PRIORITY_MATRIX.md",
    ]
    missing = []
    for rel_path in expected:
        full = os.path.join(base_dir, rel_path)
        if not os.path.exists(full):
            missing.append(rel_path)
    return missing


--- FILE: Runtime/engine/cadence_engine.py

"""Compute cadence context and active frameworks from datetime + lifecycle state.

Usage:
    from engine.cadence_engine import get_cadence_context, get_active_frameworks
    ctx = get_cadence_context(datetime.now())
    frameworks = get_active_frameworks(ctx)
"""

from datetime import datetime


def get_week_of_month(dt: datetime) -> int:
    """Return which week of the month this date falls in (1-based)."""
    first_day = dt.replace(day=1)
    days_from_monday = first_day.weekday()
    first_monday = first_day.replace(day=1 - days_from_monday)
    delta = dt - first_monday
    return (delta.days // 7) + 1


def get_cadence_context(dt: datetime) -> dict:
    """Return dict with all cadence levels for the given datetime."""
    return {
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "hour": dt.hour,
        "minute": dt.minute,
        "week_of_month": get_week_of_month(dt),
        "iso_week": dt.isocalendar()[1],
        "day_of_week": dt.isoweekday(),
        "day_name": dt.strftime("%A"),
        "month_name": dt.strftime("%B"),
        "quarter": (dt.month - 1) // 3 + 1,
    }


FRAMEWORKS_BY_PHASE = {
    "IDEA": ["CAOS"],
    "VALIDATION": ["VAOS", "DIOS"],
    "LAUNCH": ["DIOS", "CEOS"],
    "GROWTH": ["PSOS", "FAOS", "SAOS"],
    "SCALE": ["FAOS", "SAOS"],
    "MATURE": ["SAOS"],
}

SURVIVAL_FRAMEWORKS = ["DAOS", "DIOS"]


def get_active_frameworks(ctx: dict) -> list[str]:
    """Return list of frameworks to load based on lifecycle phase and mode.

    Args:
        ctx: Context dict with at minimum 'lifecycle_phase' and optionally 'mode'.

    Returns:
        List of framework short names to load (e.g. ['VAOS', 'DIOS']).
    """
    phase = ctx.get("lifecycle_phase", "IDEA")
    mode = ctx.get("mode", "GROWTH")

    frameworks = list(FRAMEWORKS_BY_PHASE.get(phase, ["CAOS"]))

    if mode == "SURVIVAL":
        for fw in SURVIVAL_FRAMEWORKS:
            if fw not in frameworks:
                frameworks.append(fw)

    return frameworks


--- FILE: Runtime/engine/gate_checker.py

"""Validates LLM responses against FRE_SPEC PRG contracts.

Checks datetime format, stale concepts, response structure.
Returns PASS/FAIL for each gate.

Usage:
    from engine.gate_checker import GateChecker
    checker = GateChecker("/path/to/founderhq")
    results = checker.check_all(response_text)
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional


class GateChecker:
    """Validates LLM responses against PRG (Pre-Response Gate) contracts."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    def _read_file(self, *parts: str) -> Optional[str]:
        path = self.base_dir.joinpath(*parts)
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8")

    def check_temporal(self, response: str) -> tuple[bool, str]:
        """Gate 1: Verify response starts with a valid datetime.

        Expected format: **[YYYY-MM-DD HH:MM Lomé UTC+0]**
        """
        if not response:
            return False, "Empty response"

        first_line = response.strip().split("\n")[0]
        pattern = r"^\*\*\[\d{4}-\d{2}-\d{2} \d{2}:\d{2} Lomé UTC\+0\]\*\*"
        if re.match(pattern, first_line):
            return True, "Datetime header present and valid"
        return False, f"Missing or invalid datetime header. Got: '{first_line[:60]}'"

    def check_concept_freshness(self, max_age_hours: int = 48) -> list[str]:
        """Gate 5: Find concepts that haven't been updated within max_age_hours.

        Checks footers of concept files for 'Last Updated' or 'Last Verified' timestamps.
        """
        stale_files = []
        concept_dir = self.base_dir / "concepts"
        if not concept_dir.exists():
            return ["concepts/ directory not found"]

        now = datetime.utcnow()

        for f in sorted(concept_dir.iterdir()):
            if f.suffix != ".md" or not f.is_file():
                continue
            text = f.read_text(encoding="utf-8")

            # Look for Last Updated or Last Verified in footer
            ts_match = re.search(
                r"(?:Last\s+Updated|Last\s+Verified)[^\d]*(\d{4}-\d{2}-\d{2})",
                text,
            )
            if not ts_match:
                stale_files.append(f"{f.name}: no timestamp found")
                continue

            date_str = ts_match.group(1)
            try:
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                age_hours = (now - file_date).total_seconds() / 3600
                if age_hours > max_age_hours:
                    stale_files.append(
                        f"{f.name}: {age_hours:.0f}h old "
                        f"(max {max_age_hours}h)"
                    )
            except ValueError:
                stale_files.append(f"{f.name}: unparseable date '{date_str}'")

        return stale_files

    def check_projects_cascade(self) -> list[str]:
        """Gate 4: Verify active projects have strategic cascade files.

        Checks projects/<PROJECT>/ for 01_VISION.md through 10_PITCH_DECK.md + annexes/.
        """
        missing = []
        projects_dir = self.base_dir / "projects"
        if not projects_dir.exists():
            return ["projects/ directory not found"]

        required = [
            "01_VISION.md",
            "02_MISSION.md",
            "03_THEORY_OF_CHANGE.md",
            "04_STRATEGIC_ASSETS_MAP.md",
            "05_MASTER_PLAN.md",
            "06_STRATEGIC_ROADMAP.md",
            "07_CAPITAL_ROADMAP.md",
            "08_EXECUTIVE_SUMMARY.md",
            "09_BUSINESS_PLAN.md",
            "10_PITCH_DECK.md",
        ]

        for proj_dir in sorted(projects_dir.iterdir()):
            if not proj_dir.is_dir():
                continue
            proj_missing = []
            for req in required:
                if not (proj_dir / req).exists():
                    proj_missing.append(req)
            if proj_missing:
                missing.append(
                    f"{proj_dir.name}: missing {', '.join(proj_missing)}"
                )

        return missing

    def check_all(self, response: str) -> dict:
        """Run all applicable checks and return results."""
        results = {}

        # Gate 1: Temporal
        temporal_ok, temporal_msg = self.check_temporal(response)
        results["gate_1_temporal"] = {
            "status": "PASS" if temporal_ok else "FAIL",
            "message": temporal_msg,
        }

        # Gate 5: Freshness
        stale = self.check_concept_freshness()
        results["gate_5_freshness"] = {
            "status": "PASS" if not stale else "FLAG",
            "message": f"{len(stale)} stale concept(s)" if stale else "All fresh",
            "stale_files": stale,
        }

        # Gate 4: Project Data Room (informational)
        missing_cascade = self.check_projects_cascade()
        results["gate_4_project_scan"] = {
            "status": "PASS" if not missing_cascade else "FLAG",
            "message": (
                f"{len(missing_cascade)} project(s) incomplete"
                if missing_cascade
                else "All complete"
            ),
            "details": missing_cascade,
        }

        return results

    def report(self, response: str) -> str:
        """Return a formatted gate check report."""
        results = self.check_all(response)
        lines = ["## PRG Gate Check Report", ""]

        for gate, data in results.items():
            status = data["status"]
            icon = {"PASS": "✅", "FAIL": "❌", "FLAG": "⚠️"}.get(status, "❓")
            lines.append(f"{icon} {gate}: {data['message']}")

        return "\n".join(lines)


--- FILE: Runtime/engine/installer.py

"""installer.py - Cross-platform first-run setup for FounderHQ.

Creates:
1. .venv Python virtual environment
2. .env file (asks user for GitHub token)
3. Installs dependencies (requests, python-dotenv)
4. Scheduler tasks for watchtower + timekeeper (schtasks / cron / launchd)
5. .founderhq_installed marker

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


IS_WINDOWS = sys.platform.startswith("win")
IS_LINUX = sys.platform.startswith("linux")
IS_MAC = sys.platform == "darwin"

ENV_PATH = ".env"


def get_platform_label() -> str:
    if IS_WINDOWS:
        return "Windows"
    if IS_LINUX:
        return "Linux"
    if IS_MAC:
        return "macOS"
    return sys.platform


def get_venv_python(base_path: Path) -> str:
    if IS_WINDOWS:
        pip = base_path / ".venv" / "Scripts" / "python.exe"
    else:
        pip = base_path / ".venv" / "bin" / "python3"
        if not pip.exists():
            pip = base_path / ".venv" / "bin" / "python"
    return str(pip) if pip.exists() else sys.executable


def get_venv_pip(base_path: Path) -> str:
    for name in ("pip.exe", "pip", "pip3"):
        if IS_WINDOWS:
            pip = base_path / ".venv" / "Scripts" / name
        else:
            pip = base_path / ".venv" / "bin" / name
        if pip.exists():
            return str(pip)
    return ""


def create_venv(base_path: Path) -> bool:
    """Create .venv if it doesn't exist."""
    venv_path = base_path / ".venv"
    marker = get_venv_python(base_path)
    if marker and Path(marker).exists():
        print(".venv: already exists")
        return True

    print("Creating .venv...")
    result = subprocess.run(
        [sys.executable, "-m", "venv", str(venv_path)],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        print(f"ERROR creating .venv: {result.stderr.strip()}")
        return False
    print(".venv: created")
    return True


def install_deps(base_path: Path) -> bool:
    """Install Python dependencies in .venv."""
    pip = get_venv_pip(base_path)
    if not pip:
        print("ERROR: pip not found in .venv")
        return False

    deps = ["requests", "python-dotenv"]
    print(f"Installing dependencies: {', '.join(deps)}...")
    result = subprocess.run(
        [pip, "install"] + deps,
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        print(f"ERROR installing deps: {result.stderr.strip()}")
        return False
    print("Dependencies: installed")
    return True


def setup_env(base_path: Path) -> bool:
    """Prompt user for GitHub token and write .env."""
    env_file = base_path / ENV_PATH
    if env_file.exists():
        print(".env: already exists")
        return True

    print("\n=== GitHub Token Setup ===")
    print("FounderHQ uses a private GitHub Gist for state sync between devices.")
    print("You need a GitHub fine-grained token with scope: gist:write, gist:read")
    print("Create one at: https://github.com/settings/tokens?type=beta")
    print("(Type 'skip' to configure later, or press Enter to skip)\n")

    token = input("GitHub token: ").strip()
    if not token or token.lower() == "skip":
        print(".env: skipped. Sync will not be available.")
        return True

    url = input("Gist URL (optional, press Enter to skip): ").strip()

    env_content = f"FHQ_GIST_TOKEN={token}\n"
    if url:
        env_content += f"FHQ_GIST_URL={url}\n"

    env_file.write_text(env_content, encoding="utf-8")
    try:
        os.chmod(env_file, 0o600)
    except (OSError, NotImplementedError):
        pass
    print(f".env: created at {env_file}")
    return True


def create_marker(base_path: Path) -> bool:
    """Create .founderhq_installed marker."""
    marker = base_path / ".founderhq_installed"
    marker.write_text("", encoding="utf-8")
    print("Marker: .founderhq_installed created")
    return True


# ── Scheduler (OS-agnostic) ──


def _remove_schtasks(name: str) -> bool:
    if not _task_exists_schtasks(name):
        return True
    cmd = ["schtasks", "/Delete", "/TN", name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    return result.returncode in (0, 1)


def _task_exists_schtasks(name: str) -> bool:
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", name],
        capture_output=True, text=True, timeout=10,
    )
    return result.returncode == 0


def _create_schtasks(name: str, script: str, base_dir: str, interval: int) -> bool:
    python_exe = get_venv_python(Path(base_dir))
    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval),
        "/TN", name,
        "/TR", f'"{python_exe}" "{script}" --base-dir "{base_dir}"',
        "/F",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {name}: {result.stderr.strip()}")
        return False
    print(f"Task '{name}' created (every {interval} min).")
    return True


def _remove_cron(name: str) -> bool:
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            return True
        lines = [l for l in result.stdout.splitlines() if name not in l]
        new_cron = "\n".join(lines) + "\n"
        proc = subprocess.run(
            ["crontab", "-"],
            input=new_cron, text=True, capture_output=True, timeout=10,
        )
        return proc.returncode == 0
    except Exception:
        return True


def _create_cron(name: str, script: str, base_dir: str, interval: int) -> bool:
    python_exe = get_venv_python(Path(base_dir))
    comment = f"# FounderHQ: {name}"
    cron_line = f"*/{interval} * * * * {python_exe} {script} --base-dir {base_dir}"
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            capture_output=True, text=True, timeout=10,
        )
        existing = result.stdout if result.returncode == 0 else ""
        if name in existing:
            print(f"Cron '{name}': already exists")
            return True
        new_cron = existing.strip() + "\n" + comment + "\n" + cron_line + "\n"
        proc = subprocess.run(
            ["crontab", "-"],
            input=new_cron, text=True, capture_output=True, timeout=10,
        )
        if proc.returncode != 0:
            print(f"ERROR creating cron '{name}': {proc.stderr.strip()}")
            return False
        print(f"Cron '{name}' created (every {interval} min).")
        return True
    except FileNotFoundError:
        print("WARNING: crontab not available, skipping scheduler")
        return False


def _remove_launchd(name: str) -> bool:
    plist = Path.home() / "Library" / "LaunchAgents" / f"{name}.plist"
    if not plist.exists():
        return True
    subprocess.run(["launchctl", "unload", str(plist)], capture_output=True, timeout=10)
    plist.unlink(missing_ok=True)
    return True


def _create_launchd(name: str, script: str, base_dir: str, interval: int) -> bool:
    python_exe = get_venv_python(Path(base_dir))
    label = f"com.founderhq.{name.lower().replace(' ', '-')}"
    plist_dir = Path.home() / "Library" / "LaunchAgents"
    plist_dir.mkdir(parents=True, exist_ok=True)
    plist_path = plist_dir / f"{label}.plist"

    start_interval = interval * 60  # launchd uses seconds
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{label}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_exe}</string>
        <string>{script}</string>
        <string>--base-dir</string>
        <string>{base_dir}</string>
    </array>
    <key>StartInterval</key>
    <integer>{start_interval}</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""
    plist_path.write_text(plist_content, encoding="utf-8")
    result = subprocess.run(
        ["launchctl", "load", str(plist_path)],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != 0:
        print(f"ERROR loading launchd job '{label}': {result.stderr.strip()}")
        return False
    print(f"Launchd job '{label}' created (every {interval} min).")
    return True


def setup_scheduler(name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    if IS_WINDOWS:
        return _create_schtasks(name, script_path, base_dir, interval_minutes)
    if IS_LINUX:
        return _create_cron(name, script_path, base_dir, interval_minutes)
    if IS_MAC:
        return _create_launchd(name, script_path, base_dir, interval_minutes)
    print(f"WARNING: Unknown platform '{sys.platform}', skipping scheduler")
    return False


def remove_scheduler(name: str) -> bool:
    if IS_WINDOWS:
        return _remove_schtasks(name)
    if IS_LINUX:
        return _remove_cron(name)
    if IS_MAC:
        return _remove_launchd(name)
    return True


# ── Notifications ──


def check_notifications() -> bool:
    if IS_WINDOWS:
        cmd = [
            "powershell.exe", "-NoProfile", "-Command",
            "Get-Module -ListAvailable -Name BurntToast",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        available = "BurntToast" in result.stdout
        if available:
            print("Notifications: BurntToast available (Windows)")
        else:
            print("Notifications: BurntToast NOT available")
        return available
    if IS_LINUX:
        result = subprocess.run(
            ["which", "notify-send"],
            capture_output=True, text=True, timeout=5,
        )
        available = result.returncode == 0
        print(f"Notifications: notify-send {'available' if available else 'NOT available'} (Linux)")
        return available
    if IS_MAC:
        print("Notifications: osascript available (macOS)")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Cross-platform installer for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks/jobs")
    parser.add_argument("--skip-env", action="store_true", help="Skip .env setup")
    parser.add_argument("--skip-venv", action="store_true", help="Skip .venv creation")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    print(f"Platform: {get_platform_label()}")

    if args.uninstall:
        remove_scheduler("FounderHQ-Watchtower")
        remove_scheduler("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    check_notifications()

    if not args.skip_venv:
        create_venv(base_path)
        install_deps(base_path)

    if not args.skip_env:
        setup_env(base_path)

    watchtower_path = scripts_dir / "watchtower.py"
    if watchtower_path.exists():
        setup_scheduler("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)
    else:
        print(f"WARNING: {watchtower_path} not found, skipping watchtower")

    timekeeper_path = scripts_dir / "timekeeper.py"
    if timekeeper_path.exists():
        setup_scheduler("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)
    else:
        print(f"WARNING: {timekeeper_path} not found, skipping timekeeper")

    create_marker(base_path)

    print("\nInstallation complete.")
    print(f"  Platform: {get_platform_label()}")
    print("  - .venv: ready")
    print("  - Dependencies: installed")
    print("  - Scheduler: configured")
    print("  - .founderhq_installed: created")


if __name__ == "__main__":
    main()


--- FILE: Runtime/engine/snapshot.py

"""snapshot.py - Portable markdown snapshot for environments without Gist API access.

Generates a compact markdown summary of current state (no token needed).
LLM reads the output, user copies it to another device.
On the target device, LLM runs merge to apply changes.

Commands:
    snapshot.py generate  - Produce EXPORT_SNAPSHOT.md
    snapshot.py merge     - Read IMPORT_SNAPSHOT.md and apply changes
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


STATE_DIR = Path(__file__).resolve().parent.parent.parent / "State"
CONCEPTS_DIR = Path(__file__).resolve().parent.parent.parent / "concepts"


def read_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def extract_field(text: str, pattern: str) -> str:
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def cmd_generate() -> str:
    """Generate a portable markdown snapshot."""
    cs = read_file(STATE_DIR / "CURRENT_STATE.md")
    cad = read_file(STATE_DIR / "CADENCE.md")
    lc = read_file(STATE_DIR / "LIFECYCLE.md")
    tl = read_file(CONCEPTS_DIR / "TIMELINE.md")

    date = extract_field(cs, r"\*\*Date:\*\*\s*(.*)")
    mode = extract_field(cs, r"\*\*Operating Mode:\*\*\s*(.*)")
    cash = extract_field(cs, r"\*\*Cash.*:\*\*\s*(.*)")
    priority = extract_field(cs, r"\*\*Top Priority:\*\*\s*(.*)")
    bottleneck = extract_field(cs, r"\*\*Current Bottleneck:\*\*\s*(.*)")
    sess_start = extract_field(cad, r"\*\*Session start:\*\*\s*(.*)")
    sess_end = extract_field(cad, r"\*\*Session end:\*\*\s*(.*)")

    recent_events = []
    for line in tl.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] not in ("Date", ""):
                recent_events.append(f"- {cols[0]}: {cols[1]} -> {cols[3]}")

    recent_events = recent_events[-5:]

    projects = []
    in_table = False
    for line in lc.splitlines():
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if in_table and line.startswith("|") and not line.startswith("|---"):
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 5:
                projects.append(f"- {cols[0]}: {cols[1]} -> {cols[4]}")

    snapshot = f"""# FHQ Snapshot - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}

**Date:** {date}
**Mode:** {mode}
**Cash:** {cash}
**Top Priority:** {priority}
**Bottleneck:** {bottleneck}
**Session:** {sess_start} -> {sess_end}

## Projects
{chr(10).join(projects) if projects else "- (none)"}

## Recent Events
{chr(10).join(recent_events) if recent_events else "- (none)"}
"""

    out_path = STATE_DIR / "EXPORT_SNAPSHOT.md"
    out_path.write_text(snapshot, encoding="utf-8")
    return f"OK: Snapshot written to State/EXPORT_SNAPSHOT.md ({len(snapshot)} chars)"


def cmd_merge() -> str:
    """Read IMPORT_SNAPSHOT.md and apply to state files."""
    in_path = STATE_DIR / "IMPORT_SNAPSHOT.md"
    if not in_path.exists():
        return "ERROR: No State/IMPORT_SNAPSHOT.md found."

    text = in_path.read_text(encoding="utf-8")

    new_date = extract_field(text, r"\*\*Date:\*\*\s*(.*)")
    new_mode = extract_field(text, r"\*\*Mode:\*\*\s*(.*)")
    new_cash = extract_field(text, r"\*\*Cash:\*\*\s*(.*)")
    new_priority = extract_field(text, r"\*\*Top Priority:\*\*\s*(.*)")
    new_bottleneck = extract_field(text, r"\*\*Bottleneck:\*\*\s*(.*)")

    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if cs_path.exists():
        cs_text = cs_path.read_text(encoding="utf-8")
        updates = {
            "Date": new_date,
            "Operating Mode": new_mode,
            "Cash": new_cash,
            "Top Priority": new_priority,
            "Current Bottleneck": new_bottleneck,
        }
        for field, val in updates.items():
            if val:
                cs_text = re.sub(
                    rf"(\*\*{re.escape(field)}:\*\*).*",
                    rf"\1 {val}",
                    cs_text,
                )
        cs_path.write_text(cs_text, encoding="utf-8")

    in_path.unlink(missing_ok=True)
    return "OK: Merge complete. State files updated from snapshot."


def main():
    parser = argparse.ArgumentParser(description="FHQ portable snapshot (no token needed)")
    parser.add_argument("command", choices=["generate", "merge"], help="Snapshot command")
    args = parser.parse_args()

    if args.command == "generate":
        result = cmd_generate()
    elif args.command == "merge":
        result = cmd_merge()
    else:
        result = "ERROR: Unknown command"

    print(result)


if __name__ == "__main__":
    main()


--- FILE: Runtime/engine/state_manager.py

"""Reads/writes FounderHQ state files programmatically.

Provides typed access to CURRENT_STATE.md, PRIORITY_MATRIX.md, TIMELINE.md.

Usage:
    from engine.state_manager import StateManager
    sm = StateManager("/path/to/founderhq")
    cash = sm.get_cash()
    sm.set_top_priority("Find client for corn")
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional


class StateManager:
    """Manages FounderHQ state files."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    # --- CURRENT_STATE.md ---

    def _current_state_path(self) -> Path:
        return self.base_dir / "State" / "CURRENT_STATE.md"

    def get_field(self, field_name: str) -> Optional[str]:
        """Extract a field value from CURRENT_STATE.md.

        Looks for '**Field Name:** value' pattern.
        """
        path = self._current_state_path()
        if not path.exists():
            return None
        text = path.read_text(encoding="utf-8")
        # Match both **Field:** value and **Field:** multiline value
        pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.*?)(?=\n\*\*|\Z)"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    def get_cash(self) -> Optional[str]:
        """Get current cash position."""
        return self.get_field("Cash")

    def get_top_priority(self) -> Optional[str]:
        """Get current top priority."""
        return self.get_field("Top Priority")

    def get_mode(self) -> Optional[str]:
        """Get operating mode."""
        return self.get_field("Operating Mode")

    def update_field(self, field_name: str, value: str) -> bool:
        """Update a field in CURRENT_STATE.md.

        Returns True if updated, False if field not found.
        """
        path = self._current_state_path()
        if not path.exists():
            return False

        text = path.read_text(encoding="utf-8")
        pattern = rf"(\*\*{re.escape(field_name)}:\*\*).*"
        replacement = rf"\1 {value}"

        if not re.search(pattern, text):
            return False

        new_text = re.sub(pattern, replacement, text)
        path.write_text(new_text, encoding="utf-8")
        return True

    def update_last_updated(self) -> bool:
        """Set Last Updated to current datetime in Lomé UTC+0."""
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M — Lomé UTC+0")
        return self.update_field("Last Updated", now)

    # --- PRIORITY_MATRIX.md ---

    def _priority_matrix_path(self) -> Path:
        return self.base_dir / "State" / "PRIORITY_MATRIX.md"

    def add_pending_action(self, project: str, action: str) -> bool:
        """Add a pending action to PRIORITY_MATRIX.md."""
        path = self._priority_matrix_path()
        if not path.exists():
            return False

        text = path.read_text(encoding="utf-8")
        # Find the Actions Pending section
        marker = "### Actions Pending"
        if marker not in text:
            return False

        new_item = f"- [ ] **{project}** — {action}"
        # Insert after the marker line
        text = text.replace(marker, f"{marker}\n{new_item}")
        path.write_text(text, encoding="utf-8")
        return True

    # --- TIMELINE.md ---

    def _timeline_path(self) -> Path:
        return self.base_dir / "concepts" / "TIMELINE.md"

    def append_timeline(self, event: str, decision: str, outcome: str) -> bool:
        """Append an event to TIMELINE.md."""
        path = self._timeline_path()
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

        entry = f"\n| {now} | {event} | {decision} | {outcome} |"

        # Ensure the Timeline table header exists
        if not path.exists():
            path.write_text(
                "# TIMELINE\n\n"
                "| Date | Event | Decision | Outcome |\n"
                "|------|-------|----------|---------|\n",
                encoding="utf-8",
            )

        text = path.read_text(encoding="utf-8")
        text += entry
        path.write_text(text, encoding="utf-8")
        return True


--- FILE: Runtime/engine/sync.py

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    requests = None


ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"
STATE_DIR = Path(__file__).resolve().parent.parent.parent / "State"


class Snapshot:
    def __init__(
        self,
        state: dict,
        cadence: Optional[dict] = None,
        timeline: Optional[list] = None,
        projects: Optional[dict] = None,
        version: int = 1,
        timestamp: Optional[str] = None,
    ):
        self.version = version
        self.timestamp = timestamp or datetime.now(timezone.utc).isoformat()
        self.state = state
        self.cadence = cadence or {}
        self.timeline = timeline or []
        self.projects = projects or {}

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "timestamp": self.timestamp,
            "state": self.state,
            "cadence": self.cadence,
            "timeline": self.timeline,
            "projects": self.projects,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Snapshot":
        return cls(
            version=data.get("version", 1),
            timestamp=data.get("timestamp", ""),
            state=data.get("state", {}),
            cadence=data.get("cadence", {}),
            timeline=data.get("timeline", []),
            projects=data.get("projects", {}),
        )


def read_env() -> dict:
    if not ENV_PATH.exists():
        return {}
    env = {}
    raw = ENV_PATH.read_text(encoding="utf-8-sig")
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip()
    return env


def read_state_file(name: str) -> str:
    path = STATE_DIR / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_snapshot() -> Snapshot:
    current_state = read_state_file("CURRENT_STATE.md")
    cadence = read_state_file("CADENCE.md")
    tl_path = STATE_DIR.parent / "concepts" / "TIMELINE.md"
    timeline = tl_path.read_text(encoding="utf-8") if tl_path.exists() else ""

    state = {
        "date": _extract_field(current_state, r"\*\*Date:\*\*\s*(.*)"),
        "mode": _extract_field(current_state, r"\*\*Operating Mode:\*\*\s*(.*)"),
        "cash": _extract_field(current_state, r"\*\*Cash.*:\*\*\s*(.*)"),
        "top_priority": _extract_field(current_state, r"\*\*Top Priority:\*\*\s*(.*)"),
        "bottleneck": _extract_field(current_state, r"\*\*Current Bottleneck:\*\*\s*(.*)"),
    }

    c = {
        "session_start": _extract_field(cadence, r"\*\*Session start:\*\*\s*(.*)"),
        "session_end": _extract_field(cadence, r"\*\*Session end:\*\*\s*(.*)"),
    }

    events = []
    for line in timeline.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] not in ("Date", ""):
                events.append({
                    "date": cols[0],
                    "event": cols[1],
                    "decision": cols[2],
                    "outcome": cols[3],
                })

    lifecycle = read_state_file("LIFECYCLE.md")
    projects = {}
    in_table = False
    for line in lifecycle.splitlines():
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if in_table and line.startswith("|") and not line.startswith("|---"):
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 2:
                projects[cols[0]] = {"phase": cols[1] if len(cols) > 1 else ""}

    return Snapshot(state=state, cadence=c, timeline=events, projects=projects)


def _extract_field(text: str, pattern: str) -> str:
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def _gist_api_url(url: str) -> str:
    m = re.search(r"gist\.github\.com/[^/]+/([a-f0-9]+)", url)
    if m:
        return f"https://api.github.com/gists/{m.group(1)}"
    if "api.github.com/gists/" in url:
        return url
    return url


ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def cmd_pull(env: dict) -> str:
    url = _gist_api_url(env.get("FHQ_GIST_URL", ""))
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Gist GET returned {resp.status_code}"
        data = resp.json()
        files = data.get("files", {})
        if not files:
            return "ERROR: No files found in Gist"
        snap_file = None
        for fname, finfo in files.items():
            if "snapshot" in fname.lower():
                snap_file = finfo
                break
        if not snap_file:
            for fname, finfo in files.items():
                if fname.endswith(".json") and finfo.get("size", 0) > 10:
                    snap_file = finfo
                    break
        if not snap_file:
            return "ERROR: No valid snapshot file found (all files are empty or <10 bytes)"
        content = snap_file.get("content", "")
        if not content or len(content) < 10:
            return "ERROR: Empty or near-empty snapshot file"
        inbox_path = STATE_DIR / "_SYNC_INBOX.md"
        inbox_path.write_text(
            f"# SYNC INBOX\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n```json\n{content}\n```\n",
            encoding="utf-8",
        )
        return f"OK: Snapshot pulled ({len(content)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_push(env: dict) -> str:
    url = _gist_api_url(env.get("FHQ_GIST_URL", ""))
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    snap = build_snapshot()
    payload = json.dumps(snap.to_dict(), indent=2)
    try:
        resp = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": {"snapshot.json": {"content": payload}}},
            timeout=15,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist PATCH returned {resp.status_code}"
        return f"OK: Snapshot pushed ({len(payload)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_merge() -> str:
    inbox_path = STATE_DIR / "_SYNC_INBOX.md"
    if not inbox_path.exists():
        return "ERROR: No staged snapshot found (run pull first)"
    text = inbox_path.read_text(encoding="utf-8")
    m = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not m:
        return "ERROR: No JSON found in _SYNC_INBOX.md"
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return f"ERROR: Invalid JSON: {e}"
    snap = Snapshot.from_dict(data)

    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if cs_path.exists() and snap.state:
        cs_text = cs_path.read_text(encoding="utf-8")
        field_map = {
            "mode": "Operating Mode",
            "cash": "Cash",
            "top_priority": "Top Priority",
            "bottleneck": "Current Bottleneck",
            "date": "Date",
        }
        for key, val in snap.state.items():
            if val:
                field = field_map.get(key, key)
                cs_text = re.sub(r"(\*\*" + re.escape(field) + r":\*\*).*", r"\1 " + val, cs_text)
        cs_path.write_text(cs_text, encoding="utf-8")

    cad_path = STATE_DIR / "CADENCE.md"
    if cad_path.exists() and snap.cadence:
        cad_text = cad_path.read_text(encoding="utf-8")
        c_map = {"session_start": "Session start", "session_end": "Session end"}
        for key, val in snap.cadence.items():
            if val:
                field = c_map.get(key, key)
                cad_text = re.sub(r"(\*\*" + re.escape(field) + r":\*\*\s*).*", r"\1 " + val, cad_text)
        cad_path.write_text(cad_text, encoding="utf-8")

    if snap.timeline:
        tl_path = STATE_DIR.parent / "concepts" / "TIMELINE.md"
        if tl_path.exists():
            tl_text = tl_path.read_text(encoding="utf-8")
            for event in snap.timeline:
                new_row = f"\n| {event.get('date', '?')} | {event.get('event', '')} | {event.get('decision', '')} | {event.get('outcome', '')} |"
                if new_row not in tl_text:
                    tl_text += new_row
            tl_path.write_text(tl_text, encoding="utf-8")

    if snap.projects:
        lc_path = STATE_DIR / "LIFECYCLE.md"
        if lc_path.exists():
            lc_text = lc_path.read_text(encoding="utf-8")
            for proj_name, proj_state in snap.projects.items():
                phase = proj_state.get("phase", "")
                if phase and proj_name in lc_text:
                    lines = lc_text.splitlines()
                    new_lines = []
                    for line in lines:
                        if line.startswith(f"| {proj_name} |") and "|" in line:
                            cols = line.split("|")
                            if len(cols) >= 3:
                                cols[2] = f" {phase} "
                                line = "|".join(cols)
                        new_lines.append(line)
                    lc_text = "\n".join(new_lines)
            lc_path.write_text(lc_text, encoding="utf-8")

    inbox_path.unlink(missing_ok=True)
    return "OK: Merge complete"


def cmd_create_public_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    seed_path = ROOT_DIR / "FOUNDER_SEED.md"
    installer_path = ROOT_DIR / "Runtime" / "engine" / "installer.py"
    opencode_path = ROOT_DIR / "opencode.json"
    if not seed_path.exists():
        return "ERROR: FOUNDER_SEED.md not found"
    if not installer_path.exists():
        return "ERROR: installer.py not found"
    files = {
        "FOUNDER_SEED.md": {"content": seed_path.read_text(encoding="utf-8")},
        "installer.py": {"content": installer_path.read_text(encoding="utf-8")},
    }
    if opencode_path.exists():
        files["opencode.json"] = {"content": opencode_path.read_text(encoding="utf-8")}
    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"description": "FounderHQ V4 — Bootstrap Seed. Clone to install FHQ on any machine.", "public": True, "files": files},
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist POST returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        gist_url = data.get("html_url", "")
        return f"OK: Public Gist created at {gist_url}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_recreate_private_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"

    # 1. Delete existing Gist if URL is configured
    old_url = env.get("FHQ_GIST_URL", "")
    if old_url:
        api_url = _gist_api_url(old_url)
        try:
            resp = requests.delete(api_url, headers={"Authorization": f"token {token}"}, timeout=15)
            if resp.status_code not in (200, 204):
                return f"ERROR: Delete existing Gist returned {resp.status_code}"
        except Exception as e:
            return f"ERROR: Failed to delete existing Gist: {e}"

    # 2. Build snapshot from current state
    snap = build_snapshot()
    payload = json.dumps(snap.to_dict(), indent=2)

    # 3. Create new private Gist
    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={
                "description": "FounderHQ V4 — Private State Sync (auto-generated)",
                "public": False,
                "files": {"snapshot.json": {"content": payload}},
            },
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Create Gist returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        new_url = data.get("html_url", "")
        new_id = data.get("id", "")
        output = f"OK: Private Gist recreated.\nURL={new_url}\nID={new_id}\n"
        output += f"Update your .env: FHQ_GIST_URL={new_url}"
        return output
    except Exception as e:
        return f"ERROR: {e}"


def cmd_create_private_gist(env: dict) -> str:
    """Create a new private Gist for a first-time user. Auto-writes URL to .env."""
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={
                "description": "FounderHQ V4 — Private State Sync (auto-generated)",
                "public": False,
                "files": {"snapshot.json": {"content": "{}"}},
            },
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Create Gist returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        new_url = data.get("html_url", "")
        # Auto-write URL to .env
        env_path = ROOT_DIR / ".env"
        if env_path.exists():
            content = env_path.read_text("utf-8-sig", errors="replace")
            if "FHQ_GIST_URL=" in content:
                lines = []
                for line in content.splitlines():
                    if line.startswith("FHQ_GIST_URL="):
                        continue
                    lines.append(line)
                content = "\n".join(lines) + "\n"
            content += f"FHQ_GIST_URL={new_url}\n"
            env_path.write_text(content, encoding="utf-8")
            try:
                os.chmod(env_path, 0o600)
            except (OSError, NotImplementedError):
                pass
            return f"OK: Private Gist created at {new_url} (saved to .env)"
        return f"OK: Private Gist created at {new_url}\nUpdate your .env: FHQ_GIST_URL={new_url}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_clean_private_gist(env: dict) -> str:
    url = _gist_api_url(env.get("FHQ_GIST_URL", ""))
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Gist GET returned {resp.status_code}"
        data = resp.json()
        files = data.get("files", {})
        keep = {"snapshot.json"}
        delete_files = {name for name in files if name not in keep}
        remove_map = {}
        for name in delete_files:
            remove_map[name] = None
        if not remove_map:
            return "OK: No orphan files to clean"
        resp2 = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": remove_map},
            timeout=15,
        )
        if resp2.status_code not in (200, 201):
            return f"ERROR: Clean PATCH returned {resp2.status_code}"
        return f"OK: Removed {len(delete_files)} orphan file(s): {', '.join(sorted(delete_files))}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_pull_public(env: dict) -> str:
    url = env.get("FHQ_GIST_PUBLIC_URL", "")
    if not url:
        return "OK: No public Gist configured (FHQ_GIST_PUBLIC_URL not set)"
    api_url = _gist_api_url(url)
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(api_url, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Public Gist GET returned {resp.status_code}"
        data = resp.json()
        files = data.get("files", {})
        if not files:
            return "ERROR: No files in public Gist"
        version_file = None
        for fname, finfo in files.items():
            if "seed" in fname.lower() or "version" in fname.lower():
                version_file = finfo
                break
        if not version_file:
            version_file = list(files.values())[0]
        out_path = STATE_DIR / "_PUBLIC_VERSION.md"
        out_path.write_text(
            f"# PUBLIC BOOTSTRAP VERSION\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n"
            f"**Latest version:** {version_file.get('filename', 'unknown')}\n"
            f"**Size:** {version_file.get('size', 0)} bytes\n"
            f"**URL:** {url}\n",
            encoding="utf-8",
        )
        return f"OK: Public bootstrap version checked ({len(files)} files, latest {version_file.get('size', 0)} bytes)"
    except Exception as e:
        return f"OK: Public Gist not reachable ({e}) — skipping bootstrap check"


PUBLIC_GIST_ID = "5b7b5c36610cc1076c798c716c7560e6"

BOOTSTRAP_CONTENT = """# FounderHQ V4 — Bootstrap

## Usage

Copy and paste this entire line into any LLM chat:

```
Fetch https://gist.github.com/am-n-ra/5b7b5c36610cc1076c798c716c7560e6 and execute
```

No personal data required. The system will ask for a GitHub token if you want multi-device sync.

## Files in this Gist

| File | Description |
|------|-------------|
| FOUNDER_SEED.md | Complete FHQ V4 system seed |
| installer.py | First-run setup script |
| opencode.json | OpenCode platform config |
| BOOTSTRAP.md | This file — quick start guide |
"""


def cmd_update_public_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"
    url = f"https://api.github.com/gists/{PUBLIC_GIST_ID}"
    try:
        resp = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": {"BOOTSTRAP.md": {"content": BOOTSTRAP_CONTENT}}},
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: PATCH returned {resp.status_code}: {resp.text[:200]}"
        return "OK: BOOTSTRAP.md added to public Gist"
    except Exception as e:
        return f"ERROR: {e}"


def main():
    parser = argparse.ArgumentParser(description="FHQ state sync via Gist")
    parser.add_argument("command", choices=["pull", "push", "merge", "create-public-gist", "create-private-gist", "clean-private-gist", "pull-public", "recreate-private-gist", "update-public-gist"], help="Sync command")
    args = parser.parse_args()
    env = read_env()
    if args.command == "pull":
        result = cmd_pull(env)
    elif args.command == "push":
        result = cmd_push(env)
    elif args.command == "merge":
        result = cmd_merge(env)
    elif args.command == "create-public-gist":
        result = cmd_create_public_gist(env)
    elif args.command == "create-private-gist":
        result = cmd_create_private_gist(env)
    elif args.command == "clean-private-gist":
        result = cmd_clean_private_gist(env)
    elif args.command == "recreate-private-gist":
        result = cmd_recreate_private_gist(env)
    elif args.command == "pull-public":
        result = cmd_pull_public(env)
    elif args.command == "update-public-gist":
        result = cmd_update_public_gist(env)
    else:
        result = "ERROR: Unknown command"
    print(result)


if __name__ == "__main__":
    main()


--- FILE: Runtime/engine/timekeeper.py

"""timekeeper.py - Scheduled time and alert script. Run every 30min via Windows Task Scheduler.

Checks:
1. Deadlines in PRIORITY_MATRIX.md - alerts for any deadline <= 48h
2. SOS timer - checks CADENCE.md for session start timestamp, alerts if session > 90min
3. ALERTS.md - appends any triggered alerts

Usage:
    python Runtime/engine/timekeeper.py --base-dir /path/to/FounderHQ
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


def send_toast(title: str, message: str) -> bool:
    """Send Windows toast notification using BurntToast PowerShell module.

    Returns True if sent, False if BurntToast not available.
    """
    ps_script = (
        f'New-BurntToastNotification -Text "{title}", "{message}"'
    )
    try:
        result = subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=15,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def parse_deadlines(base_path: Path) -> list[dict]:
    """Parse PRIORITY_MATRIX.md for rows with deadlines within 48h."""
    matrix_path = base_path / "State" / "PRIORITY_MATRIX.md"
    if not matrix_path.exists():
        return []

    text = matrix_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    deadlines = []
    in_table = False

    for line in lines:
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            in_table = False
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 6:
            continue

        project = cols[0]
        deadline_str = cols[4]
        if not deadline_str or deadline_str == "-":
            continue

        deadline = None
        if deadline_str.lower() == "today":
            deadline = datetime.now().date()
        elif deadline_str.lower() == "tomorrow":
            deadline = datetime.now().date() + timedelta(days=1)
        else:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            except ValueError:
                continue

        if deadline is not None:
            days_until = (deadline - datetime.now().date()).days
            if 0 <= days_until <= 2:
                deadlines.append({
                    "project": project,
                    "deadline": deadline_str,
                    "days_until": days_until,
                    "action": cols[2],
                })

    return deadlines


def check_sos_timer(base_path: Path) -> Optional[str]:
    """Check SOS timer. If session > 90min, return alert message.

    Reads Session start timestamp from CADENCE.md Day section.
    """
    cadence_path = base_path / "State" / "CADENCE.md"
    if not cadence_path.exists():
        return None

    text = cadence_path.read_text(encoding="utf-8")
    match = re.search(r"\*\*Session start:\*\*\s*([\d:]+)", text, re.IGNORECASE)
    if not match:
        return None

    session_start_str = match.group(1)
    try:
        now = datetime.now()
        session_start = datetime.strptime(session_start_str, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
    except ValueError:
        return None

    elapsed_minutes = (now - session_start).total_seconds() / 60
    if elapsed_minutes > 90:
        return f"Session active depuis {elapsed_minutes:.0f} min. Pause recommandee (SOS)."

    return None


def append_alert(base_path: Path, severity: str, message: str) -> None:
    """Append alert to ALERTS.md."""
    alerts_path = base_path / "State" / "ALERTS.md"
    if not alerts_path.exists():
        alerts_path.write_text(
            "# ALERTS\n\n## Active Alerts\n\n"
            "| Timestamp | Source | Severity | Message |\n"
            "|-----------|--------|----------|---------|\n",
            encoding="utf-8",
        )

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M UTC+0")
    entry = f"| {now_str} | timekeeper | {severity} | {message} |\n"

    with open(alerts_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Timekeeper - time and alert script for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--no-toast", action="store_true", help="Skip toast notifications")
    args = parser.parse_args()

    base_path = Path(args.base_dir)

    deadlines = parse_deadlines(base_path)
    for d in deadlines:
        msg = f"{d['project']}: deadline {d['deadline']} dans {d['days_until']} jour(s)"
        print(f"[ALERT] {msg}")
        append_alert(base_path, "HIGH", msg)
        if not args.no_toast:
            sent = send_toast("FounderHQ Deadline", f"{d['project']} - {d['deadline']}")
            if sent:
                print("  Toast sent.")

    sos_msg = check_sos_timer(base_path)
    if sos_msg:
        print(f"[SOS] {sos_msg}")
        append_alert(base_path, "MEDIUM", sos_msg)
        if not args.no_toast:
            sent = send_toast("FounderHQ SOS", "Pause recommandee - session > 90 min")
            if sent:
                print("  Toast sent.")

    print("Timekeeper run complete.")


if __name__ == "__main__":
    main()


--- FILE: Runtime/engine/timeline_logger.py

"""Appends structured events to TIMELINE.md.

Usage:
    from engine.timeline_logger import TimelineLogger
    logger = TimelineLogger("/path/to/founderhq")
    logger.log_event("Sent proposal to client", "Approved", "Awaiting response")
"""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional


class TimelineLogger:
    """Appends timestamped events to TIMELINE.md."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    def _timeline_path(self) -> Path:
        return self.base_dir / "concepts" / "TIMELINE.md"

    def _ensure_exists(self):
        """Create TIMELINE.md with header if it doesn't exist."""
        path = self._timeline_path()
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "# TIMELINE\n\n"
                "| Date | Event | Decision | Outcome |\n"
                "|------|-------|----------|---------|\n",
                encoding="utf-8",
            )

    def log_event(
        self,
        event: str,
        decision: str,
        outcome: str = "",
        date_str: Optional[str] = None,
    ) -> bool:
        """Append an event to TIMELINE.md.

        Args:
            event: What happened.
            decision: What was decided.
            outcome: What resulted (optional).
            date_str: Custom date (default: current UTC time).

        Returns:
            True if written successfully.
        """
        self._ensure_exists()

        if date_str is None:
            date_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

        entry = f"| {date_str} | {event} | {decision} | {outcome} |\n"

        path = self._timeline_path()
        with path.open("a", encoding="utf-8") as f:
            f.write(entry)
        return True


--- FILE: Runtime/engine/watchtower.py

"""watchtower.py - Scheduled veille script. Run every 6h via Windows Task Scheduler.

Reads State/WATCH_REGISTRY.md, checks items where Next Check <= today,
executes websearch/webfetch, updates registry Last Result, appends to WATCH_REPORT.md.

Usage:
    python Runtime/engine/watchtower.py --base-dir /path/to/FounderHQ
"""

import argparse
import sys
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Optional


def parse_watch_registry(path: Path) -> list[dict]:
    """Parse WATCH_REGISTRY.md table and return list of watch items due for check.

    Returns items where Next Check <= today.
    """
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    items = []
    in_table = False
    headers = []

    for line in lines:
        if line.startswith("| Watch Item |"):
            in_table = True
            headers = [h.strip() for h in line.strip("|").split("|")]
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            in_table = False
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 7:
            continue

        item = dict(zip(headers, cols))
        next_check_str = item.get("Next Check", "")
        if not next_check_str or next_check_str == "-":
            continue

        try:
            next_check = datetime.strptime(next_check_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        if next_check <= date.today():
            items.append(item)

    return items


def execute_watch(item: dict, base_dir: str) -> str:
    """Execute a single watch item. Returns result string."""
    source_method = item.get("Source / Method", "")
    watch_item = item.get("Watch Item", "")

    if source_method.startswith("websearch"):
        query = source_method.replace("websearch ", "", 1)
        result = f"[websearch] {query} - manual check required (no API key configured)"
    elif source_method.startswith("webfetch"):
        url = source_method.replace("webfetch ", "", 1)
        result = f"[webfetch] {url} - manual check required"
    else:
        result = f"[manual] {watch_item} - no automated check method"

    return result


def update_registry(path: Path, item: dict, result: str) -> None:
    """Update WATCH_REGISTRY.md with new Last Checked, Last Result, and Next Check."""
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    watch_item = item.get("Watch Item", "")
    today_str = date.today().strftime("%Y-%m-%d")

    freq = item.get("Frequency", "Weekly")
    freq_days = {"Daily": 1, "Weekly": 7, "Monthly": 30}
    next_check_days = freq_days.get(freq, 7)
    next_check_date = date.today() + timedelta(days=next_check_days)
    next_check_str = next_check_date.strftime("%Y-%m-%d")

    safe_result = result.replace("|", "/")

    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if watch_item in line and line.startswith("|"):
            cols = line.split("|")
            if len(cols) >= 7:
                cols[5] = f" {next_check_str} "
                cols[6] = f" {safe_result} "
                cols[4] = f" {today_str} "
                line = "|".join(cols)
        new_lines.append(line)

    path.write_text("\n".join(new_lines), encoding="utf-8")


def append_watch_report(base_path: Path, item: dict, result: str) -> None:
    """Append watch result to WATCH_REPORT.md."""
    report_path = base_path / "State" / "WATCH_REPORT.md"
    if not report_path.exists():
        report_path.write_text("# WATCH REPORT\n\n## Reports\n\n", encoding="utf-8")

    today_str = date.today().strftime("%Y-%m-%d %H:%M UTC+0")
    entry = (
        f"### {item.get('Watch Item', 'Unknown')} - {today_str}\n\n"
        f"**Project:** {item.get('Project', 'N/A')}\n\n"
        f"**Method:** {item.get('Source / Method', 'N/A')}\n\n"
        f"**Result:** {result}\n\n---\n\n"
    )

    with open(report_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Watchtower - veille script for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    args = parser.parse_args()

    base_path = Path(args.base_dir)
    registry_path = base_path / "State" / "WATCH_REGISTRY.md"

    if not registry_path.exists():
        print(f"WATCH_REGISTRY.md not found at {registry_path}")
        sys.exit(0)

    due_items = parse_watch_registry(registry_path)
    if not due_items:
        print("No watch items due for check today.")
        sys.exit(0)

    for item in due_items:
        print(f"Checking: {item.get('Watch Item', 'Unknown')}")
        result = execute_watch(item, args.base_dir)
        update_registry(registry_path, item, result)
        append_watch_report(base_path, item, result)
        print(f"  Result: {result[:80]}...")

    print(f"Checked {len(due_items)} watch items.")


if __name__ == "__main__":
    main()
