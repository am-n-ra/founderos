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
