# DIOS — DISTRIBUTION_MEMORY

## Mission

Accumulate market intelligence from every campaign so DIOS gets smarter with every post.

## Core Rule

The canonical DISTRIBUTION_MEMORY lives at `concepts/DISTRIBUTION_MEMORY.md`. This sub-module defines HOW DIOS reads from and writes to it.

## Read Before Every Campaign

Before DIOS generates a new distribution strategy, query DISTRIBUTION_MEMORY for:

1. Which hooks won for this audience?
2. Which language converted best?
3. Which platform distributed furthest?
4. Which CTA drove action?
5. Which objections were most common?

## Write After Every Campaign

After each campaign, update DISTRIBUTION_MEMORY with:

```
Campaign: [name]
Product: [product]
Audience: [primary segment]
Language: [language used]
Platform: [platform used]
Hook: [hook text]
CTA: [call to action]
Views: [number]
Engagement: [likes, comments, shares]
Messages: [WhatsApp DMs received]
Conversions: [sales]
Revenue: [FCFA]
Cost: [production + distribution cost]
ROI: [(revenue - cost) / cost]
Lesson: [what to repeat or stop]
```

## Learning Loop

```
Campaign → Data → DISTRIBUTION_MEMORY → Pattern Detection → KNOWLEDGE update → Better DIOS strategy → Next campaign
```

## Pattern Detection

After 3+ campaigns with the same product, DIOS should identify:

- Best hook pattern (which attention source converts?)
- Best language (which language generates DMs?)
- Best platform (which platform drives sales?)
- Best CTA (which instruction gets action?)

These patterns are promoted to `concepts/KNOWLEDGE.md` as validated truths.

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Last Verified | 2026-06-21 |
| Owner | DIOS |
| Dependencies | concepts/DISTRIBUTION_MEMORY.md, concepts/KNOWLEDGE.md |
