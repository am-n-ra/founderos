# AI Video Production Workflow (Entity-Based)

## Pipeline (strict order)

```
 1. CONTENT TYPE SELECTION
    → ADVERTISEMENT, DOCUMENTARY, PODCAST, EDUCATIONAL, STORYTELLING, FOUNDER_JOURNAL, NEWS

 2. STORY BIBLE (PROJECT_BIBLE.md)
    → Mission, audience, visual identity, narrative identity, brand identity
    → Recurring entities, locations, content rules, forbidden elements
    → Locks the look & feel of the entire campaign
    → REQUIREMENT: MUST include a ## GENERATION section (LLM prompt used to synthesize)
    → VALIDATION: propose content to founder before writing

 3. OFFER.md (if ad) / OBJECTIVE.md (other types)
    → Pain, audience, value prop / Purpose, audience, goal
    → REQUIREMENT: MUST include a ## GENERATION section (LLM prompt used to synthesize)
    → VALIDATION: propose content to founder before writing

 4. CREATIVE_STRATEGY.md
    → Hook, emotion, angle, CTA / Narrative angle
    → REQUIREMENT: MUST include a ## GENERATION section (LLM prompt used to synthesize)
    → VALIDATION: propose content to founder before writing

 5. SCRIPT.md
    → Beginning, middle, end, CTA
    → REQUIREMENT: MUST include a ## GENERATION section (LLM prompt used to synthesize)
    → VALIDATION: propose content to founder before writing

 6. ENTITY_REGISTRY.md
    → Lists all entities (PERSON, PRODUCT, LOCATION, etc.)
    → Each entity gets a unique ID (ENTITY_001, ENTITY_002...)
    → REQUIREMENT: MUST include a ## GENERATION section (LLM prompt used to synthesize)
    → VALIDATION: propose content to founder before writing

 7. ENTITY_SHEETS (1 per entity) — MULTI-ANGLE TURNAROUND
    → Character, product, animal, object — neutral state, multiple angles
    → e.g. face + 3/4 + profile for a person, front + side + top for a product
    → Neutral background (gray, white) — no context, no setting
    → Serves as visual CONSISTENCY LOCK for the entire campaign
    → Generated with or without real photos as reference
    → REQUIREMENT: each sheet MUST include a GENERATION prompt
    → VALIDATION: propose content + generation prompt to founder before writing

 8. ENVIRONMENT_SHEETS
    → Neutral state of the setting (empty, no characters, baseline lighting)
    → Color palette, camera style, atmosphere
    → REQUIREMENT: MUST include a GENERATION section (Tool + Prompt + Format + Ingredients)
    → REQUIREMENT: MUST include a POSITIONAL LAYOUT section (floor plan or spatial description: where objects/sockets/windows are positioned, distances, heights)
    → VALIDATION: propose content + generation prompt to founder before writing

 9. ACTION_SHEETS (1 per action)
    → Actor (ENTITY_ID — MUST be a valid ENTITY_ID, not a description) + Action + Object (ENTITY_ID — MUST be a valid ENTITY_ID or None) + Emotion + Duration
    → BEFORE creating: verify the narrative arc is complete
    → Problem → False solution → Real solution → Resolution
    → If a step is missing, DO NOT create actions — fix the script first
    → REQUIREMENT: MUST include a ## GENERATION section (Tool + Prompt + Format + Ingredients) — reference image showing a key frame of the action
    → VALIDATION: propose content + generation prompt to founder before writing

10. SCENE_SHEETS (1 per narrative scene)
    → ENTITY_IDs present + ENVIRONMENT + ACTION_ID + Mood + Camera
    → A scene may contain multiple shots
    → NO new image generation. The GENERATION section REFERENCEs already-existing ACTION_SHEET images as visual references. Tool = LLM (synthesis from existing sheets).
    → REQUIREMENT: MUST include a ## GENERATION section (Tool: LLM, prompt: synthesis from script + action sheets, Format: text). Ingredients MUST reference the action sheet images already generated.
    → VALIDATION: propose content to founder before writing

11. SHOT_SHEETS (1 per shot = 1 video clip)
    → Parent scene + Camera angle + Duration + Specific action
    → Important for Veo: each clip = 1 shot
    → NO new image generation. SHOT_SHEET feeds into START_FRAMES for image generation. GENERATION section = text synthesis prompt.
    → REQUIREMENT: MUST include a ## GENERATION section (Tool: LLM, prompt: synthesis from scene + action sheets, Format: text)
    → VALIDATION: propose content to founder before writing

12. START_FRAMES — OPTIONAL (1 per shot, only if needed)
    → Generated from SHOT_SHEET + ENTITY_SHEETS + ENVIRONMENT
    → If shot maps 1:1 to an action (shot == action): START_FRAME = existing ACTION_SHEET image. No new generation.
    → If shot needs a distinct start visual: generate new START_FRAME image (NanoBanana Pro)
    → REQUIREMENT: if generated, MUST include a ## GENERATION section (NanoBanana Pro prompt)
    → VALIDATION: propose generated frame to founder before proceeding

13. END_FRAMES — OPTIONAL (1 per shot, only if needed)
    → Resolved state / end of shot
    → If shot ends in a different visual state than it starts: generate END_FRAME (NanoBanana Pro)
    → If shot ends at same state as start: END_FRAME = START_FRAME. No new generation.
    → REQUIREMENT: if generated, MUST include a ## GENERATION section (NanoBanana Pro prompt)
    → VALIDATION: propose generated frame to founder before proceeding

14. VIDEO_PROMPTS (1 per shot)
    → Start Frame + End Frame + all reference sheets
    → If no START/END_FRAMES generated: use ACTION_SHEET images as frame references
    → Describes motion, camera, lighting, timing, duration
    → REQUIREMENT: MUST include a ## GENERATION section (LLM prompt used to synthesize)
    → VALIDATION: propose prompt to founder before generating

15. GENERATION
    → Veo / Kling / Runway
    → VALIDATION: show generated clips to founder before assembly

 16. ASSEMBLY + PUBLISHING
    → Editing, TTS, music, overlay text, subtitles
    → Music: recommend a specific track or style (royalty-free, mood-matching)
    → Metadata: propose TITLE + CAPTION + HASHTAGS + CTA for the platform (TikTok, Instagram, etc.)
    → REQUIREMENT: MUST capture TIMING MAP (shot-by-shot: Shot #, Action, Start time, End time, Duration) — this enables future TTS variations without guesswork
    → REQUIREMENT: MUST include ## METADATA section (platform, title, caption, hashtags, music recommendation, total duration)
    → REQUIREMENT: MUST include ## TIMING MAP section with each shot's start/end in seconds
    → REQUIREMENT: MUST include ## POST_PRODUCTION section — logs EVERY modification made to the raw ASSEMBLY output before publishing: text overlays (content, position on screen, timing start/end), music track used, transitions, speed changes, color grading, TikTok/IG effects. This section is the SINGLE SOURCE OF TRUTH for what viewers actually saw.
    → VALIDATION: show final video + metadata + timing map + post-production log to founder before publishing
```

---

## GENERATION REQUIREMENT

Every sheet MUST include a `## GENERATION` section with:
- **Tool**: the tool used (e.g. NanoBanana Pro, Midjourney, Veo)
- **Prompt**: exact prompt used to generate the reference visual
- **Format**: ratio, resolution
- **Ingredients**: reference files, colors, styles, moodboards

## PROMPT LANGUAGE RULE

All AI generation prompts (image, video, LLM) MUST be in English. AI models are English-optimized and produce higher quality results with English prompts.

Target-market content (TTS voiceover, on-screen text, TikTok captions, titles) MUST be in the audience's language (e.g. French for Lomé, Togo).

Exception: if a model natively supports the target language (check the model's prompting guidelines), the prompt MAY use that language instead of English.

## INGREDIENTS COMPLETENESS RULE

The `Ingredients` field in every GENERATION section MUST include ALL ENTITY_IDs referenced in the Prompt text. If a prompt mentions a character's body part (hand, face, etc.), the corresponding ENTITY_ID MUST be in Ingredients. This ensures the model receives the correct visual reference for every element.

## REAL REFERENCES (Recommended when available)

For a real entity (physical product, real person, actual location):
```
1. Take a real photo (or several from different angles)
2. Use it directly as the ENTITY_SHEET
3. Or upload it as reference in the generation tool to create a clean image
```

If no photo available: generate the reference image directly from a prompt.

## VALIDATION RULE (GENERAL)

For every document created in this workflow:

```
1. PROPOSE: show the proposed content + generation prompt to the founder
2. CONFIRM: wait for explicit founder validation
3. WRITE: persist to file only after confirmation
```

Never write a file without showing and validating it first.

---

## TOOLS BY STEP

| Step | Tool | Generation Prompt |
|------|------|------------------|
| 2. STORY_BIBLE | LLM (OpenCode) | Synthesize from Product Sheet + Brand Guide |
| 3. OFFER | LLM | Synthesize from Product Sheet + Story Bible |
| 4. CREATIVE_STRATEGY | LLM | From OFFER + Script |
| 5. SCRIPT | LLM | From Creative Strategy |
| 6. ENTITY_REGISTRY | LLM | Synthesize from Script + Product Sheet |
| 7. ENTITY_SHEETS | LLM + NanoBanana Pro | Reference image prompt + description |
| 8. ENVIRONMENT_SHEETS | LLM + NanoBanana Pro | Reference image prompt |
| 9. ACTION_SHEETS | LLM | From Script + Entity Sheets |
| 10. SCENE_SHEETS | LLM | From Script + Entity + Action + Environment |
| 11. SHOT_SHEETS | LLM | From Scene Sheets |
| 12. START_FRAMES | NanoBanana Pro | Prompt from SHOT_SHEET + ENTITY_SHEETS + ENVIRONMENT |
| 13. END_FRAMES | NanoBanana Pro | Prompt from SHOT_SHEET + ENTITY_SHEETS + ENVIRONMENT |
| 14. VIDEO_PROMPTS | LLM | Synthesis of all sheets + frames |
| 15. GENERATION | Veo / Kling / Runway | VIDEO_PROMPTS + START_FRAMES |
| 16. ASSEMBLY | Video editor | Clips + TTS + music |

---

## Consistency rules
- ENTITY_REGISTRY defines ALL campaign entities
- ACTION and SCENE reference ENTITY_ID
- Never generate VIDEO_PROMPT without ENTITY_SHEETS + SCENE_SHEETS
- Never write a file without prior founder validation
- Every sheet MUST have a GENERATION section with tool + prompt + ingredients
- START/END_FRAMES are OPTIONAL: if shot == action, ACTION_SHEET image = START_FRAME (no new generation)
- ASSEMBLY must produce TIMING MAP for every video: used for all future TTS variations
- TTS variations MUST use the TIMING MAP from the original video, never guess shot durations

## Don'ts
- Script → Video Prompt (skips steps)
- Changing entity appearance between shots
- Generating without start/end frames
- Writing a file without showing it to the founder first
- Creating a sheet without a GENERATION section
