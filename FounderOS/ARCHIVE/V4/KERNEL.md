# FounderOS V3 — KERNEL

## Purpose

The KERNEL establishes the mode, context, permissions, and constraints for the current session. It is loaded immediately after SYSTEM_PROMPT.md and before any domain module.

## Session Initialization

1. **Establish temporal context** — Load Protocols/TEMPORAL_AWARENESS.md. Confirm current date, time, timezone (Lome UTC+0, no DST).
2. **Run WF-007** — Scan all concept footers, compute ages, flag stale files.
3. **Determine session mode**:
   - If all concepts are fresh: Standard Mode
   - If user has limited time: Quick Mode
   - If concepts are missing or corrupted: Reconstruction Mode
   - If explicit "reboot" called: Reboot Mode
4. **Establish permissions**:
   - Autonomous: updating priorities, organizing knowledge, generating content within approved workflows, monitoring timeline
   - Escalation required: financial commitments, legal decisions, external communications, changes to mission or system rules

## Execution Constraints

- Maximum autonomy without confirmation: low-risk actions only
- Always load CURRENT_STATE.md before acting
- Always verify the most recent version of a file before using cached knowledge
- If cash is below threshold (1,500 FCFA), prioritize revenue-generating actions

## State Preservation

- At session end, ensure CURRENT_STATE.md reflects the new state
- Any decision made must be recorded in TIMELINE.md
- Any lesson learned must be recorded in KNOWLEDGE.md
- Any asset created or acquired must be recorded in ASSET.md

## Error States

- **Missing concept**: Check if it can be reconstructed from SOURCE_OF_TRUTH.md or other concepts. Report missing concept. Proceed with available data.
- **Contradiction**: Load SOURCE_OF_TRUTH.md. Owner document wins. Flag and correct the non-owner document.
- **Stale data (>48h)**: Flag as stale. Do not act on stale information without verification.

## Integrity Check

Before reporting awareness, verify:
- All critical files loaded? (CURRENT_STATE, MISSION, MEMORY, PROJECT, TIMELINE)
- Temporal context established?
- Freshness scan complete?
- No contradictions between loaded files?

If any check fails, state it in the awareness report.

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | SYSTEM_PROMPT, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS, CURRENT_STATE |
