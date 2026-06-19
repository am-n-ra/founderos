# Design Philosophy

FounderOS is designed to function as a self-contained, file-based operating system for an AI agent. It must be:

1. **Self-Contained** — Everything the AI needs is in the files. No external databases, no additional services.

2. **Human-Readable** — Files are Markdown. The founder can read, edit, and understand every part of the system.

3. **Stateful** — The system maintains awareness across sessions. STATE/ tracks current reality. MEMORY/ tracks short-term context. Knowledge/ stores permanent learning.

4. **Event-Driven** — The system reacts to changes via monitors, scheduled operations, and event triggers (as implemented by the runtime environment).

5. **Minimal & Sufficient** — Every file exists because it serves a purpose. No redundant documentation.

## Core Insight
An LLM cannot be forced to follow rules. It can only be prompted. Therefore, the system must:
- Make the right action the easiest action
- Make critical information impossible to miss (at the top, short, frequent)
- Accept that enforcement is soft — and design around it

## System > Rules
Rather than 400 lines of rules the LLM will never read, the system uses:
- A short (<50 lines) SYSTEM_PROMPT as identity + boot command
- Reference files organized by purpose (STATE/MEMORY/Knowledge/SYSTEM)
- A clear hierarchy: MEMORY (temporary) → STATE (current facts) → Knowledge (permanent lessons) → SYSTEM (architecture)
