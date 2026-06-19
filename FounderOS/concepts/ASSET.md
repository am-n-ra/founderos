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

Last updated: 2026-06-18 (added: brand identity, story/series bible templates, content subtypes, reuse rule, continuity gate)

Assets compound over time.

A young system has few assets.

A mature system has many.

Asset tracking prevents rebuilding what already exists.
