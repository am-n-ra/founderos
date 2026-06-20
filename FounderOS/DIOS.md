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

## Domain 7: Distribution Memory

Mission: Accumulate market intelligence from every campaign.

DIOS queries DISTRIBUTION_MEMORY before every new campaign to find:
- Which hooks won for this audience?
- Which language converted best?
- Which platform distributed furthest?
- Which CTA drove action?

DISTRIBUTION_MEMORY is stored as a concept at concepts/DISTRIBUTION_MEMORY.md.

Each campaign entry captures: hook, audience, language, platform, views, engagement, conversions, revenue, ROI, learnings.

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

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
| Dependencies | CEOS.md, AI_VIDEO_MASTER_DOMAIN.md, DISTRIBUTION_MEMORY.md |
