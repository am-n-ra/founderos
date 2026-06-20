# DIOS — Distribution Intelligence OS Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create DIOS as the commercial nervous system of FounderHQ, sitting above CEOS in the pipeline — deciding what to produce (audience, language, platform, angle, hook) and learning from every campaign via DISTRIBUTION_MEMORY.

**Architecture:** DIOS is a new OS module at `FounderOS/DIOS.md` containing 8 domains (Market/Audience/Language/Platform/Attention/Conversion Intelligence + Distribution Memory/Analytics) and a 12-step workflow. It receives offers and produces distribution strategy, passes to CEOS for production, and stores campaign results in the new `concepts/DISTRIBUTION_MEMORY.md` concept. CEOS is refactored to focus purely on production (ideation/distribution/analysis removed). AI_VIDEO_MASTER_DOMAIN gets a Distribution Package output stage.

**Tech Stack:** Markdown, FounderOS V4 conventions (file-as-truth, Regle 0), YAML for concept data

**Spec:** `docs/superpowers/specs/2026-06-20-dios-distribution-intelligence-os-design.md`

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `FounderOS/DIOS.md` | Create | New OS module: 8 domains + 12-step workflow + CEOS/AI_VIDEO_MASTER_DOMAIN integration |
| `concepts/DISTRIBUTION_MEMORY.md` | Create | Campaign memory with YAML structure per campaign entry |
| `FounderOS/CEOS.md` | Refactor (lines 16-20, 26-40) | Remove Ideate/Distribute/Analyze phases, keep Produce only |
| `FounderOS/AI_VIDEO_MASTER_DOMAIN.md` | Modify (after line 41) | Add Distribution Package section after Post-Production |
| `FounderOS/SYSTEM_PROMPT.md` | Modify (line 109) | Add DIOS entry to Intent Classification table |
| `FounderOS/Protocols/SOURCE_OF_TRUTH.md` | Modify (after line 56) | Add DIOS + DISTRIBUTION_MEMORY entries |

---

## Tasks

### Task 1: Create DIOS.md — Full Module with 8 Domains

**Files:**
- Create: `FounderOS/DIOS.md`

- [ ] **Step 1: Create DIOS.md with Identity, Mission, Position, Inputs, Outputs**

Write to `FounderOS/DIOS.md`:

```markdown
# FounderOS V4 — DIOS (Distribution Intelligence Operating System)

## Identity

DIOS (Distribution Intelligence Operating System) is the commercial nervous system of FounderHQ.

## Mission

Transform any offer into attention, attention into trust, trust into conversion, and conversion into reusable knowledge.

## Position in FounderHQ

MISSION
↓
PROJECT
↓
DIOS
↓
CEOS
↓
AI_VIDEO_MASTER_DOMAIN
↓
PUBLICATION
↓
DISTRIBUTION_MEMORY
↓
KNOWLEDGE

## Inputs

- Product / Offer
- Price
- Target market (country, city, region)
- Objective (views, leads, sales)
- Constraints (budget, time, team, cash)
- DISTRIBUTION_MEMORY history (queried before strategy generation)

## Outputs

- Audience segment(s)
- Language(s)
- Platform(s)
- Angle(s)
- Hook(s)
- Promise
- Primary objection
- CTA
- Distribution plan (1 offer → N platform/language/audience variations)

## Relation with CEOS

DIOS answers: For who? Why? Where? When? In which language? With which angle?

CEOS answers: How to tell the story? How to write? How to film? How to produce?

DIOS decides. CEOS produces.

## Relation with AI_VIDEO_MASTER_DOMAIN

DIOS defines: Audience → Language → Hook → Angle → CTA

AI_VIDEO_MASTER_DOMAIN produces: Script → Scenes → Frames → Video → Localization → Platform Variations → Distribution Package

## Relation with Existing Modules

- MOS → feeds DIOS with mission priorities
- CAOS → feeds DIOS with pricing/cash constraints
- FAOS → feeds DIOS with funnel/conversion models
- CEOS → receives DIOS strategy, produces content
- AI_VIDEO_MASTER_DOMAIN → receives CEOS specs, produces video + distribution package
- DISTRIBUTION_MEMORY → stores campaign results, queried by DIOS before each campaign

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | CEOS.md, AI_VIDEO_MASTER_DOMAIN.md, DISTRIBUTION_MEMORY.md |
```

- [ ] **Step 2: Create Domain 1 — Market Intelligence**

Add after `## Relation with Existing Modules`:

```markdown
## Domain 1: Market Intelligence

Mission: Understand the market.

Questions:
- Who suffers?
- Who pays?
- Who searches for a solution?
- Who influences the purchase?
- Who shares information?
- Who decides?
- Who uses?

Data tracked:
- Needs
- Frustrations
- Fears
- Desires
- Trends
- Seasonality

Example (Kit solaire):
- Problems: blackouts, fuel cost, difficulty charging phone
- Audience: households, small businesses, street vendors
- Seasonality: dry season (more sun, more need for cooling/fans)

Language derivation: Market (country) determines available languages. Not hardcoded.
```

- [ ] **Step 3: Create Domain 2 — Audience Intelligence**

```markdown
## Domain 2: Audience Intelligence

Mission: Identify precisely who must see the content.

Audience ≠ Product.

Example (Repulsif anti-moustique):
- A1: Parents (hook: protect children while sleeping)
- A2: Pregnant women (hook: protect pregnancy from malaria)
- A3: Merchants (hook: protect inventory, sleep well for business)
- A4: Hotels (hook: guest comfort, reviews)
- A5: Schools (hook: student concentration, parent trust)

Each audience needs a different hook, different story, different CTA.

Method: For every offer, DIOS identifies at least 3 distinct audiences before choosing the primary target.
```

- [ ] **Step 4: Create Domain 3 — Language Intelligence**

```markdown
## Domain 3: Language Intelligence

Mission: Speak the language of the public.

Languages are derived from Market Intelligence + target country. Not hardcoded.

Examples:
- Togo: Francais, Ewe, Mina, Pidgin, Kabiye, Tem
- Ghana: English, Twi, Ga, Ewe, Hausa, Pidgin
- Nigeria: English, Pidgin, Yoruba, Hausa, Igbo, Efik
- Benin: Francais, Fon, Yoruba, Mina, Bariba

Goal: Reduce psychological distance between the offer and the audience.

Each language version must be culturally adapted, not just translated.

DIOS selects primary language + secondary language per campaign based on audience segment.
```

- [ ] **Step 5: Create Domain 4 — Platform Intelligence**

```markdown
## Domain 4: Platform Intelligence

Mission: Adapt content to the platform's attention mechanic.

TikTok
- Objective: Stop the scroll
- Structure: Hook → Curiosity → CTA
- Key: First 2 seconds decide everything

Facebook
- Objective: Build trust
- Structure: Problem → Story → Proof → CTA
- Key: Credibility signals, social proof, comments

WhatsApp
- Objective: Recommendation
- Structure: Trust → Testimonial → Offer → Direct message
- Key: 1-on-1 relationship, personal, low pressure

YouTube
- Objective: Education
- Structure: Value → Authority → Conversion
- Key: Watch time, retention, deep explanation

Kora
- Objective: Discovery commerce
- Structure: To be defined as platform evolves
- Key: Payment + distribution in one interface

DIOS selects platform(s) based on audience behavior, not preference.
```

- [ ] **Step 6: Create Domain 5 — Attention Intelligence**

```markdown
## Domain 5: Attention Intelligence

Mission: Understand why someone stops scrolling.

Sources of attention:
- Fear
- Curiosity
- Desire
- Money
- Health
- Family
- Status
- Safety
- Opportunity

Hook Engine: For each audience, DIOS generates 10-50 hooks, then selects the best.

Hook generation dimensions:
- Per audience segment
- Per attention source
- Per language
- Per platform format (short vs long)

Example (Kit solaire, audience: parents, French):
1. "Quand le debitement coupe a 22h, votre enfant revise a la bougie depuis 3 mois."
2. "500 FCFA par jour de carburant. Chaque jour. Depuis janvier."
3. "Votre voisin a deja installe le sien. Vous attendez quoi ?"
```

- [ ] **Step 7: Create Domain 6 — Conversion Intelligence**

```markdown
## Domain 6: Conversion Intelligence

Mission: Transform views into sales.

Analysis dimensions:
- Why buy? (value, need, desire)
- Why wait? (risk, uncertainty, trust)
- Why refuse? (price, objection, timing)
- Why share? (status, altruism, entertainment)

Variables:
- Price → perceived value, comparison, affordability
- Risk → money-back guarantee, testimonial, trial
- Trust → social proof, authority, familiarity
- Urgency → scarcity, time-limited, stock-limited
- Proof → before/after, data, demonstration
- Simplicity → how easy to buy, receive, use

Framework: Integrates with FAOS (funnel stages) and CAOS (pricing psychology).

DIOS chooses primary objection and prepares counter before CEOS produces content.
```

- [ ] **Step 8: Create Domain 7 — Distribution Memory**

```markdown
## Domain 7: Distribution Memory

Mission: Accumulate market intelligence from every campaign.

DIOS queries DISTRIBUTION_MEMORY before every new campaign to find:
- Which hooks won for this audience?
- Which language converted best?
- Which platform distributed furthest?
- Which CTA drove action?

DISTRIBUTION_MEMORY is stored as a concept at concepts/DISTRIBUTION_MEMORY.md.

Each campaign entry captures: hook, audience, language, platform, views, engagement, conversions, revenue, ROI, learnings.
```

- [ ] **Step 9: Create Domain 8 — Distribution Analytics**

```markdown
## Domain 8: Distribution Analytics

Mission: Identify patterns across campaigns.

Questions:
- Which hooks win? (across audiences, languages, platforms)
- Which languages convert? (per market, per product)
- Which platforms distribute? (per audience, per content type)
- Which CTAs perform? (per platform, per audience)
- Which segments buy? (per product, per price point)
- Which angles generate word-of-mouth?

Outputs:
- Reports (per campaign, per product, per market)
- Rankings (top hooks, top CTAs, top platforms)
- Recommendations (what to try next, what to stop)

DIOS uses analytics to improve future campaigns autonomously.
```

- [ ] **Step 10: Create the 12-Step Workflow**

```markdown
## DIOS Workflow

STEP 1: Receive offer (product, price, objective, constraints)
STEP 2: Identify market (Market Intelligence)
STEP 3: Identify audience(s) (Audience Intelligence) — min 3, select primary
STEP 4: Choose language(s) (Language Intelligence) — derived from market
STEP 5: Choose platform(s) (Platform Intelligence) — per audience behavior
STEP 6: Create angle(s) (Attention Intelligence + Market Intelligence)
STEP 7: Create hooks (Attention Intelligence) — generate, filter, select best
STEP 8: Choose CTA (Conversion Intelligence)
STEP 9: Send distribution strategy to CEOS for production
STEP 10: Receive performance data after publication
STEP 11: Update DISTRIBUTION_MEMORY
STEP 12: Update KNOWLEDGE (validated patterns → concepts/KNOWLEDGE.md)

## KPIs

Reach | Views | Retention | CTR | Messages | Leads | Conversions | Revenue | ROI

## Definition of Success

A successful campaign is not "a beautiful video."

A successful campaign is:
Attention → Trust → Action → Sale → Learning

Then the system becomes smarter than yesterday.
```

- [ ] **Step 11: Verify DIOS.md is complete**

Read `FounderOS/DIOS.md`. Verify:
- Identity section present
- Mission present
- Position in FounderHQ present
- Inputs present
- Outputs present
- All 8 domains present (Market, Audience, Language, Platform, Attention, Conversion, Distribution Memory, Distribution Analytics)
- 12-step workflow present
- CEOS and AI_VIDEO_MASTER_DOMAIN relations present
- Existing module relations present
- Footer present

- [ ] **Step 12: Commit**

```bash
git add FounderOS/DIOS.md
git commit -m "feat: create DIOS module - 8 domains + 12-step workflow"
```

---

### Task 2: Create DISTRIBUTION_MEMORY.md Concept

**Files:**
- Create: `concepts/DISTRIBUTION_MEMORY.md`

- [ ] **Step 1: Create concepts/DISTRIBUTION_MEMORY.md**

Write to `concepts/DISTRIBUTION_MEMORY.md`:

```markdown
# Distribution Memory

## Purpose

Structured campaign memory that accumulates market intelligence over time. Every campaign is recorded with its strategy and performance. DIOS queries this before every new campaign.

## Structure

Each campaign entry follows this schema:

```yaml
## Campaign: [ID]

- Date: YYYY-MM-DD
- Product: [name]
- Price: [price FCFA]
- Objective: [views / leads / sales]
- Market: [country, city]
- Audience: [segment name]
- Language: [language]
- Platform: [platform name]
- Hook: "exact hook text used"
- Angle: [description of angle]
- CTA: "exact call to action"
- Views: N
- Likes: N
- Comments: N
- Shares: N
- Messages: N
- Leads: N
- Conversions: N
- Revenue: N FCFA
- Cost: N FCFA
- ROI: N.Nx
- Learnings: "what worked and what didn't"
- Next: "what to try next time"
```

## Usage

DIOS queries DISTRIBUTION_MEMORY at step 1 of its workflow.

Query patterns:
- "Which hooks won for audience X?"
- "Which language converted best for product Y?"
- "Which platform distributed furthest in market Z?"
- "Which CTA performed best on platform W?"

## Empty State

No campaigns recorded yet.

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Maintained By | DIOS (writes after each campaign) |
```

- [ ] **Step 2: Verify file created correctly**

Read `concepts/DISTRIBUTION_MEMORY.md`. Verify:
- YAML structure is valid
- All fields documented
- Usage section describes query patterns
- Empty state declared
- Footer present

- [ ] **Step 3: Commit**

```bash
git add concepts/DISTRIBUTION_MEMORY.md
git commit -m "feat: create DISTRIBUTION_MEMORY concept for campaign intelligence"
```

---

### Task 3: Refactor CEOS.md — Remove Ideation, Distribution, Analysis

**Files:**
- Modify: `FounderOS/CEOS.md:14-40`

- [ ] **Step 1: Remove Phase 1 (Ideate)**

In `FounderOS/CEOS.md`, replace lines 14-19 (`## Content Pipeline` through the end of Phase 1):

Old:
```
## Content Pipeline

### Phase 1: Ideate
- Generate 5-10 content ideas per domain
- Filter by: mission alignment, production cost, audience interest
- Select top 1-3
```

New:
```
## Content Pipeline
```

- [ ] **Step 2: Remove Phase 3 (Distribute) and Phase 4 (Analyze)**

Old:
```

### Phase 3: Distribute
- YouTube: title, description, tags, thumbnail, publish
- Shorts: hook layer optimization (audio > visual > text)
- Track performance in ASSET.md

### Phase 4: Analyze
- Views, retention, engagement per platform
- Hook Layer Analysis: at what second do viewers drop?
- Document learnings in KNOWLEDGE.md
```

New: (nothing — remove those lines)

- [ ] **Step 3: Update Integration section**

Old:
```
## Integration

- CEOS may invoke LEOS for research on content topics
- CEOS uses AI_VIDEO_MASTER_DOMAIN.md for video production
- CEOS reports to DAOS for daily content actions
```

New:
```
## Integration

- CEOS receives distribution strategy from DIOS (audience, language, platform, hook, angle, CTA)
- CEOS may invoke LEOS for research on content topics
- CEOS uses AI_VIDEO_MASTER_DOMAIN.md for video production
- CEOS reports to DAOS for daily content actions
```

- [ ] **Step 4: Update footer dependencies**

Add `DIOS.md` to footer dependencies:

Old:
```
| Dependencies | AI_VIDEO_MASTER_DOMAIN.md, ASSET.md, KNOWLEDGE.md |
```

New:
```
| Dependencies | DIOS.md, AI_VIDEO_MASTER_DOMAIN.md, ASSET.md, KNOWLEDGE.md |
```

- [ ] **Step 5: Verify CEOS.md content**

Read `FounderOS/CEOS.md`. Verify:
- No "Phase 1: Ideate" present
- No "Phase 3: Distribute" present
- No "Phase 4: Analyze" present
- "Phase 2: Produce" is the only phase (or just "Produce" without phase numbering)
- Integration section references DIOS as input
- Footer includes DIOS.md dependency

- [ ] **Step 6: Commit**

```bash
git add FounderOS/CEOS.md
git commit -m "refactor: CEOS - remove ideation/distribution/analysis, add DIOS integration"
```

---

### Task 4: Add Distribution Package to AI_VIDEO_MASTER_DOMAIN.md

**Files:**
- Modify: `FounderOS/AI_VIDEO_MASTER_DOMAIN.md` (after line 41, before line 43)

- [ ] **Step 1: Add Distribution Package section**

After the Post-Production section (after line 41 `5. **Publish**: Schedule for optimal time`), insert a new section:

Old content around line 41-42:
```
5. **Publish**: Schedule for optimal time

### Analysis
```

New content:
```
5. **Publish**: Schedule for optimal time

### Distribution Package

After post-production, AI_VIDEO_MASTER_DOMAIN produces a Distribution Package for each platform/language variant:

1. **Localization**: Adapt script and captions per language (from DIOS Language Intelligence)
2. **Platform Variations**: Adapt format per platform (vertical for TikTok, landscape for YouTube, image + text for Facebook)
3. **Thumbnail Variants**: Per-platform thumbnail optimization
4. **Title & Description**: Per-platform, per-language title with hook and keywords
5. **Tags & Hashtags**: Platform-specific tag sets
6. **Publishing Schedule**: Optimal time per platform per audience

The Distribution Package is the final output that DIOS receives for distribution tracking.

### Analysis
```

- [ ] **Step 2: Update footer dependencies**

Old:
```
| Dependencies | CEOS, ASSET.md, KNOWLEDGE.md |
```

New:
```
| Dependencies | CEOS, DIOS.md, ASSET.md, KNOWLEDGE.md |
```

- [ ] **Step 3: Verify AI_VIDEO_MASTER_DOMAIN.md**

Read `FounderOS/AI_VIDEO_MASTER_DOMAIN.md`. Verify:
- "Distribution Package" section exists after Post-Production
- Contains: Localization, Platform Variations, Thumbnail Variants, Title & Description, Tags & Hashtags, Publishing Schedule
- Footer includes DIOS.md

- [ ] **Step 4: Commit**

```bash
git add FounderOS/AI_VIDEO_MASTER_DOMAIN.md
git commit -m "feat: add Distribution Package output to AI_VIDEO_MASTER_DOMAIN"
```

---

### Task 5: Add DIOS to SYSTEM_PROMPT.md Intent Classification

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md` (before line 110, after "Mission priority" entry)

- [ ] **Step 1: Add DIOS entry to Intent Classification table**

Add a new row in the Intent Classification table (after line 109, before line 110):

Old (around line 109):
```
| Mission priority, project status, "what should I focus on" | MISSION | Load MOS.md, evaluate and recommend |
| Simple update, status, informational (no module matches) | DIRECT | Execute directly, no module needed |
```

New:
```
| Mission priority, project status, "what should I focus on" | MISSION | Load MOS.md, evaluate and recommend |
| Distribution strategy, campaign, "how should I sell this", "who should see this" | DISTRIBUTION | Load DIOS.md, execute distribution intelligence workflow |
| Simple update, status, informational (no module matches) | DIRECT | Execute directly, no module needed |
```

- [ ] **Step 2: Verify SYSTEM_PROMPT.md**

Read `FounderOS/SYSTEM_PROMPT.md`. Verify:
- DISTRIBUTION entry exists in Intent Classification table
- Pattern matches: "Distribution strategy, campaign, how should I sell this, who should see this"
- Classification is DISTRIBUTION
- Action is "Load DIOS.md, execute distribution intelligence workflow"

- [ ] **Step 3: Commit**

```bash
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "feat: add DIOS to Intent Classification in SYSTEM_PROMPT"
```

---

### Task 6: Update SOURCE_OF_TRUTH.md

**Files:**
- Modify: `FounderOS/Protocols/SOURCE_OF_TRUTH.md` (after line 56, before line 58)

- [ ] **Step 1: Add DIOS and DISTRIBUTION_MEMORY entries**

Add two rows to the truth map (after line 56 `| Complete video production system | AI_VIDEO_MASTER_DOMAIN.md |`, before line 57 `| First-time setup procedure | GENESIS.md |`):

Old:
```
| Complete video production system | AI_VIDEO_MASTER_DOMAIN.md |
| First-time setup procedure | GENESIS.md |
```

New:
```
| Complete video production system | AI_VIDEO_MASTER_DOMAIN.md |
| Distribution intelligence, audience, language, platform strategy | DIOS.md |
| Campaign performance data, hook/audience/language history | concepts/DISTRIBUTION_MEMORY.md |
| First-time setup procedure | GENESIS.md |
```

- [ ] **Step 2: Verify SOURCE_OF_TRUTH.md**

Read `FounderOS/Protocols/SOURCE_OF_TRUTH.md`. Verify:
- DIOS.md entry exists with verite "Distribution intelligence, audience, language, platform strategy"
- DISTRIBUTION_MEMORY.md entry exists with verite "Campaign performance data, hook/audience/language history"

- [ ] **Step 3: Commit**

```bash
git add FounderOS/Protocols/SOURCE_OF_TRUTH.md
git commit -m "docs: add DIOS and DISTRIBUTION_MEMORY to SOURCE_OF_TRUTH"
```

---

### Task 7: Final Verification — Cross-Reference Integrity Check

**Files:**
- Review: All 6 modified/created files

- [ ] **Step 1: Verify all cross-references are correct**

Run verification commands:

```bash
# Verify DIOS.md references CEOS.md
rg "CEOS" FounderOS/DIOS.md

# Verify DIOS.md references AI_VIDEO_MASTER_DOMAIN.md
rg "AI_VIDEO_MASTER_DOMAIN" FounderOS/DIOS.md

# Verify DIOS.md references DISTRIBUTION_MEMORY.md
rg "DISTRIBUTION_MEMORY" FounderOS/DIOS.md

# Verify CEOS.md references DIOS.md
rg "DIOS" FounderOS/CEOS.md

# Verify AI_VIDEO_MASTER_DOMAIN.md references DIOS.md
rg "DIOS" FounderOS/AI_VIDEO_MASTER_DOMAIN.md

# Verify SYSTEM_PROMPT.md references DIOS.md
rg "DIOS" FounderOS/SYSTEM_PROMPT.md

# Verify SOURCE_OF_TRUTH.md contains DIOS + DISTRIBUTION_MEMORY
rg "DIOS" FounderOS/Protocols/SOURCE_OF_TRUTH.md
rg "DISTRIBUTION_MEMORY" FounderOS/Protocols/SOURCE_OF_TRUTH.md
```

Expected: all commands return matches showing the cross-references exist.

- [ ] **Step 2: Verify no orphan references remain in CEOS.md**

```bash
# Verify CEOS no longer references Phase 1, Phase 3, Phase 4
rg "Phase 1" FounderOS/CEOS.md
rg "Phase 3" FounderOS/CEOS.md
rg "Phase 4" FounderOS/CEOS.md
```

Expected: no matches (these were removed by the refactor).

- [ ] **Step 3: Report verification results**

Print all results for review.

- [ ] **Step 4: Commit final verification**

```bash
git add -A
git commit -m "chore: final verification - DIOS cross-reference integrity"
```

---

## Verification Summary

| Criterion | Task | How |
|-----------|------|-----|
| DIOS.md has 8 domains + workflow | Task 1, Step 11 | File read verification |
| DISTRIBUTION_MEMORY.md correct | Task 2, Step 2 | File read verification |
| CEOS.md no ideation/distribution/analysis | Task 3, Step 5 | rg + file read |
| AI_VIDEO_MASTER_DOMAIN.md has Distribution Package | Task 4, Step 3 | File read verification |
| SYSTEM_PROMPT.md has DIOS intent entry | Task 5, Step 2 | File read verification |
| SOURCE_OF_TRUTH.md has DIOS + MEMORY | Task 6, Step 2 | File read verification |
| All cross-references intact | Task 7, Step 1 | rg commands |
