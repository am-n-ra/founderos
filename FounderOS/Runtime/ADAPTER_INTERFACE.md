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
