# CONCEPT BOUNDARIES

## Purpose

Prevent concept overlap.

FounderHQ becomes unmaintainable when concepts share responsibility for the same information.

Every piece of information belongs to exactly one concept.

If information could belong to two concepts, the boundary is wrong.

---

## How To Use This Document

For each concept, this document defines:

- **Role** — what the concept exists to do
- **Answers** — what questions this concept answers
- **Does NOT answer** — what questions belong to OTHER concepts
- **Boundary test** — if a piece of information could be placed in two concepts, the boundary is violated

---

## MISSION

**Role:** Define desired transformations of reality.

**Answers:**
- Why do we exist?
- Where are we trying to go?
- What future state are we bringing into existence?
- What is our long-term direction?

**Does NOT answer:**
- What should we do today? (→ PROJECT, MEMORY)
- What resources do we have? (→ ASSET, MEMORY)
- What did we learn? (→ KNOWLEDGE)
- When did something happen? (→ TIMELINE)

**Boundary test:** If a piece of information tells you WHAT to build, not WHY to build it, it belongs to PROJECT, not MISSION.

---

## PROJECT

**Role:** Represent active execution units that advance missions.

**Answers:**
- What are we building or doing?
- What stage is this effort in?
- What is blocked?
- What changed recently?
- What is the next action?

**Does NOT answer:**
- Why does this effort exist? (→ MISSION)
- What is the current priority? (→ MEMORY)
- What validated truth applies here? (→ KNOWLEDGE)
- What strategy should we use? (→ PLAYBOOK)
- What assets are available? (→ ASSET)

**Boundary test:** If a project's reason for existing is documented inside the project file, it has crossed into MISSION territory. The project should reference a mission, not contain it.

---

## MEMORY

**Role:** Store temporary operational context.

**Answers:**
- What is the current priority?
- What decisions were made recently?
- What is blocking progress right now?
- What is the current operating mode?
- What concerns are active?
- What context changes between sessions?

**Does NOT answer:**
- What truths have been validated? (→ KNOWLEDGE)
- What is our long-term direction? (→ MISSION)
- What happened in the past? (→ TIMELINE)

**Boundary test:** If a piece of information in MEMORY is still true after 30 days, it probably belongs in KNOWLEDGE. MEMORY is for what changes.

---

## KNOWLEDGE

**Role:** Store validated truths, patterns, principles, and domain expertise.

**Answers:**
- What do we know to be true?
- What lessons have been validated?
- What patterns have we observed?
- What principles guide our decisions?
- What research has been conducted?

**Does NOT answer:**
- What is the current priority? (→ MEMORY)
- What happened recently? (→ TIMELINE)
- What is the current project status? (→ PROJECT)
- How do we execute a specific process? (→ WORKFLOW)
- What strategy fits this situation? (→ PLAYBOOK)

**Boundary test:** If a piece of KNOWLEDGE has not been validated (tested, observed, confirmed), it is a hypothesis, not knowledge. Store it elsewhere until validated.

---

## TIMELINE

**Role:** Record the temporal evolution of FounderHQ.

**Answers:**
- What happened?
- When did it happen?
- In what sequence did events occur?
- How much time has passed between events?

**Does NOT answer:**
- What is the current state? (→ MEMORY, PROJECT)
- What did we learn from an event? (→ KNOWLEDGE)
- Why did something happen? (→ MISSION, PLAYBOOK)

**Boundary test:** If a TIMELINE entry contains analysis, lessons, or reasoning beyond "what happened and when," that analysis belongs in KNOWLEDGE. The timeline records facts, not interpretations.

---

## WORKFLOW

**Role:** Define repeatable execution procedures.

**Answers:**
- How do we execute a recurring process?
- What are the steps?
- What must be true before each step?
- What must be produced at each step?
- When should we stop or escalate?

**Does NOT answer:**
- What strategy should we use? (→ PLAYBOOK)
- What do we know to be true? (→ KNOWLEDGE)
- What should we work on now? (→ MEMORY, PROJECT)

**Boundary test:** If a WORKFLOW entry explains WHY a step exists rather than HOW to execute it, the reasoning belongs in PLAYBOOK or KNOWLEDGE.

---

## PLAYBOOK

**Role:** Store proven, reusable strategies.

**Answers:**
- What strategy works in this type of situation?
- When should we use this approach?
- What evidence supports this strategy?
- When should we NOT use this strategy?

**Does NOT answer:**
- How do we execute step by step? (→ WORKFLOW)
- What do we know about the domain? (→ KNOWLEDGE)
- What is the current situation? (→ MEMORY, PROJECT)

**Boundary test:** If a PLAYBOOK contains step-by-step execution instructions, the execution details belong in a WORKFLOW. The playbook is the strategy; the workflow is the procedure.

---

## ASSET

**Role:** Represent reusable resources.

**Answers:**
- What reusable resources exist?
- Where is each asset located?
- What is its status?
- Who owns it?
- Which projects use it?

**Does NOT answer:**
- What do we know about the domain? (→ KNOWLEDGE)
- How do we use this asset? (→ WORKFLOW)
- What project is this asset for? (→ PROJECT — an asset may have a relationship, but its existence is not defined by any single project)

**Boundary test:** If an ASSET entry primarily contains knowledge or instructions about how to use the asset, those belong in KNOWLEDGE or WORKFLOW. The asset registry tracks existence and location, not usage.

---

## SYSTEM

**Role:** Store the rules that govern FounderHQ itself.

**Answers:**
- What are the invariants of FounderHQ?
- What concepts must exist?
- How should an LLM operate within FounderHQ?
- What are the quality standards?
- What are the governance rules?
- How is time handled?

**Does NOT answer:**
- What is our mission? (→ MISSION)
- What is the current priority? (→ MEMORY)
- What have we learned? (→ KNOWLEDGE)

**Boundary test:** If a SYSTEM document contains operational data (current priorities, project status, etc.), that data belongs in its respective concept. SYSTEM contains only meta-rules.

---

## Overlap Detection

When reviewing any concept implementation, check for:

### Direct Overlap

The same fact appears in two concepts.

Example: Cash value in MEMORY and PROJECT.

**Fix:** Determine which concept owns cash. All other concepts reference, not contain.

### Implied Overlap

Two concepts could reasonably contain the same fact.

Example: A lesson learned from a project could go in KNOWLEDGE or PROJECT.

**Fix:** The lesson goes in KNOWLEDGE. The project references it. The project does not contain it.

### Drift Overlap

Two concepts were separate initially but converge over time.

Example: MEMORY accumulates so much that it becomes a de facto KNOWLEDGE base.

**Fix:** Archive old MEMORY entries. Move validated items to KNOWLEDGE. Keep MEMORY lean.

---

## Enforcement

Enforcement is not technical.

There is no script that prevents overlap.

Enforcement is procedural:

1. During any session, if the LLM detects overlap, it flags it
2. The overlap is recorded in the affected concepts
3. The user is informed and asked which concept should own the disputed information
4. The incorrect copy is removed or marked as a reference

---

## Footer

Clear boundaries are what separate a system from a pile of files.

A pile of files works at 10 entries.

A system works at 10,000 entries.

Boundaries are what scale.
