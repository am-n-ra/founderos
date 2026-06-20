# FounderOS V3 — INSTALL

## Purpose

INSTALL is the deployment guide for setting up FounderOS in a new environment (new machine, new LLM, new IDE).

## Requirements

- Any LLM that supports reading and writing files (ChatGPT, Claude, Gemini, DeepSeek, local models)
- Any IDE or file system that supports markdown files
- Git (optional — for version tracking and reboot delta detection)
- Operating System: Windows, macOS, Linux (any)

## Installation Steps

### 1. Clone or Copy FounderHQ

```bash
git clone <repository> FounderHQ
# OR
# Copy the FounderHQ directory manually
```

### 2. Verify Directory Structure

Ensure all OS files exist under FounderOS/. If any are missing, run GENESIS to recreate them.

### 3. Set Up Protocols

Protocols/FOUNDEROS_PROTOCOL.md is the boot sequence. It must be loadable on first read. Ensure:
- All Protocol files exist
- SOURCE_OF_TRUTH.md has entries for all files
- DECISION_GATES.md references the correct frameworks

### 4. Configure State

State/CURRENT_STATE.md must be updated with:
- Current date
- Cash position
- Current bottleneck
- Current priority
- Session objective

### 5. First Boot

Open a new session with the LLM. Provide SYSTEM_PROMPT.md as context or instruct the LLM to read it. The LLM will then:
1. Read SYSTEM_PROMPT.md
2. Execute KERNEL boot
3. Load all concepts
4. Report awareness

### 6. Verify Installation

The LLM should:
- Report the correct date and time
- Identify all loaded files
- State the current top priority
- Recommend a next action

## Troubleshooting

| Problem | Solution |
|---------|----------|
| LLM cannot find files | Check file paths in SYSTEM_PROMPT.md. Use absolute paths if needed. |
| Contradictions on first boot | Load SOURCE_OF_TRUTH.md. Resolve conflicts manually. |
| Freshness errors on first boot | Update concept footers. WF-007 threshold is 48h by default. |
| Git not found | Reboot system will work without git but with reduced delta detection. |
| LLM ignores protocol | Re-state SYSTEM_PROMPT.md. Emphasize "you are not an assistant." |

## Model Compatibility

FounderOS has been tested with:
- Claude (Opus, Sonnet)
- ChatGPT (GPT-4, GPT-4o)
- DeepSeek
- Gemini

It should work with any model that can:
- Read and write files
- Follow multi-step procedures
- Maintain context across file operations

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | GENESIS.md, FOUNDEROS_PROTOCOL.md |
