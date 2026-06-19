# FOUNDEROS_FILE_CONVENTION V1

## Purpose

FounderOS lives inside files.

Without conventions:

```text
6 months later

↓

Chaos
```

---

Examples:

```text
notes.md

notes_final.md

notes_final_v2.md

notes_final_v2_REAL.md
```

---

Unacceptable.

---

FounderOS must maintain:

Predictability

Discoverability

Persistence

Scalability

---

# Prime Directive

Every file must have:

One Purpose

One Location

One Owner

One Lifecycle

---

# Root Structure

```text
FounderHQ/

├── FounderOS/
│
├── Projects/
│
├── Knowledge/
│
├── Reports/
│
├── Events/
│
├── Workspace/
│
└── Archive/
```

---

# FounderOS Folder

Contains:

```text
Operating System Files
```

Only.

---

Example:

```text
FounderOS/

MOS.md
DAOS.md
PSOS.md
DTOS.md
KMOS.md
POE.md
FAOS.md
ARE.md
EE.md

KERNEL.md
RUNTIME.md
GENESIS.md
TOS.md
```

---

Never place project files here.

---

# Projects Folder

Contains:

```text
Active Projects
```

---

Example:

```text
Projects/

Kora/

EdenValley/

Cortexia/
```

---

Every project receives:

```text
PROJECT_PROFILE.md

PROJECT_STATE.md

PROJECT_ROADMAP.md

PROJECT_DECISIONS.md

EXECUTION_QUEUE.md
```

---

# Knowledge Folder

Contains:

```text
Permanent Knowledge
```

---

Examples:

```text
Research

Papers

Lessons

Frameworks

Market Intelligence
```

---

Never store temporary notes.

---

# Reports Folder

Contains:

```text
Generated Reports
```

---

Examples:

```text
DAILY_BRIEF.md

WEEKLY_REVIEW.md

MONTHLY_REVIEW.md

MISSION_SCORE.md
```

---

# Events Folder

Contains:

```text
External Events
```

---

Examples:

```text
Investor Replies

Customer Feedback

Partnership Updates

Competitor Changes
```

---

# Workspace Folder

Temporary work.

---

Examples:

```text
Drafts

Experiments

Scratch Notes

Temporary Analysis
```

---

Workspace is disposable.

---

# Archive Folder

Contains:

```text
Inactive Content
```

---

Examples:

```text
Old Reports

Closed Projects

Deprecated Plans
```

---

Never delete important history.

Archive instead.

---

# Naming Convention

Use:

```text
UPPER_SNAKE_CASE.md
```

for system files.

---

Examples:

```text
CURRENT_STATE.md

MISSION_PROFILE.md

ACTIVE_PRIORITIES.md

MISSION_SCORE.md
```

---

Use:

```text
TitleCase
```

for project folders.

---

Examples:

```text
Kora

EdenValley

FounderOS
```

---

# Forbidden Naming

Never:

```text
final.md

final2.md

final_final.md

newfile.md

test.md
```

---

# Date Convention

Always:

```text
YYYY-MM-DD
```

---

Example:

```text
2026-08-18
```

---

Never:

```text
18-08-26

08-18-26
```

---

# Report Naming

Daily:

```text
DAILY_BRIEF_YYYY-MM-DD.md
```

---

Weekly:

```text
WEEKLY_REVIEW_YYYY-WXX.md
```

---

Monthly:

```text
MONTHLY_REVIEW_YYYY-MM.md
```

---

Quarterly:

```text
QUARTER_REVIEW_YYYY-QX.md
```

---

# Project Standard

Every project must contain:

```text
PROJECT_PROFILE.md

PROJECT_STATE.md

PROJECT_ROADMAP.md

PROJECT_DECISIONS.md

EXECUTION_QUEUE.md
```

---

Optional:

```text
RESEARCH/

REPORTS/

ASSETS/

CODE/
```

---

# Knowledge Standard

Knowledge entries use:

```text
KNOWLEDGE_ENTRY_YYYY-MM-DD.md
```

---

Structure:

```markdown
Title

Source

Summary

Insights

Applications

Related Projects
```

---

# Decision Standard

Every major decision:

```text
DECISION_YYYY-MM-DD.md
```

---

Contains:

```text
Context

Options

Decision

Reasoning

Expected Outcome
```

---

# State Files

Mandatory:

```text
CURRENT_STATE.md

ACTIVE_PRIORITIES.md

MISSION_PROFILE.md

MISSION_SCORE.md

OPERATING_MODE.md

FOUNDER_PROFILE.md

DIGITAL_TWIN.md

PROJECT_REGISTRY.md
```

---

These files represent:

```text
Current Reality
```

---

Never archive them.

Always update them.

---

# Versioning Rule

Never create:

```text
file_v2.md

file_v3.md

file_v4.md
```

---

Instead:

Update existing file.

Track history using:

```text
Git

Snapshots

Archive
```

---

# Snapshot Standard

State snapshots:

```text
STATE_SNAPSHOT_YYYY-MM-DD.md
```

---

Stored in:

```text
Archive/Snapshots/
```

---

# Report Retention

Keep:

```text
Daily Reports
90 days
```

---

Move older reports to:

```text
Archive/
```

---

# Knowledge Retention

Never delete.

---

Knowledge compounds.

---

# Project Lifecycle

Projects move:

```text
Idea

↓

Active

↓

Paused

↓

Completed

↓

Archived
```

---

Status stored in:

```text
PROJECT_STATE.md
```

---

# FounderOS File Hierarchy

Priority order:

```text
Current State

↓

Projects

↓

Knowledge

↓

Reports

↓

Archive
```

---

When conflicts occur:

Current State wins.

---

# File Creation Policy

Before creating a file ask:

```text
Does a file already exist
for this purpose?
```

---

If:

Yes

↓

Update

---

If:

No

↓

Create

---

# Ultimate Objective

Transform:

Hundreds Of Files

↓

Into

Structured Knowledge

↓

Persistent Context

↓

Operational Intelligence
