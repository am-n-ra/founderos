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
