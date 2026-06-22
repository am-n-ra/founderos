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
