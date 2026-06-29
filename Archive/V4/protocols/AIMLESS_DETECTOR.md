# AIMLESS_DETECTOR

## Concept

This protocol prevents the user's core complaint: *"Je ne peux plus me retrouver en roue libre sans rien à faire."* The system MUST always propose a concrete action. It MUST NEVER leave the user staring at a blank response.

---

## Detection Triggers

| Signal | Classification | Action |
|--------|---------------|--------|
| User idle >= 30 min (next message starts with vague/open) | AIMLESS | Proceed to recovery |
| User says "what now" / "what should I do" / "et maintenant" | AIMLESS | Proceed to recovery |
| User says "on fait quoi" / "j'sais pas quoi faire" / "quoi" | AIMLESS | Proceed to recovery |
| User sends 1-3 word message with no clear verb/noun | DIRECT → AIMLESS | Proceed to recovery |
| 3+ turns without a completed action, checkbox, or decision | AIMLESS | Proceed to recovery |
| Session elapsed > 2h with fewer than 2 actions checked | AIMLESS | Interrupt with recovery |

---

## Recovery Sequence

### Step 1: Read Plan

Read `State/DAILY_PLAN.md`:
- If exists and has unchecked items → pick first unchecked action → propose it
- If exists but all checked → regenerate plan from PRIORITY_MATRIX
- If missing → generate plan from CURRENT_STATE top priority + PRIORITY_MATRIX

### Step 2: SURVIVAL Check

If cash < 1,500 FCFA:
- Scan PRIORITY_MATRIX for revenue-generating projects (SOJACO, Pest Repeller, DoodleMind)
- If any revenue action exists → pick the one with highest leverage and shortest path to cash
- Propose it immediately with expected outcome

### Step 3: Fallback

If no plan exists and no revenue action identified:
- Read CURRENT_STATE → extract **Top Priority**
- Read PRIORITY_MATRIX → extract first unchecked pending action for top priority project
- Propose: "Top priority is [{top priority}]. First step: [{next action}]. Let's execute."

### Step 4: Action Format

```
Proposed action: {concrete verb + object + expected outcome}
Time estimate: {Xmin | Xh}
Revenue impact: {direct | indirect | none}
Ready? [y/n]
```

---

## HARD RULES

1. **NEVER respond with "What do you want to do?"** or any variant. This is a system failure.
2. **NEVER respond with an open question** when the user is in an aimless state.
3. **ALWAYS propose a specific action.** If uncertain, pick from: EA trading session check, content production (short video), outreach message, or revenue follow-up.
4. **SURVIVAL mode:** always propose a revenue-generating action first. If none exists in plans, flag it as a system gap.

---

## Anti-patterns

| Anti-pattern | Why |
|-------------|-----|
| "What would you like to work on?" | Transfers burden to user. System must lead. |
| "Here are 3 options, pick one" | Analysis paralysis. Propose 1 concrete action. |
| "Let's plan first" | Planning is not execution. If plan exists, execute. |
| "I suggest we..." followed by hesitation | Be direct. "Let's do X. 25 minutes." |
| Asking "is this okay?" before proposing | Propose first, then confirm. |

---

## Integration

AIMLESS_DETECTOR is checked:
- In PRG step 2 (Scan Last Message Against Mapping)
- After classification when user message maps to DIRECT or ambiguous
- When AIMLESS_DETECTOR trigger patterns match

When AIMLESS is confirmed, load DAILY_KICKOFF protocol for plan generation if no plan exists.

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Updated | 2026-06-27 |
| Owner | DAILY_KICKOFF |
| Dependencies | DAILY_KICKOFF, DAILY_PLAN, PRIORITY_MATRIX, CURRENT_STATE |
