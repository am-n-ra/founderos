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
