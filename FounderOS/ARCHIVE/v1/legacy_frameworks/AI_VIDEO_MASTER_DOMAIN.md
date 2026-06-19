# AI_VIDEO_MASTER_DOMAIN V2

## Purpose
Produce consistent, scalable, reusable AI-generated visual content.

## Prime Directive
AI Video is not about prompts. AI Video is about entities. Prompts are generated from entities.

## Core Principle
Everything visible on screen is an entity. Consistency is achieved through entity persistence.

## Entity Types
PERSON, PRODUCT, LOCATION, ORGANIZATION, BRAND, ANIMAL, OBJECT, VEHICLE, CONCEPT, EVENT.

## Entity Registry
All entities registered before production. ENTITY_REGISTRY.md with ENTITY_ID, Type, Name.

## Entity Sheets
- PERSON_SHEET: name, age, gender, appearance, skin tone, hair, clothing, voice, expressions, personality
- PRODUCT_SHEET: name, brand, shape, dimensions, material, color, texture, logo, visual identifiers
- LOCATION_SHEET: architecture, lighting, weather, furniture, textures, mood, colors, time of day
- ORGANIZATION_SHEET: name, mission, logo, visual identity, colors, tone, brand rules
- OBJECT_SHEET: appearance, material, color, scale, function
All sheets have CONSISTENCY LOCK.

## Environment System
Independent from entities. Defines: lighting, atmosphere, weather, time, mood, color palette, camera style, visual style.

## Action System
Reusable actions. ACTION_SHEET with: Actor (ENTITY_ID), Action, Object (ENTITY_ID), Emotion, Duration.

## Scene System
Combines entities + environment + actions. SCENE_SHEET with: entities list, environment, actions, narrative purpose, emotional goal, camera direction.

## Frame System
Before video: START_FRAME, END_FRAME (optional: MID_FRAMEs). Generated from Scene Sheets + Entity Sheets + Environment Sheets.

## Video Prompt Generation
Downstream asset. Depends on: Scene Sheet, Entity Sheets, Environment Sheet, Action Sheet, Start Frame, End Frame. Only after all dependencies exist.

## Content Types
- ADVERTISEMENT: Customer Profile, Offer, Product Entity, CTA
- DOCUMENTARY: Fact Validation, Historical Entities, Narration Plan, Research Sources
- PODCAST: Host Sheet, Guest Sheet, Studio Sheet, Outline, Talking Points
- EDUCATIONAL: Learning Objective, Teaching Plan, Examples, Visual Demonstrations
- STORYTELLING: Characters, Narrative Arc, Conflict, Resolution
- FOUNDER_JOURNAL: Founder Sheet, Mission Context, Current Challenge, Lesson, Takeaway
- NEWS: Sources, Fact Validation, Timeline, Narration

## Quality Gates
Before generation: Entity Sheets exist ✓ Environment Sheets exist ✓ Action Sheets exist ✓ Scene Sheets exist ✓ Frame Assets exist ✓. If not: STOP. Generate missing assets.

## FounderOS Rule
Do not think in prompts. Think in entities. Do not think in clips. Think in scenes. Do not think in videos. Think in systems.
