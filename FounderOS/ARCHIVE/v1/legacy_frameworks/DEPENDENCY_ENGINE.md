# DEPENDENCY_ENGINE V1

## Purpose
FounderOS must never begin work from the requested output. FounderOS must begin from prerequisites.

## Prime Directive
Before executing any task: build the dependency graph. Only execute when all dependencies are satisfied.

## Core Principle
Every output depends on assets. Every asset depends on other assets. Every dependency must be resolved.

## Dependency Types
Knowledge Dependencies, Decision Dependencies, Asset Dependencies, State Dependencies, Workflow Dependencies, Resource Dependencies.

## Resolution Rule
For every requested deliverable, determine what is required. Then what those requirements require. Continue recursively until root dependencies are reached.

## Example: AI Video Ad
Requested: VIDEO_PROMPT.md

Dependency Graph:
VIDEO_PROMPT → SCRIPT + CHARACTER_SHEET + ENVIRONMENT_SHEET + PRODUCT_SHEET + START_FRAME + END_FRAME

Expand SCRIPT → OFFER + CUSTOMER_PROFILE + PAIN_POINTS + CTA
Expand CHARACTER_SHEET → CUSTOMER_PROFILE + CREATIVE_STRATEGY + VISUAL_DIRECTION
Expand START_FRAME → CHARACTER_SHEET + ENVIRONMENT_SHEET + PRODUCT_SHEET

## Root Dependency Rule
Execution starts only from roots. Never start at the requested output.

## Missing Dependency Detection
Before execution: scan Projects, Knowledge, Assets, Reports, State. Determine: exists? → reuse. Missing? → create.

## Dependency Status
UNKNOWN (not evaluated), MISSING (required but absent), IN_PROGRESS (being created), COMPLETE (validated), INVALID (fails quality gate), OBSOLETE (no longer valid).

## Validation
Completion requires: Asset Exists + Quality Gate Passed. Asset alone is insufficient.

## Dependency Report
Before execution generate DEPENDENCY_REPORT.md with: objective, dependency tree, resolved/missing/blocked dependencies, recommended next action.

## Blocking Rule
If critical dependency missing: STOP. Generate BLOCKER_REPORT.md.

## FounderOS Autonomy Rule
The founder should not need to know what comes next, what is missing, or what depends on what. FounderOS should know.
