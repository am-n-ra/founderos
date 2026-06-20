# ASSET

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 8.

## Role

Represent reusable resources.

An asset is anything of value that can be used across projects, missions, or time.

---

## Core Rule

An asset entry tracks existence, location, and status.

An asset entry does NOT contain knowledge about how to use the asset.

Usage knowledge belongs in KNOWLEDGE or WORKFLOW.

---

## Structure

Each asset entry should include:

**ASSET_ID** — unique identifier

**NAME** — what this asset is called

**TYPE** — category (Content, Code, Design, Relationship, Inventory, Tool, Document, Other)

**LOCATION** — where the asset resides (file path, URL, physical location, contact)

**STATUS** — Available / In Use / Depleted / Obsolete

**PROJECT_ORIGIN** — which project created this asset (if applicable)

**PROJECTS_USING** — which projects currently use this asset

**NOTES** — brief operational notes (not knowledge, not instructions)

---

## Current Assets

---

**ASSET_ID:** A-001

**NAME:** Stop Nuisibles TikTok Account

**TYPE:** Relationship (platform account)

**LOCATION:** @stopnuisibles228 on TikTok

**STATUS:** Available

**PROJECT_ORIGIN:** SN-001 (Video 1)

**PROJECTS_USING:** SN-002 (Variation #2), SN-003 (Video 2)

**NOTES:** 5 followers as of 2026-06-18, 0 posts before SN-001

---

**ASSET_ID:** A-002

**NAME:** Pest Repeller Inventory

**TYPE:** Inventory

**LOCATION:** Physical stock in Lomé

**STATUS:** Available (100 units)

**PROJECT_ORIGIN:** None (purchased directly, not produced by a project)

**PROJECTS_USING:** SN-001, SN-002, SN-003, FO-002

**NOTES:** Cost 4,000 FCFA/unit, selling price 5,900 FCFA, margin 1,900 FCFA. Supplier contact documented but reorder process not yet complete.

---

**ASSET_ID:** A-003

**NAME:** Video 1 Production Sheets

**TYPE:** Content (documents)

**LOCATION:** Projects/Stop Nuisibles/CONTENT/ (VIDEO1_PRODUCTION.md, VIDEO1_TIMING_MAP.md, SCRIPTS_J1.md, PRODUCT_SHEET.md, CONTENT_PROCESS.md)

**STATUS:** Available

**PROJECT_ORIGIN:** SN-001

**PROJECTS_USING:** SN-002 (reference for adaptation)

**NOTES:** Includes timing map, storyboard, prompts, voiceover script. Applicable to future videos with hook modifications.

---

**ASSET_ID:** A-009

**NAME:** DoodleMind YouTube Channel

**TYPE:** Relationship (platform account)

**LOCATION:** YouTube — DoodleMind channel (English, niche psycho/histoire/cerveau)

**STATUS:** Available (0 subscribers, 0 videos published)

**PROJECT_ORIGIN:** DM-001 (DoodleMind Channel Launch)

**PROJECTS_USING:** DM-001

**NOTES:** Channel created 2026-06-19. Short #1 script and 30 image prompts in KnowledgeAssets/. Target audience US/AU. Format: 9:16 hand-drawn doodle, 30-60s. YouTube Short #1 analytics from cross-post: 335 views, 72.8% retention, 87.5% like rate, 28.6% CTR.

---

**ASSET_ID:** A-010

**NAME:** Soya Supplier Contacts

**TYPE:** Relationship (supplier)

**LOCATION:** Phone numbers in MEMORY.md (Recent Decisions)

**STATUS:** Available (not yet contacted)

**PROJECT_ORIGIN:** SS-001 (Soya Supplier Sourcing)

**PROJECTS_USING:** SS-001

**NOTES:** 7 suppliers found 2026-06-19: Ste SODJA (96 68 43 65), SCOOPS AKPENE SOJA (91 58 84 56), SOYCAIN (91 73 66 83), CIFS TOGO (91 11 44 40), AGROKOM TOGO (90 01 44 41), MAMAN SOJA (92 62 64 68), SOCMEL (99 46 89 34). Existing suppliers from earlier research: AGROTRADE, TOGO SOJA, IVEMA. Need to call to confirm: price per bol, minimum order, delivery terms, payment terms.

---

**ASSET_ID:** A-011

**NAME:** DoodleMind Short #1 Assets

**TYPE:** Content

**LOCATION:** concepts/KnowledgeAssets/short_why_your_brain_forgets_dreams.txt, concepts/KnowledgeAssets/prompts_why_your_brain_forgets_dreams.txt

**STATUS:** Available (not yet used)

**PROJECT_ORIGIN:** DM-001 (DoodleMind Channel Launch)

**PROJECTS_USING:** DM-001

**NOTES:** Script + 30 image prompts + metadata (title, description, tags) for "Why Your Brain Forgets Your Dreams." Images not yet generated. Video not yet published.

---

**ASSET_ID:** A-004

**NAME:** WhatsApp Business Account

**TYPE:** Relationship (communication channel)

**LOCATION:** +228 71 39 21 22

**STATUS:** Available

**PROJECT_ORIGIN:** None

**PROJECTS_USING:** FO-002 (First Revenue), all Stop Nuisibles projects

**NOTES:** Primary sales channel. Number changed from 91 to 71 before Video 1 publish.

---

**ASSET_ID:** A-005

**NAME:** Zoclo Livraison Content Pack

**TYPE:** Content (archived)

**LOCATION:** Archive/Zoclo Livraison/ (SCRIPTS_J1-7.md, CONTENT_MATRIX.md, ASSETS/BRAND_GUIDE.md)

**STATUS:** Available (archived)

**PROJECT_ORIGIN:** Zoclo Livraison (archived mission)

**PROJECTS_USING:** None (pattern reference only)

**NOTES:** 30-day content calendar, 21 scripts, complete brand guide. Reusable content framework (hook→problem→solution→proof→CTA). Product-specific content (Postinor 2 delivery) not reusable but structural patterns are.

---

**ASSET_ID:** A-006

**NAME:** FounderOS Foundation Documents

**TYPE:** Document (system)

**LOCATION:** FounderOS/ (MANIFEST, CONCEPT_REGISTRY, BOUNDARIES, PROTOCOL, TEMPORAL_AWARENESS, AUDIT, RELATIONSHIP_MODEL)

**STATUS:** Available

**PROJECT_ORIGIN:** FO-001 (FounderOS v2 Reconstruction)

**PROJECTS_USING:** FO-001 (active), all future projects (via protocol)

**NOTES:** 7 foundation documents as of 2026-06-18. These define FounderHQ itself and are referenced by every operation.

---

**ASSET_ID:** A-007

**NAME:** Supplier Contact — Pest Repeller

**TYPE:** Relationship (supplier)

**LOCATION:** Documented in Projects/Stop Nuisibles/SUPPLIER/ (two files exist, need consolidation)

**STATUS:** Available (incomplete — missing phone, payment terms, reorder process)

**PROJECT_ORIGIN:** None

**PROJECTS_USING:** FO-002 (First Revenue), all Stop Nuisibles projects

**NOTES:** Current supplier at 4,000 FCFA/unit. Sold 2,000 units of previous version. Reorder process not documented — critical gap for scaling.

---

## Content-Type Subtypes

For video production and creative assets, use these subtypes under the TYPE field:

- **Entity** — character, product, object (has ENTITY_SHEET)
- **Environment** — location, setting (has ENVIRONMENT_SHEET)
- **Scene** — entity + environment composition (has SCENE_SHEET)
- **Shot** — framed camera composition (has SHOT_SHEET)
- **Prompt** — generation prompt used to create an asset
- **Script** — written content script
- **Audio** — voiceover, music, sound effect
- **Video** — raw or assembled video clip
- **Thumbnail** — cover image for video

---

## Brand Identity

**ASSET_ID:** A-008

**NAME:** FounderHQ Brand Identity

**TYPE:** Design

**LOCATION:** concepts/ASSET.md (this entry) + visual files in Projects/ as they are created

**STATUS:** Available

**PROJECT_ORIGIN:** FounderHQ (root mission)

**PROJECTS_USING:** All projects (inherited)

**NOTES:**
- Tone: Direct, sans bullshit / Technique mais pas jargon / Africain mais pas "folklore" / Confiant mais pas arrogant
- Brand Pillars: Innovation accessible, Clarté radicale, Exécution méthodique
- Visual: Minimaliste, sombre, sérieux, accent orange/rouge, photos réelles pas de stock
- Tagline: "Construit pour durer. Conçu pour l'Afrique."

---

## Story Bible

**ASSET_ID:** Template — Story Bible

**TYPE:** Document

**STRUCTURE:** PROJECT_NAME, MISSION, AUDIENCE, CONTENT OBJECTIVE, VISUAL IDENTITY (color palette, lighting, camera style, typography), NARRATIVE IDENTITY (tone, pacing, emotion, narration style), BRAND IDENTITY (values, positioning, voice), RECURRING ENTITIES, RECURRING LOCATIONS, CONTENT RULES, FORBIDDEN RULES

**INHERITANCE CHAIN:** Story Bible → Entity Registry → Scenes → Assets

**NOTES:** A video is temporary. A project universe is persistent. The Story Bible is the source of truth for all content belonging to a project, brand, campaign, documentary, channel, podcast or series. All future content inherits through the chain above.

---

## Series Bible

**ASSET_ID:** Template — Series Bible

**TYPE:** Document

**STRUCTURE:** SERIES_NAME, MISSION, AUDIENCE, FORMAT, NARRATIVE ARC, RECURRING ENTITIES, RECURRING LOCATIONS, VISUAL RULES, AUDIO RULES, CONTINUITY RULES, EPISODE TRACKER

**EPISODE TRACKER:** EPISODE_ID, DATE, SUMMARY, KEY EVENTS, NEW ENTITIES, NEW LOCATIONS, LESSONS

**NOTES:** A single video is an asset. A series is an ecosystem. The Series Bible maintains continuity across episodes. Series can evolve; changes must be recorded.

---

## Asset Management Rules

1. An asset is not knowledge. Do not store usage instructions in ASSET.
2. **Reuse Rule:** Before creating a new asset, search the registry. If it exists: reuse, update, version. Do not duplicate.
3. **Continuity Gate:** Before creating a new asset in a series, verify consistency with the Series Bible and all previous episodes.
4. An asset's status must be updated when it changes (sold, consumed, transferred).
5. An asset created by a project should be added here when the project completes.
6. An asset that is not used by any project for 90 days may be archived.
7. An asset that is obsolete should be marked as Obsolete, not deleted.

---

## Footer

Last updated: 2026-06-20 (added: A-009 DoodleMind YouTube channel, A-010 Soya supplier contacts, A-011 DoodleMind Short #1 assets)

Assets compound over time.

A young system has few assets.

A mature system has many.

Asset tracking prevents rebuilding what already exists.
