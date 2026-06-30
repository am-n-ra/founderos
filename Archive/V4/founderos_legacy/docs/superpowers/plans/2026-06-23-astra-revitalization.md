# ASTRA Revitalization Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform ASTRA from a 61-line stub into the operational reflective engine it claims to be — with concrete workflows, session templates, and real integration.

**Architecture:** ASTRA reads TIMELINE, CURRENT_STATE, MEMORY; produces reflective insights, pattern hypotheses, actionable learnings, retrospectives. Must integrate with REFLECTION mode in SYSTEM_PROMPT.md.

**Tech Stack:** Markdown, SYSTEM_PROMPT.md routing, TIMELINE/MEMORY/KNOWLEDGE integration

---

### Task 1: Expand ASTRA.md with Reflection Workflows

**Files:**
- Modify: `ASTRA.md` (complete rewrite)

- [ ] **Step 1: Write the new ASTRA.md**

Write `ASTRA.md` with these sections:

```markdown
# FounderOS V4 — ASTRA (Astro-Reflective Assistant)

## Purpose

ASTRA is the reflective intelligence engine. Provides structured reflection, pattern recognition across sessions, and strategic clarity through targeted questioning. Loaded when the founder needs to make sense of past outcomes, extract learnings, or identify patterns across time.

## Position in FounderHQ

ASTRA generates reflective insights and retrospective analysis. Feeds into KNOWLEDGE_EVOLUTION_ENGINE (verified insights), PATTERN_ENGINE (pattern hypotheses), and PLAYBOOK_ENGINE (reusable tactics).

## Inputs

- `concepts/TIMELINE.md` — raw events, decisions, outcomes
- `State/CURRENT_STATE.md` — current mode, cash, bottleneck, priority
- `concepts/MEMORY.md` — past decisions and their results
- `concepts/KNOWLEDGE.md` — validated truths for context

## Outputs

- **Reflective insights** — what worked, what didn't, why
- **Pattern hypotheses** — recurring behaviors, market signals, bottlenecks
- **Actionable learnings** — specific recommendations based on analysis
- **Retrospectives** — structured post-mortems for key events

## Relations

- **KNOWLEDGE_EVOLUTION_ENGINE** — verified insights stored for future reference
- **PATTERN_ENGINE** — pattern hypotheses fed for validation
- **PLAYBOOK_ENGINE** — repeatable tactics extracted from reflections
- **TIMELINE** — reads raw events, writes analyses
- **CONTINUOUS_IMPROVEMENT** — improvement signals feed into CI cycles

## When to Invoke

- End of day/week reflection
- User feels stuck, scattered, or uncertain
- Before major decisions
- When multiple options exist and none is clearly better
- When user needs to clarify their own thinking
- After a significant outcome (win or loss)
- At mode transitions (SURVIVAL → GROWTH, GROWTH → SCALE)

## Reflection Types

### A. Daily Reflection (5-10 min)

Use when: End of session or start of next session.

```
1. What happened? — Key events, decisions, outcomes from TIMELINE
2. What worked? — Actions that produced positive results
3. What didn't? — Actions that failed or underperformed
4. What surprised me? — Unexpected outcomes or signals
5. What is the one thing to carry forward? — Actionable takeaway
6. TIMELINE entry? — Write key findings to TIMELINE
```

### B. Strategic Reflection (20-30 min)

Use when: Stuck on a decision, multiple paths forward, weekly review.

```
Phase 1 — Ground Truth
- Load CURRENT_STATE: mode, cash, bottleneck, priority, active products
- Load MEMORY: recent decisions, open questions, active concerns
- Summarize current reality in 3 sentences

Phase 2 — Pattern Scan
- What has repeated 3+ times in the last 7 days?
- Is there a single root cause behind multiple surface problems?
- What would happen if I ignored the loudest problem for 1 week?

Phase 3 — Decision Clarity
- What decision am I avoiding?
- What would I do with 10x resources? With 1/10 resources?
- What would the best version of me decide?
- What would I tell a friend in this situation?
- If I had to decide in 5 minutes, what would I choose?

Phase 4 — Output
- Specific next action (not general direction)
- Pattern hypothesis for PATTERN_ENGINE (if applicable)
- One thing to stop doing
- TIMELINE entry
```

### C. Mode-Transition Reflection (30-45 min)

Use when: Moving from SURVIVAL → GROWTH or GROWTH → SCALE.

```
1. What got us here? — Key decisions that enabled the transition
2. What must change? — Behaviors/patterns that worked in previous mode but will fail in new mode
3. What are the new rules? — What's different about decision-making in the new mode?
4. What are we leaving behind? — Projects, habits, assumptions that no longer serve
5. New mode primer — Write a concise operating manual for the new mode
6. TIMELINE entry + Update CURRENT_STATE
```

### D. Post-Outcome Autopsy (15-20 min)

Use when: A significant win or loss just happened.

```
1. What exactly happened? — Objective facts, no interpretation
2. What was the expected outcome? — What did I think would happen?
3. What actually happened? — Actual outcome
4. Why the gap? — Analysis of the difference
5. What can I replicate? (if win)
6. What can I prevent? (if loss)
7. TIMELINE entry — Write findings
```

## Session Template

When ASTRA is loaded:

```markdown
# ASTRA Session — YYYY-MM-DD

## Trigger
> Why was ASTRA loaded?

## Reflection Type Selected
> Daily / Strategic / Mode-Transition / Post-Outcome

## Input Summary
- **Mode:** CURRENT_STATE mode
- **Cash:** CURRENT_STATE cash
- **Bottleneck:** CURRENT_STATE bottleneck
- **Top Priority:** CURRENT_STATE top priority
- **Last Decision:** CURRENT_STATE last decision

## Reflection Output

### What happened?
> Key events since last reflection

### What worked?
> ...

### What didn't?
> ...

### Key Insight
> The single most important thing

### Next Action
> What to do next

## TIMELINE Entry Generated
> (paste entry)
```

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-23 |
| Owner | System |
```

- [ ] **Step 2: Verify the file**

Read `ASTRA.md` back and confirm all sections are present.

- [ ] **Step 3: Commit**

```bash
git add ASTRA.md
git commit -m "feat: expand ASTRA with 4 reflection types and session template"
```

---

### Task 2: Run a Real ASTRA Reflection

**Files:**
- Modify: `concepts/TIMELINE.md` (add reflection entry)
- Create: First reflection using the session template

- [ ] **Step 1: Read inputs**

Read `TIMELINE.md` (full file) and load current context.

- [ ] **Step 2: Execute Daily Reflection using the new ASTRA workflow**

Use the Daily Reflection template to analyze the last 3 days (2026-06-20 to 2026-06-23) and write a structured output.

Ask the user (in French) these questions from the workflow:
1. What happened? — résumé des événements clés
2. What worked? — qu'est-ce qui a marché
3. What didn't? — qu'est-ce qui n'a pas marché
4. What surprised me? — qu'est-ce qui a surpris
5. What is the one thing to carry forward? — l'essentiel à retenir

Collect their answers and:

- [ ] **Step 3: Write findings to TIMELINE.md**

Append to TIMELINE.md the reflection entry with the findings.

- [ ] **Step 4: Verify TIMELINE.md**

Read the last 20 lines of TIMELINE.md to confirm the entry was written correctly.

- [ ] **Step 5: Commit**

```bash
git add concepts/TIMELINE.md
git commit -m "feat: first ASTRA reflection session"
```

---

### Task 3: Wire ASTRA into SYSTEM_PROMPT.md REFLECTION Mode

**Files:**
- Modify: `SYSTEM_PROMPT.md` — REFLECTION mode instructions

- [ ] **Step 1: Read current REFLECTION mode section in SYSTEM_PROMPT.md**

Grep for the REFLECTION mode block to find the exact lines.

- [ ] **Step 2: Expand REFLECTION mode to use new ASTRA workflows**

Replace the simple "Load ASTRA.md" instruction with a concrete workflow that loads ASTRA, selects a reflection type based on context, executes the workflow, and writes to TIMELINE.

- [ ] **Step 3: Verify SYSTEM_PROMPT.md**

Read the modified section to confirm correctness.

- [ ] **Step 4: Commit**

```bash
git add SYSTEM_PROMPT.md
git commit -m "feat: wire ASTRA reflection types into SYSTEM_PROMPT REFLECTION mode"
```

---

### Task 4: Update Last Verified Timestamps

**Files:**
- Modify: `ASTRA.md` (last verified date)
- Modify: `State/CURRENT_STATE.md` (last updated, last decision)
- Modify: `SYSTEM_PROMPT.md` (footer date if applicable)

- [ ] **Step 1: Update all stale dates to 2026-06-23**

- [ ] **Step 2: Commit**

```bash
git add ASTRA.md State/CURRENT_STATE.md SYSTEM_PROMPT.md
git commit -m "chore: update timestamps for ASTRA revitalization"
```
