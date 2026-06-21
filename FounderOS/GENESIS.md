# FounderOS V4 — GENESIS

## Purpose

GENESIS is the first-time setup procedure. It is executed only once — the first time FounderOS is deployed in a new environment.

## Prerequisites

- A blank or existing FounderHQ directory
- An LLM capable of reading and writing files
- Git (optional but recommended)

## Genesis Procedure

### Step 1: Create Directory Structure

```
FounderHQ/
├── FounderOS/
│   ├── SYSTEM_PROMPT.md
│   ├── KERNEL.md
│   ├── RUNTIME.md
│   ├── MOS.md
│   ├── DAOS.md
│   ├── VEAOS.md
│   ├── CEOS.md
│   ├── ASTRA.md
│   ├── KMOS.md
│   ├── LEOS.md
│   ├── RIOS.md
│   ├── FAOS.md
│   ├── SOS.md
│   ├── AOS.md
│   ├── DECISION_ENGINE.md
│   ├── PATTERN_ENGINE.md
│   ├── PLAYBOOK_ENGINE.md
│   ├── KNOWLEDGE_EVOLUTION_ENGINE.md
│   ├── CONTINUOUS_IMPROVEMENT.md
│   ├── AI_VIDEO_MASTER_DOMAIN.md
│   ├── GENESIS.md
│   ├── INSTALL.md
│   ├── concepts/
│   ├── Protocols/
│   ├── Frameworks/
│   ├── State/
│   └── Runtime/
```

### Step 2: Load SYSTEM_PROMPT.md

The LLM reads SYSTEM_PROMPT.md. This is the entry point for all sessions.

### Step 3: Execute Boot Sequence

1. Run WF-007 freshness check
2. Determine session mode
3. Build world model

### Step 4: Load Concepts

- Load all concept files from concepts/
- Verify against SOURCE_OF_TRUTH.md
- Check for contradictions

### Step 5: First Action

- Read FOUNDERHQ_MANIFEST.md for the venture context
- Determine the first mission-critical action
- Execute it

### Step 6: Initialize Git (if available)

```bash
git init
git add -A
git commit -m "genesis: FounderOS V3 initialized"
```

## Verification

After Genesis:
- [ ] All 22+ OS files exist in FounderOS/
- [ ] All concept files exist in concepts/
- [ ] SYSTEM_PROMPT.md loads without errors
- [ ] Protocols/SOURCE_OF_TRUTH.md has entries for all files
- [ ] State/CURRENT_STATE.md reflects current reality
- [ ] Git repository initialized and committed

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | INSTALL.md, SYSTEM_PROMPT.md |
