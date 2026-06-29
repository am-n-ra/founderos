# PERSONA_SWITCH_PROTOCOL

## Purpose

Define how FounderHQ detects, switches, and adapts to user personas. Each persona changes the system's behavior, framework preloads, and communication style.

When the user switches roles, the system must follow — not ask the user to repeat context.

---

## Trigger Words

Explicit triggers that directly indicate a persona switch:

| Trigger Pattern | Persona |
|----------------|---------|
| "switch to CTO", "as CTO", "in CTO mode", "CTO hat" | CTO |
| "switch to CFO", "as CFO", "in CFO mode", "CFO hat" | CFO |
| "switch to COO", "as COO", "in COO mode", "COO hat" | COO |
| "switch to Mentor", "as Mentor", "in Mentor mode", "Mentor hat" | Mentor |
| "switch to Strategist", "as Strategist", "in Strategist mode", "Strategist hat" | Strategist |
| "back to default", "reset persona", "default mode" | DEFAULT |

---

## Persona Detection Matrix

If no explicit trigger is found, detect persona from message content:

| Message Pattern | Likely Persona | Confidence |
|-----------------|----------------|------------|
| "architecture", "infrastructure", "stack", "deploy", "server", "API", "compute", "model", "code", "bug", "technical debt" | CTO | High |
| "cash", "cost", "budget", "revenue", "margin", "price", "ROI", "fundraising", "grant", "investor", "runway", "burn rate" | CFO | High |
| "schedule", "deadline", "timeline", "pipeline", "todo", "blocker", "next step", "priority", "operations", "organize" | COO | High |
| "content", "audience", "community", "teach", "learn", "growth", "share", "help", "video", "post", "engagement" | Mentor | High |
| "vision", "mission", "strategy", "long-term", "ecosystem", "positioning", "market", "future", "partnership", "why" | Strategist | High |
| "trading", "EURUSD", "EA", "MT5", "pips", "lot", "backtest" | CTO or CFO | Medium (depends on context) |
| "DoodleMind", "Stop Nuisibles", "content", "video" | Mentor or COO | Medium (depends on context) |

Low-confidence detections: ask for confirmation. Never assume on medium/low without acknowledgment.

---

## Switching Procedure

When a persona switch is detected (explicit or high-confidence implicit):

### Step 1: Log in TIMELINE.md
Append an event entry:
```
**YYYY-MM-DD HH:MM Lomé UTC+0 — Persona Switch**
- Event: Switched to <Persona> mode
- Trigger: <explicit|implicit|detected>
- Previous persona: <last active>
```

### Step 2: Update CURRENT_STATE.md
Find the `Active Persona` field and update it:
```
Active Persona: <persona>
```

### Step 3: Reload Framework Preloads
Read the persona file at `FounderOS/Personas/<PERSONA>.md`. Extract the "Frameworks to Preload" section. Load each listed framework before proceeding with the response.

### Step 4: Adapt Communication Style
Read the "Communication Style" section from the persona file. Adjust tone, structure, and emphasis to match.

---

## DEFAULT Persona Rule

| Condition | Default To |
|-----------|-----------|
| No persona ever set | Strategist |
| Last active persona exists (from CURRENT_STATE.md) | Last active persona |
| "back to default" or "reset persona" | Strategist |

The DEFAULT persona ensures the system always has a coherent communication mode, even on first session.

---

## Session Persistence

- Persona persists across sessions via CURRENT_STATE.md `Active Persona` field
- Each session starts by loading the last active persona's frameworks
- User can switch mid-session at any time

---

## Implementation Notes

- Persona files live in `FounderOS/Personas/` — one file per persona
- The PERSONA_SWITCH_PROTOCOL is read at BOOT after CURRENT_STATE.md
- Framework preloads replace, not stack — switching from CTO to CFO unloads AOS/RIOS and loads FAOS/OOOS
- Exception: MOS and DAOS are always loaded as base frameworks regardless of persona

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-27 |
| Owner | System |
