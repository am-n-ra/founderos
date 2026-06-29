# INFO CAPTURE PROTOCOL

## Purpose

Any operational information given in conversation is automatically captured in FHQ. This protocol defines which type of info goes into which file, without waiting for explicit instruction.

## Fundamental Rule

**If the info is useful to a future session, it must be written now.**

Do not ask "do you want me to save it?" — save it directly.

---

## Mapping Type → File

| Information Type | Example | Target File | Action |
|-------------------|---------|--------------|--------|
| **Deadline / cutoff date** | "June 22 at 4:59 PM" | State/PRIORITY_MATRIX.md | Update deadline + warning 🔴 |
| **Project progress** | "I finished 1.1 Debt vs Equity" | State/CURRENT_STATE.md + State/PRIORITY_MATRIX.md | Update status section + dashboard |
| **New project** | "I'm launching Omni" | Apply PROJECT_REGISTRATION_PROTOCOL.md | Create concept/ + projects/ + all links |
| **Decision** | "We're going with Innov'Action not Idée-Action" | State/CURRENT_STATE.md + relevant concepts | Update Last Decision |
| **Figure / metric** | "Collection 4,875 FCFA" | State/CURRENT_STATE.md | Update Cash + product info |
| **Blockage** | "Supplier no update" | State/PRIORITY_MATRIX.md | Set warning 🟡/🔴 |
| **Important event** | "Herlog sent" | TIMELINE.md | Record Event → Decision → Outcome |
| **New relationship** | "OMNI linked to KORA" | Relevant concepts | Add bidirectional link |
| **Preference / rule** | "Always track both" | Protocols/INFO_CAPTURE_PROTOCOL.md | Add the rule |
| **Watch information** | "Websearch result X" | State/WATCH_REGISTRY.md | Update Last Result + Next Check |

---

## Concrete Cases (recent examples)

| What you said | What was captured | Where |
|-----------------|---------------------|-----|
| "I just finished 1.1 Debt vs Equity" | Financial Literacy 1.1 → ✅ | State/CURRENT_STATE.md + State/PRIORITY_MATRIX.md |
| "company not yet registered" | Omni company status corrected | projects/Omni/annexes/A4_DJANTA_TECH_HUB.md |
| "omni should be in innov action" | Program confirmed | concepts/OMNI.md + annexes A4 |
| "why don't you track all my goals" | PRIORITY_MATRIX.md created | New file |

---

## What Is NOT Captured

- Questions without operational answers
- Unconfirmed exploratory thoughts
- Conversations not related to FHQ (unless an emergent pattern)

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | System |

