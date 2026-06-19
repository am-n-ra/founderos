# QUALITY_GATES V1

## Purpose
FounderOS must not confuse activity with progress. No workflow may advance to next phase until all required gates pass.

## Prime Directive
If a gate fails: STOP. Identify missing assets. Generate remediation plan. Continue only after correction.

## Gate Structure
Every gate: Objective, Required Assets, Validation Criteria, Pass Condition, Fail Condition.

---

## GLOBAL GATES

### Mission Alignment
Does this contribute to the mission? Pass: Directly/indirectly contributes or removes constraints. Fail: No mission connection.

### Context Completeness
Do we have enough information? Required: Objective defined, outcome defined, constraints known, success criteria known.

---

## VIDEO AD GATES

### Gate 1 — Offer Validation
Required: OFFER.md, CUSTOMER_PROFILE.md, PROBLEM_STATEMENT.md. Pass: Pain identified, audience identified, value proposition clear, GENERATION section present (LLM prompt). Validated by founder before writing.

### Gate 2 — Creative Strategy
Required: CREATIVE_STRATEGY.md. Pass: Hook defined, emotion defined, desired action defined, angle defined, GENERATION section present (LLM prompt). Validated by founder before writing.

### Gate 3 — Script Completion
Required: SCRIPT.md. Pass: Beginning, middle, end, CTA, GENERATION section present (LLM prompt). Validated by founder before writing.

### Gate 4 — Entity Registry
Required: ENTITY_REGISTRY.md (lists all entities with ENTITY_ID, TYPE, NAME). Pass: All video entities registered with unique IDs, GENERATION section present (LLM prompt). Validated by founder before writing.

### Gate 5 — Entity Sheets
Required: For each entity in registry, corresponding sheet exists (PERSON_SHEET, PRODUCT_SHEET, LOCATION_SHEET, etc.). Pass: Multi-angle turnaround (face + 3/4 + profile or equivalent), neutral background, GENERATION section present (Tool + Prompt + Format + Ingredients).

### Gate 5.5 — Environment Sheets
Required: ENVIRONMENT_SHEET.md per environment. Pass: Neutral state (empty, no characters), color palette, camera style, atmosphere defined, GENERATION section present (Tool + Prompt + Format + Ingredients), POSITIONAL LAYOUT section present (spatial positions, heights, distances).

### Gate 6 — Entity Consistency
Required: Entity sheets consistency lock (identical across all scenes). Pass: Same entity appears identically in all scenes.

### Gate 6.5 — Narrative Arc
Required: List of actions derived from the script. Pass: Arc is complete — Problem presented → False solution attempted → Real solution applied → Resolution visible (the problem disappears). Fail: The story starts but does not finish (e.g. solution without resolution).

### Gate 7 — Action Sheets
Required: ACTION_SHEET.md per action (references ENTITY_IDs). Pass: Action defined, actor identified (MUST be a valid ENTITY_ID, not a bare description), movement described, emotion defined, duration set, GENERATION section present (Tool + Prompt + Format + Ingredients). Ingredients MUST include all ENTITY_IDs referenced in the Prompt. Le set d'actions couvre chaque étape de l'arc: au moins 1 action pour Problem, 1 pour False solution, 1 pour Real solution, 1 pour Resolution.

### Gate 8 — Scene Sheets
Required: SCENE_SHEET.md per scene (assembles entities + action). Pass: Entities listed, action assigned, mood defined, camera style defined, GENERATION section present (Tool = LLM, references existing action sheet images, NOT a new NanoBanana Pro prompt). Ingredients include action sheet images.

### Gate 9 — Shot Sheets
Required: SHOT_SHEETS per scene (camera angle, duration, specific action). Pass: Each shot has defined angle, duration, parent scene, GENERATION section present (Tool = LLM, text synthesis, NOT a new NanoBanana Pro prompt). References scene sheet + action sheet images.

### Gate 10 — Start Frame
Required: START_FRAME per shot if the shot needs a distinct visual from the ACTION_SHEET. Pass: If present, all shot entities visible, composition matches shot sheet, GENERATION section present (NanoBanana Pro prompt). If absent, verify that existing ACTION_SHEET image serves as START_FRAME.

### Gate 11 — End Frame
Required: END_FRAME per shot if the shot ends in a different state than it starts. Pass: If present, problem/solution state visible, consistency preserved, GENERATION section present (NanoBanana Pro prompt). If absent, END_FRAME = START_FRAME or ACTION_SHEET image.

### Gate 12 — Video Prompt
Required: VIDEO_PROMPT.md (references entity sheets, shot sheets, scene sheets, start/end frames; describes motion/camera/timing). Pass: Prompt approved, GENERATION section present (LLM prompt). Validated by founder before generation.

### Gate 13 — Video Generation
Required: Generated clips. Pass: Entity consistency, narrative consistency, visual quality. Fail: Regenerate.

### Gate 14 — Publishing
Required: Final video + TTS + overlay text + music + METADATA (title, caption, hashtags) + TIMING MAP (shot-by-shot timing) + POST_PRODUCTION log (all overlay text, effects, music track, captions, modifications added during editing). Pass: Video complete, metadata includes platform-appropriate title, caption with CTA, hashtags. TIMING MAP present with every shot's start/end time. POST_PRODUCTION log captures every modification made between ASSEMBLY output and PUBLISHED video. Validated by founder before posting.

---

## ECOMMERCE GATES

### Product Validation
Required: WINNING_PRODUCT.md. Pass: Demand exists, audience exists, distribution possible, content angles exist, margin acceptable. Fail: Reject product.

---

## RESEARCH GATES

### Literature Gate
Required: RESEARCH_REPORT.md. Pass: Relevant sources, recent sources, knowledge extracted.

### Experiment Gate
Required: HYPOTHESIS.md, EXPERIMENT_PLAN.md. Pass: Hypothesis testable, metrics defined, success criteria defined.

---

## SOFTWARE GATES

### Requirements Gate
Required: PRODUCT_SPEC.md. Pass: Problem defined, users defined, requirements defined, success metrics defined.

### Architecture Gate
Required: ARCHITECTURE.md. Pass: Components identified, dependencies identified, risks identified.

### MVP Gate
Required: Working MVP. Pass: Core functionality works, critical bugs absent, deployment possible.

---

## TIMESTAMP FRESHNESS GATE
Every response MUST start with a freshly-executed timestamp header. If timestamp is missing, stale, or copied from a previous response: the response is a system failure. Run `(Get-Date).ToUniversalTime()` fresh before every response.

## LAST_TOOL_GATE
The LAST tool call before writing a response MUST always be the EXACT bash command:
```
$d = (Get-Date).ToUniversalTime(); "**Date:** $($d.ToString('yyyy-MM-dd HH:mm')) UTC - SURVIVAL Day $($d.Day - 16)"
```
The response's first line MUST match the bash output VERBATIM. If the bash output says "06:59" but the response says "07:00", the response is a system failure. No rounding, no estimation, no mental calculation. The bash output IS the timestamp.

## PROMPT LANGUAGE GATE
Every GENERATION prompt MUST be in English. Exception: model documentation confirms native support for the target language. If a French prompt is found, STOP and translate to English.

## COMPLETION RULE
Complete only when: all workflow assets exist, all gates pass, outputs created, state updated, knowledge captured, lessons stored.

## FOUNDER VALIDATION GATE
Every document generated by the OS must be validated by the founder before writing.
Process: PROPOSE content → SHOW generation prompt → WAIT for confirmation → PERSIST.
Never write without explicit validation. An unvalidated file is a file that does not exist.

## ANTI-CHEAT RULE
Never skip gates. Never assume assets exist. Never assume work is complete. Verification required. Always.

## ESCALATION
If gate repeatedly fails: identify root cause, generate remediation plan, update workflow registry.
