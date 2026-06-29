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
