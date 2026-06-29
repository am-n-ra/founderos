# DECISION_GATES

## Concept

Decision Gates enforce FounderHQ's execution discipline.

Before every action, the agent must identify the action type, load the required concepts, verify their freshness, and only then respond.

Without gates, FounderHQ is a library.

---

## How Gates Work

```
Action Request
    ↓
Identify Action Type (match the request to a gate below)
    ↓
LOAD required concepts (read them in the current session)
    ↓
LOAD optional frameworks (if applicable — read the lens)
    ↓
VERIFY freshness (is each concept older than its max age?)
    ↓
CHECK escalation level — does this action require founder approval?
    ↓
APPLY lens framework (answer the lens questions in context)
    ↓
APPLY PRIORITIZATION_PROTOCOL (is this the right action NOW?)
    ↓
Respond (or escalate with options)
```

**Escalation check:** If the action involves Financial, Legal, Security, Hiring, Equity, External Communications, or Personal Data — escalate to founder regardless of gate type.

**Failure mode:** If a required concept is stale (> max age), flag it before responding. Do not proceed without current data.

---

## Universal Action Types

### 1. Strategic

**Triggers:** "What should I do?", "What's the priority?", "Which direction?", "Define next action", "How to allocate time?"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `State/CURRENT_STATE.md` — Cash, Bottleneck, Priority, Last Decision (real-time)
- `Concepts/TIMELINE.md` — Last 7 days events (max 14 days)
- `Concepts/PROJECT.md` — Active projects, Status, Next Action (max 7 days)

**Optional Frameworks:**
- CAOS — Allocation hierarchy, survival protocol
- SAOS — System analysis, bottleneck identification

---

### 2. Financial

**Triggers:** "Set a price", "Create an offer", "Discount", "Budget", "Spend money", "Investment decision"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `State/CURRENT_STATE.md` — Cash, Active Product (real-time)
- `Concepts/ASSET.md` — Product cost, Margin, Supplier data (max 30 days)

**Optional Frameworks:**
- CAOS — Capital preservation, allocation hierarchy
- FAOS — Capital sourcing, runway analysis

---

### 3. Product

**Triggers:** "Define a product", "Validate an offer", "Position a product", "Feature decision", "Product pivot"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — Relevant product knowledge (max 14 days)
- `Concepts/ASSET.md` — Existing products, inventory, supply chain (max 30 days)

**Optional Frameworks:**
- PSOS — Product strategy, positioning, validation

---

### 4. Content

**Triggers:** "Write a script", "Create a video", "Write a post", "Propose a hook", "Design a CTA", "Plan content"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — Content principles, audience tactics, offer design (max 14 days)
- `Concepts/WORKFLOW.md` — WF-001 Video Production (max 30 days)
- `State/CURRENT_STATE.md` — Cash, Active Product, Top Priority, Bottleneck (real-time)

**Optional Frameworks:**
- CEOS — Hook analysis, conversion strategy, distribution
- MAOS (Content/) — Marketing campaign planning, audience acquisition
- AI_VIDEO_MASTER_DOMAIN (AI/) — Entity-based video production pipeline

---

### 5. Operational

**Triggers:** "Execute a process", "Run a workflow", "Follow a procedure", "Checklist execution"

**Required Concepts:**
- `Concepts/WORKFLOW.md` — Relevant workflow(s) (max 30 days)
- `State/CURRENT_STATE.md` — Current priority, bottleneck (real-time)

**Optional Frameworks:**
- None (workflows are self-contained)

---

### 6. Research

**Triggers:** "Research a topic", "Analyze a market", "Investigate a competitor", "Explore an opportunity"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — What we already know (max 14 days)

**Optional Frameworks:**
- SAOS — System analysis, dependency mapping
- PSOS — Opportunity evaluation

---

### 7. Learning

**Triggers:** "Learn a skill", "Study a field", "Read a resource", "Take a course"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/KNOWLEDGE.md` — What we already know (max 14 days)

**Optional Frameworks:**
- PSOS — Learning Principle: learn → apply → build → validate

---

### 8. Creative

**Triggers:** "Brainstorm ideas", "Generate concepts", "Create something new", "Explore a creative direction"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/ASSET.md` — Brand guidelines, existing assets (max 30 days)

**Optional Frameworks:**
- CEOS — Audience alignment
- PSOS — Leverage principle
- AI_VIDEO_MASTER_DOMAIN (AI/) — Video production concepts, entity framework

---

### 9. Technical

**Triggers:** "Build something", "Configure a tool", "Set up a system", "Write code", "Fix a technical issue"

**Required Concepts:**
- `Concepts/WORKFLOW.md` — Relevant workflow (max 30 days)
- `Concepts/KNOWLEDGE.md` — Relevant technical knowledge (max 14 days)

**Optional Frameworks:**
- SAOS — System analysis, bottleneck identification
- AAOS (AI/) — Automation design, agent architecture

---

### 10. Relationship

**Triggers:** "Contact someone", "Send a message", "Network", "Partnership outreach", "Hire", "Collaborate"

**Required Concepts:**
- `Concepts/MISSION.md` — Current Missions (max 7 days)
- `Concepts/PROJECT.md` — Current projects, relevant context (max 7 days)

**Optional Frameworks:**
- FAOS — Capital hierarchy (relationships as capital)
- PSOS — Trust principle

---

## Gate Bypass Rule

If no action type matches the request, classify by intent:

- "Decide what to do" → Strategic
- "Spend/create with money" → Financial
- "Make something for others" → Content or Product
- "Follow a procedure" → Operational
- "Learn something" → Learning or Research
- "Build/create technically" → Technical

When in doubt, use Strategic.

---

## Footer

Version: V2 — Universal taxonomy (10 types). Frameworks: 8 actifs (CAOS, CEOS, PSOS, FAOS, SAOS, MAOS, AAOS, AI_VIDEO_MASTER_DOMAIN), 3 experimental (PMOS, RIOS, LEOS). Integre PRIORITIZATION_PROTOCOL.

Gates are enforced by the agent at boot. There is no other gatekeeper.

If a gate is skipped, the action is unconstrained. That is the system's failure mode.

If you skip a gate, flag it: "⚠️ GATE SKIPPED: [action type] — response may be unconstrained."
