# INC-001: FHQ_MODE Protocol Not Executed

**Severity:** Critical
**Date:** 2026-06-22
**Status:** Open

## Description

The FHQ_MODE protocol (defined in SYSTEM_PROMPT.md and opencode.json) was not being executed when the user typed `fhq`. Instead of executing Get-Date, tracking session time, and running the full kernel cycle (BOOT→OBSERVE→ORIENT→DECIDE→ACT→LEARN→UPDATE), the LLM responded as if `fhq` was natural language.

## Root Cause

The `opencode.json` file specifies:

```json
{
  "instructions": ["SYSTEM_PROMPT.md", "Runtime/FRE_SPEC.md"],
  "customInstructions": [...]
}
```

However, the referenced files were NOT loaded into the LLM's context at session start. The system prompt provided by OpenCode did not include:
- The contents of SYSTEM_PROMPT.md (which defines FHQ_MODE, PRG, Get-Date requirements)
- The contents of FRE_SPEC.md (runtime contracts)
- The customInstructions from opencode.json

Without these instructions visible to the LLM, protocol execution was impossible.

## Evidence

- 6+ user messages using `fhq` prefix without any FHQ_MODE execution
- CADENCE.md "Last fhq" stuck at 21:25 (before INC-001 was filed)
- No Get-Date output before responses
- No kernel cycle execution

## Fix Applied

1. SYSTEM_PROMPT.md loaded manually and protocol now followed
2. CADENCE.md updated (Last fhq → 22:55)

## Permanent Fix Required

1. **Diagnose why opencode.json instructions are not being loaded** — check OpenCode CLI behavior, file paths, config schema
2. **Alternative:** Add the content of SYSTEM_PROMPT.md directly into opencode.json as customInstructions (inline) to bypass the loading issue
3. **Fallback:** Create a symlink or copy SYSTEM_PROMPT.md content to a location that OpenCode loads reliably

## Owner

System

## Lessons

- Never assume config files are loaded — verify by checking what rules are visible
- Protocol files should be self-summarizing; add a "loaded" marker or hash to confirm
- Consider inline instructions in opencode.json customInstructions as belt-and-suspenders
