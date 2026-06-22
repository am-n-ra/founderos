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
