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
