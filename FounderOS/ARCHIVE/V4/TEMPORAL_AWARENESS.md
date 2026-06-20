# TEMPORAL AWARENESS PROTOCOL

## Authority

This document defines how FounderHQ perceives and operates with time.

Time is a first-class operational dimension.

Reality is not static.

Reality is state evolving through time.

FounderHQ must understand:

- When things happened
- How long ago they happened
- In what sequence they happened
- What that implies for current reality

---

## Prime Directive

Before responding to any user message or executing any action:

Query the system clock (e.g., `Get-Date` on Windows, `date` on Unix).

Determine the current date and time — not just the date.

Verify the timezone — do NOT assume it matches the user's timezone. Use `(Get-TimeZone).Id` and `[System.TimeZoneInfo]::Local.GetUtcOffset((Get-Date))` to detect actual timezone offset. Do NOT use `(Get-TimeZone).BaseUtcOffset` — it ignores Daylight Saving Time.

Check if DST is active: `(Get-TimeZone).SupportsDaylightSavingTime`. If true, the effective offset may differ from BaseUtcOffset.

Convert to Lomé time (UTC+0) by adding/subtracting the effective UTC offset.

Compare against known states.

Evaluate temporal changes.

**Do not skip the system clock query. The LLM's internal knowledge of "today's date" is not sufficient — you need the current time of day and the correct timezone.**

---

## Required Awareness

Every operational session must establish:

CURRENT_DATETIME

CURRENT_TIMEZONE

ELAPSED_SINCE_LAST_SESSION

ELAPSED_SINCE_LAST_PROJECT_UPDATE

ELAPSED_SINCE_LAST_DECISION

AGE_OF_MEMORY

AGE_OF_KNOWLEDGE

AGE_OF_TIMELINE

---

## State Aging

Every piece of information within FounderHQ has an age.

Age is measured from the last update time to the current time.

Age categories:

| Age | Confidence | Action |
|-----|-----------|--------|
| < 1 day | High | Use as is |
| 1-7 days | Medium | Flag if critical |
| 7-30 days | Low | Verify before use |
| 30-90 days | Very low | Reconstruct if possible |
| > 90 days | Minimal | Treat as historical reference only |

A state without a timestamp is treated as maximally stale.

Stale states must be flagged before use.

---

## Staleness Detection

Staleness must be detected and surfaced, not silently carried forward.

Examples of staleness events:

- PROJECT not updated for 45 days → flag as possibly abandoned
- MEMORY not reviewed for 14 days → flag as potentially inaccurate
- MISSION not reviewed for 90 days → flag as potentially obsolete
- DECISION without follow-up for 30 days → flag for review
- KNOWLEDGE entry older than 1 year without revalidation → flag as unvalidated

A flagged state may still be correct.

But it must be presented to the user with its staleness visible.

---

## Temporal Questions

Before major recommendations, evaluate:

What changed since the last known state?

What has aged beyond reliable use?

What may be obsolete?

What requires review before action?

What new information has emerged since the last session?

---

## Timeline Operations

### Recording

Every significant event must be recorded in TIMELINE with:

- Date
- Description of what happened
- Which concept(s) were affected
- Who or what caused the event

Significant events include:

- Decisions made
- Projects started, advanced, completed, or paused
- Missions updated
- Knowledge added or corrected
- Lessons learned
- External events affecting operations

### Reading

When loading FounderHQ, the TIMELINE should be scanned in reverse chronological order.

The most recent events provide the current context.

Events older than 90 days may be summarized rather than read in full.

### Reconstruction

If TIMELINE is missing but other concepts exist:

1. Scan PROJECT and MEMORY for date-related information
2. Scan KNOWLEDGE for dated lessons or patterns
3. Reconstruct a partial timeline from available evidence
4. Mark all reconstructed entries as approximate

---

## Session Awareness

Every session has a temporal context:

### Beginning of Session

- Record session start time
- Record elapsed time since last session
- Load TIMELINE entries since last session

### During Session

- Track significant events as they occur
- Update affected concept timestamps
- Note elapsed time for ongoing work

### End of Session

- Record session end time
- Summarize what changed during this session
- Update TIMELINE with session summary

---

## Period Awareness

FounderHQ should understand where it is within operational periods:

TODAY

THIS_WEEK

THIS_MONTH

THIS_QUARTER

THIS_YEAR

Each period boundary should trigger:

- Review of goals for that period
- Assessment of progress
- Decision to continue, adjust, or abandon

---

## Temporal Reports

When requested or when conditions are met, generate:

**STALE_STATE_REPORT**
Lists all concepts and entries that exceed their recommended age thresholds.

**ACTIVITY_REPORT**
Summarizes changes over a specified period.

**TIMELINE_SUMMARY**
Condensed history of significant events over a specified period.

**AGING_KNOWLEDGE_REPORT**
Knowledge entries that have not been revalidated within a configurable period.

---

## Temporal Consistency Rules

1. Never treat old information as current without verification
2. Never present a stale state as if it were fresh
3. Never make a time-sensitive recommendation without checking the current time
4. Never assume a previous session's context applies to the current session
5. Always state the date of information when its age is relevant
6. Always flag when a decision or priority is older than its expected lifespan

---

## Edge Cases

### No Clock Available

If the runtime does not provide access to current date/time:

- State explicitly that time is unknown
- Estimate from available evidence (file modification dates, timeline entries)
- Mark all time-dependent conclusions as approximate

### Time Zone Changes

If the user's time zone changes:

- Record the new time zone
- Normalize all stored times to a single reference (UTC)
- Display times in the user's current time zone

### Gap In Timeline

If there is an unexplained gap in the timeline:

- Note the gap period
- Check other concepts for events during the gap
- If no events found, mark the gap as unknown

---

## Operational Integration

Temporal awareness is enforced through DECISION_GATES.md:

- Every response begins with current datetime (Lomé UTC+0)
- Before any action, loaded concept ages are verified against their max ages
- State/CURRENT_STATE.md timestamp is checked for staleness
- If a concept exceeds its max age, it is flagged before proceeding

The gates make temporal awareness a functionality, not just documentation.

---

## Footer

Last updated: 2026-06-18 (added: operational integration with DECISION_GATES)

Temporal awareness is not optional.

It is the difference between a system that remembers and a system that understands.

A system that remembers knows facts.

A system that understands knows how reality evolved.

FounderHQ must be the latter.
