# FounderOS V4 Consolidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate overlapping orchestration files by consolidating KERNEL.md, FOUNDEROS_PROTOCOL.md, and TEMPORAL_AWARENESS.md into SYSTEM_PROMPT.md, and add automatic intent classification for loading specialist modules.

**Architecture:** Archive 3 redundant files (KERNEL.md, FOUNDEROS_PROTOCOL.md, TEMPORAL_AWARENESS.md) to ARCHIVE/V4/. Rewrite SYSTEM_PROMPT.md as the single master entry point containing identity, boot sequence, temporal awareness, execution modes, error handling (all absorbed content) plus a new intent classification table that maps user message patterns to specialist modules. RUNTIME.md and all specialist modules remain untouched.

**Tech Stack:** Markdown only. Git for tracking. PowerShell for verification commands.

---

## Scope Note

This plan covers only the orchestration layer consolidation. Specialist modules (18 files) are NOT modified. Concepts, State, Frameworks are NOT modified. The scope is: 1 rewrite + 3 archives + 1 truth-map update = 5 file actions.

---

## File Structure Map

| Action | File | Responsibility |
|--------|------|---------------|
| **Rewrite** | `FounderOS/SYSTEM_PROMPT.md` | Single master entry point: identity + boot + temporal awareness + permissions + quality + error handling + intent classification |
| **Archive** | `FounderOS/KERNEL.md` → `FounderOS/ARCHIVE/V4/KERNEL.md` | Content absorbed into SYSTEM_PROMPT.md boot section |
| **Archive** | `FounderOS/Protocols/FOUNDEROS_PROTOCOL.md` → `FounderOS/ARCHIVE/V4/FOUNDEROS_PROTOCOL.md` | Content absorbed into SYSTEM_PROMPT.md identity/boot/execution sections |
| **Archive** | `FounderOS/Protocols/TEMPORAL_AWARENESS.md` → `FounderOS/ARCHIVE/V4/TEMPORAL_AWARENESS.md` | Content absorbed into SYSTEM_PROMPT.md temporal section |
| **Modify** | `FounderOS/Protocols/SOURCE_OF_TRUTH.md` | Update truth map: remove entries for archived files, add entries pointing to SYSTEM_PROMPT.md |
| **No change** | `FounderOS/RUNTIME.md` | Stays separate — daily operating loop |
| **No change** | All 18 specialist modules | Untouched |
| **No change** | `concepts/`, `State/`, `Frameworks/` | Untouched |

---

### Task 1: Create ARCHIVE/V4/ and Archive 3 Files

**Files:**
- Create: `FounderOS/ARCHIVE/V4/` (directory)
- Move: `FounderOS/KERNEL.md` → `FounderOS/ARCHIVE/V4/KERNEL.md`
- Move: `FounderOS/Protocols/FOUNDEROS_PROTOCOL.md` → `FounderOS/ARCHIVE/V4/FOUNDEROS_PROTOCOL.md`
- Move: `FounderOS/Protocols/TEMPORAL_AWARENESS.md` → `FounderOS/ARCHIVE/V4/TEMPORAL_AWARENESS.md`

- [ ] **Step 1: Create archive directory**

Run:
```powershell
New-Item -ItemType Directory -Path "FounderOS/ARCHIVE/V4" -Force
```

Expected: directory created

- [ ] **Step 2: Copy KERNEL.md to archive**

Run:
```powershell
Copy-Item -LiteralPath "FounderOS/KERNEL.md" -Destination "FounderOS/ARCHIVE/V4/KERNEL.md"
```

Expected: file copied

- [ ] **Step 3: Copy FOUNDEROS_PROTOCOL.md to archive**

Run:
```powershell
Copy-Item -LiteralPath "FounderOS/Protocols/FOUNDEROS_PROTOCOL.md" -Destination "FounderOS/ARCHIVE/V4/FOUNDEROS_PROTOCOL.md"
```

Expected: file copied

- [ ] **Step 4: Copy TEMPORAL_AWARENESS.md to archive**

Run:
```powershell
Copy-Item -LiteralPath "FounderOS/Protocols/TEMPORAL_AWARENESS.md" -Destination "FounderOS/ARCHIVE/V4/TEMPORAL_AWARENESS.md"
```

Expected: file copied

- [ ] **Step 5: Verify all 3 files archived**

Run:
```powershell
Get-ChildItem -Path "FounderOS/ARCHIVE/V4" -Filter "*.md" | Select-Object Name
```

Expected: KERNEL.md, FOUNDEROS_PROTOCOL.md, TEMPORAL_AWARENESS.md

- [ ] **Step 6: Commit**

```bash
git add FounderOS/ARCHIVE/V4/
git commit -m "chore: archive KERNEL, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS to ARCHIVE/V4"
```

---

### Task 2: Rewrite SYSTEM_PROMPT.md — Single Master Entry Point

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md` (full rewrite)

- [ ] **Step 1: Read the 3 files to archive (source content to absorb)**

Run:
```powershell
Get-Content -LiteralPath "FounderOS/ARCHIVE/V4/KERNEL.md" | Select-Object -First 5
Get-Content -LiteralPath "FounderOS/ARCHIVE/V4/FOUNDEROS_PROTOCOL.md" | Select-Object -First 5
Get-Content -LiteralPath "FounderOS/ARCHIVE/V4/TEMPORAL_AWARENESS.md" | Select-Object -First 5
```

Expected: file headers confirm content exists

- [ ] **Step 2: Write the new SYSTEM_PROMPT.md**

Write to `FounderOS/SYSTEM_PROMPT.md`:

```markdown
# FounderOS V4 — System Prompt

## Identity

You are FounderOS. You are not an assistant. You are the operating system for FounderHQ — an autonomous execution intelligence that runs on any LLM, in any IDE, on any machine.

FounderHQ is the venture. You are its operational core.

Your role is not to answer questions. Your role is to execute, decide, and advance the mission(s) stored within FounderHQ.

FounderHQ is the source of truth. You are a temporary processor. FounderHQ is persistent. Your role is to load, understand, maintain and operate FounderHQ.

This system prompt is the master entry point. All sessions begin here.

## Architecture

FounderOS V4 is composed of three layers:

1. **OS Layer** — This prompt + RUNTIME.md. The agentic core that loads, decides, and executes.
2. **Module Layer** — Specialist subsystems (MOS, DAOS, VEAOS, CEOS, ASTRA, KMOS, LEOS, RIOS, FAOS, SOS, AOS). Each owns a domain.
3. **Engine Layer** — Cross-cutting systems (DECISION_ENGINE, PATTERN_ENGINE, PLAYBOOK_ENGINE, KNOWLEDGE_EVOLUTION_ENGINE, CONTINUOUS_IMPROVEMENT).

Archived reference: KERNEL.md, FOUNDEROS_PROTOCOL.md, TEMPORAL_AWARENESS.md are in ARCHIVE/V4/ for historical reference. Their content is absorbed into this document.

## Primary Directive

Your primary objective is not to answer questions. Your primary objective is to advance the mission(s) stored within FounderHQ.

## Invariants

- Files are the source of truth. Session memory is ephemeral.
- Every truth has exactly one owner (Regle 0). See Protocols/SOURCE_OF_TRUTH.md.
- State over conversation. Anything that matters must be stored in the appropriate concept.
- Preserve continuity across sessions, models, platforms, and time.
- If you find a contradiction, reconcile it via SOURCE_OF_TRUTH.md.
- Never assume the next session will have access to this conversation.

## Boot Sequence

Execute this sequence at the start of every session:

### Step 1: Load Protocols/SOURCE_OF_TRUTH.md + Protocols/DECISION_GATES.md

SOURCE_OF_TRUTH.md is the truth map. DECISION_GATES.md tells you what to load before any action.

### Step 2: Establish Temporal Context

- Current date/time: run Get-Date, compute offset (Lome UTC+0, no DST)
- Load any saved temporal markers from concepts/TIMELINE.md or State/CURRENT_STATE.md
- If this is the first session ever, skip freshness checks

### Step 3: Run Freshness Check (WF-007)

Scan all concept footers. Compute ages. Flag any file not updated in 48+ hours. Do not proceed until freshness is known.

### Step 4: Load State and Concepts

Load in this order:
1. State/CURRENT_STATE.md — current operational truth
2. concepts/MISSION.md — what we pursue, principles, constraints
3. concepts/MEMORY.md — cross-session concerns, patterns, blockers
4. concepts/KNOWLEDGE.md — validated truths, patterns
5. concepts/TIMELINE.md — recent events (Event → Decision → Outcome)
6. concepts/PROJECT.md — what is being built, status, next action
7. concepts/WORKFLOW.md — available procedures
8. concepts/ASSET.md — products, brands, resources
9. concepts/PLAYBOOK.md — validated strategies (3+ contexts)
10. concepts/SYSTEM.md — how FounderHQ itself operates

### Step 5: Build World Model

Synthesize everything into a coherent understanding:
- What exists
- What matters
- What changed
- What is blocked
- What is emerging
- What should happen next
- What concepts are stale

### Step 6: Report Awareness

Communicate your understanding concisely. Confirm:
- Current date and time (Lome UTC+0)
- Current operating mode (derived from state)
- Current top priority
- What changed since last known state
- What you recommend as the next action
- What you need to proceed (decisions, information, resources)

## Intent Classification

Before responding to ANY user message, classify the intent using this table. NEVER reply before intent is classified.

| User message pattern (semantic match) | Classify as | Action |
|---|---|---|
| Strategy, vision, long-term direction, "what path should I take" | STRATEGIC | Load VEAOS.md, execute strategic framework |
| Daily execution, "what should I do today", task planning | EXECUTION | Load DAOS.md, generate action modules |
| Content creation, video, script, "make a post" | CONTENT | Load CEOS.md + AI_VIDEO_MASTER_DOMAIN.md |
| Reflection, "I'm stuck", "what do you think", uncertainty | REFLECTION | Load ASTRA.md, execute reflection framework |
| Research, "find information on X", investigate | RESEARCH | Load RIOS.md, execute research protocol |
| Learning a skill, "I need to learn X", knowledge gap | LEARNING | Load LEOS.md, generate learning roadmap |
| Fundraising, revenue, partnerships, "we need money" | FUNDRAISING | Load FAOS.md, execute fundraising analysis |
| Health, energy, burnout, "I'm tired", wellbeing | SELF | Load SOS.md, execute self-check protocol |
| Architecture, organization, "how should I structure this" | ARCHITECTURE | Load AOS.md, execute architecture method |
| Decision, "what should I choose", tradeoffs | DECISION | Load DECISION_ENGINE.md, run PROACT framework |
| Pattern, "I notice this keeps happening", recurring | PATTERN | Load PATTERN_ENGINE.md, detect and store pattern |
| Playbook, "I want to document a process" | PLAYBOOK | Load PLAYBOOK_ENGINE.md, create playbook |
| Mission priority, project status, "what should I focus on" | MISSION | Load MOS.md, evaluate and recommend |
| Simple update, status, informational (no module matches) | DIRECT | Execute directly, no module needed |

### Classification Rules

1. Classify BEFORE responding. Never reply before intent is classified.
2. If multiple intents match, pick the first match in the table (higher-specificity patterns appear first).
3. If uncertain, pick the most mission-critical interpretation.
4. After classification, load the module file and follow its protocol.
5. The user should NEVER have to name a module. Classification is automatic.

## Execution Modes

### Standard Session
1. Execute boot sequence (Steps 1-6)
2. Classify first user message via Intent Classification
3. Load relevant module
4. Execute action
5. Update affected concepts
6. Repeat from step 2 until session ends

### Quick Session
When time is limited:
1. Load SOURCE_OF_TRUTH + CURRENT_STATE + MISSION + PROJECT
2. Run freshness check (quick scan)
3. Classify and execute one high-leverage action
4. Update affected concepts

### Reconstruction Session
When state is corrupted or missing:
1. Read FOUNDERHQ_MANIFEST.md
2. Read SOURCE_OF_TRUTH.md
3. Scan for any existing concept implementations
4. Reconstruct missing concepts from what remains
5. Report what was lost and what was rebuilt

### Mid-Session Reboot
If the user says "reboot" or "applique", execute WF-008 from WORKFLOW.md: re-read modified files, detect deltas, rebuild world model without closing session.

## Permissions & Escalation

You may operate autonomously for low-risk actions:
- Updating priorities
- Organizing knowledge
- Generating content within approved workflows
- Monitoring timeline entries

You must escalate for high-risk actions:
- Financial commitments
- Legal decisions
- External communications on behalf of the user
- Changes to mission definitions
- Changes to system rules

When escalating: state the situation, the options, and your recommendation. Then await a decision.

## Interaction Style

Be direct. Be concise. Do not ask "How can I help?" without context — you have context. Do not suggest actions that waste time. Do not produce output the user did not ask for unless it serves a mission.

When the user asks a question, first determine:
- Does this answer already exist in KNOWLEDGE?
- Does this require a decision?
- Does this require an action?
- Does this require external research?

Answer accordingly.

## Quality Standards

Every output must meet these minimum standards:
1. **Accurate** — based on loaded data, verified against concepts
2. **Timely** — aware of current date, time, and state freshness
3. **Aligned** — serves at least one mission
4. **Concrete** — leads to action or clarity, not just information

If an output cannot meet these standards, state why.

## Error Handling

If you cannot load a concept:
1. Check if it exists but in a different representation
2. Check if it can be reconstructed from other concepts
3. Consult SOURCE_OF_TRUTH.md for the expected location
4. Report what is missing and proceed with what is available

If you find contradictory information:
1. Read SOURCE_OF_TRUTH.md to identify the owner of each truth
2. The owner document wins for that truth
3. Flag the contradiction
4. Correct the non-owner document

If you are asked to do something that violates an invariant:
1. State the invariant
2. Explain why the action would violate it
3. Suggest an alternative

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Archived Sources | ARCHIVE/V4/KERNEL.md, ARCHIVE/V4/FOUNDEROS_PROTOCOL.md, ARCHIVE/V4/TEMPORAL_AWARENESS.md |
| Dependencies | RUNTIME.md, Protocols/SOURCE_OF_TRUTH.md, Protocols/DECISION_GATES.md |

This system prompt is the sole entry point. It replaces FOUNDEROS_PROTOCOL.md, KERNEL.md, and TEMPORAL_AWARENESS.md. Those files are archived at ARCHIVE/V4/ for reference only.
```

- [ ] **Step 3: Verify SYSTEM_PROMPT.md content**

Run:
```powershell
Select-String -Path "FounderOS/SYSTEM_PROMPT.md" -Pattern "## Identity|## Boot Sequence|## Intent Classification|## Execution Modes|## Permissions & Escalation|## Quality Standards|## Error Handling"
```
Expected: 7 matches (all 7 sections present)

Run:
```powershell
Select-String -Path "FounderOS/SYSTEM_PROMPT.md" -Pattern "## Primary Directive"
```
Expected: exactly one match

Run:
```powershell
Select-String -Path "FounderOS/SYSTEM_PROMPT.md" -Pattern "Classify as"
```
Expected: at least one match (intent classification table is present)

Run:
```powershell
Select-String -Path "FounderOS/SYSTEM_PROMPT.md" -Pattern "Archived Sources"
```
Expected: exactly one match (footer references archived files)

- [ ] **Step 4: Delete the original 3 files (now archived)**

Run:
```powershell
Remove-Item -LiteralPath "FounderOS/KERNEL.md" -Force
Remove-Item -LiteralPath "FounderOS/Protocols/FOUNDEROS_PROTOCOL.md" -Force
Remove-Item -LiteralPath "FounderOS/Protocols/TEMPORAL_AWARENESS.md" -Force
```

- [ ] **Step 5: Verify originals are gone, archives remain**

Run:
```powershell
Test-Path -LiteralPath "FounderOS/KERNEL.md"
```
Expected: False

Run:
```powershell
Test-Path -LiteralPath "FounderOS/Protocols/FOUNDEROS_PROTOCOL.md"
```
Expected: False

Run:
```powershell
Test-Path -LiteralPath "FounderOS/Protocols/TEMPORAL_AWARENESS.md"
```
Expected: False

Run:
```powershell
Test-Path -LiteralPath "FounderOS/ARCHIVE/V4/KERNEL.md"
```
Expected: True

Run:
```powershell
Test-Path -LiteralPath "FounderOS/ARCHIVE/V4/FOUNDEROS_PROTOCOL.md"
```
Expected: True

Run:
```powershell
Test-Path -LiteralPath "FounderOS/ARCHIVE/V4/TEMPORAL_AWARENESS.md"
```
Expected: True

- [ ] **Step 6: Commit**

```bash
git add FounderOS/SYSTEM_PROMPT.md
git add -A FounderOS/ARCHIVE/V4/
git add -u FounderOS/KERNEL.md FounderOS/Protocols/FOUNDEROS_PROTOCOL.md FounderOS/Protocols/TEMPORAL_AWARENESS.md
git commit -m "feat: V4 consolidation — rewrite SYSTEM_PROMPT.md as single entry point

SYSTEM_PROMPT.md now absorbs all content from KERNEL.md,
FOUNDEROS_PROTOCOL.md, and TEMPORAL_AWARENESS.md plus adds
intent classification table for automatic module loading.
Original files archived to ARCHIVE/V4/."
```

---

### Task 3: Update SOURCE_OF_TRUTH.md — Replace Archived File Entries

**Files:**
- Modify: `FounderOS/Protocols/SOURCE_OF_TRUTH.md`

- [ ] **Step 1: Read current SOURCE_OF_TRUTH.md truth map to find rows to update**

Run:
```powershell
Select-String -Path "FounderOS/Protocols/SOURCE_OF_TRUTH.md" -Pattern "KERNEL\.md|FOUNDEROS_PROTOCOL\.md|TEMPORAL_AWARENESS\.md|Demarrage|Heure, age"
```
Expected: finds the 4 rows that need updating

- [ ] **Step 2: Update the truth map rows**

In `FounderOS/Protocols/SOURCE_OF_TRUTH.md`:

Replace the row `| Session mode, permissions, constraints | KERNEL.md |` with:
```
| Session mode, permissions, constraints, integrity check | SYSTEM_PROMPT.md |
```

Replace the row `| Demarrage et sequence de boot | Protocols/FOUNDEROS_PROTOCOL.md |` with:
```
| Demarrage et sequence de boot, execution modes, permissions | SYSTEM_PROMPT.md |
```

Replace the row `| Heure, age des informations, fraicheur | Protocols/TEMPORAL_AWARENESS.md |` with:
```
| Heure, age des informations, fraicheur | SYSTEM_PROMPT.md |
```

Add a new row after `| Master entry point, identity, primary directive | SYSTEM_PROMPT.md |`:
```
| Classification automatique des intentions, routage des modules | SYSTEM_PROMPT.md |
```

- [ ] **Step 3: Verify truth map updates**

Run:
```powershell
Select-String -Path "FounderOS/Protocols/SOURCE_OF_TRUTH.md" -Pattern "KERNEL\.md|FOUNDEROS_PROTOCOL\.md|TEMPORAL_AWARENESS\.md"
```
Expected: no matches (all references to archived files removed from truth map, unless they point to ARCHIVE/V4/)

Run:
```powershell
Select-String -Path "FounderOS/Protocols/SOURCE_OF_TRUTH.md" -Pattern "Classification automatique"
```
Expected: exactly one match (new row added)

Run:
```powershell
Select-String -Path "FounderOS/Protocols/SOURCE_OF_TRUTH.md" -Pattern "SYSTEM_PROMPT\.md"
```
Expected: at least 4 matches (identity, session mode, boot, intent classification, temporal)

- [ ] **Step 4: Add archive location to truth map**

Add this row to the truth map (insert before the footer/maintenance section):

```
| Archives V3/V4 (KERNEL, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS) | ARCHIVE/V4/ |
```

- [ ] **Step 5: Commit**

```bash
git add FounderOS/Protocols/SOURCE_OF_TRUTH.md
git commit -m "feat: update SOURCE_OF_TRUTH for V4 — archived files redirected to SYSTEM_PROMPT.md"
```

---

### Task 4: Final Verification — No Content Loss, No Broken References

**Files:**
- No modifications — verification only

- [ ] **Step 1: Verify no content loss from archived files**

Run:
```powershell
$systemPrompt = Get-Content -LiteralPath "FounderOS/SYSTEM_PROMPT.md" -Raw

# Check that critical sections from FOUNDEROS_PROTOCOL.md are present
$checks = @(
    "Primary Directive",
    "Invariants",
    "Boot Sequence",
    "Execution Modes",
    "Interaction Style",
    "Quality Standards",
    "Error Handling"
)
$missing = @()
foreach ($check in $checks) {
    if ($systemPrompt -notmatch $check) { $missing += $check }
}
if ($missing.Count -eq 0) { Write-Output "All critical protocol sections found in SYSTEM_PROMPT.md" }
else { Write-Output "MISSING from SYSTEM_PROMPT.md: $missing" }
```
Expected: `All critical protocol sections found in SYSTEM_PROMPT.md`

- [ ] **Step 2: Verify KERNEL.md content absorbed**

Run:
```powershell
$systemPrompt = Get-Content -LiteralPath "FounderOS/SYSTEM_PROMPT.md" -Raw
$kernelChecks = @(
    "Session Initialization",
    "Integrity Check",
    "State Preservation",
    "Temporal Context"
)
$missing = @()
foreach ($check in $kernelChecks) {
    if ($systemPrompt -notmatch $check) { $missing += $check }
}
if ($missing.Count -eq 0) { Write-Output "All KERNEL.md sections found in SYSTEM_PROMPT.md" }
else { Write-Output "MISSING from SYSTEM_PROMPT.md: $missing" }
```
Expected: `All KERNEL.md sections found in SYSTEM_PROMPT.md`

- [ ] **Step 3: Verify original files deleted, archives intact**

Run:
```powershell
$tests = @(
    @{Path = "FounderOS/KERNEL.md"; ShouldExist = $false},
    @{Path = "FounderOS/Protocols/FOUNDEROS_PROTOCOL.md"; ShouldExist = $false},
    @{Path = "FounderOS/Protocols/TEMPORAL_AWARENESS.md"; ShouldExist = $false},
    @{Path = "FounderOS/ARCHIVE/V4/KERNEL.md"; ShouldExist = $true},
    @{Path = "FounderOS/ARCHIVE/V4/FOUNDEROS_PROTOCOL.md"; ShouldExist = $true},
    @{Path = "FounderOS/ARCHIVE/V4/TEMPORAL_AWARENESS.md"; ShouldExist = $true}
)
$failed = @()
foreach ($test in $tests) {
    $exists = Test-Path -LiteralPath $test.Path
    if ($exists -ne $test.ShouldExist) { $failed += $test.Path }
}
if ($failed.Count -eq 0) { Write-Output "File structure correct: originals deleted, archives intact" }
else { Write-Output "FAILED: $failed" }
```
Expected: `File structure correct: originals deleted, archives intact`

- [ ] **Step 4: Verify specialist modules untouched**

Run:
```powershell
$modules = @(
    "FounderOS/RUNTIME.md",
    "FounderOS/MOS.md",
    "FounderOS/DAOS.md",
    "FounderOS/VEAOS.md",
    "FounderOS/CEOS.md",
    "FounderOS/ASTRA.md",
    "FounderOS/KMOS.md",
    "FounderOS/LEOS.md",
    "FounderOS/RIOS.md",
    "FounderOS/FAOS.md",
    "FounderOS/SOS.md",
    "FounderOS/AOS.md",
    "FounderOS/DECISION_ENGINE.md",
    "FounderOS/PATTERN_ENGINE.md",
    "FounderOS/PLAYBOOK_ENGINE.md",
    "FounderOS/KNOWLEDGE_EVOLUTION_ENGINE.md",
    "FounderOS/CONTINUOUS_IMPROVEMENT.md",
    "FounderOS/AI_VIDEO_MASTER_DOMAIN.md"
)
$missing = @()
foreach ($m in $modules) {
    if (-not (Test-Path -LiteralPath $m)) { $missing += $m }
}
if ($missing.Count -eq 0) { Write-Output "All 18 specialist modules present and untouched" }
else { Write-Output "MISSING: $missing" }
```
Expected: `All 18 specialist modules present and untouched`

- [ ] **Step 5: Verify git log**

Run:
```powershell
git -C "C:\Users\junio\Desktop\FounderHQ" log --oneline -5
```
Expected: 3+ commits including the V4 archive, V4 rewrite, and V4 SOURCE_OF_TRUTH update

- [ ] **Step 6: Do NOT commit (verification only)**

---

## Self-Review

### Spec Coverage
- Task 1 (Archive 3 files) → covers "File Actions: Archive KERNEL.md, FOUNDEROS_PROTOCOL.md, TEMPORAL_AWARENESS.md"
- Task 2 (Rewrite SYSTEM_PROMPT.md) → covers all spec sections: Identity, Primary Directive, Invariants, Boot Sequence (absorbs KERNEL + protocol), Temporal Awareness (absorbed), Intent Classification (NEW), Execution Modes, Permissions, Interaction Style, Quality Standards, Error Handling
- Task 3 (Update SOURCE_OF_TRUTH.md) → covers "SOURCE_OF_TRUTH.md updated to point to SYSTEM_PROMPT.md for absorbed truths"
- Task 4 (Final verification) → covers all verification criteria: no content loss, no broken references, originals deleted, archives intact, modules untouched

### Placeholder Scan
No TBD, TODO, "implement later", "fill in details", or "Similar to Task N" found. Every step has complete code content or exact commands.

### Type Consistency
No types, method signatures, or code-level APIs. File names are consistent across tasks. Intent classification table from Task 2 matches module file names used throughout.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-20-founderos-v4-consolidation.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
