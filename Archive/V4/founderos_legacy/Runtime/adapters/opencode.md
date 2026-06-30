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
