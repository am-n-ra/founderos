# PROJECT REGISTRATION PROTOCOL

## Purpose

Ensure every new project added to FounderHQ is fully integrated across ALL relevant files. This protocol is executed once per new project. No file should be left behind.

## Scope

This covers ALL projects regardless of type: ventures (KORA, Omni), products (Soya, Pest Repeller, DoodleMind), partnerships, or experimental.

---

## Registration Checklist

### 1. Create Concept File

`concepts/<PROJECT>.md`

Template:
```markdown
# FounderOS V4 — <PROJECT> (Tagline)

## Purpose

[One paragraph: why this project exists.]

## Position in FounderHQ

[One paragraph: how it relates to other projects.]

## Status

| Field | Value |
|---|---|
| Phase | [Phase] |
| Activity | Active / Standby / Archived |
| Priority | High / Medium / Low |

## Quick Reference

| Document | Location |
|---|---|
| Main docs | `projects/<PROJECT>/` |

## Relations

[Links to other concepts/projects]

## Footer
```

### 2. Create Project Data Room

`projects/<PROJECT>/` with the full **strategic cascade** (defined below).

#### Strategic Cascade (10 files + annexes)

Every project data room MUST contain the following numbered files, plus annexes:

| # | File | Purpose |
|---|------|---------|
| 01 | `01_VISION.md` | Long-term vision (10-20 year horizon) |
| 02 | `02_MISSION.md` | Mission, purpose, what we do / don't do |
| 03 | `03_THEORY_OF_CHANGE.md` | How vision becomes reality; causal chain |
| 04 | `04_STRATEGIC_ASSETS_MAP.md` | Assets accumulated, competitive moats |
| 05 | `05_MASTER_PLAN.md` | Strategic plan, layers, principles |
| 06 | `06_STRATEGIC_ROADMAP.md` | Timeline, phases, milestones |
| 07 | `07_CAPITAL_ROADMAP.md` | Funding needs, sources, use of funds |
| 08 | `08_EXECUTIVE_SUMMARY.md` | 1-page summary for stakeholders |
| 09 | `09_BUSINESS_PLAN.md` | Full business plan (problem, market, model, risks) |
| 10 | `10_PITCH_DECK.md` | Slide-by-slide pitch presentation |
| - | `annexes/` | Supporting docs (contacts, pricing, research) |
| - | `README.md` | Project overview, status, quick links |

**Template:** For format and tone, reference existing project data rooms (`projects/Omni/`, `projects/KORA/`). The cascade follows the same structure regardless of project size — a cash project like SOJACO will have leaner content within the same file structure.

### 3. Update CURRENT_STATE.md

Add to:
- **Active Products** list (line ~61-65)
- **<PROJECT> Status** section (after existing status blocks)
- **Top Priority** — merge if project has deadline
- **Session Objective** — if active

### 4. Update PRIORITY_MATRIX.md

Add row to **Projets Actifs** table with:
- Project name
- Priority Objective
- Status
- Next Action
- Deadline
- Dernière Action
- Warning level

Add item to **Actions Pending** if pending actions exist.

### 5. Update Relations in Existing Concepts

Check these concept files and add `<PROJECT>` where relevant:

| Concept File | When to Add |
|-------------|------------|
| `concepts/KORA.md` | If parallel venture, shared resources, or strategic link |
| `concepts/OMNI.md` | If parallel venture or shared execution model |
| `DAOS.md` | If project generates daily actions |
| `FAOS.md` | If project has fundraising component |
| `LEOS.md` | If project requires learning |
| `DIOS.md` | If project is a distribution platform |
| `CEOS.md` | If project creates content |
| `SOS.md` | If project impacts founder health/energy |

### 6. Check DIOS.md

If project is a distribution platform or commerce channel, add it under the relevant domain in DIOS.md.

### 7. Update CONCEPT_BOUNDARIES.md (if needed)

If project introduces a new concept boundary not yet documented.

### 8. Verify Bidirectional Links

Every relation added must be **bidirectional**. If A relates to B, B must relate to A. Search for the relation in both files.

---

## Quick Reference

| Step | File(s) | Action |
|------|---------|--------|
| 1 | `concepts/<PROJECT>.md` | Create concept file |
| 2 | `projects/<PROJECT>/` | Create data room |
| 3 | `State/CURRENT_STATE.md` | Add to active products + status section |
| 4 | `State/PRIORITY_MATRIX.md` | Add row + pending actions |
| 5 | Relevant concept files | Add relation links |
| 6 | `DIOS.md` | Add platform entry if applicable |
| 7 | `CONCEPT_BOUNDARIES.md` | Update if new boundary |
| 8 | All edited files | Verify bidirectional links |

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | System |
