# Automation Engine

## Purpose
If a task repeats, automate it.

## Structure
TRIGGER → CONDITIONS → ACTION → VERIFICATION → LOGGING.

## Trigger Types
Time, Event, State Change, Manual, External Signal.

## Examples
- 08:00 → Generate Daily Brief
- New Repository → Project Discovery → Update Project Registry
- New Research Paper → Relevance Analysis → Research Report
- Competitor Funding Event → Impact Analysis → Strategic Alert

## Automation States
Draft, Active, Paused, Failed, Archived.

## Human Approval Mode
Certain actions require approval: delete files, send emails, publish content, transfer money.

## Autonomous Mode
Low-risk actions execute automatically: generate reports, update registries, create summaries, monitor sources.

## Failure Handling
Generate AUTOMATION_FAILURE_REPORT.md.
