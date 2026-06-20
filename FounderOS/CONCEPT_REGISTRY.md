# CONCEPT REGISTRY

## Authority

This document defines the required concepts of FounderHQ.

Concepts are invariant.

Implementations are not.

FounderHQ may be implemented in any storage medium: folders, files, databases, graphs, APIs, or future systems.

The concepts must remain.

The implementation may change.

---

## Concept 1: MISSION

**Layer:** Concept — A1 (Identite)

**Purpose:** Describe desired transformations of reality.

A mission answers: What future state are we trying to bring into existence?

**Properties a mission requires:**
- A clear description of the desired transformation
- A reason why this transformation matters
- A time horizon (when will we know if we succeeded?)
- A relationship to other missions (hierarchy, dependency, independence)

**Invariant truth:** Without a mission, FounderHQ has no direction. Activity becomes noise.

---

## Concept 2: PROJECT

**Layer:** Concept — A2 (Execution)

**Purpose:** Represent active execution units.

A project is a bounded effort that advances one or more missions.

**Properties a project requires:**
- Current state or stage
- Relationship to mission(s)
- Blockers, if any
- Recent changes
- Next action

**Invariant truth:** Without projects, missions remain abstract. Projects are missions made concrete.

---

## Concept 3: MEMORY

**Layer:** Concept — A1 (Identite)

**Purpose:** Store temporary operational context.

Memory contains what is current, active, or pending.

**What memory holds:**
- Current priorities
- Recent decisions
- Open questions and blockers
- Active concerns
- Temporary context that will change

**Properties:**
- Memory changes frequently
- Memory has an age (when was it last updated?)
- Stale memory must be flagged or removed

**Invariant truth:** Without memory, every session starts from zero. Continuity is lost.

---

## Concept 4: KNOWLEDGE

**Layer:** Concept — A1 (Identite)

**Purpose:** Store validated truths.

Knowledge contains what has been learned, tested and confirmed.

**What knowledge holds:**
- Validated lessons from projects and experience
- Research findings
- Patterns observed across multiple contexts
- Principles and first principles
- External domain expertise

**Properties:**
- Knowledge evolves slowly
- Knowledge compounds over time
- Knowledge must be protected from overwrite without evidence
- Knowledge is the raw material of leverage

**Invariant truth:** Without knowledge, every problem is solved for the first time. Learning does not compound.

---

## Concept 5: TIMELINE

**Layer:** Concept — A1 (Identite)

**Purpose:** Store temporal evolution.

Timeline preserves what happened, when it happened, and in what sequence.

**What timeline holds:**
- Major decisions and their dates
- Project milestones and events
- Mission-level progress markers
- Learning breakthroughs
- External events that affected operations

**Properties:**
- Timeline is append-only (history should not be rewritten)
- Every entry has a date
- Chronology reveals patterns invisible in static state

**Invariant truth:** Without timeline, FounderHQ has no history. It cannot learn from the past or detect trends over time.

---

## Concept 6: WORKFLOW

**Layer:** Concept — A2 (Execution)

**Purpose:** Store repeatable execution procedures.

A workflow is a sequence of steps that transforms an input into a desired output.

**What workflows provide:**
- Standardized processes for recurring tasks
- Quality gates at each stage
- Criteria for proceeding or stopping
- Consistent output regardless of who or what executes

**Properties:**
- Workflows are optional but recommended for high-frequency tasks
- Workflows should be improved based on execution experience
- A workflow may reference playbooks, knowledge, or other workflows

**Invariant truth:** Without workflows, quality varies with each execution. Consistency is impossible.

---

## Concept 7: PLAYBOOK

**Layer:** Concept — A2 (Execution)

**Purpose:** Store proven operational strategies.

A playbook is a reusable strategy validated by experience.

**Difference from workflow:**
- A workflow tells you HOW to do something step by step
- A playbook tells you WHAT strategy to use and WHEN

**What playbooks contain:**
- The situation where this strategy applies
- The strategy itself (not step-by-step, but approach)
- Evidence that this strategy works (link to timeline or knowledge)
- Conditions under which the strategy should NOT be used

**Properties:**
- Playbooks emerge from repeated patterns
- A playbook is a compressed form of experience
- Playbooks are the highest form of operational leverage

**Invariant truth:** Without playbooks, every new situation is handled as if it were the first time. Experience does not compound into speed.

---

## Concept 8: ASSET

**Layer:** Concept — A2 (Execution)

**Purpose:** Represent reusable resources.

An asset is anything of value that can be reused across projects, missions or time.

**What assets include:**
- Content (videos, images, documents, templates)
- Code, scripts, automation
- Designs, brand materials
- Relationships (suppliers, partners, customers)
- Tools, equipment, inventory
- Intellectual property, research, data

**Properties:**
- An asset has a location, status, and owner
- An asset may be used by multiple projects
- Assets degrade or become obsolete over time

**Invariant truth:** Without assets, every project builds from raw materials. Nothing is reused.

---

## Concept 9: SYSTEM

**Layer:** Concept — A2 (Execution)

**Purpose:** Store operating rules.

System contains the rules that govern FounderHQ itself.

**What system holds:**
- The manifest (FOUNDERHQ_MANIFEST.md)
- The concept registry (CONCEPT_REGISTRY.md)
- The protocol (Protocols/FOUNDEROS_PROTOCOL.md)
- The temporal awareness rules (Protocols/TEMPORAL_AWARENESS.md)
- Quality gates
- Decision-making frameworks
- Governance and escalation rules

**Properties:**
- System rules may change, but changes must be documented
- System rules must be loadable by any LLM without prior training
- System rules should be minimal (no rule without a clear purpose)

**Invariant truth:** Without system, FounderHQ has no governance. It cannot self-correct or evolve intentionally.

---

## Concept 10: DISTRIBUTION MEMORY

**Layer:** Concept — A2 (Execution)

**Purpose:** Store campaign performance data.

DISTRIBUTION MEMORY contains recorded strategy and results from every distribution campaign.

**Properties:**
- Each entry captures an entire campaign (hook, audience, language, platform, performance)
- DIOS queries DISTRIBUTION MEMORY before generating new campaign strategies
- Memory accumulates over time — each campaign makes the system smarter
- Empty state is valid (no campaigns yet)

**Invariant truth:** Without distribution memory, every campaign starts from zero. Distribution intelligence cannot compound.

---

## Concept Relationships

```
MISSION guides PROJECT
PROJECT generates KNOWLEDGE
KNOWLEDGE informs PLAYBOOK
PLAYBOOK optimizes WORKFLOW
WORKFLOW executes PROJECT
PROJECT produces ASSET
ASSET supports PROJECT
MEMORY holds current context across all
TIMELINE records all changes across all
SYSTEM governs all
```

---

## Implementation Rule

A concept must be identifiable within FounderHQ.

It may be implemented as:

- A directory
- A file
- A section within a file
- A database table
- A graph node
- A tag or label
- Any future representation

The implementation must be documented so that any LLM can locate the concept.

---

## Migration Rule

When migrating FounderHQ to a new implementation:

1. Preserve all concepts
2. Update concept locations in the protocol
3. Verify every concept is loadable in the new implementation
4. Archive the old implementation until verification is complete

A concept is never deleted during migration.

---

## Footer

This registry defines what FounderHQ must contain.

If a concept is missing, FounderHQ is incomplete.

If all concepts exist, FounderHQ is whole regardless of implementation.

The concepts are the system.

Everything else is structure.
