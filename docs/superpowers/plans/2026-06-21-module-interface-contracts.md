# Module Interface Contracts — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Position, Inputs, Outputs, Relations, Workflow sections to all 14 V4 modules, following DIOS.md pattern.

**Architecture:** Each module receives 5 new sections (Position, Inputs, Outputs, Relations, Workflow) after the existing Purpose section. Existing content moves verbatim into Workflow. File length increases ~20-40 lines per module.

**Files modified:** 14 modules in FounderOS/

---

### Task 1: Core Strategy Modules (MOS, VEAOS, DAOS)

**Files:**
- Modify: `FounderOS/MOS.md`
- Modify: `FounderOS/VEAOS.md`
- Modify: `FounderOS/DAOS.md`

For each file:
1. Read the file
2. After the `## Purpose` section (and its content), insert:
   - `## Position in FounderHQ`
   - `## Inputs`
   - `## Outputs`
   - `## Relations`
   - `## Workflow`
3. Move existing content below Purpose into the Workflow section
4. Preserve existing footer unchanged

**Exact content to insert per module:**

**MOS.md:**
```
## Position in FounderHQ

MOS sits at the top of the execution stack. It is loaded when the agent needs to determine what to pursue. It feeds priorities to DAOS (daily execution) and context to PROJECT (project state).

## Inputs
- `concepts/MISSION.md` — mission definitions, hierarchy, active/paused/archived status
- `State/CURRENT_STATE.md` — cash position, bottlenecks, current operating mode
- `concepts/TIMELINE.md` — recent events that affect priorities

## Outputs
- Priority list — ranked actions serving the highest mission
- Strategic recommendations — Stop/Pause/Accelerate/Delegate/Automate/Kill for each project
- Drift detection — when projects consume resources without mission progress

## Relations
- **DAOS** — receives priorities and generates daily action modules
- **PROJECT** — updates project status based on priority shifts
- **DECISION_ENGINE** — called when tradeoffs between missions need structured analysis

## Workflow
```

**VEAOS.md:**
```
## Position in FounderHQ

VEAOS handles long-term strategic thinking. It is loaded when the agent faces questions about direction, vision, or multi-month planning. It feeds strategic context into MOS (priority setting) and DECISION_ENGINE (long-term decisions).

## Inputs
- `concepts/MISSION.md` — long-term mission definitions
- `concepts/TIMELINE.md` — historical patterns and trajectory
- `State/CURRENT_STATE.md` — current constraints and resources

## Outputs
- Strategic scenarios — 3-5 year projections
- Vision statements — refined mission language
- Strategic recommendations — what to pursue, what to deprioritize over long horizon

## Relations
- **MOS** — strategic context informs priority setting
- **DECISION_ENGINE** — strategic tradeoffs use PROACT framework
- **TIMELINE** — strategic decisions recorded as timeline events

## Workflow
```

**DAOS.md:**
```
## Position in FounderHQ

DAOS owns daily execution. It is loaded by RUNTIME Phase 2 (Decide) or when SURVIVAL Auto-Drive triggers. It receives priorities from MOS and produces concrete actions the founder can execute immediately.

## Inputs
- `concepts/MOS.md` — current top priority
- `State/CURRENT_STATE.md` — cash, blockers, mode
- `concepts/PLAYBOOK.md` — relevant playbooks for today's situation

## Outputs
- Action modules — scripts, timing, expected outcome, fallback for 1-3 actions
- Execution context — what changed since yesterday, what is blocked, what is ready

## Relations
- **MOS** — receives top priority
- **CEOS** — delegates content actions when applicable
- **FAOS** — delegates financial actions when applicable
- **TIMELINE** — writes execution outcomes after each action

## Workflow
```

- [ ] **Step 1: Edit MOS.md** — read, insert sections after Purpose, move existing content to Workflow
- [ ] **Step 2: Edit VEAOS.md** — same pattern
- [ ] **Step 3: Edit DAOS.md** — same pattern
- [ ] **Step 4: Commit**

```bash
git add FounderOS/MOS.md FounderOS/VEAOS.md FounderOS/DAOS.md
git commit -m "feat: add interface contracts to MOS, VEAOS, DAOS"
```

---

### Task 2: Content & Distribution Modules (CEOS, AI_VIDEO_MASTER_DOMAIN, DIOS)

**Files:**
- Modify: `FounderOS/CEOS.md`
- Modify: `FounderOS/AI_VIDEO_MASTER_DOMAIN.md`
- Modify: `FounderOS/DIOS.md` — already has full structure, skip

**CEOS.md content:**
```
## Position in FounderHQ

CEOS produces content assets. It is loaded after DIOS determines distribution requirements. It feeds production specs to AI_VIDEO_MASTER_DOMAIN and outputs content to DIOS for distribution.

## Inputs
- `FounderOS/DIOS.md` — distribution requirements (platform, audience, format)
- `FounderOS/AI_VIDEO_MASTER_DOMAIN.md` — video production framework
- `concepts/ASSET.md` — brand assets, existing content

## Outputs
- Content scripts — hook, body, CTA per platform
- Production briefs — specs for AI_VIDEO_MASTER_DOMAIN
- Content metadata — titles, descriptions, tags, thumbnails

## Relations
- **DIOS** — receives distribution requirements, sends finished content
- **AI_VIDEO_MASTER_DOMAIN** — receives production briefs for video generation
- **ASSET** — creates and updates content assets

## Workflow
```

**AI_VIDEO_MASTER_DOMAIN.md content:**
```
## Position in FounderHQ

AI_VIDEO_MASTER_DOMAIN is the video production engine. It receives production briefs from CEOS and generates AI video prompts, assembly instructions, and quality checks.

## Inputs
- `FounderOS/CEOS.md` — production brief, script, visual direction
- `concepts/ASSET.md` — brand assets, reference materials

## Outputs
- Image prompts — scene-by-scene AI generation prompts
- Video assembly — frame sequences, transitions, timing
- Quality checklist — hook verification, retention checkpoints

## Relations
- **CEOS** — receives production briefs
- **DIOS** — finished video sent for distribution packaging
- **ASSET** — video files tracked as assets

## Workflow
```

- [ ] **Step 1: Edit CEOS.md** — insert sections after Purpose, move existing content to Workflow
- [ ] **Step 2: Edit AI_VIDEO_MASTER_DOMAIN.md** — insert sections, reformat existing content into Workflow steps
- [ ] **Step 3: Commit**

```bash
git add FounderOS/CEOS.md FounderOS/AI_VIDEO_MASTER_DOMAIN.md
git commit -m "feat: add interface contracts to CEOS, AI_VIDEO_MASTER_DOMAIN"
```

---

### Task 3: Reflection, Research & Learning (ASTRA, RIOS, LEOS)

**Files:**
- Modify: `FounderOS/ASTRA.md`
- Modify: `FounderOS/RIOS.md`
- Modify: `FounderOS/LEOS.md`

**ASTRA.md content:**
```
## Position in FounderHQ

ASTRA provides clarity when the founder is stuck, uncertain, or needs reflection. It is loaded when the agent detects confusion, indecision, or emotional weight. It feeds reframed problems into DECISION_ENGINE.

## Inputs
- `State/CURRENT_STATE.md` — current mode, blockers, session objective
- `concepts/MEMORY.md` — cross-session concerns, recurring patterns
- `concepts/TIMELINE.md` — recent events leading to current state

## Outputs
- Reframed problem — alternative perspective on the situation
- Clarity statement — what is actually going on vs what it feels like
- Decision options — concrete paths forward with tradeoffs

## Relations
- **DECISION_ENGINE** — feeds reframed problems for structured analysis
- **SOS** — coordinates when emotional state affects decision quality
- **MEMORY** — stores reflective insights as cross-session patterns

## Workflow
```

**RIOS.md content:**
```
## Position in FounderHQ

RIOS conducts external research. It is loaded when the agent needs information beyond the filesystem — market data, competitor analysis, factual verification. It can be called by any module.

## Inputs
- Research question — from any module or direct user request
- Search context — domain, sources, depth required

## Outputs
- Research findings — structured by question, with source citations
- Verified facts — confirmed or refuted claims
- Knowledge entries — validated findings written to KNOWLEDGE.md

## Relations
- **KNOWLEDGE** — validated research written as knowledge entries
- **Any module** — can be called by any module needing external data
- **TIMELINE** — research activities recorded as timeline events

## Workflow
```

**LEOS.md content:**
```
## Position in FounderHQ

LEOS manages learning. It is loaded when the founder identifies a skill gap or knowledge need. It produces learning roadmaps and resources, and validates completion.

## Inputs
- Learning goal — from any module or direct user request
- `concepts/KNOWLEDGE.md` — existing knowledge, validated lessons

## Outputs
- Learning roadmap — step-by-step skill acquisition plan
- Resource list — tutorials, courses, references
- Validation criteria — how to confirm the skill was acquired

## Relations
- **KNOWLEDGE** — validated lessons written to KNOWLEDGE.md
- **PROJECT** — learning milestones tracked as project tasks
- **Any module** — skill gaps identified by any module trigger learning

## Workflow
```

- [ ] **Step 1: Edit ASTRA.md**
- [ ] **Step 2: Edit RIOS.md**
- [ ] **Step 3: Edit LEOS.md**
- [ ] **Step 4: Commit**

```bash
git add FounderOS/ASTRA.md FounderOS/RIOS.md FounderOS/LEOS.md
git commit -m "feat: add interface contracts to ASTRA, RIOS, LEOS"
```

---

### Task 4: Business & Wellbeing (FAOS, SOS, AOS)

**Files:**
- Modify: `FounderOS/FAOS.md`
- Modify: `FounderOS/SOS.md`
- Modify: `FounderOS/AOS.md`

**FAOS.md content:**
```
## Position in FounderHQ

FAOS handles fundraising, revenue, and partnerships. It is loaded when the founder needs money, investors, or strategic allies. It produces fundraising plans and tracks financial pipeline.

## Inputs
- `State/CURRENT_STATE.md` — cash position, burn rate, mode
- `concepts/MISSION.md` — fundraising justification
- `concepts/ASSET.md` — products, pricing, revenue data

## Outputs
- Fundraising plan — targets, channels, timeline, pitch
- Partner list — potential allies with contact and approach
- Revenue tracking — actual vs projected revenue

## Relations
- **DAOS** — fundraising actions executed via daily action modules
- **SOS** — founder capacity affects fundraising outreach capacity
- **ASSET** — revenue data tracked as assets

## Workflow
```

**SOS.md content:**
```
## Position in FounderHQ

SOS monitors founder wellbeing. It is loaded when the agent detects fatigue, burnout, or the founder reports tiredness. It assesses energy, recommends rest, and adjusts execution expectations.

## Inputs
- `State/CURRENT_STATE.md` — session history, action load
- `concepts/TIMELINE.md` — recent session duration and intensity
- Founder's self-report — energy level, mood, focus

## Outputs
- Energy assessment — current state, projected capacity
- Rest recommendation — break duration, recovery activity
- Adjusted expectations — what is realistic given energy level

## Relations
- **DAOS** — adjusts daily action load based on energy
- **ASTRA** — coordinates when emotional state affects clarity
- **TIMELINE** — wellbeing checkpoints recorded

## Workflow
```

**AOS.md content:**
```
## Position in FounderHQ

AOS maintains FounderOS integrity. It is loaded when architecture decisions arise or system structure needs review. It audits concepts, detects drift, and recommends structural improvements.

## Inputs
- `FounderOS/SYSTEM_PROMPT.md` — current system architecture
- `Protocols/SOURCE_OF_TRUTH.md` — truth ownership map
- `concepts/SYSTEM.md` — system rules and governance

## Outputs
- Architecture recommendations — structural improvements
- Drift detection — concept boundary violations
- Audit findings — concept purity, consistency issues

## Relations
- **SYSTEM** — architecture changes affect system rules
- **CONTINUOUS_IMPROVEMENT** — coordinates improvement cycles
- **CONCEPT_AUDIT** — audit findings recorded

## Workflow
```

- [ ] **Step 1: Edit FAOS.md**
- [ ] **Step 2: Edit SOS.md**
- [ ] **Step 3: Edit AOS.md**
- [ ] **Step 4: Commit**

```bash
git add FounderOS/FAOS.md FounderOS/SOS.md FounderOS/AOS.md
git commit -m "feat: add interface contracts to FAOS, SOS, AOS"
```

---

### Task 5: Engines (DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE)

**Files:**
- Modify: `FounderOS/DECISION_ENGINE.md`
- Modify: `FounderOS/PATTERN_ENGINE.md`
- Modify: `FounderOS/PLAYBOOK_ENGINE.md`

**DECISION_ENGINE.md content:**
```
## Position in FounderHQ

DECISION_ENGINE provides structured decision-making. It is loaded when the agent faces tradeoffs, uncertainty, or multi-option choices. It runs the PROACT framework and outputs a recommendation.

## Inputs
- Decision question — what needs to be decided
- Decision context — options, criteria, constraints (from any module or user)
- `concepts/KNOWLEDGE.md` — past decisions and lessons

## Outputs
- Decision recommendation — ranked options with tradeoff analysis
- PROACT framework output — Problem, Objectives, Alternatives, Consequences, Tradeoffs
- Decision record — written to TIMELINE.md

## Relations
- **MOS** — strategic decisions affect priorities
- **ASTRA** — receives reframed problems for analysis
- **TIMELINE** — decisions recorded for future reference

## Workflow
```

**PATTERN_ENGINE.md content:**
```
## Position in FounderHQ

PATTERN_ENGINE detects recurring patterns across actions and outcomes. It is loaded after multiple similar events occur, or when the agent senses a repeating dynamic. It feeds pattern data to PLAYBOOK_ENGINE.

## Inputs
- `concepts/TIMELINE.md` — event history
- `concepts/KNOWLEDGE.md` — validated lessons
- `concepts/MEMORY.md` — cross-session observations

## Outputs
- Detected patterns — what repeats, under what conditions, with what outcome
- Pattern recommendations — confirm, investigate, or codify as playbook

## Relations
- **PLAYBOOK_ENGINE** — confirmed patterns become playbooks
- **KNOWLEDGE** — pattern insights written as knowledge
- **TIMELINE** — pattern detection events recorded

## Workflow
```

**PLAYBOOK_ENGINE.md content:**
```
## Position in FounderHQ

PLAYBOOK_ENGINE creates and validates playbooks. It is loaded when a pattern has been confirmed across 3+ contexts or when the agent needs to document a repeatable process.

## Inputs
- `FounderOS/PATTERN_ENGINE.md` — detected patterns ready for codification
- `concepts/WORKFLOW.md` — existing workflows that may become playbooks
- `concepts/KNOWLEDGE.md` — validated strategies and lessons

## Outputs
- Validated playbooks — documented in PLAYBOOK.md with trigger conditions
- Playbook status — draft, validated, deprecated
- Playbook recommendations — what to use for current situation

## Relations
- **PATTERN_ENGINE** — receives patterns for codification
- **WORKFLOW** — playbooks may update workflows
- **DAOS** — action modules reference relevant playbooks

## Workflow
```

- [ ] **Step 1: Edit DECISION_ENGINE.md**
- [ ] **Step 2: Edit PATTERN_ENGINE.md**
- [ ] **Step 3: Edit PLAYBOOK_ENGINE.md**
- [ ] **Step 4: Commit**

```bash
git add FounderOS/DECISION_ENGINE.md FounderOS/PATTERN_ENGINE.md FounderOS/PLAYBOOK_ENGINE.md
git commit -m "feat: add interface contracts to DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE"
```

---

### Task 6: Meta-Systems (KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT)

**Files:**
- Modify: `FounderOS/KNOWLEDGE_EVOLUTION_ENGINE.md`
- Modify: `FounderOS/CONTINUOUS_IMPROVEMENT.md`

**KNOWLEDGE_EVOLUTION_ENGINE.md content:**
```
## Position in FounderHQ

KNOWLEDGE_EVOLUTION_ENGINE manages knowledge decay and revalidation. It is loaded during freshness checks or on request. It audits KNOWLEDGE.md entries by age and flags entries needing revalidation.

## Inputs
- `concepts/KNOWLEDGE.md` — all knowledge entries with timestamps
- `concepts/TIMELINE.md` — recent events that may invalidate old knowledge
- Freshness scan (WF-007) — age data from boot sequence

## Outputs
- Knowledge staleness report — entries exceeding revalidation thresholds
- Revalidation recommendations — which entries to verify, in priority order
- Archive recommendations — entries to move to historical reference

## Relations
- **KNOWLEDGE** — directly manages knowledge entry lifecycle
- **TIMELINE** — revalidation events recorded
- **WF-007** — triggered by freshness check workflow

## Workflow
```

**CONTINUOUS_IMPROVEMENT.md content:**
```
## Position in FounderHQ

CONTINUOUS_IMPROVEMENT manages meta-improvement of FounderOS itself. It is loaded periodically or on request to audit system health and recommend improvements.

## Inputs
- `FounderOS/SYSTEM_PROMPT.md` — current system architecture and rules
- `FounderOS/concepts/SYSTEM.md` — system governance rules
- `FounderOS/CONCEPT_AUDIT.md` — past audit findings
- `concepts/TIMELINE.md` — system changes and their outcomes

## Outputs
- Improvement recommendations — what to fix, in priority order
- System health report — architecture, consistency, gap analysis
- Audit triggers — when a full concept audit is needed

## Relations
- **AOS** — improvement recommendations executed via architecture changes
- **SYSTEM** — governance rules updated when system changes
- **CONCEPT_AUDIT** — audit findings recorded

## Workflow
```

- [ ] **Step 1: Edit KNOWLEDGE_EVOLUTION_ENGINE.md**
- [ ] **Step 2: Edit CONTINUOUS_IMPROVEMENT.md**
- [ ] **Step 3: Commit**

```bash
git add FounderOS/KNOWLEDGE_EVOLUTION_ENGINE.md FounderOS/CONTINUOUS_IMPROVEMENT.md
git commit -m "feat: add interface contracts to KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT"
```

---

### Task 7: Verification

- [ ] **Step 1: Check all 14 modules have new sections**

```bash
$modules = @("MOS.md","VEAOS.md","DAOS.md","CEOS.md","AI_VIDEO_MASTER_DOMAIN.md","ASTRA.md","RIOS.md","LEOS.md","FAOS.md","SOS.md","AOS.md","DECISION_ENGINE.md","PATTERN_ENGINE.md","PLAYBOOK_ENGINE.md","KNOWLEDGE_EVOLUTION_ENGINE.md","CONTINUOUS_IMPROVEMENT.md")
$missing = @()
foreach ($m in $modules) {
    $c = Get-Content -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\$m" -Raw
    if (-not ($c -match "## Position in FounderHQ")) { $missing += $m }
}
if ($missing.Count -eq 0) { Write-Output "ALL MODULES HAVE INTERFACE CONTRACTS" } else { Write-Output "MISSING: $($missing -join ', ')" }
```

- [ ] **Step 2: Check Inputs/Outputs present in all**

```bash
$missingIO = @()
foreach ($m in $modules) {
    $c = Get-Content -LiteralPath "C:\Users\junio\Desktop\FounderHQ\FounderOS\$m" -Raw
    if (-not ($c -match "## Inputs") -or -not ($c -match "## Outputs")) { $missingIO += $m }
}
if ($missingIO.Count -eq 0) { Write-Output "ALL MODULES HAVE INPUTS/OUTPUTS" } else { Write-Output "MISSING IO: $($missingIO -join ', ')" }
```

- [ ] **Step 3: Check original content preserved**

Spot-check 2-3 modules that had substantial original content (e.g., DAOS had Action Module Format, DIOS was already complete, CEOS had core protocol). Verify the original text exists within the Workflow section.

- [ ] **Step 4: Commit verification**

```bash
git add -A
git commit -m "verification: all 14 modules have interface contracts — Position, Inputs, Outputs, Relations, Workflow"
```
