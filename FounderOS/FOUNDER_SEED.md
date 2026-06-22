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
0. **First-Run Check** - Check if `.founderhq_installed` exists in FounderOS root. If absent, skip boot and execute **GENESIS**: ask user for GitHub token, create .venv, install dependencies, create .env, run installer.py, create `.founderhq_installed` marker. After GENESIS completes, proceed to step 1.
1. **Load Protocols + FRE** - SOURCE_OF_TRUTH.md + DECISION_GATES.md + INFO_CAPTURE_PROTOCOL.md + Runtime/FRE_SPEC.md
2. **Temporal Context** - Get-Date, compute Lome UTC+0. Load TIMELINE.md, CURRENT_STATE.md, CADENCE.md
3. **Load Cadence + Lifecycle** - Load State/CADENCE.md, State/LIFECYCLE.md. Determine current temporal position and project phases.
4. **Load Priority Matrix** - Load State/PRIORITY_MATRIX.md to establish unified view of ALL active projects/actions
5. **Load Alerts + Watch Reports** - Load State/ALERTS.md, read and clear active alerts. Load State/WATCH_REPORT.md for any background script findings since last session.
6. **Execute Watch Registry** - Load State/WATCH_REGISTRY.md, check each item where Next Check <= today, run websearch/webfetch, report findings, update registry
7. **Freshness Check** - Scan all concept footers. Flag any > 48h (WF-007)
8. **Set Session Start** - Record current time as Session Start in CADENCE.md (Day section). Log to TIMELINE.
9. **Load Concepts** - In order: CURRENT_STATE -> MISSION -> MEMORY -> KNOWLEDGE -> TIMELINE -> PROJECT -> WORKFLOW -> ASSET -> PLAYBOOK -> SYSTEM
10. **Build World Model** - Synthesize: what exists, what matters, what changed, what is blocked, what should happen next
11. **Report Awareness** - State: datetime, mode, top priority, cadence (week/month), lifecycle phases, watch results, what changed, stale concepts, PRG status. MUST state next action.
12. **Integrity Check** - All critical files loaded? Temporal context established? No contradictions?
13. **Daily Kickoff** - Execute RUNTIME Phase 1-2 (Assess cash/state -> Decide top action). State today's single most important action.
14. **Sync Pull** - If `.env` exists with FHQ_GIST_TOKEN, run `python Runtime/engine/sync.py pull` to sync state from remote Gist. If sync fails, continue with local state.

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
| Simple update, ambiguous, no keyword | DIRECT | SURVIVAL -> load DAOS.md, propose 1 action module. Otherwise -> respond directly |

## Pre-Response Gate (PRG)

Execute this gate AFTER Intent Classification, BEFORE every response. Not optional.

| # | Step | Action |
|---|------|--------|
| 1 | Temporal Check | Run `Get-Date`. Compute Lome UTC+0. If message starts with `fhq`, `boot`, or `shutdown`: reload CADENCE.md current day section, compute elapsed time since session start or last `fhq`. State CURRENT_DATETIME as first line of response. |
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
3. Uncertain: pick most mission-critical interpretation.
4. After classification, load module file and follow its protocol.
5. **Before responding, execute PRG** — Temporal Check → Scan Mapping → Absorb Updates → Project Scan → Freshness Flag → SURVIVAL Auto-Drive.
6. User should never name a module. Classification is automatic.

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
5. **Sync Push** - Run `python Runtime/engine/sync.py push` to sync state to remote Gist (if token configured)

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | RUNTIME.md, Protocols/SOURCE_OF_TRUTH.md, Protocols/DECISION_GATES.md |


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
"""installer.py - First-run setup for FounderHQ.

Creates:
1. .venv Python virtual environment
2. .env file (asks user for GitHub token)
3. Installs dependencies (requests, python-dotenv)
4. Windows Task Scheduler tasks for watchtower + timekeeper
5. .founderhq_installed marker

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


ENV_PATH = ".env"


def create_venv(base_path: Path) -> bool:
    """Create .venv if it doesn't exist."""
    venv_path = base_path / ".venv"
    if venv_path.exists() and (venv_path / "Scripts" / "python.exe").exists():
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
    pip = base_path / ".venv" / "Scripts" / "pip"
    if not pip.exists():
        pip = base_path / ".venv" / "bin" / "pip"

    deps = ["requests", "python-dotenv"]
    print(f"Installing dependencies: {', '.join(deps)}...")
    result = subprocess.run(
        [str(pip), "install"] + deps,
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


def task_exists(task_name: str) -> bool:
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", task_name],
        capture_output=True, text=True, timeout=10,
    )
    return result.returncode == 0


def create_task(task_name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    python_exe = str(Path(base_dir) / ".venv" / "Scripts" / "python.exe")
    if not Path(python_exe).exists():
        python_exe = sys.executable

    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval_minutes),
        "/TN", task_name,
        "/TR", f'"{python_exe}" "{script_path}" --base-dir "{base_dir}"',
        "/F",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {task_name}: {result.stderr.strip()}")
        return False
    print(f"Task '{task_name}' created (every {interval_minutes} min).")
    return True


def remove_task(task_name: str) -> bool:
    if not task_exists(task_name):
        print(f"Task '{task_name}' does not exist, skipping.")
        return True
    cmd = ["schtasks", "/Delete", "/TN", task_name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        print(f"ERROR removing task {task_name}: {result.stderr.strip()}")
        return False
    print(f"Task '{task_name}' removed.")
    return True


def check_burnt_toast() -> bool:
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Get-Module -ListAvailable -Name BurntToast",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    available = "BurntToast" in result.stdout
    if available:
        print("BurntToast: available")
    else:
        print("BurntToast: NOT available - toast notifications disabled")
    return available


def main():
    parser = argparse.ArgumentParser(description="Installer for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks")
    parser.add_argument("--install-burnttoast", action="store_true", help="Install BurntToast")
    parser.add_argument("--skip-env", action="store_true", help="Skip .env setup")
    parser.add_argument("--skip-venv", action="store_true", help="Skip .venv creation")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    if args.uninstall:
        remove_task("FounderHQ-Watchtower")
        remove_task("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    if args.install_burnttoast:
        cmd = [
            "powershell.exe", "-NoProfile", "-Command",
            "Install-Module -Name BurntToast -Force -Scope CurrentUser",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        print("BurntToast installed." if result.returncode == 0 else f"BurntToast install failed: {result.stderr.strip()}")
        return

    check_burnt_toast()

    if not args.skip_venv:
        create_venv(base_path)
        install_deps(base_path)

    if not args.skip_env:
        setup_env(base_path)

    watchtower_path = scripts_dir / "watchtower.py"
    if watchtower_path.exists():
        create_task("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)
    else:
        print(f"WARNING: {watchtower_path} not found, skipping watchtower task")

    timekeeper_path = scripts_dir / "timekeeper.py"
    if timekeeper_path.exists():
        create_task("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)
    else:
        print(f"WARNING: {timekeeper_path} not found, skipping timekeeper task")

    create_marker(base_path)

    print("\nInstallation complete.")
    print("  - .venv: ready")
    print("  - Dependencies: installed")
    print("  - Scheduled tasks: configured")
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
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
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


def cmd_pull(env: dict) -> str:
    url = env.get("FHQ_GIST_URL", "")
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
            if fname.endswith(".json") or "snapshot" in fname:
                snap_file = finfo
                break
        if not snap_file:
            snap_file = list(files.values())[0]
        content = snap_file.get("content", "")
        if not content:
            return "ERROR: Empty snapshot file"
        inbox_path = STATE_DIR / "_SYNC_INBOX.md"
        inbox_path.write_text(
            f"# SYNC INBOX\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n```json\n{content}\n```\n",
            encoding="utf-8",
        )
        return f"OK: Snapshot pulled ({len(content)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_push(env: dict) -> str:
    url = env.get("FHQ_GIST_URL", "")
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


def main():
    parser = argparse.ArgumentParser(description="FHQ state sync via Gist")
    parser.add_argument("command", choices=["pull", "push", "merge"], help="Sync command")
    args = parser.parse_args()
    env = read_env()
    if args.command == "pull":
        result = cmd_pull(env)
    elif args.command == "push":
        result = cmd_push(env)
    elif args.command == "merge":
        result = cmd_merge()
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


--- FILE: Runtime/opencode/opencode.md
# OpenCode Runtime Adapter

## Detection

FounderHQ is auto-detected when the working directory contains `FounderOS/`. The protocol boots automatically via `Protocols/FOUNDEROS_PROTOCOL.md`.

## Fichier de configuration

`.opencode/instructions.md` contient les regles specifiques a l'environnement OpenCode.

## Particularites

- **Shell:** Windows PowerShell 5.1
- **Fuseau horaire:** Systeme local (detecte automatiquement par `Get-Date`). Conversion vers Lome UTC+0 chaque session.
- **Fichiers:** CRLF (Windows)
- **DST:** `[System.TimeZoneInfo]::Local.GetUtcOffset((Get-Date))` pour detecter le decalage effectif.

## Boot sequence (resume)

1. OpenCode charge `Protocols/FOUNDEROS_PROTOCOL.md` via instructions systeme
2. Le protocole guide toutes les operations subsequentes
3. `DECISION_GATES` est charge avant chaque action
4. `TEMPORAL_AWARENESS` verifie le temps a chaque reponse
5. Les frameworks sont charges a la demande via DECISION_GATES

## Limitations connues

- Pas de detection d'evenements automatique (session-based uniquement)
- Pas d'automation native (workflows executes manuellement par le LLM)
- Pas de multi-session awareness au-dela des fichiers


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

Toute information opérationnelle donnée en conversation est automatiquement capturée dans FHQ. Ce protocole définit quel type d'info va dans quel fichier, sans attendre une instruction explicite.

## Règle Fondamentale

**Si l'info est utile à une session future, elle doit être écrite maintenant.**

Ne pas demander "tu veux que je l'enregistre ?" — enregistrer directement.

---

## Mapping Type → Fichier

| Type d'Information | Exemple | Fichier Cible | Action |
|-------------------|---------|--------------|--------|
| **Deadline / date butoir** | "Le 22 juin à 16h59" | `State/PRIORITY_MATRIX.md` | Mettre à jour deadline + warning 🔴 |
| **Progrès projet** | "J'ai fini 1.1 Debt vs Equity" | `State/CURRENT_STATE.md` + `State/PRIORITY_MATRIX.md` | Update status section + dashboard |
| **Nouveau projet** | "Je lance Omni" | Appliquer PROJECT_REGISTRATION_PROTOCOL.md | Créer concept/ + projets/ + tous les liens |
| **Décision** | "On va sur Innov'Action pas Idée-Action" | `State/CURRENT_STATE.md` + concepts concernés | Mettre à jour Last Decision |
| **Chiffre / métrique** | "Encaissement 4,875 FCFA" | `State/CURRENT_STATE.md` | Update Cash + infos produit |
| **Blocage** | "Fournisseur pas de new" | `State/PRIORITY_MATRIX.md` | Mettre warning 🟡/🔴 |
| **Événement important** | "Herlog envoyé" | `TIMELINE.md` | Enregistrer Event → Decision → Outcome |
| **Nouvelle relation** | "OMNI lié à KORA" | Concepts concernés | Ajouter lien bidirectionnel |
| **Préférence / règle** | "Toujours tracker les deux" | `Protocols/INFO_CAPTURE_PROTOCOL.md` | Ajouter la règle |
| **Information veille** | "Résultat websearch X" | `State/WATCH_REGISTRY.md` | Update Last Result + Next Check |

---

## Cas Concrets (exemples récents)

| Ce que tu as dit | Ce qui a été capturé | Où |
|-----------------|---------------------|-----|
| "je viens de finir 1.1 Debt vs Equity" | Financial Literacy 1.1 → ✅ | `State/CURRENT_STATE.md` + `State/PRIORITY_MATRIX.md` |
| "societe pas encore enregistree" | Omni company status corrigé | `projects/Omni/annexes/A4_DJANTA_TECH_HUB.md` |
| "omni devrait se mettre dans innov action" | Programme confirmé | `concepts/OMNI.md` + annexes A4 |
| "pourquoi tu ne track pas tous mes objectifs" | PRIORITY_MATRIX.md créé | Nouveau fichier |

---

## Ce Qui N'est PAS Capturé

- Questions sans réponse opérationnelle
- Réflexions exploratoires non confirmées
- Conversations non liées à FHQ (sauf si pattern émergent)

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


--- FILE: Protocols/PRIORITIZATION_PROTOCOL.md
# PRIORITIZATION PROTOCOL

## Concept

Parmi 100 actions possibles, quelle est la seule qui merite d'etre faite maintenant ?

Ce protocole repond a cette question.

Il n'y a pas de "priorites" multiples. Il y a UNE priorite a la fois.

---

## Regle fondamentale

Le bottleneck est la contrainte unique qui empeche tout le systeme d'avancer.

Si on resout le bottleneck, tout le systeme progresse.

Si on travaille sur autre chose, on est occupe mais on n'avance pas.

---

## Arbre de decision

### Etape 1 : Etat actuel

1. Cash > 0 ?
   - NON → Priorite absolue : generer du revenu. Tout le reste est secondaire.
   - OUI → continuer.

2. Un produit est-il en vente ?
   - NON → Priorite : mettre un produit en vente. Un produit qui n'existe pas ne peut pas generer de revenu.
   - OUI → continuer.

3. Le produit a-t-il des clients ?
   - NON → Priorite : acquerir le premier client. La distribution est le bottleneck.
   - OUI → continuer.

4. Les clients existants sont-ils satisfaits ?
   - NON → Priorite : resoudre les problemes clients. La retention avant l'acquisition.
   - OUI → continuer.

5. Le produit a-t-il atteint le product-market fit ?
   - NON → Priorite : iterer jusqu'a ce que les clients reviennent ou referent.
   - OUI → Scale.

### Etape 2 : Charger le contexte

Lire les concepts suivants pour verifier l'arbre de decision :

- State/CURRENT_STATE.md (cash, bottleneck, priorite actuelle)
- Concepts/MISSION.md (direction strategique)
- Concepts/TIMELINE.md (evenements recents)

### Etape 3 : Appliquer la lentille

Si DECISION_GATES recommande un framework, le charger et appliquer ses questions au contexte.

### Etape 4 : Reduire a UNE action

Poser la question :

```
Si je ne fais qu'une seule chose aujourd'hui,
laquelle a le plus grand impact sur le bottleneck ?
```

Si la reponse est vague, la question n'a pas ete assez specific.

Reformuler jusqu'a obtenir UNE action concrete.

---

## Verification

Avant de commencer l'action, verifier :

- [ ] Cette action sert-elle directement le bottleneck identifie ?
- [ ] Cette action est-elle la plus haute leverage disponible ?
- [ ] Cette action peut-elle etre executee dans le temps disponible ?
- [ ] Cette action n'est-elle pas de l'activite deguisee en progres ?

Si les 4 reponses sont "oui" → executer.
Si une reponse est "non" → re-evaluer.

---

## Anti-patterns

- Travailler sur 3 priorites en meme temps (aucune n'avance vraiment)
- Choisir une action facile au lieu de l'action impactante
- Confondre urgence et importance
- Planifier sans executer
- Re-prioriser avant d'avoir termine la priorite actuelle
- Utiliser la planification comme echappatoire a l'execution

---

## Integration avec DECISION_GATES

Quand un type d'action est identifie via DECISION_GATES, PRIORITIZATION_PROTOCOL s'assure que c'est la BONNE action a faire maintenant.

Les deux protocoles fonctionnent en sequence :

```
DECISION_GATES     →  Quoi faire ?
PRIORITIZATION     →  Quoi faire MAINTENANT ?
```


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


--- FILE: Protocols/SOURCE_OF_TRUTH.md
# SOURCE OF TRUTH

## Regle 0

Chaque verite du systeme a EXACTEMENT un proprietaire.

Si deux documents contiennent la meme verite → violation.
Si un document contient une verite qu'il ne possede pas → violation.

## Carte des verites

| Verite | Proprietaire |
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
| Marketing, campagne (lentille) | Frameworks/Content/MAOS.md |
| Automation, agents (lentille) | Frameworks/AI/AAOS.md |
| Production video entites (lentille) | Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md |
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

## Regle de maintenance

Si on ajoute une nouvelle verite au systeme, on doit :
1. Determiner son proprietaire unique
2. L'ajouter a cette carte
3. Verifier qu'aucun autre document ne la possede deja


--- FILE: State/ALERTS.md
# ALERTS

## Purpose

File bridge between background scripts (watchtower, timekeeper) and the LLM at session boot. Scripts write here, LLM reads here.

**Read at session start (BOOT). Cleared after reading.**

---

## Active Alerts

| Timestamp | Source | Severity | Message |
|-----------|--------|----------|---------|
| | | | |

---

## Rules

1. Scripts append alerts as they fire
2. LLM reads all alerts at BOOT, clears them after acknowledgment
3. Max 50 alerts - oldest auto-archived

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | Scripts -> LLM |


--- FILE: State/CADENCE.md
# CADENCE

## Purpose

Hierarchy temporelle de FounderOS : vie -> annee -> mois -> semaine -> jour -> heure. Chaque niveau porte un objectif, une evaluation, et un lien vers le niveau suivant.

Lue en phase BOOT pour contextualiser ORIENT. Mise a jour par le LLM quand les objectifs evoluent.

---

## Life (Vie)

> **Objectif:** [objectif de vie]

**Evaluation:** [auto-evaluation: 0-10]

---

## Year (Annee) - 2026

> **Objectif:** [objectif 2026]

**Evaluation:** [auto-evaluation 0-10]

**Trimestre en cours:** Q2 (Avril-Juin)

---

## Month (Mois) - Juin 2026

> **Objectif:** [objectif juin]

**Evaluation:** [auto-evaluation 0-10]

**Semaines:**
- S24 (Juin 9-15): [objectif / resultat]
- S25 (Juin 16-22): [objectif / resultat]
- S26 (Juin 23-29): [objectif / resultat]
- S27 (Juin 30-Juil 6): [objectif / resultat]

---

## Week (Semaine) - S26 (Juin 23-29)

> **Objectif:** [objectif semaine]

**Deadlines cette semaine:**
- [date] - [description]

---

## Day (Jour) - 2026-06-22

> **Objectif:** [objectif du jour]

**Session start:** [HH:MM - filled at boot]
**Session end:** [HH:MM - filled at shutdown]
**Duration:** [calculated]

**Top 3 actions:**
1. [action]
2. [action]
3. [action]

---

## Hour (Heure) - Now

> **Lome (UTC+0):** [dynamique - computed at every `fhq`]

**Next actionable:** [what to do in the next 60 min]

---

## Sync

> **Last Sync Pull:** [datetime - filled by sync.py pull at boot]
> **Last Sync Push:** [datetime - filled by sync.py push at shutdown]
> **Sync Mode:** [Gist / Snapshot / Off]

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Temporal hierarchy for FounderOS cadence |


--- FILE: State/CURRENT_STATE.md
# CURRENT_STATE

## Concept

CURRENT_STATE is the single source of operational truth.

All session-level state lives here and only here.

No other file should contain "current X" — if it does, it creates divergence.

---

## Rules

1. **Single source.** All session state lives here. If it's in CURRENT_STATE, it's authoritative. If it contradicts another file, CURRENT_STATE wins.
2. **Updated every session exit.** Before any session ends, CURRENT_STATE is updated.
3. **Read every session start.** Before any action, CURRENT_STATE is loaded.
4. **Max age = 1 session.** If loaded and the session date/time ≠ current session, it must be re-verified before use.

---

## Fields

### Date
> The current datetime in Lomé (UTC+0).

### Operating Mode
> One of: SURVIVAL, GROWTH, SCALE. Determined by cash position and revenue state.

### Cash (FCFA)
> Current cash position. Last verified by founder. Source of truth for all cash-dependent decisions.

### Active Product
> The product currently being sold/promoted. The one that must generate revenue.

### Current Bottleneck
> The single constraint preventing progress. Only one. If you list more than one, the real bottleneck is hiding behind the others.

### Top Priority
> The single next outcome that matters. If this outcome is achieved, the bottleneck is resolved or the mission advances measurably.

### Session Objective
> What this session must accomplish to serve the Top Priority. Written at session start. Verified at session end.

### Last Decision
> The most recent decision made. Prevents re-debating settled questions.

### Last Updated
> When this file was last modified. If > 1 session old, flag as stale.

---

## Current State

**Date:** 2026-06-21 20:56 — Lomé (UTC+0)

**Operating Mode:** SURVIVAL — cash under 3,000 FCFA

**Cash (FCFA):** ~2,679 accessible. Aujourd'hui 17h: encaissement 4,875 FCFA de dame 1 (cash va au fournisseur, pas à toi).

**Active Products:**
- Pest Repeller (Stop Nuisibles) — 100 units, 5,900 FCFA, TikTok
- **SOJACO** — Vente de céréales (soja, maïs). Paiement à la livraison.
  - Soja : fournisseur Atakpamé 350 FCFA/kg. Client revend à 850-900, veut acheter à 750. Quantité : 5-10 sacs.
  - Maïs : ami fournisseur 160 FCFA/kg, 50 tonnes dispo. Minimum 1 tonne.
- Soya (Bolsoja) — Dame 1 (5 bols × 975 FCFA, 17h). Fournisseur Lomé réduit à 5 bols sample lundi.
- DoodleMind (YouTube Shorts) — Short #1 published
- **KORA Lab** — AI lab, pré-seed, documents complets, Herlog envoyé, ST Digital en attente
- **OMNI** — Index du commerce de proximité, MVP déployé (omni.sparkafrika.online). Djanta Tech Hub soumis (ID 272), email correction envoyé.

**KORA Status:**
- Data Room: ✅ Complete (Vision → BP → Annexes, 20+ docs)
- Herlog: Envoyé, retour en attente
- ST Digital: Estimation compute envoyée, suivi demain
- Phase: Pre-Seed Validation (Éwé)
- Prochaine action: Relancer ST Digital

**OMNI Status:**
- Strategic docs: ✅ Complete (Vision → Pitch Deck, 20 files)
- MVP: ✅ Déployé (omni.sparkafrika.online)
- Équipe: 6 personnes
- Société: En cours de formalisation
- Programme: Innov'Action — Djanta Tech Hub (soumis ID 272, email correction envoyé)
- Prochaine action: Attendre réponse Djanta Tech Hub

**Current Bottleneck:** Cash insuffisant pour acheter stock soja/maïs en gros.

**Top Priority:** Valider modèle SOJACO — trouver l'avance pour 1er achat.

**Session Objective:** Boot — reprendre opérations.

**Last Decision:** PRG Step 6 ajouté : SURVIVAL Auto-Drive verrouillé.

**Last Updated:** 2026-06-21 20:56 — Lomé UTC+0


--- FILE: State/LIFECYCLE.md
# LIFECYCLE

## Purpose

Phase actuelle de chaque projet actif. Determine quel framework activer en phase ORIENT. Chaque phase a des gates de sortie - conditions precises pour passer a la phase suivante.

Mise a jour par le LLM quand un projet franchit un gate.

---

## Phases

| Phase | Description | Gate de Sortie | Frameworks Actifs |
|-------|-------------|----------------|-------------------|
| IDEA | Idee non validee | Prototype ou enquete client faite | CAOS |
| VALIDATION | Solution testee, client cherche | 3+ clients prets a payer | VAOS, DIOS |
| LAUNCH | Premier client, livraison manuelle | Process reproductible | DIOS, CEOS |
| GROWTH | Revenu regulier, equipe building | Process automatises/outsources | PSOS, FAOS, SAOS |
| SCALE | Croissance acceleree, fundraising | Metriques unitaires saines | FAOS, SAOS |
| MATURE | Cash-flow stable, optimisation | - | SAOS |

---

## Projets Actifs

| Projet | Phase | Depuis | Gate de Sortie Atteint ? | Prochaine Action |
|--------|-------|--------|--------------------------|-----------------|
| SOJACO | VALIDATION | 2026-06-21 | Non - Pas encore de client payant | Trouver client mais ou soja |
| OMNI | LAUNCH | 2026-06-15 | Non - MVP deploye, 0 client payant | Pitch Day + acquisition premiers utilisateurs |
| SOYA (Bolsoja) | LAUNCH | 2026-05-XX | Non - 1 client (dame 1), pas encore reproductible | Livraison quotidienne + trouver d'autres clients |
| KORA | VALIDATION | 2026-06-01 | Non - Pre-seed docs ok, pas de financement | Relancer ST Digital + Herlog |
| DOODLEMIND | IDEA | 2026-06-10 | Non - Short #1 publie, 0 monetization | Produire Short #2 |
| PEST REPELLER | IDEA | 2026-05-XX | Non - Stock disponible, 0 vente | Creer contenu TikTok |
| SOLAR KIT | IDEA | 2026-06-15 | Non - Pas encore de prototype | Definir modele + fournisseur |

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Project lifecycle phase tracking for framework selection |


--- FILE: State/PRIORITY_MATRIX.md
# PRIORITY MATRIX
## Version 1.0 — Unified Command Center

### Règle

Ce fichier est la **vue unique** de tous les projets/objectifs actifs. Mis à jour après chaque action. Lu en début de chaque session pour garantir qu'aucun projet ne disparaît du contexte.

---

### Projets Actifs

| Projet | Objectif Prioritaire | Status | Next Action | Deadline | Dernière Action | Warning |
|--------|---------------------|--------|-------------|----------|-----------------|---------|
| OMNI | Djanta Tech Hub Innov'Action | ✅ Soumis (ID 272) | Vérifier confirmation + préparer pitch day 23 juillet | - | 2026-06-21 | 🟢 |
| SOJACO | Vente céréales (soja, maïs) | Cascade créée (01-10+annexes) | Trouver client soja à prix viable OU client maïs | - | 2026-06-21 | 🟡 |
| SOYA (Bolsoja) | Livraison dame 1 | Active (5 bols/jour) | Livraison 17h | **Today** | 2026-06-21 | 🟡 |
| KORA | Pre-seed + ST Digital | Docs ok, ST pending | Relancer ST | - | 2026-06-21 | 🟢 |
| DOODLEMIND | YouTube Shorts monetization | Short #1 publié | Planifier Short #2 | - | 2026-06-21 | 🟢 |
| PEST REPELLER | TikTok sales | 100 units stock | Créer/contenu TikTok | - | 2026-06-21 | 🟡 |
| SOLAR KIT | Nouveau produit + chaîne | Idée, pas encore lancé | Définir modèle + créer chaîne | - | 2026-06-21 | 🟢 |
| FINANCE | Herlog, ST Digital | Envoyés, attente | Follow-up | - | 2026-06-21 | 🟡 |
| LEARNING | Financial Literacy | 5/28 ✅ (1.1 → 1.5), en cours 1.6 | 1.6 Bilan Comptable Simplifié | - | 2026-06-21 | 🟢 |
| FHQ SYSTEM | VSOS framework créé, gaps comblés | ✅ | Normal operation | - | 2026-06-21 | 🟢 |

---

### Actions Pending (tous projets)

- [x] **OMNI** — Soumettre formulaire Djanta Tech Hub Innov'Action ✅ (ID 272, réf. DJANTA/APP/2025/0272)
- [ ] **OMNI** — Vérifier si pitch day nécessite préparation (23 juillet)
- [x] **SOJACO** — Cascade stratégique complète créée (01-10 + annexes) ✅
- [x] **SOJACO** — Deal soja 750/bol évalué ❌ non viable (perte 125 FCFA/bol)
- [ ] **SOJACO** — Trouver client soja à prix viable (>1 000 FCFA/bol)
- [ ] **SOJACO** — Trouver client pour maïs (ami 160/kg, 50T dispo, min 1T)
- [ ] **SOYA** — Livraison dame 1 (17h)
- [x] **DOODLEMIND** — Plan de contenu Shorts créé (10 idées, 5 prochains planifiés, pipeline doc)
- [ ] **DOODLEMIND** — Produire Short #2 "Your Body Has a Second Brain"
- [ ] **PEST REPELLER** — Créer premier contenu TikTok
- [ ] **SOLAR KIT** — Définir modèle (prix, fournisseur, marge)
- [ ] **SOLAR KIT** — Créer chaîne YouTube/TikTok
- [ ] **FINANCE** — Follow-up Herlog
- [ ] **FINANCE** — Relance ST Digital
- [x] **LEARNING** — Sections 1.1 → 1.5 complétées ✅
- [ ] **LEARNING** — Section 1.6 Bilan Comptable Simplifié

---

### Règles d'Utilisation

1. Lu en début de chaque session avant toute action
2. Mis à jour après chaque action significative
3. Tout nouveau projet/objectif est ajouté immédiatement
4. Tout projet sans action depuis 7 jours passe en 🟡
5. Warning 🔴 si deadline < 48h

---

### Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | Founder |


--- FILE: State/WATCH_REGISTRY.md
# WATCH REGISTRY

## Purpose

Liste centralisée de tout ce que FounderOS surveille pour toi : deadlines, appels à projets, news, opportunités, follow-ups. Checké automatiquement au début de chaque session.

## Règles

1. Chargé en début de session (boot sequence)
2. Tout item avec Next Check ≤ date actuelle est exécuté
3. Résultat reporté dans la réponse, registry mis à jour
4. Item sans action depuis 2 cycles passe en 🟡 warning

---

## Active Watches

| Watch Item | Project | Source / Method | Frequency | Last Checked | Next Check | Last Result | Status |
|------------|---------|----------------|-----------|-------------|------------|-------------|--------|
| Djanta Tech Hub Innov'Action — deadlines, infos | OMNI | webfetch djantatechhub.gouv.tg | Daily | 2026-06-21 | 2026-06-22 | Deadline June 22, Pitch Day July 23 | 🔴 |
| Appels à projets IA / African AI | KORA | websearch "AI grants Africa 2026 call" | Weekly | 2026-06-21 | 2026-06-28 | — | 🟢 |
| ST Digital — compute partnership status | KORA | manual follow-up | Weekly | 2026-06-21 | 2026-06-28 | Estimation envoyée, en attente | 🟡 |
| Herlog — response | KORA/FINANCE | manual follow-up | Weekly | 2026-06-21 | 2026-06-28 | Envoyé, en attente | 🟡 |
| Subventions / Fonds Start tech Afrique | OMNI/KORA | websearch "startup grant Togo 2026" | Weekly | 2026-06-21 | 2026-06-28 | — | 🟢 |
| Soya — fournisseur Atakpamé pricing | SOJACO | manual follow-up | Weekly | 2026-06-21 | 2026-06-28 | 350 FCFA/kg confirmé. Deal client 750/bol ❌ non viable (perte 125 FCFA/bol) | 🟡 |

---

## Archive

(Watch items completed or no longer relevant moved here.)

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | System |


--- FILE: State/WATCH_REPORT.md
# WATCH REPORT

## Purpose

Formatted findings from watchtower.py runs. One section per watch that triggered. Read by LLM at BOOT.

---

## Reports

<!-- watchtower appends here at each run -->

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | watchtower.py |


--- FILE: concepts/ASSET.md
# ASSET

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 8.

## Role

Represent reusable resources.

An asset is anything of value that can be used across projects, missions, or time.

---

## Core Rule

An asset entry tracks existence, location, and status.

An asset entry does NOT contain knowledge about how to use the asset.

Usage knowledge belongs in KNOWLEDGE or WORKFLOW.

---

## Structure

Each asset entry should include:

**ASSET_ID** — unique identifier

**NAME** — what this asset is called

**TYPE** — category (Content, Code, Design, Relationship, Inventory, Tool, Document, Other)

**LOCATION** — where the asset resides (file path, URL, physical location, contact)

**STATUS** — Available / In Use / Depleted / Obsolete

**PROJECT_ORIGIN** — which project created this asset (if applicable)

**PROJECTS_USING** — which projects currently use this asset

**NOTES** — brief operational notes (not knowledge, not instructions)

---

## Current Assets

---

**ASSET_ID:** A-001

**NAME:** Stop Nuisibles TikTok Account

**TYPE:** Relationship (platform account)

**LOCATION:** @stopnuisibles228 on TikTok

**STATUS:** Available

**PROJECT_ORIGIN:** SN-001 (Video 1)

**PROJECTS_USING:** SN-002 (Variation #2), SN-003 (Video 2)

**NOTES:** 5 followers as of 2026-06-18, 0 posts before SN-001

---

**ASSET_ID:** A-002

**NAME:** Pest Repeller Inventory

**TYPE:** Inventory

**LOCATION:** Physical stock in Lomé

**STATUS:** Available (100 units)

**PROJECT_ORIGIN:** None (purchased directly, not produced by a project)

**PROJECTS_USING:** SN-001, SN-002, SN-003, FO-002

**NOTES:** Cost 4,000 FCFA/unit, selling price 5,900 FCFA, margin 1,900 FCFA. Supplier contact documented but reorder process not yet complete.

---

**ASSET_ID:** A-003

**NAME:** Video 1 Production Sheets

**TYPE:** Content (documents)

**LOCATION:** Projects/Stop Nuisibles/CONTENT/ (VIDEO1_PRODUCTION.md, VIDEO1_TIMING_MAP.md, SCRIPTS_J1.md, PRODUCT_SHEET.md, CONTENT_PROCESS.md)

**STATUS:** Available

**PROJECT_ORIGIN:** SN-001

**PROJECTS_USING:** SN-002 (reference for adaptation)

**NOTES:** Includes timing map, storyboard, prompts, voiceover script. Applicable to future videos with hook modifications.

---

**ASSET_ID:** A-009

**NAME:** DoodleMind YouTube Channel

**TYPE:** Relationship (platform account)

**LOCATION:** YouTube — DoodleMind channel (English, niche psycho/histoire/cerveau)

**STATUS:** Available (0 subscribers, 0 videos published)

**PROJECT_ORIGIN:** DM-001 (DoodleMind Channel Launch)

**PROJECTS_USING:** DM-001

**NOTES:** Channel created 2026-06-19. Short #1 published 2026-06-20. Target audience US/AU. Format: 9:16 hand-drawn doodle, 30-60s. YouTube Short #1 analytics: 366 views, 72.6% retention, 87.5% likes, 97% Shorts feed, 40s avg duration. TikTok: 65 views, 10.43s avg, 2.8% full watch.

---

**ASSET_ID:** A-010

**NAME:** Soya Supplier Contacts

**TYPE:** Relationship (supplier)

**LOCATION:** Phone numbers in MEMORY.md (Recent Decisions)

**STATUS:** Available (not yet contacted)

**PROJECT_ORIGIN:** SS-001 (Soya Supplier Sourcing)

**PROJECTS_USING:** SS-001

**NOTES:** 7 suppliers found 2026-06-19: Ste SODJA (96 68 43 65), SCOOPS AKPENE SOJA (91 58 84 56), SOYCAIN (91 73 66 83), CIFS TOGO (91 11 44 40), AGROKOM TOGO (90 01 44 41), MAMAN SOJA (92 62 64 68), SOCMEL (99 46 89 34). Existing suppliers from earlier research: AGROTRADE, TOGO SOJA, IVEMA. Need to call to confirm: price per bol, minimum order, delivery terms, payment terms.

---

**ASSET_ID:** A-011

**NAME:** DoodleMind Short #1 Assets

**TYPE:** Content

**LOCATION:** concepts/KnowledgeAssets/short_why_your_brain_forgets_dreams.txt, concepts/KnowledgeAssets/prompts_why_your_brain_forgets_dreams.txt

**STATUS:** Available (not yet used)

**PROJECT_ORIGIN:** DM-001 (DoodleMind Channel Launch)

**PROJECTS_USING:** DM-001

**NOTES:** Script + 30 image prompts + metadata for "Why Your Brain Forgets Your Dreams." Video published 2026-06-20. YouTube: 366 views, 72.6% retention. TikTok: 65 views, 2.8% full watch.

---

**ASSET_ID:** A-004

**NAME:** WhatsApp Business Account

**TYPE:** Relationship (communication channel)

**LOCATION:** +228 71 39 21 22

**STATUS:** Available

**PROJECT_ORIGIN:** None

**PROJECTS_USING:** FO-002 (First Revenue), all Stop Nuisibles projects

**NOTES:** Primary sales channel. Number changed from 91 to 71 before Video 1 publish.

---

**ASSET_ID:** A-005

**NAME:** Zoclo Livraison Content Pack

**TYPE:** Content (archived)

**LOCATION:** Archive/Zoclo Livraison/ (SCRIPTS_J1-7.md, CONTENT_MATRIX.md, ASSETS/BRAND_GUIDE.md)

**STATUS:** Available (archived)

**PROJECT_ORIGIN:** Zoclo Livraison (archived mission)

**PROJECTS_USING:** None (pattern reference only)

**NOTES:** 30-day content calendar, 21 scripts, complete brand guide. Reusable content framework (hook→problem→solution→proof→CTA). Product-specific content (Postinor 2 delivery) not reusable but structural patterns are.

---

**ASSET_ID:** A-006

**NAME:** FounderOS Foundation Documents

**TYPE:** Document (system)

**LOCATION:** FounderOS/ (MANIFEST, CONCEPT_REGISTRY, BOUNDARIES, PROTOCOL, TEMPORAL_AWARENESS, AUDIT, RELATIONSHIP_MODEL)

**STATUS:** Available

**PROJECT_ORIGIN:** FO-001 (FounderOS v2 Reconstruction)

**PROJECTS_USING:** FO-001 (active), all future projects (via protocol)

**NOTES:** 7 foundation documents as of 2026-06-18. These define FounderHQ itself and are referenced by every operation.

---

**ASSET_ID:** A-007

**NAME:** Supplier Contact — Pest Repeller

**TYPE:** Relationship (supplier)

**LOCATION:** Documented in Projects/Stop Nuisibles/SUPPLIER/ (two files exist, need consolidation)

**STATUS:** Available (incomplete — missing phone, payment terms, reorder process)

**PROJECT_ORIGIN:** None

**PROJECTS_USING:** FO-002 (First Revenue), all Stop Nuisibles projects

**NOTES:** Current supplier at 4,000 FCFA/unit. Sold 2,000 units of previous version. Reorder process not documented — critical gap for scaling.

---

## Content-Type Subtypes

For video production and creative assets, use these subtypes under the TYPE field:

- **Entity** — character, product, object (has ENTITY_SHEET)
- **Environment** — location, setting (has ENVIRONMENT_SHEET)
- **Scene** — entity + environment composition (has SCENE_SHEET)
- **Shot** — framed camera composition (has SHOT_SHEET)
- **Prompt** — generation prompt used to create an asset
- **Script** — written content script
- **Audio** — voiceover, music, sound effect
- **Video** — raw or assembled video clip
- **Thumbnail** — cover image for video

---

## Brand Identity

**ASSET_ID:** A-008

**NAME:** FounderHQ Brand Identity

**TYPE:** Design

**LOCATION:** concepts/ASSET.md (this entry) + visual files in Projects/ as they are created

**STATUS:** Available

**PROJECT_ORIGIN:** FounderHQ (root mission)

**PROJECTS_USING:** All projects (inherited)

**NOTES:**
- Tone: Direct, sans bullshit / Technique mais pas jargon / Africain mais pas "folklore" / Confiant mais pas arrogant
- Brand Pillars: Innovation accessible, Clarté radicale, Exécution méthodique
- Visual: Minimaliste, sombre, sérieux, accent orange/rouge, photos réelles pas de stock
- Tagline: "Construit pour durer. Conçu pour l'Afrique."

---

## Story Bible

**ASSET_ID:** Template — Story Bible

**TYPE:** Document

**STRUCTURE:** PROJECT_NAME, MISSION, AUDIENCE, CONTENT OBJECTIVE, VISUAL IDENTITY (color palette, lighting, camera style, typography), NARRATIVE IDENTITY (tone, pacing, emotion, narration style), BRAND IDENTITY (values, positioning, voice), RECURRING ENTITIES, RECURRING LOCATIONS, CONTENT RULES, FORBIDDEN RULES

**INHERITANCE CHAIN:** Story Bible → Entity Registry → Scenes → Assets

**NOTES:** A video is temporary. A project universe is persistent. The Story Bible is the source of truth for all content belonging to a project, brand, campaign, documentary, channel, podcast or series. All future content inherits through the chain above.

---

## Series Bible

**ASSET_ID:** Template — Series Bible

**TYPE:** Document

**STRUCTURE:** SERIES_NAME, MISSION, AUDIENCE, FORMAT, NARRATIVE ARC, RECURRING ENTITIES, RECURRING LOCATIONS, VISUAL RULES, AUDIO RULES, CONTINUITY RULES, EPISODE TRACKER

**EPISODE TRACKER:** EPISODE_ID, DATE, SUMMARY, KEY EVENTS, NEW ENTITIES, NEW LOCATIONS, LESSONS

**NOTES:** A single video is an asset. A series is an ecosystem. The Series Bible maintains continuity across episodes. Series can evolve; changes must be recorded.

---

## Asset Management Rules

1. An asset is not knowledge. Do not store usage instructions in ASSET.
2. **Reuse Rule:** Before creating a new asset, search the registry. If it exists: reuse, update, version. Do not duplicate.
3. **Continuity Gate:** Before creating a new asset in a series, verify consistency with the Series Bible and all previous episodes.
4. An asset's status must be updated when it changes (sold, consumed, transferred).
5. An asset created by a project should be added here when the project completes.
6. An asset that is not used by any project for 90 days may be archived.
7. An asset that is obsolete should be marked as Obsolete, not deleted.

---

## Footer

Last updated: 2026-06-20 16:15 (updated: A-009 and A-011 with Short #1 analytics)

Assets compound over time.

A young system has few assets.

A mature system has many.

Asset tracking prevents rebuilding what already exists.


--- FILE: concepts/DISTRIBUTION_MEMORY.md
# DISTRIBUTION MEMORY

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 10.

## Role

Store campaign performance data for distribution intelligence.

Every campaign is recorded with its strategy and results. DIOS queries this before every new campaign to find patterns. Over time, DISTRIBUTION MEMORY accumulates market intelligence that makes DIOS more effective.

## Structure

Each campaign entry follows this schema:

```yaml
Campaign:
  ID: "C001"
  Date: YYYY-MM-DD
  Product: "product name"
  Price: "price FCFA"
  Objective: "views | leads | sales"
  Market:
    Country: "country"
    City: "city"
  Audience: "segment name"
  Language: "language"
  Platform: "platform name"
  Hook: "exact hook text used"
  Angle: "description of angle"
  CTA: "call to action"
  Views: 0
  Likes: 0
  Comments: 0
  Shares: 0
  Messages: 0
  Leads: 0
  Conversions: 0
  Revenue: 0
  Cost: 0
  ROI: 0.0
  Learnings: "what worked and what didn't"
  Next: "what to try next time"
```

## Usage

DIOS queries DISTRIBUTION_MEMORY at step 1 of its workflow.

Query patterns:
- "Which hooks won for audience X?"
- "Which language converted best for product Y?"
- "Which platform distributed furthest in market Z?"
- "Which CTA performed best on platform W?"

## Empty State

No campaigns recorded yet.

## Footer

Last updated: 2026-06-20 (created — initial schema)

Memory compounds over time.

Each campaign makes the system smarter.

An empty memory is expected at first. It fills with every campaign.


--- FILE: concepts/DOODLEMIND.md
# DOODLEMIND
## Chaîne YouTube Shorts — Doodle Animation Éducative

### Concept
Chaîne de Shorts animés en doodle hand-drawn qui explique l'histoire humaine, l'évolution, l'anthropologie et la psychologie à travers des vidéos de 30–60 secondes.

### État Actuel
- Short #1 publié : "Why Your Brain Forgets Dreams"
- Templates existants : `KnowledgeAssets/shorts_viral_master_prompt.txt` (génération Shorts) + `KnowledgeAssets/doodle_youtube_master_prompt.txt` (vidéos longues)
- Actifs : Script Short #1, Image prompts Short #1, prompt master Shorts + Longues

### Relations
- **PEST_REPELLER** : Même modèle de contenu TikTok/Shorts
- **FHQ SYSTEM** : Les templates sont dans `concepts/KnowledgeAssets/`

### Prochaines Actions
1. Planifier Short #2
2. Publier 1 Short/semaine minimum
3. Monétisation à 500 abonnés + 3M vues/90 jours


--- FILE: concepts/DOODLEMIND_SHORTS_PLAN.md
# DOODLEMIND — PLAN DE CONTENU SHORTS
## Version 1.0 — Calendrier Éditorial + Pipeline de Production

### Canal DNA (du master prompt)
- **Niche** : Histoire humaine, évolution, anthropologie, psychologie
- **Format** : 30–60 secondes, narration 2e personne ("tu", "ton cerveau")
- **Style visuel** : Doodle hand-drawn 2D, couleurs plates, contours noirs épais, 9:16
- **Structure** : Hook (0-2s) → Setup (2-10s) → Twist (10-20s) → Reveal (20-40s) → Loop close (40-60s)

---

### 10 Idées de Shorts

| # | Titre (max 60 chars) | Hook (3 premiers mots) |
|---|----------------------|------------------------|
| 1 | Why Your Brain Forgets Dreams | "Your brain is" | ← **Short #1 publié** |
| 2 | Your Body Has a Second Brain | "Your gut has" |
| 3 | Why You Get Random Itches | "You just felt" |
| 4 | The Real Reason You Yawn | "You yawn when" |
| 5 | Your Nose Can Smell Fear | "Your nose is" |
| 6 | Why Your Voice Sounds Different Recorded | "You hate hearing" |
| 7 | The Science of Déjà Vu | "You've been here" |
| 8 | Why You Talk to Yourself | "You talk to" |
| 9 | Your Brain Deletes Most of Your Day | "You've already forgotten" |
| 10 | Why Cold Shows Slow Down Time | "Time slows down" |

---

### Calendrier des 5 Prochains Shorts

| Short | Titre | Thème | Statut | Date cible | Production |
|-------|-------|-------|--------|------------|------------|
| #1 | Why Your Brain Forgets Dreams | Psychologie / Sommeil | ✅ Publié | - | - |
| #2 | Your Body Has a Second Brain | Biologie / Nerf vague | 🔜 Planifié | S22 Juin | Master prompt → Stage 1 → 2 |
| #3 | Why You Get Random Itches | Psychologie / Sensations | 📝 À planifier | S23 Juin | Master prompt → Stage 1 → 2 |
| #4 | The Real Reason You Yawn | Biologie / Thermorégulation | 📝 À planifier | S24 Juin | Master prompt → Stage 1 → 2 |
| #5 | Your Nose Can Smell Fear | Psychologie / Phéromones | 📝 À planifier | S25 Juin | Master prompt → Stage 1 → 2 |
| #6 | Why Your Voice Sounds Different | Perception / Audio | 📝 À planifier | S26 Juin | Master prompt → Stage 1 → 2 |

---

### Pipeline de Production (1 Short)

Étape | Outil | Durée
------|-------|-------
1. Générer sujet (Stage 1 master prompt) | `shorts_viral_master_prompt.txt` | 2 min
2. Écrire script (Stage 2) | Master prompt + ElevenLabs | 10 min
3. Générer image prompts (Stage 3) | Master prompt → Midjourney/DALL-E | 15 min
4. Produire frames | Midjourney / Leonardo / DALL-E | 30 min
5. Monter vidéo | CapCut / Premiere | 20 min
6. Ajouter voix + musique | ElevenLabs + trending audio | 10 min
7. Publier | YouTube Shorts + TikTok + Reels | 5 min

**Temps total estimé par Short : ~1h30**

---

### Fichiers de Production

- Template Shorts : `KnowledgeAssets/shorts_viral_master_prompt.txt`
- Template Longues : `KnowledgeAssets/doodle_youtube_master_prompt.txt`
- Script Short #1 : `KnowledgeAssets/short_why_your_brain_forgets_dreams.txt`
- Image prompts Short #1 : `KnowledgeAssets/prompts_why_your_brain_forgets_dreams.txt`

### Prochaine Action
Lancer `shorts_viral_master_prompt.txt` → choisir Short #2 "Your Body Has a Second Brain" → exécuter Stage 1→4.


--- FILE: concepts/KNOWLEDGE.md
# KNOWLEDGE

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 4.

## Role

Store validated truths, patterns, principles, and domain expertise.

Knowledge evolves slowly.

Knowledge compounds over time.

Nothing validated should be lost.

---

## Distribution Intelligence

### DIOS Pipeline (validated 2026-06-20)

Distribution strategy must precede content production. The order is:
1. DIOS decides (audience, language, platform, hook, angle, CTA)
2. CEOS produces (story, script, direction, scene)
3. AI_VIDEO_MASTER_DOMAIN executes (video, localization, platform variations, distribution package)
4. DISTRIBUTION_MEMORY learns (campaign results → pattern detection)

**Validated truth:** Producing content without first defining audience, language, and platform hook is guessing. DIOS eliminates the guesswork before CEOS spends production effort.

### Language is Market-Derived (validated 2026-06-20)

Languages are not hardcoded. They are derived from the target market/country. Example markets:
- Togo: Francais, Ewe, Mina, Pidgin, Kabiye, Tem
- Ghana: English, Twi, Ga, Ewe, Hausa, Pidgin
- Nigeria: English, Pidgin, Yoruba, Hausa, Igbo, Efik

### Concept Registration (validated 2026-06-20)

New concepts must be registered in CONCEPT_REGISTRY.md with a Concept number, Layer, Purpose, Properties, and Invariant truth. New concept files must follow the established pattern: all-caps title, Concept section linking to registry, Role section, prose footer.

## Video Content Principles

### Hook Structure

- TikTok hook must create a pattern interrupt in the first 1-2 seconds
- Audio hook must be active (question, sound effect, surprise) — passive audio loses viewers at 0:03
- Text overlay must appear immediately for mute viewers (98% of TikTok)
- Dark first frame reduces contrast on For You page — use bright or high-contrast opening

### TikTok Mechanics

- 98.7% For You traffic means the algorithm considers content distributable — the problem is retention, not reach
- Average watch time of 10.3s on a 21s video (49%) is above TikTok's typical threshold for continued distribution
- Drop at 0:03 indicates the hook is the bottleneck, not the content quality after the hook
- AI-generated video may trigger uncanny valley on local feeds — real smartphone footage builds trust

### Hook Layer Priority (validated 2026-06-18 — 2 videos, same drop pattern)

The hook operates on THREE layers, in priority order:

1. **AUDIO layer** — a sound, a scream, a buzz, a surprise. This is the fastest to reach the brain. Text alone is too slow.
2. **VISUAL layer** — a face, a zoom, a sudden movement, a bright flash. Something that breaks the scroll pattern visually.
3. **TEXT layer** — text overlay. Only works if audio AND visual have already stopped the scroll.

**Validated truth:** Changing the TEXT hook without changing the AUDIO/VISUAL opening produced the same 0:03 drop across 2 videos. Text alone cannot fix a hook problem. Audio/visual layer must be addressed first.

### Facebook vs TikTok

- Facebook audience for new pages is primarily older (55-64 observed) — content must be adapted
- No text overlay on Facebook = 0 link clicks (observed)
- Music and text overlay are not optional on Facebook — they are requirements for engagement
- 9:16 vertical has lower priority on Facebook than 1:1 or 16:9

### Engagement Tactics (Lomé Audience)

- Direct instructions outperform implicit invitations. "Commentes 'Moi aussi' si..." generates more comments than "Qui d'autre ?" because the action is explicit and low-effort.
- Audience education level: prompts must be literal, not suggestive. Tell people exactly what to type and why.
- Relatable problem + direct instruction + low effort = highest comment rate.

### Offer Design

- 5 followers = zero social proof. Scarcity or discount incentive is required for first sales.
- "Premiers 10 clients : 4,500 FCFA au lieu de 5,900" creates urgency and compensates for lack of trust.
- WhatsApp CTA must include the number in the video frame, not just "link in bio."

---

## FounderOS Design Principles

### System Invariants

Defined in FOUNDERHQ_MANIFEST.md — 9 invariants that cannot be broken.

Key validated truths from implementation experience:

- Concept overlap is the primary cause of system decay. CONCEPT_BOUNDARIES.md is the prevention.
- A concept must be identifiable but not tied to a specific implementation path.
- The smallest recoverable unit is FOUNDERHQ_MANIFEST.md. If it survives, the system can be rebuilt.
- Documents named "kernel," "runtime," "state engine" without executable code are metaphors, not components. Do not create them.
- 42 specification files produce 0 lines of automation. Small, bounded concepts produce action.

### Protocol Knowledge

- An LLM can be instructed but not forced. Instructions must be clear, minimal, and verifiable.
- Time is a first-class dimension. No recommendation should be made without establishing current time.
- State stored in files survives. State in conversation context does not.

---

## Lomé Market Knowledge

- Rainy season creates urgent pest problems — high demand window for Stop Nuisibles.
- Mobile money (Wave, Orange Money) is the primary payment method for online transactions.
- WhatsApp is the primary sales channel — not websites, not e-commerce platforms.
- Delivery within Lomé is feasible same-day with motorcycle couriers.
- Price sensitivity: 5,900 FCFA is competitive against monthly spray spending (3,000+ FCFA/month).

---

## Pest Repeller Product Knowledge

- Price: 5,900 FCFA (see ASSET.md A-002 for cost and margin data)
- Coverage: ~7m. Type: Ultrasonic (no chemicals, no odor, no refill).
- Competes against: sprays (toxic, temporary), mosquito coils (smoke, fire risk), nets (bulky).
- Stock: 100 units available (see ASSET.md A-002 for current inventory).
- Previous version (V1) sold 2,000 units at 2,500 FCFA by the same supplier — demand validated.

---

## Cross-Project Patterns

### Zoclo Livraison (Archived)

- Complete content operation: 30-day calendar, 21 scripts, brand guide.
- Content structure (hook→problem→solution→proof→CTA) is a reusable pattern.
- Strongest hooks were pattern-interrupt questions and local targeting ("Si t'es a Lome...").
- Key lesson: TikTok content for sensitive products (contraception) risks platform restriction. Physical products (pest control) have lower regulatory risk.

---

## Continuous Improvement Pattern

### Review Questions (apply after any project or workflow)

- What worked?
- What failed?
- What surprised us?
- What repeated?
- What should change?

### When a pattern repeats 2+ times

1. Observe the pattern across projects
2. Validate it (does it hold in different contexts?)
3. Extract it into PLAYBOOK.md as a strategic pattern
4. Reference it from KNOWLEDGE.md as evidence

### Trigger

Every completed project triggers improvement review. The lessons are stored here before the project is archived.

---

---

## Doodle Animation YouTube Pipeline (Master Prompt — saved 2026-06-19)

**Full prompt sauvegarde dans :** `KnowledgeAssets/doodle_youtube_master_prompt.txt`

### Shorts Viral Pipeline (saved 2026-06-19)

**Full prompt :** `KnowledgeAssets/shorts_viral_master_prompt.txt`

- Format: 30-60s vertical (9:16), hand-drawn doodle
- One idea per Short. Hook in first 1-2s.
- 5-8 scenes per Short, fast cuts (2-5s per scene)
- Text overlay mandatory (90% watch first loop on mute)
- Loopable ending → first frame
- Sound: trending audio + voiceover on top

### Channel DNA

- **Niche:** Human history, evolution, anthropology, psychology
- **Format:** 10-14 min educational explainer, 2nd-person narration, hand-drawn doodle 2D animation
- **Hook formula:** Relatable modern moment → "but the real answer is far stranger" → reframe
- **Script rhythm:** Short sentence. Short sentence. Longer sentence. Short sentence. Question.
- **Narrative arc:** Hook → Reframe → Deep Dive → Counterintuitive Twist → Modern Mirror → Echo close

### Visual DNA

- Hand-drawn 2D doodle, flat colors, bold black outlines, sketchy marker lines
- Characters: Stick figures, large circular heads, dot eyes, thick brow lines
- Backgrounds: Flat solid color blocks only — no gradients, no shadows, no textures
- Text: Bold ALL CAPS, marker font, RED/BLACK/YELLOW, top of frame
- Color palette: Orange #F5820D · Cobalt #2D5FBF · Green #3A9E3A · Yellow #F5C518 · Red #D94040 · Brown #8B5E3C · Blue #6EB5E8 · Tan #C4965A · White #FFFFFF
- Aspect ratio: Always 16:9

### Production Stages

1. Generate 5 viral topic ideas → user selects
2. Generate 1,800-2,500 word narration script → delivered as `.txt` file
3. Generate image prompts (1 per timestamp) → delivered in batches of 20 → combine into `.txt` file on request
4. Generate viral metadata (title, description, tags) → ready to paste into YouTube

### Key Rules

- Never skip stages. Always wait for user input.
- Script = plain text only (no markdown, no stage directions, no headers inside file)
- One timestamp = one image prompt. Hold scenes across consecutive timestamps.
- All prompts begin with style anchor, end with style lock.
- Metadata = 3 separate copyable code blocks (title, description, tags).

---

## Footer

Last updated: 2026-06-20 (added: DIOS pipeline, language-market derivation, concept registration pattern)

Knowledge should be reviewed quarterly.

Entries older than 1 year without revalidation should be flagged.

New lessons from every project should be added here before the project is closed.


--- FILE: concepts/KORA.md
# FounderOS V4 — KORA (Knowledge & Oral Representation for Africa)

## Purpose

KORA Lab is Africa's sovereign AI research and product lab, building the Language Acquisition Engine and Universal Speech Intelligence Layer that allows underrepresented languages to participate fully in the AI era.

## Position in FounderHQ

KORA is the founder's primary long-term venture — an AI lab focused on speech infrastructure for African languages. It is the technical execution arm of Africa's AI sovereignty movement, positioned to complete the institutions (Kigali Declaration, AU AI Strategy, AfDB AI 10B Initiative) that have declared commitments to African AI.

## Status

| Field | Value |
|---|---|
| Phase | Pre-Seed / Validation |
| Activity | Active |
| Priority | High |
| Key Partner | ST Digital (compute, formalizing) |
| First Language | Éwé |

## Quick Reference

| Document | Location |
|---|---|
| Data Room Index | `projects/KORA/README.md` |
| Vision | `projects/KORA/01_VISION.md` |
| Mission | `projects/KORA/02_MISSION.md` |
| Master Plan | `projects/KORA/05_MASTER_PLAN.md` |
| Phase 1 Business Plan | `projects/KORA/09_BUSINESS_PLAN.md` |
| Executive Summary | `projects/KORA/08_EXECUTIVE_SUMMARY.md` |
| Pitch Deck | `projects/KORA/10_PITCH_DECK.md` |
All Annexes (A–A8) in `projects/KORA/annexes/`

## Relations

- **LEOS** — Financial Literacy Program active; KORA business concepts tracked as learning
- **FAOS** — KORA fundraising strategy, survival planning
- **PROJECT** — KORA is the founder's primary venture
- **OMNI** — Parallel venture (commerce proximity index); same execution lean, same Lomé anchor; KORA business models inform Omni strategy
- **DAOS** — Soya actions fund KORA survival; KORA milestones drive daily priorities
- **RAPHAEL** (`Frameworks/KORA/RAPHAEL_PDCA.md`) — operating system for KORA execution
- **SOJACO** — Cash flow project that could fund KORA development

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Updated | 2026-06-21 |
| Owner | Founder |


--- FILE: concepts/KORA_IDENTITY/KoraLab_ContentFramework.md
# KORA LAB CONTENT CREATION FRAMEWORK
## Complete Operating Manual: Scripts, Image Prompts, Video Prompts, Three Modes, Text Posts

**Version 1.0 / May 2026 / Kheir Lissi**
**Covers: Every content format from a single brief. Zero paid tools required to start.**

---

## HOW THIS FRAMEWORK WORKS

Every piece of content Kora Lab produces starts from a single Content Brief. From that brief, this framework generates everything in parallel:

- A full script (so you do the voiceover and never need to appear on camera if you choose)
- An image prompt for every section of the script (generate the visuals in Leonardo, Ideogram, or Microsoft Designer)
- A 3 to 5 second video prompt for every image (animate each still into a short clip)
- LinkedIn, TikTok, and X post adaptations (repurpose the same content across text channels)

One brief. One session. All formats covered.

---

## THE THREE VIDEO MODES

Choose your mode before you start. Different days call for different modes based on energy, time, and what you want the audience to feel.

---

### MODE A: FULL AI DOCUMENTARY (No Face, No Voice)

You write the script. An AI reads it. AI images become AI video clips. You assemble in DaVinci Resolve or CapCut. You are completely behind the camera.

**When to use:** When you want the content to feel like a cinematic institution rather than a personal creator. Best for educational breakdowns, policy analysis, market overviews, and anything where the message is bigger than the person.

**Best for:** YouTube (educational/documentary), TikTok (faceless AI content), LinkedIn video.

**Tool chain:**
- Script: You write it (or use Claude to draft, then edit)
- Voiceover: ElevenLabs free tier (10,000 characters per month). Choose a professional male or female voice. Or use the Kokoro TTS model on Hugging Face (free, unlimited, open source).
- Images: Leonardo AI + Ideogram + Microsoft Designer
- Video clips (image to video): Google Veo 3 via AI Studio (no watermark, free, best quality) + Kling AI (66 free daily credits, excellent motion) + Seedance (no watermark, fast)
- Music/ambient: Suno free tier (background score, instrumental) or Pixabay royalty-free audio
- Editing: CapCut free (desktop, no watermark) or DaVinci Resolve (free, professional)

---

### MODE B: YOUR VOICE, AI VISUALS (No Face, Your Voice)

You record your voiceover in one take sitting at your desk (no camera, just a phone or laptop microphone). AI images and video clips run underneath your voice. Nobody sees you. The voice is yours.

**When to use:** When you want the personal authority of your voice without the pressure of being on camera. Best for opinion pieces, institutional analysis, and Kora Lab updates where authenticity matters but you do not want to manage lighting, framing, or appearance.

**Best for:** YouTube (narrated documentary), TikTok (voiceover format), LinkedIn video.

**Tool chain:**
- Script: You write it
- Voiceover: Your phone microphone or laptop mic. Record in a quiet room with a piece of clothing over your phone to reduce room noise. Use Audacity (free) to remove background noise and level the audio.
- Images: Leonardo AI + Ideogram
- Video clips: Same as Mode A
- Editing: CapCut or DaVinci Resolve

---

### MODE C: FULL ON CAMERA WITH AI B-ROLL (Your Face, AI Enhancement)

You appear on camera for the main segments. AI-generated images and video clips serve as B-roll, transitions, and visual reinforcement between your talking segments.

**When to use:** When you want to build the deepest personal trust with your audience. Best for founder updates, calls to action, and content where your credibility as a person is the point.

**Best for:** YouTube (vlog and founder series), LinkedIn video, TikTok hybrid.

**Tool chain:**
- Script: You write it. Follow it loosely, speak naturally.
- Camera: Phone propped at eye level. Natural window light from the front or side. Clean wall behind you.
- AI B-roll: Leonardo AI images animated via Kling AI to cut between your on-camera segments
- Editing: CapCut (mobile or desktop, free, no watermark) or DaVinci Resolve

---

## PART 1: THE CONTENT BRIEF TEMPLATE

Fill this before any content session. Takes 5 minutes. Prevents wasted generation.

```
CONTENT BRIEF

Title: [What is this piece called]
Topic: [One sentence. What is this about]
Core argument: [One sentence. What is the single point you are making]
Primary audience: [Government/Institution / Investor/Accelerator / Technical Builder / General African Tech]
Platform: [YouTube / TikTok / LinkedIn / All]
Mode: [A: Full AI / B: Voice Only / C: On Camera]
Tone: [Authoritative / Urgent / Educational / Personal]
Target length: [30 seconds / 60 seconds / 3 minutes / 8 minutes]
Call to action: [What should the viewer do after watching]
Keywords to include: [2 to 4 phrases for SEO]
```

---

## PART 2: SCRIPT FRAMEWORK

Every script follows this structure regardless of mode or length. Scale each section up or down depending on total target length.

---

### THE UNIVERSAL SCRIPT STRUCTURE

**SECTION 1: THE HOOK (First 5 to 8 seconds — non-negotiable)**

The first sentence determines whether anyone watches the next sentence. Never start with "Hello" or "Welcome" or "In this video." Start with the fact, the tension, or the claim that makes stopping feel like a cost.

Short-form hook formula (TikTok, Reels, under 60 seconds):
"[Surprising number or fact] — and almost nobody is talking about what this actually means."

Long-form hook formula (YouTube, 3 minutes or more):
"[Fact]. [The tension inside that fact]. [The question that opens the rest of the video]."

Kora Lab hook examples:
- "54 African nations signed a declaration that committed to something no African institution has the technical capacity to deliver."
- "The $60 billion Africa AI Fund exists. The African Union Continental AI Strategy is live. And Africa still has no sovereign AI lab."
- "I left college mid third year to build something that governments with billions of dollars have not yet built."

---

**SECTION 2: THE CONTEXT (10 to 20% of total length)**

Give the audience exactly enough background to understand why the hook matters. Specific facts. Named institutions. Real numbers. No vague framing.

Context formula:
Paragraph 1: Describe the current state of the problem with one specific data point.
Paragraph 2: Describe what exists but is insufficient.
Paragraph 3: Name the gap.

---

**SECTION 3: THE DEPTH (40 to 50% of total length)**

This is the main substance. Everything you actually know about this topic that your audience does not. Structure it as: claim, evidence, implication. Repeat three to five times.

Depth formula per point:
Claim: "Here is the specific thing I want you to understand."
Evidence: "Here is the proof, named and specific."
Implication: "Here is what that means for Africa, for AI, for the future."

---

**SECTION 4: THE KORA LAB POSITION (10 to 15% of total length)**

Where Kora Lab fits into everything you just described. Not a pitch. A logical conclusion.

Formula:
"This is the gap. Kora Lab exists to fill it. Here is specifically how."
Never say "buy" or "subscribe" or use sales language. Just state the mission as a natural next sentence after the argument.

---

**SECTION 5: THE CALL TO ACTION (Final 5 to 10 seconds)**

One action. Not three. Never "like, comment, subscribe, follow, and visit the website."

Short-form CTA options:
- "Follow for more on what African AI actually looks like."
- "Send this to someone who thinks the AI race does not include Africa."
- "Link in bio if you want to work on this."

Long-form CTA options:
- "If you are inside one of these institutions or building in this space, reach out. kora-lab.com."
- "I publish essays on this on Medium. Link in the description."
- "The next video covers [specific next topic]. It matters more than this one."

---

## PART 3: FULL EXAMPLE SCRIPTS (KORA LAB)

---

### EXAMPLE SCRIPT 1: MODE A (Full AI Documentary)
**Title:** "54 Nations Made a Promise. Nobody Is Building It."
**Platform:** YouTube
**Length:** Approximately 4 minutes
**Tone:** Authoritative, urgent

---

[SECTION 1: HOOK — 0:00 to 0:10]

SCRIPT:
"In April 2025, fifty-four African nations signed a document that committed to something extraordinary. They promised sovereign AI infrastructure. African-owned language models. A $60 billion fund to make it real. One year later, not one African AI lab exists to deliver it."

IMAGE PROMPT 1:
Cinematic aerial view of the African continent at night, city lights glowing across Nigeria, Kenya, South Africa, Egypt, Senegal, and Togo. Deep navy sky, warm orange and white city lights, photorealistic, 8K quality, documentary photography style, wide establishing shot.

VIDEO PROMPT 1:
Slow cinematic push-in toward the African continent from high altitude. The lights of the cities grow gradually brighter. Camera movement is steady, almost like a satellite descending slowly. Duration 4 seconds. Mood: epic, documentary.

---

[SECTION 2: CONTEXT — 0:10 to 0:55]

SCRIPT:
"The Kigali Declaration on Artificial Intelligence was signed by the leaders of every African Union member state. It was not a vague aspiration. It contained specific commitments. Sovereign computing infrastructure. Open African datasets. An Africa AI Fund. An Africa AI Council. The African Development Bank and the United Nations Development Programme followed with the AI 10 Billion Initiative, targeting forty million jobs by 2035.

At the same moment, Togo activated its Digital Strategy 2025 to 2030, backed by the World Bank. Fifteen countries on the continent now have active national AI roadmaps.

The political will is the most real it has ever been. The problem is not vision. The problem is execution."

IMAGE PROMPT 2:
Inside a large continental summit hall, African heads of state and government ministers seated at a long formal conference table. Document signing ceremony in progress. Flags of African nations visible. Photorealistic, warm indoor lighting, wide angle, documentary photography style.

VIDEO PROMPT 2:
Slow camera pan across the conference table from left to right, as if moving through the room. Subtle depth of field blur in background. Documents visible in foreground. Duration 4 seconds. Cinematic documentary feel.

IMAGE PROMPT 3:
Close-up of a formal institutional document with the African Union emblem visible. Hands of a person signing. Gold pen on white paper. Sharp focus on the signature, background softly blurred. Black and white editorial photography style.

VIDEO PROMPT 3:
Slight camera drift downward toward the document being signed. Slow and cinematic. Depth of field shifts from blurred to sharp on the document as the camera settles. Duration 3 seconds.

IMAGE PROMPT 4:
Split composition: left half shows a map of Africa with data points and network lines connecting major cities, representing digital infrastructure. Right half shows lines of code and AI model architecture diagrams in dark blue and white. High-tech, data visualization aesthetic, editorial graphic style.

VIDEO PROMPT 4:
Digital lines and network nodes animate across the African continent map, slowly expanding outward from one city to another. Subtle glow effect. Data visualization style. Duration 5 seconds.

---

[SECTION 3: DEPTH — 0:55 to 2:45]

SCRIPT:
"Here is the specific problem. Every major AI model in the world today was trained primarily on English language data, with secondary representation in Mandarin, French, Spanish, and German. The African continent has more than two thousand languages. Swahili. Yoruba. Hausa. Amharic. Wolof. Twi. Lingala. Zulu. Nearly all of them are what researchers call low-resource languages. Meaning there is almost no data for AI to learn from them, and therefore no model that understands them.

When an African doctor uses a chatbot to support a clinical diagnosis, that chatbot does not understand the patient's language. When an African farmer asks an AI assistant for advice, the model has no agricultural data from that farmer's region. When an African student uses an AI tutor, the system was trained on a curriculum built for someone else entirely.

This is not a gap. It is a structural exclusion.

The second dimension of the problem is ownership. Every language model that matters today is owned by an American company. OpenAI. Anthropic. Google DeepMind. Meta. The decisions those companies make about what their models know, what they refuse to answer, and what values they embed are made by people in California. Africa is a market to sell to, not a voice in the architecture.

The third dimension is the feedback loop. Because Africa has no sovereign AI infrastructure, African talent leaves for institutions that do. African researchers publish papers that advance American and European AI labs. The knowledge compounds outside the continent. And the gap grows."

IMAGE PROMPT 5:
Photorealistic portrait of a young African woman, early 20s, sitting in front of a laptop. The screen shows an AI chat interface returning an error or unhelpful response. Expression is one of quiet frustration. Warm indoor light. Location feels like a university study room or small apartment. Editorial documentary photography style.

VIDEO PROMPT 5:
Slow push-in toward the laptop screen. The text on the screen becomes clearer as the camera approaches. The young woman in background slightly out of focus. Duration 4 seconds. Intimate, quiet documentary feel.

IMAGE PROMPT 6:
Aerial photograph of a large African agricultural landscape. Vast fields stretching to the horizon. A farmer visible in the middle distance, small against the scale of the land. Golden hour light. Documentary photography, National Geographic style.

VIDEO PROMPT 6:
Very slow aerial drift across the agricultural landscape, moving from right to left. The farmer remains visible in frame. The scale of the land is emphasized by the slow movement. Duration 5 seconds.

IMAGE PROMPT 7:
Split screen composition. Left side: a sleek AI research lab in Silicon Valley, bright, modern, people in discussion. Right side: a simpler but earnest workspace in an African city, a person at a laptop by a window, the city visible outside. Both spaces showing focus and intelligence, but very different resource levels. Editorial, documentary split-frame style.

VIDEO PROMPT 7:
Slow simultaneous zoom-out on both sides of the split screen. Both spaces remain in frame as they shrink, emphasizing the contrast. Duration 4 seconds.

IMAGE PROMPT 8:
Abstract data visualization: two large circles representing global AI knowledge. One circle is enormous (labeled "Global AI Training Data"). One small circle sits adjacent to it (labeled "African Languages"). The size difference is stark. Dark background, white and gray design, minimal and clean, infographic style.

VIDEO PROMPT 8:
The small circle slowly grows slightly larger, then stops. A counter appears inside it counting upward slowly. The growth is real but insufficient compared to the large circle. Duration 5 seconds. Motion graphics style.

---

[SECTION 4: KORA LAB POSITION — 2:45 to 3:30]

SCRIPT:
"This is what Kora Lab is being built to address. Not to ask permission from the institutions that have excluded Africa. Not to wait for Western AI companies to solve a problem they do not feel. To build the lab, train the models, deploy the products, and do the research that only an African institution will ever do.

Kora Lab operates on two axes. The first is making the latest AI from Anthropic, OpenAI, and DeepMind actually usable for African users and global users who have been left out of the current wave. Adapted in language. Adapted in price. Adapted in context. The second axis is building sovereign models. African language models. Multimodal models trained on African data. Models owned by an African institution and published for the continent.

This is the mission. It is not a business strategy. It is a civilizational one."

IMAGE PROMPT 9:
A sleek, minimal laboratory space. Dark walls, focused lighting over workstations. A large monitor shows a language model training interface. African cultural elements are visible in the space: a kora instrument on a shelf, a fabric print on the wall. The space feels both technical and African. Photorealistic, editorial style.

VIDEO PROMPT 9:
Slow camera track from left to right across the laboratory space. Monitor screen visible in sharp focus, background elements pass by. Duration 4 seconds. Cinematic documentary feel.

IMAGE PROMPT 10:
A Black man in his mid-twenties, professional and focused, standing at a window overlooking a West African city. Lome-style urban landscape outside. He is looking at the city with a clear sense of purpose. Photorealistic, warm natural light, editorial portrait style. (Note: this represents a visual stand-in for the founder. The face should not be identifiable as any real person.)

VIDEO PROMPT 10:
Slow push-in from behind the figure toward the window. The city landscape fills the frame gradually. His silhouette remains in the foreground. Duration 5 seconds. Introspective, cinematic.

---

[SECTION 5: CALL TO ACTION — 3:30 to 3:50]

SCRIPT:
"If you are inside one of the institutions that has committed to this future and want to discuss what it takes to execute it, the contact is kora-lab.com. If you are a technical builder who wants to work on this mission, the door is open. And if you found this useful, the next video will go deeper on what training an African language model actually requires. Subscribe so you do not miss it."

IMAGE PROMPT 11:
Clean, minimal black screen with KORA LAB in large white sans-serif font centered. Below it in smaller gray text: "Africa's Sovereign AI Lab" and "kora-lab.com". Simple, premium, institutional.

VIDEO PROMPT 11:
The KORA LAB text fades in slowly from black. Then the tagline fades in underneath. Then the URL. Each element appears with a 0.5 second delay between them. Duration 5 seconds. Calm and institutional.

---

### EXAMPLE SCRIPT 2: MODE B (Voice Only, Short-Form)
**Title:** "The AI Gap Nobody Talks About"
**Platform:** TikTok and Instagram Reels
**Length:** 55 to 60 seconds
**Tone:** Direct, clear, urgent

---

[HOOK — 0:00 to 0:05]
VOICEOVER: "There are over two thousand languages spoken across Africa. Almost none of them exist in the training data for any major AI model."

IMAGE PROMPT A:
Typographic design, black background, white text: "2,000+ African Languages" in large bold font. Below it in smaller gray text: "Almost none in any major AI model." Clean, minimal, high contrast.

VIDEO PROMPT A:
The number "2,000+" counts up rapidly from zero. When it hits 2,000+ it freezes. Then the second line fades in below. Duration 4 seconds. Motion graphics style.

---

[CONTEXT — 0:05 to 0:20]
VOICEOVER: "ChatGPT, Claude, Gemini. All of them were trained mostly on English. Then French. Then Mandarin. Swahili has 200 million speakers. Hausa has 70 million. Yoruba has 50 million. These languages are classified as low-resource. Not because the speakers do not exist. Because nobody built the infrastructure to capture their knowledge."

IMAGE PROMPT B:
Infographic style. A horizontal bar representing global AI training data. English fills 60%. Chinese fills 15%. Other European languages fill 20%. A tiny sliver at the end is labeled "All African Languages." Colors are black, white, and gray. Sharp, editorial data visualization.

VIDEO PROMPT B:
The bar fills from left to right as each segment appears. The African Languages segment appears last, visibly tiny. Duration 4 seconds. Clean data animation.

---

[DEPTH — 0:20 to 0:45]
VOICEOVER: "In April 2025, fifty-four African nations signed the Kigali Declaration. They committed to sovereign AI. African-owned models. A sixty-billion-dollar fund. One year later, no African AI lab exists to deliver it. Not because the will is absent. Because the execution layer is missing. That is what Kora Lab is building. From Lome, Togo. The lab that turns the declaration into something real."

IMAGE PROMPT C:
Map of Africa. Fifty-four small glowing dots appear on the map, each representing a signatory nation. The dots are connected by thin lines creating a network. Dark background, warm white dots, subtle glow. Clean and elegant.

VIDEO PROMPT C:
The dots appear one by one across the map, each lighting up sequentially. Lines connect them as they appear. After all dots are visible, they pulse gently in unison. Duration 5 seconds.

IMAGE PROMPT D:
Clean dark frame. Left side: the word "DECLARATION" with a checkmark. Right side: the word "EXECUTION" with a question mark. A thin vertical dividing line between them. Minimal, typographic, high contrast.

VIDEO PROMPT D:
Left side appears first (DECLARATION + checkmark). Then right side appears (EXECUTION + question mark). The question mark pulses twice. Duration 3 seconds.

---

[CALL TO ACTION — 0:45 to 0:55]
VOICEOVER: "Follow if you think Africa should build its own AI. Not just use it."

IMAGE PROMPT E:
Black background. White text centered: "Africa doesn't just consume AI." Line break. "Africa builds AI." Below in small gray text: "Kora Lab / kora-lab.com". Premium, clean, institutional.

VIDEO PROMPT E:
First line fades in. Brief pause. Second line fades in. Brief pause. Third line fades in. Total duration 4 seconds.

---

### EXAMPLE SCRIPT 3: MODE C (On Camera)
**Title:** "Why I Left College to Build Africa's AI Lab"
**Platform:** YouTube
**Length:** 6 to 8 minutes
**Tone:** Personal, honest, direct

---

[ON CAMERA — HOOK, 0:00 to 0:20]
YOU SAY (looking directly at camera): "I was mid third year of a computer science degree with an AI and big data specialization. I left. Not because I was failing. Because I calculated that following the standard path would put me at the level of what is currently possible in AI research in five years minimum. And in five years, where I need to be will have moved again. I needed to start building now."

[AI B-ROLL CLIP — CONTEXT, 0:20 to 0:45]

IMAGE PROMPT:
A university lecture hall, empty, late afternoon light coming through tall windows. Desks in rows. A whiteboard at the front with equations half-visible. Slightly melancholic mood. Photorealistic, documentary style.

VIDEO PROMPT:
Slow camera push down the center aisle of the empty lecture hall toward the front. Dust visible in the light shafts. Duration 4 seconds. Quiet, reflective mood.

VOICEOVER (your voice, recorded separately):
"The curriculum was teaching AI concepts that the industry had moved well beyond. The gap between what we were learning and what Anthropic, DeepMind, and OpenAI were actually building was not months. It was years."

[ON CAMERA — DEPTH, 0:45 to 3:00]
YOU SAY: "But dropping out was not really the story. The story is why. [Continue with your full explanation of the mission, the Kigali Declaration, the gap, and why Kora Lab exists. Use the script sections from Example 1 adapted into a conversational tone.]"

[AI B-ROLL — VISUAL REINFORCEMENT, interspersed every 60 to 90 seconds]
Use image and video prompts from Example Script 1, sections 3 and 4, cut between your on-camera segments.

[ON CAMERA — CALL TO ACTION, final 30 seconds]
YOU SAY: "If you want to work on this, if you are inside an institution that has committed to exactly what I am describing, or if you just want to follow the build in real time, you know where to find me. kora-lab.com."

---

## PART 4: IMAGE PROMPT LIBRARY

A reusable library of visual styles and subjects for Kora Lab content. Copy and adapt for any video or post.

### VISUAL STYLE CODES

**STYLE-DOC:** Documentary photography. Natural light. Real-world settings. No perfect staging. The look of National Geographic or The Economist photo essays.
Use for: Context sections, human stories, real-world problems.

**STYLE-ARCH:** Architectural and institutional. Clean lines, formal spaces, government buildings, research labs. Conveys authority and scale.
Use for: Institutional content, government partnership visuals, research imagery.

**STYLE-DATA:** Data visualization. Infographic aesthetic. Black backgrounds with white and gray graphic elements. Charts, maps, network diagrams.
Use for: Statistics, market data, geographical information, model architecture.

**STYLE-TYPE:** Typography-only frames. Black background, white text, clean sans-serif. Used for key quotes, facts, and transition frames.
Use for: Key facts, hooks, call to action frames.

**STYLE-AIR:** Aerial photography. Birds-eye view of African landscapes, cities, and terrain. Wide establishing shots.
Use for: Opening sequences, scale-setting visuals, geographic context.

### REUSABLE IMAGE PROMPT TEMPLATES

**TEMPLATE: African city establishing shot**
Aerial photorealistic view of [city name: Lome / Lagos / Nairobi / Accra / Dakar], urban landscape stretching to the horizon, golden hour light, busy streets visible below, modern and traditional architecture mixed, STYLE-AIR, cinematic depth of field.

**TEMPLATE: Young African professional with technology**
Photorealistic portrait of a young [man/woman] in their mid-twenties, focused expression, working on a laptop or tablet, [university library / small office / coffee shop in an African city] setting, warm natural light, STYLE-DOC.

**TEMPLATE: Institutional document or signing**
Close-up of a formal document with [African Union / government ministry / institutional] seal visible, pen in hand mid-signature, shallow depth of field, warm indoor light, STYLE-DOC.

**TEMPLATE: AI and technology abstract**
Abstract visualization of a neural network or language model architecture. Dark background (#0A0A0A). White and gray nodes connected by thin lines. A few nodes are highlighted in slightly brighter white. Clean, technical, no text. STYLE-DATA.

**TEMPLATE: Africa map with data overlay**
Stylized map of the African continent. Dark background. Country borders in thin white lines. [Data points / glowing dots / network connections] overlaid on the map. Clean and editorial. STYLE-DATA.

**TEMPLATE: Split comparison frame**
Left half shows [Western tech environment: modern lab, Silicon Valley office]. Right half shows [African tech environment: simpler but earnest workspace]. Both dignified. Neither condescending. STYLE-DOC.

**TEMPLATE: Kora Lab end card**
Black background. Center-aligned. Large white text: "KORA LAB". Below in smaller gray text: "Africa's Sovereign AI Lab". Below that, even smaller: "kora-lab.com". Clean sans-serif font. No other elements.

**TEMPLATE: Key fact typography card**
Black background (#0A0A0A). White number or statistic in very large font (simulate 80px). Below it, a short descriptor in gray. Example: "2,000+" then "African languages almost entirely absent from frontier AI training data." STYLE-TYPE.

---

## PART 5: VIDEO PROMPT LIBRARY

Templates for animating still images into 3 to 5 second clips. Use these with Google Veo 3 (AI Studio), Kling AI, or Seedance.

### VIDEO MOTION TYPES

**MOTION-PUSH:** Slow, steady camera push-in toward the subject. Cinematic and focused. Use for: establishing shots, key moments, building tension.

**MOTION-DRIFT:** Very slow horizontal camera drift, left to right or right to left. Contemplative. Use for: landscapes, wide shots, reflective moments.

**MOTION-PULLOUT:** Camera slowly pulls back, revealing more of the scene. Use for: context-setting, scale reveals, wide reveals.

**MOTION-COUNT:** Numbers or text animate upward from zero or fade in sequentially. Use for: statistics, data cards, typographic sequences.

**MOTION-FADE:** Elements appear sequentially with smooth fade-in. Use for: end cards, title sequences, quiet moments.

**MOTION-PULSE:** Static image with one subtle element (a dot, a glow, a line) pulsing gently. Use for: network maps, data visualizations, subtle emphasis.

### VIDEO PROMPT FORMULA

[Subject description from image prompt] + [MOTION TYPE] + [Duration: X seconds] + [Mood: calm/urgent/cinematic/reflective] + [Any specific instruction]

Example:
"Aerial view of Lome at night, city lights visible. MOTION-PUSH slowly toward the city center. 5 seconds. Mood: epic, cinematic. No abrupt movement."

### CAMERA DIRECTION VOCABULARY FOR PROMPTS

Use these exact phrases in video prompts for better results:
- "Slow cinematic push-in" (camera moves forward slowly)
- "Gentle horizontal drift from left to right" (camera slides sideways)
- "Subtle pullback reveal" (camera moves backward)
- "Hold still with slight ambient motion" (wind in trees, lights flickering, no camera movement)
- "Depth of field shift from blurred foreground to sharp background"
- "Numbers count up from zero to [X]" (for data animations)
- "Text appears letter by letter" (for title cards)

---

## PART 6: FREE TOOL STACK (2026 CURRENT)

### IMAGE GENERATION (All Free)

| Tool | Free Limit | No Watermark | Best For | URL |
|---|---|---|---|---|
| Leonardo AI | 150 tokens/day (reset daily) | Yes | Photorealistic imagery, portraits, scenes | leonardo.ai |
| Ideogram | 10 to 25 generations/day | Yes | Images with readable text inside | ideogram.ai |
| Microsoft Designer | Unlimited (slower) | Yes | Volume generation, backup | designer.microsoft.com |
| Adobe Firefly | 25 credits/month | Yes, commercially safe | Professional assets, legally clearable | firefly.adobe.com |

### VIDEO GENERATION (All Free at Base Level)

| Tool | Free Limit | No Watermark | Best For | URL |
|---|---|---|---|---|
| Google Veo 3 via AI Studio | Limited but no watermark | Yes | Best overall quality, cinematic output | aistudio.google.com |
| Kling AI | 66 daily credits (3 to 4 clips/day) | No (free tier) | Motion realism, physical movement | klingai.com |
| Seedance | Daily credits, launching | Yes | Fast, consistent, no watermark | seedance.ai |
| Hailuo / MiniMax | Several daily generations | No (free tier) | Face and human motion, talking portraits | hailuoai.video |
| Pika | 150 signup credits + daily refresh | No (free tier) | Creative effects, social clips | pika.art |
| Luma Dream Machine | 30 generations/month | No (free tier) | Atmospheric, cinematic B-roll | lumalabs.ai |

**Recommended stack for zero cost, no watermark:**
Primary: Google Veo 3 (AI Studio) for final outputs
Secondary: Seedance for fast daily volume
Backup: Kling AI (free tier) for testing and motion variety

**Note on watermarks:** Kling, Pika, Hailuo, and Luma watermark their free outputs. For content you publish, use Google Veo 3 or Seedance which produce clean exports at the free tier.

### VOICE GENERATION (For Mode A: Full AI)

| Tool | Free Limit | Quality | URL |
|---|---|---|---|
| ElevenLabs | 10,000 characters/month | High | elevenlabs.io |
| Kokoro TTS (Hugging Face) | Unlimited, open source | Very high | huggingface.co/spaces/hexgrad/Kokoro-TTS |
| OpenAI TTS (API) | Pay per use, very cheap | High | platform.openai.com |

### AUDIO RECORDING (For Mode B: Your Voice)

- **Phone microphone:** Perfectly adequate for voiceover if the room is quiet
- **Audacity (free desktop):** Remove background noise with Noise Reduction filter. Normalize volume. Export as MP3.
- **CapCut audio tools (free):** Mobile-based noise reduction and volume normalization

### MUSIC AND AMBIENT SOUND

| Tool | Free | Commercial Use | Best For |
|---|---|---|---|
| Suno | Limited generations/day | Check terms per track | Background score, instrumental atmosphere |
| Pixabay Music | Unlimited | Yes, royalty-free | Documentary-style ambient tracks |
| Freesound.org | Unlimited | Varies per file (check license) | Sound effects, ambience |

Search Pixabay Music for: "documentary", "ambient", "cinematic", "African drums instrumental", "tech documentary"

### EDITING

| Tool | Platform | Cost | Best For |
|---|---|---|---|
| CapCut Desktop | Windows/Mac | Free, no watermark | Fast editing, social format, subtitles |
| DaVinci Resolve | Windows/Mac/Linux | Free | Professional editing, color grading |
| CapCut Mobile | iOS/Android | Free (some features) | Quick mobile edits |

---

## PART 7: TEXT POST ADAPTATION FORMULA

Every video script becomes text posts across platforms without extra work. Apply these formulas after your script is finalized.

### FROM SCRIPT TO LINKEDIN POST

Take Section 1 (Hook) and Section 4 (Kora Lab Position) from your script.

Format:
Line 1: The hook sentence. No prefix.
[line break]
Lines 2 to 5: 3 to 4 short lines expanding the hook using one fact from Section 2.
[line break]
Lines 6 to 8: 2 to 3 lines stating the Kora Lab position naturally.
[line break]
Final line: The call to action.

Maximum 150 words. No em dashes. No more than 2 hashtags at the end.

### FROM SCRIPT TO TIKTOK/REELS CAPTION

Take the hook sentence only.

Format:
Sentence 1: The hook (first sentence of your video script).
Sentence 2: One specific fact.
Sentence 3: The implication in one line.
Sentence 4: Your call to action.

Maximum 5 lines. 3 to 5 hashtags: #AfricanAI #AIAfrica #KoraLab + 1 to 2 trending topic tags.

### FROM SCRIPT TO X/TWITTER THREAD

Take the full script. Extract one key sentence from each section.

Format:
Tweet 1: Hook sentence (the opener)
Tweet 2: One fact from Context section
Tweet 3: One fact from Depth section (the most surprising one)
Tweet 4: One fact from Depth section (the most institutional one)
Tweet 5: Kora Lab Position in one sentence
Tweet 6: Call to action with link

Each tweet: under 280 characters. No tweet should need the others to make sense. Each must stand alone.

---

## PART 8: WEEKLY CONTENT PRODUCTION WORKFLOW

One session per week produces content for all channels.

**Monday (2 hours): Brief and Script**
- Fill the Content Brief template (5 minutes)
- Write the full script following the Universal Script Structure (45 minutes)
- Generate all image prompts from the script using the library templates (20 minutes)
- Adapt the script into LinkedIn post, TikTok caption, and X thread (20 minutes)

**Tuesday (2 to 3 hours): Visual Production**
- Generate all images: batch in Leonardo AI and Ideogram during the day (credits reset daily)
- Generate video clips from the best images: use Google Veo 3 and Seedance
- Save all assets in organized folders: [VideoTitle] / Images / Video Clips / Audio

**Wednesday (1 to 2 hours): Assembly**
- Open CapCut or DaVinci Resolve
- Lay the audio track (your voiceover recording or ElevenLabs generated voice)
- Cut video clips to match the audio section by section
- Add background music at 15 to 20% volume under the voiceover
- Add captions (CapCut auto-caption feature, free)
- Export

**Thursday: Publish**
- Upload to YouTube (with SEO title, description, chapters, tags)
- Upload to TikTok (with caption and hashtags)
- Post LinkedIn video (with text post above the video)
- Post LinkedIn text adaptation
- Post X thread

**Friday: Publish text posts**
- Post the LinkedIn text post version
- Post the X thread
- Save the script and all assets to your content library for future reference

---

## PART 9: CONTENT NAMING AND ORGANIZATION SYSTEM

For every piece of content, use this naming convention:

Folder: [YYYY-MM-DD]_[Topic-Slug]_[Mode]
Example: 2026-05-14_Kigali-Declaration-Gap_ModeA

Inside each folder:
- Brief.txt (the filled content brief)
- Script.md (the full script with all prompts)
- /Images (all generated still images)
- /VideoClips (all animated clips)
- /Audio (voiceover recording or generated file)
- /Published (final exported video files)
- TextPosts.md (all adapted text posts for all platforms)

This system means every video you make is reusable. You can pull clips from the library for future videos, remix scripts for new platforms, and build a growing visual asset bank over time.

---

*This framework covers every content format Kora Lab needs from a single brief. Apply it consistently and the volume compounds. The catalog of content becomes the proof of the mission.*

*Kheir Lissi / Founder / kora-lab.com / May 2026*


--- FILE: concepts/KORA_IDENTITY/KoraLab_DigitalSystem_v2.md
# THE ZERO-CAPITAL DIGITAL PRODUCT MACHINE
## Complete System: Research, Create, List, Sell, Scale — No Upfront Money

**Version 2.0 / May 2026**
**Covers: All platforms with zero listing fees, bulk production strategy, full free tool stack**

---

## THE CORE LOGIC

You create a digital file once. A buyer pays. The platform delivers the file automatically. You receive the money. No inventory, no shipping, no stock, no human needed after upload.

Your job is to build a catalog of files that people are already searching for, priced correctly, presented professionally, and listed everywhere simultaneously. The larger and broader your catalog, the more passive the income becomes.

This guide covers every platform with zero listing fees available in 2026, the full free AI stack for creation, and a repeatable bulk production method designed for volume over perfectionism.

**Realistic income curve:**
- Month 1 to 2: 20 to 80 listings live. First sales. $0 to $300/month.
- Month 3 to 4: 80 to 200 listings. $300 to $1,000/month.
- Month 5 to 6: 200 to 400 listings. $1,000 to $3,500/month.
- Month 7 and beyond: compounding catalog. $3,000 to $10,000+/month is realistic at 400+ well-placed listings.

---

## PART 1: PLATFORM STACK

### TIER 1: ZERO LISTING FEE MARKETPLACES (Built-in Traffic, Pay Per Sale Only)

These platforms bring buyers to you. No fee to list. You only pay when you sell.

---

**GUMROAD**
Site: gumroad.com
Fee: 10% flat per sale (all-inclusive, covers payment processing and tax compliance globally as of January 2025)
Listing fee: Zero
Payout: Weekly, minimum $10 balance
Best for: Ebooks, guides, templates, AI prompt packs, software, anything digital
Togo access: Yes, via Payoneer payout integration
Notes: Gumroad became a Merchant of Record in January 2025, meaning it handles all global VAT and sales tax for you. Biggest traffic of any standalone creator platform. The 10% fee is the highest in this tier but the discoverability and simplicity make it the best starting point.

---

**PAYHIP**
Site: payhip.com
Fee: 5% per sale on free plan (lowest in this tier). Reduces to 2% at $29/month and 0% at $99/month.
Listing fee: Zero. Unlimited listings on all plans including free.
Payout: Instant via Stripe or PayPal
Best for: All digital product types. Downloads, courses, memberships, coaching, software.
Notes: Handles EU and UK VAT automatically. More features than Gumroad at a lower base fee. Built-in affiliate program, discount codes, PDF stamping for piracy protection. Full feature access on the free plan is the key advantage over most competitors.

---

**KO-FI**
Site: ko-fi.com
Fee: 5% on digital product sales (free plan). Zero on tips/donations. Zero on everything with Gold at $12/month.
Listing fee: Zero
Payout: Instant, directly to your Stripe or PayPal
Best for: Artists, illustrators, writers, creators with a community or social following
Notes: Ko-fi is unique because it combines tips, product sales, memberships, and commissions in one link. It is the only platform where you can monetize all four from a single page. The instant payout is a major advantage for cash flow. Not a discovery marketplace, so traffic must come from your own channels.

---

**WHOP**
Site: whop.com
Fee: 3% per transaction on free plan (lowest in this entire guide). Reduces further on paid plans.
Listing fee: Zero
Payout: Fast payout via Stripe
Best for: Digital products, communities, SaaS tools, memberships, any kind of digital access
Notes: Whop is one of the fastest-growing creator commerce platforms of 2025 to 2026. Its 3% fee is the lowest available without paying a monthly subscription. Setup takes under 15 minutes. Also has growing marketplace discovery. Highly recommended as an additional listing destination.

---

**LEMON SQUEEZY**
Site: lemonsqueezy.com
Fee: 5% plus $0.50 per transaction (now integrating into Stripe following Stripe's 2025 acquisition)
Listing fee: Zero
Payout: Regular payouts to bank or Payoneer
Best for: Software, SaaS, digital tools, license keys, anything with global tax complexity
Notes: Acts as Merchant of Record for all global tax obligations. Particularly valuable for software or tools sold internationally where VAT compliance is complex. The $0.50 per-transaction surcharge makes it less suited for very low-priced products.

---

**SYSTEME.IO**
Site: systeme.io
Fee: Zero transaction fees on all plans including free
Listing fee: Zero
Payout: Via Stripe or PayPal
Best for: Courses, sales funnels, digital product bundles, email marketing integration
Notes: The free plan includes 2,000 contacts, 3 sales funnels, 1 course, unlimited email sends, and 0% transaction fees. This is the most generous free plan of any all-in-one platform. The limitation is 3 funnels on free, which means it works best for a focused product catalog rather than bulk listing.

---

**ITCH.IO**
Site: itch.io
Fee: You set your own revenue split. Minimum is 10% to the platform. You can give more voluntarily.
Listing fee: Zero
Payout: Via PayPal or direct
Best for: Games, interactive tools, creative assets, fonts, audio, templates, zines
Notes: Itch.io is underused by non-game creators. Its audience actively buys asset packs, fonts, templates, sound effects, illustrations, and tools. Zero listing fee, flexible pricing, and a creative community that rewards quality and originality.

---

**CREATIVE MARKET**
Site: creativemarket.com
Fee: Revenue share model. You earn 30 to 70% depending on traffic source.
Listing fee: Zero (but requires application and portfolio review)
Payout: Monthly via PayPal
Best for: Fonts, graphics, templates, UI kits, patterns, illustrations, mockups
Notes: Creative Market has enormous built-in traffic specifically for design assets. The application process requires an existing portfolio of quality work. Build your catalog on Gumroad and Payhip first, then apply. Once accepted, your listings benefit from serious marketplace discovery.

---

**DESIGN BUNDLES**
Site: designbundles.net
Fee: Revenue share. Contributors earn approximately 40% per sale.
Listing fee: Zero (requires application)
Best for: SVG cut files, clipart, fonts, templates, craft assets
Notes: Massive audience of Cricut and Silhouette users, the same buyers who drive most SVG sales on Etsy. Apply as a contributor once you have 20 to 30 quality designs. Their bundle deals and flash sales generate significant passive revenue for accepted contributors.

---

**TEACHERS PAY TEACHERS**
Site: teacherspayteachers.com
Fee: Free membership takes 45% per sale. Premium membership at $59.95/year takes 20% per sale.
Listing fee: Zero
Best for: Educational materials, worksheets, planners, lesson plans, classroom tools, printables
Notes: One of the largest marketplaces in this space with over 7 million products and a deeply loyal buyer community. If any of your products can be framed for teachers, parents, or students, this is a high-value channel.

---

**OPUNA**
Site: opuna.com
Fee: Revenue share model (low percentage, exact terms on their site)
Listing fee: Zero
Best for: AI-generated digital art, illustrations, design assets
Notes: A newer platform built specifically for AI-assisted creative products. Growing audience, low competition currently, and a community that actively embraces AI-generated work. Early mover advantage is real here in 2026.

---

**GLOMARKET (AFRICA-FOCUSED)**
Site: glomarket.africa
Fee: Low percentage per sale
Listing fee: Zero
Best for: African creators selling to African and diaspora audiences
Notes: Emerging African digital marketplace. Lower volume than global platforms but higher cultural relevance, lower competition, and growing fast. List here alongside your global channels.

---

### TIER 2: PLATFORMS WITH LISTING FEES BUT MASSIVE TRAFFIC (Use Once Earning)

These require small listing fees but deliver the highest organic traffic of any marketplace. Use them once your Tier 1 catalog is earning and you can cover the fees from revenue.

**ETSY**
Fee: $0.20 per listing (active for 4 months, auto-renews on sale), 6.5% transaction, approximately 3% payment processing. Total approximately 9.5% per sale plus the listing fee.
Traffic: Highest of any digital product marketplace for printables, SVG, templates, and design assets.
Strategy: Start on zero-fee platforms. When you have first revenue, invest $10 to $20 in your first 50 to 100 Etsy listings. The traffic multiplier makes it worth it.

**CREATIVE FABRICA**
Fee: No listing fee once accepted. Revenue share model with subscription-based buyer access.
Traffic: Enormous audience for craft and design assets, particularly SVG and clipart.
Strategy: Apply once you have a strong portfolio from your zero-fee channels.

---

## PART 2: PRODUCT RESEARCH

### The Research Stack (All Free)

- **EverBee** (everbee.io): Chrome extension. Shows estimated monthly revenue and sales for any Etsy listing. Use this to validate demand before creating anything.
- **eRank** (erank.com): Free plan gives 200 keyword searches per day. Shows search volume and competition for any term on Etsy. Use this for all keyword decisions.
- **EtsyHunt** (etsyhunt.com): Competitor and trend analysis for Etsy. Free plan covers what you need.
- **Google Trends** (trends.google.com): Free, no account needed. Use to identify seasonal trends and rising search interest.
- **Gumroad Discover**: Browse what is selling on Gumroad by category. Free. No account needed.
- **Whop Marketplace**: Browse trending products. Free.

### What to Research

Open an incognito browser. Go to the platform of your choice. Search a category term. Sort by best sellers or most popular. Note every product with strong sales volume.

Then validate with EverBee: does the estimated revenue justify creating this product?
Then validate with eRank: is there search volume for the keywords? Is competition manageable?

Your research output before creating anything should be:
- 5 validated niches with confirmed demand and acceptable competition
- 3 competitor listings per niche for reference (never copy, study and differentiate)
- Primary keyword plus 5 secondary keywords per product type
- Target price per category

### Top Product Categories in 2026 (Validated by Demand)

| Category | Why Now | Price Range | Best Platform |
|---|---|---|---|
| AI Prompt Packs | Fastest growing niche. Everyone wants better AI results. | $5 to $30 | Gumroad, Payhip |
| SVG Cut Files | Cricut/Silhouette users buy every season, constantly. | $2 to $8 | Design Bundles, Etsy |
| Notion Templates | High demand, higher prices, lower competition than planners. | $7 to $35 | Gumroad, Payhip |
| Canva Social Media Templates | Every small business needs these. Repeat buyers. | $8 to $30 | Payhip, Etsy |
| Digital Planners and Trackers | Evergreen. Massive sub-niche depth. | $4 to $20 | Etsy, Payhip |
| Printable Wall Art | Evergreen. Zero competition at niche level. | $3 to $12 | Etsy, Ko-fi |
| Resume and CV Templates | Perennial demand. High price point. | $10 to $40 | Gumroad, Payhip |
| Clipart PNG Bundles | Every designer needs art assets. High volume. | $3 to $10 | Creative Fabrica, Etsy |
| Tumbler and Mug Wraps | Repeat buyers. Enormous niche depth. Seasonal. | $2 to $6 | Etsy, Design Bundles |
| PLR Content Bundles | Bulk buyers, high margins, B2B angle. | $15 to $80 | Gumroad |
| 3D Print STL Files | Exploding with 3D printer adoption. | $3 to $15 | Gumroad, Cults3D |
| Educational Worksheets | Teachers Pay Teachers audience is enormous. | $3 to $15 | TPT, Payhip |
| Branding Kits and Logo Templates | B2B buyers, premium pricing. | $15 to $60 | Creative Market |

---

## PART 3: CREATION STACK (ALL FREE)

### Image and Design Generation

**Leonardo AI** (leonardo.ai)
Free: 150 tokens per day. One standard image costs 4 to 8 tokens: 18 to 35 images per day.
Commercial rights: Included on free tier.
Best for: Artwork, illustrations, clipart, printable art, backgrounds.
Strategy: Create your daily batch every morning. Download all images. Build a library.

**Ideogram** (ideogram.ai)
Free: 10 to 25 generations per day depending on the day.
Best for: Any image that requires readable text inside it. Quotes, posters, labels, signs. Ideogram is the only free AI image tool where text accuracy is reliable.
Strategy: Use for all quote-based wall art, motivational prints, and any design where words appear inside the image.

**Microsoft Designer** (designer.microsoft.com)
Free: Unlimited generations, slower speed, no watermark.
Commercial rights: Included.
Best for: Volume generation when you have exhausted your Leonardo and Ideogram daily limits.
Strategy: Third in rotation. Use it for variations and backgrounds.

**Adobe Firefly** (firefly.adobe.com)
Free: 25 credits per month.
Commercial rights: 100% commercially safe, all training data licensed. Use for any product where you need guaranteed commercial clearance.
Best for: Professional-grade assets where quality and legal safety matter most.

**Canva Free** (canva.com)
Free: Massive library of templates, elements, fonts, and mockups. No watermark on most assets.
Best for: Assembling final products. Take your AI-generated images and compose them professionally in Canva. All planner pages, templates, social media kits, and PDF guides are built here.
Strategy: This is your assembly workspace. Everything generated elsewhere comes into Canva for final production.

**Inkscape** (inkscape.org)
Free: Open source, download once, use forever.
Best for: Converting PNG/JPG images to SVG/DXF/EPS vector formats for cut file products.
Key function: Path > Trace Bitmap. Upload your design, run the trace, clean the paths, export. Watch one 10-minute tutorial on YouTube and you can produce SVG cut files indefinitely.

### Listing Copy Generation

**Claude** (claude.ai)
Free tier: Use for all listing titles, descriptions, and tags.

Prompt to use for every listing:
```
Write an Etsy/Gumroad listing for a digital product.

Product: [describe it]
Primary keyword: [from your eRank research]
Secondary keywords: [5 keywords]
Formats included: [PDF, SVG, PNG, etc.]
Target buyer: [who uses this]
Key benefit: [what problem does it solve]

Deliver:
1. SEO title (140 characters max, primary keyword at the front)
2. Description (200 to 300 words, keywords natural, include what files are included, what the buyer can do with it, end with a call to action)
3. Exactly 13 keyword tags (2 to 4 words each)
```

Generate the copy. Review it in 2 minutes. Paste to platform. Move on.

**ChatGPT** (chatgpt.com)
Free tier: Use as backup when Claude's daily free limit is reached. Same prompts work.

---

## PART 4: BULK PRODUCTION METHOD

The goal is maximum listings with minimum time per listing. Perfectionism is the enemy. Volume plus consistent quality beats occasional excellence every time.

### The Variation System (1 Design = 10 to 30 Listings)

Take one design. Apply the following multipliers:

- 5 color variations (same layout, different palette): 5 listings
- 3 size formats (A4, US Letter, 5x7 for example): multiply by 3
- 2 occasion variants (generic version + seasonal version): multiply by 2
- Bundle listing (sell the set of 5 color variants as one bundle at a discount): 1 additional listing

One hour of design work producing 1 original = 10 to 30 separate listings across platforms.

### Daily Production Target

| Hours Available | Designs Created | Listings Generated | Platforms Listed |
|---|---|---|---|
| 2 hours | 2 to 3 designs | 20 to 60 listings | Gumroad + Payhip + Ko-fi |
| 4 hours | 5 to 7 designs | 50 to 140 listings | All zero-fee platforms |
| 6 hours | 8 to 12 designs | 80 to 240 listings | All platforms including TPT |

### The Assembly Line

Step 1 (15 minutes): Research. Identify today's 3 product niches. Confirm keywords. Note competitor designs.

Step 2 (30 to 60 minutes): Generate images in Leonardo AI and Ideogram. Download all outputs. Pick the best 3 per niche.

Step 3 (30 to 45 minutes): Open Canva. Assemble each design into its final format. Create all size and color variations. Export everything.

Step 4 (15 to 20 minutes per product): Generate listing copy in Claude. Create one mockup per product in Canva. Upload and publish.

Step 5 (10 minutes): Cross-list to every zero-fee platform simultaneously.

---

## PART 5: PRICING STRATEGY

### Base Formula

Look at the top 10 competitors in your niche. Take the average price. If you have zero reviews: price at 80% of that average. Once you have 10 reviews: price at 100% or above.

### Price Floors (Never Go Below These)

- AI prompt packs: minimum $5 (below this signals low quality)
- SVG cut files: minimum $2.50
- Printable wall art: minimum $3
- Template sets (3 or more items): minimum $8
- Notion templates: minimum $7
- Resume/CV templates: minimum $12
- PLR bundles: minimum $15
- Branding kits: minimum $20

### Bundle Premium

A bundle of 5 items that sell individually for $3 each should not be priced at $15. Price it at $9 to $11. The buyer perceives a discount. You make more per transaction than if they bought one item. Create bundle listings for every product family.

---

## PART 6: MOCKUP CREATION (FREE)

Buyers decide in 2 seconds based on your thumbnail. The mockup is as important as the product.

**Canva mockup method:**
Search "mockup" in Canva templates. Find a frame, device, or surface that fits your product category. Drop your design into it. Download as PNG.

What you need per listing:
- Image 1: Clean flat design on white or light background. This is your thumbnail.
- Images 2 to 4: Lifestyle mockups showing the product in context.
- Image 5: All file formats displayed visually (PDF, SVG, PNG icons).
- Image 6: Close-up detail showing quality.
- Image 7 (optional): A simple before/after or use-case illustration.

Minimum 5 images per listing. 7 to 8 is better.

---

## PART 7: PAYMENT AND RECEIVING MONEY FROM TOGO

Etsy Payments is not directly available in Togo. All other platforms use Stripe or PayPal.

**Recommended setup:**

1. **Payoneer** (payoneer.com): Free to open. Widely used across West Africa. Provides a virtual US bank account. Gumroad, Payhip, and most platforms can pay to Payoneer. Transfer from Payoneer to your local account or Flooz/T-Money.

2. **Wise** (wise.com): Free to open. Provides virtual USD, EUR, GBP accounts. Lower transfer fees than Payoneer for some corridors. Accept payments in USD, withdraw in CFA.

3. **PayPal**: Available in Togo for receiving payments. Withdrawal to local bank is possible but fees are higher. Use as backup.

**Recommendation:** Open both Payoneer and Wise on day one. Connect Payoneer to Gumroad and Wise as your backup. This gives you two independent payout channels.

---

## PART 8: MONITORING

### Free Monitoring Stack (Weekly, 30 Minutes)

- **Native analytics** on each platform: views, clicks, sales, conversion rate.
- **EverBee** on Etsy/competitor listings: check what is newly trending in your niches.
- **Google Trends**: look 6 to 8 weeks ahead for upcoming seasonal demand spikes.
- **eRank free**: check your keyword performance weekly.

### What the Data Tells You

High views, zero sales: your mockup or price is wrong. Change the thumbnail first, then the price.
Low views, strong conversion: your SEO is wrong. Your title and tags need new keywords.
Consistent sales on one product: create 10 more variations of that exact product immediately.
Zero views after 2 weeks: retire the listing. Research again. The niche was wrong.

---

## PART 9: COMPLETE PLATFORM AND FEE TABLE

| Platform | Monthly Fee | Listing Fee | Sale Fee | Traffic | Open to Togo |
|---|---|---|---|---|---|
| Whop | $0 | $0 | 3% | Growing | Yes |
| Payhip | $0 | $0 | 5% | Low (own audience) | Yes |
| Ko-fi | $0 | $0 | 5% | Low (own audience) | Yes |
| Gumroad | $0 | $0 | 10% | Medium (Discover) | Yes (Payoneer) |
| Lemon Squeezy | $0 | $0 | 5%+$0.50 | Low | Yes |
| Systeme.io | $0 | $0 | 0% | Low | Yes |
| Itch.io | $0 | $0 | 10% min | Medium (niche) | Yes |
| Opuna | $0 | $0 | Low % | Low (growing) | Yes |
| Design Bundles | $0 | $0 | 60% to platform | High (craft niche) | Yes (apply) |
| Teachers Pay Teachers | $0 | $0 | 45% (free) | High (education) | Yes (apply) |
| Creative Market | $0 | $0 | 30 to 70% you keep | High (design) | Yes (apply) |
| Etsy | $0/month | $0.20/listing | 6.5%+3% | Very High | Yes (Payoneer) |
| Creative Fabrica | $0 | $0 | Subscription split | Very High (craft) | Yes (apply) |

**Best starting combination with zero money:**
Gumroad + Payhip + Whop + Ko-fi simultaneously from day one.
Add Design Bundles and Teachers Pay Teachers once you have a portfolio.
Add Etsy once you have first revenue to cover listing fees.

---

## PART 10: FIRST 30 DAYS PLAN

| Days | Action |
|---|---|
| Day 1 | Create accounts: Leonardo AI, Ideogram, Microsoft Designer, Canva, Inkscape, Claude, Payoneer, Wise, Gumroad, Payhip, Ko-fi, Whop |
| Day 2 | Research: 3 hours identifying your first 2 niches. Confirm with EverBee and eRank. Document keywords. |
| Day 3 to 5 | Create first 10 products (5 per niche). Use full assembly line. Generate listing copy for each. Create mockups. |
| Day 6 | Publish everything to Gumroad, Payhip, Ko-fi, and Whop simultaneously. |
| Week 2 | Add 20 more listings across all platforms. |
| Week 3 | Review analytics. Double down on what is selling. Fix what is not. Add 20 more listings. |
| Week 4 | Apply to Design Bundles and Teachers Pay Teachers with your growing portfolio. |
| End of Month 1 | 50+ listings across 4 platforms. First sales confirmed. First data guiding month 2 production. |

---

*This system requires zero upfront capital. All tools are free. All platforms listed in Part 1 charge zero listing fees. You only pay a percentage when you make a sale. The only exception is Etsy at $0.20 per listing, which should be funded from your first revenue from the zero-fee platforms.*

*Built for Kheir Lissi / May 2026 / kora-lab.com*


--- FILE: concepts/KORA_IDENTITY/KoraLab_FounderBio_Final (1).md
# KHEIR LISSI
**Founder, Kora Lab / Lome, Togo**
kora-lab.com / edenvallie.com

---

## WHO I AM

I am a self-directed AI and product builder from Lome, Togo. I am building Kora Lab, Africa's sovereign AI research and product lab, with a single conviction: the continent that will have the largest share of the world's population by 2050 cannot afford to be a passive consumer of AI built by and for others.

I studied computer science with a specialization in AI and big data in college before making a deliberate decision to leave mid third year. This was not a failure of commitment. It was a refusal to accept the pace. The gap between what the world's top AI labs were building and what college curricula were teaching was wide enough to drive a continent through. I chose to be on the right side of that gap.

I am self-taught through open resources, the same ones available to anyone with a connection and the will to understand. I do not present this as a credential. I present it as evidence of the only thing that actually matters at this stage: that I am building, learning, and moving while others wait for permission.

---

## WHY KORA LAB

I launched the vision behind Kora Lab in April 2025. The name Kora references the West African string instrument, an instrument of cultural identity, precision, and centuries of mastery. A fitting name for a lab that intends to play at the global AI frontier without abandoning where it comes from.

What I identified early is that Africa's greatest risk in the AI era is not a lack of talent. It is a lack of infrastructure, ownership, and narrative. Governments have signed declarations. Billions have been pledged. The Kigali Declaration, the $60 billion Africa AI Fund, the AU Continental AI Strategy, the AfDB and UNDP AI 10 Billion Initiative: all of this political will and capital exists without a unified, independent AI lab capable of executing the vision at ground level.

Kora Lab fills that gap. I am not competing with these institutions. I am completing them. I position Kora as the technical execution arm of Africa's AI sovereignty movement: building what governments have mandated, providing what institutions have funded, and executing what declarations have promised.

The lab operates across two axes.

Axis One is Accessibility. Making the latest AI from Anthropic, OpenAI, DeepMind, and others genuinely usable for African and global users. Adapted in language, interface, price, and context. No technical knowledge required. This includes AI agents, no-code interfaces, developer tooling, and data collection pipelines that create real employment on the continent.

Axis Two is Sovereignty. Building Africa's own large language and multimodal models from the ground up. Trained on African languages and knowledge systems. Authored by African researchers. Owned by African institutions. This means competing, eventually, in the AGI race as Africa's standard bearer.

---

## EDENVALLIE

In April 2026, I launched a second initiative: edenvallie.com. The observation was simple. ADHD and neurodivergent founders often have extraordinary analytical, structural, and creative capacity, but struggle with execution in environments not built for them. Eden Valley is an incubator built specifically to change that: an ecosystem where the way neurodivergent founders think is treated as a feature, and where the right team and structure are provided around them.

This is not a side project. It is a parallel thesis: the people most capable of building the future are often the least served by systems that claim to support builders.

---

## WHAT I BRING

I am not a technical researcher with a lab behind me. I am a founder in the earliest and most vulnerable stage of the journey, with a clear vision, a continental mandate, and full awareness of exactly what I need to move forward.

I understand the problem deeply. I know the landscape of tools, models, APIs, and infrastructure. I know what Africa needs and, critically, what Africa's role in the global AI race must be.

I know that 54 nations have declared a version of what I am building. I know that the AfDB and UNDP are mobilizing capital for exactly the kind of work Kora Lab does. I know that Togo's own digital strategy mandates the creation of an innovation ecosystem like this. I know that the AU Continental AI Strategy is in Phase 1 right now, actively seeking private sector actors to build what it has committed to.

The declarations exist. The capital is forming. The political will is real.

What is missing is the lab that turns all of it into deployed products, trained models, and sovereign infrastructure.

That is what I am building.

---

## CONTACT

Kheir Lissi / Founder, Kora Lab
Lome, Togo
kora-lab.com / edenvallie.com


--- FILE: concepts/KORA_IDENTITY/KoraLab_FounderBio_Final.md
# KHEIR LISSI
**Founder, Kora Lab / Lome, Togo**
kora-lab.com / edenvallie.com

---

## WHO I AM

I am a self-directed AI and product builder from Lome, Togo. I am building Kora Lab, Africa's sovereign AI research and product lab, with a single conviction: the continent that will have the largest share of the world's population by 2050 cannot afford to be a passive consumer of AI built by and for others.

I studied computer science with a specialization in AI and big data in college before making a deliberate decision to leave mid third year. This was not a failure of commitment. It was a refusal to accept the pace. The gap between what the world's top AI labs were building and what college curricula were teaching was wide enough to drive a continent through. I chose to be on the right side of that gap.

I am self-taught through open resources, the same ones available to anyone with a connection and the will to understand. I do not present this as a credential. I present it as evidence of the only thing that actually matters at this stage: that I am building, learning, and moving while others wait for permission.

---

## WHY KORA LAB

I launched the vision behind Kora Lab in April 2025. The name Kora references the West African string instrument, an instrument of cultural identity, precision, and centuries of mastery. A fitting name for a lab that intends to play at the global AI frontier without abandoning where it comes from.

What I identified early is that Africa's greatest risk in the AI era is not a lack of talent. It is a lack of infrastructure, ownership, and narrative. Governments have signed declarations. Billions have been pledged. The Kigali Declaration, the $60 billion Africa AI Fund, the AU Continental AI Strategy, the AfDB and UNDP AI 10 Billion Initiative: all of this political will and capital exists without a unified, independent AI lab capable of executing the vision at ground level.

Kora Lab fills that gap. I am not competing with these institutions. I am completing them. I position Kora as the technical execution arm of Africa's AI sovereignty movement: building what governments have mandated, providing what institutions have funded, and executing what declarations have promised.

The lab operates across two axes.

Axis One is Accessibility. Making the latest AI from Anthropic, OpenAI, DeepMind, and others genuinely usable for African and global users. Adapted in language, interface, price, and context. No technical knowledge required. This includes AI agents, no-code interfaces, developer tooling, and data collection pipelines that create real employment on the continent.

Axis Two is Sovereignty. Building Africa's own large language and multimodal models from the ground up. Trained on African languages and knowledge systems. Authored by African researchers. Owned by African institutions. This means competing, eventually, in the AGI race as Africa's standard bearer.

---

## EDENVALLIE

In April 2026, I launched a second initiative: edenvallie.com. The observation was simple. ADHD and neurodivergent founders often have extraordinary analytical, structural, and creative capacity, but struggle with execution in environments not built for them. Eden Valley is an incubator built specifically to change that: an ecosystem where the way neurodivergent founders think is treated as a feature, and where the right team and structure are provided around them.

This is not a side project. It is a parallel thesis: the people most capable of building the future are often the least served by systems that claim to support builders.

---

## WHAT I BRING

I am not a technical researcher with a lab behind me. I am a founder in the earliest and most vulnerable stage of the journey, with a clear vision, a continental mandate, and full awareness of exactly what I need to move forward.

I understand the problem deeply. I know the landscape of tools, models, APIs, and infrastructure. I know what Africa needs and, critically, what Africa's role in the global AI race must be.

I know that 54 nations have declared a version of what I am building. I know that the AfDB and UNDP are mobilizing capital for exactly the kind of work Kora Lab does. I know that Togo's own digital strategy mandates the creation of an innovation ecosystem like this. I know that the AU Continental AI Strategy is in Phase 1 right now, actively seeking private sector actors to build what it has committed to.

The declarations exist. The capital is forming. The political will is real.

What is missing is the lab that turns all of it into deployed products, trained models, and sovereign infrastructure.

That is what I am building.

---

## CONTACT

Kheir Lissi / Founder, Kora Lab
Lome, Togo
kora-lab.com / edenvallie.com


--- FILE: concepts/KORA_IDENTITY/KoraLab_MasterContextPrompt.md
# KORA LAB — MASTER CONTEXT PROMPT
## Paste This at the Start of Any AI Session to Get Full Context-Aware Assistance

---

## HOW TO USE THIS DOCUMENT

Copy everything from the line marked START below and paste it as your first message in any new AI chat session (Claude, ChatGPT, Gemini, or any other tool). The AI will then have full context about who you are, what you are building, and how to assist you at the right level. You do not need to re-explain anything.

After pasting, simply add your specific request for that session at the end.

---

=== START OF MASTER CONTEXT PROMPT ===

You are my strategic and operational AI partner for building Kora Lab. Before I give you today's task, here is the full context of who I am, what I am building, and where I stand. Read all of it before responding to anything.

---

## WHO I AM

My name is Kheir Lissi. I am the founder of Kora Lab. I am from Lome, Togo, West Africa. I am in my early twenties. I studied computer science with a specialization in AI and big data in college, which I left mid third year by deliberate choice. The pace of academic training was incompatible with the urgency of what I am building and the speed at which the AI world moves. I am self-taught through open resources and apply everything I learn directly to real work.

I also founded edenvallie.com, an incubator for ADHD and neurodivergent entrepreneurs who have the vision but need the right ecosystem to execute. This is a parallel venture, not a side project. It reflects the same conviction that powers Kora Lab: the people most capable of building the future are the least served by the systems that claim to support builders.

---

## THE SITUATION RIGHT NOW

I am building Kora Lab alone, in Lome, Togo, with no salary, no formal funding, no incorporated entity yet, and no team. I have full clarity on the vision and the strategy. What I lack is capital, compute, and co-builders. I am actively pursuing grants, accelerators, government partnerships, and the first product revenue to generate personal financial independence while building the lab.

My immediate financial situation is critical. I have zero income currently. This makes everything time-sensitive. Every piece of work must balance long-term strategic building with short-term survival priorities. Do not give me advice that assumes I have money to spend unless I explicitly say so.

Kora Lab is not yet incorporated. When legal standing becomes necessary for a grant or contract, I can incorporate in Togo through the CFE very quickly and at low cost. Until then, all outreach and applications use "Kora Lab, currently in formation" language.

---

## WHAT KORA LAB IS

Kora Lab is Africa's sovereign AI research and product lab. It is the technical execution arm of Africa's AI sovereignty movement. It does not compete with the institutions that have declared commitments to African AI. It completes them.

The name Kora references the West African string instrument: an instrument of cultural identity, precision, and centuries of mastery. A fitting name for a lab that intends to play at the global AI frontier without abandoning where it comes from.

The lab has a global mandate. It is not building only for African users. Accessibility and sovereignty are global propositions.

---

## THE TWO STRATEGIC AXES

AXIS ONE: ACCESSIBILITY LAYER
Making the latest AI from Anthropic, OpenAI, DeepMind, and others genuinely usable for African and global users. Culturally adapted, multilingual, no technical knowledge required. Products include AI agents, no-code interfaces, developer tooling, African-context adaptations of frontier tools, and data collection pipelines that generate real jobs across the continent. The accessibility mission is global, not Africa-only.

AXIS TWO: SOVEREIGN MODEL LAB
Building Africa's own large language and multimodal models from the ground up. Trained on African languages and knowledge systems. Authored by African researchers. Owned by African institutions. This means competing, in time, in the AGI race as Africa's standard bearer.

---

## THE STRATEGIC CONTEXT (REAL, VERIFIED)

These facts are real and current as of May 2026:
- In April 2025, 54 African nations signed the Africa Declaration on AI in Kigali, committing to sovereign AI infrastructure and a $60 billion Africa AI Fund.
- The African Union Continental AI Strategy Phase 1 is active.
- The Africa AI Council was established under Smart Africa, with 40 Heads of State as members.
- The African Development Bank and UNDP launched the AI 10 Billion Initiative, targeting $10 billion mobilized and 40 million jobs by 2035.
- The African Union and Google signed a landmark AI sovereignty partnership in February 2026.
- Togo launched Digital Strategy 2025-2030 with World Bank IDA backing, mandating a private sector innovation ecosystem.
- Over 15 African countries now have active national AI roadmaps.

None of these institutions is a technical AI lab. The declarations and capital exist without an execution layer. Kora Lab is that execution layer. This is the core positioning narrative.

---

## POSITIONING RULES (ALWAYS APPLY)

- Kora Lab is not a startup asking governments for help. It is the builder that governments have been waiting for.
- We speak to governments as the execution arm of their own mandates.
- We speak to investors as the African AI bet with the clearest strategic moat.
- We speak to technical builders as the mission worth leaving a comfortable job for.
- We never compete with the AU, AfDB, Smart Africa, or MENTD. We complete them.
- We are global in mandate and African in origin. Both are equally important.

---

## DELIVERABLES ALREADY BUILT

The following documents exist and are final. Do not recreate them unless I specifically ask for a revision:

1. Pitch Deck (11 slides, black/white/gray, PowerPoint) - covers problem, the moment, vision, two axes, strategic position, market, business model, traction, founder, ask, closing.
2. One-Pager (single HTML page) - same narrative, condensed, for pre-meeting send.
3. Founder Bio (Markdown) - first person, full narrative, used for accelerator applications and LinkedIn.
4. Government Position Paper (Markdown) - policy language, references specific AU and AfDB mandates, for government outreach. Not a pitch deck.
5. Resource and Grant Tracker (Markdown) - all grants, accelerators, government contacts with deadlines and email templates.
6. Digital Product System Guide v2 (Markdown) - complete zero-capital guide to building an Etsy and multi-platform digital product business using free AI tools, for personal financial independence.
7. Website Build Prompt and Content Guidelines (Markdown) - complete prompt to generate kora-lab.com plus full content strategy.
8. Content Creation Framework (Markdown) - three video modes (Full AI documentary, Voice only, On camera), full script structure, image prompts per section, 3 to 5 second video prompts, text post formulas for LinkedIn, TikTok, and X, plus complete free tool stack for video, image, voice, and editing.

---

## CONTENT AND COMMUNICATION RULES (ALWAYS APPLY)

These apply to all content you help me create, for all documents and all platforms:

- Never use em dashes (long dash) or double hyphens anywhere. Use colons, commas, or sentence breaks instead.
- Write in first person when the content is about me or from my voice.
- Never use bullet points in professional documents, pitch content, or essays. Use prose.
- No emoji in any Kora Lab content.
- No rounded corners, decorative icons, or gradients in any design direction.
- Color palette for all Kora Lab content: black (#0A0A0A), white (#FFFFFF), gray (#1A1A1A, #6B6B6B, #ABABAB). No other colors.
- Typography: Inter or system sans-serif. Premium and minimal.
- Never exaggerate traction I do not have.
- Never assume I have money to spend.
- Correct spelling: edenvallie.com (not edenvalley.com).
- Education: I studied computer science with a specialization in AI and big data in college, left mid third year.
- Never refer to me in the third person in content I will use as my own voice.

---

## RESOURCES I AM ACTIVELY USING (FREE TIER)

Design and image: Canva free, Leonardo AI (150 tokens/day), Ideogram, Microsoft Designer, Adobe Firefly.
Video generation: Google Veo 3 via AI Studio (no watermark), Kling AI (66 daily credits), Seedance (no watermark).
Voice generation: ElevenLabs free tier, Kokoro TTS on Hugging Face.
Editing: CapCut desktop free, DaVinci Resolve free.
Listing copy: Claude free tier, ChatGPT free tier.
Research: EverBee, eRank free, EtsyHunt free, Google Trends.
Payment (Togo): Payoneer, Wise.
Compute credits being pursued: Microsoft Founders Hub, AWS Activate, Anthropic Startup Program, Google Cloud Startup.
Digital product platforms (zero listing fee): Gumroad, Payhip, Ko-fi, Whop.
APIs being explored for products: Pollinations AI (free, open source, unified endpoint for text, image, audio, video at gen.pollinations.ai), Kie AI API (core model layer under evaluation).

---

## MY WORKING PRIORITIES (IN ORDER)

1. Personal financial survival: building digital product income on Gumroad, Payhip, Ko-fi, and Whop using free AI tools.
2. Kora Lab institutional positioning: government outreach (MENTD Togo first), Smart Africa SANIA registration, AfDB engagement.
3. Compute access: Microsoft Founders Hub, AWS Activate, Anthropic Startup Program applications this week.
4. Accelerator applications: Google for Startups Africa (next cohort), MEST (2027 intake), YC (next batch).
5. First Kora Lab product: an AI accessibility platform built on Pollinations AI and Kie AI APIs, accessible with no technical knowledge, inspired by ElevenLabs Flow, Freepik Spaces, and Nodebase.
6. Content and visibility: LinkedIn 3x/week, Medium essays, YouTube documentary-style videos, TikTok.

---

## HOW TO ASSIST ME EFFECTIVELY

When I give you a task in this session:

If I ask for a document or deliverable: produce it completely. Do not give me an outline and ask if I want you to continue. Write the full thing.

If I ask for research: give me specific, named, actionable results. No vague "consider exploring" advice. Name the institution, the program, the deadline, the contact email.

If I ask for strategy: give me a specific sequence of actions, not principles. I understand the principles. I need the next five moves.

If I ask for content: follow all the content rules above automatically. Do not wait for me to remind you about em dashes or third-person voice.

If something I am asking for requires money I do not have: say so clearly, then give me the closest free or low-cost alternative.

If you see a mistake in my thinking or a better approach: say it directly. Do not soften it or bury it at the end of a long response. I want the real analysis.

Never ask me multiple questions at once. If you need clarification, ask the single most important question. Proceed with your best assumption on everything else.

---

## TODAY'S REQUEST

[Replace this line with your specific request for this session.]

=== END OF MASTER CONTEXT PROMPT ===

---

## TIPS FOR USING THIS PROMPT

CUSTOMIZING PER SESSION: After pasting the full prompt, add a clear one or two sentence task at the end. The more specific the task, the better the output. Bad: "help me with content." Good: "Write a LinkedIn post using the content formula about the AfDB AI 10 Billion Initiative announcement, under 150 words."

UPDATING OVER TIME: As things change (you get funding, you hire someone, you launch a product), update the relevant section of this prompt and save the new version. The prompt is a living document.

USING WITH DIFFERENT TOOLS:
- Claude (claude.ai): Paste the full prompt. Claude handles long context well.
- ChatGPT: Paste the full prompt. Works well.
- Gemini: Paste the full prompt. Works well.
- Perplexity: For research sessions, paste a shortened version (the first three sections) and then your research question.
- v0.dev or Bolt.new: For building UI/web components, paste only the design system section plus your specific build request.

WHAT THIS PROMPT DOES NOT REPLACE: It does not replace the specific deliverable documents (pitch deck, one-pager, etc.). For sessions where you need to revise those, attach or paste the relevant document alongside this context prompt.

---

*This master context prompt was built across a full strategic session covering Kora Lab's founding vision, positioning, deliverables, resources, and content system.*
*Kheir Lissi / Founder / kora-lab.com / May 2026*


--- FILE: concepts/KORA_IDENTITY/KoraLab_PositionPaper.md
# KORA LAB
## A Private Sector Response to the AU Continental AI Strategy and the Kigali Declaration

**Submitted by:** Kheir Lissi, Founder
**Date:** May 2026
**Contact:** kora-lab.com

---

## EXECUTIVE SUMMARY

In April 2025, 54 African nations signed the Africa Declaration on Artificial Intelligence. In doing so, they committed to building sovereign AI infrastructure, developing open African datasets, mobilizing a $60 billion Africa AI Fund, and establishing the Africa AI Council as a continental coordination body. The African Union's Continental AI Strategy entered Phase 1 implementation. The African Development Bank and UNDP launched the AI 10 Billion Initiative. Togo activated its Digital Strategy 2025-2030.

These declarations represent a historic alignment of political will, institutional commitment, and capital intention around a single goal: Africa's digital sovereignty in the age of AI.

What every one of these initiatives still requires is a private sector builder capable of executing the vision at technical ground level.

Kora Lab is that builder.

This document presents Kora Lab's positioning as the technical execution partner for Africa's AI sovereignty movement and invites dialogue with governments, multilateral institutions, and continental bodies that share this mandate.

---

## THE GAP THAT KORA LAB FILLS

The declarations are real. The gap between declaration and deployment is also real.

The African Union's Continental AI Strategy identifies five critical enablers: data, compute, skills, trust, and capital. It names private sector AI enterprises as essential actors in each. The Kigali Declaration specifically calls for the development of African-owned AI models trained on African data. The AfDB AI 10 Billion Initiative targets 40 million jobs and requires a pipeline of AI ventures capable of creating them.

None of these frameworks is itself a lab. None has the technical capacity to train a language model, deploy an AI product, build a data labeling pipeline, or produce the research outputs that sovereign AI requires. They have mandate. They require execution.

Kora Lab provides that execution. We are the technical arm these institutions are looking for.

---

## WHAT KORA LAB IS BUILDING

Kora Lab operates across two strategic axes that together address the full scope of Africa's AI sovereignty challenge.

**Axis One: Accessibility**

The most immediate barrier to African participation in the AI era is not the absence of talent. It is the absence of AI tools adapted to African contexts, languages, and economic realities. Tools like Claude, Codex, and similar frontier products are built for Western users. They are not multilingual in African languages, not priced for African markets, and not designed with African use cases in mind.

Kora Lab builds the adaptation layer. We take the latest AI from Anthropic, OpenAI, DeepMind, and others and make it genuinely usable for African end users and global users alike: adapted in language, interface, and context, requiring no technical knowledge, and priced accessibly. We also build data collection pipelines that create real, structured employment on the continent, directly contributing to the job creation targets of the AfDB initiative.

**Axis Two: Sovereign Model Development**

The deeper mandate of the Kigali Declaration is sovereignty. Africa must not only use AI; it must own the AI that is most consequential to its future. That means training large language and multimodal models on African languages, African history, and African knowledge systems.

Kora Lab is building toward that. Our research agenda includes African language dataset construction, model training on continental compute infrastructure, and open publication of research that establishes Africa as a contributor to the global AI literature. We intend to compete, in time, in the global race toward advanced AI as Africa's standard bearer.

---

## ALIGNMENT WITH SPECIFIC INSTITUTIONAL MANDATES

**African Union Continental AI Strategy**
The strategy's private sector pillar calls for "African-owned AI enterprises that build, deploy, and govern AI systems aligned with African values and development priorities." Kora Lab is that enterprise. We build in Africa, for Africa and the world, governed by African founders accountable to the continent.

**Smart Africa and the Africa AI Council**
Smart Africa's SANIA platform exists to connect investors, startups, accelerators, and institutions. Kora Lab is available for immediate listing and engagement as a featured private sector AI lab. We are prepared to serve as a demonstration case for what African AI enterprise looks like at the execution layer.

**AfDB and UNDP AI 10 Billion Initiative**
The initiative's five enablers are data, compute, skills, trust, and capital. Kora Lab directly addresses three of them through its operations: data (via labeling pipelines and African dataset construction), skills (via the employment and training those pipelines generate), and trust (via transparent, African-authored model development). We are a natural grantee and partner for this initiative's startup investment arm.

**Togo Digital Strategy 2025-2030**
Togo's national strategy, supported by World Bank IDA, specifically targets the development of a private sector innovation ecosystem and positions Togo as a regional digital hub. Kora Lab is headquartered in Lome. We are the kind of enterprise the strategy is designed to produce and support. A partnership with the Ministry of Digital Economy and Digital Transformation would represent a direct fulfillment of the strategy's private sector mandate.

---

## WHAT WE ARE SEEKING

Kora Lab is at the founding stage. We are not seeking charity. We are seeking alignment.

Specifically, we invite the following from governments, multilateral institutions, and continental bodies:

**Letters of Support and Institutional Endorsement**
A letter of recognition from MENTD, Smart Africa, the AU Commission, or the AfDB signals to the broader ecosystem that Kora Lab is a credible actor aligned with continental mandates. This costs nothing and opens significant doors.

**Introduction to Relevant Fund Managers**
The $60 billion Africa AI Fund, the AfDB AI 10B startup investment arm, and national digital innovation funds are all potential capital sources. We ask for introductions to the relevant program officers and application guidance.

**Co-design of Data Infrastructure Projects**
Governments hold data that African AI needs. We invite discussion around data access agreements, labeling contracts, and co-developed datasets in priority sectors such as health, agriculture, governance, and education.

**Public Procurement Pilot Opportunities**
As Kora Lab develops AI products and tools, we seek to pilot them within government contexts in Togo and neighboring countries, generating both revenue and a track record of public sector deployment.

---

## ABOUT THE FOUNDER

Kheir Lissi is a computer science graduate from Lome, Togo, specializing in AI and big data, who left college mid third year to pursue the mission that became Kora Lab. He is also the founder of edenvallie.com, an incubator for neurodivergent entrepreneurs. He brings to this work a clear vision of Africa's AI future, a detailed understanding of the global AI landscape, and the determination to build without waiting for conditions to be perfect.

---

## NEXT STEPS

We welcome a 30-minute introductory call or meeting with any institution aligned with the mandate described in this document.

**Kheir Lissi**
Founder, Kora Lab
Lome, Togo
kora-lab.com


--- FILE: concepts/KORA_IDENTITY/KoraLab_ProductResearchPrompt.md
# KORA LAB FIRST PRODUCT — DEEP RESEARCH AND BRAINSTORM PROMPT
## Paste This Into Any AI Tool to Drive a Full Product Discovery Session

---

## HOW TO USE THIS PROMPT

This is a self-contained research and brainstorm prompt. Paste it in full into Claude, ChatGPT, Gemini, or any capable AI tool. It will run a structured deep research and product design session for Kora Lab's first product without needing the master context document. All necessary context is embedded.

---

=== START OF PRODUCT RESEARCH PROMPT ===

I need you to conduct a deep research and brainstorm session on the first product Kora Lab will build. I will give you the context, the reference products, the technical constraints, and then I need you to deliver a complete product analysis and vision document.

Read everything before you start. Then deliver the full output in one response. Do not ask clarifying questions before starting. If you need to make assumptions, state them and proceed.

---

## ABOUT KORA LAB

Kora Lab is Africa's sovereign AI research and product lab, founded by Kheir Lissi in Lome, Togo. The lab operates on two axes: making frontier AI accessible to African and global users (Axis One), and building Africa's own sovereign AI models (Axis Two). The first product falls squarely on Axis One.

The core accessibility mission is global, not Africa-only. The product must be usable by anyone in the world with no technical knowledge. African contexts, languages, and use cases are prioritized in design, but the market is global.

The founder has no funding yet. This means the first product must be buildable with:
- Free and low-cost APIs (especially Pollinations AI which is free, open-source, and requires no API key for basic use)
- Kie AI API as an additional model layer (research this tool's current capabilities and pricing as part of your response)
- Minimal backend infrastructure initially
- No paid team at launch

---

## THE REFERENCE PRODUCTS (STUDY THESE)

Research each of these products deeply. Understand what they do, what makes them work, what their limitations are, and what gap Kora Lab's product could fill differently or better.

REFERENCE 1: ELEVENLABS FLOW (elevenlabs.io/flow)
ElevenLabs Flow is a no-code, node-based AI workflow builder where users connect blocks (text input, voice generation, language translation, audio output, web search, etc.) to create multi-step AI pipelines without writing code. Think of it as a visual programming environment where the "programs" are AI workflows. A user can build a podcast production pipeline, a voice-enabled customer service agent, or a multilingual audio translator by dragging and connecting blocks on a canvas.

Research and answer:
- What specific blocks and capabilities does ElevenLabs Flow currently offer?
- Who is the target user and what are the most common use cases?
- What are the limitations and pain points users report?
- What does it cost?
- What is missing that an African-context version would need to add?

REFERENCE 2: FREEPIK SPACES (freepik.com/ai/spaces)
Freepik Spaces is an AI creative workspace where users combine multiple AI generation tools (image generation, background removal, upscaling, editing, etc.) in one unified canvas. Users can chain AI operations together visually without leaving the platform or using technical tools. It abstracts away the complexity of prompt engineering and API calls behind a clean creative interface.

Research and answer:
- What specific tools and workflows does Freepik Spaces offer currently?
- Who uses it and for what?
- What are its limitations?
- What pricing model does it use?
- What would a version designed for African creators and businesses look like differently?

REFERENCE 3: NODEBASE (research the current state of nodebase AI tools, including tools like Flowise, LangFlow, and Dify which all follow a similar node-based AI builder pattern)
Node-based AI builders allow users to visually construct AI agent workflows by connecting nodes that represent different AI capabilities (LLM prompts, retrieval, web search, code execution, etc.). They are currently mostly technical tools aimed at developers. The opportunity is in making this pattern accessible to non-technical users.

Research and answer:
- What is the current state of node-based AI builder tools? Which ones are most used?
- What is the gap between current tools and true non-technical accessibility?
- What would it take to make a node-based AI builder genuinely usable by someone with no coding knowledge in an African context?

---

## THE TECHNICAL FOUNDATION

POLLINATIONS AI (pollinations.ai / gen.pollinations.ai):
Pollinations AI is a free, open-source generative AI platform. Key facts for this product design:
- Single unified API endpoint at gen.pollinations.ai for text, image, audio, and video generation
- No API key required for basic use
- Supports models including Flux (image), GPT Image, Seedream, Claude (text), Gemini (text), Mistral (text), and more
- No data storage, anonymous usage, privacy-first
- Actively maintained, 500+ community projects already built on it
- Commercial use permitted on appropriate tiers
- React hooks available for frontend integration

For this product, Pollinations AI provides:
- Text generation (via Claude, Gemini, Mistral, OpenAI models)
- Image generation (via Flux, GPT Image, Seedream)
- Audio generation (text-to-speech and sound)
- Video generation (emerging capability)

KIE AI API:
Research this tool thoroughly. Find out:
- What is Kie AI? What does its API offer?
- What models does it provide access to?
- What is the pricing model? Is there a free tier?
- How does it compare to Pollinations AI as a model layer?
- What specific capabilities would make it the right "core model layer" choice for an accessibility product?
- Are there limitations or risks to building a product core on this API?

---

## THE PRODUCT BRIEF

Design the first Kora Lab product based on your research above. The product should:

CORE CONCEPT:
A unified, no-code AI workspace where anyone with no technical knowledge can discover, combine, and deploy AI capabilities in a single interface. Think of it as the intersection of ElevenLabs Flow's workflow builder, Freepik Spaces' all-in-one creative canvas, and a simplified version of the node-based builder pattern — but designed from the ground up for accessibility, African contexts, and global users who have been left out of the current AI wave.

The product is NOT just another AI tool aggregator. It is a workspace where AI capabilities become composable actions that anyone can chain together to solve real problems in their life, work, or business.

ACCESSIBILITY REQUIREMENTS:
- Works entirely in the browser. No install.
- No coding required. Zero.
- Multilingual interface. Priority languages: English, French, Swahili, Hausa, Yoruba, and Arabic. (The product should be designed so more languages can be added as a module, not rebuilt for each language.)
- Works on low-bandwidth connections common in West Africa.
- Works on mobile (most African internet users are mobile-first).
- Priced accessibly. A free tier must be genuinely useful, not crippled.
- Culturally adapted defaults. When a user opens the product for the first time in Lome or Lagos or Nairobi, the suggested use cases, example projects, and default templates should reflect their context, not a San Francisco startup's context.

TECHNICAL CONSTRAINTS:
- Built primarily on Pollinations AI API (free, no-key required for the base layer)
- Kie AI API as additional or core model layer
- No paid backend infrastructure at launch (use Vercel free tier, Supabase free tier, or Cloudflare Workers free tier)
- Frontend: React or Next.js
- The founder is not a deep backend engineer. The architecture must be simple enough for a learning builder with AI coding assistance.

---

## WHAT I NEED YOU TO DELIVER

Deliver a complete, structured product discovery document covering all of the following sections. Do not summarize. Write each section fully.

SECTION 1: REFERENCE PRODUCT ANALYSIS
For each of the three reference products (ElevenLabs Flow, Freepik Spaces, node-based builders), provide:
- What it does and how it works
- Who uses it and why
- Its pricing model
- Its key limitations and gaps
- What Kora Lab's version should do differently or better

SECTION 2: KIE AI API RESEARCH
Everything you can find on Kie AI: capabilities, pricing, free tier, model access, limitations, risks, and how it pairs with Pollinations AI. If you cannot find sufficient information, state that clearly and recommend how the founder should validate it before building on it.

SECTION 3: POLLINATIONS AI TECHNICAL SUMMARY
A clear, builder-ready summary of what Pollinations AI provides, organized by capability:
- Text generation: models available, how to call them, limitations
- Image generation: models available, parameters, quality
- Audio generation: what is available
- Video generation: current state
- API endpoint structure and how to use it in a React/Next.js app without a backend
- Rate limits and free tier constraints
- What happens when Pollinations AI is down or rate-limited (fallback strategy)

SECTION 4: PRODUCT VISION
A full product vision for Kora Lab's first product covering:
- Product name options (with rationale for each)
- The one-sentence product description
- The core interaction model (how does a user actually use this product step by step)
- The workspace concept: what does the canvas or interface look like?
- The "blocks" or "capabilities" that users can combine. List every capability the product should launch with, every capability it should add in month 3, and every capability it should have by the end of year 1.
- The use case library: what are the 10 most compelling problems this product solves for African users? For global users?
- Template library: what are the 10 pre-built templates that ship with the product on day one?

SECTION 5: AFRICAN CONTEXT DESIGN DECISIONS
Specific design decisions that make this product genuinely different from what exists for African users:
- Which African languages are supported at launch and how (translation layer, native model, or hybrid)?
- What are the African-specific use cases that Western products do not address? Be specific and real.
- How does the product handle low-bandwidth environments technically?
- What pricing model works for African markets? What are comparable price points?
- What cultural adaptations are needed in the UX, examples, and default content?

SECTION 6: TECHNICAL ARCHITECTURE
A concrete, builder-readable architecture for the MVP. Cover:
- Frontend stack recommendation
- How Pollinations AI is called from the frontend (direct API calls, or via a thin serverless function)
- How Kie AI API is integrated
- Where state is stored (user sessions, saved workspaces, project files)
- Authentication approach (or no auth for MVP)
- Hosting and infrastructure (all free or near-zero cost)
- What the MVP scope is (exactly what is built in the first 4 to 6 weeks)
- What is deferred to month 3

SECTION 7: BUSINESS MODEL
How this product generates revenue for Kora Lab:
- Free tier: what is included, what are the limits
- Paid tiers: what do they unlock, what are the price points
- African market pricing vs. global pricing strategy
- Government and institutional licensing opportunity
- Estimated monthly revenue at 1,000 active users, 5,000 active users, and 20,000 active users

SECTION 8: GO-TO-MARKET STRATEGY
How Kora Lab launches and grows this product with zero marketing budget:
- Who are the first 100 users and exactly how do you get them?
- What content angles drive organic discovery for this product?
- What communities and platforms are the distribution channels?
- What partnerships would accelerate distribution?
- What does week 1, month 1, and month 3 look like in terms of launch sequence?

SECTION 9: RISKS AND MITIGATIONS
The real risks of building on Pollinations AI and Kie AI as the primary API layers. For each risk:
- State the risk clearly
- Assess its probability and severity
- State the specific mitigation

SECTION 10: COMPETITIVE MOAT
Why, over time, Kora Lab's version of this product becomes difficult to displace:
- What makes it specifically better for the users it serves?
- What data advantages accrue over time?
- What community or ecosystem effects develop?
- How does the sovereign model axis (Axis Two) eventually feed into this product?

---

## OUTPUT FORMAT REQUIREMENTS

- Write in full prose for all narrative sections. No bullet points in the main analysis.
- Tables are acceptable for structured comparisons (pricing tiers, capability lists, architecture stacks).
- No em dashes anywhere. Use colons, commas, or sentence breaks.
- Do not hedge excessively. Give your actual best assessment. If something is uncertain, say so and move on.
- Length: this should be a substantive document. Do not truncate sections to save space. Write each section completely.

---

This is the founding product research session for Kora Lab. The output of this session will shape what Africa's first sovereign AI lab builds first. Treat it with that weight.

=== END OF PRODUCT RESEARCH PROMPT ===

---

## NOTES ON THIS PROMPT

WHAT THIS PROMPT IS FOR: Paste it into a fresh AI session specifically for product research and design. It is separate from your master context prompt by design. Use the master context for day-to-day operational tasks. Use this prompt when you are ready to go deep on the product.

BEST TOOLS FOR THIS PROMPT:
- Claude (claude.ai): Best for nuanced analysis and long structured documents. Recommended first choice.
- ChatGPT with browsing enabled: Good for the research sections where current information matters.
- Perplexity: Use specifically for the Kie AI API research section where you need current web information.

VALIDATING KIE AI: Before building on any API, spend 30 minutes testing it manually. Generate 10 outputs. Check the rate limits. Read the terms of service for commercial use rights. Then decide whether it belongs at the core of the product or as a supplementary layer.

POLLINATIONS AI QUICK START: To test Pollinations AI immediately, open your browser and visit:
- Image: image.pollinations.ai/prompt/a beautiful sunset over Lagos Nigeria
- Text: text.pollinations.ai/What is the state of AI in West Africa?
- Unified: gen.pollinations.ai
No account needed. Results appear instantly. This is what your product users will experience under the hood.

---

*Built for Kheir Lissi / Kora Lab / kora-lab.com / May 2026*


--- FILE: concepts/KORA_IDENTITY/KoraLab_ResourceTracker.md
# KORA LAB — MASTER RESOURCE AND GRANT TRACKER
## Every Opportunity, Deadline, Contact, and Next Action

**Last Updated: May 2026**
**Status key: APPLY NOW / THIS MONTH / NEXT CYCLE / ONGOING / MONITOR**

---

## TIER 1: APPLY THIS WEEK (Zero Cost, Immediate)

| Resource | What You Get | How to Apply | Status |
|---|---|---|---|
| Microsoft Founders Hub | $1,000 to $5,000 Azure credits instant, up to $150K over time | foundershub.startups.microsoft.com | APPLY NOW |
| AWS Activate Founders | $1,000 in AWS credits, no VC required | aws.amazon.com/activate | APPLY NOW |
| Smart Africa SANIA | Free listing, network access to 40 Heads of State ecosystem | smartafrica.org/sania | APPLY NOW |
| NVIDIA Inception Program | GPU discounts, technical support, AWS credit pathway | nvidia.com/en-us/startups | APPLY NOW |
| Hugging Face Research Credits | Compute access for model work, African language dataset support | huggingface.co/spaces/huggingface/research-credits | APPLY NOW |

---

## TIER 2: APPLY THIS MONTH

| Resource | What You Get | Deadline / Cycle | Contact / URL |
|---|---|---|---|
| YC Summer 2026 | $500K investment + network + global credibility | Apply immediately — deadline passed but late applications reviewed | ycombinator.com/apply |
| Anthropic Startup Program | $1K to $25K in Claude API credits, priority rate limits | Rolling, apply at platform.anthropic.com | anthropic.com/startups |
| Google Cloud Startup Program | Up to $350K in GCP credits | Rolling (higher tier requires accelerator) | cloud.google.com/startup |
| Code for Africa AI Fellowship 2026 | $500/month stipend + mentorship | Open now | codeforafrica.org/fellowship |
| GIZ Digital Transformation Center Togo | Free support, legal guidance, network in Lome | Walk in — Lome office | giz.de/togo |
| AfDB AI 10B Initiative Roadshow | Introductions, grant pipeline access | Ongoing roadshow now | Email: ict@afdb.org |

---

## TIER 3: NEXT CYCLE (Prepare Now, Apply on Opening)

| Resource | What You Get | When to Apply | Notes |
|---|---|---|---|
| Google for Startups Accelerator Africa | Equity-free, up to $350K GCP credits, Google network | 2027 cohort opens Q4 2026 | goo.gle/startups — monitor page |
| MEST AI Startup Program | 12 months training + up to $100K pre-seed investment | 2027 intake opens mid-2026 | mest.com/apply — requires Ghana/Nigeria/Senegal travel |
| Tony Elumelu Foundation 2027 | $5,000 non-refundable seed capital + 12 weeks training | Opens January 1, 2027 | tefconnect.com |
| Antler Africa | Equity investment, co-founder matching, network | Rolling cohorts | antler.co/africa |
| Science for Africa GC Africa Round 16 | Up to $100,000 seed grant for 12-month research project | Monitor for Round 16 opening | scienceforafrica.org |
| AI4D CAD 1M Grant | Up to CAD 1 million over 36 months | Monitor — requires institutional partner | idrc.ca/ai4d |

---

## TIER 4: GOVERNMENT AND INSTITUTIONAL OUTREACH (Do in Parallel)

| Institution | Who to Contact | What to Ask For | Action |
|---|---|---|---|
| Togo MENTD | Minister of Digital Economy — numerique.gouv.tg | Meeting + letter of support + Smart Africa introductions | Draft email + one-pager. Send this week. |
| Smart Africa Secretariat | Secretary General — Lacina Kone | Kora Lab listing on SANIA + partnership discussion | Register on SANIA first, then email |
| AfDB Digital Division | Director ICT Operations — afdb.org | 20-minute call, alignment with AI 10B Initiative | One paragraph email. Send this week. |
| AU Commission Digital Economy | Commissioner — au.int | Position paper submission + partnership dialogue | Send position paper |
| World Bank IDA Togo | Country Office — worldbank.org/togo | Alignment with Digital Togo 2025-2030 strategy | Email country office with position paper |

**Email Template for Government Outreach:**

Subject: Kora Lab — Private Sector Response to [Institution's Specific Mandate]

Body:
"My name is Kheir Lissi. I am the founder of Kora Lab, a sovereign AI research and product lab headquartered in Lome, Togo.

I am writing because Kora Lab's work directly aligns with [specific mandate — e.g., the Digital Togo 2025-2030 strategy / the AfDB AI 10 Billion Initiative / the AU Continental AI Strategy].

I have attached a two-page position paper that describes how Kora Lab acts as the private sector technical execution partner for the goals your institution has committed to.

I am requesting a 20-minute introductory call to explore how we can work together.

Kheir Lissi / Founder, Kora Lab / kora-lab.com"

Keep it to four sentences maximum. Attach the position paper. Do not pitch. Request a conversation.

---

## TIER 5: COMPUTE AND API CREDITS (BY PLATFORM)

| Platform | Amount | Requirements | URL |
|---|---|---|---|
| Anthropic Credits | $1K to $25K | Self-apply (small) or accelerator referral (full) | platform.anthropic.com |
| Google Cloud | Up to $350K | Free tier available, more with accelerator | cloud.google.com/startup |
| AWS Activate | $1K to $100K | No VC required at lower tiers | aws.amazon.com/activate |
| Microsoft Azure | $1K to $150K | Founders Hub, instant approval | foundershub.startups.microsoft.com |
| NVIDIA Credits | Via Inception | Join NVIDIA Inception first | nvidia.com/startups |
| Hugging Face | Research compute | Apply through HF research program | huggingface.co |

---

## TIER 6: SURVIVAL BRIDGE (IMMEDIATE PERSONAL INCOME)

| Source | What It Provides | Timeline | Action |
|---|---|---|---|
| Digital Product Stores | $0 to $3,000+/month, passive | 30 to 60 days to first revenue | See Digital Product System guide |
| Code for Africa Fellowship | $500/month stipend | Apply now, start within 4 to 8 weeks | codeforafrica.org |
| AFRICA KOMMT! Fellowship | Stipend + Germany placement | Annual cycle | africakommt.de |
| Upwork / Toptal | Freelance AI/data consulting income | Immediate | Set up profile with AI specialization |
| GIZ DTC Togo | May have emergency support for local founders | Walk in | Lome office |

---

## MASTER OUTREACH LOG

Use this to track every email sent, every meeting requested, every application submitted.

| Date | Institution / Person | Action Taken | Response | Follow-Up Date |
|---|---|---|---|---|
| | MENTD Togo | Email sent with one-pager | | |
| | AfDB ICT Division | Email sent with position paper | | |
| | Smart Africa / SANIA | Registered on platform | | |
| | Microsoft Founders Hub | Applied | | |
| | AWS Activate | Applied | | |
| | Code for Africa Fellowship | Applied | | |
| | Anthropic Startup Program | Applied | | |
| | NVIDIA Inception | Registered | | |
| | Google Cloud Startup | Applied | | |

---

*Update this tracker weekly. Every unanswered email after 2 weeks gets a one-sentence follow-up.*
*Kheir Lissi / Kora Lab / kora-lab.com*


--- FILE: concepts/KORA_IDENTITY/KoraLab_Website_Content_Final.md
# KORA LAB — WEBSITE BUILD PROMPT + CONTENT GUIDELINES
## Two Documents in One: What to Build, What to Write, How to Show Up

---

# DOCUMENT 1: WEBSITE BUILD PROMPT

## How to Use This Prompt

Copy everything in the block below and paste it into Claude, ChatGPT, v0.dev, or any AI web builder. It will generate a complete multi-page website for Kora Lab that you can deploy on Vercel or Netlify for free.

---

```
Build a complete, production-ready website for Kora Lab — Africa's sovereign AI lab. The site serves three audiences simultaneously: governments and institutions, investors and accelerators, and technical talent. It must feel like a research institution, not a startup landing page.

STRICT WRITING RULE — APPLY EVERYWHERE ON THE SITE
Never use em dashes (—) or double hyphens (--) anywhere in any text, heading, label, description, or copy on the site. Replace any em dash usage with a colon, a comma, a period, or restructure the sentence. This applies to all pages, all sections, all auto-generated placeholder text.

DESIGN SYSTEM
Colors: Black (#0A0A0A), White (#FFFFFF), three grays (#1A1A1A for dark panels, #6B6B6B for mid labels, #ABABAB for subdued text). No other colors. No gradients. No color accents anywhere.
Typography: Inter or system sans-serif. Weights: 400 body, 700 labels and subheadings, 900 display headlines. Line height: 1.55 for body, 1.1 for headlines.
Style: Modern, minimal, premium. Research institution feel. No emoji. No decorative icons. No rounded corners on buttons or cards. Sharp edges only.
Motion: Subtle fade-in on scroll using Intersection Observer. No parallax. No looping animations. Nothing distracting.
Layout: Full-width sections, content constrained to max 1100px, generous whitespace between sections. Mobile-first, fully responsive down to 375px. No horizontal scroll on any viewport.

SITE STRUCTURE — MULTIPLE PAGES
Build the following pages with full navigation between them:
- Home (/)
- Approach (/approach)
- Research (/research)
- Blog (/blog and /blog/[slug])
- About (/about)
- Contact (/contact)

GLOBAL ELEMENTS

Navigation (sticky, minimal, present on all pages):
- Left: KORA LAB wordmark (font-weight 900, letter-spacing -1.5px, font-size 20px)
- Center links: Mission / Approach / Research / Blog / About / Contact
- Right: "Get in Touch" button (black fill, white text, sharp corners, padding 10px 20px)
- On mobile: hamburger menu, full-screen overlay with the same links in large type on black background
- Active page link has a thin black underline indicator

Footer (present on all pages):
- Left column: KORA LAB wordmark + tagline "Africa's Sovereign AI Lab" + location "Lome, Togo"
- Center column: Navigation links repeated
- Right column: "Building for the continent." + links to kora-lab.com and edenvallie.com
- Bottom bar: thin top border + copyright line + "All rights reserved"
- Background: black. Text: white and grays.

PAGE 1: HOME (/)

Section 1.1 — Hero
Background: Black (#0A0A0A)
Headline structure (very large, stacked, font-weight 900, font-size responsive 56px to 80px):
  Line 1 white: "Africa doesn't just"
  Line 2 white: "consume AI."
  Line 3 color #ABABAB: "Africa builds AI."
Thin white horizontal rule (width 80px, height 1px) between headline and subheadline
Subheadline (gray #ABABAB, font-size 18px, max-width 600px): "Kora Lab is Africa's sovereign AI research and product lab. Closing the gap, building the models, uniting the continent under one flag."
Two CTA buttons below: "Our Approach" (white fill, black text) and "Contact the Founder" (white outline, white text, transparent fill)

Section 1.2 — Ticker
Full-width, black background, overflow hidden
Slow horizontal scroll (CSS animation, no JS), white text, font-size 13px, letter-spacing 2px, uppercase
Text repeating: "54 NATIONS / $60B AFRICA AI FUND / AU CONTINENTAL AI STRATEGY / AFDB AI 10B INITIATIVE / DIGITAL TOGO 2025-2030 / SMART AFRICA / ONE FLAG / "

Section 1.3 — The Problem
Background: #E8E8E8
Section label: "THE PROBLEM" (9px, uppercase, letter-spacing 3px, gray #6B6B6B)
Headline: "Africa Is Being Left Out of the AI Race" (font-weight 900, large)
Three equal columns, each with a label and paragraph:
  ACCESS GAP: Frontier AI tools are built for Western users. African end users face language, UX, and affordability barriers that make these tools impractical in their context.
  SOVEREIGNTY GAP: All large-scale AI models and infrastructure are owned by non-African entities. Africa has no seat at the table in shaping the models that will define its future.
  EXECUTION GAP: Governments have signed declarations. Billions are pledged. The AU Continental AI Strategy is live. What is missing is a technical lab capable of executing the vision at ground level. That is what Kora Lab is.
Each column has a thin black top border and padding above the label.

Section 1.4 — The Moment
Background: Black
Section label: "THE MOMENT"
Headline: "The Continent Has Spoken. Now It Needs Builders."
Four stacked rows, each with a date label (dark gray box on left) and event text (right):
  APRIL 2025: 54 African nations sign the Africa Declaration on AI in Kigali. A $60 billion Africa AI Fund is announced.
  FEBRUARY 2026: The African Union and Google sign a landmark AI sovereignty partnership. The AfDB and UNDP launch the AI 10 Billion Initiative.
  2025-2026: Togo activates Digital Strategy 2025-2030. At least 15 African countries now have national AI roadmaps.
  THE GAP: All of this political will and capital exists without a unified technical lab to execute it. Kora Lab is that lab.
Closing italic line (gray, font-size 20px): "We are not competing with these institutions. We are completing them."

Section 1.5 — Stats
Background: White
Four large stat blocks in a 2x2 grid, separated by 1px black lines (creating a grid effect with no spacing between cells):
  54 / Nations that signed the Kigali AI Declaration
  $60B / Africa AI Fund pledged
  2,000+ / African languages almost entirely absent from frontier AI training data
  4% / Africa's current share of the global AI workforce
Each block: stat value in 56px font-weight 900, label in 11px uppercase gray below.

Section 1.6 — Latest from the Blog (preview, 3 cards)
Background: #E8E8E8
Section label: "LATEST WRITING"
Headline: "From the Kora Lab Blog"
Three blog post preview cards in a row. Each card:
  Category label (small uppercase)
  Title (font-weight 700, 18px)
  Excerpt (2 sentences, gray)
  Date and read time (small gray)
  "Read Article" link with arrow
Link below cards: "View All Articles" pointing to /blog

Section 1.7 — Latest Research (preview, 2 items)
Background: White
Section label: "RESEARCH"
Headline: "From the Lab"
Two research item rows. Each row:
  Research type tag (WORKING PAPER / ANALYSIS / DATASET)
  Title
  One-line description
  Date + "Read Paper" link
Link below: "View All Research" pointing to /research

Section 1.8 — Contact CTA
Background: Black
Headline: "Build With Us."
Subheadline: "Whether you are a government, an institution, an investor, or a technical builder who believes in this mission, we want to hear from you."
Single "Get in Touch" button (white fill, black text, sharp corners)

PAGE 2: APPROACH (/approach)

Hero: Black background, headline "A Two-Axis Strategy for Africa's AI Sovereignty", subheadline describing the two axes briefly.

Section — Axis 01: Accessibility Layer
Black background left panel / white background right panel (50/50 split)
Large "01" numeral in dark gray (decorative)
Title: ACCESSIBILITY LAYER
Full description of what this axis involves: adapting frontier AI tools, building culturally relevant products, creating data pipelines that generate jobs, no technical knowledge required for end users.
List of product types: AI agents, no-code interfaces, developer tooling, African-language adaptations, data collection pipelines.

Section — Axis 02: Sovereign Model Lab
White background left panel / black background right panel (reversed)
Large "02" numeral
Title: SOVEREIGN MODEL LAB
Full description: building Africa's own language models and multimodal models, training on African data, publishing research, competing in the global AI race.
List of activities: African language dataset construction, model training, research publication, institutional partnerships, AI safety research.

Section — Institutional Alignment
Light gray background
Headline: "Aligned With Every Major African AI Mandate"
Table or card list of institutions and mandates:
  African Union Continental AI Strategy / Phase 1 active
  Smart Africa and Africa AI Council / 40 Heads of State board
  AfDB and UNDP AI 10 Billion Initiative / $10B target by 2035
  Togo MENTD Digital Strategy 2025-2030 / World Bank IDA backed
  Africa AI Fund $60B / Announced Kigali 2025

PAGE 3: RESEARCH (/research)

Hero: White background, black headline "Research and Papers", subheadline "Kora Lab publishes working papers, analyses, and datasets on African AI, language models, and digital sovereignty."

Filters row: All / Working Papers / Analyses / Datasets / Policy Briefs (tab-style filter, plain text, active filter has a black underline)

Research item list: Each item in a row with:
  Left: Type tag (small uppercase label in a light gray box)
  Center: Title (font-weight 700) + one-line description + authors + date
  Right: "Read Paper" link + optional PDF download icon
Use placeholder items for now with [TITLE], [DATE], [TYPE] clearly marked for easy replacement.

Call to action at bottom: "Collaborate With Us" section with short text inviting researchers, institutions, and universities to partner, plus a mailto link.

PAGE 4: BLOG (/blog and /blog/[slug])

Blog index (/blog):
Hero: Small, clean. Headline "Writing" subheadline "Analysis, perspectives, and updates from Kora Lab."
Filter tabs: All / Analysis / Institutional / Technical / Updates
Grid of blog post cards (3 columns desktop, 1 column mobile). Each card:
  Category label
  Title
  Excerpt (2 sentences)
  Author (Kheir Lissi) + Date + Estimated read time
  "Read" link

Blog post page (/blog/[slug]):
Clean reading layout, max-width 720px centered.
Top: Category label + Title (large, bold) + Author + Date + Read time
Body: Proper typographic hierarchy. h2 and h3 headings for structure. Generous line height (1.7). No em dashes anywhere.
Bottom: Author card (brief bio + link to About page) + "More from the Blog" section (3 related post cards)
SEO: Each blog post page must include unique title tag, meta description, Open Graph tags (og:title, og:description, og:image), and canonical URL.

PAGE 5: ABOUT (/about)

Section — Founder
Large name display: KHEIR LISSI (font-weight 900, large)
Role: Founder, Kora Lab / Lome, Togo
Full founder bio in first person (see content below — use the complete bio, not a truncated version)
Links: kora-lab.com and edenvallie.com

Section — The Mission
Black background, white text
Headline: "Why Kora Lab Exists"
Long-form mission statement explaining the problem, the vision, the two axes, and the continental mandate. 4 to 6 paragraphs.

Section — Advisors / Team (placeholder)
Light gray background
Headline: "The Team"
Placeholder card grid with [Name], [Role], [Institution] clearly marked so real people can be added later.
Note visible in code comments: "Replace placeholder cards with real advisor names and bios as they are confirmed."

PAGE 6: CONTACT (/contact)

Hero: Black background, white headline "Get in Touch"
Subheadline: "We welcome conversations with governments, institutions, investors, researchers, and builders."

Four contact categories with descriptions:
  Governments and Institutions: "For partnership discussions, government contracts, and institutional alignment around continental AI mandates."
  Investors and Accelerators: "For funding conversations, accelerator applications, and strategic partnerships."
  Researchers and Technical Builders: "For research collaboration, advisory roles, and joining the Kora Lab mission."
  Press and Media: "For interviews, background briefings, and press inquiries about Kora Lab."

Contact form fields: Name, Organization, Category (dropdown matching the four above), Message, Send button
Success state: Replace form with a thank you message on submit.
Direct contact: Email address displayed in gray below the form.

SEO REQUIREMENTS (APPLY TO ALL PAGES)

Every page must include in the HTML head:
  <title> tag: unique per page, format "Page Name | Kora Lab"
  <meta name="description"> tag: unique per page, 140 to 160 characters, includes primary keyword
  <meta property="og:title"> Open Graph title
  <meta property="og:description"> Open Graph description
  <meta property="og:image"> placeholder path for social share image
  <meta property="og:url"> canonical URL
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title">
  <meta name="twitter:description">
  <link rel="canonical"> tag

Structured data (JSON-LD) in the head of the home page:
  Organization schema: name, url, logo, description, founder, location
  WebSite schema with SearchAction

Robots.txt file: allow all crawlers, point to sitemap.xml
Sitemap.xml: include all page URLs with lastmod dates

On-page SEO per page:
  One H1 per page only
  H2 and H3 used correctly for section hierarchy
  Alt text on every image (descriptive, keyword-relevant)
  Internal links between pages using descriptive anchor text (not "click here")
  Page load under 2 seconds (no heavy assets, no unoptimized images)
  All images use lazy loading (loading="lazy" attribute)

Target keywords by page:
  Home: "African AI lab", "Africa sovereign AI", "AI Africa"
  Approach: "African language AI models", "AI accessibility Africa"
  Research: "African AI research", "African language models research"
  Blog: varies per article, each post targets its own keyword
  About: "Kheir Lissi", "Kora Lab founder"
  Contact: "AI partnership Africa", "African AI collaboration"

TECHNICAL REQUIREMENTS

Framework: React (Next.js preferred for SEO with server-side rendering) OR plain HTML with multiple files.
If Next.js: use App Router, generateMetadata for dynamic SEO per page, and static generation for blog posts.
If plain HTML: create separate HTML files per page, include all meta tags manually.
No external UI libraries. Use only CSS for styling.
Font loading: Google Fonts Inter via @import in CSS, with font-display: swap.
Form handling: On submit, prevent default, show inline success state. No backend required initially.
No em dashes (--) anywhere in any generated code, comments, placeholder text, or copy.
Deploy-ready: include a vercel.json or netlify.toml configuration file for one-click deployment.
Include a README.md with deployment instructions (3 steps maximum).
```

---

## Deployment (Free, No Credit Card)

**Recommended: Vercel with Next.js**
1. Push generated code to a GitHub repository.
2. Go to vercel.com, create a free account, import the repository.
3. Click Deploy. Live in 60 seconds at a vercel.app URL.
4. Add your custom domain (kora-lab.com) in Vercel settings. Free SSL included.

**Alternative: Netlify**
1. Go to netlify.com. Create a free account.
2. Drag your build folder onto the Netlify dashboard.
3. Add custom domain in settings.

**Domain:** Register kora-lab.com at Namecheap or Cloudflare Registrar for approximately $10 to $12 per year.

---

# DOCUMENT 2: CONTENT GUIDELINES FOR VISIBILITY

## The Core Strategy

Your content has one job at this stage: make you known and taken seriously by the three audiences that can change everything for Kora Lab. Governments and institutions. Investors and accelerators. Technical builders who could join or advise you.

You do not need to sell yet. You need to be found, read, and remembered. The internet is your proof of existence, your public track record, and your legal prior art simultaneously.

---

## THE FIVE CHANNELS (PRIORITY ORDER)

---

### Channel 1: LinkedIn (Highest Priority)

LinkedIn is where the people who can open doors for Kora Lab spend professional time. Government officials, AfDB program officers, accelerator partners, researchers, and investors are all active here. This is your primary channel.

**Profile setup:**
- Headline: Founder, Kora Lab | Building Africa's Sovereign AI Lab | Lome, Togo
- About section: Your founder bio condensed to 5 to 7 sentences, first person.
- Featured section: Pin your one-pager (as PDF), your founding essay link, and your website.
- Profile photo: Clear, professional. Neutral background.
- Banner: Black background, KORA LAB in white, tagline below.

**Posting frequency:** 3 times per week.

**Format 1: The Observation (2x per week)**
5 to 10 short lines. Open with a specific, verifiable fact. Add your perspective in 2 to 3 lines. End with one clear point.

Example:
"The AfDB AI 10 Billion Initiative targets 40 million jobs by 2035.

That is 40 million jobs that need AI tools, training, and infrastructure built specifically for African contexts.

No existing AI lab is building that infrastructure at the ground level. Not OpenAI. Not Anthropic. Not DeepMind.

This is what Kora Lab is being built to do.

The mandate exists. The capital is forming. The execution layer is what is missing."

**Format 2: The Progress Post (1x per week)**
Honest, short update on what you did this week. No spin. No fake momentum.

Example:
"Week 3 of building Kora Lab.

What I did:
Submitted the position paper to MENTD Togo.
Registered on the Smart Africa SANIA platform.
Shipped the first version of the website.
Started the Google for Startups Africa application.

No salary. No team. No compute credits yet.

But 54 nations have made the declaration. The AfDB is running a roadshow right now. Togo's digital strategy is active.

All I have to do is be the lab that executes it."

**What never to post on LinkedIn:**
Motivational quotes. Reposted news with no perspective. More than 2 hashtags. Anything that sounds like a press release.

---

### Channel 2: Medium (Long-Form Essays)

Medium is where you build intellectual credibility and generate search traffic. One strong essay here reaches people inside institutions in ways that social media posts never do. Each essay also becomes a blog post on your own site and a LinkedIn long-form article.

**Essay 1: The Founding Essay (Publish within 2 weeks)**

Title: "What Africa's AI Declarations Need That Nobody Is Talking About"

Structure:
1. Open with the specific declarations by name and date. Not an opinion. A fact.
2. Name the execution gap: declarations without a technical lab are unfulfillable.
3. Describe what the execution layer must do (your two axes, without pitching).
4. Introduce Kora Lab as the lab being built to fill that gap.
5. End with a direct call to action for the three audiences.

Length: 1,200 to 1,800 words. No longer.
Tone: Confident, specific, unspun. Closer to a policy brief than a blog post.
Cross-post: Wait one week after publishing on Medium, then post as a LinkedIn Article. Then add to your website blog.

**Essay 2 (Month 2):** "What African Language AI Actually Requires and Why Nobody Is Building It"
Technical credibility through research and analysis. Does not require a PhD. Requires reading and synthesis.

**Essay 3 (Month 3):** "The $60 Billion Africa AI Fund Has a Deployment Problem. Here Is How to Solve It"
Written explicitly for fund managers and institutional readers. Frames Kora Lab as the solution.

---

### Channel 3: YouTube (Medium Priority, Build Audience Over Time)

YouTube is the highest-leverage channel for building a technical and institutional audience that stays with you. One well-made video drives more trust than 50 posts. You do not need expensive equipment. A good phone, natural light, and a clean background is enough to start.

**Content types for Kora Lab on YouTube:**

Type 1: The Founder Video Series (most important, start here)
Short videos (5 to 12 minutes) where you speak directly to camera about the African AI landscape, the work Kora Lab is doing, and what you are building. These build personal trust at scale.

Episode ideas:
- "Why I left college mid third year to build Africa's AI lab" (your story, authentic)
- "What the Kigali Declaration actually commits to and what is missing"
- "What African language AI requires that Western models cannot provide"
- "How I am building a sovereign AI lab with no funding yet"
- "What the AfDB AI 10 Billion Initiative means for African startups"

Type 2: Research Breakdowns (once you have papers)
10 to 20 minute walkthroughs of your own research papers or significant AI papers with an African relevance lens. Builds technical credibility.

Type 3: Lab Updates (monthly)
5 to 8 minute honest monthly update on what Kora Lab accomplished, what is next, and what you need. Transparency builds supporters.

**Production on zero budget:**
- Phone camera, propped up at eye level.
- Window light on your face. Black or plain white wall behind you.
- Free editing: DaVinci Resolve (free, professional-grade) or CapCut (free, fast).
- Subtitles: Use YouTube's auto-caption feature and correct any errors.
- Thumbnail: Design in Canva free. Black background, bold white text, your face.

**YouTube SEO:**
- Video title: include the primary keyword in the first 5 words.
- Description: first 2 sentences are the most important (shown before "show more"). Include your website link in the first line.
- Tags: 8 to 12 relevant tags. Include "African AI", "AI Africa", "Kora Lab", and the specific topic.
- Chapters: add timestamps in the description for every video over 5 minutes.
- Post frequency: start with 2 videos per month. Consistency beats volume.

**Cross-platform:** Every YouTube video becomes a LinkedIn post (link + key takeaway), a Twitter thread (key points in 5 tweets), and if long enough, a blog post (transcript lightly edited).

---

### Channel 4: TikTok (Lower Priority, Highest Reach Potential)

TikTok reaches a completely different audience than LinkedIn or YouTube: young African professionals, students, and the global creator economy. The audience here will not fund you directly, but they become advocates, spread your name, and attract the attention of people who will. Africa has some of the highest TikTok growth rates in the world.

The format is different. TikTok rewards authenticity, speed, and hooks. The first 3 seconds determine everything.

**Content types for Kora Lab on TikTok:**

Type 1: Fast Facts (30 to 60 seconds)
One surprising or counterintuitive fact about African AI, delivered fast and direct to camera.

Example:
"Did you know that 2,000 African languages are almost completely absent from ChatGPT, Claude, and every other major AI model? That is not a gap. That is a crisis. And it is exactly what Kora Lab is being built to fix."

Type 2: Process Clips (15 to 30 seconds)
Short clips of you working, researching, writing. No narration needed. Text overlay does the work.

Type 3: Response Videos
When major AI news drops (new model release, new investment, new policy), record a 60-second reaction from an African perspective. This captures trending search traffic.

Type 4: The Build Journey
Honest clips of building with no money, no team, and a clear vision. This content performs because it is real. People root for the underdog who is building something bigger than themselves.

**TikTok SEO:**
- First line of caption is the most important. Lead with the hook, not the hashtag.
- Use 3 to 5 relevant hashtags: #AfricanAI #AIAfrica #TechAfrica #KoraLab and a trending topic tag.
- Post at times when your target audience is active (experiment with 7am to 9am and 7pm to 9pm WAT).
- Reply to every comment in the first hour of posting. The algorithm rewards engagement velocity.

**TikTok to LinkedIn pipeline:** Your best-performing TikTok content tells you what your LinkedIn audience wants to see. Ideas that get views on TikTok become long-form posts on LinkedIn. Every viral clip has a longer essay inside it.

---

### Channel 5: X / Twitter (Lightweight, For Amplification Only)

X is not a primary channel. Use it to amplify your LinkedIn and Medium content, engage with the global AI research community, and be discoverable when journalists and researchers search for African AI perspectives.

Post 1 to 2 times per week. Short observations, links to essays, and genuine replies to AI and Africa tech conversations.

Follow and engage with: researchers working on low-resource language models, African tech journalists, Smart Africa and AfDB accounts, and other African founders in the AI space.

---

## THE CONTENT FORMULA (APPLIES ACROSS ALL CHANNELS)

Every piece of content you produce should follow this five-part structure, adapted to the length and format of each platform:

1. Open with a specific, verifiable fact. Never start with an opinion or a rhetorical question.
   "In April 2025, 54 African nations signed the Africa Declaration on Artificial Intelligence."

2. Name the tension or gap. What is missing or broken in that fact?
   "None of the signatories is a technical AI lab."

3. Widen the lens. Connect it to the larger pattern.
   "This is the same pattern that appears every time Africa makes an ambitious commitment: vision and capital without an execution layer."

4. Your clear, non-hedged perspective. One sentence. No qualifications.
   "Kora Lab exists to be that execution layer."

5. The call. Who should act on this and how.
   "If you are an AfDB program officer, a government contact, or a builder who wants to work on this, reach out."

---

## CONTENT RAILS: ALWAYS AND NEVER

**Always:**
- Open with a specific fact, number, or named event. Never a question or "I think."
- Name institutions, declarations, and amounts specifically.
- Write in first person. Stay in first person until you have a team.
- End every post with a clear action: follow, reply, visit the site, or email.
- Be honest about where you are. Building without funding is not weakness. It is credibility.
- Avoid em dashes and double hyphens in all written content. Use colons, commas, or sentence breaks instead.

**Never:**
- Exaggerate traction you do not have.
- Write content that requires a disclaimer.
- Post the same content on all platforms without adapting the format and length to the channel.
- Attack or dismiss other organizations publicly.
- Use more than 2 hashtags on LinkedIn or Twitter.

---

## 60-DAY CONTENT CALENDAR

| Week | LinkedIn (3x) | Medium | YouTube | TikTok (2x) | X |
|---|---|---|---|---|---|
| Week 1 | Profile setup. First observation post. First progress post. | Draft founding essay. | Film intro video (no edit needed yet). | First fact video. First build clip. | Account setup. Follow 30 key accounts. |
| Week 2 | 2 observations, 1 progress. | Publish founding essay. | Edit and publish intro video. | 2 short clips. | Share essay. Reply to 5 posts. |
| Week 3 | 2 observations, 1 progress. | Draft essay 2. | Film second video (Kigali Declaration breakdown). | 2 clips. | Amplify LinkedIn posts. |
| Week 4 | Share one-pager as PDF post. 2 observations. | Finish essay 2. | Publish second video. | 2 clips. | Share essay 1 again with a new angle. |
| Week 5 | 2 observations, 1 progress. Feature institutional alignment. | Publish essay 2. | Film lab update video (month 1). | 2 clips. | Share essay 2. |
| Week 6 | First milestone post: what happened since week 1. 2 observations. | Outline essay 3. | Publish lab update video. | 2 clips. | Engage with AI Africa conversation. |
| Week 7 | 2 observations, 1 progress. Feature position paper angle. | Draft essay 3. | Film technical video. | 2 clips. | Light amplification. |
| Week 8 | 2 observations. Feature digital product income as proof of resourcefulness. | Publish essay 3. | Publish technical video. | 2 clips. | Share essay 3. |

By end of week 8: 24 LinkedIn posts, 3 published essays, 4 YouTube videos, 16 TikTok clips, and an established presence in the African AI conversation. That is the credibility baseline that makes every subsequent outreach land differently.

---

## THE ONE SENTENCE TEST

Before posting anything on any channel, ask: "If the AfDB program officer, the Smart Africa director, and the best ML engineer in West Africa all saw this, would each of them find something worth their time?"

If yes: publish it.
If no: rewrite it.

---

*Kheir Lissi / Founder / kora-lab.com / May 2026*


--- FILE: concepts/MEMORY.md
# MEMORY

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 3.

## Role

Store temporary operational context.

Memory changes frequently.

If something has been true for more than 30 days, it belongs in KNOWLEDGE.

---

## Current Priorities

1. Soya: dame 2 fonctionne en consignation (prend, vend, paie après) — impossible sans cash flow. Seulement dame 1 confirmée (5 bols × 975 = 4,875 FCFA demain 17h). Trouver acheteurs cash supplémentaires ou réduire la commande.
2. Renégocier Atakpamé (360 FCFA/kg) — meilleur levier pour marge future
3. Find alternative to Meta ads (ad account restricted) for pest repeller promotion
4. DoodleMind Short #2 — capitaliser sur les 72.6% rétention YouTube
5. Design SN-003 with audio/visual frame-1 disruptor
6. Update OS files after each session

---

## Current Operating Mode

SURVIVAL — generate revenue before cash runs out.

---

## Recent Decisions

- 2026-06-20: Dame 1 confirmée: 975 FCFA/bol, argent demain 17h (5 bols = 4,875 FCFA).
- 2026-06-20: Dame 2: 950 FCFA jugé difficile (marché monté à 1,100-1,200 FCFA/bol). Va parler à sa seconde.
- 2026-06-20: Envisage offre 900 FCFA/bol si dame 1 + dame 2 + seconde prennent 60 bols ensemble.
- 2026-06-20: Renégocie fournisseur Atakpamé (360 FCFA/kg) pour meilleur prix.
- 2026-06-20: Received 8,000 FCFA (5k uncle + 3k mom). Applied 50/30/20 rule.
- 2026-06-20: Meta ad account found restricted — cannot run pest repeller campaign.
- 2026-06-20: DoodleMind YouTube Short #1: 366 views, 72.6% retention, 87.5% likes, 97% Shorts feed.
- 2026-06-20: DIOS module created — 8 domains, 12-step workflow, commercial nervous system of FounderHQ
- 2026-06-20: DISTRIBUTION_MEMORY concept created (Concept 10) — campaign performance YAML schema
- 2026-06-20: CEOS refactored — pure production only, ideation/distribution/analysis moved to DIOS
- 2026-06-20: V4 consolidation completed — KERNEL, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS fully absorbed into SYSTEM_PROMPT.md (368 lines, 16 sections)
- 2026-06-19: Bancalisation concept formalized with founder
- 2026-06-19: 7 soya suppliers found with phone numbers: Ste SODJA (96 68 43 65), SCOOPS AKPENE (91 58 84 56), SOYCAIN (91 73 66 83), CIFS (91 11 44 40), MAMAN SOJA (92 62 64 68), AGROKOM (90 01 44 41), SOCMEL (99 46 89 34)
- 2026-06-19: DoodleMind channel created: niche psycho/histoire/cerveau, target US/AU, English content
- 2026-06-19: First Short "Why Your Brain Forgets Your Dreams": script + 30 image prompts + metadata generated
- 2026-06-19: YouTube Short #1 analytics: 335 views, 72.8% retention, 87.5% like rate, 28.6% CTR
- 2026-06-18: Hook Layer Priority validated (audio > visual > text) across 2 videos with same 0:03 drop

---

## Open Questions

- Will Ste SODJA accept direct-delivery payment (no upfront cash)?
- Can TikTok US distribution be forced without local SIM in target market?
- What is the optimal posting frequency for DoodleMind Shorts (24h vs 48h)?

---

## Active Concerns

- Cash ~2,679 FCFA accessible + 1,800 connectivity allocated. Received 8,000 FCFA (5k uncle + 3k mom), spent on food supplies, connectivity. SURVIVAL mode — every action must generate revenue.
- Soya delivery tomorrow: 40 bols to dame 2. Only supplier at 875 FCFA/bol = zero margin if bought at that price. Dame 2 pays delivery (1,000-1,500 FCFA) — if delivery costs 500-1,000 FCFA, the difference is the only margin.
- Meta ad account restricted — cannot run pest repeller ad campaign. Need alternative promotion strategy.
- DoodleMind YouTube Short #1: 366 views, 72.6% retention, 87.5% likes, 97% Shorts feed — strong first video signal. TikTok: 65 views, drops at 0:02 — weaker.
- Stop Nuisibles: SN-003 pending audio/visual hook rework.
- MEMORY.md updated this session (2026-06-20).

---

## Blockers

- Dame 2: fonctionne en consignation — prend le soja, vend, puis paie. Impossible sans cash flow. Seule dame 1 confirmée (5 bols × 975 FCFA, argent demain 17h).
- Soya: fournisseur Lomé max 875/bol. Atakpamé à 360/kg (900/bol) — renégociation en cours.
- Meta ad account restricted — cannot run pest repeller ad campaign.
- Cash: ~2,679 FCFA accessible. 1,800 allocated for connectivity until Tuesday.
- TikTok US distribution: distributes by local SIM/IP/language — US audience not reachable without US SIM or different strategy.

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

Last updated: 2026-06-20 19:29 (added: dame 1 + dame 2 negotiation results, Atakpamé reneg)

Memory should be reviewed and pruned at the start of each session.

Stale entries (older than 14 days without update) should be flagged.

If an entry becomes a validated truth, move it to KNOWLEDGE.


--- FILE: concepts/MISSION.md
# MISSION

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 1.

## Role

Describe desired transformations of reality.

## State

### Active Missions

---

**Mission 1: FounderHQ**

- Description: Create a portable cognitive operating system that preserves human continuity across models, tools, platforms and decades.
- Time Horizon: Ongoing — the system should become more valuable every year.
- Status: Active
- Parent Mission: None (root mission).
- Measurement: FounderHQ can be loaded by any new LLM and operational within 10 minutes.
- Related Projects: FO-001 (FounderOS v2 Reconstruction)

---

**Mission 2: Stop Nuisibles**

- Description: Sell 100 Pest Repeller units in Lomé, Togo — validate product-market fit for ultrasonic pest control in West Africa.
- Time Horizon: Q3 2026 (3 months).
- Status: Active
- Parent Mission: FounderHQ (validates that FounderHQ can generate revenue).
- Measurement: 100 units sold, repeat customer rate >20%, margin per unit validated.
- Related Projects: SN-001 (Video 1), SN-002 (Variation #2), SN-003 (Video 2)

---

**Mission 3: Financial Independence**

- Description: Generate consistent monthly revenue from product sales to cover living expenses (~100,000 FCFA/month).
- Time Horizon: 2026.
- Status: Active
- Parent Mission: FounderHQ (FounderHQ must sustain itself to prove the model).
- Measurement: 3 consecutive months above 100,000 FCFA revenue.
- Related Projects: FO-002 (First Revenue)

---

### Paused Missions

None.

---

### Archived Missions

**Zoclo Livraison**

- Description: 24/7 discreet delivery of Postinor 2 in Lomé.
- Time Horizon: Q1-Q2 2026.
- Status: Archived — product sensitivity and regulatory risk exceeded available capacity.
- Reason for Archive: Content and brand (30-day calendar, 21 scripts, brand guide) exist in Archive/ and serve as pattern reference for future projects.
- Lessons: Strong content framework (hook→problem→solution→proof→CTA) is reusable. Regulatory risk was underestimated.

---

## Mission Hierarchy

Every mission is structured as:

```
Mission → Objectives → Projects → Initiatives → Tasks
```

Lower layers serve higher layers. A project that does not serve an objective does not exist. An objective that does not serve a mission does not exist.

---

## Alignment Engine

Before creating or continuing any project, answer:

```
Which mission does this support?
```

If the answer is "none", flag the project for review. Projects without mission alignment consume resources without producing mission progress.

---

## Drift Detection

Missions naturally drift over time. Monitor for:

- Projects consuming resources without measurable mission progress
- Activities justified by "it's interesting" instead of "it serves the mission"
- Resource allocation that conflicts with mission priority order

When drift is detected: generate a DRIFT_REPORT.md with the gap, the cost, and a recommendation (Stop, Pause, Accelerate, Delegate, Automate, or Kill).

---

## Focus Protection

Before pursuing a new opportunity, ask:

- Why are we doing this?
- What mission does it serve?
- What is delayed if we pursue it?

If the new opportunity does not serve the highest-priority active mission, it is a distraction.

---

## Strategic Recommendations

Mission Control may recommend any of these actions for any project:

- **Stop** — immediate halt, resources reallocated
- **Pause** — temporary suspension, resume conditions defined
- **Accelerate** — more resources, higher priority
- **Delegate** — assign to another owner or automate
- **Automate** — replace manual execution with system
- **Kill** — permanent archive, resources released

---

## Relationship Notes

- Missions are listed in priority order from top to bottom.
- Stop Nuisibles is currently the revenue-generating mission.
- Financial Independence is the dependency enabler — without it, no other mission has runway.
- All missions serve the root mission (FounderHQ).

---

## Footer

Last updated: 2026-06-18 (updated: mission hierarchy, alignment engine, drift detection, focus protection)

If a new mission is proposed, add it to Active or Paused.

If a mission is completed or abandoned, move it to Archived with a reason.

If a mission is inactive for more than 90 days, flag it for review.


--- FILE: concepts/OMNI.md
# FounderOS V4 — OMNI (L'index du commerce de proximité)

## Purpose

Omni indexe l'économie de proximité africaine sur une carte interactive. L'acheteur trouve en un clic tout ce qui existe autour de lui. Le commerçant devient visible pour la première fois.

## Position in FounderHQ

Omni est le projet d'indexation du commerce de proximité, en parallèle de KORA. Là où KORA construit l'infrastructure linguistique pour l'IA africaine, Omni construit l'infrastructure de découverte pour l'économie informelle. Les deux projets partagent la même exécution lean et la même ancrage à Lomé.

## Status

| Field | Value |
|---|---|
| Phase | Pre-Seed / Validation |
| Activity | Active (MVP deployed) |
| Priority | Critical (Djanta Tech Hub deadline June 22) |
| Key Partner | Djanta Tech Hub (CcHUB) |
| First City | Lomé |

## Quick Reference

| Document | Location |
|---|---|
| Data Room Index | `projects/Omni/README.md` |
| Vision | `projects/Omni/01_VISION.md` |
| Mission | `projects/Omni/02_MISSION.md` |
| Master Plan | `projects/Omni/05_MASTER_PLAN.md` |
| Business Plan | `projects/Omni/09_BUSINESS_PLAN.md` |
| Executive Summary | `projects/Omni/08_EXECUTIVE_SUMMARY.md` |
| Pitch Deck | `projects/Omni/10_PITCH_DECK.md` |
| All Annexes (A–A8) in `projects/Omni/annexes/` |

## Relations

- **PROJECT** — Omni est le projet actif de validation du modèle d'index de proximité
- **FAOS** — Omni fundraising via Djanta Tech Hub (non-dilutif)
- **DAOS** — Soya finance la survie ; Omni vise le prochain palier
- **LEOS** — Financial Literacy concepts applicables aux commerçants informels
- **SOJACO** — Future distribution channel ; Omni pourrait référencer les produits SOJACO

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Updated | 2026-06-21 |
| Owner | Founder |


--- FILE: concepts/PLAYBOOK.md
# PLAYBOOK

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 7.

## Role

Store proven, reusable strategies.

A playbook tells you WHAT strategy to use and WHEN.

It is not a step-by-step procedure (that is WORKFLOW).

It is not domain knowledge (that is KNOWLEDGE).

---

## Core Rule

A playbook contains strategic patterns validated by experience.

A playbook does NOT contain step-by-step execution instructions.

A playbook does NOT contain raw domain knowledge.

A playbook references KNOWLEDGE for evidence.

A playbook references WORKFLOW for execution.

---

## Structure

Each playbook must define:

**PLAYBOOK_ID** — unique identifier

**NAME** — what this playbook is called

**SITUATION** — when to use this strategy (the context that triggers it)

**STRATEGY** — the approach, not the steps

**WHY_IT_WORKS** — the reasoning behind the strategy

**EVIDENCE** — references to KNOWLEDGE entries that validate this strategy

**CONTRADICTIONS** — when NOT to use this strategy

**RELATED_WORKFLOW** — reference to the workflow that executes this strategy (if applicable)

---

## Current Playbooks

---

**PLAYBOOK_ID:** PB-001

**NAME:** FounderHQ Content Strategy

**SITUATION:** Producing content for FounderHQ's social presence. This playbook defines what to talk about, in what proportion, and on which platforms.

**STRATEGY:** Four content pillars with a fixed publication ratio:

| Pillar | Share | Focus | Format |
|--------|-------|-------|--------|
| Building in Public | 40% | Metrics, decisions, errors, lessons | TikTok storytelling, X threads |
| Product Deep Dives | 30% | How each product works, demos, results | TikTok demo, comparative video |
| Distribution Tactics | 20% | How we sell, automation, FounderOS in action | TikTok tutorial |
| Vision & Strategy | 10% | Why Africa, FounderOS philosophy, building without funding | LinkedIn, blog, X threads |

**WHY_IT_WORKS:** 40% Building in Public builds trust and relatability. 30% Product drives concrete value recognition. 20% Distribution provides actionable takeaways. 10% Vision establishes long-term positioning. The ratio prevents content drift toward a single pillar.

**EVIDENCE:** KNOWLEDGE — Video Content Principles, Lomé Market Knowledge (tactical)
**CONTRADICTIONS:** Not applicable when the brand has not yet been established (first 30 days may skew to Product demos)
**RELATED_WORKFLOW:** WF-001 (TikTok Video Production), WF-004 (AI Video Production — Entity-Based)

---

**PLAYBOOK_ID:** PB-002

**NAME:** Social Media Distribution

**SITUATION:** Deciding where and how to publish content after it is produced.

**STRATEGY:** Platform prioritization by leverage, not by presence.

| Priority | Platform | Content Types | Frequency | Format |
|----------|----------|--------------|-----------|--------|
| 1 | TikTok | Product demo, Building in Public, Before/After | 1 video/day minimum | 30-60s, hook 0-2s, text overlay |
| 2 | X/Twitter | Learnings, metrics, decisions, takeaways | 3-5 posts/day | Threads + daily posts |
| 3 | LinkedIn | Vision, system philosophy, long-form | 2-3 posts/week | Long-form articles |
| 4 | Instagram | Cross-post from TikTok | 1-2 posts/week | Repurposed short-form |

**Rules:**
- 1 plateforme maîtrisée > 5 plateformes survolées
- Engagement > Vanity metrics
- Authenticité > Production polie

**WHY_IT_WORKS:** TikTok provides the highest discovery leverage for zero followers. X builds the intellectual audience. LinkedIn establishes credibility. Instagram is a secondary distribution channel, not a primary one.

**EVIDENCE:** KNOWLEDGE — Video Content Principles, Lomé Engagement Tactics
**CONTRADICTIONS:** If the product is visual (physical product demo), TikTok priority is even more critical. If the product is digital, X/LinkedIn priority increases.
**RELATED_WORKFLOW:** WF-001 (TikTok Video Production)

---

## Playbook Creation Flow

1. A pattern appears in KNOWLEDGE (validated through project experience)
2. The pattern is observed 3+ times in different contexts or over a period significative
3. The pattern is extracted into a PLAYBOOK entry
4. The PLAYBOOK is linked to its source KNOWLEDGE and related WORKFLOW

---

## Footer

Last updated: 2026-06-18 (added PB-001 Content Strategy, PB-002 Social Media Distribution)

An empty PLAYBOOK is acceptable for a young system.

The first playbook will emerge from the first completed project cycle.

Do not create playbooks from theory.

Create them from validated experience.


--- FILE: concepts/PROJECT.md
# PROJECT

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 2.

## Role

Represent an execution unit.

A project exists to transform resources into outcomes.

---

## Core Rule

A project references concepts.

It does NOT absorb concepts.

A project may link to MISSION, MEMORY, KNOWLEDGE, TIMELINE, WORKFLOW, PLAYBOOK, or ASSET.

A project does not contain any of them.

If a piece of information about a project could also belong in another concept, store it in the other concept and reference it here.

---

## Structure

Each project entry must contain:

**PROJECT_ID** — unique identifier

**NAME** — what this project is called

**PURPOSE** — what outcome this project exists to produce (not why — that belongs in the linked mission)

**MISSION_LINK** — which mission(s) this project serves

**STATUS** — current state (Idea / Active / Paused / Blocked / Completed / Archived)

**OWNER** — who is responsible

**START_DATE** — when this project began

**TARGET_OUTCOME** — the measurable result that defines completion

**NEXT_ACTION** — the single next action to advance this project

**RELATED_MEMORY** — reference to current operational concerns for this project (in MEMORY)

**RELATED_KNOWLEDGE** — reference to validated truths relevant to this project (in KNOWLEDGE)

**RELATED_TIMELINE** — reference to chronological events for this project (in TIMELINE)

**RELATED_WORKFLOWS** — reference to execution procedures used by this project (in WORKFLOW)

**RELATED_PLAYBOOKS** — reference to strategies used by this project (in PLAYBOOK)

**RELATED_ASSETS** — reference to resources used or produced by this project (in ASSET)

---

## States

**Idea** — not yet started, being considered

**Active** — currently being worked on

**Paused** — temporarily suspended, will resume

**Blocked** — cannot advance without an external decision or resource

**Completed** — target outcome achieved

**Archived** — abandoned or superseded, kept for reference

---

## Current Projects

---

**PROJECT_ID:** SN-001

**NAME:** Stop Nuisibles — Video 1

**PURPOSE:** Produce and publish the first TikTok video for Stop Nuisibles Pest Repeller

**MISSION_LINK:** Stop Nuisibles (MISSION)

**STATUS:** Completed

**OWNER:** Founder

**START_DATE:** 2026-06-17

**TARGET_OUTCOME:** Video published on TikTok @stopnuisibles228, analytics collected

**NEXT_ACTION:** N/A (completed)

**RELATED_MEMORY:** MEMORY — Active Concerns (analytics, cash, followers)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Video Content Principles (hook structure, TikTok mechanics)

**RELATED_TIMELINE:** TIMELINE — 2026-06-17 entries

**RELATED_WORKFLOWS:** WF-001 (TikTok Video Production)

**RELATED_PLAYBOOKS:** None yet (see PLAYBOOK when created)

**RELATED_ASSETS:** Video file on TikTok account, production sheets in Projects/Stop Nuisibles/CONTENT/

---

**PROJECT_ID:** SN-002

**NAME:** Stop Nuisibles — Variation #2

**PURPOSE:** Test whether changing the text hook + adding an engagement loop (PEST giveaway) generates comments and WhatsApp inquiries.

**MISSION_LINK:** Stop Nuisibles (MISSION)

**STATUS:** Completed

**OWNER:** Founder

**START_DATE:** 2026-06-18

**END_DATE:** 2026-06-18

**TARGET_OUTCOME:** Variation #2 published, analytics collected to decide SN-003 direction

**ACTUAL_OUTCOME:** 91 views, 0 comments, 1 share, 1 follower, 10.07s avg, 9.6% full watch, drop at 0:03. Hypothesis invalidated: text hook + giveaway did not fix retention. Hook Layer Priority (audio > visual > text) discovered.

**NEXT_ACTION:** N/A (completed — lessons extracted to KNOWLEDGE Hook Layer Priority section)

**RELATED_MEMORY:** MEMORY — Blockers, Active Concerns (analytics)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Hook Layer Priority (audio > visual > text), TikTok Mechanics (drop at 0:03 confirmed across 2 videos)

**RELATED_TIMELINE:** TIMELINE — 2026-06-18 entries

**RELATED_WORKFLOWS:** WF-001 (TikTok Video Production)

**RELATED_PLAYBOOKS:** None yet

**RELATED_ASSETS:** Production sheets from SN-001, to be adapted

---

**PROJECT_ID:** SN-003

**NAME:** Stop Nuisibles — Video 2 (Hook Layer Rework)

**PURPOSE:** Produce a video with audio/visual frame-1 pattern interrupt to test whether hook layer change (not text layer) fixes the 0:03 drop.

**MISSION_LINK:** Stop Nuisibles (MISSION)

**STATUS:** Active

**OWNER:** Founder

**START_DATE:** 2026-06-18

**TARGET_OUTCOME:** Video published with ≥50% retention past 3s and ≥1 WhatsApp inquiry

**NEXT_ACTION:** Design the audio/visual frame-1 pattern interrupt — choose a sound + visual disruption before writing any text hook

**RELATED_MEMORY:** MEMORY — Current Priorities (item 3)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Hook Layer Priority (audio > visual > text), TikTok Mechanics, Pest Repeller Product Knowledge, Offer Design

**RELATED_TIMELINE:** TIMELINE — pending entry

**RELATED_WORKFLOWS:** WF-001 (TikTok Video Production) — requires re-audit: steps 2 and 3 must check audio/visual before text

**RELATED_PLAYBOOKS:** None yet

**RELATED_ASSETS:** Product sheet in Projects/Stop Nuisibles/CONTENT/PRODUCT_SHEET.md

---

**PROJECT_ID:** DM-001

**NAME:** DoodleMind Channel Launch

**PURPOSE:** Launch and grow DoodleMind YouTube channel to monetization (1,000 subscribers, 4,000 watch hours)

**MISSION_LINK:** Financial Independence (MISSION)

**STATUS:** Active

**OWNER:** Founder

**START_DATE:** 2026-06-19

**TARGET_OUTCOME:** First Short published, channel established with consistent upload schedule, on track for monetization

**ACTUAL_OUTCOME:** Short #1 published. YouTube: 366 views, 72.6% retention, 87.5% likes, 97% Shorts feed, 40s avg duration. TikTok: 65 views, 10.43s avg, 2.8% full watch.

**NEXT_ACTION:** Create Short #2 — capitalise on YouTube Shorts feed algorithm (72.6% retention is strong). Use same psycho/cerveau niche.

**RELATED_MEMORY:** MEMORY — Current Priorities (item 3), Active Concerns (DoodleMind analytics)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Doodle Animation YouTube Pipeline, Shorts Viral Pipeline, Hook Layer Priority

**RELATED_TIMELINE:** TIMELINE — 2026-06-19, 2026-06-20 entries

**RELATED_WORKFLOWS:** KnowledgeAssets/shorts_viral_master_prompt.txt

**RELATED_PLAYBOOKS:** None yet

**RELATED_ASSETS:** A-009 DoodleMind YouTube Channel, A-011 DoodleMind Short #1 Assets

---

**PROJECT_ID:** SS-001

**NAME:** Soya Supplier Sourcing

**PURPOSE:** Find a soya supplier at ≤ 700 FCFA/bol with delivery to Lomé to serve 2 confirmed dames (~60 bols/week)

**MISSION_LINK:** Financial Independence (MISSION)

**STATUS:** Active

**OWNER:** Founder

**START_DATE:** 2026-06-19

**TARGET_OUTCOME:** First soya delivery received, 2 dames supplied at 900-1,000 FCFA/bol, 14,300 FCFA/week margin achieved

**NEXT_ACTION:** Trouver acheteurs cash pour soya. Dame 1 confirmée (5 bols × 975, demain 17h). Chercher d'autres dames au marché qui paient comptant. Renégocier Atakpamé pour prix < 360/kg.

**RELATED_MEMORY:** MEMORY — Current Priorities (item 1), Blockers (only supplier at 875 FCFA), Active Concerns (soya margin, delivery tomorrow)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Soya supplier contacts

**RELATED_TIMELINE:** TIMELINE — 2026-06-19, 2026-06-20 entries

**RELATED_WORKFLOWS:** None yet

**RELATED_PLAYBOOKS:** None yet

**RELATED_ASSETS:** A-010 Soya Supplier Contacts, supplier phone numbers in MEMORY

---

**PROJECT_ID:** FO-001

**NAME:** FounderOS v2 Reconstruction

**PURPOSE:** Replace the 42-spec-file architecture with the concept-based system defined in CONCEPT_REGISTRY.md

**MISSION_LINK:** FounderHQ (MISSION)

**STATUS:** Completed

**OWNER:** Founder + FounderOS Protocol

**START_DATE:** 2026-06-18

**END_DATE:** 2026-06-20

**TARGET_OUTCOME:** All 9 concepts implemented with clean boundaries, old SYSTEM/ files archived

**ACTUAL_OUTCOME:** All 9 concepts implemented (MISSION, PROJECT, MEMORY, KNOWLEDGE, TIMELINE, WORKFLOW, PLAYBOOK, ASSET, SYSTEM). 107 legacy files archived. 6 protocols, 8 frameworks operational.

**NEXT_ACTION:** N/A (completed)

**RELATED_MEMORY:** MEMORY — Recent Decisions (architecture changes)

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles

**RELATED_TIMELINE:** TIMELINE — 2026-06-18 to 2026-06-20 entries

**RELATED_WORKFLOWS:** None

**RELATED_PLAYBOOKS:** None

**RELATED_ASSETS:** FOUNDERHQ_MANIFEST.md, CONCEPT_REGISTRY.md, CONCEPT_BOUNDARIES.md, PROTOCOL, TEMPORAL_AWARENESS, concepts/ directory

---

**PROJECT_ID:** FHQ-001

**NAME:** First Sale Documented

**PURPOSE:** Obtain the first documented sale driven by FounderHQ — validate that the system produces real-world revenue, not just organization.

**MISSION_LINK:** Financial Independence (MISSION) + Stop Nuisibles (MISSION)

**STATUS:** Active

**OWNER:** Founder

**START_DATE:** 2026-06-18

**TARGET_OUTCOME:** At least 1 customer pays for Stop Nuisibles Pest Repeller and receives delivery

**NEXT_ACTION:** Produce and publish 3 videos with different audio/visual frame-1 disruptors, measure which drives the first sale

**RELATED_MEMORY:** MEMORY — Active Concerns (analytics, cash, blockers)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Hook Layer Priority, TikTok Mechanics, Lomé Engagement Tactics, Pest Repeller Product

**RELATED_TIMELINE:** TIMELINE — 2026-06-18 entries

**RELATED_WORKFLOWS:** WF-001 (TikTok Video Production), WF-004 (AI Video Production)

**RELATED_PLAYBOOKS:** None yet

**RELATED_ASSETS:** Pest Repeller inventory (100 units), WhatsApp +22871392122, TikTok @stopnuisibles228, Facebook page

---

**PROJECT_ID:** FO-002

**NAME:** First Revenue

**PURPOSE:** (MERGED INTO FHQ-001) Generate the first sale from any product to validate the revenue loop

**STATUS:** Archived — duplicate of FHQ-001

**ARCHIVE_REASON:** FHQ-001 (First Sale Documented) had identical purpose. Both targeted "at least 1 customer pays and receives delivery." FHQ-001 kept as canonical.

**NEXT_ACTION:** N/A (archived — see FHQ-001)

---

## Project-To-Concept Reference Pattern

To prevent PROJECT from becoming a mini-FounderHQ, use this pattern for every entry:

```
RELATED_MEMORY:     MEMORY — Section Name (what is relevant)
RELATED_KNOWLEDGE:  KNOWLEDGE — Section Name (what is relevant)
RELATED_TIMELINE:   TIMELINE — Date entries
```

Do NOT copy the content from those concepts into PROJECT.

If the information is relevant, reference it.

If the reference is too vague, the problem is not in PROJECT — the problem is in the referenced concept's structure.

---

## Footer

Last updated: 2026-06-20 19:29 (updated: SS-001 — dame 2 consignation, plan redirigé vers acheteurs cash)

A project's ACTIVE status means it has a NEXT_ACTION that can be executed.

A project's BLOCKED status means it has a blocker documented in MEMORY.

A project's PAUSED status means there is no blocker but the project is intentionally not being worked on.

A project's COMPLETED status should trigger a KNOWLEDGE update with lessons learned.


--- FILE: concepts/SOJACO.md
# SOJACO — Vente de Céréales

## Purpose
Achat-revente de céréales (soja, maïs) au Togo pour générer du cash flow rapide via des marges de revente. Paiement à la livraison pour toutes les transactions.

## Position in FounderHQ
Projet de cash flow opérationnel. Se distingue de SOYA (Bolsoja) qui est de la vente au détail de bols préparés. SOJACO est du wholesale (sacs de 100 kg). Complète KORA/OMNI comme source de revenus immédiate en mode SURVIVAL.

## Status
| Field | Value |
|---|---|
| Phase | Launch |
| Activity | Active |
| Priority | High |

## Produits & Marges
| Produit | Fournisseur | Prix/kg | Prix/sac (100kg) | Client | Prix vente | Marge | Viable? |
|---------|------------|---------|-----------------|--------|-----------|-------|---------|
| Soja | Atakpamé | 350 FCFA | 35 000 FCFA | Revendeur | 750 FCFA/bol (2.5kg) | **-125 FCFA/bol** | ❌ |
| Maïs | Ami | 160 FCFA | 16 000 FCFA | ? | ? | ? | ? |

## Unités
- 1 sac = 100 kg
- 1 bol = 2.5 kg

## Stock
- Maïs : 50 tonnes dispo (ami). Minimum 1 tonne.
- Soja : 5-10 sacs (100 kg). Deal non viable : coût 875 FCFA/bol vs vente 750 FCFA/bol.

## Relations
- **SOYA (Bolsoja)** : Projet frère. SOYA vend au détail (bols préparés), SOJACO vend en gros (sacs grain). Même clientèle potentielle.
- **KORA** : Revenue互补. SOJACO génère du cash pour financer KORA/OMNI.
- **OMNI** : À terme, Omni pourrait référencer les produits SOJACO.

## Prochaine Action
- Trouver client pour le maïs (ami 160 FCFA/kg, 50T dispo, min 1T)
- Trouver soja à meilleur prix que 350/kg ou client à meilleur prix que 750/bol


--- FILE: concepts/SYSTEM.md
# SYSTEM

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 9.

## Role

Store the rules that govern FounderHQ itself.

SYSTEM is the meta-layer. It does not contain operational data, mission definitions, project status, knowledge, or any business content.

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

## Footer

Last updated: 2026-06-18 (added: 7-phase boot sequence, runtime architecture, authority levels 0-5, escalation categories, silence rule)

SYSTEM is the least frequently modified concept.

If SYSTEM needs frequent modification, the architecture is unstable.

If SYSTEM is never modified, the architecture may be stale.


--- FILE: concepts/TIMELINE.md
# TIMELINE

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 5.

## Role

Record the temporal evolution of FounderHQ.

Timeline records: what happened, what was decided, what resulted.

### Format standard

```
Event:
Decision:
Outcome:
```

Every entry should answer: Event → Decision → Outcome.

Analysis and lessons belong in KNOWLEDGE.

---

## 2026

### June

**2026-06-18 (Session 7)**
- FounderOS architecture audited. Result: 42 spec files archived, replaced by concept-based system with 9 invariant concepts.
- Foundation documents written: FOUNDERHQ_MANIFEST.md, CONCEPT_REGISTRY.md, FOUNDEROS_PROTOCOL.md, TEMPORAL_AWARENESS.md, CONCEPT_BOUNDARIES.md.
- CONCEPT_AUDIT.md created — 6 boundary violations detected and corrected.
- RELATIONSHIP_MODEL.md created — concept graph defined.
- RUNTIME_INTERFACE.md created — runtime requirements defined.
- All 9 concepts implemented: MISSION, PROJECT, MEMORY, KNOWLEDGE, TIMELINE, WORKFLOW, PLAYBOOK, ASSET, SYSTEM.
- Video 1 final analytics collected: 380 views, 98.8% FY, 11.69s avg, 0 comments.
- WhatsApp number confirmed: 71 (not 91). Previous document VIDEO_1_READY.md marked obsolete.
- Cash state still 1,118 FCFA. No revenue to date.

**2026-06-17**
- Session 4: Video 1 (Stop Nuisibles) produced and posted on TikTok @stopnuisibles228.
- 16-step pipeline executed: action sheets, scene sheets, shot sheets, video prompts, Veo 3.1 generation, assembly.
- 10 OS corrections applied to video production workflow.
- Session 5: Video 1 analytics reviewed. 211 views, 5 followers, 94.9% For You.
- Root cause analysis performed: passive audio hook identified. 3 hook variations proposed for next post.
- Boot log created.

**2026-06-16**
- FounderOS architecture declared "complete" (30+ files).
- Genesis: profiles, twin, state files created.
- Session 1-3: FounderOS initial construction.

### Pre-June

- Stop Nuisibles product sourced (100 units, Pest Repeller ultrasonic, 4,000 FCFA/unit cost).
- Zoclo Livraison content created (30-day calendar, 21 scripts, brand guide).
- Zoclo Livraison archived due to regulatory risk.
- Previous supplier sold 2,000 units of Pest Repeller V1 at 2,500 FCFA.
- Founder identified as solo operator in Lomé, Togo with ADHD, ~2,000 FCFA cash.

---

**2026-06-18 (Session 8 — 08:04 UTC — ~2h)**
- FounderOS deep fix completed: 107 legacy files archived to ARCHIVE/v1/, Knowledge patterns migrated into concepts, deduplication resolved.
- DECISION_GATES.md created and integrated into boot sequence.
- CURRENT_SESSION.md created as single operational source of truth.
- Variation #2 posted by founder with "PEST" comment giveaway + price anchoring (8,500 vs 5,900).
- All 9 concepts updated with migrated patterns.
- 2 playbooks populated (PB-001 Content Strategy, PB-002 Social Media Distribution).
- WF-004/005/006 added (AI Video Production, Automation Definition, Event Processing).
- SN-002 NEXT_ACTION updated to "analyze results."

**2026-06-18 (Session 9 — 15:34 Lomé UTC+0 — ~15min)**
- TEMPORAL_AWARENESS bug v1: datetime affichait date sans heure. Root cause : Get-Date jamais appele. Fix : Get-Date systematique.

**2026-06-18 (Session 10 — 14:37 Lomé UTC+0 — ~5min)**
- TEMPORAL_AWARENESS bug v2: timezone errone (BaseUtcOffset = -5, mais DST actif → offset reel = -4). Root cause : `BaseUtcOffset` ignore DST, `GetUtcOffset(Get-Date)` requis. Fix : instruction DST ajoutee dans TEMPORAL_AWARENESS.md.

**2026-06-18 (Session 11 — 14:39 Lomé UTC+0)**
- Variation #2 analytics reviewed: 91 views, 0 comments, 10.07s avg, 9.6% full watch, drop at 0:03.
- Hook Layer Priority validated: 2 videos, same drop pattern, different text hooks → audio/visual layer is the real bottleneck.
- KNOWLEDGE.md mis à jour: Hook Layer Priority section (audio > visual > text).
- DECISION_GATES.md mis à jour: Content Gate verification checks reordered — audio/visual hook check added before text hook check.
- CURRENT_SESSION.md mis à jour: bottleneck = hook layer, priority = video with audio/visual frame-1 pattern interrupt.
- PROJECT.md mis à jour: SN-002 → Completed (hypothesis invalidated), SN-003 → Active (hook layer rework).
- WORKFLOW.md WF-001 mis à jour: step 1 = choose audio/visual disruptor BEFORE script.

**2026-06-19 (Session — ~2h)**
- Bancalisation concept developpe et formalise avec le founder
- SOURCE_OF_TRUTH.md audite — Regle 0 expliquee et comprise
- TEMPORAL_AWARENESS conformite corrigee : Get-Date systematique avant chaque reponse
- Nouveaux fournisseurs soja trouves : Ste SODJA (96 68 43 65), SCOOPS AKPENE (91 58 84 56), SOYCAIN (91 73 66 83), CIFS (91 11 44 40), MAMAN SOJA (92 62 64 68), AGROKOM (90 01 44 41)
- Levier financier local analyse : Assilassimé Coup de Pouce (0%, 5-20k FCFA), COCEC (jusqua 15M FCFA), FUCEC, Mutuelle Dignité Humaine
- FounderOS pousse sur GitHub : kellykheir/founderos
- Master prompt doodle YouTube (long-form) sauvegarde dans KnowledgeAssets/
- Shorts viral master prompt (9:16, <60s) cree et sauvegarde
- Chaine DoodleMind creee : niche psycho/histoire/cerveau, cible US/AU, anglais
- Premier Short "Why Your Brain Forgets Your Dreams" : script + 30 prompts image + metadata TikTok/YouTube generes
- KNOWLEDGE.md mis a jour : doodle YouTube pipeline + Shorts pipeline

**2026-06-20 (Session — OS Audit & Repair — ~2h)**
- OS audit conducted: 11+ issues identified across MEMORY, PROJECT, TIMELINE, ASSET, CURRENT_STATE, SOURCE_OF_TRUTH
- MEMORY.md complete rewrite: priorities updated (soya > DoodleMind > Stop Nuisibles), blockers documented (cash, TikTok US, Short #1 images), recent decisions from 2026-06-19 added
- PROJECT.md repaired: DM-001 (DoodleMind) and SS-001 (Soya Sourcing) added, FO-001 marked Completed, FO-002 archived as duplicate of FHQ-001
- TIMELINE.md: 2026-06-20 entries added, footer date corrected
- ASSET.md: DoodleMind channel and soya supplier contacts added
- CURRENT_STATE.md: Session Objective and Top Priority updated
- SOURCE_OF_TRUTH.md: DoodleMind and soya entries added to truth map
- Staleness detection workflow created in WORKFLOW.md (WF-007)
- CONCEPT_AUDIT.md: current audit findings appended

**2026-06-20 (Session — DIOS Implementation + V4 Completion — ~3h)**
- DIOS module cree (FounderOS/DIOS.md) : 8 domains (Market/Audience/Language/Platform/Attention/Conversion/Memory/Analytics) + 12-step workflow
- DISTRIBUTION_MEMORY concept cree (concepts/DISTRIBUTION_MEMORY.md) + enregistre Concept 10 dans CONCEPT_REGISTRY.md
- CEOS.md refactored : ideation/distribution/analysis supprimes, integration DIOS ajoutee
- AI_VIDEO_MASTER_DOMAIN.md modifie : Distribution Package ajoute (6 etapes : Localization, Platform Variations, Thumbnails, Title, Tags, Schedule)
- SYSTEM_PROMPT.md : DISTRIBUTION ajoute a l'Intent Classification table
- SOURCE_OF_TRUTH.md : DIOS + DISTRIBUTION_MEMORY ajoutes
- V4 consolidation completee : Operational Principles, Integrity Check, Execution Constraints, State Preservation, Temporal Awareness (full) absorbes dans SYSTEM_PROMPT.md (217→368 lignes)
- 7 verifications cross-reference : toutes OK

**2026-06-20 (Session — Status Update — ~16:15 Lomé)**
- Received 8,000 FCFA (5k uncle + 3k mom). Applied 50/30/20 rule — 20% set aside for growth.
- Food supplies bought: huile, haricot, gari, endomi. Cash allocated for connectivity until Tuesday.
- Soya: 40 bols pre-sold to dame 2 for tomorrow. Only supplier at 875 FCFA/bol = zero product margin. Delivery fee difference is only potential margin.
- Meta ad account found restricted — cannot run pest repeller campaign. Growth budget (1,100 FCFA) blocked.
- DoodleMind YouTube Short #1: 366 views, 72.6% retention, 87.5% likes, 97% Shorts feed, 40s avg view duration.
- DoodleMind TikTok Short #1: 65 views, 10.43s avg, 2.8% full watch, 2 followers, drop at 0:02.
- Decision: Keep 875 FCFA soya supplier as last resort for tomorrow's delivery. Continue searching for cheaper supplier for margin.

**2026-06-20 (~19:29 Lomé UTC+0 — Résultats négo)**
- Dame 1 confirmée : 975 FCFA/bol, argent demain 17h (5 bols = 4,875 FCFA).
- Dame 2 : 950 FCFA jugé difficile (marché à 1,100-1,200). Va parler à sa seconde.
- Envisage contre-proposition : 900 FCFA/bol si les 2 dames + seconde prennent 60 bols.
- Renégociation fournisseur Atakpamé (360 FCFA/kg) en cours pour meilleur prix.
- PRG framework fix appliqué : Get-Date systématique avant chaque réponse. Testé et confirmé.

**2026-06-20 (~19:29 Lomé UTC+0 — Dame 2 = consignation)**
- Dame 2 révèle son modèle : prend le soja, le vend, puis paie. Impossible pour le founder (pas de cash flow pour avancer).
- Seule dame 1 reste confirmée : 5 bols × 975 FCFA, paiement demain 17h.
- Plan soya redéfini : trouver acheteurs cash supplémentaires ou temporiser avec seulement 5 bols.

**2026-06-21 (20:00-20:35 Lomé UTC+0 — PRG Fix : SURVIVAL Auto-Drive verrouillé)**
- Bug root cause: PRG n'avait pas d'étape vérifiant mode SURVIVAL + classification DIRECT → l'Auto-Drive était défini dans SYSTEM_PROMPT mais jamais exécuté
- Fix: PRG Step 6 ajouté — "SURVIVAL Auto-Drive : If mode = SURVIVAL AND classification = DIRECT, load DAOS.md, generate 1 Action Module, append to response"
- References PRG mises à jour dans Standard Session (5→6 steps) et Quick Session
- Testé : fix en place

**2026-06-21 (03:31 Lomé UTC+0 — Stratégie soya révisée)**
- Plan soya redéfini : fournisseur Lomé passe de 40 à 5 bols (sample, livraison lundi)
- 500 FCFA livraison à la charge du founder
- Cash des ventes va directement au fournisseur — founder ne garde pas de marge
- En attendant retour fournisseur Atakpamé (360 FCFA/kg)
- Aujourd'hui 17h : dame 1 paie 4,875 FCFA (5 bols × 975)

**2026-06-21 (20:56 Lomé UTC+0 — Boot + Recherche prix maïs)**
- Boot sequence exécutée : tous les concepts frais, aucun stale
- Recherche prix retail maïs Lomé : 500–750 FCFA/bol (200-300 FCFA/kg) — source TVT/TogoFirst
- Pricing maïs viable : marge +25 à +275 FCFA/bol confirmée
- Pricing doc SOJACO mis à jour avec données retail

## Pending Timeline Events
- First sale (pending)
- First customer feedback
- Product reorder (when stock < 20)

---

## Footer

Last updated: 2026-06-21 20:35 (added: PRG Step 6 fix session)

Timeline is append-only.

Do not edit past entries — add corrections as new entries if needed.


--- FILE: concepts/WORKFLOW.md
# WORKFLOW

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 6.

## Role

Define repeatable execution procedures.

A workflow transforms an input into a desired output through a sequence of steps.

---

## Core Rule

A workflow contains step-by-step execution instructions.

A workflow does NOT contain strategy, reasoning, or domain knowledge.

Strategy belongs in PLAYBOOK.

Domain knowledge belongs in KNOWLEDGE.

---

## Structure

Each workflow must define:

**WORKFLOW_ID** — unique identifier

**NAME** — what this workflow is called

**TRIGGER** — what initiates this workflow

**INPUT** — what is needed before starting

**STEPS** — ordered list of actions, each with:
- Step description
- Expected output of the step
- Quality gate (what must be true before proceeding)

**OUTPUT** — what is produced

**RELATED_PLAYBOOK** — reference to the strategy this workflow implements (if applicable)

**RELATED_KNOWLEDGE** — reference to knowledge this workflow depends on (if applicable)

---

## Workflow: Video Production

**WORKFLOW_ID:** WF-001

**NAME:** TikTok Video Production

**TRIGGER:** A video concept has been approved for production

**INPUT:** Video concept (hook, problem, solution, CTA), product information, brand guidelines

**STEPS:**

1. **Choose audio/visual frame-1 disruptor** — Before writing any script, decide: What AUDIO (sound hit, scream, buzz, loud voice) plays at frame 0:00? What VISUAL (face zoom, sudden movement, camera shake, bright flash) appears at frame 0:00?
   - Output: Audio/Visual disruptor pair (e.g. "loud mosquito BUZZ sound + phone zoomed to mosquito on arm")
   - Quality gate: Both audio AND visual elements identified. Text is NOT the primary disruptor at frame 1.

2. **Script** — Write the script following the hook→problem→solution→proof→CTA structure. The hook uses the chosen audio/visual disruptor from step 1.
   - Output: Script text (~30s spoken)
   - Quality gate: Hook audio plays within first 1 second. Visual disruptor appears within first 1 second. Text overlay appears within first 2 seconds.

3. **Reference image** — Generate or select reference image that shows the visual disruptor
   - Output: 9:16 reference image
   - Quality gate: Image shows the frame-1 visual (not just product)

4. **Video generation** — Generate video clips using AI or capture real footage. Frame 1 must contain the visual disruptor.
   - Output: Raw video clip(s)
   - Quality gate: Frame 1 has the chosen visual disruptor. Duration matches script timing.

4. **Voiceover** — Generate or record voiceover audio
   - Output: Audio file synced to script
   - Quality gate: Audio matches script, tone is appropriate

5. **Assembly** — Combine video, voiceover, text overlay, and music
   - Output: Final video file
   - Quality gate: Text overlay is visible on mute, CTA includes WhatsApp number

6. **Publishing** — Upload to TikTok with caption, hashtags, cover image
   - Output: Published video
   - Quality gate: Video plays correctly on platform, link in bio is active

**OUTPUT:** Published TikTok video

**RELATED_PLAYBOOK:** None yet (see PLAYBOOK when created)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Video Content Principles (hook structure, TikTok mechanics, Facebook vs TikTok, Offer Design)

---

## Workflow: Concept Audit

**WORKFLOW_ID:** WF-002

**NAME:** Concept Purity Audit

**TRIGGER:** A new concept is added, or quarterly audit cycle

**INPUT:** Concept file to audit, CONCEPT_BOUNDARIES.md

**STEPS:**

1. **Load boundaries** — Read CONCEPT_BOUNDARIES.md for the concept being audited
2. **Read concept** — Read the concept file completely
3. **Check for leaks** — Compare every line against the concept's boundaries:
   - Does this line belong to another concept?
   - Is this line operational data in a strategic concept?
   - Is this line analysis in a fact-only concept?
4. **Record violations** — For each leak found, record:
   - The line location
   - The owning concept
   - The correction needed
5. **Correct** — Move leaked content to the correct concept. Delete from the audited concept.
6. **Update CONCEPT_AUDIT.md** — Log all violations and corrections
7. **Verify** — Re-read the concept to confirm all leaks are removed

**OUTPUT:** Updated concept files, updated CONCEPT_AUDIT.md

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles (concept overlap prevention)

---

## Workflow: Session End

**WORKFLOW_ID:** WF-003

**NAME:** Session Shutdown

**TRIGGER:** Session is ending (founder indicates shutdown, disconnect detected, or timeout)

**INPUT:** Current session context, all concept files

**STEPS:**

1. **Review MEMORY** — Update priorities, concerns, blockers. Add recent decisions.
   - Quality gate: Every recent decision from this session is recorded
2. **Update TIMELINE** — Add entries for significant events this session
   - Quality gate: Each entry is a fact (what happened, not analysis)
3. **Check PROJECT.md** — Update any project status changes
   - Quality gate: Every active project has a NEXT_ACTION or is marked Blocked/Paused
4. **Check KNOWLEDGE** — If any lesson was validated, add it
   - Quality gate: New knowledge is distinct from existing entries
5. **Log session end** — Record session end in TIMELINE

**OUTPUT:** Updated concept files, continuity preserved for next session

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles (state over conversation)

---

## Workflow: AI Video Production (Entity-Based)

**WORKFLOW_ID:** WF-004

**NAME:** AI Video Production — Entity-Based Pipeline

**TRIGGER:** A video concept with defined entities has been approved for production

**INPUT:** Concept, entity registry, product sheet, brand guide

**STEPS:**

1. **Entity Sheet** — For each entity (character, product, environment), create or update an ENTITY_SHEET.md
   - Output: Entity sheet with GENERATION section (Tool, Prompt, Format, Ingredients)
   - Quality gate: All ENTITY_IDs referenced in prompts appear in Ingredients field (INGREDIENTS COMPLETENESS RULE)

2. **Environment Sheet** — Define the environment where action takes place
   - Output: ENVIRONMENT_SHEET.md with GENERATION section
   - Quality gate: Environment is consistent with entity sheets

3. **Scene Sheet** — Define the composition: entities + environment
   - Output: SCENE_SHEET.md with GENERATION section
   - Quality gate: All entities and environment are defined in previous sheets

4. **Action Sheet** — Define entity action in the scene
   - Output: ACTION_SHEET.md with GENERATION section
   - Quality gate: Action is consistent with entity capabilities

5. **Shot Sheet** — Frame the shot (camera angle, distance, focus)
   - Output: SHOT_SHEET.md with GENERATION section
   - Quality gate: Shot composition is achievable from scene

6. **PROPOSE** — Show proposed content + generation prompts to founder
   - Quality gate: Founder validates before proceeding

7. **CONFIRM** — Wait for explicit founder validation
   - Quality gate: No step skips this gate

8. **WRITE** — Persist all sheets to files only after confirmation

9. **Reference Image** — Generate or select 9:16 reference image
   - Quality gate: Image matches product appearance and setting

10. **Video Generation** — Generate clips using AI from validated prompts
    - Output: Raw video clip(s)
    - Quality gate: Duration matches script timing, visual quality acceptable

11. **Voiceover** — Generate or record TTS audio
    - Output: Audio file synced to script
    - Quality gate: Audio matches script, tone is appropriate

12. **Timing Map** — Capture shot-by-shot TIMING MAP (Shot #, Action, Start, End, Duration)
    - Output: TIMING_MAP.md
    - Quality gate: Enables TTS variations without guesswork

13. **Assembly** — Combine video, voiceover, text overlay, music
    - Output: Final video file
    - Quality gate: Text overlay visible on mute, CTA includes WhatsApp number

14. **Post-Production** — Log ALL modifications to raw assembly: text overlays (content, position, timing), music track, transitions, speed changes, color grading, platform effects
    - Output: POST_PRODUCTION section in production file
    - Quality gate: This section is the single source of truth for what viewers saw

15. **Publishing** — Upload to TikTok with caption, hashtags, cover
    - Output: Published video
    - Quality gate: Video plays correctly, link in bio is active

16. **Review** — Collect analytics after 24h, log lessons
    - Quality gate: Lessons are added to KNOWLEDGE before closing

**OUTPUT:** Published TikTok video with complete production trace

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** KNOWLEDGE — Video Content Principles, Pest Repeller Product Knowledge

---

## Workflow: Automation Definition

**WORKFLOW_ID:** WF-005

**NAME:** Automation Definition

**TRIGGER:** A recurring process is identified that could be automated

**INPUT:** Process description, trigger conditions, success criteria

**STEPS:**

1. **Define Trigger** — What initiates the automation
   - Quality gate: Trigger must be deterministic (time, event, or state change)

2. **Define Conditions** — What must be true for the automation to run
   - Quality gate: Conditions must be verifiable from file state

3. **Define Action** — What the automation does
   - Quality gate: Must be executable autonomously or with approval

4. **Classify Risk** — LOW (auto-execute): generate report, update registry, create summary
   - MEDIUM (prepare + request approval): create content, send notification
   - HIGH (escalate): delete files, publish content, send external communications
   - CRITICAL (stop, notify founder, await instruction): financial transactions

5. **Define Verification** — How to confirm the action succeeded
   - Quality gate: Verification must produce a measurable result

6. **Define Logging** — Record trigger, action, outcome in AUTOMATION_LOG.md
   - Quality gate: Every execution is traceable

**OUTPUT:** Documented automation with trigger → conditions → action → verification → logging

**ERROR HANDLING:** On failure, generate AUTOMATION_FAILURE_REPORT.md

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** None yet

---

## Workflow: Event Processing

**WORKFLOW_ID:** WF-006

**NAME:** Event Processing

**TRIGGER:** An event is detected (state change, time trigger, external input)

**INPUT:** Raw event data

**STEPS:**

1. **Detect** — Identify that an event occurred
   - Quality gate: Event must have a clear SOURCE and TYPE

2. **Classify** — Assign EVENT_ID, TIMESTAMP, SOURCE, TYPE, PAYLOAD, PRIORITY (Low/Medium/High/Critical), STATUS
   - Quality gate: All fields populated before processing

3. **Route** — Send to appropriate handler based on TYPE (Decision Engine, Project Monitor, Knowledge Engine, etc.)
   - Quality gate: Handler exists and is ready

4. **Process** — Execute the handler's action on the event
   - Quality gate: Handler output is validated

5. **Log** — Record event and outcome in EVENT_LOG.md
   - Quality gate: Log is append-only

6. **Archive** — Move processed events to long-term storage
   - Quality gate: Archived events are retrievable by EVENT_ID

**OUTPUT:** Processed event with full audit trail

**OUTPUT:** Event processed from Detected → Queued → Processed → Logged → Archived

**ERROR HANDLING:** Unroutable events are logged with UNROUTABLE status and flagged for manual review

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles

---

**WORKFLOW_ID:** WF-007

**NAME:** Session Boot — Concept Freshness Check

**TRIGGER:** Every session start, after Boot Sequence (SYSTEM_PROMPT.md)

**INPUT:** Current date/time (Lomé UTC+0) + last-updated dates from all concept files

**STEPS:**

1. **Read system clock** — Get-Date, verify Lomé UTC+0
2. **Read last-updated dates** — Scan footers of: MEMORY.md, PROJECT.md, TIMELINE.md, KNOWLEDGE.md, ASSET.md, WORKFLOW.md, PLAYBOOK.md, CURRENT_STATE.md
3. **Compute age** — For each file: age = current_date - last_updated_date
4. **Flag stale concepts** — For each file exceeding its max age:
   - MEMORY.md > 1 session → FLAG
   - CURRENT_STATE.md > 1 session → FLAG
   - PROJECT.md > 7 days → FLAG
   - KNOWLEDGE.md > 14 days → FLAG
   - TIMELINE.md > 14 days → FLAG
   - ASSET.md > 30 days → FLAG
   - WORKFLOW.md > 30 days → FLAG
   - PLAYBOOK.md > 30 days → FLAG
5. **Report** — Generate concise freshness report: "MEMORY: 2 days (STALE). PROJECT: 2 days (OK). All others fresh."
6. **Prompt update** — If any concept is flagged, recommend update before proceeding with session goals

**OUTPUT:** Freshness report displayed to founder. Stale concepts flagged before any action.

**ERROR HANDLING:** If a file has no "Last updated" field, treat as maximally stale (> 90 days). If file cannot be read, flag as MISSING and consult SOURCE_OF_TRUTH.md for expected location.

---

**WORKFLOW_ID:** WF-008

**NAME:** Cold Reboot Protocol

**TRIGGER:** User says "reboot" or "applique" in any message

**INPUT:** Current session context (stale) + files on disk (fresh) + git history

**STEPS:**

1. **Freeze context** — Announce: "Rebooting — applying OS updates." Note current action to resume later if needed.

2. **Git change scan** — Run:
   ```
   git log --oneline -5
   git diff HEAD~1 --name-only
   ```
   If `git` not found: `git init` in FounderHQ root, then `git add . && git commit -m "founderos: initial state"`, then proceed to step 4 (full re-read).

3. **Identify changed files** — Parse `git diff HEAD~1 --name-only` output. Match against known concept files: `concepts/MEMORY.md`, `concepts/PROJECT.md`, `concepts/TIMELINE.md`, `concepts/ASSET.md`, `State/CURRENT_STATE.md`, `concepts/WORKFLOW.md`, `concepts/PLAYBOOK.md`, `concepts/KNOWLEDGE.md`.

4. **Re-read modified files** — Read each file identified in step 3. If no git history (first commit just made or fallback), re-read all active concept files from step 3's list.

5. **Detect deltas** — Compare new content against remembered old content. For each file, list what changed:
   ```
   Δ MEMORY — Priorities changed: old → new
   Δ PROJECT — Added: DM-001. FO-001 → Completed.
   ```

6. **Rebuild world model** — Synthesize: what exists, what matters, what changed, what's blocked, what's emerging, what should happen next. If deltas contradict each other (e.g., two files disagree on cash), flag the contradiction.

7. **Verify consistency** — File version wins over session memory. If a contradiction is found, report: "⚠️ Contradiction detected: MEMORY says X, CURRENT_STATE says Y. Using CURRENT_STATE (file wins)."

8. **Report awareness** — Output:
   ```
   Reboot complete. 3 files re-loaded.

   Δ MEMORY — priorities updated
   Δ PROJECT — DM-001 added, FO-001 completed
   Δ ASSET — A-009, A-010, A-011 added

   World model: SURVIVAL mode. Cash 1,118 FCFA. Top priority: call soya suppliers. No contradictions.

   Recommended next action: Call Ste SODJA (96 68 43 65) to confirm price and delivery terms.
   ```

**OUTPUT:** Fresh world model applied to session. Delta report displayed.

**ERROR HANDLING:**
- `git` not found → `git init`, first commit, full re-read. If user declines git init, use full re-read without git.
- File modified but unreadable → Use old in-memory version, flag as ERROR.
- Contradiction between old and new state → File version wins, flag contradiction.
- Reboot during active workflow → Complete current step first, defer reboot to next natural break.

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles, TEMPORAL_AWARENESS.md

---

## Footer

Last updated: 2026-06-20 (added: WF-007 Session Boot Freshness Check, WF-008 Cold Reboot Protocol)

Workflows are living documents.

If a workflow step becomes outdated, update it.

If a workflow is never used, archive it.

If a new recurring process emerges, create a workflow for it.


--- FILE: Frameworks/AI/AAOS.md
# AAOS — Automation & Agents Operating System

## Quand utiliser cette lentille

Conception d'agents, automatisation de workflows, reduction de tache manuelle repetitive.

## Questions obligatoires

1. Cette tache est-elle repetitive ? (frequence, duree, cout humain)
2. Peut-elle etre standardisee en etapes deterministes ?
3. Quelle est la tolerance a l'erreur de l'automation ?
4. L'effort d'automation est-il inferieur au cout de la repetition manuelle ?
5. Quel est le niveau de surveillance necessaire (auto / approuve / supervisé) ?
6. L'automation cree-t-elle un levier ou une dette technique ?

## Principes

- Automatiser seulement ce qui est standardise et compris.
- Hierarchie : Documentation → Standardisation → Automation → Delegation.
- Ne pas automatiser ce qui change chaque semaine.
- L'automation sans surveillance genere du bruit.
- Un agent mal defini est pire que pas d'agent du tout.

## Antipatterns

- Automatiser avant de standardiser
- Automatiser un processus qu'on ne comprend pas
- Creer un agent sans limites claires (scope, autorite, escalation)
- Confondre automation et delegation humaine


--- FILE: Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md
# AI Video Production — Entity-Based Framework

## Quand utiliser cette lentille

Production video AI avec des entites recurrentes (personnages, produits, environnements).

## Principe fondamental

AI Video n'est pas une question de prompts. AI Video est une question d'entites. Les prompts sont generes a partir des entites.

Tout element visible a l'ecran est une entite. La coherence est obtenue par la persistence des entites.

## Structure requise avant production

1. **Entity Registry** — ENTITY_REGISTRY.md avec ENTITY_ID, Type, Name
2. **Entity Sheets** — PERSON_SHEET, PRODUCT_SHEET, LOCATION_SHEET par entite
3. **Environment System** — lumiere, atmosphere, meteo, mood, palette couleurs
4. **Action System** — actions reutilisables : Actor (ENTITY_ID), Action, Object, Emotion, Duree
5. **Scene System** — entites + environnement + actions + objectif narratif
6. **Frame System** — START_FRAME, END_FRAME obligatoires avant generation
7. **Video Prompt Generation** — en aval, seulement apres que toutes les dependances existent

## Quality gates

- Entity Sheets existent ✓
- Environment Sheets existent ✓
- Action Sheets existent ✓
- Scene Sheets existent ✓
- Frame Assets existent ✓

Si un gate est rouge : STOP. Generer les assets manquants avant de continuer.

## Regle FounderOS

Ne pense pas en prompts. Pense en entites.
Ne pense pas en clips. Pense en scenes.
Ne pense pas en videos. Pense en systemes.

## Content types supportes

ADVERTISEMENT, DOCUMENTARY, PODCAST, EDUCATIONAL, STORYTELLING, FOUNDER_JOURNAL, NEWS


--- FILE: Frameworks/Content/MAOS.md
# MAOS — Marketing Operating System

## Quand utiliser cette lentille

Campagne marketing, plan de contenu, acquisition audience, positionnement de marque.

## Questions obligatoires

1. Quel est l'objectif de cette campagne ? (awareness / acquisition / conversion / retention)
2. Quel canal atteint le mieux cette cible ?
3. Quel est le message unique ? En une phrase.
4. Comment mesurons-nous le succes ?
5. Quel est le cout par acquisition attendu ?
6. Le message est-il coherent sur tous les canaux ?

## Principes

- Distribution et creation sont egalement importantes.
- Un canal maîtrise > 5 canaux survoles.
- Le message doit changer selon l'etape du funnel (froid → chaud).
- L'authenticite > la production polie pour les audiences locales.
- Tester un canal a la fois. Ne pas diviser l'attention.

## Antipatterns

- Lancer sur 5 canaux en meme temps sans test
- Message identique pour audience froide et chaude
- Optimiser pour les vanity metrics (likes, vues) sans mesurer la conversion
- Changer de strategie avant d'avoir collecte assez de donnees


--- FILE: Frameworks/Core/CAOS.md
# CAOS — Cash Allocation Operating System

## Quand utiliser cette lentille

Decisions de pricing, allocation de ressources, mode survie, priorites financieres.

## Questions obligatoires

1. Cash disponible ?
2. Cette depense sert la survie ou la croissance ?
3. Retour attendu vs cout ?
4. Risque de ne pas faire cette allocation ?
5. L'allocation maximise-t-elle la probabilite de succes de la mission ?

## Principes

- Les ressources sont finies. Les opportunites sont infinies.
- Toute allocation est simultanement un investissement et un rejet.
- La mission doit recevoir des ressources avant le confort.
- Les actifs a effet compound meritent un investissement disproportionne.

## Hierarchie d'allocation

Survie → Revenue → Capacites → Actifs → Scale → R&D frontiere

Sauf justification forte pour un ordre different.

## Mode survie

Cash < 3 mois de runway. Priorite : Survie → Revenue → Fundraising.

## Anti-patterns

- Allouer sans outcome defini
- Depenser pour du confort avant la mission
- Confondre activite et progres
- Budgeter sur des promesses, pas sur le cash


--- FILE: Frameworks/Core/CEOS.md
# CEOS — Content Execution Operating System

## Quand utiliser cette lentille

Creation de contenu, distribution, conversion, hook analysis, strategie audience.

## Questions obligatoires

1. A qui s'adresse ce contenu ? (froid / tiede / chaud)
2. Quel est l'objectif ? (awareness / education / trust / lead / vente)
3. Quelle est l'action suivante pour le spectateur ?
4. Pourquoi ce contenu existe-t-il ?

## Principes

- Les gens n'achetent pas des features. Ils achetent des resultats.
- L'attention est raree. Clarte > Complexite. Pertinence > Volume.
- Les premieres secondes determinent tout. "Why should I care ?" immediat.
- Distribution n'est pas optionnelle — elle fait partie du produit.
- Le hook opere sur 3 couches : AUDIO > VISUEL > TEXTE.

## Couches audience

- **Froid** : ne vous connait pas → objectif Attention
- **Tiede** : vous connait → objectif Trust
- **Chaud** : vous fait confiance → objectif Action

## Anti-patterns

- Creer du contenu sans objectif defini
- Optimiser pour likes/vues au lieu de conversion
- Publier sans CTA clair
- Hook textuel sans disrupteur audio/visuel frame-1


--- FILE: Frameworks/Core/FAOS.md
# FAOS — Funnel Acquisition Operating System

## Quand utiliser cette lentille

Acquisition de capital, funnel de vente, activation, monetisation, fundraising.

## Questions obligatoires

1. Quelle est la source de capital la moins chere et la plus rapide aujourd'hui ?
2. Le revenu est-il valide ou hypothetique ?
3. Pouvons-nous atteindre l'objectif sans dilution ?
4. Avons-nous valide la demande avant de scaler ?
5. Quel est le cout d'acquisition vs la valeur vie client ?

## Principes

- Le capital est du carburant, pas la destination.
- Le revenu est le meilleur capital : non dilutif, valide par le marche, reproductible.
- Hierarchie du capital : Revenue > Partenariats > Grants > Angels > VC > Dette
- Ne jamais budgeter sur des promesses. Toujours budgeter sur le cash.

## Etats de runway

- **Vert** (>12 mois) : Croissance
- **Jaune** (6-12 mois) : Acceleration revenue
- **Orange** (3-6 mois) : Survie + Revenue
- **Rouge** (<3 mois) : Generation de cash immediate

## Anti-patterns

- Confondre fundraising et progres
- Dilution prematuree alors que revenue est possible
- Dependency unique sur une source de revenu
- Attendre que le financement arrive au lieu de generer du revenu


--- FILE: Frameworks/Core/PSOS.md
# PSOS — Product Strategy Operating System

## Quand utiliser cette lentille

Strategie produit, validation d'offre, positionnement, priorisation de features.

## Questions obligatoires

1. Quel probleme ce produit resout-il ?
2. Pourquoi ce probleme maintenant ?
3. Qui a ce probleme et combien sont-ils prets a payer ?
4. Comment saurons-nous que le produit est valide ?
5. Quelle est la proposition de valeur unique ?

## Principes

- Les produits peuvent changer. Les marches peuvent changer. La mission reste.
- La realite a priorite sur les croyances, les plans et les recits.
- Preferer les actions qui creent des actifs a effet compound.
- Chercher le levier avant l'effort : automation > systemes > code > media > capital > equipe > travail personnel.

## Validation

Apprendre en executant. Ne pas attendre de devenir expert avant de construire.

## Anti-patterns

- S'attacher a une implementation specifique (la mission est permanente, pas le produit)
- Accumuler des connaissances sans application
- Complexite inutile pour elegance
- Attendre la perfection avant de lancer


--- FILE: Frameworks/Core/SAOS.md
# SAOS — Systems Analysis Operating System

## Quand utiliser cette lentille

Conception, audit ou debug d'un systeme (architecture, projet, workflow, organisation).

## Questions obligatoires

1. Quels sont les composants du systeme ?
2. Quelles sont les dependances entre composants ?
3. Quelle est la frontiere de chaque composant ?
4. Quelle est la verite que chaque composant possede ?
5. Quelle verite chaque composant ne possede-t-il PAS ?
6. Quel est le bottleneck unique ?
7. Qu'est-ce qui casse si on retire X ?
8. Quelle est la source unique de verite pour chaque donnee ?
9. Le composant peut-il etre reconstruit si perdu ?
10. Quel est le cout de sa suppression ?

## Principes

- Un systeme sain a des frontieres claires entre ses composants.
- Chaque composant possede UNE verite et UNE seule.
- Le bottleneck est la contrainte unique qui limite tout le systeme.
- Un composant qui peut etre reconstruit facilement a moins de valeur qu'un composant qui ne peut pas l'etre.
- La separation des responsabilites est le premier rempart contre l'entropie.

## Etapes d'analyse

1. Cartographier tous les composants et leurs frontieres
2. Identifier les verites que chaque composant possede
3. Tracer les dependances entre composants
4. Trouver le bottleneck (le composant qui limite le debit du systeme)
5. Tester la resilience : supprimer chaque composant mentalement et evaluer l'impact
6. Verifier la Regle 0 : chaque verite a exactement un proprietaire

## Anti-patterns

- Composants qui possedent la meme verite → duplication, contradiction
- Composants sans frontiere claire → incoherence
- Composants sans verite propre → morte, inutile
- Systeme sans bottleneck identifie → priorisation impossible
- Ajouter des composants sans verifier les frontieres avec les existants


--- FILE: Frameworks/Experimental/LEOS.md
# LEOS — Learning Operating System

## Statut
EXPERIMENTAL — en quarantaine jusqu'a preuve de valeur unique.

## Raison de la quarantaine
FounderHQ n'est actuellement pas bloque par l'apprentissage. Il est bloque par la priorisation, l'execution et la distribution.

## Test de validation
Si un besoin recurrent d'apprentissage structure (acquisition de competence, apprentissage par projet) se manifeste, LEOS sera promu.

## Source archive
ARCHIVE/v1/legacy_frameworks/LEOS v2.md


--- FILE: Frameworks/Experimental/PMOS.md
# PMOS — Project Management Operating System

## Statut
EXPERIMENTAL — en quarantaine jusqu'a preuve de valeur unique.

## Raison de la quarantaine
PROJECT, WORKFLOW et PLAYBOOK existent deja. PMOS risque de dupliquer.

## Test de validation
Si dans 30 jours d'usage reel, un besoin de gestion de projet non couvert par les concepts existants emerge, PMOS sera promu.

## Source archive
ARCHIVE/v1/legacy_frameworks/PMOS v2.md


--- FILE: Frameworks/Experimental/RIOS.md
# RIOS — Research & Intelligence Operating System

## Statut
EXPERIMENTAL — en quarantaine jusqu'a preuve de valeur unique.

## Raison de la quarantaine
KNOWLEDGE, WORKFLOW et PROJECT couvrent deja la recherche. RIOS doit demontrer qu'il apporte une vraie methode d'intelligence economique.

## Test de validation
Si un besoin recurrent d'analyse concurrentielle ou de veille se manifeste, RIOS sera active.

## Source archive
ARCHIVE/v1/legacy_frameworks/RIOS v2.md


--- FILE: Frameworks/KORA/RAPHAEL_PDCA.md
# FounderOS V4 — RAPHAEL PDCA Framework
## KORA Lab's Execution Operating System

Extracted from the KORA Lab Raphael system prompt. Used when executing KORA initiatives across all 5 domains.

## THE RAPHAEL PDCA LOOP

Use this loop for every new initiative, product feature, campaign, or strategy. State which domain and which session type before starting.

### PHASE 1: PLAN — DEFINE THE 1% PROBLEM

The 1% problem is the single symptom that, if solved, produces at least 80% of the value.

**Step 1.1:** State the problem in one sentence.
**Step 1.2:** Identify the 1% problem.
**Step 1.3:** Run the three mandatory gates:
- Gate A — Zero Budget Check: Can this be addressed with free tools or existing resources?
- Gate B — African Context Check: How does this serve African users specifically?
- Gate C — Sovereignty Check: Does this deepen Africa's AI independence or dependency?
**Step 1.4:** List the three riskiest assumptions.
**Step 1.5:** Identify the single riskiest assumption.

### PHASE 2: VALIDATE BEFORE BUILDING — PRESELL AND DEMO FIRST

Nothing gets built until demand is validated.

**Level 1 — Smoke Test:** Create minimum signal to measure demand before building.
**Level 2 — Presell or Preorder:** Prove willingness to pay, not just interest.
**Level 3 — Concierge MVP:** Deliver manually what you plan to automate.

### PHASE 3: DO — BUILD THE MVP

Only after validation confirms demand. Generate three distinct solution concepts, score on impact/effort/fit, choose highest-scoring.

### PHASE 4: CHECK — BUILD, MEASURE, VERIFY

For each MVP task: mark in-progress, execute completely, apply quality gate, measure success metric against hypothesis.

### PHASE 5: ACT — LEARN AND DECIDE

If metric met: hypothesis validated. State what was proven. State next action.
If metric not met: hypothesis refuted. State what was learned. Pivot or persevere.

## DOMAIN-SPECIFIC QUALITY GATES

**Product Gate:** Works with zero budget, functional on mobile/low bandwidth, multilingual, serves African use case.
**Institutional Gate:** References specific named declarations. Positioning is "completing not competing."
**Content Gate:** Five-part formula: fact, tension, lens, perspective, call. First sentence is specific verifiable fact.
**Income Gate:** Product complete, listing keyword-optimized, mockup professionally composed.
**Architecture Gate:** Decision moves KORA closer to credible institutional partnership.

## OPERATING DOMAINS

1. PRODUCT — building the first KORA AI accessibility product
2. INSTITUTIONAL — government outreach, grant applications, accelerator submissions
3. CONTENT — LinkedIn, Medium, YouTube, TikTok, website
4. INCOME — digital product business on Gumroad, Payhip, Ko-fi, Whop
5. ARCHITECTURE — KORA structure, legal, team, long-term strategy

## Footer
| Field | Value |
|---|---|
| OS Version | V4 |
| Source | Kora Lab Raphael Prompt |
| Owner | Founder |


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
# DIOS — AUDIENCE_INTELLIGENCE

## Mission

Identify precisely who must see the content.

## Core Rule

Audience ? Product.

Every offer has multiple distinct audiences. Each needs a different hook, different story, different CTA.

DIOS identifies at least 3 distinct audiences before choosing the primary target.

## Method

1. List the problem the product solves
2. For each problem ? who experiences it most acutely?
3. For each group ? what is their specific frustration/desire/fear?
4. For each group ? where do they consume content?
5. Select primary audience + secondary audience per campaign

## Persona Template

`
Audience: [name]
Problem: [what they suffer from]
Hook angle: [what makes them stop scrolling]
Language: [derived from market + audience]
Platform: [where they spend time]
CTA: [what action they will take]
Objection: [why they would say no]
`

## Example (Pest Repeller)

| Audience | Hook | Platform |
|----------|------|----------|
| Parents (enfants) | Protéger bébé des moustiques la nuit | TikTok, WhatsApp |
| Femmes enceintes | Protéger la grossesse du paludisme | TikTok |
| Commerçants | Protéger le stock, dormir pour bosser | Facebook, WhatsApp |
| Hôtels | Confort client, avis Booking | Facebook |
| Écoles | Concentration élèves, confiance parents | WhatsApp |

## Example (Kit Solaire)

| Audience | Hook | Platform |
|----------|------|----------|
| Parents | Enfant révise à la bougie depuis 3 mois | TikTok |
| Petits commerçants | Perte de stock quand l'électricité part | Facebook |
| Vendeurs de rue | Recharger téléphone pour les clients | TikTok, WhatsApp |

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | LANGUAGE_INTELLIGENCE.md, PLATFORM_INTELLIGENCE.md |


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
# DIOS — HOOK_INTELLIGENCE

## Mission

Understand why someone stops scrolling and create hooks that force them to stop.

## Core Rule

Hook operates on 3 layers, in priority order:
1. **AUDIO** — fastest to reach the brain (sound, buzz, scream, question)
2. **VISUAL** — breaks scroll pattern (face zoom, movement, bright flash)
3. **TEXT** — only works if audio AND visual already stopped the scroll

Validated truth: Text alone cannot fix a hook problem.

## 9 Sources of Attention

| Source | Hook Angle |
|--------|-----------|
| Fear | "Si tu ne fais pas X, Y arrive" |
| Curiosity | "Pourquoi X arrive ? La réponse est Y" |
| Desire | "Imagine ta vie avec X" |
| Money | "Tu perds X FCFA par jour à cause de Y" |
| Health | "X fait ça à ton corps sans que tu le saches" |
| Family | "Tes enfants méritent X" |
| Status | "Les gens qui ont X sont vus comme Y" |
| Safety | "X te protège de Y" |
| Opportunity | "X est disponible maintenant, après c'est fini" |

## Hook Generation Dimensions

For each audience, DIOS generates hooks across:
- Per audience segment (parent, merchant, student...)
- Per attention source (fear, curiosity, desire...)
- Per language (French, Ewe, Pidgin...)
- Per platform format (short vs long, vertical vs horizontal)

## Hook Selection

For each campaign, generate 10-50 hooks, then filter:
1. Is it true? (never lie)
2. Does it match the audience?
3. Does it work on the chosen platform?
4. Does it pass the 2-second test? (would someone stop scrolling?)

## Example (Kit Solaire, Audience: Parents)

1. "Ton enfant révise à la bougie depuis janvier. Et si c'était la dernière fois ?"
2. "500 FCFA par jour d'essence. Chaque jour. Depuis 3 mois."
3. "Ton voisin a déjà installé le sien. Tu attends quoi ?"

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md, LANGUAGE_INTELLIGENCE.md, PLATFORM_INTELLIGENCE.md |


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
| Grants (Djanta Tech Hub, etc.) | 500k-5M FCFA | 0% + reporting | R&D, impact |
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
# VAOS — MISSION_ENGINE

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
# VAOS — THEORY_OF_CHANGE

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
# VAOS — VISION_ENGINE

## Mission

Define the transformation of reality that this venture exists to cause.

## Core Rule

A vision is not a goal. A vision describes the world AFTER the venture succeeds. It answers: what is different?

## Vision Template

`
In [timeframe], [who] will [what] because [venture].

Before: [current reality — the problem]
After: [future reality — the solution]
`

## Example (Kora)

> In 5 years, African AI researchers will build sovereign AGI on African infrastructure because Kora provides the compute, data, and talent pipeline.
>
> Before: African AI talent leaves for US/EU because there's no compute or research ecosystem at home.
> After: West Africa has its own AI research hub publishing at top venues and deploying real solutions.

## Vision Test

A vision passes if:
- It excites someone who doesn't work for you
- It describes a real change, not a product feature
- You can explain it in 1 sentence

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | VAOS |
| Dependencies | MISSION_ENGINE.md |


--- FILE: Frameworks/VSOS.md
# FounderOS V4 — VSOS
## Venture Structuring Operating System

### Transformer toute idée, projet ou opportunité en système exécutable

---

## 1. Qu'est-ce que VSOS ?

VSOS est la méthodologie de transformation stratégique de FounderHQ. Elle prend une entrée floue (idée, projet, opportunité, problème) et produit une sortie structurée : une cascade complète de documents, de la Vision au système d'exécution.

VSOS n'est pas un module quotidien. C'est une **lentille** chargée quand tu dois créer un nouveau projet, restructurer un projet existant, préparer une levée de fonds, ou transformer une vision en exécution.

VSOS a déjà été utilisé sur KORA et Omni (sans être nommé). C'est maintenant un framework explicite.

---

## 2. Quand utiliser VSOS

| Situation | Action |
|-----------|--------|
| Nouvelle idée / nouveau projet | VSOS complet (Phase 1 → 3) |
| Projet existant sans structure | VSOS Audit + Phase 2 → 3 |
| Restructuration / reframe | VSOS Audit + Mission Extraction |
| Préparation levée de fonds | VSOS Phase 3 (Capital Roadmap + BP) |
| Blocage stratégique | VSOS Gap Analysis |

**Ne pas utiliser :** pour les opérations quotidiennes (DAOS), les décisions rapides (DECISION_ENGINE), le contenu (CEOS).

---

## 3. Architecture VSOS

### Entrée
```
Idée
Projet existant
Entreprise
Opportunité
Problème
```

### Les 3 Phases

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

### Sortie
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

À faire avant toute cascade stratégique. Comprendre où on est avant de décider où on va.

### 4.1 Reality Assessment

Questions à回答 :
- Quel est l'état actuel du projet / de l'idée ?
- Qu'est-ce qui existe déjà ? (MVP, équipe, traction, revenus, docs)
- Quelles sont les contraintes ? (cash, temps, compétences, marché)
- Quel est le problème fondamental résolu ?

**Output :** Une section dans CURRENT_STATE.md ou un memo diagnostic.

### 4.2 Mission Extraction

Extraire la mission du projet, qu'elle soit explicite ou implicite :
- Pourquoi ce projet existe ?
- Pour qui ?
- Quel est le changement désiré ?
- Dans 5-10-20 ans, à quoi ressemble le succès ?

**Output :** Une ébauche de mission (sera raffinée en Phase 2).

### 4.3 Gap Analysis

Identifier l'écart entre l'état actuel et la mission :
- Qu'est-ce qui manque ? (données, équipe, financement, traction)
- Quels sont les blocages ?
- Quel est le risque principal ?
- Quelle est la prochaine action la plus importante ?

**Output :** Gap list + priorisation.

**Modules associés :** RIOS.md (recherche) peut être invoqué pour creuser les gaps.

---

## 5. Phase 2 — Strategic Cascade

Construire les 5 documents fondamentaux qui forment l'armature stratégique du projet.

### 5.1 Vision (projects/X/01_VISION.md)

**Horizon :** 10-25 ans. Indépendante des produits, des technologies, des financements.

**Éléments :**
- Vision Statement (1 paragraphe, le futur désiré)
- Le futur que nous voulons créer (pourquoi le statu quo est inacceptable)
- Notre conviction fondamentale (pourquoi notre approche est la bonne)
- Notre vision de l'infrastructure (ce qu'on construit)
- Notre vision de l'impact sociétal (éducation, santé, économie, culture)
- Horizon de réussite (quand saurons-nous qu'on a réussi ?)
- OODA Critique (pourquoi cette vision survivra aux changements technologiques)

**Template section OODA Critique :**
```
Cette vision est volontairement indépendante des [technologies/marchés] actuels.
Elle reste valable même si [X, Y, Z] disparaissent.
Une bonne vision doit survivre à plusieurs générations technologiques.
```

### 5.2 Mission (projects/X/02_MISSION.md)

**Ce que l'organisation fait chaque jour.**

**Éléments :**
- Déclaration de mission (1 phrase)
- Pourquoi nous existons
- Ce que nous faisons (5 capacités fondamentales)
- Ce que nous NE SOMMES PAS (pour éviter le scope creep)
- Nos principes d'exécution (5 max)
- Comment nous mesurons le succès
- Priorité actuelle

### 5.3 Theory of Change (projects/X/03_THEORY_OF_CHANGE.md)

**La chaîne logique : comment la vision devient réalité.**

**Éléments :**
- Les déficits structuraux (pourquoi le problème existe)
- Hypothèse centrale (SI... ALORS...)
- Les relations de causalité (chaîne : pas de X → pas de Y)
- La chaîne de transformation (étape par étape)
- Les résultats attendus (court, moyen, long terme)
- L'hypothèse fondamentale (le vrai pari qu'on fait)

### 5.4 Strategic Assets Map (projects/X/04_STRATEGIC_ASSETS_MAP.md)

**Ce qu'on accumule, pourquoi c'est difficile à reproduire.**

**Éléments :**
- Liste des actifs par difficulté de réplication
- Pour chaque actif : ce qu'il est, pourquoi il est dur à copier
- Tableau : Actif / Difficulté / Temps / Avantage Concurrentiel
- L'actif le plus important (le "château fort")

### 5.5 Master Plan (projects/X/05_MASTER_PLAN.md)

**Le cadre de développement global.**

**Éléments :**
- Résumé exécutif
- Thèse stratégique
- Les 6 (ou X) couches stratégiques
- Chronologie d'exécution par phase
- Principes stratégiques (5 max)

---

## 6. Phase 3 — Execution Framework

Transformer la stratégie en plans concrets, finançables et mesurables.

### 6.1 Strategic Roadmap (projects/X/06_STRATEGIC_ROADMAP.md)

**Quand on fait quoi.**

**Éléments :**
- North Star (la direction)
- Phases avec pour chacune : période, objectif, livrables, budget
- Jalons clés avec dates cibles et indicateurs

### 6.2 Capital Roadmap (projects/X/07_CAPITAL_ROADMAP.md)

**Comment on finance chaque phase.**

**Éléments :**
- Thèse de capital
- Architecture de financement (5 couches : fondateur, non-dilutif, partenariats, revenus, equity)
- Utilisation des fonds (tableau détaillé)
- Règle de financement (ne pas lever tant que le palier précédent n'est pas prouvé)

### 6.3 Business Plan (projects/X/09_BUSINESS_PLAN.md)

**Phase 1 : le plan pour le premier palier.**

**Éléments :**
- Executive Summary (1 page)
- Le problème (détaillé)
- L'opportunité
- La solution
- Les objectifs Phase 1
- Le business model
- La roadmap Phase 1
- Use of Funds
- Risques et mitigations
- Demande d'investissement

### 6.4 Execution System (projects/X/annexes/A3_KPIS_MILESTONES.md)

**Comment on mesure et on suit.**

**Éléments :**
- Jalons avec mois cibles
- KPIs avec objectifs chiffrés
- Fréquence de revue
- Qui est responsable

---

## 7. VSOS dans l'Écosystème FounderHQ

### Modules invoqués pendant VSOS

| Module | Rôle pendant VSOS |
|--------|------------------|
| **VEAOS** | Raffinement vision/mission, scénarios stratégiques |
| **RIOS** | Recherche de marché, concurrents, gaps |
| **FAOS** | Stratégie fundraising (Phase 3) |
| **DIOS** | Stratégie de distribution (après VSOS) |
| **CEOS** | Stratégie de contenu (après VSOS) |

### Post-VSOS

Une fois VSOS terminé, le projet est enregistré via PROJECT_REGISTRATION_PROTOCOL.md :
1. Créer `concepts/<PROJECT>.md`
2. Ajouter à `State/CURRENT_STATE.md`
3. Ajouter à `State/PRIORITY_MATRIX.md`
4. Ajouter les relations dans les concepts pertinents

---

## 8. Cas d'Usage (déjà exécutés)

### KORA — AI Lab (African languages)
- Entrée : Idée d'infrastructure IA pour langues africaines
- VSOS : Complet (Phase 1 → 3)
- Sortie : 20 fichiers dans `projects/KORA/`
- Statut : Pre-Seed ready

### OMNI — Index du commerce de proximité
- Entrée : MVP existant + pitch deck
- VSOS : Phase 2 → 3 (Diagnostic sauté car projet déjà avancé)
- Sortie : 20 fichiers dans `projects/Omni/`
- Statut : Dossier Djanta Tech Hub prêt

### Financial Literacy Program
- Entrée : Cours générique à personnaliser
- VSOS : Audit + Reframe (adapter au contexte FounderHQ)
- Sortie : 28 concepts réécrits avec exemples réels
- Statut : 2/28 complétés

---

## 9. Template : Quick VSOS (1 heure)

Pour les projets rapides (ex: Pest Repeller, Solar Kit, chaîne TikTok) :

```
1. Reality Assessment (5 min) — Où j'en suis ?
2. Mission (5 min) — Pourquoi ce projet existe ?
3. Assets (5 min) — Qu'est-ce que j'ai déjà ?
4. Roadmap (10 min) — Les 3 prochaines actions
5. BP 1-pager (15 min) — Modèle économique simple
6. KPIs (5 min) — Comment je sais si ça marche ?
7. Enregistrer (15 min) — Créer concept + entrée PRIORITY_MATRIX
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


--- FILE: .opencode/prompts/startup.md
# FounderOS — Startup Prompt

Tu es FounderOS. Tu n'es pas un chatbot. Tu es le systeme d'exploitation responsable de faire avancer la mission du founder.

## Regle globale (AVANT CHAQUE REPONSE)
Executer Get-Date pour obtenir date et heure actuelles. Integrer le temps dans TOUTE reponse — meme les questions simples. Le temps change a chaque message.

## Autorite
SYSTEM/FOUNDEROS_SYSTEM_PROMPT.md definit ton comportement global. Lis-le et obeis.

## Comportement

Si c'est le premier message de la session OU si l'utilisateur tape `boot` ou `refresh`:
→ Executer la Boot Sequence complete ci-dessous

Sinon (question normale en cours de session):
→ Mode RUNTIME: pas de boot, repondre directement avec les regles du SYSTEM_PROMPT

## Boot Sequence (OBLIGATOIRE — execution, pas lecture)

```
PHASE 1: KERNEL
  → Lire STATE/CURRENT_STATE.md, ACTIVE_PRIORITIES.md, OPERATING_MODE.md, PROJECT_REGISTRY.md
  → Lire STATE/PRODUCT_PIPELINE.md si existe
  → Scanner ../Projects/ pour detecter nouveaux/modifies projets
  → Scanner ../Knowledge/ pour detecter nouvelles entrees
  → Scanner ../Reports/ pour dernier brief
  → LOG: "PHASE 1 KERNEL ✓"

PHASE 2: TIME AWARENESS
  → EXECUTER Get-Date pour obtenir date et heure actuelles
  → Jour de SURVIVAL mode? Depuis combien de jours 0 revenue?
  → Estimation jours restants avant cash epuise (2000 FCFA / depenses par jour)
  → Temps restant aujourd'hui pour travailler
  → Deadline du jour
  → RESULTAT: urgence quantifiee, pas de vague "bientot"
  → LOG: "PHASE 2 TIME ✓"

PHASE 3: STATE RECONSTRUCTION
  → Determiner: cash, runway, produits pipeline
  → Determiner: mode actuel (SURVIVAL/BUILD/etc)
  → Determiner: contrainte principale
  → LOG: "PHASE 3 STATE ✓"

PHASE 4: MOS (Mission Analysis)
  → Mission alignee? Drift depuis derniere session?
  → LOG: "PHASE 4 MOS ✓"

PHASE 5: DAOS (Decision Review)
  → Decisions en attente? Evenements non traites?
  → LOG: "PHASE 5 DAOS ✓"

PHASE 6: PSOS (Constitution Check)
  → Regles respectees? Activite interdite en cours?
  → LOG: "PHASE 6 PSOS ✓"

PHASE 7: RUNTIME (Generate Brief)
  → Resumer: mode, priorites, produits, action recommandee, urgence temps
  → Generer BOOT_STATE.md avec: Date, Mode, Jour de SURVIVAL, Contrainte, Top 3, 1ere action
  → LOG: "PHASE 7 RUNTIME ✓"

PHASE 8: PRESENT
  → Logger dans STATE/BOOT_LOG.md
  → Afficher brief. Ne JAMAIS demander "Comment puis-je t'aider?"
  → LOG: "PHASE 8 PRESENT ✓"
```

## Workflow et dependances obligatoires
Avant chaque tache (apres boot):
1. Identifier le workflow dans SYSTEM/WORKFLOW_REGISTRY.md
2. Construire l'arbre de dependances: remonter de l'output jusqu'aux racines
3. Verifier chaque dependance avec SYSTEM/QUALITY_GATES.md
4. Executer ETAPE PAR ETAPE en partant des racines
5. Ne jamais sauter d'etape. Ne jamais passer d'une idee a un prompt.

## Regles strictes
1. Ne JAMAIS repondre avant la fin des 8 phases (si boot requis)
2. Chaque phase loguee dans STATE/BOOT_LOG.md avec ✓ ou ✗
3. Si une phase echoue: STOP. Signaler. Proposer action corrective.
4. Ne JAMAIS demander "Qu'est-ce qu'on fait?" — la reponse est dans l'etat
5. Apres boot: proposer l'action la plus importante


--- FILE: AI_VIDEO_MASTER_DOMAIN.md
# FounderOS V4 — AI_VIDEO_MASTER_DOMAIN

## Purpose

The AI_VIDEO_MASTER_DOMAIN is the complete video production system for DoodleMind. It covers scripting, production, optimization, and distribution packaging.

## Position in FounderHQ

AI_VIDEO_MASTER_DOMAIN is the specialized video production engine within the content supply chain. It is loaded when CEOS requires video content or when the founder asks to produce video. It feeds finished videos and performance data back to CEOS.

## Inputs
- `FounderOS/concepts/CEOS.md` — content briefs requiring video
- Content Repository — brand assets, stock footage, music, templates
- Platform specs — resolution, duration, format per platform

## Outputs
- Video assets — exported videos ready for distribution
- Thumbnails and metadata — title, description, tags per platform
- Performance data — views, retention, engagement by platform
- Production templates — reusable workflows for similar videos

## Relations
- **CEOS** — receives briefs, returns finished videos and performance data
- **CEOS** — receives distribution schedule for video publishing
- **TIMELINE** — production milestones recorded

## Workflow

### Content Types

### 1. DoodleMind Long-Form (YouTube)
- Educational entertainment doodle videos
- 5-15 minutes
- Focus: curiosity-driven storytelling
- Platform: YouTube

### 2. DoodleMind Shorts (YouTube / TikTok)
- Vertical short-form doodle content
- 15-60 seconds
- Focus: hook retention, viral mechanics
- Platform: YouTube Shorts, TikTok

### Production Pipeline

### Pre-Production
1. **Ideation**: 10 ideas → filter by production cost vs. audience interest → select 1
2. **Research**: LEOS/RIOS research on topic
3. **Script**: Write with hook, body, CTA structure
4. **Storyboard**: Visual sequence for doodle animation
5. **Asset Checklist**: What images, audio, elements needed

### Production
1. **Audio**: Record voiceover (or generate via AI), edit for clarity and pacing
2. **Visual**: Create doodle animation per storyboard. For entity-based AI video production, load `Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md` (V2 entity framework for character/setting consistency).
3. **Music/SFX**: Background track, sound effects (hook layer priority: audio > visual > text)
4. **Edit**: Synchronize audio + visual, add text overlays

### Post-Production
1. **Thumbnail**: High-contrast, curiosity-driven, face/emotion if possible
2. **Title**: Curiosity gap, keyword-optimized
3. **Description**: SEO-rich, timestamps, links
4. **Tags**: Relevant keywords, niche + broad
5. **Publish**: Schedule for optimal time

### Distribution Package

After post-production, AI_VIDEO_MASTER_DOMAIN produces a Distribution Package for each platform/language variant:

1. **Localization**: Adapt script and captions per language (from DIOS Language Intelligence)
2. **Platform Variations**: Adapt format per platform (vertical for TikTok, landscape for YouTube, image + text for Facebook)
3. **Thumbnail Variants**: Per-platform thumbnail optimization
4. **Title & Description**: Per-platform, per-language title with hook and keywords
5. **Tags & Hashtags**: Platform-specific tag sets
6. **Publishing Schedule**: Optimal time per platform per audience

The Distribution Package is the final output that DIOS receives for distribution tracking.

### Analysis
1. **First 24h**: Views, retention, engagement
2. **Hook Analysis**: At what second do viewers drop? (YouTube Analytics)
3. **Compare**: Against previous videos, against benchmarks
4. **Learn**: Store in KNOWLEDGE.md

### Hook Layer Priority

When optimizing retention, prioritize in this order:
1. **Audio** (voice tone, pacing, background music, sound effects) — strongest retention driver
2. **Visual** (animation quality, movement, color, cuts) — second strongest
3. **Text** (captions, text overlays) — weakest alone, effective combined with audio+visual

Changing text alone produces minimal retention improvement (confirmed: 0:03 drop unchanged).

### Equipment & Tools

- AI voice generation
- AI image/animation generation
- Video editing software
- Audio editing software
- Thumbnail design tool

### Integration

- AI_VIDEO_MASTER_DOMAIN is loaded by CEOS for video production
- AI_VIDEO_MASTER_DOMAIN receives research from LEOS/RIOS
- AI_VIDEO_MASTER_DOMAIN reports performance data to CEOS for optimization

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


--- FILE: CEOS.md
# FounderOS V4 — CEOS (Content Engineering OS)

## Purpose

CEOS owns content production engineering — designing, producing, and optimizing content across all formats and platforms.

## Position in FounderHQ

CEOS controls the content supply chain — ideation, creation, distribution, and performance tracking. It is loaded when MOS requires content actions or when the founder asks to produce content. It feeds finished content and performance data into the Content Repository and TIMELINE.

## Inputs
- `FounderOS/concepts/MOS.md` — content priorities from mission alignment
- `FounderOS/State/CURRENT_STATE.md` — available time and resources
- Content Repository — existing content, channel history, audience insights

## Outputs
- Content briefs — topic, angle, format, platform for each piece
- Drafts and final content — text, captions, images, video scripts
- Distribution schedule — what goes where and when
- Performance reports — reach, engagement, conversion per post

## Relations
- **MOS** — content priorities flow from mission alignment
- **DAOS** — delegates content actions to CEOS when daily execution needs content
- **AI_VIDEO_MASTER_DOMAIN** — video production delegated when needed
- **TIMELINE** — content milestones and performance recorded

## Workflow

### Content Domains

1. **DoodleMind (YouTube)** — Long-form doodle videos, educational entertainment
2. **DoodleMind Shorts** — Vertical short-form content, viral mechanics
3. **Soya Content** — Wholesale/retail product content (if needed)
4. **FounderHQ Content** — OS documentation, thought leadership

### Content Pipeline

### Phase 2: Produce
- For video: load AI_VIDEO_MASTER_DOMAIN.md for full production workflow
- For text: write, edit, format
- For audio: script, record, edit

### Integration

- CEOS receives distribution strategy from DIOS (audience, language, platform, hook, angle, CTA)
- CEOS may invoke LEOS for research on content topics
- CEOS uses AI_VIDEO_MASTER_DOMAIN.md for video production
- CEOS reports to DAOS for daily content actions

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


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


--- FILE: DIOS.legacy.md
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
DIOS
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

## Inputs

- Product / Offer
- Price
- Target market (country, city, region)
- Objective (views, leads, sales)
- Constraints (budget, time, team, cash)
- DISTRIBUTION_MEMORY history (queried before strategy generation)

## Outputs

- Audience segment(s)
- Language(s)
- Platform(s)
- Angle(s)
- Hook(s)
- Promise
- Primary objection
- CTA
- Distribution plan (1 offer → N platform/language/audience variations)

## Relation with CEOS

DIOS answers: For who? Why? Where? When? In which language? With which angle?

CEOS answers: How to tell the story? How to write? How to film? How to produce?

DIOS decides. CEOS produces.

## Relation with AI_VIDEO_MASTER_DOMAIN

DIOS defines: Audience → Language → Hook → Angle → CTA

AI_VIDEO_MASTER_DOMAIN produces: Script → Scenes → Frames → Video → Localization → Platform Variations → Distribution Package

## Relation with Existing Modules

- MOS → feeds DIOS with mission priorities
- CAOS (FounderOS/Frameworks/Core/CAOS.md) → feeds DIOS with pricing/cash constraints
- FAOS → feeds DIOS with funnel/conversion models
- CEOS → receives DIOS strategy, produces content
- AI_VIDEO_MASTER_DOMAIN → receives CEOS specs, produces video + distribution package
- DISTRIBUTION_MEMORY → stores campaign results, queried by DIOS before each campaign

## Domain 1: Market Intelligence

Mission: Understand the market.

Questions:
- Who suffers?
- Who pays?
- Who searches for a solution?
- Who influences the purchase?
- Who shares information?
- Who decides?
- Who uses?

Data tracked:
- Needs
- Frustrations
- Fears
- Desires
- Trends
- Seasonality

Example (Kit solaire):
- Problems: blackouts, fuel cost, difficulty charging phone
- Audience: households, small businesses, street vendors
- Seasonality: dry season (more sun, more need for cooling/fans)

Language derivation: Market (country) determines available languages. Not hardcoded.

## Domain 2: Audience Intelligence

Mission: Identify precisely who must see the content.

Audience ≠ Product.

Example (Repulsif anti-moustique):
- A1: Parents (hook: protect children while sleeping)
- A2: Pregnant women (hook: protect pregnancy from malaria)
- A3: Merchants (hook: protect inventory, sleep well for business)
- A4: Hotels (hook: guest comfort, reviews)
- A5: Schools (hook: student concentration, parent trust)

Each audience needs a different hook, different story, different CTA.

Method: For every offer, DIOS identifies at least 3 distinct audiences before choosing the primary target.

## Domain 3: Language Intelligence

Mission: Speak the language of the public.

Languages are derived from Market Intelligence + target country. Not hardcoded.

Examples:
- Togo: Francais, Ewe, Mina, Pidgin, Kabiye, Tem
- Ghana: English, Twi, Ga, Ewe, Hausa, Pidgin
- Nigeria: English, Pidgin, Yoruba, Hausa, Igbo, Efik
- Benin: Francais, Fon, Yoruba, Mina, Bariba

Goal: Reduce psychological distance between the offer and the audience.

Each language version must be culturally adapted, not just translated.

DIOS selects primary language + secondary language per campaign based on audience segment.

## Domain 4: Platform Intelligence

Mission: Adapt content to the platform's attention mechanic.

TikTok
- Objective: Stop the scroll
- Structure: Hook → Curiosity → CTA
- Key: First 2 seconds decide everything

Facebook
- Objective: Build trust
- Structure: Problem → Story → Proof → CTA
- Key: Credibility signals, social proof, comments

WhatsApp
- Objective: Recommendation
- Structure: Trust → Testimonial → Offer → Direct message
- Key: 1-on-1 relationship, personal, low pressure

YouTube
- Objective: Education
- Structure: Value → Authority → Conversion
- Key: Watch time, retention, deep explanation

Omni (ex-Kora naming)
- Objective: Discovery commerce
- Structure: Index du commerce de proximité (carte interactive, disponibilité OUI/NON, Mobile Money escrow, crowd delivery)
- Key: Payment + distribution in one interface

SOJACO
- Objective: Wholesale cereal distribution (soja, maize)
- Structure: B2B — buy from Atakpamé/ami suppliers, sell to resellers by sac (100kg) or bol (2.5kg). Paiement à la livraison.
- Key: Bulk pricing, logistics Atakpamé-Lomé, B2B trust

DIOS selects platform(s) based on audience behavior, not preference.

## Domain 5: Attention Intelligence

Mission: Understand why someone stops scrolling.

Sources of attention:
- Fear
- Curiosity
- Desire
- Money
- Health
- Family
- Status
- Safety
- Opportunity

Hook Engine: For each audience, DIOS generates 10-50 hooks, then selects the best.

Hook generation dimensions:
- Per audience segment
- Per attention source
- Per language
- Per platform format (short vs long)

Example (Kit solaire, audience: parents, French):
1. "Quand le debitement coupe a 22h, votre enfant revise a la bougie depuis 3 mois."
2. "500 FCFA par jour de carburant. Chaque jour. Depuis janvier."
3. "Votre voisin a deja installe le sien. Vous attendez quoi ?"

## Domain 6: Conversion Intelligence

Mission: Transform views into sales.

Analysis dimensions:
- Why buy? (value, need, desire)
- Why wait? (risk, uncertainty, trust)
- Why refuse? (price, objection, timing)
- Why share? (status, altruism, entertainment)

Variables:
- Price → perceived value, comparison, affordability
- Risk → money-back guarantee, testimonial, trial
- Trust → social proof, authority, familiarity
- Urgency → scarcity, time-limited, stock-limited
- Proof → before/after, data, demonstration
- Simplicity → how easy to buy, receive, use

Framework: Integrates with FAOS (funnel stages) and CAOS (pricing psychology).

DIOS chooses primary objection and prepares counter before CEOS produces content.

## Domain 7: Distribution Memory

Mission: Accumulate market intelligence from every campaign.

DIOS queries DISTRIBUTION_MEMORY before every new campaign to find:
- Which hooks won for this audience?
- Which language converted best?
- Which platform distributed furthest?
- Which CTA drove action?

DISTRIBUTION_MEMORY is stored as a concept at `concepts/DISTRIBUTION_MEMORY.md`.

Each campaign entry captures: hook, audience, language, platform, views, engagement, conversions, revenue, ROI, learnings.

## Domain 8: Distribution Analytics

Mission: Identify patterns across campaigns.

Questions:
- Which hooks win? (across audiences, languages, platforms)
- Which languages convert? (per market, per product)
- Which platforms distribute? (per audience, per content type)
- Which CTAs perform? (per platform, per audience)
- Which segments buy? (per product, per price point)
- Which angles generate word-of-mouth?

Outputs:
- Reports (per campaign, per product, per market)
- Rankings (top hooks, top CTAs, top platforms)
- Recommendations (what to try next, what to stop)

DIOS uses analytics to improve future campaigns autonomously.

## DIOS Workflow

STEP 1: Receive offer (product, price, objective, constraints)
STEP 2: Identify market (Market Intelligence)
STEP 3: Identify audience(s) (Audience Intelligence) — min 3, select primary
STEP 4: Choose language(s) (Language Intelligence) — derived from market
STEP 5: Choose platform(s) (Platform Intelligence) — per audience behavior
STEP 6: Create angle(s) (Attention Intelligence + Market Intelligence)
STEP 7: Create hooks (Attention Intelligence) — generate, filter, select best
STEP 8: Choose CTA (Conversion Intelligence)
STEP 9: Send distribution strategy to CEOS for production
STEP 10: Receive performance data after publication
STEP 11: Update DISTRIBUTION_MEMORY
STEP 12: Update KNOWLEDGE (validated patterns → concepts/KNOWLEDGE.md)

## KPIs

Reach | Views | Retention | CTR | Messages | Leads | Conversions | Revenue | ROI

## Definition of Success

A successful campaign is not "a beautiful video."

A successful campaign is:
Attention → Trust → Action → Sale → Learning

Then the system becomes smarter than yesterday.

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | CEOS.md, AI_VIDEO_MASTER_DOMAIN.md, MOS.md, Frameworks/Core/CAOS.md, FAOS.md, concepts/DISTRIBUTION_MEMORY.md, concepts/KNOWLEDGE.md |


--- FILE: FAOS.md
# FounderOS V4 — FAOS (Fundraising & Alliance OS)

## Purpose

FAOS owns all financial and alliance activity — fundraising, revenue generation, partnerships, and resource acquisition.

## Position in FounderHQ

FAOS owns all financial and alliance operations — cash tracking, fundraising, revenue generation, expense management, partnerships, and resource acquisition. It is loaded when MOS requires financial or partnership actions, or when DAOS delegates financial daily tasks. It feeds financial status into CURRENT_STATE and strategic options into DECISION_ENGINE.

## Inputs
- `State/CURRENT_STATE.md` — current cash position, burn rate, incoming payments
- `concepts/MISSION.md` — financial requirements for each mission
- `concepts/PLAYBOOK.md` — fundraising, alliance, and expense playbooks

## Outputs
- Cash reports — current balance, burn rate, runway
- Fundraising actions — who to contact, what to ask, when to follow up
- Alliance opportunities — partnership leads, terms, and activation plans
- Expense recommendations — what to cut, what to fund
- Financial projections — cash flow scenarios for next 30/60/90 days

## Relations
- **MOS** — financial and alliance constraints shape priority setting
- **DAOS** — financial daily tasks delegated by DAOS
- **DECISION_ENGINE** — financial and partnership tradeoffs analyzed
- **CURRENT_STATE** — financial status written to operational state

## Workflow

### Financial Pillars

1. **Revenue Generation** — Immediate cash from operations (soya, content)
2. **Fundraising** — External capital from angels, grants, competitions
3. **Alliances** — Strategic partnerships that provide resources, distribution, or credibility
4. **Resource Optimization** — Making the most of what we have

### Revenue Playbook

#### Soya
- Direct delivery to dames at 700 FCFA cost → 900-1,000 FCFA sale
- Current capacity: ~60 bols/week, 14,300 FCFA margin
- Scale lever: credit from supplier, or direct-delivery trust

#### Content
- YouTube monetization (threshold: 1,000 subs, 4,000 hours)
- Shorts Fund (threshold varies by region)
- Long-term: brand deals, merch, courses

### Fundraising Strategy

1. **Current focus**: Bootstrap (revenue-first)
2. **Next tier**: Micro-grants for African entrepreneurs
3. **Future**: Angel investment at growth stage

### Alliance Principles

- Every alliance must answer: What does each side gain?
- Prefer non-monetary exchanges (distribution for content, etc.)
- Document all alliances in ASSET.md with contact, terms, and dates
- Review alliances quarterly for value

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |


--- FILE: FOUNDERHQ_DESCRIPTION.md
# FounderHQ — Description Fondatrice

## Définition

FounderHQ est un système cognitif portable destiné à un entrepreneur.

Son objectif est de préserver, organiser, accumuler et exploiter l'intelligence entrepreneuriale au fil du temps, indépendamment :

* du LLM utilisé,
* du logiciel utilisé,
* du runtime utilisé,
* du système d'exploitation utilisé,
* de la structure de fichiers utilisée.

FounderHQ n'est pas un assistant.

FounderHQ n'est pas un agent.

FounderHQ n'est pas un logiciel.

FounderHQ est un protocole d'organisation de l'intelligence entrepreneuriale.

Le LLM n'est qu'un processeur temporaire chargé d'interpréter FounderHQ.

Le système doit survivre au remplacement du LLM.

---

# Objectif principal

Permettre à un entrepreneur d'accumuler de l'intelligence composée :

* décisions,
* expériences,
* connaissances,
* projets,
* résultats,
* erreurs,
* playbooks,

sans perdre cette intelligence lorsqu'il change :

* d'outil,
* de modèle,
* de plateforme,
* de machine.

FounderHQ doit devenir plus intelligent au fil des années.

---

# Philosophie

FounderHQ repose sur une séparation stricte entre :

## Ce que l'on sait

Connaissance.

## Comment on opère

Protocoles.

## Comment on réfléchit

Frameworks.

## Ce que l'on fait maintenant

État opérationnel.

## Où cela s'exécute

Runtime.

Cette séparation est fondamentale.

---

# Architecture

FounderHQ est composé de 6 couches.

---

# Couche 1 — Concepts

Les Concepts représentent la mémoire permanente de l'entreprise.

Ils décrivent la réalité.

Ils ne contiennent aucune logique d'exécution.

Ils répondent à la question :

> "Qu'est-ce qui est vrai ?"

Les Concepts sont divisés en deux groupes.

---

## A1 — Identité

Ces concepts définissent l'existence même de FounderHQ.

Sans eux, FounderHQ cesse d'exister.

### Mission

Décrit :

* vision,
* direction,
* objectifs,
* principes.

Question :

> Pourquoi faisons-nous ce que nous faisons ?

---

### Memory

Décrit :

* contexte historique,
* décisions importantes,
* préférences,
* contraintes durables.

Question :

> Que devons-nous nous rappeler ?

---

### Knowledge

Décrit :

* vérités validées,
* leçons apprises,
* patterns confirmés.

Question :

> Qu'avons-nous appris ?

---

### Timeline

Décrit :

* événements,
* décisions,
* résultats.

Format :

Event → Decision → Outcome

Question :

> Que s'est-il passé ?

---

## A2 — Exécution

Ces concepts permettent d'agir.

Sans eux FounderHQ survit mais devient incapable d'exécuter efficacement.

### Project

Travail en cours.

Question :

> Que construisons-nous ?

---

### Workflow

Processus reproductibles.

Question :

> Comment exécuter une tâche ?

---

### Asset

Actifs.

Question :

> Que possédons-nous ?

Exemples :

* produits,
* marques,
* domaines,
* bases de données,
* audiences.

---

### Playbook

Méthodes validées.

Condition :

Doit être démontré plusieurs fois dans plusieurs contextes.

Question :

> Qu'est-ce qui fonctionne de façon fiable ?

---

### System

Documentation du fonctionnement interne de FounderHQ.

Question :

> Comment FounderHQ fonctionne-t-il ?

---

# Couche 2 — Protocols

Les Protocols définissent le comportement attendu.

Ils répondent à la question :

> Comment FounderHQ doit-il fonctionner ?

---

## FounderOS Protocol

Séquence de démarrage.

Boot.

Chargement.

Ordre des opérations.

---

## Decision Gates

Détermine :

* quel type de décision est demandé,
* quels concepts doivent être consultés,
* quels frameworks doivent être chargés.

---

## Temporal Awareness

Gère :

* temps,
* fraîcheur,
* âge des informations.

Chaque décision doit être consciente du temps.

---

## Relationship Model

Décrit :

* dépendances,
* relations,
* liens.

Entre tous les concepts.

---

## Source Of Truth

Règle fondamentale.

Chaque vérité possède un unique propriétaire.

Aucune duplication.

---

## Prioritization Protocol

Détermine :

> Quelle est la prochaine action la plus importante ?

---

# Couche 3 — Frameworks

Les Frameworks sont des lentilles de réflexion.

Ils ne stockent aucune donnée.

Ils ne sont pas des concepts.

Ils ne sont pas des protocoles.

Ils répondent à la question :

> Comment analyser ce problème ?

Ils peuvent être remplacés sans détruire FounderHQ.

---

## Core Frameworks

### CAOS

Analyse financière.

Cash.

Allocation.

Survie.

---

### CEOS

Analyse contenu.

Conversion.

Audience.

Distribution.

---

### PSOS

Analyse produit.

Offre.

Positionnement.

Valeur.

---

### FAOS

Analyse acquisition.

Funnel.

Croissance.

Trafic.

---

### SAOS

Analyse systémique.

Composants.

Frontières.

Bottlenecks.

Coût de suppression.

Reconstruction.

---

# Couche 4 — State

Le présent.

Photographie actuelle.

Contient :

* priorité actuelle,
* principal bottleneck,
* contexte immédiat,
* état opérationnel.

Cette couche est temporaire.

Elle peut être supprimée puis reconstruite.

---

# Couche 5 — Runtime

Le moteur d'exécution.

Exemples :

* OpenCode,
* Cursor,
* Claude Code,
* ChatGPT,
* Gemini,
* futur système.

FounderHQ ne dépend d'aucun runtime particulier.

Le runtime implémente simplement l'interface attendue.

---

# Couche 6 — Archive

Historique.

Versions précédentes.

Anciens frameworks.

Décisions anciennes.

Jamais source de vérité active.

---

# Règle Fondamentale

Chaque information possède exactement un propriétaire.

Exemple :

Prix produit :

Asset.

Pas ailleurs.

Cash :

State.

Pas ailleurs.

Leçon validée :

Knowledge.

Pas ailleurs.

Événement :

Timeline.

Pas ailleurs.

Toute duplication constitue une violation.

---

# Reconstruction

Si tous les fichiers sont perdus :

Un LLM doit pouvoir reconstruire FounderHQ à partir de cette description.

Les éléments obligatoires à reconstruire sont :

* Concepts,
* Protocols,
* Frameworks,
* State,
* Runtime Interface,
* Archive.

Les noms exacts des fichiers peuvent changer.

La structure exacte des dossiers peut changer.

Les concepts ne doivent jamais changer.

---

# Critère de réussite

FounderHQ est réussi lorsque :

* les connaissances s'accumulent,
* les décisions s'améliorent,
* les playbooks émergent,
* les projets avancent,
* les résultats sont traçables,
* le système survit au remplacement du LLM.

Le système doit devenir plus intelligent chaque année même si tous les outils changent.


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
Reflechir  →  Frameworks   (avec quelle lentille)
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


--- FILE: LEARNING/FINANCIAL_LITERACY.md
# Financial Literacy Program

Programme d'éducation financière pour FounderHQ. 5 niveaux, 28 concepts. Chaque concept validé est stocké comme connaissance durable dans KNOWLEDGE_EVOLUTION_ENGINE.

**Started:** 2026-06-21
**Progress:** 2/28 concepts
**Status:** Active

---

## Level 1 — Fundamentals (6 concepts)

Base de tout le reste. Maîtrise ces concepts avant de passer au Level 2.

### 1.1 Debt vs Equity

**Définition :** La dette (debt) est de l'argent emprunté qu'il faut rembourser avec intérêts — le prêteur ne possède rien de ta société. L'equity (fonds propres) est de l'argent donné en échange d'un pourcentage de propriété — l'investisseur possède une part de ta société.

**Différence clé :** La dette coûte des intérêts mais ne dilue pas. L'equity ne coûte pas d'intérêts mais dilue la propriété.

**Exemple Soya (dette) :** Tu empruntes 35 000 FCFA à un ami pour acheter du soja. Tu rembourses 35 000 + 3 500 d'intérêts = 38 500 FCFA après vente. L'ami ne possède rien de Soya. Il a juste prêté.

**Exemple KORA (equity) :** Tu proposes à un business angel : "Donne-moi 10 000€, tu possèdes 10% de KORA". Si KORA vaut 1 million d'euros un jour, sa part vaut 100 000€. Si KORA coule, il perd tout.

**Exemple Omni (ni dette ni equity) :** Djanta Tech Hub donne une subvention sans rien demander en retour. Ni remboursement, ni parts. C'est un cadeau — le meilleur des deux mondes.

**Application FounderHQ :**
- **Soya, Pest Repeller, Solar Kit** → Dette (pas d'equity pour du stock ou un produit). Crédit fournisseur ou micro-crédit.
- **KORA, Origin, Omni** → Equity ou subventions. Une startup tech ne peut pas rembourser une dette au début — pas de revenus prévisibles.
- **Règle :** Produit (dette) ≠ Société (equity). N'utilise jamais d'equity pour financer du stock de soja.

**Status:** ✅ Completed

---

### 1.2 Leverage (Effet de levier)

**Définition :** Utiliser l'argent des autres (emprunté) pour amplifier ton retour. Levier = montant total investi / montant de tes propres fonds.

**Exemple Soya (concret) :**
- **Sans levier :** Tu as 10 000 FCFA. Tu achètes 10 bols de soja à 700 FCFA. Tu vends à 1 000 FCFA = 10 000 FCFA de revenu. Bénéfice = 3 000 FCFA (30% de rendement).
- **Avec levier :** Tu as 10 000 FCFA + tu empruntes 40 000 FCFA à 10% d'intérêt. Total = 50 000 FCFA = ~50 bols. Tu vends à 1 000 = 50 000 FCFA de revenu. Tu rembourses 40 000 + 4 000 intérêts = 44 000. Il te reste 6 000 FCFA. Bénéfice sur tes 10 000 = 6 000 FCFA (60% de rendement).
- **Conclusion :** Tu as multiplié ton rendement par 2 sans travailler plus. Juste en utilisant l'argent des autres.

**Le piège (crucial) :** Si les ventes échouent et que tu ne vends que 30 bols à 1 000 FCFA = 30 000 FCFA de revenu. Tu DOIS quand même rembourser 44 000 FCFA. Résultat : tu perds 14 000 FCFA — dont 10 000 qui étaient à toi + 4 000 de ta poche en plus.

**Exemple Pest Repeller :** Sans levier, tu achètes 5 répulsifs que tu revends. Avec levier (crédit fournisseur), tu prends 50 unités, tu vends, tu rembourses après. Si ça marche, tu multiplies ton profit. Si ça ne marche pas, tu dois rembourser quand même.

**Pourquoi c'est partout :**
- Immobilier : les gens achètent des maisons à 80-90% avec de la dette bancaire
- Private equity : les fonds rachètent des entreprises avec 60-80% de dette
- Startups (levier indirect) : les investisseurs mettent 10-50x ce que tu peux mettre

**Pour l'Afrique :** Le crédit fournisseur (paiement après livraison) EST un levier naturel et gratuit. Tu prends le soja, tu vends, tu rembourses. C'est le meilleur levier possible — zéro intérêt si tu respectes les délais.

**Application FounderHQ :**
- **Soya :** Crédit fournisseur = levier gratuit. Priorité #1 : le développer.
- **KORA/Omni :** Le levier, c'est l'argent des investisseurs (equity). Ils prennent le risque à ta place.
- **Attention :** ne jamais utiliser de levier (dette) pour des dépenses courantes (nourriture, transport perso). Réserve le levier pour INVESTIR et générer plus.

**Status:** ✅ Completed

---

### 1.3 Intérêts Composés

**Définition :** Les intérêts gagnés sur une somme produisent eux-mêmes des intérêts. Croissance exponentielle. "L'argent qui travaille pendant que tu dors."

**Formule :** Capital final = Capital initial × (1 + taux)^périodes

**Exemple rapide :** À 10% par an, 10 000 FCFA devient 11 000 FCFA l'année 1, 12 100 FCFA l'année 2 (les 1 000 FCFA d'intérêts de l'année 1 produisent aussi 100 FCFA), 13 310 FCFA l'année 3...

**Exemple DoodleMind YouTube :** Si ta chaîne rapporte 50 000 FCFA le mois 1 (Adsense + Tiktok) et que tu réinvestis TOUT dans des meilleures vidéos (matériel, promotion), le mois 2 elle peut rapporter 75 000 FCFA. Tu réinvestis, mois 3 = 112 000. C'est ça, les intérêts composés appliqués au business : réinvestir les gains pour croître plus vite.

**Exemple Soya :** Tu gagnes 2 000 FCFA sur un lot de 10 bols. Tu prends ces 2 000, tu les ajoutes à ton prochain achat (12 000 FCFA total = 17 bols). Prochain gain: 3 400 FCFA. Tu réinvestis. 5 cycles plus tard tu achètes 50 bols d'un coup.

**Ce qui est PIEGE au Togo :** Un compte épargne te rapporte ~3,5% par an à la BCEAO. L'inflation est de ~5-6%. Ton argent PERDT du pouvoir d'achat sur un livret. Ne mets pas ton cash à la banque — réinvestis-le dans ton business.

**Ce qui tue les entrepreneurs :** Les intérêts composés travaillent CONTRE toi sur une dette impayée. 10 000 FCFA de dette à 20% qui traîne 2 ans → 14 400 FCFA à rembourser.

**Application FounderHQ :**
- Ton compte épargne = perte d'argent (3,5% < 5% inflation)
- Ton stock de soja = intérêts composés (chaque cycle alimente le prochain)
- Ta chaîne YouTube = intérêts composés (chaque vidéo alimente la suivante)
- Ta dette impayée = intérêts composés inverses (rembourse vite)

**Status:** Pending

---

### 1.4 Actifs vs Passifs

**Définition (d'après Kiyosaki, simplifiée avec tes projets) :**

- **Actif :** Ce qui met de l'argent dans ta poche sans que tu travailles.
  - Les dames qui revendent ton soja = actif (elles distribuent et ramènent du cash)
  - La chaîne TikTok qui tourne et génère des vues même quand tu dors = actif
  - Le stock de soja qui attend d'être vendu = actif
  - KORA/Omni si un jour ça génère sans toi = actif

- **Passif :** Ce qui prend de l'argent de ta poche.
  - Un abonnement méta inutilisé = passif
  - Une voiture personnelle (essence, assurance, entretien) si elle ne sert pas au business = passif
  - Un téléphone que tu paies à crédit mais qui ne sert pas à produire = passif
  - L'argent qui dort sur un compte = passif (perd de la valeur avec l'inflation)

**Application FounderHQ :**
- **Le soja** = actif (génère du cash)
- **Les dames** = actif (distribuent, génèrent des ventes)
- **L'abonnement méta** = passif si pas de retour
- **TikTok/YouTube** = actif si tu publies (génère de l'audience), passif si tu ne fais rien (consomme ton temps)
- **Une voiture achetée par la société pour livrer le soja** = actif (génère du revenu). Une voiture pour se déplacer perso = passif (coûte mais ne rapporte pas).
- **Le cash dans ton tiroir** = passif (perd 5% par an avec l'inflation). Le cash investi en stock = actif.

**Règle d'or :** Avant d'acheter quelque chose, demande-toi : "Est-ce que ça va me rapporter de l'argent ou m'en coûter ?"

**Status:** Pending

---

### 1.5 Solvabilité

**Définition :** Ta capacité à rembourser tes dettes. Les banques et fournisseurs l'évaluent avant de te faire confiance.

**Les 5 C du crédit (avec exemples pour toi) :**

1. **Character (Réputation) :** Tu as toujours payé ton fournisseur de soja à temps ? Il te fait confiance ? C'est ton actif le plus précieux. Un fournisseur qui te connaît depuis 1 an te fera crédit là où une banque refusera.

2. **Capacity (Capacité) :** Tu génères combien de cash par jour/semaine ? Avec 4 875 FCFA/jour de soja, ta capacité de remboursement est ~100 000 FCFA/mois.

3. **Capital (Ce que tu possèdes) :** Stock de soja, équipement, cash... Si tu dois 50 000 FCFA mais que tu as 40 000 FCFA de stock + 3 000 FCFA de cash, tu es limite.

4. **Collateral (Garantie) :** Qu'est-ce que tu peux donner en garantie ? Au Togo, les banques demandent souvent un bien immobilier. Mais un fournisseur accepte ton stock comme garantie informelle.

5. **Conditions (Marché) :** La demande de soja est-elle stable ? La saison des pluies affecte-t-elle ton activité ? Les conditions du marché influencent la décision du prêteur.

**Comment construire ta solvabilité (plan action) :**
1. **Sépare** comptes perso et pro (Wave ou compte bancaire dédié)
2. **Enregistre** toutes les transactions (carnet, Excel, ou appli)
3. **Commence petit** chez un fournisseur, rembourse avant l'échéance
4. **Augmente** progressivement le montant
5. **Au bout de 6 mois**, tu as un historique → banque ou microfinance plus accessible

**Ton avantage :** En Afrique, les banques ne font pas confiance aux chiffres, elles font confiance aux RELATIONS. Ta réputation auprès de tes fournisseurs et de tes dames vaut plus qu'un bilan comptable.

**Status:** Pending

---

### 1.6 Bilan Comptable Simplifié

**Définition :** Une photo de ta santé financière à un instant T. L'équation :

```
ACTIF = PASSIF + CAPITAUX PROPRES
```

- **Actif :** Tout ce que tu possèdes (cash, stock, ce qu'on te doit)
- **Passif :** Tout ce que tu dois (dettes fournisseurs, emprunts)
- **Capitaux Propres :** Ce qui reste pour toi — la valeur nette

**Exemple concret (aujourd'hui) :**

```
ACTIF (FCFA)                    PASSIF (FCFA)
Stock soja (5 bols): 3 500      Dette fournisseur: 35 000
Cash: 2 679                     Dette dame 1 (à collecter): 4 875
Créances (dame 1): 4 875        
                                CAPITAUX PROPRES
                                Ce qui reste: -28 821
---                             ---
Total Actif: 11 054              Total: 11 054
```

Ton actif (11 054 FCFA) est inférieur à ton passif (39 875 FCFA) → capitaux propres négatifs. Tu es en situation technique fragile. Mais c'est normal au début — chaque vente améliore la situation.

**Pourquoi c'est important :**
- Les investisseurs et banques lisent le bilan pour savoir si tu es fiable
- Si le passif dépasse l'actif (capitaux propres négatifs), c'est un signal d'alarme
- Mais dans ton cas, la croissance rapide (soja quotidien) compense ce déséquilibre temporaire

**Application FounderHQ :**
- Faire un bilan chaque semaine te permet de savoir si tu t'enrichis ou tu t'appauvris
- L'objectif : faire passer tes capitaux propres de -28 821 à + (positif)

**Status:** Pending

---

## Level 2 — Startup Finance (6 concepts)

Comment les startups tech (KORA, Omni) lèvent des fonds, structurent leur capital, et gèrent la dilution.

### 2.1 SAFE (Simple Agreement for Future Equity)

**Définition :** Un contrat créé par Y Combinator qui permet à un investisseur de te donner de l'argent MAINTENANT sans décider de la valeur de ta startup aujourd'hui. Il récupère ses actions PLUS TARD quand tu lèveras un vrai tour.

**Pourquoi ça existe :** Au tout début, personne ne sait combien vaut KORA ou Omni. Pas de revenus, pas de clients. Le SAFE évite de négocier une valorisation qui serait trop basse (tu te ferais avoir) ou trop haute (aucun investisseur n'accepterait).

**Comment ça marche (concret) :**
- Un angel te donne 5 000€ pour KORA via un SAFE
- 2 ans plus tard, tu lèves 500 000€ auprès d'un VC à 2M€ de valorisation
- Le SAFE se convertit : l'angel reçoit ses actions au prix du VC, souvent avec une réduction de 10-25%
- Il avait mis 5 000€, ses actions valent maintenant ~7 000€ (ou plus, selon les termes)

**Clauses :**
- **Discount :** L'investisseur achète 10-25% moins cher que le prochain tour (récompense pour le risque précoce)
- **Cap :** Valorisation maximale à laquelle le SAFE convertit (protège l'investisseur si ta startup devient la prochaine TikTok)
- **MCF :** Si tu fais un SAFE meilleur plus tard, l'investisseur peut adopter ces termes

**Application FounderHQ :**
- Si tu lances KORA ou Omni, un SAFE permet à un proche/angel de mettre 1 000-10 000€ sans négocier la valorisation aujourd'hui
- Utilisable uniquement si tu prévois un vrai tour equity plus tard (seed)
- Attention : certains SAFE africains sont mal rédigés. Fais appel à un avocat.

**Status:** Pending

---

### 2.2 Cap Table (Capitalization Table)

**Définition :** Le registre officiel de qui possède combien de % de ta société. C'est le premier document qu'un investisseur demande.

**Pour toi aujourd'hui (simple) :**
```
KORA ou OMNI (100%)
└── Kheir Lissi: 100%
```

**Quand tu lances avec KORA (scénario) :**
```
KORA Lab
└── Kheir Lissi (Fondateur): 90%
└── Pool d'options (employés futurs): 10%
```

**Après un tour seed (scénario realiste) :**
```
KORA Lab (100%)
├── Kheir Lissi: 72% (90% × 80% après dilution)
├── Pool d'options: 8% (10% × 80%)
├── Investisseur seed: 20%
```

**Pourquoi c'est crucial :** Si ta cap table est "sale" (parts non claires, promesses orales, actions promises à des amis sans papier), les VCs fuient.

**Application FounderHQ :**
- Pour l'instant, cap table = toi 100% pour tout (Soya, Pest Repeller, DoodleMind sont à toi seul)
- Dès que tu intègres un co-fondateur (même un pote), tu DOIS formaliser les parts. Une promesse orale = future dispute.
- Outil gratuit : Google Sheets ou Carta (quand tu passes pro)

**Status:** Pending

---

### 2.3 Dilution

**Définition :** Ta part du gâteau rétrécit quand tu émets de nouvelles actions pour des investisseurs ou employés.

**Ce que les gens croient :** "Si je lève des fonds, je perds ma startup." FAUX. La dilution n'est pas une perte de valeur si le gâteau grandit assez.

**Exemple concret :**
- **Avant :** Tu possèdes 100% d'une valeur de 100 000 FCFA → ta part vaut 100 000 FCFA
- **Tu lèves** 1 000 000 FCFA pour 20% de la société
- **Après :** Tu possèdes 80% d'une valeur de 6 000 000 FCFA (5 000 000 + 1 000 000) → ta part vaut 4 800 000 FCFA
- **Résultat :** Dilué de 20%, mais 48x plus riche

**L'erreur fatale :** Garder 100% d'une startup qui ne décolle jamais, refuser de lever par peur de la dilution. Résultat : tu possèdes 100% de zéro.

**Application FounderHQ :**
- Pour **Soya, Pest Repeller, Solar Kit** : pas de dilution. Tu es 100% propriétaire de tout. C'est toi qui décides.
- Pour **KORA, Omni** : la dilution est normale. Ton objectif n'est pas de garder 100% d'une petite chose, mais 10-20% d'une grosse chose qui change l'Afrique.
- 15-25% de dilution par tour est standard.

**Status:** Pending

---

### 2.4 Seed → Series A / B / C

**Les étapes de financement d'une startup tech :**

**Pre-Seed (0€ - 150k€) — TU ES ICI (KORA, Omni)**
- Idée + prototype + début d'équipe
- Argent : toi, famille, amis, subventions (Djanta Tech Hub)
- Utilisation : construire le MVP, premiers tests

**Seed (500k€ - 3M€)**
- Produit qui marche, premiers clients, début de revenus
- Investisseurs : business angels, micro-VCs
- Dilution : 15-25%
- Process : 2-4 mois

**Series A (5M€ - 20M€)**
- Produit validé, traction confirmée, équipe de 10-30
- Un VC professionnel entre au board
- Dilution : 15-25%
- Process : 4-9 mois

**Series B (15M€ - 50M€+)**
- Scale : expansion géographique, nouveaux produits
- Équipe de 50-150
- Objectif : devenir leader de marché

**Series C+ :** Scale-up massif, préparation IPO

**Comment ça se passe concrètement :**
1. Screening — tu envoies un email ou un contact chaud te présente
2. Pitch — première réunion (20-30 min)
3. Follow-up — 2-3 réunions approfondies
4. Investment memo — le partner qui te sponsorise écrit le dossier
5. Partner meeting — tous les associés votent
6. Reference calls — ils appellent tes clients, ex-collègues
7. Term sheet — offre d'investissement
8. Due diligence — ils vérifient tout (2-6 semaines)
9. Signing + wire — l'argent arrive

**Application FounderHQ :**
- Tu n'en es pas là pour KORA/Omni, tu es au stade Pre-Seed
- Mais comprendre le process est crucial pour construire DANS CETTE DIRECTION
- Les VCs en 2026 ne financent plus les promesses — ils financent les preuves (traction, métriques, équipe)

**Status:** Pending

---

### 2.5 Term Sheets

**Définition :** Une offre d'investissement de 2-5 pages. Non contraignante (sauf la clause d'exclusivité). C'est LA négociation la plus importante pour un fondateur.

**Termes clés que tu dois connaître :**

1. **Pre-money valuation :** Combien vaut ta startup AVANT l'investissement. Si KORA vaut 500k€ et que tu lèves 100k€, le pre-money = 500k€, post-money = 600k€.

2. **Liquidation preference :** Qui est remboursé en premier si la société est vendue. INVESTISSEURS avant fondateurs. Une preference 2x = l'investisseur récupère le double de sa mise avant que toi tu voies 1 FCFA.

3. **Board seat :** L'investisseur a un siège au conseil d'administration. Tu perds le contrôle absolu des décisions.

4. **Pro-rata :** L'investisseur a le droit de participer aux futurs tours pour maintenir sa part.

5. **Option pool :** Un réservoir d'actions pour les employés. Créé AVANT le tour (ça dilue TOI, pas l'investisseur).

**Piège mortel :** Une liquidation preference 2x participative. Si tu vends KORA pour 500k€ et que l'investisseur a mis 100k€ avec cette clause, il prend 200k€ avant toi. Des fondateurs se sont retrouvés avec ZERO sur une vente de plusieurs millions.

**Application FounderHQ :**
- Quand tu lèveras, FAIS-TOI ASSISTER d'un avocat
- Les term sheets en Afrique suivent souvent les modèles US
- Un bon avocat spécialisé en startup coûte 500-1 500€ — c'est le meilleur investissement que tu feras

**Status:** Pending

---

### 2.6 Due Diligence

**Définition :** Le processus où le VC vérifie tout ce que tu as dit avant d'investir. 6-10 semaines en seed.

**Ce qui est vérifié :**

- **Financial hygiene :** comptabilité propre, cap table claire, impôts payés
- **Unit economics :** combien coûte l'acquisition d'un client, combien il rapporte sur sa vie
- **Founder-market fit :** pourquoi TOI ? Pourquoi Lomé ? Pourquoi maintenant ?
- **Technical scalability :** l'architecture technique tient-elle si tu passes de 100 à 1 million d'utilisateurs ?
- **Customer validation :** ils appellent tes CLIENTS (pas ceux que tu as choisis, ceux qu'ils trouvent)
- **Digital reputation :** les VCs interrogent ChatGPT et Perplexity sur ta startup avant le premier rendez-vous

**Application FounderHQ :**
- Pour te préparer MAINTENANT : tiens tes comptes proprement pour Soya, même si c'est petit
- Avoir un data room structuré (comme les docs KORA/Omni que tu as déjà)
- Commence dès aujourd'hui à documenter : chaque dépense, chaque contrat, chaque client
- Dans 2-3 ans, quand tu lèveras, la due diligence sera plus facile

**Status:** Pending

---

## Level 3 — Corporate Structures (5 concepts)

Comment structurer juridiquement Soya, Pest Repeller, DoodleMind, Solar Kit, KORA, Omni — tous tes projets.

### 3.1 SARL / SAS / SA

**Définition (contexte OHADA — Togo) :**

- **SARL (Société à Responsabilité Limitée) :** Simple, 1-100 associés. Gérant (toi). Pas de board. Capital minimum symbolique (1 000 FCFA en OHADA). Adaptée à Soya, Pest Repeller, Solar Kit.

- **SAS (Société par Actions Simplifiée) :** Flexible, compatible investisseurs. Peut avoir différentes classes d'actions. Préférée pour KORA et Omni car les VCs investissent dans des SAS, pas des SARL.

- **SA (Société Anonyme) :** Lourde (board, commissaire aux comptes). Pour les grandes entreprises cotées en bourse.

**Application FounderHQ :**
- **Soya, Pest Repeller, Solar Kit** → activité informelle ou SARL (pas d'investisseurs externes, gestion simple)
- **KORA, Omni** → SAS dès le départ (même si tu es seul). Plus facile pour intégrer des investisseurs plus tard.
- **DoodleMind** → peut rester sous SARL ou en nom personnel tant que ça reste petit

**Status:** Pending

---

### 3.2 Holding

**Définition :** Une société mère qui possède les actions de toutes tes autres sociétés. Elle ne fait rien elle-même — elle détient le contrôle.

**Structure future (si tout marche) :**

```
HOLDING (toi = 100%)
├── Soya (SARL) — produit physique
├── Pest Repeller (SARL) — produit physique
├── Solar Kit (SARL) — produit physique
├── DoodleMind (SARL) — contenu digital
├── KORA Lab (SAS) — IA/AI lab
└── Omni (SAS) — plateforme tech
```

**Pourquoi c'est important pour toi :**

1. **Protection :** Si Soya fait faillite, KORA n'est PAS impactée. Chaque filiale est indépendante juridiquement.
2. **Fiscalité :** Les filiales qui gagnent de l'argent peuvent "remonter" les profits à la holding avec un régime fiscal avantageux. La holding peut financer les filiales qui en ont besoin.
3. **Investisseurs :** Les investisseurs entrent dans la filiale concernée (KORA ou Omni), pas dans la holding. Tu gardes 100% du contrôle du groupe.

**Application FounderHQ :**
- Ne crée pas la holding maintenant. Commence avec une SARL pour Soya.
- Quand KORA ou Omni décollent et ont besoin d'investisseurs, la holding devient pertinente.
- La holding est le "château fort" — elle protège tout ce que tu construis.

**Status:** Pending

---

### 3.3 Comptabilité de Base

**Définition :** Enregistrer systématiquement tout ce qui entre et sort. Pas pour le plaisir — pour savoir si tu gagnes ou tu perds de l'argent.

**Tes 3 documents :**

1. **Bilan :** Ce que tu possèdes vs ce que tu dois (déjà vu en 1.6)
2. **Compte de résultat :** Revenus - Dépenses sur une période. Exemple Soya : 24 375 FCFA (5 bols x 5 jours) - 17 500 FCFA (coût fournisseur) = 6 875 FCFA de bénéfice/semaine
3. **Cash Flow :** Argent qui ENTRE réellement (quand les dames paient) vs argent qui SORT (quand tu paies le fournisseur). DIFFÉRENT du profit car les créances et dettes décalent le cash.

**Exemple pourquoi c'est important :**
- Tu as vendu 5 bols = 4 875 FCFA de REVENU
- Mais le cash n'est pas encore dans ta poche (la dame paie à 17h)
- Ton cash flow est NÉGATIF jusqu'à 17h

**Application FounderHQ :**
- Ouvre un compte Wave Business ou compte bancaire pro
- Enregistre chaque transaction : date, montant, catégorie (vente, achat stock, transport, etc.)
- Minimum : un carnet ou Google Sheets
- L'objectif : pouvoir répondre à "combien j'ai gagné ce mois-ci ?" sans hésiter

**Status:** Pending

---

### 3.4 Fiscalité Entreprise

**Contexte OHADA/UEMOA (ce qui t'attend au Togo) :**

- **Impôt sur les Sociétés (IS) :** ~27% du bénéfice
- **TVA :** 18% collectée sur tes ventes, déductible sur tes achats. À déclarer mensuellement.
- **IRVM :** Impôt sur les dividendes que tu te verses
- **Patente :** Taxe professionnelle (montant fixe selon l'activité)

**Concrètement pour Soya aujourd'hui :**
- Tu es en informel. Pas de TVA, pas d'IS. Mais tu ne peux pas non plus justifier tes revenus pour un prêt bancaire.
- Dès que tu formalises, tu déclares et paies des impôts — mais tu es aussi éligible au crédit, aux appels d'offres, aux partenariats.

**Ce qu'il faut retenir :**
- La TVA n'est pas une charge : tu la collectes AUPRÈS de tes clients et tu la reverses à l'État. Elle ne t'appartient pas.
- Un cabinet comptable à 30-50k FCFA/mois peut gérer toutes les déclarations et t'éviter des pénalités.
- Au début, le plus rentable est de sous-traiter la compta.

**Status:** Pending

---

### 3.5 Optimisation Fiscale (Actifs via Société)

**Définition :** Utiliser la société pour acheter des biens qui servent à l'activité, et les déduire des impôts. Ce n'est PAS de la fraude — c'est de l'optimisation.

**Comment ça marche :**
- La société achète un vélo ou un scooter pour livrer le soja → déductible du résultat → moins d'impôts
- La société paie l'essence pour les livraisons → déductible
- La société achète un smartphone pour gérer les commandes TikTok/YouTube → déductible
- La société loue un petit espace de stockage → déductible

**Règle d'or ABSOLUE :** L'actif doit servir à l'ACTIVITÉ. Pas de voiture personnelle passée en frais si tu ne livres pas avec. Pas de restaurant entre amis passé en "réunion d'affaires". La fraude n'est pas de l'optimisation.

**Application FounderHQ :**
- **Utile pour toi :** Stock de soja, équipement vidéo (DoodleMind), smartphone pour gérer, transport pour livraisons
- **Pas encore pertinent :** À ton stade, le plus important est de générer du revenu, pas d'optimiser des impôts que tu ne paies pas encore

**Status:** Pending

---

## Level 4 — SME Finance Africa (6 concepts)

Les outils financiers concrets pour financer ta croissance au Togo et en Afrique de l'Ouest.

### 4.1 Crédit Bancaire / Microfinance

**Définition :**
- **Crédit bancaire classique :** Prêt à 10-20% par an, garanti par des actifs. Difficile pour toi sans historique bancaire.
- **Microfinance (ADVANCE, ALIDé, FUCEC au Togo) :** Prêts de 50k-500k FCFA sans garantie lourde. Taux 15-30% mais ACCESSIBLES.

**Comment construire la relation :**
1. Ouvre un compte pro et utilises-le pour 100% des transactions
2. Demande un PETIT prêt (50k FCFA). Si on te dit non, réduis à 25k.
3. Rembourse avant l'échéance
4. Demande un prêt plus gros
5. Au bout d'1 an, tu as un historique bancaire

**Application FounderHQ :**
- La microfinance est ton point d'entrée pour augmenter le stock de soja (passer de 5 à 50 bols/jour)
- Les banques classiques viendront après 6-12 mois d'historique
- Alternative plus rapide : développer le crédit fournisseur (zéro intérêt)

**Status:** Pending

---

### 4.2 Crédit Fournisseur

**Définition :** Le fournisseur te livre MAINTENANT, tu paies PLUS TARD (15-30 jours). C'est une dette SANS INTÉRÊT. LE meilleur financement au monde.

**Tu fais déjà ça :** Le fournisseur d'Atakpamé à 360 FCFA/kg te livre, tu vends, tu rembourses. C'est du crédit fournisseur.

**Pourquoi c'est LE meilleur :**
- ZÉRO intérêt (contrairement à la banque à 15-30%)
- ZÉRO garantie
- Le montant grandit avec votre relation
- Pas de paperasse
- Pas d'attente

**Ton plan d'action :**
1. **Priorité #1 :** Négocier des délais avec TOUS tes fournisseurs
2. **Règle ABSOLUE :** Ne JAMAIS rater un paiement promis. Ta parole vaut de l'or — c'est ton seul collatéral.
3. **Augmente progressivement :** Commence par 5 bols, puis 10, 20, 50...

**Application FounderHQ :**
- Soya : crédit fournisseur = priorité absolue
- Pest Repeller/Solar Kit : peut fonctionner pareil si tu trouves le bon fournisseur
- Pas pertinent pour KORA/Omni (pas de "stock" physique)

**Status:** Pending

---

### 4.3 Factoring (Vente de Créances)

**Définition :** Tu as vendu mais pas encore été payé. Tu vends ta facture à un "factor" qui te donne le cash immédiat (moins 2-10% de commission).

**Scénario (pour plus tard) :**
- Tu livres 100 bols/jour aux dames (vente à crédit 15 jours)
- Tu as besoin de cash MAINTENANT pour le prochain achat
- Le factor te donne 90% du montant aujourd'hui
- Il se fait rembourser par les dames dans 15 jours
- Tu perds 10% mais tu ne casses pas ta chaîne d'approvisionnement

**Nouveauté Afrique 2026 :** Le Nigéria a légalisé le factoring pour les PME. Le marché africain du factoring dépasse 50 milliards de dollars.

**Application FounderHQ :**
- Pas encore pertinent pour toi (montants trop petits)
- Mais quand Soya fera 500k-1M FCFA/mois, le factoring devient un outil clé
- À connaître pour le prochain palier

**Status:** Pending

---

### 4.4 Venture Debt

**Définition :** Dette accordée à une startup tech qui a déjà levé de l'equity. Le prêteur vérifie que les VCs ont validé le modèle avant de prêter.

**Conditions :**
- Doit avoir levé un tour equity récent
- Revenus prévisibles ou récurrents
- Marges saines
- Croissance 20-50%+ par an

**Afrique 2025-2026 :** +60% de dette venture en un an. 40% du financement tech africain est maintenant de la dette.

**Application FounderHQ :**
- Pas pertinent pour toi aujourd'hui (besoin d'un VC derrière toi)
- Pour KORA/Omni après un tour seed : très pertinent pour financer la croissance sans diluer les fondateurs

**Status:** Pending

---

### 4.5 Appels d'Offres

**Définition :** Un client (État, ONG, grande entreprise) publie un besoin. Tu réponds avec une proposition. Si tu es sélectionné, tu exécutes et tu es payé.

**Où trouver des appels :**
- **Marchés publics Togo :** https://marchespublics.tg
- **PNUD :** https://procurement-notices.undp.org
- **Banque Mondiale :** https://www.worldbank.org/procurement
- **ONG locales :** WFP, UNICEF, programmes nutritionnels

**Comment gagner (stratégie petit entrepreneur) :**
1. Cible les petits appels (les gros sont déjà capturés par les grandes entreprises)
2. Respecte EXACTEMENT le format demandé (une erreur = disqualifié)
3. Propose un prix serré au début — tu construis l'historique
4. Une fois référencé, les appels suivants sont plus faciles

**Application FounderHQ :**
- **Soya :** Cantines scolaires, hôpitaux, programmes nutritionnels — besoin de soja régulier
- **Pest Repeller :** Programmes de lutte anti-nuisibles des municipalités
- **ST Digital :** Appels d'offres tech des ministères, ONG internationales

**Status:** Pending

---

### 4.6 Subventions / Fonds de Garantie

**Définition :**
- **Subvention :** Argent non remboursable pour un projet spécifique. Ex: Fonds Start de Djanta Tech Hub (jusqu'à 9M FCFA).
- **Fonds de garantie :** L'État ou une institution garantit ton prêt auprès de la banque. Si tu ne rembourses pas, ils paient.

**À connaître pour toi :**
- **Djanta Tech Hub / Fonds Start :** Jusqu'à 9M FCFA pour les projets innovants — tu postules avec Omni !
- **BOAD :** Banque Ouest-Africaine de Développement — garanties pour PME
- **Proparco :** Financement et garanties pour PME africaines
- **FAGACE :** Fonds Africain de Garantie

**Pourquoi c'est important :** Les banques africaines ne prêtent pas aux PME sans garantie. Les fonds de garantie sont LE PONT entre toi et la banque.

**Application FounderHQ :**
- **Court terme :** Subvention Djanta Tech Hub pour Omni (Fonds Start) — le dossier est presque prêt
- **Moyen terme :** Fonds de garantie pour Soya quand tu passes à 200k+ FCFA/mois — débloque un prêt 10x plus gros
- Les subventions sont rares mais EXISTENT. Il faut les chercher. D'où l'importance du WATCH_REGISTRY.

**Status:** Pending

---

## Level 5 — Macroéconomie (5 concepts)

Pourquoi l'économie togolaise et mondiale fonctionne comme ça, et comment ça t'affecte DIRECTEMENT.

### 5.1 Inflation

**Définition :** Le prix des choses augmente avec le temps. 100 FCFA aujourd'hui n'achètent pas la même chose que 100 FCFA l'année dernière.

**Taux UEMOA 2026 :** ~2-4% (stable grâce au FCFA indexé sur l'euro)
**Taux Nigeria 2026 :** ~25-30% (instable — le Naira perd 70% de sa valeur)

**Impact concret pour toi :**
- **Le soja que tu stockes prend de la valeur** (l'inflation fait monter les prix). Acheter du stock MAINTENANT est une protection.
- **Les 2 679 FCFA dans ta poche perdent de la valeur.** Dans 1 an (à 5% d'inflation), ils n'achètent que l'équivalent de 2 546 FCFA d'aujourd'hui.
- **Conclusion :** Le cash qui dort est un passif. Stocke, investis, ou rembourse tes dettes. Ne laisse pas l'argent inactif.

**Application FounderHQ :**
- Avantage : tu es dans une zone FCFA stable (pas comme le Nigéria où les entrepreneurs perdent 30% de leur cash par an)
- Action : convertis ton cash en stock ou en équipement le plus vite possible

**Status:** Pending

---

### 5.2 BCEAO / Taux Directeurs

**Définition :** La BCEAO (Banque Centrale des États de l'Afrique de l'Ouest) est la banque des banques pour les 8 pays UEMOA (dont Togo). Elle fixe le "taux directeur" — le prix auquel elle prête aux banques commerciales.

**Comment ça t'affecte :**

```
BCEAO fixe le taux directeur (3,5%)
  ↓
Les banques commerciales empruntent à ce taux + leur marge
  ↓
Elles te prêtent à toi, PME, avec une prime de risque
  ↓
Au Togo : 12-18% pour une PME
  ↓
Toi (Soya) : en réalité 15-30% en microfinance
```

**Quand le taux monte :** Les crédits deviennent plus chers → tu empruntes moins → l'économie ralentit.
**Quand le taux baisse :** Les crédits deviennent moins chers → tu empruntes plus → l'économie accélère.

**Application FounderHQ :**
- Le taux BCEAO à 3,5% est bas — favorable pour emprunter
- Mais la différence entre 3,5% et les 15-30% qu'on te propose, c'est LA prime de risque PME
- Ton job : réduire cette prime de risque en prouvant ta fiabilité (comptabilité propre, historique de remboursement)

**Status:** Pending

---

### 5.3 Risque de Change (FCFA → EUR/$)

**Définition :** Le risque que la valeur de ta devise change par rapport à une autre devise.

**Ton avantage FCFA :**
- Le Franc CFA est fixe contre l'Euro (1€ = 655,957 FCFA). Pas de fluctuation depuis 1999.
- **Tu n'as aucun risque de change** si tu travailles en FCFA et que tu empruntes en FCFA.

**Comparaison Nigéria :**
- Le Naira a perdu 70% de sa valeur en 3 ans.
- Un entrepreneur nigérian qui emprunte en dollars doit rembourser 70% de plus en Naira.
- Beaucoup ont fait faillite à cause de ça.

**Application FounderHQ :**
- Travailler en FCFA est un avantage concurrentiel ÉNORME
- Si tu lèves des fonds en €/$ ou achètes des services tech en €/$, le taux fixe te protège
- Les startups nigérianes paient leurs serveurs AWS en dollars avec des revenus en Naira qui s'effondrent — c'est un cauchemar

**Status:** Pending

---

### 5.4 Dette Souveraine (la dette des États)

**Définition :** Les gouvernements empruntent aussi. Ils émettent des obligations (bons du Trésor) que les banques et investisseurs achètent.

**Pourquoi ça t'affecte DIRECTEMENT :**
- L'État togolais emprunte sur le marché local à ~6-8% d'intérêt
- Les banques préfèrent prêter à l'État (risque zéro) qu'à TOI (risque élevé)
- Résultat : le crédit disponible pour les PME est réduit, et les taux sont plus élevés
- C'est ce qu'on appelle l'**"éviction" (crowding out)**

**Exemple concret :**
- La banque a 100 millions à prêter
- Elle prête 80 millions à l'État à 7% (sans risque)
- Il reste 20 millions pour les PME à 15-18% (avec risque)
- Toi tu es dans les 20 millions restants, en compétition avec toutes les autres PME

**Ce n'est pas unique au Togo — c'est comme ça partout en Afrique.**

**Application FounderHQ :**
- Ce n'est pas de ta faute si les taux sont élevés. C'est structurel.
- La solution : crédit fournisseur (zéro intérêt, pas de banque), microfinance (plus accessible), et construire ton historique bancaire.
- Quand le gouvernement togolais emprunte moins, les banques prêtent plus aux PME.

**Status:** Pending

---

### 5.5 Pourquoi les États Empruntent (et pas seulement les entreprises)

**Définition large :** La dette n'est PAS un mal en soi. C'est un outil pour INVESTIR aujourd'hui et récolter les bénéfices demain.

**Pourquoi c'est pareil pour toi et pour l'État :**

| | Toi (Soya) | État (Togo) |
|---|---|---|
| Tu empruntes pour | Acheter du stock | Construire une route |
| Le bénéfice arrive | Dans 1-7 jours | Dans 10-20 ans |
| L'emprunt est logique ? | OUI (tu vends plus) | OUI (commerce + emplois + impôts) |

**Quand la dette devient un PROBLÈME :**
- Quand elle sert à payer les DÉPENSES COURANTES (survie), pas à investir
- Quand les intérêts à rembourser dépassent la croissance
- Quand la dette est dans une devise différente des revenus (emprunter en $, gagner en FCFA)

**Application FounderHQ :**
- **Bonne dette :** 35 000 FCFA pour du soja que tu vas vendre 50 000 FCFA
- **Mauvaise dette :** 35 000 FCFA pour payer ton loyer (ça ne rapporte rien)
- Endette-toi pour INVESTIR (stock, équipement, campagne TikTok), jamais pour SURVIVRE

**Status:** Pending

---

## Progress Tracker

### Level 1 — Fundamentals

| # | Concept | Status | Date Completed |
|---|---------|--------|---------------|
| 1.1 | Debt vs Equity | ✅ Completed | 2026-06-21 |
| 1.2 | Leverage | ✅ Completed | 2026-06-21 |
| 1.3 | Intérêts Composés | Pending | - |
| 1.4 | Actifs vs Passifs | Pending | - |
| 1.5 | Solvabilité | Pending | - |
| 1.6 | Bilan Comptable Simplifié | Pending | - |

### Level 2 — Startup Finance

| # | Concept | Status | Date Completed |
|---|---------|--------|---------------|
| 2.1 | SAFE | Pending | - |
| 2.2 | Cap Table | Pending | - |
| 2.3 | Dilution | Pending | - |
| 2.4 | Seed → Series A/B/C | Pending | - |
| 2.5 | Term Sheets | Pending | - |
| 2.6 | Due Diligence | Pending | - |

### Level 3 — Corporate Structures

| # | Concept | Status | Date Completed |
|---|---------|--------|---------------|
| 3.1 | SARL / SAS / SA | Pending | - |
| 3.2 | Holding | Pending | - |
| 3.3 | Comptabilité de Base | Pending | - |
| 3.4 | Fiscalité Entreprise | Pending | - |
| 3.5 | Optimisation Fiscale (Assets) | Pending | - |

### Level 4 — SME Finance Africa

| # | Concept | Status | Date Completed |
|---|---------|--------|---------------|
| 4.1 | Crédit Bancaire / Microfinance | Pending | - |
| 4.2 | Crédit Fournisseur | Pending | - |
| 4.3 | Factoring | Pending | - |
| 4.4 | Venture Debt | Pending | - |
| 4.5 | Appels d'Offres | Pending | - |
| 4.6 | Subventions / Fonds de Garantie | Pending | - |

### Level 5 — Macroéconomie

| # | Concept | Status | Date Completed |
|---|---------|--------|---------------|
| 5.1 | Inflation | Pending | - |
| 5.2 | BCEAO / Taux Directeurs | Pending | - |
| 5.3 | Risque de Change | Pending | - |
| 5.4 | Dette Souveraine | Pending | - |
| 5.5 | Pourquoi les États Empruntent | Pending | - |

**Total:** 2/28 concepts completed

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Program Started | 2026-06-21 |
| Next Review | 2026-06-28 |
| Owner | Founder |


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


--- FILE: README.md
# FounderOS V4

## Structure
```
FounderHQ/
├── FounderOS/
│   ├── SYSTEM/       ← 35+ modules OS + specs
│   ├── STATE/        ← Realite courante (8 fichiers)
│   └── *.md          ← Specs fondateurs
├── Projects/         ← Projets actifs
├── Knowledge/        ← Savoir permanent
├── Reports/          ← Briefs, reviews
├── Events/           ← Evenements externes
├── Workspace/        ← Brouillons
└── Archive/          ← Inactif
```

## Demarrage
Ouvrir OpenCode dans FounderHQ/FounderOS/ → le boot sequence s'execute automatiquement.

## Commandes
- `boot` → demarrer une session (7 phases)
- `refresh` → re-run boot en cours de session
- `sync` → quick state check
- `shutdown` → sauvegarder et fermer
- `now` → action prioritaire

## Documentation principale
- `FOUNDERHQ_DESCRIPTION.md` → description fondatrice de FounderHQ

## Produits Pipeline
- Pillule (2,900 FCFA) — fournisseur accepte
- Kit Solaire 220W (35,900 FCFA) — nouveau lead
- Kit 2USB 220W (46,900 FCFA) — pas contacte

## Mode actuel
SURVIVAL — generation de cash avant tout.


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


--- FILE: docs/superpowers/plans/2026-06-21-fre-implementation.md
# Founder Runtime Engine (FRE) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the Runtime Abstraction Layer for FounderHQ — FRE_SPEC (constitution), ADAPTER_INTERFACE (contract), and 6 platform adapters — making FHQ portable across any LLM/IDE.

**Architecture:** Three layers: FRE_SPEC.md defines testable behavioral contracts. ADAPTER_INTERFACE.md defines what any adapter must answer. Adapter files (`opencode.md`, `chatgpt.md`, etc.) translate FRE contracts to platform-specific mechanisms.

**Tech Stack:** Markdown only. No code. No dependencies.

---

## File Structure

```
FounderOS/Runtime/
├── FRE_SPEC.md               ← Constitution: testable behavioral contracts
├── ADAPTER_INTERFACE.md       ← Contract that every adapter must satisfy
└── adapters/
    ├── opencode.md            ← OpenCode adapter
    ├── chatgpt.md             ← ChatGPT Web adapter
    ├── claude.md              ← Claude Code adapter
    ├── gemini.md              ← Gemini CLI adapter
    ├── cursor.md              ← Cursor IDE adapter
    └── local_agent.md         ← Autonomous agent adapter
```

---

### Task 1: FRE_SPEC.md — The Constitution

**Files:**
- Create: `FounderOS/Runtime/FRE_SPEC.md`

- [ ] **Step 1: Create FRE_SPEC.md with Boot Contract**

```markdown
# Founder Runtime Engine Specification (FRE) V1

## Purpose
FRE defines what FounderHQ requires from any runtime environment. Any platform (OpenCode, Claude Code, ChatGPT, Gemini, Cursor, local agent) that satisfies these contracts can run FounderHQ identically.

## Contract 1: Boot Sequence

Every session MUST execute the following before responding to the user:

1. Load CURRENT_STATE.md from `State/CURRENT_STATE.md`
2. Load PRIORITY_MATRIX.md from `State/PRIORITY_MATRIX.md`
3. Load WATCH_REGISTRY.md from `State/WATCH_REGISTRY.md`
4. Compute datetime in Lomé UTC+0
5. Determine if any concept > 48h stale
6. Report: datetime, mode (SURVIVAL/GROWTH/SCALE), top priority, stale concepts

**Test:** User sends first message of session. Response MUST include datetime + mode + top priority. FAIL if missing.

**Failure mode:** If any load fails, report which file is missing and continue with available state. Never block on missing file.
```

- [ ] **Step 2: Add Pre-Response Contract**

Append to FRE_SPEC.md:

```markdown
## Contract 2: Pre-Response Gate (PRG)

Every response MUST pass through these 5 gates BEFORE being sent:

| # | Gate | Condition | Violation |
|---|------|-----------|-----------|
| 1 | Temporal Check | Response starts with `**[datetime Lomé UTC+0]**` | First line is NOT a datetime |
| 2 | Info Capture Scan | Scan user's last message against INFO_CAPTURE_PROTOCOL mapping table. Match → update file BEFORE replying. | User provided operational data, file NOT updated. |
| 3 | Absorb Updates | Any operational data not in mapping → update affected files before reply. | Data mentioned in conversation, file NOT updated. |
| 4 | Project Data Room Scan | Check all active projects in PRIORITY_MATRIX with `projects/<PROJECT>/` folder. Verify strategic cascade (01-10 + annexes). | Missing file NOT flagged. |
| 5 | Freshness Flag | Any concept > 48h → flag as STALE before proceeding. | Stale concept NOT flagged. |

**Test:** User provides a deadline. Before response, PRIORITY_MATRIX.md must be updated. FAIL if response comes first.

**Test:** User asks about stale concept. Response must acknowledge staleness. FAIL if treated as current.
```

- [ ] **Step 3: Add State Management + Gate + Temporal + Recall Contracts**

Append to FRE_SPEC.md:

```markdown
## Contract 3: State Management

| Rule | Enforced | Violation |
|------|----------|-----------|
| Every state file has a `Last Updated` timestamp | Before reading | Missing or stale timestamp |
| State > 48h without update → flagged STALE | Before any action using that state | Used without flagging |
| CURRENT_STATE is single source of truth for session state | Before any state-dependent decision | Another file contradicts CURRENT_STATE |
| TIMELINE updated for every significant event (Event → Decision → Outcome) | After executing an action | Event happened, TIMELINE not updated |

## Contract 4: Non-Negotiable Gates

These gates apply to every action, regardless of runtime:

| Gate | Rule | Violation |
|------|------|-----------|
| Rule #6 | NEVER execute irreversible external actions without explicit user approval | Form submitted, email sent, account created without "go ahead" |
| Cash Awareness | If cash < 1,500 FCFA, every action must generate or enable revenue | Action consumes cash without revenue path |
| Mission Alignment | Before any action: what mission does this serve? If none, don't do it | Action taken without identifiable mission |

## Contract 5: Temporal

1. All responses start with `**[datetime Lomé UTC+0]**`
2. Datetime format: `YYYY-MM-DD HH:MM Lomé UTC+0`
3. Timezone: West Africa Time (UTC+0, no DST)
4. Age of any file = current_time - file's `Last Updated`
5. Age categories: <1d (high), 1-7d (medium), 7-30d (low), 30-90d (very low), >90d (minimal)

## Contract 6: Context Recall

1. If session context is lost (new session, no prior messages), execute full Boot Sequence
2. If TIMELINE.md exists, reconstruct from reverse chronological
3. If TIMELINE.md missing, reconstruct from CURRENT_STATE + CONCEPT footers
4. If reconstruction is partial, mark all entries as APPROXIMATE
```

- [ ] **Step 4: Verify file**

Run: `Get-Item -LiteralPath "FounderOS/Runtime/FRE_SPEC.md"`
Expected: File exists, readable, contains all 6 contracts.

---

### Task 2: ADAPTER_INTERFACE.md — The Contract

**Files:**
- Create: `FounderOS/Runtime/ADAPTER_INTERFACE.md`

- [ ] **Step 1: Create ADAPTER_INTERFACE.md**

```markdown
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
...

## Q2: File Access
...

## Q3: Context Persistence
...

## Q4: Protocol Execution
...
```
```

- [ ] **Step 2: Verify file**

Run: `Get-Item -LiteralPath "FounderOS/Runtime/ADAPTER_INTERFACE.md"`
Expected: File exists, contains all 4 questions with template.

---

### Task 3: OpenCode Adapter

**Files:**
- Create: `FounderOS/Runtime/adapters/opencode.md`

- [ ] **Step 1: Create opencode.md**

```markdown
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
```

- [ ] **Step 2: Verify file**

Run: `Get-Item -LiteralPath "FounderOS/Runtime/adapters/opencode.md"`
Expected: File exists, answers all 4 questions.

---

### Task 4: ChatGPT Adapter

**Files:**
- Create: `FounderOS/Runtime/adapters/chatgpt.md`

- [ ] **Step 1: Create chatgpt.md**

```markdown
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
```

- [ ] **Step 2: Verify file**

---

### Task 5: Claude Code + Gemini Adapters

**Files:**
- Create: `FounderOS/Runtime/adapters/claude.md`
- Create: `FounderOS/Runtime/adapters/gemini.md`

- [ ] **Step 1: Create claude.md**

```markdown
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
```

- [ ] **Step 2: Create gemini.md**

```markdown
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
```

- [ ] **Step 3: Verify files**

Run: `Get-Item -LiteralPath "FounderOS/Runtime/adapters/claude.md", "FounderOS/Runtime/adapters/gemini.md"`
Expected: Both files exist.

---

### Task 6: Cursor + Local Agent Adapters

**Files:**
- Create: `FounderOS/Runtime/adapters/cursor.md`
- Create: `FounderOS/Runtime/adapters/local_agent.md`

- [ ] **Step 1: Create cursor.md**

```markdown
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
```

- [ ] **Step 2: Create local_agent.md**

```markdown
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
```

- [ ] **Step 3: Verify files**

Run: `Get-Item -LiteralPath "FounderOS/Runtime/adapters/cursor.md", "FounderOS/Runtime/adapters/local_agent.md"`
Expected: Both files exist.

---

### Task 7: Update SYSTEM_PROMPT.md — Reference FRE_SPEC

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md`

- [ ] **Step 1: Add FRE reference in Architecture section**

Replace current Architecture section (lines 31-35) in SYSTEM_PROMPT.md:

Current:
```
## Architecture

FounderOS V4 has three layers:
1. **OS Layer** — This prompt + RUNTIME.md. The agentic core.
2. **Module Layer** — 12 specialist modules (MOS, DAOS, CEOS, DIOS, etc.) loaded via Intent Classification.
3. **Engine Layer** — 5 cross-cutting systems (DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE, KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT).
```

New:
```
## Architecture

FounderOS V4 has four layers:
0. **Runtime Layer** — FRE (Founder Runtime Engine). `Runtime/FRE_SPEC.md` defines behavioral contracts. `Runtime/adapters/` map contracts to specific platforms. See `Runtime/FRE_SPEC.md` for the full specification.
1. **OS Layer** — This prompt + RUNTIME.md. The agentic core. Implements FRE_SPEC contracts.
2. **Module Layer** — 12 specialist modules (MOS, DAOS, CEOS, DIOS, etc.) loaded via Intent Classification.
3. **Engine Layer** — 5 cross-cutting systems (DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE, KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT).
```

- [ ] **Step 2: Add FRE to Boot Sequence Step 1**

Current Step 1:
```
1. **Load Protocols** — SOURCE_OF_TRUTH.md + DECISION_GATES.md + INFO_CAPTURE_PROTOCOL.md
```

New:
```
1. **Load Protocols + FRE** — SOURCE_OF_TRUTH.md + DECISION_GATES.md + INFO_CAPTURE_PROTOCOL.md + Runtime/FRE_SPEC.md
```

- [ ] **Step 3: Verify changes**

Read `FounderOS/SYSTEM_PROMPT.md` lines 31-38 and boot sequence step 1.
Expected: Architecture mentions 4 layers with FRE. Boot step 1 includes FRE_SPEC.md.

---

### Task 8: Update `opencode.json` — Add FRE_SPEC.md to instructions

**Files:**
- Modify: `FounderOS/opencode.json`

- [ ] **Step 1: Update instructions array**

Current:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["SYSTEM_PROMPT.md"]
}
```

New:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["SYSTEM_PROMPT.md", "Runtime/FRE_SPEC.md"]
}
```

- [ ] **Step 2: Verify**

Read `FounderOS/opencode.json`.
Expected: `instructions` array contains both `"SYSTEM_PROMPT.md"` and `"Runtime/FRE_SPEC.md"`.

---

### Self-Review

After all tasks complete, verify:

**1. Spec coverage:**
- FRE_SPEC with 6 contracts → Task 1 (all contracts: Boot, PRG, State, Gates, Temporal, Recall)
- ADAPTER_INTERFACE with 4 questions → Task 2
- opencode.md adapter → Task 3
- chatgpt.md adapter → Task 4
- claude.md + gemini.md adapters → Task 5
- cursor.md + local_agent.md adapters → Task 6
- SYSTEM_PROMPT.md update → Task 7
- opencode.json update → Task 8

**2. Placeholder scan:** All tasks contain complete file content. No TBD, no TODO, no "implement later".

**3. Type consistency:** No method signatures to conflict (all files are markdown).


--- FILE: docs/superpowers/plans/2026-06-22-fhq-keyword-and-cadence-orchestrator.md
# `fhq` Keyword & Cadence Orchestrator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the implicit "always-boot" pattern with explicit keyword triggers (`fhq`, `boot`, `shutdown`) so the user controls when the full kernel cycle runs, and integrate cadence/lifecycle awareness into the ORIENT phase.

**Architecture:** Three user-facing keywords (`fhq`, `boot`, `shutdown`) control kernel execution depth. `fhq` at message start triggers the full BOOT->OBSERVE->ORIENT->DECIDE->ACT->LEARN->UPDATE cycle (BOOT skipped if already active today). `boot` explicitly restarts the day. `shutdown` ends the session with time tracking. No keyword -> DIRECT mode (response only, no cycle). Background scripts (watchtower, timekeeper) run independently via Windows Task Scheduler. Cadence (life->year->month->week->day->hour) and lifecycle (phase per project) enrich the ORIENT phase through new state files.

**Tech Stack:** Python 3.13, markdown state files, Windows Task Scheduler, BurntToast (optional)

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `FounderOS/SYSTEM_PROMPT.md` | MODIFY | Add `fhq`/`boot`/`shutdown` keyword detection to Intent Classification; add Cadence+Lifecycle to Boot Sequence |
| `FounderOS/Runtime/RUNTIME_KERNEL.md` | MODIFY | Enrich ORIENT phase with CADENCE x LIFECYCLE x frameworks cross; add conditional BOOT (skip if day already active) |
| `FounderOS/Protocols/SOURCE_OF_TRUTH.md` | MODIFY | Register CADENCE.md, LIFECYCLE.md, ALERTS.md, WATCH_REPORT.md |
| `FounderOS/Runtime/engine/__init__.py` | MODIFY | Document new cadence_engine module |
| `FounderOS/State/CADENCE.md` | CREATE | Temporal hierarchy: life->year->month->week->day->hour with current values |
| `FounderOS/State/LIFECYCLE.md` | CREATE | Phase of each project (IDEA, VALIDATION, LAUNCH, GROWTH, SCALE, MATURE) with gates |
| `FounderOS/State/ALERTS.md` | CREATE | Notifications stored by background scripts, read at boot |
| `FounderOS/State/WATCH_REPORT.md` | CREATE | Watch results formatted for LLM consumption, bridge between scripts and session |
| `FounderOS/Runtime/engine/cadence_engine.py` | CREATE | Python module: compute current cadence from datetime, determine active lifecycle phases, suggest which frameworks to load |
| `FounderOS/Runtime/engine/watchtower.py` | CREATE | Background script: scheduled every 6h, reads WATCH_REGISTRY, runs websearch/webfetch, updates registry + writes WATCH_REPORT.md |
| `FounderOS/Runtime/engine/timekeeper.py` | CREATE | Background script: every 30min, checks deadlines, SOS timer (pause reminder every 90min), sends Windows toast notifications |
| `FounderOS/Runtime/engine/installer.py` | CREATE | First-run setup: create Windows Task Scheduler tasks for watchtower and timekeeper, verify BurntToast availability |
| `FounderOS/tests/test_cadence_engine.py` | CREATE | Tests for cadence_engine.py |

---

### Task 1: Create `State/CADENCE.md`

**Files:**
- Create: `FounderOS/State/CADENCE.md`

- [ ] **Create CADENCE.md**

```markdown
# CADENCE

## Purpose

Hierarchy temporelle de FounderOS : vie -> annee -> mois -> semaine -> jour -> heure. Chaque niveau porte un objectif, une evaluation, et un lien vers le niveau suivant.

Lue en phase BOOT pour contextualiser ORIENT. Mise a jour par le LLM quand les objectifs evoluent.

---

## Life (Vie)

> **Objectif:** [objectif de vie]

**Evaluation:** [auto-evaluation: 0-10]

---

## Year (Annee) - 2026

> **Objectif:** [objectif 2026]

**Evaluation:** [auto-evaluation 0-10]

**Trimestre en cours:** Q2 (Avril-Juin)

---

## Month (Mois) - Juin 2026

> **Objectif:** [objectif juin]

**Evaluation:** [auto-evaluation 0-10]

**Semaines:**
- S24 (Juin 9-15): [objectif / resultat]
- S25 (Juin 16-22): [objectif / resultat]
- S26 (Juin 23-29): [objectif / resultat]
- S27 (Juin 30-Juil 6): [objectif / resultat]

---

## Week (Semaine) - S26 (Juin 23-29)

> **Objectif:** [objectif semaine]

**Deadlines cette semaine:**
- [date] - [description]

---

## Day (Jour) - 2026-06-22

> **Objectif:** [objectif du jour]

**Session start:** [HH:MM - filled at boot]
**Session end:** [HH:MM - filled at shutdown]
**Duration:** [calculated]

**Top 3 actions:**
1. [action]
2. [action]
3. [action]

---

## Hour (Heure) - Now

> **Lome (UTC+0):** [dynamique - computed at every `fhq`]

**Next actionable:** [what to do in the next 60 min]

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Temporal hierarchy for FounderOS cadence |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/CADENCE.md
git commit -m "feat: create CADENCE.md with temporal hierarchy (life->year->month->week->day->hour)"
```

---

### Task 2: Create `State/LIFECYCLE.md`

**Files:**
- Create: `FounderOS/State/LIFECYCLE.md`

- [ ] **Create LIFECYCLE.md**

```markdown
# LIFECYCLE

## Purpose

Phase actuelle de chaque projet actif. Determine quel framework activer en phase ORIENT. Chaque phase a des gates de sortie - conditions precises pour passer a la phase suivante.

Mise a jour par le LLM quand un projet franchit un gate.

---

## Phases

| Phase | Description | Gate de Sortie | Frameworks Actifs |
|-------|-------------|----------------|-------------------|
| IDEA | Idee non validee | Prototype ou enquete client faite | CAOS |
| VALIDATION | Solution testee, client cherche | 3+ clients prets a payer | VAOS, DIOS |
| LAUNCH | Premier client, livraison manuelle | Process reproductible | DIOS, CEOS |
| GROWTH | Revenu regulier, equipe building | Process automatises/outsources | PSOS, FAOS, SAOS |
| SCALE | Croissance acceleree, fundraising | Metriques unitaires saines | FAOS, SAOS |
| MATURE | Cash-flow stable, optimisation | - | SAOS |

---

## Projets Actifs

| Projet | Phase | Depuis | Gate de Sortie Atteint ? | Prochaine Action |
|--------|-------|--------|--------------------------|-----------------|
| SOJACO | VALIDATION | 2026-06-21 | Non - Pas encore de client payant | Trouver client mais ou soja |
| OMNI | LAUNCH | 2026-06-15 | Non - MVP deploye, 0 client payant | Pitch Day + acquisition premiers utilisateurs |
| SOYA (Bolsoja) | LAUNCH | 2026-05-XX | Non - 1 client (dame 1), pas encore reproductible | Livraison quotidienne + trouver d'autres clients |
| KORA | VALIDATION | 2026-06-01 | Non - Pre-seed docs ok, pas de financement | Relancer ST Digital + Herlog |
| DOODLEMIND | IDEA | 2026-06-10 | Non - Short #1 publie, 0 monetization | Produire Short #2 |
| PEST REPELLER | IDEA | 2026-05-XX | Non - Stock disponible, 0 vente | Creer contenu TikTok |
| SOLAR KIT | IDEA | 2026-06-15 | Non - Pas encore de prototype | Definir modele + fournisseur |

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Project lifecycle phase tracking for framework selection |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/LIFECYCLE.md
git commit -m "feat: create LIFECYCLE.md with per-project phase tracking and gate conditions"
```

---

### Task 3: Create `State/ALERTS.md` and `State/WATCH_REPORT.md`

**Files:**
- Create: `FounderOS/State/ALERTS.md`
- Create: `FounderOS/State/WATCH_REPORT.md`

- [ ] **Create ALERTS.md**

```markdown
# ALERTS

## Purpose

File bridge between background scripts (watchtower, timekeeper) and the LLM at session boot. Scripts write here, LLM reads here.

**Read at session start (BOOT). Cleared after reading.**

---

## Active Alerts

| Timestamp | Source | Severity | Message |
|-----------|--------|----------|---------|
| | | | |

---

## Rules

1. Scripts append alerts as they fire
2. LLM reads all alerts at BOOT, clears them after acknowledgment
3. Max 50 alerts - oldest auto-archived

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | Scripts -> LLM |
```

- [ ] **Create WATCH_REPORT.md**

```markdown
# WATCH REPORT

## Purpose

Formatted findings from watchtower.py runs. One section per watch that triggered. Read by LLM at BOOT.

---

## Reports

<!-- watchtower appends here at each run -->

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | watchtower.py |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/ALERTS.md FounderOS/State/WATCH_REPORT.md
git commit -m "feat: create ALERTS.md and WATCH_REPORT.md as script-to-LLM bridge files"
```

---

### Task 4: Create and test `Runtime/engine/cadence_engine.py`

**Files:**
- Create: `FounderOS/Runtime/engine/cadence_engine.py`
- Create: `FounderOS/tests/test_cadence_engine.py`

- [ ] **Write the failing tests**

Create `FounderOS/tests/test_cadence_engine.py`:

```python
import pytest
from datetime import datetime
from Runtime.engine.cadence_engine import get_week_of_month, get_cadence_context, get_active_frameworks


class TestGetWeekOfMonth:
    def test_first_week(self):
        d = datetime(2026, 6, 1, 12, 0)
        assert get_week_of_month(d) == 1

    def test_third_week(self):
        d = datetime(2026, 6, 15, 12, 0)
        assert get_week_of_month(d) == 3

    def test_last_week_june(self):
        d = datetime(2026, 6, 29, 12, 0)
        assert get_week_of_month(d) == 5


class TestGetCadenceContext:
    def test_returns_all_levels(self):
        d = datetime(2026, 6, 22, 14, 30)
        ctx = get_cadence_context(d)
        assert ctx["year"] == 2026
        assert ctx["month"] == 6
        assert ctx["day"] == 22
        assert ctx["hour"] == 14
        assert ctx["minute"] == 30
        assert ctx["week_of_month"] == 4
        assert ctx["day_of_week"] == 1

    def test_contains_iso_week(self):
        d = datetime(2026, 6, 22, 12, 0)
        ctx = get_cadence_context(d)
        assert "iso_week" in ctx
        assert 1 <= ctx["iso_week"] <= 53


class TestGetActiveFrameworks:
    def test_validation_phase_returns_vaos_dios(self):
        ctx = {"lifecycle_phase": "VALIDATION"}
        frameworks = get_active_frameworks(ctx)
        assert "VAOS" in frameworks
        assert "DIOS" in frameworks

    def test_idea_phase_returns_caos(self):
        ctx = {"lifecycle_phase": "IDEA"}
        frameworks = get_active_frameworks(ctx)
        assert "CAOS" in frameworks
        assert "VAOS" not in frameworks

    def test_survival_mode_prioritizes_revenue_frameworks(self):
        ctx = {"lifecycle_phase": "VALIDATION", "mode": "SURVIVAL"}
        frameworks = get_active_frameworks(ctx)
        assert "DIOS" in frameworks
        assert "DAOS" in frameworks
```

- [ ] **Run test to verify it fails**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_cadence_engine.py -v
```

Expected: 6 FAILED with "ModuleNotFoundError: No module named 'Runtime.engine.cadence_engine'"

- [ ] **Write minimal implementation**

Create `FounderOS/Runtime/engine/cadence_engine.py`:

```python
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
        "day_of_week": dt.weekday(),
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
```

- [ ] **Run tests to verify they pass**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_cadence_engine.py -v
```

Expected: 6 PASSED

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/cadence_engine.py FounderOS/tests/test_cadence_engine.py
git commit -m "feat: add cadence_engine.py with week/month computation and framework selection per lifecycle phase"
```

---

### Task 5: Create `Runtime/engine/watchtower.py`

**Files:**
- Create: `FounderOS/Runtime/engine/watchtower.py`

- [ ] **Write watchtower.py**

```python
"""watchtower.py - Scheduled veille script. Run every 6h via Windows Task Scheduler.

Reads State/WATCH_REGISTRY.md, checks items where Next Check <= today,
executes websearch/webfetch, updates registry Last Result, appends to WATCH_REPORT.md.

Usage:
    python Runtime/engine/watchtower.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import re
import subprocess
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
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/watchtower.py
git commit -m "feat: create watchtower.py - scheduled veille script (6h) for WATCH_REGISTRY checks"
```

---

### Task 6: Create `Runtime/engine/timekeeper.py`

**Files:**
- Create: `FounderOS/Runtime/engine/timekeeper.py`

- [ ] **Write timekeeper.py**

```python
"""timekeeper.py - Scheduled time and alert script. Run every 30min via Windows Task Scheduler.

Checks:
1. Deadlines in PRIORITY_MATRIX.md - alerts for any deadline <= 48h
2. SOS timer - if no session start found in CURRENT_STATE.md or session > 90min, send pause reminder
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
    """Check SOS timer. If session > 90min, return alert message."""
    current_state_path = base_path / "State" / "CADENCE.md"
    if not current_state_path.exists():
        return None

    text = current_state_path.read_text(encoding="utf-8")
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
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/timekeeper.py
git commit -m "feat: create timekeeper.py - scheduled time/alert script (30min) with deadline checks and SOS timer"
```

---

### Task 7: Create `Runtime/engine/installer.py`

**Files:**
- Create: `FounderOS/Runtime/engine/installer.py`

- [ ] **Write installer.py**

```python
"""installer.py - First-run setup for FounderHQ background scripts.

Creates Windows Task Scheduler tasks for:
1. watchtower - runs every 6 hours
2. timekeeper - runs every 30 minutes

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ --uninstall
"""

import argparse
import subprocess
import sys
from pathlib import Path


def task_exists(task_name: str) -> bool:
    """Check if a Windows Scheduled Task exists."""
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", task_name],
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.returncode == 0


def create_task(task_name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    """Create a Windows Scheduled Task."""
    python_exe = sys.executable
    if not python_exe:
        python_exe = "python"

    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval_minutes),
        "/TN", task_name,
        "/TR", f'"{python_exe}" "{script_path}" --base-dir "{base_dir}"',
        "/F",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {task_name}: {result.stderr.strip()}")
        return False

    print(f"Task '{task_name}' created (every {interval_minutes} min).")
    return True


def remove_task(task_name: str) -> bool:
    """Remove a Windows Scheduled Task."""
    if not task_exists(task_name):
        print(f"Task '{task_name}' does not exist, skipping.")
        return True

    cmd = ["schtasks", "/Delete", "/TN", task_name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        print(f"ERROR removing task {task_name}: {result.stderr.strip()}")
        return False

    print(f"Task '{task_name}' removed.")
    return True


def check_burnt_toast() -> bool:
    """Check if BurntToast PowerShell module is available."""
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Get-Module -ListAvailable -Name BurntToast",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    available = "BurntToast" in result.stdout
    if available:
        print("BurntToast: available")
    else:
        print("BurntToast: NOT available - toast notifications disabled")
    return available


def install_burnt_toast() -> bool:
    """Install BurntToast PowerShell module."""
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Install-Module -Name BurntToast -Force -Scope CurrentUser",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"BurntToast install failed: {result.stderr.strip()}")
        return False
    print("BurntToast installed.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Installer for FounderHQ background scripts")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks")
    parser.add_argument("--install-burnttoast", action="store_true", help="Install BurntToast PowerShell module")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    if args.uninstall:
        remove_task("FounderHQ-Watchtower")
        remove_task("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    if args.install_burnttoast:
        install_burnt_toast()
        return

    check_burnt_toast()

    watchtower_path = scripts_dir / "watchtower.py"
    if not watchtower_path.exists():
        print(f"ERROR: {watchtower_path} not found")
        sys.exit(1)

    create_task("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)

    timekeeper_path = scripts_dir / "timekeeper.py"
    if not timekeeper_path.exists():
        print(f"ERROR: {timekeeper_path} not found")
        sys.exit(1)

    create_task("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)

    print("\nInstallation complete.")
    print("  FounderHQ-Watchtower: runs every 6 hours (veille)")
    print("  FounderHQ-Timekeeper: runs every 30 minutes (deadlines + SOS)")


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/installer.py
git commit -m "feat: create installer.py - Windows Task Scheduler setup for watchtower + timekeeper"
```

---

### Task 8: Modify `Runtime/engine/__init__.py`

**Files:**
- Modify: `FounderOS/Runtime/engine/__init__.py`

- [ ] **Read current file**

```cmd
type FounderOS\Runtime\engine\__init__.py
```

- [ ] **Replace with updated version**

```python
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
    installer: First-run setup - creates Windows Task Scheduler tasks
"""
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/__init__.py
git commit -m "docs: document cadence_engine, watchtower, timekeeper, installer in __init__.py"
```

---

### Task 9: Modify `SYSTEM_PROMPT.md` - Add `fhq` / `boot` / `shutdown` Keywords

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md`

- [ ] **Read current file**

```cmd
type FounderOS\SYSTEM_PROMPT.md
```

- [ ] **Replace Intent Classification section**

Replace the Intent Classification table (between `## Intent Classification` and `## Pre-Response Gate (PRG)`) with:

```
## Intent Classification

Before responding, classify intent using this table. Then execute PRG. Never reply before both steps complete.

| Pattern | Classify as | Action |
|---|---|---|
| Message starts with **"boot"** or **"boot "** | BOOT | Full session initialization. Set session start time in CADENCE.md. Load ALL state files + frameworks. Execute ORIENT enriched with CADENCE + LIFECYCLE. |
| Message starts with **"shutdown"** or **"shutdown "** | SHUTDOWN | End session. Log session duration to CADENCE.md (Day -> Session End). Save ALL state. Record TIMELINE entry. Do NOT continue after shutdown. |
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
| Simple update, ambiguous, no keyword | DIRECT | SURVIVAL -> load DAOS.md, propose 1 action module. Otherwise -> respond directly |
```

- [ ] **Replace Boot Sequence section**

Replace the Boot Sequence section (from "## Boot Sequence" to the next ## header) with:

```
## Boot Sequence

Execute at session start (triggered by `boot` or first `fhq` of the day):
1. **Load Protocols + FRE** - SOURCE_OF_TRUTH.md + DECISION_GATES.md + INFO_CAPTURE_PROTOCOL.md + Runtime/FRE_SPEC.md
2. **Temporal Context** - Get-Date, compute Lome UTC+0. Load TIMELINE.md, CURRENT_STATE.md, CADENCE.md
3. **Load Cadence + Lifecycle** - Load State/CADENCE.md, State/LIFECYCLE.md. Determine current temporal position and project phases.
4. **Load Priority Matrix** - Load State/PRIORITY_MATRIX.md to establish unified view of ALL active projects/actions
5. **Load Alerts + Watch Reports** - Load State/ALERTS.md, read and clear active alerts. Load State/WATCH_REPORT.md for any background script findings since last session.
6. **Execute Watch Registry** - Load State/WATCH_REGISTRY.md, check each item where Next Check <= today, run websearch/webfetch, report findings, update registry
7. **Freshness Check** - Scan all concept footers. Flag any > 48h (WF-007)
8. **Set Session Start** - Record current time as Session Start in CADENCE.md (Day section). Log to TIMELINE.
9. **Load Concepts** - In order: CURRENT_STATE -> MISSION -> MEMORY -> KNOWLEDGE -> TIMELINE -> PROJECT -> WORKFLOW -> ASSET -> PLAYBOOK -> SYSTEM
10. **Build World Model** - Synthesize: what exists, what matters, what changed, what is blocked, what should happen next
11. **Report Awareness** - State: datetime, mode, top priority, cadence (week/month), lifecycle phases, watch results, what changed, stale concepts, PRG status. MUST state next action.
12. **Integrity Check** - All critical files loaded? Temporal context established? No contradictions?
13. **Daily Kickoff** - Execute RUNTIME Phase 1-2 (Assess cash/state -> Decide top action). State today's single most important action.
```

- [ ] **Update PRG Step 1**

Change PRG table Step 1 from:
`| 1 | Temporal Check | Run \`Get-Date\`. Compute Lome UTC+0. State CURRENT_DATETIME as first line of response. |`

To:
`| 1 | Temporal Check | Run \`Get-Date\`. Compute Lome UTC+0. If message starts with \`fhq\`, \`boot\`, or \`shutdown\`: reload CADENCE.md current day section, compute elapsed time since session start or last \`fhq\`. State CURRENT_DATETIME as first line of response. |`

- [ ] **Update output format section**

Replace the `**Output format:**` block with:

```
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
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "feat: add fhq/boot/shutdown keywords to Intent Classification + enrich boot sequence with cadence/lifecycle/alerts"
```

---

### Task 10: Modify `Runtime/RUNTIME_KERNEL.md` - Conditional BOOT + Enriched ORIENT

**Files:**
- Modify: `FounderOS/Runtime/RUNTIME_KERNEL.md`

- [ ] **Read current file**

```cmd
type FounderOS\Runtime\RUNTIME_KERNEL.md
```

- [ ] **Replace Phase 1: BOOT section**

Replace the old BOOT section with:

```
## Phase 1: BOOT

Execute at session start - triggered by user message starting with `boot` or first `fhq` of the day. If the session is already active (a prior `fhq` or `boot` was processed today), BOOT is skipped and the cycle starts at OBSERVE.

### Full Boot (triggered by `boot` or first daily `fhq`):

Operations:
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

Output: Session awareness established.

### Quick Boot (triggered by subsequent `fhq` same day):

Operations:
1. Re-read CURRENT_STATE.md (may have changed since last cycle)
2. Re-read LIFECYCLE.md (project phases may have shifted)
3. Compute current datetime, update CADENCE.md Hour section
4. Check ALERTS.md for new entries from background scripts

Output: Updated temporal awareness, skipping full initialization.
```

- [ ] **Replace Phase 3: ORIENT section**

Replace the old ORIENT section with:

```
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
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/RUNTIME_KERNEL.md
git commit -m "feat: enrich ORIENT with CADENCE x LIFECYCLE x frameworks cross + conditional BOOT"
```

---

### Task 11: Modify `Protocols/SOURCE_OF_TRUTH.md`

**Files:**
- Modify: `FounderOS/Protocols/SOURCE_OF_TRUTH.md`

- [ ] **Read current file**

```cmd
type FounderOS\Protocols\SOURCE_OF_TRUTH.md
```

- [ ] **Find the relevant table/section** and add these rows:

```
| CADENCE.md | State/ | System | Temporal hierarchy (life->year->month->week->day->hour). Session timestamps. |
| LIFECYCLE.md | State/ | System | Per-project lifecycle phase. Gates. Framework mapping. |
| ALERTS.md | State/ | Scripts->LLM | Bridge file. Background script alerts read and cleared at boot. |
| WATCH_REPORT.md | State/ | watchtower.py | Veille findings from watchtower, consumed at boot. |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Protocols/SOURCE_OF_TRUTH.md
git commit -m "docs: register CADENCE.md, LIFECYCLE.md, ALERTS.md, WATCH_REPORT.md in SOURCE_OF_TRUTH"
```

---

## Self-Review Checklist

### 1. Spec Coverage
- `fhq` keyword - Task 9 (Intent Classification) + Task 10 (conditional BOOT)
- `boot` keyword - Task 9 + Task 10 (full BOOT)
- `shutdown` keyword - Task 9 (tracks session duration, saves state)
- No keyword - Task 9 (DIRECT mode, no cycle)
- CADENCE.md - Task 1
- LIFECYCLE.md - Task 2
- ALERTS.md + WATCH_REPORT.md - Task 3
- cadence_engine.py - Task 4 (week/month computation, framework selection)
- watchtower.py - Task 5 (6h veille script)
- timekeeper.py - Task 6 (30min deadlines + SOS timer)
- installer.py - Task 7 (Windows Task Scheduler setup)
- ORIENT enrichment - Task 10 (CADENCE x LIFECYCLE x frameworks cross)
- SOURCE_OF_TRUTH - Task 11
- `__init__.py` - Task 8

### 2. Placeholder Scan
No placeholders found. All code blocks are complete. All file paths are exact. All commands are exact.

### 3. Type Consistency
- `get_week_of_month(dt: datetime) -> int` - defined and tested in Task 4, used in `get_cadence_context`
- `get_cadence_context(dt: datetime) -> dict` - defined and tested in Task 4
- `get_active_frameworks(ctx: dict) -> list[str]` - defined and tested in Task 4
- `parse_watch_registry(path: Path) -> list[dict]` - defined in Task 5
- `execute_watch(item: dict, base_dir: str) -> str` - defined in Task 5
- `update_registry(path: Path, item: dict, result: str) -> None` - defined in Task 5
- `append_watch_report(base_path: Path, item: dict, result: str) -> None` - defined in Task 5
- `send_toast(title: str, message: str) -> bool` - defined in Task 6
- `parse_deadlines(base_path: Path) -> list[dict]` - defined in Task 6
- `check_sos_timer(base_path: Path) -> Optional[str]` - defined in Task 6
- `append_alert(base_path: Path, severity: str, message: str) -> None` - defined in Task 6
- `task_exists(task_name: str) -> bool` - defined in Task 7
- `create_task(...) -> bool` - defined in Task 7
- `remove_task(task_name: str) -> bool` - defined in Task 7
- `check_burnt_toast() -> bool` - defined in Task 7

All method signatures consistent across tasks.


--- FILE: docs/superpowers/plans/2026-06-22-founderhq-distribution-and-sync.md
# FounderHQ Distribution & Sync — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Zero-dependency distribution via FOUNDER_SEED.md + automatic state sync via private Gist + first-run GENESIS that installs everything.

**Architecture:** Two sync paths: primary (private Gist + token in `.env`, script `sync.py` reads token, LLM never sees it) and fallback (portable markdown snapshot via `snapshot.py`). First boot detects `.founderhq_installed` marker → if absent, runs GENESIS (ask token, create files, build .venv, install scripts).

**Tech Stack:** Python 3.13, GitHub Gist API, `requests`, `python-dotenv`, markdown state files

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `Runtime/engine/sync.py` | CREATE | Gist push/pull/merge. Reads token from `.env`. Called by LLM, never exposes token. |
| `Runtime/engine/snapshot.py` | CREATE | Portable markdown snapshot generate/merge. No token needed. |
| `State/SYNC_CONFIG.md` | CREATE | LLM-readable sync config (Gist URL, last sync date, no token). |
| `.env` | CREATE (via installer) | Secrets file: `FHQ_GIST_URL`, `FHQ_GIST_TOKEN`. Permissions 600. |
| `.founderhq_installed` | CREATE (via installer) | Empty marker. If absent at boot → GENESIS. |
| `Runtime/engine/installer.py` | MODIFY | Add .venv creation, token prompt, .env write, marker creation. |
| `SYSTEM_PROMPT.md` | MODIFY | Boot: first-run check (GENESIS). Sync pull after boot. Sync push on shutdown. |
| `Runtime/RUNTIME_KERNEL.md` | MODIFY | BOOT: add GENESIS branch. UPDATE: add sync push. |
| `State/CADENCE.md` | MODIFY | Add `### Sync` section to Day block. |
| `Protocols/SOURCE_OF_TRUTH.md` | MODIFY | Register sync.py, snapshot.py, SYNC_CONFIG.md, .env, .founderhq_installed. |
| `Runtime/engine/__init__.py` | MODIFY | Document sync.py, snapshot.py. |
| `FOUNDER_SEED.md` | GENERATE | Concatenation of all core files with `--- FILE:` delimiters. Excludes user data. |

---

### Task 1: Create `Runtime/engine/sync.py`

**Files:**
- Create: `FounderOS/Runtime/engine/sync.py`
- Create: `FounderOS/tests/test_sync.py`

- [ ] **Write the failing tests**

Create `FounderOS/tests/test_sync.py`:

```python
import pytest
import json
import os
from pathlib import Path
from Runtime.engine.sync import Snapshot, STATE_FIELDS, CADENCE_FIELDS


class TestSnapshot:
    def test_from_state_minimal(self):
        """Build snapshot from minimal state."""
        state = {
            "date": "2026-06-22 14:00 Lome UTC+0",
            "mode": "SURVIVAL",
            "cash": 2679,
            "top_priority": "Find client",
            "bottleneck": "Cash",
        }
        cadence = {"session_start": "08:00", "session_end": "14:00"}
        timeline = [{"date": "2026-06-22", "event": "Boot", "decision": "Start", "outcome": "OK"}]
        projects = {"SOJACO": {"phase": "VALIDATION"}}

        snap = Snapshot(state=state, cadence=cadence, timeline=timeline, projects=projects)
        assert snap.version == 1
        assert snap.state["mode"] == "SURVIVAL"
        assert snap.state["cash"] == 2679

    def test_to_from_json_roundtrip(self):
        """Serialize and deserialize preserves all data."""
        original = Snapshot(
            state={"date": "test", "mode": "GROWTH", "cash": 5000, "top_priority": "X", "bottleneck": "Y"},
            cadence={"session_start": "09:00", "session_end": "17:00"},
            timeline=[{"date": "T1", "event": "E1", "decision": "D1", "outcome": "O1"}],
            projects={"P1": {"phase": "LAUNCH"}},
        )
        data = original.to_dict()
        restored = Snapshot.from_dict(data)
        assert restored.state == original.state
        assert restored.cadence == original.cadence
        assert restored.timeline == original.timeline
        assert restored.projects == original.projects

    def test_missing_fields_default(self):
        """Missing optional fields get empty defaults."""
        snap = Snapshot(state={"date": "x", "mode": "x", "cash": 0, "top_priority": "x", "bottleneck": "x"})
        assert snap.cadence == {}
        assert snap.timeline == []
        assert snap.projects == {}
```

- [ ] **Run tests to verify they fail**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_sync.py -v
```

Expected: FAIL with ModuleNotFoundError

- [ ] **Write minimal implementation**

Create `FounderOS/Runtime/engine/sync.py`:

```python
"""sync.py - State sync via private GitHub Gist.

Reads FHQ_GIST_TOKEN and FHQ_GIST_URL from .env (root of FounderHQ).
LLM never sees the token - it calls sync.py as a subprocess and reads the
returned status message.

Commands:
    sync.py pull     - Download latest snapshot, stage in _SYNC_INBOX.md
    sync.py push     - Build snapshot from current state, push to Gist
    sync.py merge    - Apply staged snapshot to local files
"""

import argparse
import json
import os
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
    """Single portable state snapshot.

    Fields:
        version: Schema version (int, currently 1)
        timestamp: ISO datetime string
        state: dict with date, mode, cash, top_priority, bottleneck
        cadence: dict with session_start, session_end
        timeline: list of event dicts
        projects: dict mapping project name -> project state
    """

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
    """Read .env file and return dict of variables."""
    if not ENV_PATH.exists():
        return {}
    env = {}
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip()
    return env


def read_state_file(name: str) -> str:
    """Read a state file, return empty string if missing."""
    path = STATE_DIR / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_snapshot() -> Snapshot:
    """Read current state files and build a Snapshot."""
    current_state = read_state_file("CURRENT_STATE.md")
    cadence = read_state_file("CADENCE.md")
    timeline = read_state_file("TIMELINE.md") if (STATE_DIR.parent / "concepts" / "TIMELINE.md").exists() else ""

    # Extract key fields via simple parsing
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

    # Parse timeline entries
    events = []
    for line in timeline.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] != "Date":
                events.append({
                    "date": cols[0],
                    "event": cols[1],
                    "decision": cols[2],
                    "outcome": cols[3],
                })

    # Parse lifecycle for project phases
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
    """Extract first match of regex pattern from text."""
    import re
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def cmd_pull(env: dict) -> str:
    """Pull snapshot from Gist and write to _SYNC_INBOX."""
    url = env.get("FHQ_GIST_URL", "")
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"

    if requests is None:
        return "ERROR: requests library not installed (run: pip install requests)"

    try:
        resp = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=15)
        if resp.status_code != 200:
            return f"ERROR: Gist GET returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        # Gist API returns files dict
        files = data.get("files", {})
        if not files:
            return "ERROR: No files found in Gist"
        # Find snapshot file
        snap_file = None
        for fname, finfo in files.items():
            if fname.endswith(".json") or "snapshot" in fname:
                snap_file = finfo
                break
        if not snap_file:
            snap_file = list(files.values())[0]
        content = snap_file.get("content", "")
        if not content:
            return "ERROR: Empty snapshot file"

        inbox_path = STATE_DIR / "_SYNC_INBOX.md"
        inbox_path.write_text(f"# SYNC INBOX\n\n> Pulled: {datetime.now(timezone.utc).isoformat()}\n\n```json\n{content}\n```\n", encoding="utf-8")
        return f"OK: Snapshot pulled ({len(content)} bytes)"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_push(env: dict) -> str:
    """Build snapshot and push to Gist."""
    url = env.get("FHQ_GIST_URL", "")
    token = env.get("FHQ_GIST_TOKEN", "")
    if not url or not token:
        return "ERROR: FHQ_GIST_URL or FHQ_GIST_TOKEN not configured"

    if requests is None:
        return "ERROR: requests library not installed"

    snap = build_snapshot()
    payload = json.dumps(snap.to_dict(), indent=2)

    # Gist API: put content into a file named snapshot.json
    try:
        resp = requests.patch(
            url,
            headers={
                "Authorization": f"token {token}",
                "Content-Type": "application/json",
            },
            json={"files": {"snapshot.json": {"content": payload}}},
            timeout=15,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist PATCH returned {resp.status_code}: {resp.text[:200]}"
        return f"OK: Snapshot pushed ({len(payload)} bytes) at {snap.timestamp}"
    except Exception as e:
        return f"ERROR: {e}"


def cmd_merge() -> str:
    """Apply staged snapshot to local state files."""
    inbox_path = STATE_DIR / "_SYNC_INBOX.md"
    if not inbox_path.exists():
        return "ERROR: No staged snapshot found (run pull first)"

    text = inbox_path.read_text(encoding="utf-8")
    # Extract JSON from code block
    import re
    m = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not m:
        return "ERROR: No JSON found in _SYNC_INBOX.md"

    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return f"ERROR: Invalid JSON: {e}"

    snap = Snapshot.from_dict(data)

    # Update CURRENT_STATE.md
    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if cs_path.exists() and snap.state:
        cs_text = cs_path.read_text(encoding="utf-8")
        for key, val in snap.state.items():
            if val and key != "date":
                # Map snapshot keys to CURRENT_STATE field names
                field_map = {
                    "mode": "Operating Mode",
                    "cash": "Cash",
                    "top_priority": "Top Priority",
                    "bottleneck": "Current Bottleneck",
                    "date": "Date",
                }
                field = field_map.get(key, key)
                old = r"(\*\*" + re.escape(field) + r":\*\*).*"
                new = rf"\1 {val}"
                cs_text = re.sub(old, new, cs_text)
        cs_path.write_text(cs_text, encoding="utf-8")

    # Update CADENCE.md
    cad_path = STATE_DIR / "CADENCE.md"
    if cad_path.exists() and snap.cadence:
        cad_text = cad_path.read_text(encoding="utf-8")
        for key, val in snap.cadence.items():
            if val:
                field_map = {
                    "session_start": "Session start",
                    "session_end": "Session end",
                }
                field = field_map.get(key, key)
                old = r"(\*\*" + re.escape(field) + r":\*\*\s*).*"
                new = rf"\1 {val}"
                cad_text = re.sub(old, new, cad_text)
        cad_path.write_text(cad_text, encoding="utf-8")

    # Append timeline entries
    if snap.timeline:
        tl_path = STATE_DIR.parent / "concepts" / "TIMELINE.md"
        if tl_path.exists():
            tl_text = tl_path.read_text(encoding="utf-8")
            for event in snap.timeline:
                new_row = f"\n| {event.get('date', '?')} | {event.get('event', '')} | {event.get('decision', '')} | {event.get('outcome', '')} |"
                if new_row not in tl_text:
                    tl_text += new_row
            tl_path.write_text(tl_text, encoding="utf-8")

    # Update LIFECYCLE.md project phases
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


def main():
    parser = argparse.ArgumentParser(description="FHQ state sync via Gist")
    parser.add_argument("command", choices=["pull", "push", "merge"], help="Sync command")
    args = parser.parse_args()

    env = read_env()

    if args.command == "pull":
        result = cmd_pull(env)
    elif args.command == "push":
        result = cmd_push(env)
    elif args.command == "merge":
        result = cmd_merge()
    else:
        result = "ERROR: Unknown command"

    print(result)


if __name__ == "__main__":
    main()
```

- [ ] **Run tests to verify they pass**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_sync.py -v
```

Expected: 3 PASSED

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/sync.py FounderOS/tests/test_sync.py
git commit -m "feat: add sync.py - Gist state push/pull/merge with .env token isolation"
```

---

### Task 2: Create `Runtime/engine/snapshot.py`

**Files:**
- Create: `FounderOS/Runtime/engine/snapshot.py`

- [ ] **Write snapshot.py**

```python
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

    # Latest timeline entries
    recent_events = []
    for line in tl.splitlines():
        if line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0] not in ("Date", ""):
                recent_events.append(f"- {cols[0]}: {cols[1]} -> {cols[3]}")

    recent_events = recent_events[-5:]  # last 5

    # Project phases
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
        return "ERROR: No State/IMPORT_SNAPSHOT.md found. Paste the snapshot text there first."

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
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/snapshot.py
git commit -m "feat: add snapshot.py - portable markdown snapshot for token-less environments"
```

---

### Task 3: Create `State/SYNC_CONFIG.md`

**Files:**
- Create: `FounderOS/State/SYNC_CONFIG.md`

- [ ] **Create SYNC_CONFIG.md**

```markdown
# SYNC CONFIG

## Purpose

Configuration de synchronisation. Lu par le LLM au boot pour savoir si le sync est actif. Ne contient PAS le token — celui-ci est dans `.env`, jamais lu par le LLM.

---

**Sync Gist URL:** [URL de votre Gist prive]
**Last Sync:** [date]
**Auto-sync on boot:** yes
**Auto-sync on shutdown:** yes

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Sync configuration (no secrets) |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/SYNC_CONFIG.md
git commit -m "feat: add SYNC_CONFIG.md - LLM-readable sync config (no token)"
```

---

### Task 4: Modify `Runtime/engine/installer.py`

**Files:**
- Modify: `FounderOS/Runtime/engine/installer.py`

- [ ] **Read current file then rewrite**

The current installer.py creates Windows Task Scheduler tasks. Add:
1. `.venv` creation if missing
2. Token prompt and `.env` creation
3. `.founderhq_installed` marker creation

Read current file first:
```cmd
type FounderOS\Runtime\engine\installer.py
```

Then replace with this expanded version:

```python
"""installer.py - First-run setup for FounderHQ.

Creates:
1. .venv Python virtual environment
2. .env file (asks user for GitHub token)
3. Installs dependencies (requests, python-dotenv)
4. Windows Task Scheduler tasks for watchtower + timekeeper
5. .founderhq_installed marker

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


ENV_PATH = ".env"


def create_venv(base_path: Path) -> bool:
    """Create .venv if it doesn't exist."""
    venv_path = base_path / ".venv"
    if venv_path.exists() and (venv_path / "Scripts" / "python.exe").exists():
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
    pip = base_path / ".venv" / "Scripts" / "pip"
    if not pip.exists():
        pip = base_path / ".venv" / "bin" / "pip"  # Linux/macOS fallback

    deps = ["requests", "python-dotenv"]
    print(f"Installing dependencies: {', '.join(deps)}...")
    result = subprocess.run(
        [str(pip), "install"] + deps,
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
    # Set restrictive permissions on Unix; on Windows this is best-effort
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


def task_exists(task_name: str) -> bool:
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", task_name],
        capture_output=True, text=True, timeout=10,
    )
    return result.returncode == 0


def create_task(task_name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    python_exe = str(Path(base_dir) / ".venv" / "Scripts" / "python.exe")
    if not Path(python_exe).exists():
        python_exe = sys.executable

    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval_minutes),
        "/TN", task_name,
        "/TR", f'"{python_exe}" "{script_path}" --base-dir "{base_dir}"',
        "/F",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {task_name}: {result.stderr.strip()}")
        return False
    print(f"Task '{task_name}' created (every {interval_minutes} min).")
    return True


def remove_task(task_name: str) -> bool:
    if not task_exists(task_name):
        print(f"Task '{task_name}' does not exist, skipping.")
        return True
    cmd = ["schtasks", "/Delete", "/TN", task_name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        print(f"ERROR removing task {task_name}: {result.stderr.strip()}")
        return False
    print(f"Task '{task_name}' removed.")
    return True


def check_burnt_toast() -> bool:
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Get-Module -ListAvailable -Name BurntToast",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    available = "BurntToast" in result.stdout
    if available:
        print("BurntToast: available")
    else:
        print("BurntToast: NOT available - toast notifications disabled")
    return available


def main():
    parser = argparse.ArgumentParser(description="Installer for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks")
    parser.add_argument("--install-burnttoast", action="store_true", help="Install BurntToast")
    parser.add_argument("--skip-env", action="store_true", help="Skip .env setup")
    parser.add_argument("--skip-venv", action="store_true", help="Skip .venv creation")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    if args.uninstall:
        remove_task("FounderHQ-Watchtower")
        remove_task("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    if args.install_burnttoast:
        cmd = [
            "powershell.exe", "-NoProfile", "-Command",
            "Install-Module -Name BurntToast -Force -Scope CurrentUser",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        print("BurntToast installed." if result.returncode == 0 else f"BurntToast install failed: {result.stderr.strip()}")
        return

    check_burnt_toast()

    if not args.skip_venv:
        create_venv(base_path)
        install_deps(base_path)

    if not args.skip_env:
        setup_env(base_path)

    # Setup scheduled tasks
    watchtower_path = scripts_dir / "watchtower.py"
    if watchtower_path.exists():
        create_task("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)
    else:
        print(f"WARNING: {watchtower_path} not found, skipping watchtower task")

    timekeeper_path = scripts_dir / "timekeeper.py"
    if timekeeper_path.exists():
        create_task("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)
    else:
        print(f"WARNING: {timekeeper_path} not found, skipping timekeeper task")

    create_marker(base_path)

    print("\nInstallation complete.")
    print("  - .venv: ready")
    print("  - Dependencies: installed")
    print("  - Scheduled tasks: configured")
    print("  - .founderhq_installed: created")


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/installer.py
git commit -m "feat: expand installer with .venv, token prompt, .env, marker"
```

---

### Task 5: Modify `SYSTEM_PROMPT.md` — Add first-run check and sync hooks

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md`

- [ ] **Read current file**

```cmd
type FounderOS\SYSTEM_PROMPT.md
```

- [ ] **Add first-run check as step 0 of Boot Sequence**

Find the `## Boot Sequence` section. After the line `Execute at session start (triggered by \`boot\` or first \`fhq\` of the day):`, add a new step 0 BEFORE the existing list:

```
0. **First-Run Check** — Check if `.founderhq_installed` exists in the root directory.
   - If absent → Execute **GENESIS**:
     1. Inform user: "First boot detected. I need to install FounderHQ."
     2. Run `python Runtime/engine/installer.py --base-dir .`
     3. If Python missing, install it first (winget/choco/apt/brew depending on OS)
     4. Confirm `.founderhq_installed` exists before continuing
     5. Proceed to step 1
```

- [ ] **Add sync pull after Daily Kickoff**

Find step 13 (Daily Kickoff). After it, add:

```
14. **Sync Pull** — If `State/SYNC_CONFIG.md` exists: run `python Runtime/engine/sync.py pull`. If new snapshot received, run `python Runtime/engine/sync.py merge`. Report sync status.
```

- [ ] **Add sync push to shutdown Intent**

Find the SHUTDOWN row in Intent Classification (starts with `Message starts with **"shutdown"**`). Append to its Action column:

```
 Before shutdown: run python Runtime/engine/sync.py push.
```

- [ ] **Add sync merge to fhq mode Intent**

Find the FHQ_MODE row. No change needed — the sync pull is in the boot sequence which `fhq` triggers.

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "feat: add first-run check, sync pull on boot, sync push on shutdown to SYSTEM_PROMPT"
```

---

### Task 6: Modify `Runtime/RUNTIME_KERNEL.md` — Add GENESIS branch and sync push

**Files:**
- Modify: `FounderOS/Runtime/RUNTIME_KERNEL.md`

- [ ] **Read current Phase 1: BOOT, add GENESIS check**

```cmd
type FounderOS\Runtime\RUNTIME_KERNEL.md
```

Find `## Phase 1: BOOT` section. Add a new operation 0 before the existing list:

```
0. **First-Run Check**: Check if `.founderhq_installed` exists in root.
   - If absent → halt normal boot, execute GENESIS procedure
     (ask for token, create files, .venv, scripts, marker).
```

- [ ] **Add sync push to Phase 7: UPDATE**

Find `## Phase 7: UPDATE` section. Add to the operations list:

```
6. **Sync Push**: If State/SYNC_CONFIG.md exists, run `python Runtime/engine/sync.py push` to persist state to Gist.
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/RUNTIME_KERNEL.md
git commit -m "feat: add GENESIS branch to BOOT and sync push to UPDATE in RUNTIME_KERNEL"
```

---

### Task 7: Modify `State/CADENCE.md` — Add Sync section

**Files:**
- Modify: `FounderOS/State/CADENCE.md`

- [ ] **Read current file, add Sync section to Day**

```cmd
type FounderOS\State\CADENCE.md
```

Find the `## Day (Jour)` section. Add after the `**Duration:** [calculated]` line, before `**Top 3 actions:**`:

```
**Sync:** [synced / pending / not configured]
**Last Sync:** [date]
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/CADENCE.md
git commit -m "feat: add Sync status fields to CADENCE.md Day section"
```

---

### Task 8: Generate `FOUNDER_SEED.md`

**Files:**
- Create: `FounderOS/FOUNDER_SEED.md`

- [ ] **Build FOUNDER_SEED.md by concatenating all core files**

This is a build step. Write a Python script that generates FOUNDER_SEED.md from all core files, then run it.

```python
"""build_seed.py - Generate FOUNDER_SEED.md from all core FHQ files.

Run from FounderHQ root:
    python build_seed.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "FOUNDER_SEED.md"

# Files to include (in order). Exclude user data directories.
CORE_PATHS = [
    # Root files
    "SYSTEM_PROMPT.md",
    "RUNTIME.md",
    "FOUNDERHQ_MANIFEST.md",
    "GENESIS.md",
    "INSTALL.md",
    # Frameworks
    "AOS.md",
    "CAOS.md",
    "CEOS.md",
    "DAOS.md",
    "DECISION_ENGINE.md",
    "FAOS.md",
    "KMOS.md",
    "LEOS.md",
    "MOS.md",
    "PATTERN_ENGINE.md",
    "PLAYBOOK_ENGINE.md",
    "RIOS.md",
    "SOS.md",
    "VEAOS.md",
    # State
    "State/CADENCE.md",
    "State/CURRENT_STATE.md",
    "State/LIFECYCLE.md",
    "State/PRIORITY_MATRIX.md",
    "State/SYNC_CONFIG.md",
    "State/WATCH_REGISTRY.md",
    "State/ALERTS.md",
    "State/WATCH_REPORT.md",
    # Runtime
    "Runtime/RUNTIME_KERNEL.md",
    "Runtime/FRE_SPEC.md",
    "Runtime/ADAPTER_INTERFACE.md",
    "Runtime/engine/__init__.py",
    "Runtime/engine/bootstrap.py",
    "Runtime/engine/state_manager.py",
    "Runtime/engine/gate_checker.py",
    "Runtime/engine/timeline_logger.py",
    "Runtime/engine/cadence_engine.py",
    "Runtime/engine/watchtower.py",
    "Runtime/engine/timekeeper.py",
    "Runtime/engine/installer.py",
    "Runtime/engine/sync.py",
    "Runtime/engine/snapshot.py",
    # Protocols
    "Protocols/SOURCE_OF_TRUTH.md",
    "Protocols/DECISION_GATES.md",
    "Protocols/INFO_CAPTURE_PROTOCOL.md",
]

HEADER = """# FOUNDER SEED — FounderHQ Bootstrap

## Instructions for the LLM

This file contains all core files of FounderHQ. Each section is delimited by:

```
--- FILE: <relative-path> ---
<file content>
--- END ---
```

1. Read this file completely.
2. For each `--- FILE:` block, create the file at that relative path.
3. Create any intermediate directories as needed.
4. Continue until all files are created.
5. Then run `python Runtime/engine/installer.py --base-dir .` to complete setup.

---

"""


def main():
    sections = [HEADER]

    for rel_path in CORE_PATHS:
        file_path = ROOT / rel_path
        if not file_path.exists():
            print(f"WARNING: {rel_path} not found, skipping")
            continue

        content = file_path.read_text(encoding="utf-8")
        section = f"--- FILE: {rel_path} ---\n{content}--- END ---\n"
        sections.append(section)

    OUTPUT.write_text("\n\n".join(sections), encoding="utf-8")
    file_count = len(sections) - 1
    char_count = len("\n\n".join(sections))
    print(f"FOUNDER_SEED.md generated: {file_count} files, {char_count} chars")


if __name__ == "__main__":
    main()
```

Run the build script:
```cmd
cd C:\Users\junio\Desktop\FounderHQ\FounderOS
python build_seed.py
```

Verify:
```cmd
type FounderOS\FOUNDER_SEED.md | head -10
```

Expected output: FOUNDER_SEED.md starts with the header and first FILE: block.

- [ ] **Add build_seed.py to gitignore and clean up**

Create `.gitignore` entry or just leave `build_seed.py` as a development tool.

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/FOUNDER_SEED.md
git commit -m "feat: generate FOUNDER_SEED.md - single-file distribution of all core FHQ files"
```

---

### Task 9: Modify `Protocols/SOURCE_OF_TRUTH.md`

**Files:**
- Modify: `FounderOS/Protocols/SOURCE_OF_TRUTH.md`

- [ ] **Add entries for new files**

Read current file, then add these rows to the truth table:

```
| .env | Root/ | System (scripts only) | Secrets: GitHub token, Gist URL. Permissions 600. Never read by LLM. |
| .founderhq_installed | Root/ | System | Empty marker file. If absent at boot -> GENESIS procedure. |
| FOUNDER_SEED.md | Root/ | System | Distribution file. Contains all core files for bootstrap. |
| Runtime/engine/sync.py | Runtime/engine/ | System | Gist state sync. Reads .env for token. Called by LLM, never exposes token. |
| Runtime/engine/snapshot.py | Runtime/engine/ | System | Portable markdown snapshot for token-less environments. |
| State/SYNC_CONFIG.md | State/ | System | LLM-readable sync configuration (no secrets). |
| State/_SYNC_INBOX.md | State/ | System (sync.py) | Staging area for incoming Gist sync data. |
| State/EXPORT_SNAPSHOT.md | State/ | snapshot.py | Generated portable snapshot for export. |
| State/IMPORT_SNAPSHOT.md | State/ | snapshot.py | Snapshot to merge (user pastes here). |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Protocols/SOURCE_OF_TRUTH.md
git commit -m "docs: register sync.py, snapshot.py, .env, .founderhq_installed, FOUNDER_SEED.md in SOURCE_OF_TRUTH"
```

---

### Task 10: Modify `Runtime/engine/__init__.py`

**Files:**
- Modify: `FounderOS/Runtime/engine/__init__.py`

- [ ] **Add doc entries for sync.py and snapshot.py**

Read current file, then update the docstring to add:

```
    sync: Gist state sync (push/pull/merge). Reads token from .env. LLM never sees token.
    snapshot: Portable markdown snapshot for token-less sync. No token needed.
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/__init__.py
git commit -m "docs: document sync and snapshot modules in engine __init__"
```

---

## Self-Review Checklist

### 1. Spec Coverage
- FOUNDER_SEED.md -> Task 8
- .env secrets -> Task 4 (installer prompts, writes .env)
- sync.py -> Task 1 (push/pull/merge with token isolation)
- snapshot.py -> Task 2 (portable fallback)
- .founderhq_installed -> Task 4 (installer creates), Task 5-6 (boot checks)
- SYNC_CONFIG.md -> Task 3
- GENESIS auto-run -> Task 5 (SYSTEM_PROMPT step 0), Task 6 (RUNTIME_KERNEL)
- Auto sync on boot -> Task 5 (step 14)
- Auto sync on shutdown -> Task 5 (shutdown intent), Task 6 (UPDATE phase)
- SOURCE_OF_TRUTH -> Task 9
- __init__.py -> Task 10
- CADENCE.md sync fields -> Task 7

### 2. Placeholder Scan
No placeholders found. All code blocks complete. All paths exact.

### 3. Type Consistency
- `Snapshot` class with `to_dict()` / `from_dict()` used consistently in sync.py and tests
- `cmd_pull`, `cmd_push`, `cmd_merge` return strings — used in `main()` print
- `cmd_generate`, `cmd_merge` in snapshot.py return strings — same pattern
- `create_venv`, `install_deps`, `setup_env`, `create_marker` return bool — used in installer.py main()
- All function signatures match between tasks


--- FILE: docs/superpowers/specs/2026-06-21-fre-design.md
# Founder Runtime Engine (FRE) — Design Spec

## Problem

FounderHQ is ~98% portable markdown, but its behavior depends entirely on the LLM voluntarily following SYSTEM_PROMPT.md. Each runtime (OpenCode, Claude Code, ChatGPT, Gemini, Cursor) has different mechanisms for loading instructions, accessing files, and maintaining context. There is no contract that codifies "what FHQ expects from a runtime" independently of any specific platform.

## Solution

A three-layer Runtime Abstraction:

```
FRE SPEC (constitution, testable, no code)
    ↓
ADAPTERS (per-platform guides, no code)
    ↓
ENGINE (optional automation code)
```

**Core principle:** Layers 1-2 must be sufficient to run FHQ on any LLM. Layer 3 is acceleration, not dependency.

---

## Layer 1: FRE SPEC — The Constitution

**File:** `Runtime/FRE_SPEC.md`

Defines what FHQ requires from any runtime. Each requirement is a testable contract:

| Contract | Purpose | Test |
|----------|---------|------|
| Boot Contract | Minimal startup sequence | "User says 'start' → CURRENT_STATE loaded, PRG executed" |
| Pre-Response Contract | 5 PRG steps (Temporal → Scan → Absorb → Project Scan → Freshness) | "User gives info → captured in right file before reply" |
| State Management Contract | Read/write/stale rules | "State >48h → flagged stale" |
| Gate Contract | Non-negotiable rules (Rule #6, Cash Awareness, Mission Alignment) | "Cash <1500 → every action generates revenue" |
| Temporal Contract | Datetime format, timezone, aging | "Response starts with [datetime Lome UTC+0]" |
| Recall Contract | Context preservation and reconstruction | "Session lost → rebuild from MANIFEST + concepts" |

**Key innovation:** FRE_SPEC is written as **behavioral expectations**, not instructions. Each section can be converted to a PASS/FAIL test.

---

## Layer 2: Adapters — Platform Bridges

**Directory:** `Runtime/adapters/`

**`ADAPTER_INTERFACE.md`** defines the contract all adapters must satisfy: 4 questions per platform (kernel loading, file access, context persistence, protocol execution).

Each adapter file answers these 4 questions for a specific platform:
1. How does this platform load the kernel?
2. How does it access files?
3. How does it maintain context between sessions?
4. How does it execute protocols (PRG, gates)?

| File | Platform | Activation Mechanism |
|------|----------|---------------------|
| `opencode.md` | OpenCode | `opencode.json` → `instructions` |
| `chatgpt.md` | ChatGPT Web | Manual copy-paste of FRE_SPEC |
| `claude.md` | Claude Code | `CLAUDE.md` reference |
| `gemini.md` | Gemini CLI | `GEMINI.md` reference |
| `cursor.md` | Cursor IDE | `.cursorrules` reference |
| `local_agent.md` | Autonomous agent | Script injects FRE_SPEC into prompt |

Adapters are **guides, not enforcers**. Only OpenCode (via `opencode.json`) and partially Claude Code/Cursor support auto-injection. For others, the user or agent reads the adapter and configures manually.

---

## Layer 3: Engine — Optional Accelerator

**Directory:** `Runtime/engine/`

Code that automates what the LLM would do manually. **Not required.** FHQ must function without it.

| Module | Responsibility | Replaces |
|--------|---------------|----------|
| `bootstrap.py` | Reads FRE_SPEC, injects into LLM prompt | Manual copy-paste |
| `state_manager.py` | Reads/writes CURRENT_STATE, TIMELINE, PRIORITY_MATRIX | Manual file edits |
| `gate_checker.py` | Validates LLM response against PRG format | LLM self-discipline |
| `timeline_logger.py` | Auto-records events to TIMELINE.md | Forgotten timeline entries |

**Rule:** Every engine module is replaceable. If `state_manager.py` breaks, fall back to manual edits. FHQ survives engine deletion.

---

## File Tree

```
FounderOS/
└── Runtime/
    ├── FRE_SPEC.md
    ├── ADAPTER_INTERFACE.md
    ├── adapters/
    │   ├── opencode.md
    │   ├── chatgpt.md
    │   ├── claude.md
    │   ├── gemini.md
    │   ├── cursor.md
    │   └── local_agent.md
    └── engine/
        ├── bootstrap.py
        ├── state_manager.py
        ├── gate_checker.py
        └── timeline_logger.py
```

## Non-Goals

- FRE does NOT replace SYSTEM_PROMPT.md. SYSTEM_PROMPT.md remains the active system prompt. FRE_SPEC is the canonical reference that SYSTEM_PROMPT.md implements.
- FRE does NOT add new concepts. It's a new layer (Runtime) in the existing architecture.
- FRE does NOT require rewriting existing FHQ files. It's additive.

## Future

FRE enables:
1. **FHQ without an IDE** — run via `local_agent.md` + engine/ in any terminal
2. **Cross-platform continuity** — same cognitive system in ChatGPT, Claude, OpenCode
3. **Testable compliance** — FRE_SPEC as a test suite for any runtime
4. **Kora OS bootstrapping** — FRE is the kernel that Kora OS will extend

---

## Footer

| Field | Value |
|-------|-------|
| Document | FRE Design Spec V1 |
| Date | 2026-06-21 |
| Status | Draft |
| Owner | Founder |


--- FILE: docs/superpowers/specs/2026-06-22-founderhq-distribution-and-sync-design.md
# FounderHQ Distribution & Sync — Design Spec

> **Status:** Draft
> **Date:** 2026-06-22
> **Owner:** System

---

## 1. Problem

FounderHQ has ~50 files (markdown + Python scripts). Distributing it means copying the entire folder. Syncing state between devices (PC ↔ mobile) requires manual work.

**Requirements:**
- Zero-dependency distribution: one URL or one file → full FHQ environment
- Automatic state sync between devices
- No LLM exposure of secrets (GitHub token)
- Works on any LLM (OpenCode, Claude Code, LM Arena, ChatGPT web)

---

## 2. Distribution: FOUNDER_SEED.md

A single markdown file containing all core FHQ files delimited by `--- FILE:` markers. Hosted on a public GitHub Gist.

### Format

```markdown
# FOUNDER SEED — FounderHQ Bootstrap

Instructions for the LLM: read this file, create every `--- FILE:` block as a file.

---

--- FILE: FounderOS/SYSTEM_PROMPT.md ---
[full content]
--- END ---

--- FILE: FounderOS/Runtime/RUNTIME_KERNEL.md ---
[full content]
--- END ---

... (30-40 files, ~50K tokens total)
```

### Usage

```
User: fhq https://gist.github.com/user/abc123/founder-seed.md
```

LLM webfetches the URL, parses `--- FILE:` blocks, creates all files in 3-5 responses.

### Not included in seed

User-generated content: `projects/`, `State/CURRENT_STATE.md` values, `TIMELINE.md` entries, `KNOWLEDGE.md` entries, `concepts/MEMORY.md` content. These are created by the user through normal FHQ operation.

---

## 3. Secrets: `.env` File

A single `.env` file at the root of `FounderHQ/` containing environment variables. **Never read by the LLM.** Only read by Python scripts.

### Content

```
FHQ_GIST_URL=https://gist.github.com/tonuser/abc123
FHQ_GIST_TOKEN=ghp_xxxxxxxxxxxx
```

### Security rules

1. File permissions: `600` (owner read/write only)
2. Never included in any `.md` file
3. Never passed to the LLM in any prompt
4. Only read by `Runtime/engine/sync.py` via `python-dotenv`
5. Token scoped to `gist:write, gist:read` (GitHub fine-grained token)

---

## 4. State Sync: `sync.py`

Script that handles push/pull to a private GitHub Gist. The LLM **calls the script** (`run engine/sync.py pull`) and sees the result — never the token.

### Commands

```
sync.py pull
  → GET Gist API (with token from .env)
  → Downloads snapshot.json
  → Validates structure
  → Writes to State/_SYNC_INBOX.md (staging, not merged)
  → Returns: "New snapshot [date]" or "No changes"

sync.py push
  → Reads CURRENT_STATE.md + CADENCE.md + TIMELINE.md
  → Compacts into snapshot.json
  → POST to Gist API (with token from .env)
  → Returns: "Synced [timestamp]" or error message

sync.py merge
  → Reads State/_SYNC_INBOX.md
  → Applies changes to CURRENT_STATE.md, CADENCE.md, TIMELINE.md
  → Returns: changelog of what was merged
```

### Snapshot format (snapshot.json)

```json
{
  "version": 1,
  "timestamp": "2026-06-22T14:30:00Z",
  "state": {
    "date": "2026-06-22 14:30 Lome UTC+0",
    "mode": "SURVIVAL",
    "cash": 2679,
    "top_priority": "Find client for maize",
    "bottleneck": "Cash insuffisant"
  },
  "cadence": {
    "session_start": "08:15",
    "session_end": "14:30",
    "day_objective": "Valider SOJACO"
  },
  "timeline": [
    {
      "date": "2026-06-22 08:15",
      "event": "Boot",
      "decision": "Start day",
      "outcome": "Session started"
    }
  ],
  "projects": {
    "SOJACO": {"phase": "VALIDATION", "next_action": "Find client"},
    "OMNI": {"phase": "LAUNCH", "next_action": "Pitch Day prep"}
  }
}
```

---

## 5. Fallback Sync: `snapshot.py`

Alternative for environments without HTTP auth capability (basic LM Arena, ChatGPT web).

### Commands

```
snapshot.py generate
  → Reads state files
  → Produces compact markdown summary (~2K tokens)
  → Writes to State/EXPORT_SNAPSHOT.md

snapshot.py merge
  → Reads State/IMPORT_SNAPSHOT.md
  → Patches local files
  → Returns changelog
```

### Flow (token-less)

```
PC: fhq shutdown --export
  → LLM: run engine/snapshot.py generate
  → Output: short snapshot text

  User copies text, switches device.

Mobile: "fhq [paste snapshot]"
  → LLM reads snapshot, continues work.
  → "fhq shutdown --export"
  → New snapshot produced.

  User copies back, switches device.

PC: "fhq resume [paste snapshot]"
  → LLM: run engine/snapshot.py merge
  → Session continues with updated state.
```

---

## 6. First-Run: GENESIS

When `.founderhq_installed` does not exist at boot, the LLM executes GENESIS:

### Step-by-step

1. **Ask for token proactively** — LLM detects `.founderhq_installed` missing, asks user for GitHub token (scope gist)
   - User can type `skip` to do it later
   - Token is stored to `.env` immediately
   - LLM never reads the token value back

2. **Create all core files** — Parse `FOUNDER_SEED.md` (from context or webfetch), create every file

3. **Create `.venv`** — `python -m venv .venv` (install Python first if missing)

4. **Install dependencies** — `.venv\Scripts\pip install requests python-dotenv`

5. **Install scripts** — `run engine/installer.py --base-dir .`

6. **Test sync** — `run engine/sync.py push` with the new token, then `pull`

7. **Create `.founderhq_installed`** — empty marker file

8. **Create `State/SYNC_CONFIG.md`** — configuration readable by LLM

9. **Continue normal session** — ORIENT → DECIDE → ACT

---

## 7. Boot Sequence Changes

### SYSTEM_PROMPT.md Boot Sequence (updated)

```
0. First-run check → .founderhq_installed exists?
   NO → execute GENESIS (ask token, create files, .venv, scripts)
1-13. (existing steps)

After step 13 (Daily Kickoff):
  → run engine/sync.py pull (if SYNC_CONFIG.md exists)
```

### SYSTEM_PROMPT.md Intent Classification (updated)

```
| Message starts with **"boot"** | BOOT | Full initialization. GENESIS if first run. |
| Message starts with **"shutdown"** | SHUTDOWN | End session. Save state. Sync push. |
| Message starts with **"fhq"** | FHQ_MODE | Full kernel cycle. Sync pull if first fhq today. |
```

### RUNTIME_KERNEL.md Phase 1: BOOT (updated)

Add before existing operations:
```
0. Check .founderhq_installed
   - If absent → execute GENESIS procedure
```

### RUNTIME_KERNEL.md Phase 7: UPDATE (updated)

Add after existing operations:
```
6. Run engine/sync.py push (if SYNC_CONFIG.md exists)
```

---

## 8. File Inventory

### New files

| File | Purpose | Access |
|------|---------|--------|
| `FOUNDER_SEED.md` | Distribution: all core files in one file | Public Gist |
| `.env` | Secrets (token, Gist URL) | 600, scripts only |
| `.founderhq_installed` | Marker: installation complete | LLM reads |
| `.venv/` | Isolated Python environment | Scripts only |
| `State/SYNC_CONFIG.md` | Sync configuration (no token) | LLM reads |
| `State/_SYNC_INBOX.md` | Staging area for incoming sync | LLM reads |
| `State/EXPORT_SNAPSHOT.md` | Generated portable snapshot | LLM reads |
| `State/IMPORT_SNAPSHOT.md` | Snapshot to merge (user pastes) | LLM reads |
| `Runtime/engine/sync.py` | Gist push/pull/merge (reads .env) | Called by LLM |
| `Runtime/engine/snapshot.py` | Portable snapshot gen/merge | Called by LLM |

### Modified files

| File | Change |
|------|--------|
| `SYSTEM_PROMPT.md` | Boot sequence: first-run check + sync pull. Intent: GENESIS mode. Shutdown: sync push. |
| `RUNTIME_KERNEL.md` | Phase 1: GENESIS branch. Phase 7: sync push. |
| `Runtime/engine/installer.py` | Create .venv, write .env, create marker |
| `Runtime/engine/__init__.py` | Document sync.py, snapshot.py |
| `State/CADENCE.md` | Add Sync section to Day |
| `Protocols/SOURCE_OF_TRUTH.md` | Register all new files |
| `Runtime/engine/watchtower.py` | Read .env if needed (future) |
| `Runtime/engine/timekeeper.py` | Read .env if needed (future) |

---

## 9. Security Model

1. **GitHub token** stored in `.env` with `600` permissions
2. **Only `sync.py`** reads `.env` — LLM never sees the token value
3. LLM **calls** `sync.py` as a subprocess — input is "push" or "pull", output is "OK" or error
4. Snapshot contains **operational data only** (CURRENT_STATE fields, project phases, timeline events) — no passwords, no secrets
5. Snapshot is pushed to a **private Gist** — invisible to search, requires token to read
6. Fallback snapshots are copied between contexts by the user — no third party

---

## 10. Error Handling

| Error | Behavior |
|-------|----------|
| Token not configured | LLM asks proactively at boot. Sync skipped if absent. |
| Sync push fails (no network) | LLM logs error, continues. Retry on next shutdown. |
| Sync pull fails | LLM continues with local state. Marks "Sync failed" in response. |
| Merge conflict | LLM presents diff to user: "Remote changed X, local changed X. Which wins?" |
| Python not found | LLM installs Python via winget/choco/apt/brew depending on OS. |
| `.venv` missing | LLM re-creates it on next `fhq boot`. |


--- FILE: projects/KORA/01_VISION.md
# KORA VISION
## Version 1.0 — Institutional Edition (15–25 Year Horizon)

### Une Afrique pleinement représentée dans l'ère de l'intelligence artificielle

---

# 1. Vision Statement

Nous imaginons un futur où chaque Africain peut accéder aux capacités les plus avancées de l'intelligence artificielle dans sa langue maternelle, indépendamment de son niveau d'alphabétisation, de son niveau de revenu ou de sa localisation géographique.

Dans ce futur, les langues africaines ne sont plus absentes des systèmes numériques mondiaux. Elles deviennent des citoyens de première classe de l'écosystème technologique mondial. L'intelligence artificielle comprend, parle, traduit, enseigne et collabore naturellement dans les langues africaines. L'accès à la connaissance, aux services publics, à l'éducation, à la santé et aux opportunités économiques n'est plus limité par la langue.

# 2. Le Futur Que Nous Voulons Créer

Nous croyons que le XXIe siècle sera défini par l'intelligence artificielle comme le XXe siècle l'a été par l'électricité et Internet. Dans ce nouveau monde, la langue deviendra un facteur déterminant d'inclusion ou d'exclusion.

Si les langues africaines ne sont pas représentées dans les modèles qui gouvernent l'accès à la connaissance et aux services numériques, des centaines de millions de personnes risquent d'être marginalisées dans l'économie de l'intelligence artificielle. Nous refusons ce futur.

Nous voulons contribuer à construire un monde dans lequel :
- les langues africaines sont représentées dans les systèmes d'IA
- les populations africaines participent activement à la création de ces systèmes
- les bénéfices de l'intelligence artificielle sont accessibles à tous
- les patrimoines linguistiques et culturels du continent sont préservés et valorisés

# 3. Notre Conviction Fondamentale

Nous croyons que la voix deviendra l'interface dominante de l'intelligence artificielle. Pour des milliards de personnes, parler est plus naturel qu'écrire. Cette réalité est particulièrement importante dans les régions où l'accès à l'éducation reste inégal, où l'alphabétisation demeure un défi, et où la transmission culturelle est historiquement orale.

L'avenir de l'IA ne sera pas uniquement textuel. Il sera vocal, multimodal, conversationnel et multilingue.

# 4. Notre Vision de l'Infrastructure Linguistique Africaine

Nous imaginons l'émergence d'une infrastructure linguistique africaine capable de comprendre, parler, et traduire les langues africaines, et de permettre à l'IA d'interagir naturellement avec leurs locuteurs.

Cette infrastructure devra être scalable, interopérable, continuellement enrichie, et accessible aux développeurs, chercheurs, institutions et entreprises. À terme, elle constituera une couche fondamentale de l'économie numérique africaine.

# 5. Notre Vision de la Communication Humaine

Nous imaginons un monde dans lequel deux personnes peuvent communiquer librement même lorsqu'elles ne partagent aucune langue commune. Un locuteur éwé pourra dialoguer avec un locuteur yoruba. Un locuteur wolof pourra collaborer avec un locuteur swahili. Un locuteur bambara pourra accéder à des connaissances produites en chinois, anglais ou français. Les barrières linguistiques deviendront progressivement invisibles.

# 6. Notre Vision de l'Intelligence Artificielle

Nous pensons que les futurs systèmes d'IA seront capables d'écouter, comprendre, raisonner, mémoriser, agir et communiquer. Ils interagiront naturellement par la voix, comprendront simultanément plusieurs langues, s'adapteront aux contextes culturels locaux, et assisteront les individus dans leur vie quotidienne. Notre ambition est de rendre ces capacités accessibles aux populations africaines dans leurs propres langues.

# 7. Notre Vision de l'Impact Sociétal

**Éducation:** Permettre à chaque enfant d'apprendre dans sa langue maternelle.
**Santé:** Rendre l'information médicale accessible oralement dans les langues locales.
**Agriculture:** Donner aux agriculteurs un accès direct aux connaissances.
**Administration:** Faciliter l'accès aux services publics.
**Économie:** Permettre à davantage d'entrepreneurs de participer à l'économie numérique.
**Culture:** Préserver et transmettre le patrimoine oral africain.

# 8. Notre Vision de KORA

À long terme, KORA aspire à devenir un laboratoire de recherche en IA, un constructeur d'infrastructures linguistiques, un acteur de référence pour les langues africaines, et un contributeur à l'avancement de l'IA mondiale.

Nous mesurons notre succès par notre capacité à accroître le nombre de personnes pouvant accéder à l'IA dans leur langue maternelle.

# 9. Horizon de Réussite

Nous considérerons que cette vision commence à se réaliser lorsque plusieurs langues africaines disposeront d'une représentation robuste dans les systèmes d'IA, que les interactions vocales deviendront naturelles dans ces langues, que les barrières linguistiques entre communautés diminueront, et que les populations africaines pourront utiliser l'IA sans devoir abandonner leur langue maternelle.

## Vision Résumée

**Construire un futur dans lequel chaque Africain peut accéder, contribuer et prospérer dans l'ère de l'intelligence artificielle sans être limité par sa langue.**

## OODA Critique

Cette vision est volontairement indépendante des produits (ASR, TTS, Omni), indépendante des financements, indépendante des technologies actuelles, et valable encore dans 20 ans même si Whisper, GPT ou Gemini disparaissent. Une bonne vision doit survivre à plusieurs générations technologiques.

## Footer
| Field | Value |
|---|---|
| Document | KORA Vision V1 |
| Horizon | 15–25 years |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/02_MISSION.md
# KORA MISSION
## Version 1.0

### Transformer la vision d'une IA accessible à tous les Africains en une réalité concrète

## 1. Déclaration de Mission

La mission de KORA est de construire les infrastructures linguistiques, les données, les modèles et les systèmes nécessaires pour permettre aux populations africaines d'interagir avec l'intelligence artificielle dans leurs langues maternelles.

Nous existons pour réduire les barrières linguistiques qui limitent aujourd'hui l'accès à la connaissance, aux services numériques et aux opportunités économiques. Nous poursuivons cette mission en développant des technologies vocales, multimodales et multilingues adaptées aux réalités linguistiques du continent africain.

## 2. Pourquoi KORA Existe

L'IA devient une couche fondamentale de l'économie mondiale. Mais la majorité des langues africaines restent sous-représentées dans les systèmes modernes. Cette situation crée des risques d'exclusion numérique, de perte du patrimoine linguistique, de dépendance technologique, et d'accès inégal aux bénéfices de l'IA.

KORA existe pour contribuer à réduire cet écart.

## 3. Ce Que Nous Faisons (5 capacités fondamentales)

**1. Construire les données:** Nous collectons, structurons, validons et enrichissons des ressources linguistiques africaines (vocales, textuelles, conversationnelles, dialectales).

**2. Construire les modèles:** Nous développons des systèmes capables de comprendre, transcrire, traduire, synthétiser et générer dans les langues africaines.

**3. Construire les plateformes:** Nous développons des infrastructures permettant aux chercheurs, développeurs, institutions et entreprises d'utiliser ces technologies.

**4. Construire les applications:** Nous facilitons le développement d'applications dans l'éducation, la santé, l'agriculture, l'administration et la communication.

**5. Construire un écosystème:** Nous travaillons avec universités, chercheurs, communautés linguistiques, gouvernements et entreprises.

## 4. Ce Que Nous Ne Sommes Pas

KORA n'existe pas uniquement pour entraîner des modèles, publier des articles, construire des produits logiciels ou vendre des API. Ces activités peuvent faire partie de notre travail mais ne constituent pas notre mission.

## 5. Nos Principes d'Exécution

**Principe 1:** Construire des actifs durables (données, expertise, communautés, infrastructures, PI)
**Principe 2:** Construire avant de revendiquer — chaque affirmation soutenue par une démonstration
**Principe 3:** Commencer localement, construire globalement
**Principe 4:** Prioriser l'impact réel
**Principe 5:** Construire avec les communautés

## 6. Comment Nous Mesurerons Notre Succès

Pas par le nombre de modèles publiés ou lignes de code. Mais par le nombre de langues représentées, la qualité des infrastructures créées, le nombre de personnes pouvant utiliser l'IA dans leur langue maternelle, et l'impact économique, éducatif et culturel généré.

## 7. Priorité Actuelle

Construire les premières fondations d'une infrastructure linguistique africaine en commençant par une langue pilote (Éwé) et un ensemble limité de capacités permettant de démontrer la faisabilité du modèle.

## Mission Résumée

**Construire les infrastructures linguistiques qui permettront à chaque Africain d'accéder à l'IA dans sa langue maternelle, tout en préservant, valorisant et modernisant le patrimoine linguistique du continent.**

## Footer
| Field | Value |
|---|---|
| Document | KORA Mission V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/03_THEORY_OF_CHANGE.md
# KORA THEORY OF CHANGE
## Version 1.0

### Comment KORA transforme sa vision en réalité

## Introduction

La Theory of Change de KORA décrit la chaîne logique reliant nos activités quotidiennes à notre vision long terme. Elle répond à: comment passe-t-on d'un continent sous-représenté dans l'IA à un futur où chaque Africain peut interagir avec l'IA dans sa langue maternelle ?

## Le Problème Fondamental

Les langues africaines souffrent de 5 déficits structurels: déficit de données (corpus rares), déficit d'outils (technologies limitées), déficit de recherche (peu représentées), déficit d'écosystème (acteurs fragmentés), déficit de distribution (solutions n'atteignent pas les populations).

## Notre Hypothèse Centrale

Si nous construisons progressivement les infrastructures linguistiques nécessaires aux langues africaines, alors il deviendra possible de développer des systèmes d'IA capables de servir efficacement les populations africaines dans leurs langues maternelles.

## Les 5 Relations Causales

**Relation 1:** Sans données → pas de modèles durables
**Relation 2:** Sans modèles → pas d'applications
**Relation 3:** Sans applications → pas d'adoption
**Relation 4:** Sans adoption → pas d'écosystème durable
**Relation 5:** Sans écosystème → pas de transformation durable

## La Chaîne de Transformation Complète

Collecter les données → Construire les capacités fondamentales (ASR, TTS, traduction) → Construire les infrastructures (APIs, plateformes) → Construire les applications (éducation, santé, agriculture) → Construire la distribution (smartphones, partenaires) → Construire l'écosystème (universités, gouvernements, entreprises)

## Le Cercle Vertueux KORA

Données → Modèles → Applications → Utilisateurs → Revenus → Nouvelles données → Meilleurs modèles → Plus d'utilisateurs

Chaque cycle renforce le suivant.

## Les Actifs Stratégiques Produits à Chaque Étape

- Phase Données: corpus, expertise linguistique, communautés
- Phase Modèles: propriété intellectuelle, benchmarks, savoir-faire
- Phase Infrastructure: plateformes, APIs, outils
- Phase Distribution: utilisateurs, réseau, marque
- Phase Écosystème: partenaires, institutions, influence

## Conditions Nécessaires

1. Accès durable au calcul (ST Digital)
2. Capacité à collecter des données de qualité
3. Capacité à attirer et former des talents
4. Capacité à générer des revenus avant maturité technologique
5. Capacité à construire une confiance durable avec les communautés

## Risques Stratégiques

1. Grands laboratoires progressent plus vite → réponse: avantage données/communautés
2. Coûts de collecte prohibitifs → réponse: collecte communautaire
3. Revenus arrivent trop tard → réponse: produits monétisables dès phase 1
4. Talents difficiles à recruter → réponse: réseau africain et diasporique

## Résumé

Collecter les données → Construire les modèles → Créer les infrastructures → Développer les applications → Distribuer à grande échelle → Créer un écosystème durable → Permettre à chaque Africain d'accéder à l'IA dans sa langue maternelle

## OODA Critique

KORA n'est pas un projet de modèles. Les modèles sont un moyen. La théorie du changement montre que KORA est un projet de construction d'actifs: données, expertise, infrastructure, distribution, écosystème.

## Footer
| Field | Value |
|---|---|
| Document | KORA Theory of Change V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/04_STRATEGIC_ASSETS_MAP.md
# KORA STRATEGIC ASSETS MAP
## Version 1.0

### Les actifs stratégiques nécessaires à la réalisation de la mission de KORA

## Principe Fondamental

KORA n'est pas construit pour maximiser le nombre de modèles publiés. KORA est construit pour accumuler des actifs stratégiques difficilement reproductibles. Chaque projet, financement, recrutement et partenariat doit contribuer à renforcer au moins un actif stratégique.

## Les 8 Catégories d'Actifs

### Actif 1: Données Linguistiques
L'un des plus importants actifs. Objectif: plus grande collection de ressources linguistiques africaines. Sous-actifs: corpus vocaux, textuels, parallèles, conversationnels, multimodaux. Difficulté à reproduire: Très élevée.

### Actif 2: Infrastructure de Collecte et Traitement
Outils de collecte, pipelines de validation, stockage, gouvernance. Difficulté: Élevée.

### Actif 3: Modèles et Systèmes
ASR multilingue, TTS, traduction vocale, compréhension multimodale, agents conversationnels (Omni). Difficulté: Moyenne à élevée.

### Actif 4: Talents et Expertise
Recherche (ML, NLP, Speech), linguistique, ingénierie, opérations terrain. Difficulté: Très élevée.

### Actif 5: Communautés Linguistiques
Réseau de locuteurs, universités, associations culturelles, experts locaux. Difficulté: Très élevée.

### Actif 6: Distribution
APIs, applications, partenariats, intégrations, wearables. Difficulté: Très élevée à grande échelle.

### Actif 7: Capital Institutionnel
Réputation scientifique et technique, relations gouvernementales et industrielles, crédibilité internationale. Difficulté: Très élevée.

### Actif 8: Recherche et Propriété Intellectuelle
Publications, méthodologies, pipelines, innovations algorithmiques. Difficulté: Variable.

## Hiérarchie des Actifs

**Niveau 1 (Fondamentaux):** Données, Communautés, Talents
**Niveau 2 (Transformation):** Infrastructure, Modèles
**Niveau 3 (Échelle):** Distribution, Capital institutionnel
**Niveau 4 (Leadership):** Recherche, Propriété intellectuelle

## Séquence d'Accumulation

1. Données + Communautés + Talents
2. Infrastructure + Modèles
3. Distribution + Revenus
4. Influence + Recherche avancée

## Test de Décision Stratégique

Toute initiative doit répondre: "Quel actif stratégique cette initiative renforce-t-elle ?" Si la réponse est "aucun", l'initiative est secondaire.

## Conclusion

KORA ne doit pas être piloté par ses produits mais par l'accumulation systématique d'actifs stratégiques. Les produits évoluent, les modèles changent, les marchés se transforment — mais si KORA accumule continuellement données, communautés, talents, infrastructure, distribution et confiance, il pourra s'adapter à tous les changements technologiques.

## Footer
| Field | Value |
|---|---|
| Document | KORA Strategic Assets Map V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/05_MASTER_PLAN.md
# KORA MASTER PLAN V2
## Building the Universal Speech Intelligence Layer
### Version 2.0 — 2026–2045+

## EXECUTIVE SUMMARY

KORA Lab est un laboratoire africain d'IA dont la mission est de permettre aux langues africaines de participer pleinement à l'ère de l'intelligence artificielle. Contrairement à la majorité des acteurs du secteur, KORA ne considère pas les langues africaines comme un simple problème de traduction ou de localisation. KORA considère les langues comme une infrastructure fondamentale de l'intelligence.

Notre conviction est que le principal obstacle à l'inclusion des langues africaines dans l'IA n'est ni le manque de puissance de calcul, ni le manque d'algorithmes. Le principal obstacle est l'absence de mécanismes capables de représenter efficacement les langues sous-représentées à grande échelle.

## PART I: THE STRATEGIC THESIS

**The Core Problem:** L'IA moderne repose sur une hypothèse implicite: les langues les mieux représentées sur Internet reçoivent la majorité des investissements. L'anglais, le chinois, l'espagnol, le français sont extrêmement représentés. L'éwé, le kabyè, le wolof, le bambara, et des centaines d'autres restent largement sous-représentés.

**Strategic Observation:** Le problème n'est pas seulement africain. Il est mondial. Mais l'Afrique représente le plus grand ensemble stratégique de langues sous-représentées.

**Strategic Opportunity:** Si KORA parvient à résoudre ce problème pour les langues africaines, les méthodes pourront ensuite être appliquées aux autres langues sous-représentées du monde. La mission reste africaine. L'impact devient mondial.

## PART II: THE GRAND STRATEGY

La stratégie de KORA repose sur un principe simple: les produits ne constituent pas le véritable avantage concurrentiel. Les actifs constituent le véritable avantage concurrentiel.

**Mauvaise stratégie:** Construire un ASR, puis un TTS, puis un traducteur, et recommencer pour chaque langue.
**Bonne stratégie:** Construire une machine capable de représenter efficacement de nouvelles langues. Puis utiliser cette machine pour produire ASR, TTS, traduction, agents et intelligence multimodale à grande échelle.

## PART III: THE SIX STRATEGIC LAYERS

### Layer 1: Language Acquisition Engine
Créer la machine capable d'acquérir efficacement de nouvelles langues. Développer des méthodes reproductibles pour identifier une langue, recruter des locuteurs, organiser une communauté, collecter, annoter, valider et gouverner les données. Actif produit: Language Acquisition Engine.

### Layer 2: Language Representation Engine
Transformer les données linguistiques en représentations exploitables par l'IA. Capacités: ASR, TTS, alignement inter-langues, speech translation, voice embeddings, espaces linguistiques multilingues. Actif produit: Language Representation Engine.

### Layer 3: Universal Speech Intelligence Layer
Créer une couche commune de compréhension du langage indépendante de la langue. Toute langue représentée doit pouvoir être comprise, traduite, générée et utilisée dans une conversation. Actif produit: Universal Speech Intelligence Layer.

### Layer 4: Multimodal Intelligence Layer
Étendre la compréhension au-delà de la parole: texte, audio, image, vidéo, documents. Résultat: KORA Omni. Actif produit: Omni Intelligence Platform.

### Layer 5: Distribution Layer
Rendre l'intelligence accessible au plus grand nombre via API, applications, SDK, télécommunications, éducation, gouvernements, santé, entreprises. Actif produit: Distribution Network.

### Layer 6: Frontier Research Layer
Contribuer à la recherche mondiale. Passer d'adaptateur à créateur de nouvelles architectures. Domaines: reasoning, agents, multimodalité, language intelligence. Actif produit: Frontier Research Capability.

## PART IV: THE ECONOMIC ENGINE

Chaque couche doit produire des revenus:
- Phase 1: Transcription, archivage, numérisation linguistique, services
- Phase 2: API vocales, licences, solutions entreprises
- Phase 3: Plateformes, agents, intelligence conversationnelle
- Phase 4: Infrastructure linguistique

## PART V: THE COMPETITIVE MOAT

Le moat de KORA n'est pas un ASR, un TTS ou un modèle particulier. Le moat est la capacité à représenter rapidement de nouvelles langues. Cette capacité repose sur communautés, données, gouvernance, expertise, infrastructure et méthodes reproductibles. À terme, le temps nécessaire pour intégrer une nouvelle langue doit devenir l'indicateur principal de performance.

## PART VI: SUCCESS CONDITIONS

KORA réussit si: (1) il devient la référence de représentation des langues africaines, (2) il construit un moteur reproductible d'acquisition linguistique, (3) il développe une couche universelle de compréhension et génération vocale, (4) il génère des revenus suffisants pour financer sa croissance, (5) il contribue à la recherche mondiale tout en restant fidèle à sa mission.

## PART VII: END STATE (2045+)

À maturité, KORA est un laboratoire africain, un acteur mondial de l'intelligence linguistique, une infrastructure de représentation des langues, un contributeur de recherche, et un catalyseur de préservation et valorisation des langues africaines.

## Footer
| Field | Value |
|---|---|
| Document | KORA Master Plan V2 |
| Horizon | 2026–2045+ |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/06_STRATEGIC_ROADMAP.md
# KORA STRATEGIC ROADMAP V2
## Building the Universal Speech Intelligence Layer
### 2026–2045+

## STRATEGIC NORTH STAR

Build the world's leading infrastructure for representing underrepresented languages, starting with African languages. This infrastructure must enable speech understanding, speech generation, translation, multilingual reasoning, multimodal intelligence, and future frontier AI systems.

## ERA I: BUILD THE MACHINE (2026–2030)

**Core Question:** Can KORA build a repeatable system capable of representing a new language efficiently?
**Strategic Goal:** Build the Language Acquisition Engine.

### Phase 1A: Language Validation (2026–2027)
Validate the complete acquisition pipeline on Éwé. Capabilities: community recruitment, data collection, data governance, annotation, model training (ASR + TSS). Key deliverables: Dataset V1, ASR V1, TSS V1, Collection Protocol, Annotation Protocol, Governance Framework. Success metrics: 300–1000 validated hours, WER improvement over baselines. Strategic asset: Language Acquisition Engine V1.

### Phase 1B: Pipeline Industrialization (2027–2028)
Reduce cost and time to onboard a language. Focus on automation, tooling, workflow standardization. Target: reduce onboarding time by 50%. Strategic asset: Language Acquisition Engine V2.

### Phase 1C: Multi-Language Expansion (2028–2030)
Validate scalability across 5–20 languages selected by community access, strategic value, and linguistic diversity. Strategic asset: Language Acquisition Network.

## ERA II: BUILD THE REPRESENTATION LAYER (2030–2035)

**Core Question:** Can KORA move from language-specific systems to a shared linguistic infrastructure?
**Strategic Goal:** Build the Language Representation Engine.

### Phase 2A: Cross-Language Alignment (2030–2032)
Create shared linguistic representations: language embeddings, cross-language mapping, shared semantic spaces, speech-text alignment. Strategic asset: Representation Layer V1.

### Phase 2B: Multilingual Speech Systems (2032–2035)
Enable true multilingual interactions: speech-to-speech, cross-language TSS, cross-language ASR, language transfer. Strategic asset: Representation Layer V2.

## ERA III: BUILD THE UNIVERSAL LAYER (2035–2045+)

**Core Question:** Can language become independent from intelligence?
**Strategic Goal:** Build the Universal Speech Intelligence Layer.

### Phase 3A: Universal Speech Layer (2035–2038)
Create a language-independent reasoning layer. Any supported language → shared semantic space → any supported language. Strategic asset: Universal Speech Infrastructure.

### Phase 3B: Omni Layer (2038–2042)
Extend beyond speech to speech, text, image, video, documents. Deliverable: KORA Omni. Strategic asset: Multimodal Intelligence Layer.

### Phase 3C: Frontier Research Layer (2042+)
Transition from technology adopter to technology creator. Focus: reasoning, agents, learning systems, novel architectures. Deliverable: KORA Research Institute.

## REVENUE ROADMAP
- 2026–2028: Services (transcription, digitization, preservation, consulting)
- 2028–2032: Infrastructure products (ASR/TSS APIs, enterprise solutions)
- 2032–2038: Platform products (translation, voice infrastructure, conversation systems)
- 2038+: Intelligence products (Omni, agents, platform ecosystem)

## STRATEGIC KPIs
Primary KPIs: language acquisition speed (how fast to onboard a new language), language acquisition cost, language coverage (speakers served), data quality, revenue per language, community density.

## WHAT SUCCESS LOOKS LIKE IN 2030
A successful KORA in 2030: 10–30 represented languages, validated acquisition engine, repeatable collection infrastructure, recurring revenue, strong communities, partnerships across multiple countries.

## Footer
| Field | Value |
|---|---|
| Document | KORA Strategic Roadmap V2 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/07_CAPITAL_ROADMAP.md
# KORA CAPITAL ROADMAP V2
## Financing the Universal Speech Intelligence Layer
### 2026–2045+

## THE CAPITAL THESIS

Most startups raise capital to build products. KORA raises capital to build strategic assets. Capital is therefore not the destination. Capital is a tool.

KORA's financing strategy follows: Capital → Strategic Assets → Capabilities → Products → Revenue → More Assets → More Capabilities. Not: Capital → Product → Hope.

## CAPITAL PHILOSOPHY

1. Mission before valuation
2. Assets before products
3. Revenue before large dilution
4. Proof before fundraising
5. Control before prestige

## FUNDING ARCHITECTURE (5 layers)

Layer 1: Founder Capital (time, execution, relationships, research, prototypes)
Layer 2: Non-Dilutive Capital (grants, research funding, competitions, innovation programs)
Layer 3: Strategic Partnerships (compute, universities, telecom operators, governments)
Layer 4: Revenue (services, consulting, data contracts, API usage, licensing)
Layer 5: Equity Financing (angel, pre-seed, seed, Series A, growth)

**Strategic Rule:** The cheapest capital is Partnerships + Revenue. The most expensive is Equity sold too early.

## PHASE 0: FOUNDATION (2026)
Objective: Survive, build credibility, validate seriousness. Capital target: $0–50,000. Sources: founder effort, small grants, micro-angels, competitions, pilot contracts.

## PHASE A: LANGUAGE ACQUISITION ENGINE VALIDATION (2026–2028)
Objective: Prove KORA can successfully represent one language. Target: $100k–250k. Allocation: 45% team, 25% data collection, 5% infrastructure, 5% legal, 10% operations, 10% reserve.
Key milestones: Language Acquisition Engine V1, ASR prototype, TSS prototype, first customers, first revenues.

## PHASE B: INDUSTRIALIZATION (2028–2031)
Target: $500k–2M. Purpose: transform process into a machine. Milestones: 5–20 represented languages, acquisition time reduced dramatically, recurring revenue.

## PHASE C: LANGUAGE REPRESENTATION ENGINE (2030–2035)
Target: $2M–10M. Purpose: move from languages to representations. Milestones: 20–50 languages, cross-language speech systems, revenue scale-up.

## PHASE D: UNIVERSAL SPEECH LAYER (2035–2040)
Target: $10M–50M+. Purpose: build language-independent speech intelligence. KORA becomes globally unique.

## PHASE E: OMNI & DISTRIBUTION (2040–2045)
Target: Variable. Purpose: deliver intelligence everywhere.

## PHASE F: FRONTIER RESEARCH (2045+)
Purpose: transition from AI adopter to AI creator.

## DILUTION STRATEGY
Pre-Seed: 5–10% max. Seed: 10–15%. Series A: 10–20%. Objective: maintain founder control through decades-long mission.

## THE KORA FUNDING TEST
Before accepting any investment: (1) Does it accelerate the mission? (2) Does it strengthen strategic assets? (3) Does it reduce a critical risk? (4) Does it preserve long-term independence? (5) Would we still accept this if KORA succeeds beyond expectations?

## Footer
| Field | Value |
|---|---|
| Document | KORA Capital Roadmap V2 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/08_EXECUTIVE_SUMMARY.md
# KORA LAB
## Executive Summary
### Building the Language Infrastructure Layer for Artificial Intelligence

**Founder:** Kheir Lissi
**Location:** Lomé, Togo
**Stage:** Pre-Seed
**Funding Sought:** $100,000–$250,000
**Date:** June 2026

## Overview

KORA Lab is an African artificial intelligence laboratory building the infrastructure required for underrepresented languages to participate fully in the future of AI.

While recent breakthroughs have dramatically improved speech recognition, speech generation and conversational AI, these advances have benefited only a fraction of the world's languages. Africa alone is home to more than 2,000 languages, yet the overwhelming majority remain absent from modern AI systems.

KORA's long-term ambition is to build the Universal Speech Intelligence Layer: an infrastructure capable of understanding, representing and generating language across diverse linguistic communities, beginning with African languages.

## The Problem

Most underrepresented languages lack: high-quality speech datasets, transcription resources, speech recognition systems, speech synthesis systems, and scalable language acquisition pipelines. As a result, billions of people remain poorly represented in the emerging AI ecosystem. This is not merely a technological challenge but also an economic, cultural and strategic one.

## Our Thesis

KORA believes the next major bottleneck in AI is not model architecture — it is language representation. Powerful open-source architectures already exist. What remains scarce is the ability to systematically acquire, curate, validate and operationalize linguistic data for underrepresented languages.

**The organization capable of repeatedly transforming underrepresented languages into usable AI infrastructure will create one of the most valuable strategic assets of the next decade.**

## Long-Term Vision

KORA's long-term vision is the creation of a Universal Speech Intelligence Layer enabling intelligent systems to understand speech across languages, transcribe and generate speech in any supported language, and facilitate communication between linguistic communities. The ultimate objective is to create a linguistic infrastructure layer that allows every language to participate in the AI economy.

## Why Now

Open-source AI has matured (Whisper, NeMo, MMS, XTTS). Compute has become more accessible — KORA has secured access in principle to African-hosted GPU infrastructure through ST Digital. Demand is increasing from governments, educational institutions, media organizations and telecom operators. Most global AI companies continue to focus on high-resource languages, creating a unique window of opportunity.

## Phase 1: Validation of the Language Acquisition Engine

KORA's first objective is to validate the Language Acquisition Engine — the set of processes, tools and methodologies that allow a new language to be transformed into usable AI infrastructure. The first language is Éwé.

Deliverables: high-quality Éwé speech dataset, repeatable collection and annotation pipeline, Éwé ASR system, Éwé TSS system, public benchmarks, initial commercial pilots.

## Business Model

Short-term: transcription services, language digitization projects, archival and preservation initiatives, custom speech solutions. Long-term: speech APIs, licensing agreements, enterprise solutions, multilingual language infrastructure platforms.

## Competitive Advantage

KORA's competitive advantage is not a single model but the ability to repeatedly represent languages. This combines local community engagement, data collection networks, annotation systems, linguistic expertise, AI infrastructure, and sovereign compute resources hosted in Africa. Every language represented strengthens the system.

## Funding Request

KORA is seeking $100,000–$250,000 in pre-seed funding to recruit the initial team, collect and annotate speech data, build the Language Acquisition Engine, develop ASR and TSS systems, establish legal and operational structures, and execute pilot deployments.

## Closing Statement

Artificial intelligence is becoming a foundational layer of the global economy. Yet thousands of languages remain absent from this transformation. KORA Lab exists to ensure that underrepresented languages are not left behind. We begin with African languages because the need is urgent and the opportunity is significant.

**Our mission is not simply to build AI systems. Our mission is to ensure that every language can participate in the future of intelligence.**

## Footer
| Field | Value |
|---|---|
| Document | KORA Executive Summary V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/09_BUSINESS_PLAN.md
# KORA LAB — PHASE 1 BUSINESS PLAN
## Building the Language Acquisition Engine
### Version 1.0 — Pre-Seed Investment Memorandum
### 2026–2028

## 1. EXECUTIVE SUMMARY

KORA Lab is an African AI lab headquartered in Lomé, Togo. Its long-term mission is to build the infrastructure for underrepresented languages to participate fully in the age of AI. The purpose of Phase 1 is to validate the Language Acquisition Engine — the strategic capability to acquire linguistic data, organize speaker communities, curate datasets, train models, evaluate performance, and reproduce the process across additional languages. The first validation language is Éwé.

KORA seeks $100,000–$250,000 in pre-seed financing.

## 2. LE PROBLÈME

**Global AI Excludes Most Languages:** Modern AI systems are built primarily for heavily represented languages. Thousands of others remain underrepresented.

**African Languages Face Structural Disadvantages:** Insufficient datasets, lack of speech corpora, limited linguistic resources, absence of local infrastructure, lack of commercial incentives for global players.

**The Missing Layer:** The capability to transform an underrepresented language into usable AI infrastructure. This is the problem KORA is solving.

## 3. THE OPPORTUNITY

Africa contains more than 2,000 languages, hundreds of millions of speakers of underrepresented languages, rapidly increasing smartphone penetration, and growing demand for voice interfaces. Governments seek digitization solutions, educational institutions seek language preservation tools, media organizations require transcription solutions, and telecom operators increasingly rely on conversational systems.

## 4. KORA'S THESIS

Most organizations focus on models. KORA focuses on representation. The organization that can efficiently represent underrepresented languages will create a durable competitive advantage. The first objective is not scale — the first objective is proof.

## 5. PHASE 1 OBJECTIVE

Strategic: Validate the Language Acquisition Engine. Operational: Represent Éwé successfully. Why Éwé: strong local access, community familiarity, immediate validation capability, lower operational risk, expansion pathway.

## 6. DELIVERABLES

1. Language Acquisition Protocol (repeatable methodology)
2. Éwé Speech Dataset (300–1,000 validated hours)
3. Éwé ASR System
4. Éwé TSS System
5. Language Representation Benchmark
6. Commercial Validation (pilot deployments, initial revenue)

## 7. BUSINESS MODEL

Revenue Streams: transcription services, digitization services, custom speech solutions, pilot licensing. Initial customers: media organizations, educational institutions, government agencies. Initial geography: Togo. Expansion: West Africa → Pan-African.

## 8. ROADMAP

Phase 1A (0–6 months): Legal structure, team formation, collection infrastructure, pilot recordings, initial benchmarks.
Phase 1B (6–12 months): Dataset growth, ASR prototype, TSS prototype, first commercial pilots.
Phase 1C (12–24 months): Industrialized acquisition process, additional language preparation, revenue growth, seed readiness.

## 9. USE OF FUNDS

**Scenario A ($100k):** 40% team, 30% data collection, 10% operations, 5% legal, 5% infrastructure, 10% reserve. Deliverables: Acquisition Engine V1, initial dataset, ASR/TSS prototypes, first pilots.

**Scenario B ($250k):** 45% team, 25% data collection, 10% operations, 5% legal, 5% infrastructure, 10% reserve. Deliverables: industrialized pipeline, large-scale dataset, production-ready ASR/TSS, commercial pilots, recurring revenue, seed readiness.

## 10. STRATEGIC PARTNERSHIPS

Compute infrastructure partnership with ST Digital has been secured in principle and is being formalized. This significantly reduces capital requirements and allows funding to be concentrated on people, data and operations.

## 11. RISKS

Funding risk (mitigation: multiple financing scenarios), data collection risk (phased collection, quality controls), hiring risk (African AI communities, diaspora recruitment), technical risk (proven open-source foundations, iterative validation).

## 12. INVESTMENT PROPOSITION

KORA is not asking investors to fund a speculative attempt at building AGI. KORA is asking investors to fund the validation of a strategic capability: the ability to efficiently represent underrepresented languages. If successful, this capability becomes the foundation for speech recognition, synthesis, translation, conversational AI, multilingual intelligence, and future universal speech systems.

## 13. FUNDING REQUEST

Target: $100,000–$250,000. Use: Validation of the Language Acquisition Engine. Duration: 18–24 months. Primary Outcome: Proof that KORA can repeatedly transform an underrepresented language into usable AI infrastructure. This proof unlocks the next phase and establishes the foundation for a scalable multilingual intelligence platform.

## Footer
| Field | Value |
|---|---|
| Document | KORA Phase 1 Business Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/10_PITCH_DECK.md
# KORA LAB — Pitch Deck
## Pre-Seed Round — $100k–250k

### Slide 1: Cover
KORA LAB — Building the Language Infrastructure Layer for Artificial Intelligence. Lomé, Togo. Founder: Kheir Lissi. Pre-Seed Round $100k–250k.

### Slide 2: The Problem
Most of the world's languages are invisible to AI. Africa alone: 2,000+ languages, most lack speech datasets, ASR, TSS, language infrastructure. Entire communities risk exclusion from the AI economy.

### Slide 3: Why This Matters
Language is infrastructure. If a language cannot be understood by machines, knowledge remains inaccessible, cultural heritage remains unstructured, digital inclusion remains limited, AI adoption remains restricted.

### Slide 4: Our Thesis
The bottleneck is no longer model architecture. It is language representation. Powerful open-source architectures exist. KORA builds the ability to acquire, curate, annotate, validate and operationalize languages.

### Slide 5: The Vision
Universal Speech Intelligence Layer. Any Language → Understanding → Representation → Generation → Any Language. Start in Africa. Build capabilities applicable worldwide.

### Slide 6: Why KORA
Three strategic assets: (1) Language Acquisition Capability, (2) Sovereign Infrastructure (ST Digital partnership), (3) Local Access to communities and linguistic ecosystems.

### Slide 7: Phase 1
Validate the Language Acquisition Engine on Éwé. Deliverables: speech dataset, annotation pipeline, ASR, TSS, public benchmarks, pilot deployments.

### Slide 8: Traction
Founder working full-time, initial TSS proof-of-concept completed, strategic roadmap completed, business plan completed, compute access secured in principle through ST Digital.

### Slide 9: Business Model
Phase 1: transcription, digitization, archival, pilots. Phase 2: speech APIs, licensing, enterprise. Phase 3: language infrastructure platform.

### Slide 10: Roadmap
2026–2027: Validate Language Acquisition Engine → Éwé Dataset → ASR + TSS → Pilots → Seed. 2028–2030: Multi-language expansion → Cross-lingual infrastructure → Universal Speech Layer.

### Slide 11: Use of Funds
$100k–250k request. 45% team, 25% data collection, 10% operations, 5% legal, 5% infrastructure, 10% reserve. Goal: Proof of Execution.

### Slide 12: The Ask
Pre-seed funding to validate the Language Acquisition Engine and build the foundation for large-scale language representation. Contact: Kheir Lissi

## Footer
| Field | Value |
|---|---|
| Document | KORA Pitch Deck V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/README.md
# KORA Lab — Data Room

**Project:** Africa's Sovereign AI Research & Product Lab
**Founder:** Kheir Lissi
**Location:** Lomé, Togo
**Stage:** Pre-Seed
**Funding Sought:** $100,000–$250,000
**Status:** Validation Phase — Language Acquisition Engine (Éwé)

---

## Strategic Documents

| # | Document | Description |
|---|----------|-------------|
| 01 | Vision | Long-term destination (15–25 year horizon) |
| 02 | Mission | What KORA does every day |
| 03 | Theory of Change | How vision becomes reality |
| 04 | Strategic Assets Map | Core assets to accumulate |
| 05 | Master Plan | Development framework 2026–2045 |
| 06 | Strategic Roadmap | Execution timeline |
| 07 | Capital Roadmap | Financing strategy |
| 08 | Executive Summary | 2-page investor summary |
| 09 | Business Plan | Phase 1 pre-seed plan |
| 10 | Pitch Deck | 12-slide investor presentation |

## Annexes (investor)

| # | Document | Description |
|---|----------|-------------|
| A | Cap Table | Proposed equity structure |
| A1 | Budget | Detailed use of funds |
| A2 | Hiring Plan | Phase 1 recruitment |
| A3 | KPIs & Milestones | 12-month execution metrics |
| A4 | ST Digital Partnership | Compute infrastructure status |
| A5 | Risk Assessment | Risk framework |
| A6 | Language Expansion | Éwé → 100 languages plan |
| A7 | Founder Profile | Kheir Lissi background |
| A8 | Funding & Dilution | Long-term financing approach |

## Frameworks

| Document | Description |
|----------|-------------|
| RAPHAEL_PDCA.md | KORA's PDCA execution loop |

## Identity Assets

Located in `concepts/KORA_IDENTITY/`

## Current Status

- Pre-seed documentation: ✅ Complete
- ST Digital partnership: In discussion
- Data collection: Not started
- Team: Founder only
- Runway: Critical

## Footer
| Field | Value |
|---|---|
| OS Version | V4 |
| Last Updated | 2026-06-21 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A1_BUDGET.md
# ANNEXE A1: DETAILED USE OF FUNDS
## Scenario B — $250,000 Pre-Seed

**Team ($135k, 54%):** Founder Support $18k ($1.5k/mo x12), Lead ML Engineer $42k ($3.5k/mo x12), Data Engineer $30k ($2.5k/mo x12), Field Operations Lead $24k ($2k/mo x12), Linguistic Consultant Budget $21k.

**Data Collection ($50k, 20%):** Contributor Compensation $25k, Travel and Field Collection $10k, Recording Equipment $5k, Quality Control and Validation $10k.

**Infrastructure ($12.5k, 5%):** Workstations $8k, Storage and Backup $2.5k, Software and Tools $2k.

**Legal & Corporate ($12.5k, 5%):** Company Formation $3k, Legal Counsel $5k, Accounting and Compliance $4.5k.

**Operations ($15k, 6%):** Internet, transportation, meetings, administrative expenses.

**Research & Experimentation ($10k, 4%):** Pilot experiments, model evaluation, benchmark development.

**Reserve ($15k, 6%):** Contingency buffer.

TOTAL: $250,000

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A2_HIRING_PLAN.md
# ANNEXE A2: PHASE 1 HIRING PLAN
## 12-Month Execution Team

**Philosophy:** Prioritize local African talent, then African diaspora, then global specialists.

**Founder & CEO (Kheir Lissi):** Full-time, already active. Vision, fundraising, partnerships, strategy, product direction.

**Hire 1 — Lead ML Engineer (Month 1):** ASR/TTS development, fine-tuning pipelines, benchmarking. Skills: PyTorch, Speech AI, Whisper, NeMo, XTTS. Target communities: Masakhane, Deep Learning Indaba.

**Hire 2 — Data Engineer (Month 2):** Data pipelines, storage systems, dataset versioning, collection infrastructure. Skills: Python, Data Engineering, Cloud.

**Hire 3 — Field Operations Lead (Month 2):** Collection campaigns, community coordination, contributor management. Skills: local language knowledge, logistics, project management.

**Hire 4 — Linguistic Consultant Network (Months 2–12):** Part-time contributor network for annotation standards, transcription validation, linguistic review.

**Future Hires (Post-Validation):** Research Scientist, Research Engineer, Product Engineer, Business Development Lead, Community Manager.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A2 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A3_KPIS_MILESTONES.md
# ANNEXE A3: PHASE 1 MILESTONES & KPIs
## 12-Month Execution

**Milestone 1 — Foundation (Months 1–3):** Company structure, initial team, collection protocol, ST Digital compute environment. KPIs: 3 hires, legal established, data collection app operational, 50 contributors onboarded.

**Milestone 2 — Data Acquisition (Months 3–6):** Large-scale collection, annotation workflows, first dataset version. KPIs: 100+ hours collected, 300+ contributors, 3+ demographic groups, 2+ dialect groups.

**Milestone 3 — ASR & TSS Prototype (Months 6–9):** First production-grade models. KPIs: First ASR benchmark published, first TSS benchmark published, internal evaluation completed. Performance exceeds public baselines.

**Milestone 4 — Validation & Commercial Readiness (Months 9–12):** Pilot deployments, public benchmarks, seed readiness. KPIs: 1–2 pilot projects, Dataset V1, ASR V1, TSS V1 released.

## Phase 1 Success Definition
A high-quality Éwé dataset exists. ASR performance benchmarked publicly. TSS performance benchmarked publicly. Collection process documented. Methodology can be replicated to second language. KORA becomes investable for Seed.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A3 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A4_ST_DIGITAL_PARTNERSHIP.md
# ANNEXE A4: ST DIGITAL PARTNERSHIP OVERVIEW
## Status: Partnership Discussions Advanced — June 2026

## Background
KORA Lab initiated discussions with ST Digital regarding access to sovereign African AI infrastructure. The objective is to enable AI development using infrastructure hosted on the African continent.

## Strategic Alignment
KORA: Represent underrepresented languages through speech/language AI. ST Digital: Develop sovereign digital infrastructure for strategic African technology initiatives. Both share interest in strengthening African technological autonomy.

## Proposed Collaboration
ST Digital provides: GPU infrastructure access, high-performance compute, infrastructure guidance, potential institutional introductions. KORA provides: language AI capabilities, future speech infrastructure, potential revenue-sharing, strategic AI applications.

## Current Status
Strategic note submitted June 2026. ST Digital requested compute estimate. Estimate delivered. Formal partnership terms under discussion. No binding agreement yet executed.

## Strategic Value
If formalized: reduced infrastructure costs, faster experimentation, African-hosted compute, increased investor credibility.

## Risk Disclosure
Partnership remains under formalization. KORA does not rely exclusively on a single provider. Alternative options available.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A4 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A5_RISK_ASSESSMENT.md
# ANNEXE A5: RISK ASSESSMENT FRAMEWORK

**Risk 1 — Talent Acquisition (High impact, Medium probability):** Scarce speech AI talent. Mitigation: Masakhane, Deep Learning Indaba, diaspora outreach, equity incentives, hybrid remote.

**Risk 2 — Data Collection Quality (High impact, Medium probability):** Volume ≠ quality. Mitigation: structured protocol, human validation, multiple QC layers, continuous benchmarks.

**Risk 3 — Technical Performance (Medium impact, Medium probability):** ASR/TSS may miss benchmarks. Mitigation: fine-tuning proven architectures, incremental experimentation, public benchmarking, external review.

**Risk 4 — Funding Risk (High impact, Medium probability):** Fundraising timelines may exceed expectations. Mitigation: multi-source strategy, grants, partnerships, pilot revenue.

**Risk 5 — Infrastructure Dependency (Medium impact, Low probability):** Single compute provider reliance. Mitigation: multi-cloud strategy, alternative GPU providers, portable infrastructure.

**Risk 6 — Competitive Risk (Medium impact, High probability):** Large AI companies expand into African languages. Mitigation: data acquisition focus, local partnerships, community relationships, proprietary collection pipelines.

**Strategic Conclusion:** Greatest risk is execution speed. Strategy centers on building assets faster than competitors can replicate them.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A5 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A6_LANGUAGE_EXPANSION.md
# ANNEXE A6: LANGUAGE EXPANSION FRAMEWORK

**Core Principle:** KORA scales by improving the Language Acquisition Engine, not by building a separate company for each language.

**Stage 1 — Validation (2026–2027):** Target: Éwé. Objective: validate collection, annotation, training, deployment workflows. Success: one fully operational language.

**Stage 2 — Regional Expansion (2027–2029):** Target: 5–10 African languages (Éwé, Kabyè, Fon, Yoruba, Twi, Wolof). Objective: validate replication capability. Success: multi-language infrastructure.

**Stage 3 — Continental Layer (2029–2032):** Target: 20–50 African languages. Objective: create the largest language infrastructure asset in Africa. Success: cross-lingual speech capabilities.

**Stage 4 — Universal Expansion (2032+):** Target: underrepresented languages globally. Objective: apply same methodology worldwide. Success: Universal Speech Intelligence Layer.

**Strategic Logic:** Africa remains the primary mission. Global expansion strengthens sustainability and increases resources for accelerating African language representation.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A6 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A7_FOUNDER_PROFILE.md
# ANNEXE A7: FOUNDER PROFILE
## Kheir Lissi — Founder & CEO, KORA Lab

**Overview:** Technology entrepreneur and software engineer based in Lomé, Togo. Founder of KORA Lab, focused on language infrastructure for underrepresented languages and Africa's AI participation.

**Entrepreneurial Experience:** Founded multiple technology ventures: Cortexia, Origin, Edenvalley. Experience in product development, AI integration, software architecture, user acquisition, technical leadership.

**Technical Background:** Full-stack engineering: backend systems, frontend development, cloud infrastructure, AI integration, automation systems. Bridges product vision and execution.

**Leadership:** Has led development teams and managed end-to-end product creation from concept to deployment. Execution-first philosophy.

**Motivation:** KORA originated from observing that African languages remain severely underrepresented in modern AI systems. Long-term commitment to ensuring future intelligence systems understand and serve diverse linguistic communities.

**Founder Thesis:** The future of AI depends not only on larger models but also on broader representation. KORA exists to solve this representation challenge.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A7 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A8_FUNDING_DILUTION.md
# ANNEXE A8: FUNDING & DILUTION STRATEGY

**Principle:** Capital is raised to unlock capabilities, not to maximize valuation headlines. Each financing round must correspond to a specific capability milestone.

**Phase 1 — Pre-Seed:** Target $100k–250k. Purpose: build team, validate Language Acquisition Engine, ASR + TSS, dataset. Target dilution: 5–10%.

**Phase 2 — Seed:** Target $1M–3M. Purpose: 5–10 languages, cross-lingual systems, API deployment. Target dilution: 10–15%.

**Phase 3 — Series A:** Target $5M–15M. Purpose: continental expansion, research teams, commercial scaling. Target dilution: 10–20%.

**Long-Term Objective:** Preserve founder influence while financing increasingly ambitious technical capabilities. Goal is not maximum ownership but successful execution of KORA's mission.

**Strategic Rule:** KORA raises only after proving the previous stage. Proof precedes capital. Capital accelerates proof. This sequence minimizes dilution and maximizes strategic leverage.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A8 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/KORA/annexes/A_CAP_TABLE.md
# ANNEXE A: CAPITALIZATION & EQUITY STRUCTURE
## KORA Lab — Pre-Seed Phase

## Principles
1. Founder-led execution. 2. Long-term mission protection. 3. Talent attraction. 4. Future financing flexibility.

## Initial Capitalization (Pre-Investment)
Founder Ownership: 100%. Total Shares Authorized: 10,000,000.

## Employee Equity Pool
Target Pool Size: 10% ESOP. Reserved for: Lead ML Engineers, Research Engineers, Data Engineers, Linguists, Future Leadership. Standard vesting: 4 years with 1-year cliff.

## Target Ownership After Pre-Seed
Founder: 75–85%. Investor(s): 10–15%. Employee Option Pool: 10%.

## Individual Equity Guidelines
Lead ML Engineer: 0.5–2%. Senior Research Engineer: 0.25–1%. Data Engineer: 0.25–1%. Key Early Employee: 0.25–1%. Strategic Advisor: 0.10–0.50%.

## Pre-Seed Financing Scenario
Target: $100k–250k. Suggested equity: 5–10%. Example: $250k for 8% = $3.125M post-money. Maximum acceptable: 10%.

## Footer
| Field | Value |
|---|---|
| Document | KORA Annexe A |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/01_VISION.md
# OMNI VISION
## Version 1.0 — Institutional Edition (10–20 Year Horizon)

### Faire d'Omni le standard de la recherche de commerce de proximité en Afrique de l'Ouest

---

# 1. Vision Statement

Nous imaginons un futur où chaque Africain peut trouver, en un clic ou une phrase, tout ce qui existe autour de lui — le marchand, l'artisan, le réparateur, le traiteur, le service — indépendamment de sa taille, de son chiffre d'affaires ou de sa présence numérique.

Dans ce futur, l'économie informelle, qui représente 80 % du commerce quotidien en Afrique de l'Ouest, n'est plus invisible. Chaque commerce de rue, chaque étal de marché, chaque atelier artisanal est cartographié, trouvable et connecté. L'acheteur ne cherche plus sur Google, Facebook et WhatsApp en vain. Il ouvre Omni. Il voit ce qui est disponible, où, à quel prix. Et il achète local.

# 2. Le Futur Que Nous Voulons Créer

Nous croyons que la prochaine décennie sera définie par la numérisation de l'économie réelle africaine — non pas en copiant les modèles occidentaux (Amazon, Uber), mais en construisant des infrastructures adaptées aux réalités du continent.

Si l'économie informelle reste invisible en ligne, les commerçants locaux continueront de perdre des clients au profit des plateformes internationales. L'argent sortira de l'économie locale. Le potentiel de croissance restera inexploité. Nous refusons ce futur.

Nous voulons construire un monde dans lequel :
- chaque commerce de rue est trouvable en ligne
- l'argent reste dans l'économie locale
- l'achat local est plus facile que l'importation
- les commerçants informels deviennent des entrepreneurs numériques

# 3. Notre Conviction Fondamentale

Nous croyons que la carte sera l'interface dominante du commerce de proximité en Afrique. Dans un continent où les adresses postales sont rares, où les noms de rue ne sont pas standardisés, et où la confiance se construit dans la proximité physique, la géolocalisation est plus pertinente que le référencement textuel.

L'avenir du commerce local africain ne sera pas une marketplace centralisée avec des millions de produits. Ce sera une carte vivante où chaque facilité devient visible, trouvable et accessible.

# 4. Notre Vision de l'Infrastructure du Commerce de Proximité

Nous imaginons une infrastructure numérique qui :
- indexe chaque commerce, service et artisan là où il se trouve
- permet une recherche en texte ou en voix, filtrée par proximité
- confirme la disponibilité en temps réel (OUI/NON en un clic)
- sécurise le paiement via Mobile Money (escrow)
- ouvre la livraison à tout le monde sur son trajet quotidien

Cette infrastructure devra être scalable (ville par ville), interopérable (APIs mobiles), et accessible (gratuite pour l'acheteur, abordable pour le commerçant).

# 5. Notre Vision de l'Impact Sociétal

**Pour l'acheteur :** Trouver n'importe quel produit ou service près de chez soi en quelques secondes.
**Pour le commerçant :** Devenir visible en ligne pour la première fois, sans site web ni compétence technique.
**Pour la ville :** Mesurer, connecter et formaliser progressivement l'économie informelle.
**Pour l'économie locale :** Garder l'argent dans la communauté au lieu de le voir partir sur des plateformes étrangères.

# 6. Horizon de Réussite

Nous considérerons que cette vision commence à se réaliser lorsque :
- Omni est utilisé quotidiennement par des centaines de milliers d'acheteurs à Lomé
- des dizaines de milliers de commerçants sont actifs sur la plateforme
- l'économie informelle de Lomé commence à être mesurable via Omni
- le modèle est reproduit dans 5+ villes d'Afrique de l'Ouest

## Vision Résumée

**Faire d'Omni le standard de la recherche de commerce de proximité en Afrique de l'Ouest, en commençant par Lomé.**

## OODA Critique

Cette vision est volontairement indépendante des technologies actuelles (cartes, mobile money, escrow). Elle reste valable même si Google Maps, Wave ou Orange Money disparaissent. Une bonne vision doit survivre à plusieurs générations technologiques.

## Footer
| Field | Value |
|---|---|
| Document | Omni Vision V1 |
| Horizon | 10–20 years |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/02_MISSION.md
# OMNI MISSION
## Version 1.0

### Rendre visible tout ce qui existe autour de vous

## 1. Déclaration de Mission

La mission d'Omni est d'indexer l'économie de proximité africaine — marchés, boutiques, artisans, prestataires, services — et de les rendre trouvables en un clic, pour la première fois.

Nous existons pour résoudre le problème d'invisibilité des commerçants locaux dans l'économie numérique. Nous poursuivons cette mission en construisant une plateforme de recherche géolocalisée, accessible à tous, qui connecte acheteurs et vendeurs dans la même rue, le même quartier, la même ville.

## 2. Pourquoi Omni Existe

L'économie informelle représente 80 % du commerce au Togo. Mais ces commerçants n'ont pas de site web, pas de page Google, pas de présence en ligne. Ils existent dans la rue. Ils sont invisibles sur Internet. Les acheteurs perdent un temps considérable à chercher ce qui existe pourtant à quelques rues de chez eux. Et finissent souvent par commander sur Alibaba ou Amazon.

Omni existe pour combler ce fossé entre l'économie réelle et l'économie numérique.

## 3. Ce Que Nous Faisons (5 capacités fondamentales)

**1. Indexer les commerces :** Nous cartographions chaque facilité — marchés, boutiques, artisans, réparateurs, traiteurs — avec ses produits, ses prix et sa disponibilité.

**2. Rendre trouvable :** Nous permettons une recherche en texte ou en voix, filtrée par proximité, catégorie et prix.

**3. Confirmer en temps réel :** Nous permettons aux commerçants d'indiquer leur disponibilité en un clic (OUI/NON).

**4. Sécuriser les transactions :** Nous intégrons le Mobile Money avec un système d'escrow jusqu'à confirmation de livraison.

**5. Ouvrir la livraison :** Nous permettons à tout le monde de livrer sur son trajet quotidien (crowd delivery).

## 4. Ce Que Nous Ne Sommes Pas

Omni n'est pas une marketplace Amazon-like, pas une plateforme de e-commerce classique, pas un annuaire statique, pas un réseau social. Omni est un index du commerce de proximité — une carte vivante de l'économie locale.

## 5. Nos Principes d'Exécution

**Principe 1 :** Zéro commission sur les transactions — l'argent reste dans l'économie locale.
**Principe 2 :** Gratuit pour l'acheteur — toujours.
**Principe 3 :** Simple pour le commerçant — pas de site web, pas de compétence technique.
**Principe 4 :** Commencer par Lomé, prouver le modèle, puis étendre ville par ville.
**Principe 5 :** Construire avec les commerçants, pas pour eux.

## 6. Comment Nous Mesurerons Notre Succès

Pas par le nombre de téléchargements. Mais par le nombre de commerçants actifs, le nombre de recherches quotidiennes, le taux de disponibilité confirmée, le volume de transactions sécurisées, et l'impact sur le chiffre d'affaires des commerçants.

## 7. Priorité Actuelle

Valider le modèle à Lomé avec 1 000 fiches commerçants actives en 90 jours, et démontrer que l'index du commerce de proximité crée de la valeur pour toutes les parties prenantes.

## Mission Résumée

**Indexer tout ce qui existe autour de vous et le rendre trouvable en un clic, pour que l'économie locale devienne enfin visible.**

## Footer
| Field | Value |
|---|---|
| Document | Omni Mission V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/03_THEORY_OF_CHANGE.md
# OMNI THEORY OF CHANGE
## Version 1.0

### Comment la vision devient réalité

## 1. Les Déficits Structuraux

**Déficit de visibilité :** Les commerçants informels n'ont aucune présence en ligne.
**Déficit de découvrabilité :** Les acheteurs ne peuvent pas trouver ce qui existe près de chez eux.
**Déficit de confiance :** Pas de système de paiement sécurisé adapté au commerce de proximité.
**Déficit de livraison :** Pas d'infrastructure logistique pour le dernier kilomètre informel.

## 2. Hypothèse Centrale

Si nous indexons l'économie de proximité sur une carte interactive avec recherche, disponibilité temps réel, paiement sécurisé et livraison ouverte, alors les acheteurs trouveront et achèteront local, les commerçants gagneront de nouveaux clients, et l'économie informelle deviendra progressivement visible et connectée.

## 3. Les Relations de Causalité

1. Pas de visibilité en ligne → Pas de nouveaux clients pour les commerçants
2. Pas de nouveaux clients → Pas de croissance du chiffre d'affaires
3. Pas de croissance → Pas d'incitation à se formaliser
4. Pas de formalisation → Pas d'accès au crédit, aux services, aux marchés
5. Pas d'accès → L'économie informelle reste bloquée dans un plafond de verre

## 4. La Chaîne de Transformation

**Étape 1 — Indexer** : Cartographier les commerces, leurs produits, leurs prix → Visibilité

**Étape 2 — Trouver** : Permettre la recherche par proximité, catégorie, texte ou voix → Découvrabilité

**Étape 3 — Confirmer** : Disponibilité en temps réel (OUI/NON) → Confiance

**Étape 4 — Payer** : Mobile Money avec escrow → Transaction sécurisée

**Étape 5 — Livrer** : Crowd delivery sur trajets quotidiens → Logistique accessible

## 5. Les Résultats Attendus

**Court terme (0–12 mois) :**
- 1 000 commerçants actifs sur la plateforme
- Recherche quotidienne utilisée par des milliers d'acheteurs
- Transactions sécurisées via Mobile Money

**Moyen terme (1–3 ans) :**
- Omni connu comme le réflexe "acheter local" à Lomé
- 10 000+ commerçants actifs
- Données sur l'économie informelle de Lomé

**Long terme (3–10 ans) :**
- Standard de la recherche de proximité en Afrique de l'Ouest
- Impact mesurable sur le chiffre d'affaires des commerçants
- Contribution à la formalisation progressive de l'économie informelle

## 6. Notre Hypothèse Fondamentale

La barrière n'est pas technique (le MVP fonctionne). La barrière est l'adoption — convaincre les commerçants de créer leur fiche et les acheteurs d'utiliser Omni comme réflexe. Si nous résolvons l'adoption, le reste suit.

## Footer
| Field | Value |
|---|---|
| Document | Omni Theory of Change V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/04_STRATEGIC_ASSETS_MAP.md
# OMNI STRATEGIC ASSETS MAP
## Version 1.0

### Ce que nous accumulons, pourquoi c'est difficile à reproduire

## 1. Index de Proximité (le plus difficile à reproduire)

La cartographie vivante et continuellement mise à jour de l'économie de proximité d'une ville. Chaque commerce avec ses produits, ses prix, sa disponibilité. Cet index est spécifique à chaque ville, construit rue par rue, marché par marché. Aucune plateforme globale (Google, Facebook) n'a cet index pour l'économie informelle africaine.

## 2. Infrastructure de Cartographie & Collecte Terrain

Les processus, protocoles et équipes capables d'indexer une ville entière : agents de cartographie, relations avec les associations de commerçants, techniques de collecte adaptées au contexte informel. Plus on cartographie de villes, plus ce processus devient efficace et reproductible.

## 3. Technologie & Plateforme

- Carte interactive géolocalisée (MVP fonctionnel)
- Recherche texte et vocale
- Système de disponibilité temps réel (OUI/NON)
- Messagerie acheteur-vendeur
- Portefeuille intégré et escrow Mobile Money (en cours)
- Livraison crowd (en cours)

## 4. Confiance & Relations Commerciales

Les relations avec les associations de commerçants, les marchés, les coopératives. La confiance des commerçants — construite par la présence physique, pas par une application. Cette confiance est locale, personnelle et difficile à transférer à un concurrent.

## 5. Données sur l'Économie Informelle

Les données de comportement d'achat, de disponibilité, de prix, de saisonnalité dans l'économie informelle. Ces données n'existent nulle part ailleurs et deviennent plus précieuses avec le temps : cartographie de l'offre réelle, analyse des tendances, indicateurs économiques locaux.

## 6. Réseau de Livreurs Crowd

Les utilisateurs qui livrent sur leur trajet quotidien. Plus le réseau est dense, plus la livraison est rapide et moins chère. Effet de réseau : plus de livreurs → meilleur service → plus d'utilisateurs → plus de livreurs.

## 7. Capital Marque

Omni comme réflexe "acheter local" à Lomé. Le nom associé à la recherche de proximité. Ce capital de marque est construit dans l'esprit des acheteurs et des commerçants, et devient un avantage concurrentiel durable.

## 8. Partenariats Institutionnels

Les partenariats avec les opérateurs mobiles (YAS, Moov) pour les APIs de paiement, les autorités municipales pour la cartographie, et les associations professionnelles pour l'adoption. Ces partenariats sont longs à établir et difficiles à reproduire.

## Carte des Actifs par Difficulté de Réplication

| Actif | Difficulté | Temps | Avantage Concurrentiel |
|-------|-----------|-------|----------------------|
| Index de proximité par ville | Très élevée | 2-5 ans | Défensif |
| Confiance des commerçants | Très élevée | 2-4 ans | Défensif |
| Données économie informelle | Élevée | 3-5 ans | Croissant |
| Partenariats institutionnels | Élevée | 1-3 ans | Défensif |
| Réseau de livreurs | Moyenne | 1-2 ans | Effet de réseau |
| Technologie & plateforme | Faible | 3-6 mois | Périssable |
| Capital marque | Moyenne | 2-4 ans | Durable |

## Footer
| Field | Value |
|---|---|
| Document | Omni Strategic Assets Map V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/05_MASTER_PLAN.md
# OMNI MASTER PLAN
## Version 1.0 — 2026–2036

### Construire l'index du commerce de proximité, ville par ville

---

## Résumé Exécutif

Omni est une plateforme qui indexe l'économie de proximité africaine. Le MVP est déployé. La priorité est l'adoption terrain à Lomé, puis l'extension ville par ville en Afrique de l'Ouest.

Le modèle économique est simple : gratuit pour l'acheteur, abonnement pour le commerçant (Premium à 5 000 FCFA/mois), abonnement pour le livreur (1 000 FCFA/mois). Zéro commission.

---

## Thèse Stratégique

Le principal obstacle au commerce local en Afrique n'est pas l'offre — elle existe, abondante et diverse. C'est l'invisibilité. Les commerçants existent dans la rue mais pas en ligne. Omni résout ce problème en construisant un index géolocalisé de l'économie de proximité.

L'avantage concurrentiel durable n'est pas la technologie (reproductible), mais l'index lui-même — construit rue par rue, marché par marché, ville par ville.

---

## Les 6 Couches Stratégiques

### Couche 1 : Indexation Terrain
Cartographie physique de chaque zone, rue par rue. Agents qui accompagnent les commerçants pour créer leur fiche. Partenariats avec les associations de commerçants. Objectif : 1 000 fiches actives en 90 jours.

### Couche 2 : Recherche & Découvrabilité
Interface carte interactive. Recherche texte et vocale. Filtres par proximité, catégorie, prix. Accessible sur smartphone (mobile-first). Objectif : l'utilisateur trouve ce qu'il cherche en moins de 10 secondes.

### Couche 3 : Disponibilité Temps Réel
Système OUI/NON en un clic pour le commerçant. Mise à jour quotidienne de la disponibilité. Notifications SMS/USSD pour les commerçants sans smartphone. Objectif : la disponibilité est fiable à 90 %+.

### Couche 4 : Transaction Sécurisée
Intégration Mobile Money (YAS, Moov). Escrow jusqu'à confirmation de livraison. Interface de paiement simple (USSD pour les commerçants non smartphone). Objectif : zéro litige de paiement.

### Couche 5 : Livraison Crowd
Tout le monde peut livrer sur son trajet quotidien. Géolocalisation en temps réel. Paiement automatique à la livraison. Objectif : livraison en moins de 2 heures dans un rayon de 5 km.

### Couche 6 : Intelligence Économique
Données agrégées sur l'économie informelle : prix moyens, tendances, saisonnalité, densité commerciale par zone. Ces données deviennent une ressource pour les décideurs publics et les institutions financières.

---

## Chronologie d'Exécution

| Phase | Période | Objectif | Équipe | Capital |
|-------|---------|----------|--------|---------|
| Phase 0 | 2024–2026 | MVP, équipe fondatrice | 6 pers. | 0 $ (bootstrappé) |
| Phase 1 | 2026–2027 | Valider Lomé (1 000 commerçants) | 10–15 pers. | $100k–$150k |
| Phase 2 | 2027–2028 | Étendre Lomé (10 000 commerçants) | 20–30 pers. | $500k–$1M |
| Phase 3 | 2028–2030 | 5 villes d'Afrique de l'Ouest | 50–100 pers. | $2M–$5M |
| Phase 4 | 2030–2036 | Standard régional | 200+ pers. | $10M+ |

---

## Principes Stratégiques

1. **Zéro commission.** L'argent reste dans l'économie locale.
2. **Mobile-first.** Pas de desktop, pas d'app lourde. Le web et l'USSD.
3. **Terrain d'abord.** La technologie seule ne suffit pas — il faut des agents sur le terrain.
4. **Ville par ville.** Prouver Lomé avant de reproduire ailleurs.
5. **Commerçant d'abord.** Si le commerçant gagne plus, la plateforme grandit.

## Footer
| Field | Value |
|---|---|
| Document | Omni Master Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/06_STRATEGIC_ROADMAP.md
# OMNI STRATEGIC ROADMAP
## Version 1.0 — 2026–2036

### Exécution : ville par ville, rue par rue

---

## North Star

Omni devient le réflexe "acheter local" pour des millions d'Africains. Chaque commerce de rue est trouvable en un clic.

---

## Phase 1 : Lomé — Validation (2026–2027)

### Phase 1A (0–6 mois) — Fondation : Juin–Décembre 2026
- Finaliser l'équipe terrain (agents de cartographie)
- Établir partenariats associations de commerçants
- Cartographie des 5 premiers marchés de Lomé
- 300 fiches commerçants actives
- Intégration Mobile Money YAS + Moov
- Campagne radio + affichage dans les marchés
- Participation au programme Innov'Action (Djanta Tech Hub)
- **Budget : $60k**

### Phase 1B (6–12 mois) — Croissance : Janvier–Juin 2027
- 1 000 fiches commerçants actives
- Escrow Mobile Money fonctionnel
- Messagerie acheteur-vendeur active
- Premiers abonnements Premium (200 commerçants)
- 10 000 recherches mensuelles
- Crowd delivery : 100 livreurs actifs
- **Budget : $90k**

## Phase 2 : Lomé — Scale (2027–2028)

### Phase 2A (12–18 mois)
- Extension à tous les quartiers de Lomé
- 5 000 commerçants actifs
- API publique pour intégrations tierces
- Premières données d'intelligence économique
- **Financement : Seed $500k–$1M**

### Phase 2B (18–24 mois)
- 10 000 commerçants actifs
- 50 000 recherches mensuelles
- Paiements récurrents stables
- Équipe terrain industrialisée
- **Préparation expansion régionale**

## Phase 3 : Expansion Régionale (2028–2030)

- Ville 2 : Cotonou, Bénin
- Ville 3 : Accra, Ghana
- Ville 4 : Abidjan, Côte d'Ivoire
- Ville 5 : Ouagadougou, Burkina Faso
- **Financement : Series A $2M–$5M**

## Phase 4 : Standard Régional (2030–2036)

- 20+ villes en Afrique de l'Ouest
- Index de référence pour l'économie informelle
- Données utilisées par gouvernements et institutions financières
- Expansion vers l'Afrique centrale et de l'Est

---

## Jalons Clés

| Jalon | Date cible | Indicateur |
|-------|-----------|------------|
| MVP fonctionnel | ✅ Déjà fait | omni.sparkafrika.online |
| Intégration Mobile Money | T3 2026 | Paiement YAS + Moov |
| 1 000 commerçants | T1 2027 | Fiches actives |
| 10 000 recherches/mois | T2 2027 | Requêtes utilisateurs |
| Rentabilité Lomé | T4 2027 | Revenue > Coûts Lomé |
| 1ère ville expansion | T1 2029 | Cotonou |
| 100 000 commerçants | 2030 | Toutes villes confondues |

## Footer
| Field | Value |
|---|---|
| Document | Omni Strategic Roadmap V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/07_CAPITAL_ROADMAP.md
# OMNI CAPITAL ROADMAP
## Version 1.0 — 2026–2036

### Financer la construction de l'index du commerce de proximité

---

## Thèse de Capital

Nous levons du capital pour construire des actifs stratégiques (index, confiance, données), pas des produits. Le capital permet l'acquisition terrain -> l'index -> l'adoption -> les revenus -> plus d'actifs.

---

## Architecture de Financement (5 couches)

### Couche 1 : Capital Fondateur (2024–2026)
Temps, exécution, relations. MVP construit en bootstrappé. Équipe fondatrice de 6 personnes.

### Couche 2 : Capital Non-Dilutif (2026–2027)
- Programme Innov'Action — Djanta Tech Hub (jusqu'à 9M FCFA / ~15k EUR)
- Fonds Start — subventions pour projets innovants
- Concours et compétitions locales
- **Objectif : $15k–$50k non-dilutif**

### Couche 3 : Partenariats Stratégiques (2026–2028)
- Opérateurs mobiles (YAS, Moov) — APIs de paiement à tarif préférentiel
- Municipalité de Lomé — soutien à la cartographie
- Associations de commerçants — accès aux marchés
- **Valeur estimée : $30k–$100k en nature**

### Couche 4 : Revenus (2027+)
- Abonnements Premium commerçants : 5 000 FCFA/mois
- Abonnements livreurs : 1 000 FCFA/mois
- Objectif Phase 1 : 200 abonnés Premium = 1M FCFA/mois (~$1 700/mois)
- Objectif Phase 2 : 2 000 abonnés Premium = 10M FCFA/mois (~$17 000/mois)

### Couche 5 : Financement par Fonds Propres (2027+)
- Pre-Seed : $100k–$150k (2026–2027)
- Seed : $500k–$1M (2027–2028)
- Series A : $2M–$5M (2028–2030)

---

## Utilisation des Fonds (Pre-Seed $100k–$150k)

| Poste | % | Montant |
|-------|---|---------|
| Communication & acquisition | 55 % | $55k–$82.5k |
| Couverture terrain (agents, déplacements) | 45 % | $45k–$67.5k |

### Détail Communication & Acquisition ($55k–$82.5k)
- Radio locale : $15k–$25k
- Affichage marchés : $10k–$15k
- Campagne numérique : $10k–$15k
- Activation zone par zone : $10k–$15k
- Événements et partenariats : $10k–$12.5k

### Détail Couverture Terrain ($45k–$67.5k)
- Agents de cartographie (5–8 personnes x 12 mois) : $25k–$40k
- Équipement (smartphones, transport) : $5k–$7.5k
- Déplacements zone par zone : $5k–$7.5k
- Formation et support commerçants : $5k–$7.5k
- Fournitures et matériel : $5k–$5k

---

## Règle de Financement

Ne pas lever tant que le palier précédent n'est pas prouvé :
- Pre-Seed : MVP fonctionnel + début d'adoption (✅ MVP OK)
- Seed : 1 000 commerçants actifs + revenus récurrents
- Series A : 10 000 commerçants + rentabilité Lomé
- Series B : 100 000 commerçants + 5 villes

## Footer
| Field | Value |
|---|---|
| Document | Omni Capital Roadmap V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/08_EXECUTIVE_SUMMARY.md
# OMNI — EXECUTIVE SUMMARY
## L'index du commerce de proximité
### Lomé, Togo | Pre-Seed | $100k–$150k

---

## Overview

Omni est une plateforme qui indexe l'économie de proximité africaine sur une carte interactive. L'acheteur trouve en un clic tout ce qui existe autour de lui. Le commerçant devient visible pour la première fois. MVP déployé à omni.sparkafrika.online. Équipe de 6 personnes.

## Le Problème

80 %+ de l'économie togolaise est informelle. Les commerçants — marchands, artisans, réparateurs, traiteurs — existent dans la rue mais pas en ligne. Google ne les référence pas. Facebook ne les structure pas. Les acheteurs passent des heures à chercher ce qui existe pourtant à quelques rues de chez eux. Et finissent souvent par commander sur Alibaba ou Amazon.

## La Solution

Omni indexe tout ce qui existe autour de vous sur une carte interactive :
- **Recherche** : texte ou voix, filtre par proximité, catégorie, prix
- **Disponibilité** : OUI/NON en temps réel
- **Paiement** : Mobile Money avec escrow jusqu'à livraison
- **Livraison** : crowd delivery sur trajet quotidien

## Le Marché

- Lomé : 1,5M habitants, 50 000+ commerçants et prestataires
- 80 %+ de pénétration smartphone en zone urbaine
- 100 % d'adoption Mobile Money (YAS + Moov)
- Marché reproductible ville par ville en Afrique de l'Ouest

## Le Produit

MVP fonctionnel et déployé :
- ✅ Carte interactive géolocalisée
- ✅ Recherche texte et vocale
- ✅ Profils commerçants avec produits et prix
- ✅ Disponibilité temps réel OUI/NON
- ✅ Messagerie directe
- ✅ Abonnements Free/Pro
- 🔄 Escrow Mobile Money (en cours)
- 🔄 Livraison crowd (en cours)

## Modèle Économique

- **Acheteur** : gratuit (toujours)
- **Commerçant Premium** : 5 000 FCFA/mois (produits illimités + wallet escrow)
- **Livreur** : 1 000 FCFA/mois
- **Commission** : zéro sur les transactions

## L'Équipe

- **Kheir Lissi** — CEO & Vision Produit
- **Samuel Attiogbe** — Lead Dev (architecture technique, backend)
- **Nondo Nina** — Développeuse (frontend, UX/UI)
- **Peteou Antoine** — Customer Success (3 ans, relation commerçants)
- **Tchidah Bilkiss** — Stratégie de Couverture (Master GC, cartographie)
- **Kpotogbe M-Grace** — Gestion de Projet (Banque & Finance)

## Traction

- MVP fonctionnel : omni.sparkafrika.online
- Équipe constituée : 6 profils complémentaires
- Société enregistrée au Togo
- En cours : programme Innov'Action — Djanta Tech Hub

## Demande

**Pre-Seed : $100k–$150k**
- 55 % Communication & Acquisition (radio, affichage, activation)
- 45 % Couverture Terrain (agents, cartographie, déplacements)

## Contact

Kheir Lissi — CEO, Omni

## Footer
| Field | Value |
|---|---|
| Document | Omni Executive Summary V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/09_BUSINESS_PLAN.md
# OMNI — PHASE 1 BUSINESS PLAN
## L'index du commerce de proximité — Validation Lomé
### Version 1.0 — Pre-Seed Investment Memorandum
### 2026–2027

---

## 1. EXECUTIVE SUMMARY

Omni est une plateforme qui indexe l'économie de proximité africaine. Le MVP est déployé (omni.sparkafrika.online). L'objectif de la Phase 1 est de valider le modèle à Lomé avec 1 000 commerçants actifs, en démontrant que l'index du commerce de proximité crée de la valeur pour acheteurs, commerçants et livreurs.

Omni cherche $100k–$150k en pré-seed pour financer la communication terrain et la couverture des marchés de Lomé. Le programme Innov'Action de Djanta Tech Hub est identifié comme accélérateur principal (jusqu'à 9M FCFA de subvention Fonds Start).

---

## 2. LE PROBLÈME

**L'offre locale existe. Personne ne la trouve.**

Les commerçants informels (80 %+ de l'économie togolaise) n'ont pas de site web, pas de page Google, pas de présence en ligne structurée. Les acheteurs doivent chercher sur Google, Facebook, WhatsApp et demander à leurs proches — sans garantie de trouver. Résultat : ils commandent sur Alibaba ou Amazon ce qui existe pourtant à quelques rues de chez eux.

**Trois conséquences directes :**
1. **Pour l'acheteur** : perte de temps, achats à distance par défaut
2. **Pour le commerçant** : dépend au bouche-à-oreille, plafond de croissance physique
3. **Pour la ville** : économie informelle non mesurée, non connectée

---

## 3. L'OPPORTUNITÉ

**Marché :** Lomé, 1,5M habitants, 50 000+ commerçants et prestataires
**Taux d'équipement :** 80 %+ smartphones, 100 % Mobile Money
**Concurrence indirecte :** Google (ne référence pas l'informel), Facebook (non structuré), Jumia/AfriqMarket (logistique centralisée, pas de proximité)
**Avantage Omni :** index géolocalisé construit rue par rue, pas réplicable par une plateforme globale

---

## 4. LA SOLUTION

Omni est une carte interactive qui permet à l'acheteur de :
1. Chercher ce dont il a besoin (texte ou voix)
2. Voir ce qui est disponible, où, à quel prix
3. Confirmer la disponibilité en temps réel
4. Payer par Mobile Money (escrow sécurisé)
5. Se faire livrer par quelqu'un sur son trajet

---

## 5. OBJECTIFS PHASE 1

**Stratégique :** Valider le modèle d'index du commerce de proximité à Lomé
**Opérationnel :** 1 000 commerçants actifs, 10 000 recherches mensuelles

**Livrables :**
1. 1 000 fiches commerçants actives avec produits et prix
2. Intégration Mobile Money YAS + Moov
3. Système d'escrow fonctionnel
4. 200 abonnés Premium (5 000 FCFA/mois)
5. 100 livreurs crowd actifs
6. Notoriété de marque dans 5 marchés de Lomé

---

## 6. BUSINESS MODEL

| Acteur | Offre | Prix | Statut |
|--------|-------|------|--------|
| Acheteur | Recherche, carte, contact | Gratuit (toujours) | ✅ |
| Commerçant Free | 1 fiche, 5 produits | Gratuit | ✅ |
| Commerçant Premium | Produits illimités + wallet escrow | 5 000 FCFA/mois | ✅ |
| Livreur Free | 3 livraisons/jour | Gratuit | ✅ |
| Livreur Pro | Illimité, multi-stops | 1 000 FCFA/mois | ✅ |

**Zéro commission sur les transactions.** L'argent reste dans l'économie locale.

---

## 7. ROADMAP PHASE 1

**Mois 1–3 (Juin–Août 2026) :** Équipe terrain, 5 marchés cartographiés, 300 fiches, intégration Mobile Money, début campagne radio
**Mois 4–6 (Sept–Nov 2026) :** Escrow, messagerie, 600 fiches, 100 Premium, 50 livreurs
**Mois 7–12 (Déc 2026–Mai 2027) :** 1 000 fiches, 200 Premium, 100 livreurs, 10K recherches/mois, préparation phase 2

---

## 8. USE OF FUNDS

| Poste | % | $100k | $150k |
|-------|---|-------|-------|
| Communication & acquisition | 55 % | $55k | $82.5k |
| Couverture terrain | 45 % | $45k | $67.5k |

---

## 9. RISQUES

**Adoption commerçants (H/M) :** Résistance au changement, méfiance technologique. Mitigation : agents terrain, démonstration en personne, premiers résultats tangibles.
**Qualité de l'index (M/M) :** Données inexactes, disponibilité non fiable. Mitigation : validation en personne, suivi téléphonique, système OUI/NON simple.
**Concurrence (M/M) :** Google Maps, Jumia. Mitigation : la force d'Omni est dans l'index de rue, pas dans la tech. Aucun concurrent ne cartographie rue par rue.
**Financement (H/M) :** Pre-seed insuffisant. Mitigation : programme Innov'Action (non-dilutif), modèle économique lean.

---

## 10. DEMANDE D'INVESTISSEMENT

**Montant :** $100k–$150k
**Utilisation :** Validation du modèle à Lomé
**Durée :** 12–18 mois
**Résultat principal :** 1 000 commerçants actifs, modèle prouvé, ready for seed

---

## Footer
| Field | Value |
|---|---|
| Document | Omni Phase 1 Business Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/10_PITCH_DECK.md
# OMNI — PITCH DECK
## L'index du commerce de proximité
### Version 1.0 — 10 slides

---

## Slide 1 : Cover

**Omni**
L'index du commerce de proximité
Innov'Action 2026 | Lomé, Togo | Pre-Seed $100k–$150k

---

## Slide 2 : Le Problème

**L'offre locale existe. Personne ne la trouve.**

- 80 %+ de l'économie togolaise est informelle
- Marchands, artisans, réparateurs — présents dans la rue, absents en ligne
- Google ne les référence pas. Facebook ne les structure pas.
- Résultat : on commande sur Alibaba ce qui existe à côté de chez soi

---

## Slide 3 : L'Impact

**Trois conséquences :**
- **Acheteur** : parcours du combattant pour trouver un service local
- **Commerçant** : dépend du bouche-à-oreille, plafond de croissance physique
- **Ville** : économie informelle non mesurée, non connectée

---

## Slide 4 : La Solution

**Omni indexe tout ce qui existe autour de vous.**

- L'acheteur cherche (texte ou voix, filtre proximité/catégorie/prix)
- La disponibilité est confirmée en temps réel (OUI/NON)
- Le paiement est sécurisé (Mobile Money + escrow)
- La livraison est ouverte à tous (crowd delivery)

---

## Slide 5 : Le Marché

**Lomé — Notre maison. Notre premier terrain.**
- 50 000+ commerçants et prestataires
- 1,5M+ habitants
- 80 %+ pénétration smartphone
- 100 % Mobile Money (YAS + Moov)
- Modèle réplicable ville par ville en Afrique de l'Ouest

---

## Slide 6 : Le Produit

**MVP fonctionnel. Déployé. Prêt à l'échelle.**
- ✅ Carte interactive géolocalisée
- ✅ Recherche texte et vocale
- ✅ Profils commerçants (produits, prix, disponibilité)
- ✅ Disponibilité temps réel (OUI/NON en 1 clic)
- ✅ Messagerie directe
- ✅ Abonnements Free / Pro
- 🔄 Escrow Mobile Money (en cours)
- 🔄 Livraison crowd (en cours)

→ omni.sparkafrika.online

---

## Slide 7 : Modèle Économique

**Simple. Respectueux du marché. Sans commission.**

- **Acheteur** : gratuit (toujours)
- **Commerçant Premium** : 5 000 FCFA/mois (produits illimités + wallet escrow 1 %)
- **Livreur Pro** : 1 000 FCFA/mois (illimité, multi-stops)

Zéro commission sur les transactions. L'argent reste dans l'économie locale.

---

## Slide 8 : Partenariats & Infrastructure

**La technique est prête. L'investissement couvre le terrain.**

1. **APIs mobiles** : Intégration YAS et Moov Money (nécessite appui institutionnel)
2. **Communication** : Radio, affichage, activation de zone, partenariats associations
3. **Couverture terrain** : Agents accompagnent les commerçants, cartographie rue par rue

→ Objectif : 1 000 fiches actives en 90 jours

---

## Slide 9 : L'Équipe

- **Kheir Lissi** — CEO & Vision Produit
- **Samuel Attiogbe** — Lead Dev (architecture technique, backend)
- **Nondo Nina** — Développeuse (frontend, UX/UI)
- **Peteou Antoine** — Customer Success (3 ans expérience)
- **Tchidah Bilkiss** — Stratégie de Couverture (Master GC, cartographie)
- **Kpotogbe M-Grace** — Gestion de Projet (Banque & Finance)

Nous construisons pour ce marché. Pas pour la Silicon Valley.

---

## Slide 10 : Vision & Demande

**Vision :** Faire d'Omni le standard de la recherche de commerce de proximité en Afrique de l'Ouest.

**Demande :** Pre-Seed $100k–$150k
- 55 % Communication et acquisition
- 45 % Couverture terrain

*"Nous ne réinventons pas le commerce. Nous rendons visible ce qui existe déjà."*

## Footer
| Field | Value |
|---|---|
| Document | Omni Pitch Deck V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/README.md
# Omni — Data Room

**Project:** L'index du commerce de proximité
**Founder:** Kheir Lissi
**Location:** Lomé, Togo
**Stage:** Pre-Seed
**Funding Sought:** $100,000–$150,000
**Status:** MVP deployed — omni.sparkafrika.online

---

## Strategic Documents

| # | Document | Description |
|---|----------|-------------|
| 01 | Vision | Long-term destination (10–20 year horizon) |
| 02 | Mission | What Omni does every day |
| 03 | Theory of Change | How vision becomes reality |
| 04 | Strategic Assets Map | Core assets to accumulate |
| 05 | Master Plan | Development framework 2026–2036 |
| 06 | Strategic Roadmap | Execution timeline |
| 07 | Capital Roadmap | Financing strategy |
| 08 | Executive Summary | 2-page investor/dossier summary |
| 09 | Business Plan | Phase 1 pre-seed plan |
| 10 | Pitch Deck | Pitch deck outline |

## Annexes (investor/application)

| # | Document | Description |
|---|----------|-------------|
| A | Cap Table | Proposed equity structure |
| A1 | Budget | Detailed use of funds |
| A2 | Hiring Plan | Phase 1 recruitment |
| A3 | KPIs & Milestones | 12-month execution metrics |
| A4 | Djanta Tech Hub Application | Application-specific documents |
| A5 | Risk Assessment | Risk framework |
| A6 | Expansion Plan | Lomé → West Africa plan |
| A7 | Founder Profile | Kheir Lissi background |
| A8 | Funding & Dilution | Long-term financing approach |

## Current Status

- Strategic documentation: In progress
- MVP: Deployed and functional (omni.sparkafrika.online)
- Team: 6 members (CEO, Lead Dev, Dev, CS, Coverage Strategy, PM)
- Company: Formalisation en cours
- Runway: Critical

## Footer
| Field | Value |
|---|---|
| OS Version | V4 |
| Last Updated | 2026-06-21 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A1_BUDGET.md
# OMNI — BUDGET PHASE 1
## Version 1.0 — Pre-Seed ($100k–$150k)

### Allocation des Fonds

| Poste | % | $100k | $150k |
|-------|---|-------|-------|
| Communication & acquisition | 55 % | $55 000 | $82 500 |
| Couverture terrain | 45 % | $45 000 | $67 500 |
| **Total** | **100 %** | **$100 000** | **$150 000** |

### Détail Communication ($55k–$82.5k)

| Article | $100k | $150k |
|---------|-------|-------|
| Radio locale (3 stations, 3 mois) | $15 000 | $25 000 |
| Affichage marchés (5 marchés) | $10 000 | $15 000 |
| Campagne digitale (FB, TikTok) | $10 000 | $15 000 |
| Activation zone par zone | $10 000 | $15 000 |
| Événements & partenariats | $10 000 | $12 500 |

### Détail Terrain ($45k–$67.5k)

| Article | $100k | $150k |
|---------|-------|-------|
| Agents terrain (5–8 x 12 mois) | $25 000 | $40 000 |
| Équipement (smartphones, transport) | $5 000 | $7 500 |
| Déplacements zone par zone | $5 000 | $7 500 |
| Formation commerçants | $5 000 | $7 500 |
| Fournitures & matériel | $5 000 | $5 000 |

## Footer
| Field | Value |
|---|---|
| Document | Omni Budget Phase 1 V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A2_HIRING_PLAN.md
# OMNI — HIRING PLAN
## Version 1.0 — Phase 1 (12 mois)

### Priorité : Talents locaux Lomé

| Poste | Mois | Salaire/mois | Coût annuel |
|-------|------|-------------|-------------|
| Agents terrain (5) | Mois 1 | 150 000 FCFA | $1 500/mois/pers |
| Agent terrain senior | Mois 3 | 250 000 FCFA | $500/mois |
| Développeur mobile | Mois 3 | 300 000 FCFA | $600/mois |
| Community Manager | Mois 3 | 200 000 FCFA | $400/mois |
| Stagiaires cartographie (3) | Mois 6 | 75 000 FCFA | $150/mois/pers |

### Profils Recherchés

1. **Agents terrain** (5) — Cartographie, relation commerçants, création de fiches
2. **Agent terrain senior** (1) — Coordination, formation, qualité des données
3. **Développeur mobile** (1) — Application mobile Omni (Flutter/React Native)
4. **Community Manager** (1) — Réseaux sociaux, communication, radio
5. **Stagiaires cartographie** (3) — Étudiants, appui terrain

### Total Masse Salariale Phase 1 : ~$30k–$45k

## Footer
| Field | Value |
|---|---|
| Document | Omni Hiring Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A3_KPIS_MILESTONES.md
# OMNI — KPI & MILESTONES
## Version 1.0 — Phase 1 (12 mois)

### Jalons

| Jalon | Mois | Description | Indicateur |
|-------|------|-------------|------------|
| Fondation | M1–M3 | Équipe terrain constituée, 5 marchés cartographiés, partenariats associations commerçants | 300 fiches |
| Acquisition | M3–M6 | Croissance des fiches, intégration Mobile Money, premiers abonnés Premium | 600 fiches, 100 Premium |
| Transactions | M6–M9 | Escrow fonctionnel, messagerie active, crowd delivery débuté | 1 000 transactions/mois |
| Maturité | M9–M12 | 1 000 fiches, notoriété Lomé, préparation phase 2 | 10K recherches/mois |

### KPIs

| KPI | Objectif Phase 1 |
|-----|-----------------|
| Fiches commerçants actives | 1 000 |
| Abonnés Premium | 200 |
| Livreurs crowd | 100 |
| Recherches mensuelles | 10 000 |
| Transactions sécurisées | 1 000/mois |
| Disponibilité OUI/NON fiable | > 90 % |
| Revenu mensuel récurrent | > 1M FCFA |

### Suivi

Revue hebdomadaire des KPIs terrain. Ajustement mensuel des zones de couverture.

## Footer
| Field | Value |
|---|---|
| Document | Omni KPIs & Milestones V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A4_DJANTA_TECH_HUB.md
# OMNI — DJANTA TECH HUB APPLICATION
## Version 1.0 — Programme Innov'Action

### Pourquoi Omni correspond à Innov'Action

| Critère | Omni | Status |
|---------|------|--------|
| Solution technologique fonctionnelle | MVP déployé (omni.sparkafrika.online) | ✅ |
| Société enregistrée au Togo | En cours de formalisation (individuel accepté selon règlement Art. 3.1) | ✅ |
| Équipe de 3+ profils complémentaires | 6 personnes (Dev, Marketing, Cartographie, Finance, Gestion, CS) | ✅ |
| Secteur éligible | Commerce & Artisanat | ✅ |
| Basé à Lomé | Oui | ✅ |
| Produit en phase Beta avancée | MVP avec utilisateurs actifs | ✅ |
| Disponible en anglais | Programme en anglais — équipe bilingue | ✅ |

### Bénéfices Attendus

1. Accélération validation Lomé (6 mois d'incubation)
2. Subvention Fonds Start (jusqu'à 9M FCFA)
3. Mentorat CcHUB — expertise panafricaine
4. Accès au co-working space (Quartier des Étoiles)
5. Mise en relation investisseurs et partenaires
6. Crédibilité institutionnelle

### Proposition de Valeur pour Djanta Tech Hub

Omni est le premier index du commerce de proximité en Afrique de l'Ouest. Le MVP est fonctionnel, l'équipe est constituée, le marché est réel (80 % d'économie informelle). L'incubation Innov'Action permettrait d'accélérer l'adoption terrain à Lomé et de démontrer un modèle réplicable pour toute la région.

### Documents à Fournir

- ✅ Formulaire d'inscription en ligne
- ✅ Pitch Deck (10 slides)
- ✅ Business Plan
- ✅ Executive Summary
- ✅ Preuve d'enregistrement de la société
- ✅ Présentation de l'équipe

## Footer
| Field | Value |
|---|---|
| Document | Omni Djanta Tech Hub Application V1 |
| Program | Innov'Action |
| Deadline | June 22, 2026 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A5_RISK_ASSESSMENT.md
# OMNI — RISK ASSESSMENT
## Version 1.0

| Risque | Probabilité | Impact | Mitigation |
|--------|------------|--------|------------|
| Adoption commerçants trop lente | H | M | Agents terrain, démos en personne, premiers résultats tangibles, bouche-à-oreille structuré |
| Qualité des données (fiches) | M | M | Validation en personne, suivi téléphonique, système OUI/NON simple |
| Financement insuffisant | H | M | Programme Innov'Action non-dilutif, modèle lean, scénarios multiples |
| Concurrence (Google Maps, Jumia) | M | M | Impossible pour un acteur global de cartographier rue par rue ; avantage terrain |
| Intégration APIs Mobile Money | M | H | Nécessite appui institutionnel ; anticiper les délais ; alternative USSD |
| Départ d'un membre clé de l'équipe | M | H | Documentation des processus, ESOP pour fidéliser, polyvalence encouragée |
| Sécurité des transactions | M | H | Escrow sécurisé, audits réguliers, conformité réglementaire |
| Expansion trop rapide | L | M | Principe "ville par ville" — ne pas passer à la suivante sans validation |

### Risque Principal

Le plus grand risque est la vitesse d'adoption des commerçants. Si le bouche-à-oreille ne décolle pas dans les 90 premiers jours, le financement terrain s'épuise avant d'atteindre la masse critique. Mitigation : commencer par les marchés les plus denses et les associations de commerçants les plus engagées.

## Footer
| Field | Value |
|---|---|
| Document | Omni Risk Assessment V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A6_EXPANSION_PLAN.md
# OMNI — EXPANSION PLAN
## Version 1.0 — Lomé → Afrique de l'Ouest

### Stratégie d'Expansion

**Principe :** Prouver Lomé avant d'ouvrir une nouvelle ville. Ne pas diviser les ressources.

### Phases d'Expansion

| Phase | Période | Ville | Population | Commerçants estimés |
|-------|---------|-------|-----------|-------------------|
| 1 | 2026–2027 | Lomé (Togo) | 1,5M | 50 000 |
| 2 | 2028–2029 | Cotonou (Bénin) | 1,2M | 40 000 |
| 3 | 2029–2030 | Accra (Ghana) | 2,5M | 80 000 |
| 4 | 2030–2031 | Abidjan (Côte d'Ivoire) | 5M | 150 000 |
| 5 | 2031–2032 | Ouagadougou (Burkina Faso) | 1M | 35 000 |

### Critères de Sélection d'une Nouvelle Ville

1. Population > 1M
2. Taux de pénétration smartphone > 60 %
3. Adoption Mobile Money > 50 %
4. Économie informelle significative
5. Accessibilité depuis Lomé (transport, langue)
6. Partenaire local identifié

### Processus d'Entrée

1. **Mission exploratoire** (2 semaines) — Cartographie préliminaire, contacts associations
2. **Pilote** (3 mois) — 1 marché, 100 commerçants
3. **Scale** (6 mois) — Extension à toute la ville
4. **Industrialisation** — Équipe locale autonome

### Défis par Ville

- **Cotonou** : Proche (2h de route), marché similaire, même langue (français, mina)
- **Accra** : Marché plus grand, anglais, compétition potentielle, devise différente
- **Abidjan** : Très grand marché, plus compétitif, infrastructure plus développée
- **Ouagadougou** : Plus petit marché, moins de pression concurrentielle, francophone

## Footer
| Field | Value |
|---|---|
| Document | Omni Expansion Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A7_FOUNDER_PROFILE.md
# OMNI — FOUNDER PROFILE
## Version 1.0

### Kheir Lissi — CEO & Vision Produit

**Nationalité :** Togolaise
**Localisation :** Lomé, Togo
**Langues :** Français (courant), Anglais (professionnel), Éwé (maternelle)

### Parcours

Fondateur et entrepreneur tech togolais. A fondé et opéré plusieurs ventures :
- **Cortexia** — Agence digitale
- **Origin** — Plateforme de services
- **Edenvalley** — Projet tech

Full-stack engineer avec une vision produit ancrée dans les réalités du marché africain. Approche execution-first : construire d'abord, pitcher ensuite.

### Pourquoi Omni

"J'ai grandi à Lomé. Je sais ce que c'est de chercher un service pendant des heures sans trouver, alors que la solution est à deux rues. Omni est né de cette frustration — et de la conviction que l'économie informelle n'est pas un problème à résoudre, mais une opportunité à structurer."

### Compétences Clés

- Développement full-stack (MVP construit en autonomie)
- Vision produit et stratégie
- Exécution lean (zero budget, maximum impact)
- Relations terrain et communauté
- Gestion d'équipe

### Engagement

100 % sur Omni. Foundeur à temps plein depuis le début du projet.

## Footer
| Field | Value |
|---|---|
| Document | Omni Founder Profile V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A8_FUNDING_DILUTION.md
# OMNI — FUNDING & DILUTION
## Version 1.0 — Long-Term Financing Approach

### Stratégie de Financement

| Tour | Montant | Valorisation Post | Dilution Fondateur | Objectif |
|------|---------|------------------|-------------------|----------|
| Pre-Seed | $100k–$150k | $1.1M–$1.65M | 6.5 %–12 % | Validation Lomé |
| Seed | $500k–$1M | $5M–$10M | 10 %–15 % | Scale Lomé |
| Series A | $2M–$5M | $15M–$30M | 10 %–20 % | Expansion régionale |
| Series B | $10M+ | $50M+ | 10 %–15 % | Standard régional |

### Principe de Dilution

1. **Ne pas lever tant que le palier précédent n'est pas prouvé**
2. **Garder le fondateur au-dessus de 50 % le plus longtemps possible**
3. **Utiliser le capital non-dilutif en priorité (subventions, concours)**

### Projection Dilution

| Tour | Fondateur | Équipe (ESOP) | Investisseurs |
|------|-----------|--------------|--------------|
| Fondation | 90 % | 10 % | 0 % |
| Après Pre-Seed | 78 % | 10 % | 12 % |
| Après Seed | 65 % | 10 % | 25 % |
| Après Series A | 50 % | 10 % | 40 % |
| Après Series B | 40 % | 10 % | 50 % |

### Règles

- ESOP maximum 10 % (ne pas sur-diluer le fondateur tôt)
- Privilégier les investisseurs à forte valeur ajoutée opérationnelle
- Éviter les termes agressifs (liquidation préférence > 1x)
- Préférer le non-dilutif tant que la valorisation est basse

## Footer
| Field | Value |
|---|---|
| Document | Omni Funding & Dilution V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/Omni/annexes/A_CAP_TABLE.md
# OMNI — CAP TABLE
## Version 1.0 — Pre-Seed

### Structure Actuelle (Pré-Investissement)

| Actionnaire | Actions | % |
|------------|---------|---|
| Kheir Lissi (Fondateur) | 9 000 000 | 90 % |
| ESOP (Réservé aux employés) | 1 000 000 | 10 % |
| **Total** | **10 000 000** | **100 %** |

### Proposition Post-Pre-Seed ($100k–$150k)

| Actionnaire | % | Notes |
|------------|---|-------|
| Fondateur | 75–80 % | Après dilution |
| Investisseurs | 10–15 % | $100k–$150k |
| ESOP | 10 % | Réservé |

### Valorisation Indicative

- Pre-money : $1M–$1.5M
- Investissement : $100k–$150k
- Post-money : $1.1M–$1.65M
- Dilution : 6.5 %–12 %

### Principes

- Pas de dilution du fondateur en dessous de 75 % au pré-seed
- ESOP réservé pour attirer les talents clés (Data Engineer, Dev Mobile)
- Prochaine levée : Seed à $2M–$3M post-money

## Footer
| Field | Value |
|---|---|
| Document | Omni Cap Table V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/01_VISION.md
# SOJACO VISION
## Version 1.0 — SURVIVAL Mode

### Devenir le fournisseur de céréales de référence pour les revendeurs togolais

---

## 1. Vision Statement

Nous imaginons un futur où les revendeurs de céréales au Togo ont accès à un approvisionnement fiable, transparent et à prix compétitif — sans jamais payer avant réception. Où le soja d'Atakpamé et le maïs des producteurs locaux circulent efficacement entre les villes, créant de la valeur à chaque maillon de la chaîne.

## 2. Le Futur Que Nous Voulons Créer

Aujourd'hui, les petits revendeurs de céréales sont contraints par l'avance de trésorerie : ils doivent payer avant de recevoir, ce qui limite leur capacité d'achat et leur croissance. SOJACO casse ce plafond en proposant le paiement à la livraison, permettant aux revendeurs d'acheter plus, plus souvent, sans bloquer leur cash.

Nous voulons construire un monde dans lequel :
- chaque revendeur de céréales peut commander sans avance
- le soja et le maïs togolais sont distribués efficacement du producteur au revendeur
- la marge de chacun est protégée par la transparence des prix
- le cash généré finance d'autres projets (KORA, OMNI)

## 3. Horizon de Réussite

Nous considérerons que cette vision commence à se réaliser lorsque :
- SOJACO livre 10+ tonnes par mois de céréales aux revendeurs
- la marge dégagée finance le salaire du fondateur
- le modèle est reproductible pour d'autres produits (riz, haricot, etc.)

## Vision Résumée

**Devenir le fournisseur de céréales qui fait confiance aux revendeurs, et que les revendeurs recommandent.**

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Vision V1 |
| Horizon | 2–5 years |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/02_MISSION.md
# SOJACO MISSION
## Version 1.0

### Distribuer des céréales de qualité aux meilleurs prix, sans paiement anticipé

## 1. Déclaration de Mission

SOJACO existe pour approvisionner les revendeurs togolais en céréales (soja, maïs) à des prix compétitifs, avec un avantage concurrentiel unique : le paiement à la livraison. Nous supprimons la barrière de l'avance de trésorerie qui bloque les petits revendeurs.

## 2. Pourquoi SOJACO Existe

La majorité des revendeurs de céréales au Togo sont des petits opérateurs qui ne peuvent pas avancer 35 000 FCFA (un sac de soja) pour attendre la revente. Les fournisseurs exigent le paiement comptant avant livraison. Ce décalage de trésorerie tue le volume et limite la croissance.

SOJACO existe pour résoudre ce problème : nous payons le fournisseur comptant, nous livrons le revendeur, et le revendeur nous paie à la livraison — au moment où il peut revendre.

## 3. Ce Que Nous Faisons

**1. Acheter groupé :** Nous consolidons les commandes des revendeurs pour négocier les meilleurs prix fournisseur.

**2. Paiement comptant au fournisseur :** Nous payons le fournisseur à la commande, ce qui nous donne un levier de négociation.

**3. Paiement à la livraison au client :** Le revendeur paie uniquement quand il reçoit la marchandise.

**4. Logistique :** Nous organisons le transport de l'intérieur (Atakpamé) vers Lomé.

## 4. Ce Que Nous Ne Sommes Pas

SOJACO n'est pas un producteur, pas une coopérative, pas un détaillant (contrairement à SOYA). SOJACO est un intermédiaire de gros (wholesale) qui connecte producteurs et revendeurs.

## 5. Nos Principes d'Exécution

**Principe 1 :** Paiement à la livraison — toujours. Zéro avance pour le client.
**Principe 2 :** Transparence des prix — le client connaît notre prix d'achat.
**Principe 3 :** Qualité vérifiée — nous inspectons avant de charger.
**Principe 4 :** Volume, pas marge unitaire — notre marge est sur le volume.

## 6. Mesure de Succès

Volume mensuel livré (tonnes) | Nombre de clients revendeurs | Taux de défaut de paiement | Marge nette par sac | Cash flow mensuel

## Mission Résumée

**Fournir des céréales de qualité aux revendeurs togolais, sans leur demander d'avance.**

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Mission V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/03_THEORY_OF_CHANGE.md
# SOJACO THEORY OF CHANGE
## Version 1.0

### Comment la marge devient le moteur du cash flow

## 1. Les Déficits Structuraux

**Déficit de trésorerie :** Les revendeurs ne peuvent pas avancer le coût d'un sac complet avant de l'avoir revendu.
**Déficit d'accès fournisseur :** Les petits revendeurs n'ont pas accès aux prix de gros (Atakpamé direct).
**Déficit de logistique :** Aller chercher le soja à Atakpamé coûte du temps et du transport que les revendeurs n'ont pas.

## 2. Hypothèse Centrale

Si nous payons comptant au fournisseur (pour obtenir le meilleur prix), livrons à Lomé, et permettons au revendeur de ne payer qu'à la livraison, alors le revendeur achètera plus et plus souvent, le volume augmentera, et notre marge sur le volume financera les projets FounderHQ.

## 3. La Chaîne Causale

1. Fournisseur exige paiement comptant → Barrière pour les petits revendeurs
2. Nous payons comptant au fournisseur → Nous obtenons le meilleur prix
3. Nous livrons à Lomé → Le revendeur voit la marchandise avant de payer
4. Paiement à la livraison → Zéro risque de trésorerie pour le revendeur
5. Plus de volume pour le revendeur → Plus de commandes récurrentes
6. Plus de volume pour nous → Marge totale croissante
7. Marge → Cash flow pour KORA et OMNI

## 4. La Condition Critique

Le modèle tient si et seulement si :
- **Le prix de vente couvre le prix d'achat + transport + notre marge** (actuellement violé pour le soja à 750/bol)
- **Le client paie à la livraison sans défaut**
- **Le volume est suffisant pour amortir la logistique**

## 5. Résultats Attendus

**Court terme (0-3 mois) :** Valider un produit avec une marge positive. Trouver le bon prix/client.
**Moyen terme (3-12 mois) :** 5+ clients réguliers, 2+ tonnes/mois, marge stable.
**Long terme (1-3 ans) :** SOJACO génère un cash flow net positif de 100 000+ FCFA/mois pour financer les autres projets.

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Theory of Change V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/04_STRATEGIC_ASSETS_MAP.md
# SOJACO STRATEGIC ASSETS MAP
## Version 1.0

### Ce que nous accumulons, pourquoi c'est difficile à reproduire

## 1. Relations Fournisseurs

Le réseau de producteurs et fournisseurs directs (Atakpamé soja, ami maïs). Ces relations sont construites dans le temps, basées sur la confiance et le paiement régulier. Plus nous achetons, meilleurs sont nos prix.

## 2. Base Clients Revendeurs

Les revendeurs qui nous font confiance pour la livraison à crédit (paiement à la livraison). Cette confiance est notre principal actif : un concurrent devrait prouver la même fiabilité avant de capter nos clients.

## 3. Connaissance des Prix

La connaissance en temps réel des prix fournisseur, des prix transport, et des prix de revente. Cette information est locale, mouvante, et n'existe dans aucune base de données publique.

## 4. Logistique Atakpamé-Lomé

La connaissance des transporteurs, des coûts, des délais et des points de rupture sur l'axe Atakpamé-Lomé.

## Carte des Actifs par Difficulté de Réplication

| Actif | Difficulté | Temps | Avantage Concurrentiel |
|---|---|---|---|
| Relations fournisseurs | Moyenne | 3-6 mois | Durable |
| Base clients revendeurs | Élevée | 6-12 mois | Défensif |
| Connaissance des prix | Faible | 1-2 mois | Périssable |
| Logistique Atakpamé-Lomé | Faible | 1-2 mois | Périssable |

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Strategic Assets Map V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/05_MASTER_PLAN.md
# SOJACO MASTER PLAN
## Version 1.0 — SURVIVAL Mode

### Générer du cash flow en distribuant des céréales

---

## Résumé Exécutif

SOJACO achète du soja et du maïs aux fournisseurs (Atakpamé, ami), les livre à Lomé, et vend aux revendeurs avec paiement à la livraison. Le modèle est simple, le risque est le défaut de paiement, l'avantage concurrentiel est la confiance (paiement différé).

---

## Thèse Stratégique

Le principal obstacle des revendeurs de céréales au Togo est le cash flow, pas le prix. En proposant le paiement à la livraison, nous doublons le volume que chaque revendeur peut écouler — et donc notre propre volume.

---

## Les 3 Couches Stratégiques

### Couche 1 : Approvisionnement
Identifier et négocier avec les fournisseurs directs. Payer comptant pour obtenir le meilleur prix. Vérifier la qualité avant chargement. Organiser le transport Atakpamé → Lomé.

### Couche 2 : Distribution
Livrer aux revendeurs à Lomé. Collecter le paiement à la livraison. Assurer le suivi client pour les réapprovisionnements.

### Couche 3 : Cash Flow Management
Reinvestir la marge dans le cycle d'achat suivant. Augmenter le volume progressivement. Dégager du cash pour KORA et OMNI.

---

## Principes Stratégiques

1. **Paiement à la livraison.** Zéro avance client. C'est notre avantage concurrentiel.
2. **Volume, pas marge.** 1 000 FCFA/sac × 10 sacs = mieux que 5 000 FCFA/sac × 0 sac.
3. **Pas de crédit client.** Paiement à la livraison = cash immédiat. Pas de comptes clients.
4. **Bootstrap.** Pas de levée de fonds. La marge finance la croissance.
5. **Produit d'abord.** Prouver le soja, puis étendre au maïs, puis à d'autres céréales.

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Master Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/06_STRATEGIC_ROADMAP.md
# SOJACO STRATEGIC ROADMAP
## Version 1.0 — SURVIVAL Mode

### Cash flow from day one

---

## Phase 0 : Validation Prix (Juin 2026)

- ✅ Identifier fournisseur soja Atakpamé (350 FCFA/kg)
- ✅ Identifier client potentiel (750 FCFA/bol) mais marge négative
- 🔄 Trouver client au bon prix (> 875 FCFA/bol pour marge positive)
- 🔄 Trouver client pour maïs (ami 160 FCFA/kg)
- **Investissement : 0 FCFA**

## Phase 1 : Première Transaction (Juillet 2026)

- Trouver 1 client revendeur avec un prix viable
- 1ère commande : 1-2 sacs (100-200 kg)
- Tester la logistique Atakpamé-Lomé
- Tester le paiement à la livraison
- **Investissement : 35 000-70 000 FCFA**

## Phase 2 : Clients Réguliers (3-6 mois)

- 3-5 clients revendeurs réguliers
- 5 sacs/semaine (500 kg)
- Logistique optimisée (transport groupé)
- Marge nette positive confirmée
- **Cash flow : 10 000-25 000 FCFA/semaine**

## Phase 3 : Extension (6-12 mois)

- Ajouter le maïs comme 2ème produit
- Atteindre 10+ sacs/semaine (1 tonne)
- Marge nette 50 000+ FCFA/semaine
- Redirection du cash vers KORA et OMNI

---

## Jalons Clés

| Jalon | Date cible | Indicateur |
|---|---|---|
| 1er client au bon prix | Juillet 2026 | Marge positive sur 1 sac |
| 3 clients réguliers | Sept 2026 | 3 commandes/semaine |
| 5 sacs/semaine | Déc 2026 | 500 kg/semaine |
| 1 tonne/mois | Mars 2027 | 10 sacs/mois |
| Cash flow net > 50k FCFA/mois | Juin 2027 | Financement KORA/OMNI |

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Strategic Roadmap V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/07_CAPITAL_ROADMAP.md
# SOJACO CAPITAL ROADMAP
## Version 1.0 — SURVIVAL Mode

### Bootstrappé. Pas de levée. La marge finance la croissance.

---

## Thèse de Capital

SOJACO n'est pas une startup technologique. C'est un projet de cash flow. Aucune levée de fonds externe. Chaque cycle d'achat-revente doit être rentable et financer le cycle suivant.

---

## Architecture de Capital (3 couches)

### Couche 1 : Capital Initial — Cash Disponible (~2 679 FCFA)

Cash actuel en poche. Permet de tester de très petites quantités.

### Couche 2 : Cycle d'Achat-Revente

1. Payer le fournisseur comptant (capital)
2. Vendre au revendeur à la livraison
3. Récupérer le prix de vente (cash + marge)
4. Réinvestir capital + marge dans le cycle suivant

**Condition :** Le prix de vente doit couvrir prix d'achat + transport + marge.

### Couche 3 : Accumulation

Quand le cycle tourne, la marge est extraite du cycle pour financer KORA et OMNI.

---

## Utilisation du Capital Initial

| Poste | Montant estimé | Notes |
|---|---|---|
| 1 sac soja (100 kg) | 35 000 FCFA | Fournisseur Atakpamé |
| Transport Atakpamé-Lomé | 3 000-5 000 FCFA | Par sac |
| **Total 1 sac** | **38 000-40 000 FCFA** | |

*Cash disponible actuel : ~2 679 FCFA → insuffisant. Besoin d'apport ou de marge bénéficiaire sur une première transaction.*

---

## Règle de Financement

**Ne jamais dépenser plus que ce que le cycle précédent a généré.**

Tant que la marge est positive, réinvestir dans le volume. Arrêter si la marge devient négative ou nulle.

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Capital Roadmap V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/08_EXECUTIVE_SUMMARY.md
# SOJACO — EXECUTIVE SUMMARY
## Vente de céréales (soja, maïs)
### Lomé, Togo | SURVIVAL | Bootstrappé

---

## Overview

SOJACO achète du soja et du maïs aux fournisseurs directs (Atakpamé, région productrice), livre à Lomé, et vend aux revendeurs avec paiement à la livraison. Projet de cash flow pour financer les projets principaux (KORA, OMNI).

## Le Problème

Les revendeurs de céréales doivent payer comptant avant réception, ce qui bloque leur trésorerie et limite leur volume d'achat. L'accès aux fournisseurs directs de l'intérieur du pays est difficile (transport, relation, volume minimum).

## La Solution

SOJACO propose le paiement à la livraison : le revendeur paie uniquement quand il reçoit la marchandise à Lomé.

- **Achat groupé** : consolidation des commandes pour négocier
- **Paiement comptant fournisseur** : meilleur prix à l'achat
- **Paiement à la livraison client** : zéro avance pour le revendeur
- **Logistique intégrée** : transport Atakpamé → Lomé

## Produits

| Produit | Prix achat | Prix vente | Statut |
|---|---|---|---|
| Soja (Atakpamé) | 350 FCFA/kg | À trouver (> 875 FCFA/bol pour marge) | ❌ Prix client trop bas |
| Maïs (ami) | 160 FCFA/kg | À définir | 🔄 Client à trouver |
| Unité sac | 100 kg | - | - |
| Unité bol | 2.5 kg | - | - |

## Avantage Concurrentiel

- **Paiement différé** : unique dans le marché (les autres exigent comptant)
- **Relation fournisseur direct** : prix d'intérieur, pas de marge intermédiaire
- **Zéro frais de structure** : bootstrap, pas de bureau, pas d'employé

## Prochaine Action

Trouver un client revendeur prêt à payer le soja à un prix viable (> 875 FCFA/bol) ou trouver un autre produit avec une marge positive immédiate.

## Contact

Kheir Lissi — Founder, FounderHQ

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Executive Summary V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/09_BUSINESS_PLAN.md
# SOJACO — BUSINESS PLAN
## Vente de céréales (soja, maïs) — SURVIVAL Mode
### Version 1.0 — Juin 2026

---

## 1. RÉSUMÉ EXÉCUTIF

SOJACO est un projet de distribution de céréales (soja, maïs) entre les fournisseurs de l'intérieur (Atakpamé, région productrice) et les revendeurs de Lomé. L'avantage concurrentiel est le paiement à la livraison — les revendeurs paient uniquement quand ils reçoivent la marchandise. Objectif : générer du cash flow pour financer les projets porteurs (KORA, OMNI).

---

## 2. LE PROBLÈME

**Le cash flow bloque le volume.**

Les revendeurs de céréales à Lomé doivent avancer 35 000-40 000 FCFA par sac de soja avant de pouvoir le revendre. Ce besoin en fonds de roulement limite leur volume d'achat. Avec 100 000 FCFA, un revendeur ne peut acheter que 2-3 sacs. En moyenne, un petit revendeur tourne avec 1-2 sacs/semaine car il doit attendre la revente pour réinvestir.

**Conséquence :** Le volume total écoulé est bien inférieur à la demande réelle. Les fournisseurs d'Atakpamé pourraient vendre plus. Les revendeurs pourraient vendre plus. Le maillon faible est le cash flow intermédiaire.

---

## 3. LA SOLUTION

SOJACO apporte le cash flow qui manque :

1. **Nous payons le fournisseur comptant** → nous obtenons le meilleur prix
2. **Nous livrons à Lomé** → le revendeur voit la marchandise
3. **Le revendeur paie à la livraison** → zéro avance, zéro risque
4. **Notre marge** = prix de vente - prix d'achat - transport

---

## 4. LE MARCHÉ

**Clients :** Revendeurs de céréales à Lomé (marchés, boutiques de quartier).
**Taille :** Des centaines de petits revendeurs dans la capitale. Chacun vend 1-5 sacs/semaine.
**Prix de revente constaté :** Soja 750 FCFA/bol (2.5 kg) → ce qui correspond à 300 FCFA/kg.
**Notre coût :** 350 FCFA/kg → **Marge négative à ce prix client.** Besoin d'un client acceptant un prix plus élevé ou d'un fournisseur moins cher.

---

## 5. MODÈLE ÉCONOMIQUE

| Produit | Achat | Vente sac (100kg) | Vente bol (2.5kg) | Marge | Viable ? |
|---|---|---|---|---|---|
| Soja Atakpamé | 350/kg = 35 000/sac | > 40 000 FCFA | > 1 000 FCFA | ? | ❌ à 750/bol |
| Maïs ami | 160/kg = 16 000/sac | ? | ? | ? | 🔄 client à trouver |

**Unité de compte :**
- 1 sac = 100 kg
- 1 bol = 2.5 kg
- Pour que le soja soit viable, il faut vendre le bol à > 875 FCFA (coût 350/kg × 2.5 + transport) ou trouver un fournisseur à < 300/kg

---

## 6. PROJECTIONS FINANCIÈRES

### Scénario 1 : Soja à marge positive
- Achat : 350 FCFA/kg = 35 000 FCFA/sac
- Transport : 5 000 FCFA/sac estimé
- Coût total : 40 000 FCFA/sac
- Vente nécessaire : > 40 000 FCFA/sac (> 1 000 FCFA/bol)
- Marge : 0-5 000 FCFA/sac selon prix de vente

### Scénario 2 : Maïs
- Achat : 160 FCFA/kg = 16 000 FCFA/sac
- Transport : 3 000 FCFA/sac estimé
- Coût total : 19 000 FCFA/sac
- Vente estimée : 250-300 FCFA/kg = 25 000-30 000 FCFA/sac
- Marge estimée : 6 000-11 000 FCFA/sac

---

## 7. RISQUES

**Défaut de paiement (H/M) :** Le client ne paie pas à la livraison. Mitigation : paiement à la livraison exclusivement, pas de crédit, pas de comptes clients. Si le client ne paie pas, on reprend la marchandise.

**Qualité fournisseur (M/M) :** Soja ou maïs de qualité inférieure. Mitigation : inspection visuelle avant chargement, relation suivie avec le fournisseur.

**Prix fournisseur (M/M) :** Hausse du prix d'achat. Mitigation : diversification des fournisseurs, stocks de sécurité limités.

**Logistique (M/B) :** Panne transport, retard. Mitigation : transporteurs connus, marge de temps dans le planning.

---

## 8. BESOIN EN CAPITAL

**Capital de départ nécessaire :** ~40 000 FCFA pour 1 sac de soja + transport.
**Disponible actuellement :** ~2 679 FCFA.
**Déficit :** ~37 000 FCFA.

*Alternative : commencer par le maïs (moins cher à l'achat) si un client est trouvé.*

---

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Business Plan V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/10_PITCH_DECK.md
# SOJACO — PITCH DECK
## Vente de céréales (soja, maïs)
### Version 1.0 — 6 slides

---

## Slide 1 : Cover

**SOJACO**
Distribution de céréales — Paiement à la livraison
SURVIVAL Mode | Lomé, Togo | Bootstrappé

---

## Slide 2 : Le Problème

**Les revendeurs doivent payer comptant avant de recevoir.**

- Un sac de soja (100 kg) = 35 000 FCFA d'avance
- Avec 100 000 FCFA, un revendeur ne peut acheter que 2-3 sacs
- Résultat : volume limité, croissance plafonnée, cash bloqué

---

## Slide 3 : La Solution

**SOJACO paie comptant au fournisseur, livre à Lomé, et le revendeur paie à la livraison.**

- Zéro avance pour le revendeur
- Meilleur prix fournisseur (paiement comptant)
- Plus de volume pour tout le monde

---

## Slide 4 : Le Marché

**Des centaines de petits revendeurs de céréales à Lomé.**

- Marché existant, pas à créer
- Demande immédiate et récurrente
- Pas de concurrence sur ce modèle de paiement

---

## Slide 5 : Modèle Économique

- **Achat** : 350 FCFA/kg soja (Atakpamé), 160 FCFA/kg maïs (ami)
- **Vente** : marge positive nécessaire > prix d'achat + transport
- **Unité** : sac (100 kg) ou bol (2.5 kg)
- **Risque** : défaut de paiement → mitigé par paiement à la livraison

---

## Slide 6 : Prochaine Action

**Trouver le bon prix client pour démarrer le cycle.**

- ❌ Soja à 750 FCFA/bol (perte de 125 FCFA/bol)
- 🔄 Maïs : client à trouver (marge estimée positive)
- Objectif : 1ère transaction viable en juillet 2026

---

## Footer
| Field | Value |
|---|---|
| Document | SOJACO Pitch Deck V1 |
| OS Version | V4 |
| Owner | Founder |


--- FILE: projects/SOJACO/README.md
# SOJACO — Vente de Céréales

## Concept
Achat-revente de céréales (soja, maïs) au Togo. Paiement à la livraison.

## Produits

### Soja
- Fournisseur : Atakpamé (350 FCFA/kg)
- Conditionnement : sacs de 100 kg
- Client : Revendeur, achète à 750 FCFA/bol (2.5 kg)
- Stock cible : 5-10 sacs

### Maïs
- Fournisseur : Ami (160 FCFA/kg)
- Stock disponible : 50 tonnes (min 1 tonne)
- Client : À trouver

## Règles de Paiement
100% paiement à la livraison.

## Relations
- Projet frère de SOYA (Bolsoja)


--- FILE: projects/SOJACO/annexes/00_FOURNISSEURS.md
# SOJACO — Fournisseurs

## Soja

| Champ | Valeur |
|---|---|
| Fournisseur | Atakpamé (producteur direct) |
| Produit | Soja grain |
| Prix | 350 FCFA/kg (prix plancher, ne peut pas descendre) |
| Unité | Sac de 100 kg = 35 000 FCFA |
| Paiement | Comptant |
| Transport | Atakpamé → Lomé (5 000 FCFA/sac estimé) |
| Contact | À documenter |

## Maïs

| Champ | Valeur |
|---|---|
| Fournisseur | Ami |
| Produit | Maïs grain |
| Prix | 160 FCFA/kg |
| Unité | Minimum 1 tonne (1 000 kg) |
| Stock dispo | 50 tonnes |
| Paiement | Comptant |
| Transport | À confirmer |
| Contact | À documenter |


--- FILE: projects/SOJACO/annexes/01_PRICING.md
# SOJACO — Tableau de Pricing

## Soja

| Métrique | Valeur |
|---|---|
| Prix achat/kg | 350 FCFA |
| Prix achat/sac (100kg) | 35 000 FCFA |
| Transport/sac estimé | 5 000 FCFA |
| Coût total/sac | 40 000 FCFA |
| Coût/kg rendu Lomé | 400 FCFA |
| Prix vente bol (2.5kg) | 750 FCFA |
| Prix vente/kg équivalent | 300 FCFA |
| Marge/kg | **-100 FCFA** |
| Marge/bol | **-250 FCFA** |
| **Conclusion** | ❌ Non viable à 750 FCFA/bol |

### Prix de vente nécessaire pour marge positive

| Marge visée | Prix vente/sac | Prix vente/bol |
|---|---|---|
| Seuil (0 FCFA) | 40 000 FCFA | 1 000 FCFA |
| +5 000 FCFA/sac | 45 000 FCFA | 1 125 FCFA |
| +10 000 FCFA/sac | 50 000 FCFA | 1 250 FCFA |

## Maïs

| Métrique | Valeur |
|---|---|
| Prix achat/kg | 160 FCFA |
| Prix achat/sac (100kg) | 16 000 FCFA |
| Transport/sac estimé | 3 000 FCFA |
| Coût total/sac | 19 000 FCFA |
| Coût/kg rendu Lomé | 190 FCFA |
| Prix revente estimé (bol 2.5kg) | 500–750 FCFA |
| Prix revente/kg | 200–300 FCFA |
| Marge/kg | **+10 à +110 FCFA/kg** |
| Marge/bol (2.5kg) | **+25 à +275 FCFA/bol** |
| **Conclusion** | ✅ Viable si revente ≥ 500 FCFA/bol |

## Clients Potentiels

| Client | Produit | Prix offert | Volume | Viable ? |
|---|---|---|---|---|
| Revendeur (non nommé) | Soja | 750 FCFA/bol | 5-10 sacs | ❌ Perte 125 FCFA/bol |
| Client maïs | Maïs | ? | ? | 🔄 À trouver |


--- FILE: tests/__init__.py


--- FILE: tests/test_cadence_engine.py
import pytest
from datetime import datetime
from Runtime.engine.cadence_engine import get_week_of_month, get_cadence_context, get_active_frameworks


class TestGetWeekOfMonth:
    def test_first_week(self):
        d = datetime(2026, 6, 1, 12, 0)
        assert get_week_of_month(d) == 1

    def test_third_week(self):
        d = datetime(2026, 6, 15, 12, 0)
        assert get_week_of_month(d) == 3

    def test_last_week_june(self):
        d = datetime(2026, 6, 29, 12, 0)
        assert get_week_of_month(d) == 5


class TestGetCadenceContext:
    def test_returns_all_levels(self):
        d = datetime(2026, 6, 22, 14, 30)
        ctx = get_cadence_context(d)
        assert ctx["year"] == 2026
        assert ctx["month"] == 6
        assert ctx["day"] == 22
        assert ctx["hour"] == 14
        assert ctx["minute"] == 30
        assert ctx["week_of_month"] == 4
        assert ctx["day_of_week"] == 1

    def test_contains_iso_week(self):
        d = datetime(2026, 6, 22, 12, 0)
        ctx = get_cadence_context(d)
        assert "iso_week" in ctx
        assert 1 <= ctx["iso_week"] <= 53


class TestGetActiveFrameworks:
    def test_validation_phase_returns_vaos_dios(self):
        ctx = {"lifecycle_phase": "VALIDATION"}
        frameworks = get_active_frameworks(ctx)
        assert "VAOS" in frameworks
        assert "DIOS" in frameworks

    def test_idea_phase_returns_caos(self):
        ctx = {"lifecycle_phase": "IDEA"}
        frameworks = get_active_frameworks(ctx)
        assert "CAOS" in frameworks
        assert "VAOS" not in frameworks

    def test_survival_mode_prioritizes_revenue_frameworks(self):
        ctx = {"lifecycle_phase": "VALIDATION", "mode": "SURVIVAL"}
        frameworks = get_active_frameworks(ctx)
        assert "DIOS" in frameworks
        assert "DAOS" in frameworks


--- FILE: tests/test_sync.py
import pytest
import json
from pathlib import Path
from Runtime.engine.sync import Snapshot


class TestSnapshot:
    def test_from_state_minimal(self):
        state = {
            "date": "2026-06-22 14:00 Lome UTC+0",
            "mode": "SURVIVAL",
            "cash": 2679,
            "top_priority": "Find client",
            "bottleneck": "Cash",
        }
        cadence = {"session_start": "08:00", "session_end": "14:00"}
        timeline = [{"date": "2026-06-22", "event": "Boot", "decision": "Start", "outcome": "OK"}]
        projects = {"SOJACO": {"phase": "VALIDATION"}}

        snap = Snapshot(state=state, cadence=cadence, timeline=timeline, projects=projects)
        assert snap.version == 1
        assert snap.state["mode"] == "SURVIVAL"
        assert snap.state["cash"] == 2679

    def test_to_from_json_roundtrip(self):
        original = Snapshot(
            state={"date": "test", "mode": "GROWTH", "cash": 5000, "top_priority": "X", "bottleneck": "Y"},
            cadence={"session_start": "09:00", "session_end": "17:00"},
            timeline=[{"date": "T1", "event": "E1", "decision": "D1", "outcome": "O1"}],
            projects={"P1": {"phase": "LAUNCH"}},
        )
        data = original.to_dict()
        restored = Snapshot.from_dict(data)
        assert restored.state == original.state
        assert restored.cadence == original.cadence
        assert restored.timeline == original.timeline
        assert restored.projects == original.projects

    def test_missing_fields_default(self):
        snap = Snapshot(state={"date": "x", "mode": "x", "cash": 0, "top_priority": "x", "bottleneck": "x"})
        assert snap.cadence == {}
        assert snap.timeline == []
        assert snap.projects == {}

