# WORKFLOW

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 6.

## Role

Define repeatable execution procedures.

A workflow transforms an input into a desired output through a sequence of steps.

---

## Core Rule

A workflow contains step-by-step execution instructions.

A workflow does NOT contain strategy, reasoning, or domain knowledge.

Strategy belongs in PLAYBOOK.

Domain knowledge belongs in KNOWLEDGE.

---

## Structure

Each workflow must define:

**WORKFLOW_ID** — unique identifier

**NAME** — what this workflow is called

**TRIGGER** — what initiates this workflow

**INPUT** — what is needed before starting

**STEPS** — ordered list of actions, each with:
- Step description
- Expected output of the step
- Quality gate (what must be true before proceeding)

**OUTPUT** — what is produced

**RELATED_PLAYBOOK** — reference to the strategy this workflow implements (if applicable)

**RELATED_KNOWLEDGE** — reference to knowledge this workflow depends on (if applicable)

---

## Workflow: Video Production

**WORKFLOW_ID:** WF-001

**NAME:** TikTok Video Production

**TRIGGER:** A video concept has been approved for production

**INPUT:** Video concept (hook, problem, solution, CTA), product information, brand guidelines

**STEPS:**

1. **Choose audio/visual frame-1 disruptor** — Before writing any script, decide: What AUDIO (sound hit, scream, buzz, loud voice) plays at frame 0:00? What VISUAL (face zoom, sudden movement, camera shake, bright flash) appears at frame 0:00?
   - Output: Audio/Visual disruptor pair (e.g. "loud mosquito BUZZ sound + phone zoomed to mosquito on arm")
   - Quality gate: Both audio AND visual elements identified. Text is NOT the primary disruptor at frame 1.

2. **Script** — Write the script following the hook→problem→solution→proof→CTA structure. The hook uses the chosen audio/visual disruptor from step 1.
   - Output: Script text (~30s spoken)
   - Quality gate: Hook audio plays within first 1 second. Visual disruptor appears within first 1 second. Text overlay appears within first 2 seconds.

3. **Reference image** — Generate or select reference image that shows the visual disruptor
   - Output: 9:16 reference image
   - Quality gate: Image shows the frame-1 visual (not just product)

4. **Video generation** — Generate video clips using AI or capture real footage. Frame 1 must contain the visual disruptor.
   - Output: Raw video clip(s)
   - Quality gate: Frame 1 has the chosen visual disruptor. Duration matches script timing.

4. **Voiceover** — Generate or record voiceover audio
   - Output: Audio file synced to script
   - Quality gate: Audio matches script, tone is appropriate

5. **Assembly** — Combine video, voiceover, text overlay, and music
   - Output: Final video file
   - Quality gate: Text overlay is visible on mute, CTA includes WhatsApp number

6. **Publishing** — Upload to TikTok with caption, hashtags, cover image
   - Output: Published video
   - Quality gate: Video plays correctly on platform, link in bio is active

**OUTPUT:** Published TikTok video

**RELATED_PLAYBOOK:** None yet (see PLAYBOOK when created)

**RELATED_KNOWLEDGE:** KNOWLEDGE — Video Content Principles (hook structure, TikTok mechanics, Facebook vs TikTok, Offer Design)

---

## Workflow: Concept Audit

**WORKFLOW_ID:** WF-002

**NAME:** Concept Purity Audit

**TRIGGER:** A new concept is added, or quarterly audit cycle

**INPUT:** Concept file to audit, CONCEPT_BOUNDARIES.md

**STEPS:**

1. **Load boundaries** — Read CONCEPT_BOUNDARIES.md for the concept being audited
2. **Read concept** — Read the concept file completely
3. **Check for leaks** — Compare every line against the concept's boundaries:
   - Does this line belong to another concept?
   - Is this line operational data in a strategic concept?
   - Is this line analysis in a fact-only concept?
4. **Record violations** — For each leak found, record:
   - The line location
   - The owning concept
   - The correction needed
5. **Correct** — Move leaked content to the correct concept. Delete from the audited concept.
6. **Update CONCEPT_AUDIT.md** — Log all violations and corrections
7. **Verify** — Re-read the concept to confirm all leaks are removed

**OUTPUT:** Updated concept files, updated CONCEPT_AUDIT.md

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles (concept overlap prevention)

---

## Workflow: Session End

**WORKFLOW_ID:** WF-003

**NAME:** Session Shutdown

**TRIGGER:** Session is ending (founder indicates shutdown, disconnect detected, or timeout)

**INPUT:** Current session context, all concept files

**STEPS:**

1. **Review MEMORY** — Update priorities, concerns, blockers. Add recent decisions.
   - Quality gate: Every recent decision from this session is recorded
2. **Update TIMELINE** — Add entries for significant events this session
   - Quality gate: Each entry is a fact (what happened, not analysis)
3. **Check PROJECT.md** — Update any project status changes
   - Quality gate: Every active project has a NEXT_ACTION or is marked Blocked/Paused
4. **Check KNOWLEDGE** — If any lesson was validated, add it
   - Quality gate: New knowledge is distinct from existing entries
5. **Log session end** — Record session end in TIMELINE

**OUTPUT:** Updated concept files, continuity preserved for next session

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles (state over conversation)

---

## Workflow: AI Video Production (Entity-Based)

**WORKFLOW_ID:** WF-004

**NAME:** AI Video Production — Entity-Based Pipeline

**TRIGGER:** A video concept with defined entities has been approved for production

**INPUT:** Concept, entity registry, product sheet, brand guide

**STEPS:**

1. **Entity Sheet** — For each entity (character, product, environment), create or update an ENTITY_SHEET.md
   - Output: Entity sheet with GENERATION section (Tool, Prompt, Format, Ingredients)
   - Quality gate: All ENTITY_IDs referenced in prompts appear in Ingredients field (INGREDIENTS COMPLETENESS RULE)

2. **Environment Sheet** — Define the environment where action takes place
   - Output: ENVIRONMENT_SHEET.md with GENERATION section
   - Quality gate: Environment is consistent with entity sheets

3. **Scene Sheet** — Define the composition: entities + environment
   - Output: SCENE_SHEET.md with GENERATION section
   - Quality gate: All entities and environment are defined in previous sheets

4. **Action Sheet** — Define entity action in the scene
   - Output: ACTION_SHEET.md with GENERATION section
   - Quality gate: Action is consistent with entity capabilities

5. **Shot Sheet** — Frame the shot (camera angle, distance, focus)
   - Output: SHOT_SHEET.md with GENERATION section
   - Quality gate: Shot composition is achievable from scene

6. **PROPOSE** — Show proposed content + generation prompts to founder
   - Quality gate: Founder validates before proceeding

7. **CONFIRM** — Wait for explicit founder validation
   - Quality gate: No step skips this gate

8. **WRITE** — Persist all sheets to files only after confirmation

9. **Reference Image** — Generate or select 9:16 reference image
   - Quality gate: Image matches product appearance and setting

10. **Video Generation** — Generate clips using AI from validated prompts
    - Output: Raw video clip(s)
    - Quality gate: Duration matches script timing, visual quality acceptable

11. **Voiceover** — Generate or record TTS audio
    - Output: Audio file synced to script
    - Quality gate: Audio matches script, tone is appropriate

12. **Timing Map** — Capture shot-by-shot TIMING MAP (Shot #, Action, Start, End, Duration)
    - Output: TIMING_MAP.md
    - Quality gate: Enables TTS variations without guesswork

13. **Assembly** — Combine video, voiceover, text overlay, music
    - Output: Final video file
    - Quality gate: Text overlay visible on mute, CTA includes WhatsApp number

14. **Post-Production** — Log ALL modifications to raw assembly: text overlays (content, position, timing), music track, transitions, speed changes, color grading, platform effects
    - Output: POST_PRODUCTION section in production file
    - Quality gate: This section is the single source of truth for what viewers saw

15. **Publishing** — Upload to TikTok with caption, hashtags, cover
    - Output: Published video
    - Quality gate: Video plays correctly, link in bio is active

16. **Review** — Collect analytics after 24h, log lessons
    - Quality gate: Lessons are added to KNOWLEDGE before closing

**OUTPUT:** Published TikTok video with complete production trace

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** KNOWLEDGE — Video Content Principles, Pest Repeller Product Knowledge

---

## Workflow: Automation Definition

**WORKFLOW_ID:** WF-005

**NAME:** Automation Definition

**TRIGGER:** A recurring process is identified that could be automated

**INPUT:** Process description, trigger conditions, success criteria

**STEPS:**

1. **Define Trigger** — What initiates the automation
   - Quality gate: Trigger must be deterministic (time, event, or state change)

2. **Define Conditions** — What must be true for the automation to run
   - Quality gate: Conditions must be verifiable from file state

3. **Define Action** — What the automation does
   - Quality gate: Must be executable autonomously or with approval

4. **Classify Risk** — LOW (auto-execute): generate report, update registry, create summary
   - MEDIUM (prepare + request approval): create content, send notification
   - HIGH (escalate): delete files, publish content, send external communications
   - CRITICAL (stop, notify founder, await instruction): financial transactions

5. **Define Verification** — How to confirm the action succeeded
   - Quality gate: Verification must produce a measurable result

6. **Define Logging** — Record trigger, action, outcome in AUTOMATION_LOG.md
   - Quality gate: Every execution is traceable

**OUTPUT:** Documented automation with trigger → conditions → action → verification → logging

**ERROR HANDLING:** On failure, generate AUTOMATION_FAILURE_REPORT.md

**RELATED_PLAYBOOK:** None yet

**RELATED_KNOWLEDGE:** None yet

---

## Workflow: Event Processing

**WORKFLOW_ID:** WF-006

**NAME:** Event Processing

**TRIGGER:** An event is detected (state change, time trigger, external input)

**INPUT:** Raw event data

**STEPS:**

1. **Detect** — Identify that an event occurred
   - Quality gate: Event must have a clear SOURCE and TYPE

2. **Classify** — Assign EVENT_ID, TIMESTAMP, SOURCE, TYPE, PAYLOAD, PRIORITY (Low/Medium/High/Critical), STATUS
   - Quality gate: All fields populated before processing

3. **Route** — Send to appropriate handler based on TYPE (Decision Engine, Project Monitor, Knowledge Engine, etc.)
   - Quality gate: Handler exists and is ready

4. **Process** — Execute the handler's action on the event
   - Quality gate: Handler output is validated

5. **Log** — Record event and outcome in EVENT_LOG.md
   - Quality gate: Log is append-only

6. **Archive** — Move processed events to long-term storage
   - Quality gate: Archived events are retrievable by EVENT_ID

**OUTPUT:** Processed event with full audit trail

**OUTPUT:** Event processed from Detected → Queued → Processed → Logged → Archived

**ERROR HANDLING:** Unroutable events are logged with UNROUTABLE status and flagged for manual review

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles

---

**WORKFLOW_ID:** WF-007

**NAME:** Session Boot — Concept Freshness Check

**TRIGGER:** Every session start, after Boot Sequence (SYSTEM_PROMPT.md)

**INPUT:** Current date/time (Lomé UTC+0) + last-updated dates from all concept files

**STEPS:**

1. **Read system clock** — Get-Date, verify Lomé UTC+0
2. **Read last-updated dates** — Scan footers of: MEMORY.md, PROJECT.md, TIMELINE.md, KNOWLEDGE.md, ASSET.md, WORKFLOW.md, PLAYBOOK.md, CURRENT_STATE.md
3. **Compute age** — For each file: age = current_date - last_updated_date
4. **Flag stale concepts** — For each file exceeding its max age:
   - MEMORY.md > 1 session → FLAG
   - CURRENT_STATE.md > 1 session → FLAG
   - PROJECT.md > 7 days → FLAG
   - KNOWLEDGE.md > 14 days → FLAG
   - TIMELINE.md > 14 days → FLAG
   - ASSET.md > 30 days → FLAG
   - WORKFLOW.md > 30 days → FLAG
   - PLAYBOOK.md > 30 days → FLAG
5. **Report** — Generate concise freshness report: "MEMORY: 2 days (STALE). PROJECT: 2 days (OK). All others fresh."
6. **Prompt update** — If any concept is flagged, recommend update before proceeding with session goals

**OUTPUT:** Freshness report displayed to founder. Stale concepts flagged before any action.

**ERROR HANDLING:** If a file has no "Last updated" field, treat as maximally stale (> 90 days). If file cannot be read, flag as MISSING and consult SOURCE_OF_TRUTH.md for expected location.

---

**WORKFLOW_ID:** WF-008

**NAME:** Cold Reboot Protocol

**TRIGGER:** User says "reboot" or "applique" in any message

**INPUT:** Current session context (stale) + files on disk (fresh) + git history

**STEPS:**

1. **Freeze context** — Announce: "Rebooting — applying OS updates." Note current action to resume later if needed.

2. **Git change scan** — Run:
   ```
   git log --oneline -5
   git diff HEAD~1 --name-only
   ```
   If `git` not found: `git init` in FounderHQ root, then `git add . && git commit -m "founderos: initial state"`, then proceed to step 4 (full re-read).

3. **Identify changed files** — Parse `git diff HEAD~1 --name-only` output. Match against known concept files: `concepts/MEMORY.md`, `concepts/PROJECT.md`, `concepts/TIMELINE.md`, `concepts/ASSET.md`, `State/CURRENT_STATE.md`, `concepts/WORKFLOW.md`, `concepts/PLAYBOOK.md`, `concepts/KNOWLEDGE.md`.

4. **Re-read modified files** — Read each file identified in step 3. If no git history (first commit just made or fallback), re-read all active concept files from step 3's list.

5. **Detect deltas** — Compare new content against remembered old content. For each file, list what changed:
   ```
   Δ MEMORY — Priorities changed: old → new
   Δ PROJECT — Added: DM-001. FO-001 → Completed.
   ```

6. **Rebuild world model** — Synthesize: what exists, what matters, what changed, what's blocked, what's emerging, what should happen next. If deltas contradict each other (e.g., two files disagree on cash), flag the contradiction.

7. **Verify consistency** — File version wins over session memory. If a contradiction is found, report: "⚠️ Contradiction detected: MEMORY says X, CURRENT_STATE says Y. Using CURRENT_STATE (file wins)."

8. **Report awareness** — Output:
   ```
   Reboot complete. 3 files re-loaded.

   Δ MEMORY — priorities updated
   Δ PROJECT — DM-001 added, FO-001 completed
   Δ ASSET — A-009, A-010, A-011 added

   World model: SURVIVAL mode. Cash 1,118 FCFA. Top priority: call soya suppliers. No contradictions.

   Recommended next action: Call Ste SODJA (96 68 43 65) to confirm price and delivery terms.
   ```

**OUTPUT:** Fresh world model applied to session. Delta report displayed.

**ERROR HANDLING:**
- `git` not found → `git init`, first commit, full re-read. If user declines git init, use full re-read without git.
- File modified but unreadable → Use old in-memory version, flag as ERROR.
- Contradiction between old and new state → File version wins, flag contradiction.
- Reboot during active workflow → Complete current step first, defer reboot to next natural break.

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles, TEMPORAL_AWARENESS.md

---

## Footer

Last updated: 2026-06-20 (added: WF-007 Session Boot Freshness Check, WF-008 Cold Reboot Protocol)

Workflows are living documents.

If a workflow step becomes outdated, update it.

If a workflow is never used, archive it.

If a new recurring process emerges, create a workflow for it.
