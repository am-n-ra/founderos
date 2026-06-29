# FounderOS V4 — AI_VIDEO_MASTER_DOMAIN

## Purpose

The AI_VIDEO_MASTER_DOMAIN is the complete video production system for DoodleMind. It covers scripting, production, optimization, and distribution packaging.

## Position in FounderHQ

AI_VIDEO_MASTER_DOMAIN is the specialized video production engine within the content supply chain. It is loaded when CEOS requires video content or when the founder asks to produce video. It feeds finished videos and performance data back to CEOS.

## Inputs
- `FounderOS/concepts/CEOS.md` — content briefs requiring video
- Content Repository — brand assets, stock footage, music, templates
- Platform specs — resolution, duration, format per platform

## Outputs
- Video assets — exported videos ready for distribution
- Thumbnails and metadata — title, description, tags per platform
- Performance data — views, retention, engagement by platform
- Production templates — reusable workflows for similar videos

## Relations
- **CEOS** — receives briefs, returns finished videos and performance data
- **CEOS** — receives distribution schedule for video publishing
- **TIMELINE** — production milestones recorded

## Workflow

### Content Types

### 1. DoodleMind Long-Form (YouTube)
- Educational entertainment doodle videos
- 5-15 minutes
- Focus: curiosity-driven storytelling
- Platform: YouTube

### 2. DoodleMind Shorts (YouTube / TikTok)
- Vertical short-form doodle content
- 15-60 seconds
- Focus: hook retention, viral mechanics
- Platform: YouTube Shorts, TikTok

### Production Pipeline

### Pre-Production
1. **Ideation**: 10 ideas → filter by production cost vs. audience interest → select 1
2. **Research**: LEOS/RIOS research on topic
3. **Script**: Write with hook, body, CTA structure
4. **Storyboard**: Visual sequence for doodle animation
5. **Asset Checklist**: What images, audio, elements needed

### Production
1. **Audio**: Record voiceover (or generate via AI), edit for clarity and pacing
2. **Visual**: Create doodle animation per storyboard. For entity-based AI video production, load `Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md` (V2 entity framework for character/setting consistency).
3. **Music/SFX**: Background track, sound effects (hook layer priority: audio > visual > text)
4. **Edit**: Synchronize audio + visual, add text overlays

### Post-Production
1. **Thumbnail**: High-contrast, curiosity-driven, face/emotion if possible
2. **Title**: Curiosity gap, keyword-optimized
3. **Description**: SEO-rich, timestamps, links
4. **Tags**: Relevant keywords, niche + broad
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
1. **First 24h**: Views, retention, engagement
2. **Hook Analysis**: At what second do viewers drop? (YouTube Analytics)
3. **Compare**: Against previous videos, against benchmarks
4. **Learn**: Store in KNOWLEDGE.md

### Hook Layer Priority

When optimizing retention, prioritize in this order:
1. **Audio** (voice tone, pacing, background music, sound effects) — strongest retention driver
2. **Visual** (animation quality, movement, color, cuts) — second strongest
3. **Text** (captions, text overlays) — weakest alone, effective combined with audio+visual

Changing text alone produces minimal retention improvement (confirmed: 0:03 drop unchanged).

### Equipment & Tools

- AI voice generation
- AI image/animation generation
- Video editing software
- Audio editing software
- Thumbnail design tool

### Integration

- AI_VIDEO_MASTER_DOMAIN is loaded by CEOS for video production
- AI_VIDEO_MASTER_DOMAIN receives research from LEOS/RIOS
- AI_VIDEO_MASTER_DOMAIN reports performance data to CEOS for optimization

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
