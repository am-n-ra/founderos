# DIOS Sprint 1 — Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract DIOS into a specialized framework under `Frameworks/Specialized/Distribution/` with 4 core sub-modules, master module, and system integration.

**Architecture:** DIOS currently exists as a single flat file at `DIOS.md` with 8 domains + 12-step workflow. Sprint 1 extracts 4 core domains into focused files, keeps the master module as orchestrator, and integrates into SYSTEM_PROMPT intent classification and SOURCE_OF_TRUTH.

**Tech Stack:** Markdown — no code, no tests. Verification = behavioral checks via file existence + conceptual coherence.

---

### Task 1: Create directory structure

**Files:**
- Create: `Frameworks/Specialized/Distribution/` (directory)
- Create: `Frameworks/Specialized/Distribution/DIOS/` (directory)

- [ ] **Step 1: Create directories**

Run:
```bash
mkdir -p "FounderOS/Frameworks/Specialized/Distribution/DIOS"
```

Verify:
```bash
ls -la "FounderOS/Frameworks/Specialized/Distribution/DIOS/"
```
Expected: empty directory exists

---

### Task 2: Create DIOS master module (orchestrator)

**Files:**
- Create: `Frameworks/Specialized/Distribution/DIOS.md`
- Modify: remove or redirect old `DIOS.md` at root

The master module keeps the DIOS identity, mission, position in FounderHQ, workflow, KPIs, and the domain-to-submodule mapping. Each submodule becomes a reference.

- [ ] **Step 1: Write DIOS master module**

Write `Frameworks/Specialized/Distribution/DIOS.md`:

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
**DIOS**
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

## Related Systems

- **VAOS** (Frameworks/Specialized/Venture/VAOS.md) — structures the venture before DIOS distributes it
- **CEOS** — receives DIOS strategy, produces content
- **AI_VIDEO_MASTER_DOMAIN** — receives CEOS specs, produces video + distribution package
- **FAOS** — funnel / conversion models
- **CAOS** — pricing / cash constraints
- **DISTRIBUTION_MEMORY** — stores campaign results

## DIOS Workflow

STEP 1: Receive offer (product, price, objective, constraints)
STEP 2: Load AUDIENCE_INTELLIGENCE → identify market + min 3 audiences, select primary
STEP 3: Load LANGUAGE_INTELLIGENCE → derive language(s) from market
STEP 4: Load PLATFORM_INTELLIGENCE → select platform(s) per audience behavior
STEP 5: Load HOOK_INTELLIGENCE → create angle(s) + generate/filter hooks
STEP 6: Load OFFER_INTELLIGENCE → choose CTA + counter objection
STEP 7: Send distribution strategy to CEOS for production
STEP 8: Receive performance data → update DISTRIBUTION_MEMORY + KNOWLEDGE

## Sub-modules

| Module | Path |
|--------|------|
| AUDIENCE_INTELLIGENCE | DIOS/AUDIENCE_INTELLIGENCE.md |
| LANGUAGE_INTELLIGENCE | DIOS/LANGUAGE_INTELLIGENCE.md |
| PLATFORM_INTELLIGENCE | DIOS/PLATFORM_INTELLIGENCE.md |
| HOOK_INTELLIGENCE | DIOS/HOOK_INTELLIGENCE.md |
| OFFER_INTELLIGENCE | DIOS/OFFER_INTELLIGENCE.md |
| DISTRIBUTION_INTELLIGENCE | DIOS/DISTRIBUTION_INTELLIGENCE.md |
| CONVERSION_INTELLIGENCE | DIOS/CONVERSION_INTELLIGENCE.md |
| DISTRIBUTION_MEMORY | DIOS/DISTRIBUTION_MEMORY.md |

## KPIs

Reach | Views | Retention | CTR | Messages | Leads | Conversions | Revenue | ROI

## Definition of Success

A successful campaign is not a beautiful video. A successful campaign is:
Attention → Trust → Action → Sale → Learning

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | System |
| Dependencies | CEOS.md, AI_VIDEO_MASTER_DOMAIN.md, FAOS.md, CAOS.md, concepts/DISTRIBUTION_MEMORY.md, concepts/KNOWLEDGE.md |
```

- [ ] **Step 2: Archive old root DIOS.md**

Move the old file to mark it as superseded:
```bash
mv "FounderOS/DIOS.md" "FounderOS/DIOS.legacy.md"
```
This preserves content history. The new master module at `Frameworks/Specialized/Distribution/DIOS.md` becomes canonical.

---

### Task 3: Create AUDIENCE_INTELLIGENCE.md

**Files:**
- Create: `Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md`

Extract Domain 2 (Audience Intelligence) from the old DIOS.md. Add:
- Segmentation method
- Persona template
- Integration with Market Intelligence
- The rule: min 3 audiences per offer before choosing primary

- [ ] **Step 1: Write AUDIENCE_INTELLIGENCE.md**

```markdown
# DIOS — AUDIENCE_INTELLIGENCE

## Mission

Identify precisely who must see the content.

## Core Rule

Audience ≠ Product.

Every offer has multiple distinct audiences. Each needs a different hook, different story, different CTA.

DIOS identifies at least 3 distinct audiences before choosing the primary target.

## Method

1. List the problem the product solves
2. For each problem → who experiences it most acutely?
3. For each group → what is their specific frustration/desire/fear?
4. For each group → where do they consume content?
5. Select primary audience + secondary audience per campaign

## Persona Template

```
Audience: [name]
Problem: [what they suffer from]
Hook angle: [what makes them stop scrolling]
Language: [derived from market + audience]
Platform: [where they spend time]
CTA: [what action they will take]
Objection: [why they would say no]
```

## Example (Pest Repeller)

| Audience | Hook | Platform |
|----------|------|----------|
| Parents (enfants) | Protéger bébé des moustiques la nuit | TikTok, WhatsApp |
| Femmes enceintes | Protéger la grossesse du paludisme | TikTok |
| Commerçants | Protéger le stock, dormir pour bosser | Facebook, WhatsApp |
| Hôtels | Confort client, avis Booking | Facebook |
| Écoles | Concentration élèves, confiance parents | WhatsApp |

## Example (Kit Solaire)

| Audience | Hook | Platform |
|----------|------|----------|
| Parents | Enfant révise à la bougie depuis 3 mois | TikTok |
| Petits commerçants | Perte de stock quand l'électricité part | Facebook |
| Vendeurs de rue | Recharger téléphone pour les clients | TikTok, WhatsApp |

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | LANGUAGE_INTELLIGENCE.md, PLATFORM_INTELLIGENCE.md |
```

---

### Task 4: Create LANGUAGE_INTELLIGENCE.md

**Files:**
- Create: `Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md`

Extract Domain 3 (Language Intelligence) from old DIOS.md. Emphasize:
- Language is derived from market, not hardcoded
- Cultural adaptation > translation
- Language → culture → reality mapping

- [ ] **Step 1: Write LANGUAGE_INTELLIGENCE.md**

```markdown
# DIOS — LANGUAGE_INTELLIGENCE

## Mission

Speak the language of the public. Not just translate — adapt to how they think, feel, and buy.

## Core Rule

Languages are derived from Market Intelligence + target country. Never hardcoded.

## Language Derivation

| Market | Available Languages |
|--------|-------------------|
| Togo | Français, Ewe, Mina, Pidgin, Kabiye, Tem |
| Ghana | English, Twi, Ga, Ewe, Hausa, Pidgin |
| Nigeria | English, Pidgin, Yoruba, Hausa, Igbo, Efik |
| Benin | Français, Fon, Yoruba, Mina, Bariba |

## Adaptation Layers

1. **Language** — vocabulary, grammar (e.g. French formal vs colloquial)
2. **Culture** — references, humor,禁忌, values (e.g. "protège ta famille" hits differently in Lomé vs Paris)
3. **Reality** — economic context, infrastructure, daily life (e.g. "quand l'électricité part" only works where blackouts are common)
4. **Problem** — is the problem felt the same way? (e.g. "moustique = nuisance" vs "moustique = malaria")
5. **Desire** — what does the audience aspire to? (e.g. "avoir l'air moderne" vs "protéger ce qu'on a")

## Principle

> Le français pour le sérieux. L'ewe pour le coeur. Le pidgin pour la rue.

DIOS selects primary language + secondary language per campaign based on audience segment.

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md |
```

---

### Task 5: Create PLATFORM_INTELLIGENCE.md

**Files:**
- Create: `Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md`

Extract Domain 4 (Platform Intelligence) from old DIOS.md. Include platform mechanics, objectives, and content structure per platform.

- [ ] **Step 1: Write PLATFORM_INTELLIGENCE.md**

```markdown
# DIOS — PLATFORM_INTELLIGENCE

## Mission

Adapt content to the platform's attention mechanic.

## Core Rule

DIOS selects platform(s) based on audience behavior, not preference.

## Platform Profiles

### TikTok

- Objective: Stop the scroll
- Structure: Hook → Curiosity → CTA
- Format: 30-60s vertical (9:16), text overlay mandatory, trending audio
- Key mechanic: First 2 seconds decide everything
- Attention source: Pattern interrupt (audio/visual/text)
- Best for: Product demo, building in public, before/after

### Facebook

- Objective: Build trust
- Structure: Problem → Story → Proof → CTA
- Format: 1:1 or 16:9, longer captions, comments thread
- Key mechanic: Social proof, shares, group recommendations
- Attention source: Relatability, community, credibility
- Best for: Testimonials, detailed demos, local engagement

### WhatsApp

- Objective: Recommendation and direct sale
- Structure: Trust → Testimonial → Offer → Direct message
- Format: Image + text + voice note, 1-on-1
- Key mechanic: Personal relationship, low pressure
- Attention source: Trust, familiarity, exclusivity
- Best for: Closing sales, customer support, recurring orders

### YouTube

- Objective: Education and authority
- Structure: Value → Authority → Conversion
- Format: 10-14 min horizontal 16:9 or Shorts (vertical)
- Key mechanic: Watch time, retention, subscription
- Attention source: Curiosity, deep value, entertainment
- Best for: Tutorials, deep dives, long-form storytelling

### X / Twitter

- Objective: Intellectual presence
- Structure: Hook → Insight → Thread
- Format: Text thread, 280+ characters
- Key mechanic: Retweets, engagement, followers
- Attention source: Novelty, controversy, value density
- Best for: Building in public, insights, networking

## Selection Matrix

DIOS selects platform by:
1. Audience concentration (where does the target spend time?)
2. Content format (does the offer work better in short or long form?)
3. Conversion path (how does the platform lead to a sale?)
4. Resource constraint (how much content can we produce?)

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md |
```

---

### Task 6: Create HOOK_INTELLIGENCE.md

**Files:**
- Create: `Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md`

Extract Domain 5 (Attention Intelligence) from old DIOS.md. Focus on:
- 9 sources of attention
- Hook generation dimensions
- Hook testing framework
- Hook Layer Priority (audio > visual > text) from KNOWLEDGE

- [ ] **Step 1: Write HOOK_INTELLIGENCE.md**

```markdown
# DIOS — HOOK_INTELLIGENCE

## Mission

Understand why someone stops scrolling and create hooks that force them to stop.

## Core Rule

Hook operates on 3 layers, in priority order:
1. **AUDIO** — fastest to reach the brain (sound, buzz, scream, question)
2. **VISUAL** — breaks scroll pattern (face zoom, movement, bright flash)
3. **TEXT** — only works if audio AND visual already stopped the scroll

Validated truth: Text alone cannot fix a hook problem.

## 9 Sources of Attention

| Source | Hook Angle |
|--------|-----------|
| Fear | "Si tu ne fais pas X, Y arrive" |
| Curiosity | "Pourquoi X arrive ? La réponse est Y" |
| Desire | "Imagine ta vie avec X" |
| Money | "Tu perds X FCFA par jour à cause de Y" |
| Health | "X fait ça à ton corps sans que tu le saches" |
| Family | "Tes enfants méritent X" |
| Status | "Les gens qui ont X sont vus comme Y" |
| Safety | "X te protège de Y" |
| Opportunity | "X est disponible maintenant, après c'est fini" |

## Hook Generation Dimensions

For each audience, DIOS generates hooks across:
- Per audience segment (parent, merchant, student...)
- Per attention source (fear, curiosity, desire...)
- Per language (French, Ewe, Pidgin...)
- Per platform format (short vs long, vertical vs horizontal)

## Hook Selection

For each campaign, generate 10-50 hooks, then filter:
1. Is it true? (never lie)
2. Does it match the audience?
3. Does it work on the chosen platform?
4. Does it pass the 2-second test? (would someone stop scrolling?)

## Example (Kit Solaire, Audience: Parents)

1. "Ton enfant révise à la bougie depuis janvier. Et si c'était la dernière fois ?"
2. "500 FCFA par jour d'essence. Chaque jour. Depuis 3 mois."
3. "Ton voisin a déjà installé le sien. Tu attends quoi ?"

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | AUDIENCE_INTELLIGENCE.md, LANGUAGE_INTELLIGENCE.md, PLATFORM_INTELLIGENCE.md |
```

---

### Task 7: Update SYSTEM_PROMPT.md — DIOS intent classification

**Files:**
- Modify: `SYSTEM_PROMPT.md`

Add DIOS to the intent classification table and update the DIOS workflow reference.

- [ ] **Step 1: Read SYSTEM_PROMPT.md to find exact insertion point**

```bash
grep -n "Distribution, campaign, audience" "FounderOS/SYSTEM_PROMPT.md"
```
Expected: finds the DIOS row in intent classification table.

- [ ] **Step 2: Update DIOS reference in intent classification table**

Edit the row for DISTRIBUTION to point to new location:

Replace:
```
| Distribution, campaign, audience | DISTRIBUTION | Load DIOS.md |
```
With:
```
| Distribution, campaign, audience | DISTRIBUTION | Load Frameworks/Specialized/Distribution/DIOS.md |
```

---

### Task 8: Update SOURCE_OF_TRUTH.md

**Files:**
- Modify: `Protocols/SOURCE_OF_TRUTH.md`

Add DIOS sub-modules to the truth map.

- [ ] **Step 1: Read SOURCE_OF_TRUTH.md to find insertion point**

```bash
grep -n "DIOS" "FounderOS/Protocols/SOURCE_OF_TRUTH.md"
```

- [ ] **Step 2: Add DIOS sub-modules to the truth map**

After the existing DIOS line, add:
```
| Distribution intelligence (audience, language, platform, hook) | Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md |
| Language-market derivation | Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md |
| Platform selection by audience behavior | Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md |
| Hook creation and testing | Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md |
```

---

### Task 9: Behavioral verification

**Files:** none

- [ ] **Step 1: Verify all files exist**

```bash
ls -la "FounderOS/Frameworks/Specialized/Distribution/DIOS.md"
ls -la "FounderOS/Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md"
ls -la "FounderOS/Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md"
ls -la "FounderOS/Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md"
ls -la "FounderOS/Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md"
```
Expected: all 5 files exist

- [ ] **Step 2: Verify SYSTEM_PROMPT.md references updated path**

```bash
grep "DIOS.md" "FounderOS/SYSTEM_PROMPT.md"
```
Expected: path points to `Frameworks/Specialized/Distribution/DIOS.md`

- [ ] **Step 3: Verify old root DIOS.md is archived**

```bash
ls -la "FounderOS/DIOS.legacy.md"
```
Expected: file exists (content preserved, not deleted)

- [ ] **Step 4: Verify SOURCE_OF_TRUTH.md has new entries**

```bash
grep "DIOS/AUDIENCE_INTELLIGENCE" "FounderOS/Protocols/SOURCE_OF_TRUTH.md"
grep "DIOS/LANGUAGE_INTELLIGENCE" "FounderOS/Protocols/SOURCE_OF_TRUTH.md"
```
Expected: both return matching lines

---

### Task 10: Commit

- [ ] **Step 1: Stage and commit**

```bash
git add -A
git commit -m "feat(dios): extract DIOS into specialized framework (sprint 1)

- Move DIOS.md to Frameworks/Specialized/Distribution/DIOS.md
- Extract 4 core sub-modules: AUDIENCE_INTELLIGENCE, LANGUAGE_INTELLIGENCE, PLATFORM_INTELLIGENCE, HOOK_INTELLIGENCE
- Update SYSTEM_PROMPT.md intent classification path
- Update SOURCE_OF_TRUTH.md with sub-module entries
- Archive legacy DIOS.md as DIOS.legacy.md"
```
