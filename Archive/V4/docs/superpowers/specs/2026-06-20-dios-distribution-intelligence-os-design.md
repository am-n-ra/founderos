# DIOS — Distribution Intelligence Operating System Design

## Objective

Create DIOS as a new FounderOS module that transforms any offer into attention, attention into trust, trust into conversion, and conversion into reusable knowledge. DIOS is the commercial nervous system of FounderHQ.

## Scope

**Create:** `FounderOS/DIOS.md`, `concepts/DISTRIBUTION_MEMORY.md`

**Refactor:** `FounderOS/CEOS.md` — strip ideation/distribution/analysis, keep production only

**Modify:** `FounderOS/AI_VIDEO_MASTER_DOMAIN.md` — add Distribution Package output, `FounderOS/SYSTEM_PROMPT.md` — add DIOS to Intent Classification, `FounderOS/Protocols/SOURCE_OF_TRUTH.md` — add DIOS + DISTRIBUTION_MEMORY

## Architecture

DIOS sits above CEOS in the pipeline. DIOS decides what to produce (audience, language, platform, angle, hook). CEOS executes production. AI_VIDEO_MASTER_DOMAIN handles technical video creation. DIOS then distributes and analyzes performance, feeding DISTRIBUTION_MEMORY for compound learning.

Pipeline: `Offer → DIOS (decide) → CEOS (produce) → AI_VIDEO_MASTER_DOMAIN (video) → Publish → DISTRIBUTION_MEMORY (learn) → KNOWLEDGE`

---

## File Structure Map

| File | Action | Responsibility |
|------|--------|---------------|
| `FounderOS/DIOS.md` | Create | Module OS: 8 domains (Market/Audience/Language/Platform/Attention/Conversion/Memory/Analytics) + 12-step workflow |
| `concepts/DISTRIBUTION_MEMORY.md` | Create | New concept: structured campaign memory (hook, audience, language, platform, views, conversions, ROI, learnings) |
| `FounderOS/CEOS.md` | Refactor | Strip sections: Ideation, Distribution, Analysis. Keep: Content Architecture, Script, Story, Direction, Scene, Production |
| `FounderOS/AI_VIDEO_MASTER_DOMAIN.md` | Modify | Add "Distribution Package" after production pipeline (multi-platform, multi-language variants) |
| `FounderOS/SYSTEM_PROMPT.md` | Modify | Add DIOS entry to Intent Classification table |
| `FounderOS/Protocols/SOURCE_OF_TRUTH.md` | Modify | Add DIOS + DISTRIBUTION_MEMORY to truth map |

---

## DIOS Module Specification

### Identity

DIOS (Distribution Intelligence Operating System) is the commercial nervous system of FounderHQ. Its mission: transform any offer into attention, attention into trust, trust into conversion, and conversion into reusable knowledge.

### Inputs

- Product/Offer
- Price
- Target market
- Objective (views, leads, sales)
- Constraints (budget, time, team)
- DISTRIBUTION_MEMORY history

### Outputs

- Audience segment
- Language(s)
- Platform(s)
- Angle(s)
- Hook(s)
- Promise
- Primary objection
- CTA
- Distribution plan (1 offer → N variations)

### 8 Domains

**1. Market Intelligence** — Understand the market: who suffers, who pays, who decides, who influences. Track needs, frustrations, fears, desires, seasonality. Market determines available languages.

**2. Audience Intelligence** — Each product has multiple audiences. Each audience needs a different hook, story, CTA. Not "I sell a product" but "I sell to Audience A, B, C."

**3. Language Intelligence** — Languages are not hardcoded. Derived from Market Intelligence + target country. Examples: Togo (Francais, Ewe, Mina, Pidgin, Kabiye, Tem), Ghana (English, Twi, Ga, Ewe, Hausa, Pidgin), Nigeria (English, Pidgin, Yoruba, Hausa, Igbo, Efik). Each language reduces psychological distance.

**4. Platform Intelligence** — Each platform has a different attention mechanic: TikTok (hook violent, fast rhythm), Facebook (proof, story), WhatsApp (trust, recommendation), YouTube (education, authority), Kora (discovery commerce — to be defined as platform evolves).

**5. Attention Intelligence** — Why someone stops scrolling. Sources: fear, curiosity, desire, money, health, family, status, safety, opportunity. DIOS generates 10-50 hooks per audience, selects best.

**6. Conversion Intelligence** — Why views become sales. Analyze: price, risk, trust, urgency, proof, simplicity, objections. Integrates with FAOS (funnel) and CAOS (pricing).

**7. Distribution Memory** — New concept (`concepts/DISTRIBUTION_MEMORY.md`). Per-campaign record: hook, audience, language, platform, views, engagement, conversions, revenue, ROI, learnings. DIOS queries this before every new campaign.

**8. Distribution Analytics** — Pattern detection across campaigns: which hooks win, which languages convert, which platforms distribute, which CTAs perform, which segments buy. Outputs: reports, rankings, recommendations back to DIOS.

### 12-Step Workflow

1. Receive offer
2. Identify market (Market Intelligence)
3. Identify audience(s) (Audience Intelligence)
4. Choose language(s) (Language Intelligence)
5. Choose platform(s) (Platform Intelligence)
6. Create angle(s) (Attention Intelligence)
7. Create hooks (Attention Intelligence)
8. Choose CTA (Conversion Intelligence)
9. Send to CEOS for production
10. Receive performance data
11. Update DISTRIBUTION_MEMORY
12. Update KNOWLEDGE

### Relation CEOS / DIOS

DIOS decides (who, why, where, when, language, angle). CEOS produces (story, script, direction, scene, production). AI_VIDEO_MASTER_DOMAIN executes technical video creation.

### Relation with Existing Modules

- MOS → feeds DIOS with mission priorities
- CAOS → feeds DIOS with pricing/cash constraints
- FAOS → feeds DIOS with funnel/conversion models
- CEOS → receives DIOS strategy, produces content
- AI_VIDEO_MASTER_DOMAIN → receives CEOS specs, produces video + distribution package
- DISTRIBUTION_MEMORY → stores campaign results, queried by DIOS before each campaign

### KPIs

Reach, Views, Retention, CTR, Messages, Leads, Conversions, Revenue, ROI

---

## DISTRIBUTION_MEMORY Specification

New concept at `concepts/DISTRIBUTION_MEMORY.md`. Per-campaign entry:

```yaml
## Campaign: [ID]
- Date: YYYY-MM-DD
- Product: [name]
- Audience: [segment]
- Language: [language]
- Platform: [platform]
- Hook: "hook text"
- Angle: [angle description]
- CTA: [call to action]
- Views: N
- Engagement: N (likes + comments + shares)
- Conversions: N
- Revenue: N FCFA
- Cost: N FCFA
- ROI: N.Nx
- Learnings: "what worked, what didn't"
- Next: "what to try next time"
```

DIOS queries DISTRIBUTION_MEMORY before strategy generation to find patterns.

---

## CEOS Refactor

Remove from CEOS.md:
- `## Content Pipeline` Phase 1 (Ideate) — moves to DIOS
- `## Content Pipeline` Phase 3 (Distribute) — moves to DIOS
- `## Content Pipeline` Phase 4 (Analyze) — moves to DIOS

Keep in CEOS.md:
- `## Content Domains` (4 domains)
- `## Content Pipeline` Phase 2 (Produce) — renamed to full production workflow
- `## Integration` — simplified (DIOS input + AI_VIDEO_MASTER_DOMAIN output)

---

## AI_VIDEO_MASTER_DOMAIN Modification

Add a "Distribution Package" output stage after Production Pipeline:

```
CONTENT
→ DISTRIBUTION STRATEGY (from DIOS)
→ SCRIPT (from CEOS)
→ SCENES
→ VIDEO
→ LOCALIZATION (per language)
→ PLATFORM VARIATIONS (per platform)
→ DISTRIBUTION PACKAGE (title, description, tags, thumbnail per platform)
```

---

## Verification Criteria

1. DIOS.md contains all 8 domains with actionable content
2. DISTRIBUTION_MEMORY.md has correct YAML structure
3. CEOS.md no longer contains Ideation, Distribution, or Analysis phases
4. AI_VIDEO_MASTER_DOMAIN.md has Distribution Package section
5. SYSTEM_PROMPT.md Intent Classification table includes DIOS entry
6. SOURCE_OF_TRUTH.md has DIOS + DISTRIBUTION_MEMORY entries
7. No broken cross-references (CEOS still references AI_VIDEO_MASTER_DOMAIN, etc.)

---

## Footer

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | CEOS, AI_VIDEO_MASTER_DOMAIN, SYSTEM_PROMPT, SOURCE_OF_TRUTH |
