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
