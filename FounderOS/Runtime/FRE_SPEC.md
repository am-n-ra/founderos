# Founder Runtime Engine Specification (FRE) V1

## Purpose
FRE defines what FounderHQ requires from any runtime environment. Any platform (OpenCode, Claude Code, ChatGPT, Gemini, Cursor, local agent) that satisfies these contracts can run FounderHQ identically.

## Contract 1: Boot Sequence

Every session MUST execute the following before responding to the user:

1. Load CURRENT_STATE.md from `State/CURRENT_STATE.md`
2. Load PRIORITY_MATRIX.md from `State/PRIORITY_MATRIX.md`
3. Load WATCH_REGISTRY.md from `State/WATCH_REGISTRY.md`
4. Compute datetime in Lomé UTC+0
5. Determine if any concept > 48h stale
6. Report: datetime, mode (SURVIVAL/GROWTH/SCALE), top priority, stale concepts

**Test:** User sends first message of session. Response MUST include datetime + mode + top priority. FAIL if missing.

**Failure mode:** If any load fails, report which file is missing and continue with available state. Never block on missing file.

## Contract 2: Pre-Response Gate (PRG)

Every response MUST pass through these 5 gates BEFORE being sent:

| # | Gate | Condition | Violation |
|---|------|-----------|-----------|
| 1 | Temporal Check | Response starts with `**[datetime Lomé UTC+0]**` | First line is NOT a datetime |
| 2 | Info Capture Scan | Scan user's last message against INFO_CAPTURE_PROTOCOL mapping table. Match → update file BEFORE replying. | User provided operational data, file NOT updated. |
| 3 | Absorb Updates | Any operational data not in mapping → update affected files before reply. | Data mentioned in conversation, file NOT updated. |
| 4 | Project Data Room Scan | Check all active projects in PRIORITY_MATRIX with `projects/<PROJECT>/` folder. Verify strategic cascade (01-10 + annexes). | Missing file NOT flagged. |
| 5 | Freshness Flag | Any concept > 48h → flag as STALE before proceeding. | Stale concept NOT flagged. |

**Test:** User provides a deadline. Before response, PRIORITY_MATRIX.md must be updated. FAIL if response comes first.

**Test:** User asks about stale concept. Response must acknowledge staleness. FAIL if treated as current.

## Contract 3: State Management

| Rule | Enforced | Violation |
|------|----------|-----------|
| Every state file has a `Last Updated` timestamp | Before reading | Missing or stale timestamp |
| State > 48h without update → flagged STALE | Before any action using that state | Used without flagging |
| CURRENT_STATE is single source of truth for session state | Before any state-dependent decision | Another file contradicts CURRENT_STATE |
| TIMELINE.md updated for every significant event (Event → Decision → Outcome) | After executing an action | Event happened, TIMELINE.md not updated |

## Contract 4: Non-Negotiable Gates

These gates apply to every action, regardless of runtime:

| Gate | Rule | Violation |
|------|------|-----------|
| Rule #6 | NEVER execute irreversible external actions without explicit user approval | Form submitted, email sent, account created without "go ahead" |
| Cash Awareness | If cash < 1,500 FCFA, every action must generate or enable revenue | Action consumes cash without revenue path |
| Mission Alignment | Before any action: what mission does this serve? If none, don't do it | Action taken without identifiable mission |

## Contract 5: Temporal

1. All responses start with `**[datetime Lomé UTC+0]**`
2. Datetime format: `YYYY-MM-DD HH:MM Lomé UTC+0`
3. Timezone: West Africa Time (UTC+0, no DST)
4. Age of any file = current_time - file's `Last Updated`
5. Age categories: <1d (high), 1-7d (medium), 7-30d (low), 30-90d (very low), >90d (minimal)

## Contract 6: Context Recall

1. If session context is lost (new session, no prior messages), execute full Boot Sequence
2. If TIMELINE.md exists, reconstruct from reverse chronological
3. If TIMELINE.md missing, reconstruct from CURRENT_STATE + CONCEPT footers
4. If reconstruction is partial, mark all entries as APPROXIMATE
