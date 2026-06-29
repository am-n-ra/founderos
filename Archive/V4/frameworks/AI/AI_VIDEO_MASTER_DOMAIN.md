# AI Video Production — Entity-Based Framework

## When to Use This Lens

AI video production with recurring entities (characters, products, environments).

## Core Principle

AI Video is not about prompts. AI Video is about entities. Prompts are generated from entities.

Every element visible on screen is an entity. Consistency is achieved through entity persistence.

## Required Structure Before Production

1. **Entity Registry** — ENTITY_REGISTRY.md with ENTITY_ID, Type, Name
2. **Entity Sheets** — PERSON_SHEET, PRODUCT_SHEET, LOCATION_SHEET per entity
3. **Environment System** — light, atmosphere, weather, mood, color palette
4. **Action System** — reusable actions: Actor (ENTITY_ID), Action, Object, Emotion, Duration
5. **Scene System** — entities + environment + actions + narrative objective
6. **Frame System** — START_FRAME, END_FRAME mandatory before generation
7. **Video Prompt Generation** — downstream, only after all dependencies exist

## Quality gates

- Entity Sheets exist ✓
- Environment Sheets exist ✓
- Action Sheets exist ✓
- Scene Sheets exist ✓
- Frame Assets exist ✓

If a gate is red: STOP. Generate the missing assets before continuing.

## FounderOS Rule

Don't think in prompts. Think in entities.
Don't think in clips. Think in scenes.
Don't think in videos. Think in systems.

## Content types supported

ADVERTISEMENT, DOCUMENTARY, PODCAST, EDUCATIONAL, STORYTELLING, FOUNDER_JOURNAL, NEWS
