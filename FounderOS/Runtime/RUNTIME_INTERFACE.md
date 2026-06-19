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
