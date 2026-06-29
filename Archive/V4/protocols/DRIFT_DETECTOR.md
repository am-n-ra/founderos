# DRIFT_DETECTOR

## Purpose

Detect when the user's activity diverges from mission-aligned priorities. Drift is not failure — it is a signal. The system flags it, does not block it.

Drift detection runs after every user message, as part of the PRG sequence.

---

## Detection Rules

Executed in priority order. Stop at first match.

### 1. Time Drift

**Rule:** If >48h spent on a project without measurable progress on the top-priority project (from CURRENT_STATE.md Top Priority), flag.

**Check:**
- Read CURRENT_STATE.md Top Priority
- Scan TIMELINE.md last 48h for entries related to the top-priority project
- If zero entries or zero progress markers → flag

**Severity:** MEDIUM

---

### 2. Mission Drift

**Rule:** If user spends >3 consecutive sessions on activities not traceable to any active mission in MISSION.md, flag.

**Check:**
- Read MISSION.md Active Missions
- Scan TIMELINE.md last 3 sessions
- Map each session's activities to a mission
- If any session has 0 mapped activities → increment drift counter
- If drift counter ≥ 3 → flag

**Severity:** HIGH

**Reset:** Counter resets when a mission-mapped activity occurs.

---

### 3. Scope Drift

**Rule:** If a task or project expands beyond its original scope without explicit expansion decision, flag.

**Check:**
- Compare PRIORITY_MATRIX.md Next Action vs. what is being discussed
- If user is adding sub-tasks, features, or requirements not in the original scope → flag
- Look for phrases like "also", "while we're at it", "what if we also", "let's add"

**Severity:** LOW (first occurrence), MEDIUM (repeat in same session)

---

### 4. Revenue Drift (SURVIVAL mode only)

**Rule:** If Operating Mode = SURVIVAL and >24h without any revenue-generation activity, flag.

**Check:**
- Read CURRENT_STATE.md Operating Mode
- If SURVIVAL: scan TIMELINE.md last 24h for revenue-related activities (sales, content publishing, outreach, trading, pitching)
- If zero revenue actions → flag

**Severity:** HIGH

---

## Drift Response Procedure

When drift is detected, execute in order:

### Step 1: Log to TIMELINE.md
```
**YYYY-MM-DD HH:MM Lomé UTC+0 — Drift Detected**
- Event: Drift Detected — <type>
- Description: <specific description>
- Severity: <LOW|MEDIUM|HIGH>
```

### Step 2: Write to ALERTS.md
Add entry to Active Alerts table:

| Priority | Alert | Source | Status |
|----------|-------|--------|--------|
| <severity> | Drift: <type> — <brief description> | DRIFT_DETECTOR | ACTIVE |

### Step 3: Include Drift Notice in Response
In the next response, include:

```
⚠️ Drift detected: <type> — <description>
Recommended: <correction>
```

**Correction recommendations:**
- Time drift: "Focus next session on <top priority> to realign with current bottleneck."
- Mission drift: "Review MISSION.md. Which active mission does this activity serve? If none, consider parking it."
- Scope drift: "Original scope was <original>. Expanding to <new> requires explicit approval. Confirm or revert?"
- Revenue drift: "SURVIVAL mode requires revenue action within 24h. Prioritize: <suggest specific revenue action from DAOS>."

### Step 4: NEVER Block
Drift notices are informational. Do not refuse to execute the user's request. Flag, recommend, continue.

---

## Escalation Rules

| Condition | Action |
|-----------|--------|
| 3+ drift events in 7 days | Recommend "Mission Coherence Check" session |
| 5+ drift events in 7 days | Force mode switch to STRATEGIC, load VEAOS + MOS |
| Revenue drift in SURVIVAL + cash < 1,000 FCFA | Escalate to HIGH + recommend immediate revenue action override |

### Mission Coherence Check Procedure
When triggered:
1. Read MISSION.md in full
2. Read TIMELINE.md last 14 days
3. Read CURRENT_STATE.md
4. Present findings to user: "You've had <N> drift events in 7 days. Here's what's pulling you off mission: <patterns>. Recommended: <recommit to top 1-2 priorities> or <adjust MISSION.md if priorities have genuinely changed>."
5. If MISSION.md needs updating, present edits for approval.

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-27 |
| Owner | System |
