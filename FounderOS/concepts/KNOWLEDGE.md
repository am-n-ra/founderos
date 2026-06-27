# KNOWLEDGE

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 4.

## Role

Store validated truths, patterns, principles, and domain expertise.

Knowledge evolves slowly.

Knowledge compounds over time.

Nothing validated should be lost.

---

## Distribution Intelligence

### DIOS Pipeline (validated 2026-06-20)

Distribution strategy must precede content production. The order is:
1. DIOS decides (audience, language, platform, hook, angle, CTA)
2. CEOS produces (story, script, direction, scene)
3. AI_VIDEO_MASTER_DOMAIN executes (video, localization, platform variations, distribution package)
4. DISTRIBUTION_MEMORY learns (campaign results → pattern detection)

**Validated truth:** Producing content without first defining audience, language, and platform hook is guessing. DIOS eliminates the guesswork before CEOS spends production effort.

### Language is Market-Derived (validated 2026-06-20)

Languages are not hardcoded. They are derived from the target market/country. Example markets:
- Togo: Francais, Ewe, Mina, Pidgin, Kabiye, Tem
- Ghana: English, Twi, Ga, Ewe, Hausa, Pidgin
- Nigeria: English, Pidgin, Yoruba, Hausa, Igbo, Efik

### Concept Registration (validated 2026-06-20)

New concepts must be registered in CONCEPT_REGISTRY.md with a Concept number, Layer, Purpose, Properties, and Invariant truth. New concept files must follow the established pattern: all-caps title, Concept section linking to registry, Role section, prose footer.

## Video Content Principles

### Hook Structure

- TikTok hook must create a pattern interrupt in the first 1-2 seconds
- Audio hook must be active (question, sound effect, surprise) — passive audio loses viewers at 0:03
- Text overlay must appear immediately for mute viewers (98% of TikTok)
- Dark first frame reduces contrast on For You page — use bright or high-contrast opening

### TikTok Mechanics

- 98.7% For You traffic means the algorithm considers content distributable — the problem is retention, not reach
- Average watch time of 10.3s on a 21s video (49%) is above TikTok's typical threshold for continued distribution
- Drop at 0:03 indicates the hook is the bottleneck, not the content quality after the hook
- AI-generated video may trigger uncanny valley on local feeds — real smartphone footage builds trust

### Hook Layer Priority (validated 2026-06-18 — 2 videos, same drop pattern)

The hook operates on THREE layers, in priority order:

1. **AUDIO layer** — a sound, a scream, a buzz, a surprise. This is the fastest to reach the brain. Text alone is too slow.
2. **VISUAL layer** — a face, a zoom, a sudden movement, a bright flash. Something that breaks the scroll pattern visually.
3. **TEXT layer** — text overlay. Only works if audio AND visual have already stopped the scroll.

**Validated truth:** Changing the TEXT hook without changing the AUDIO/VISUAL opening produced the same 0:03 drop across 2 videos. Text alone cannot fix a hook problem. Audio/visual layer must be addressed first.

### Facebook vs TikTok

- Facebook audience for new pages is primarily older (55-64 observed) — content must be adapted
- No text overlay on Facebook = 0 link clicks (observed)
- Music and text overlay are not optional on Facebook — they are requirements for engagement
- 9:16 vertical has lower priority on Facebook than 1:1 or 16:9

### Engagement Tactics (Lomé Audience)

- Direct instructions outperform implicit invitations. "Commentes 'Moi aussi' si..." generates more comments than "Qui d'autre ?" because the action is explicit and low-effort.
- Audience education level: prompts must be literal, not suggestive. Tell people exactly what to type and why.
- Relatable problem + direct instruction + low effort = highest comment rate.

### Offer Design

- 5 followers = zero social proof. Scarcity or discount incentive is required for first sales.
- "Premiers 10 clients : 4,500 FCFA au lieu de 5,900" creates urgency and compensates for lack of trust.
- WhatsApp CTA must include the number in the video frame, not just "link in bio."

---

## FounderOS Design Principles

### System Invariants

Defined in FOUNDERHQ_MANIFEST.md — 9 invariants that cannot be broken.

Key validated truths from implementation experience:

- Concept overlap is the primary cause of system decay. CONCEPT_BOUNDARIES.md is the prevention.
- A concept must be identifiable but not tied to a specific implementation path.
- The smallest recoverable unit is FOUNDERHQ_MANIFEST.md. If it survives, the system can be rebuilt.
- Documents named "kernel," "runtime," "state engine" without executable code are metaphors, not components. Do not create them.
- 42 specification files produce 0 lines of automation. Small, bounded concepts produce action.

### Protocol Knowledge

- An LLM can be instructed but not forced. Instructions must be clear, minimal, and verifiable.
- Time is a first-class dimension. No recommendation should be made without establishing current time.
- State stored in files survives. State in conversation context does not.

---

## Lomé Market Knowledge

- Rainy season creates urgent pest problems — high demand window for Stop Nuisibles.
- Mobile money (Wave, Orange Money) is the primary payment method for online transactions.
- WhatsApp is the primary sales channel — not websites, not e-commerce platforms.
- Delivery within Lomé is feasible same-day with motorcycle couriers.
- Price sensitivity: 5,900 FCFA is competitive against monthly spray spending (3,000+ FCFA/month).

---

## Pest Repeller Product Knowledge

- Price: 5,900 FCFA (see ASSET.md A-002 for cost and margin data)
- Coverage: ~7m. Type: Ultrasonic (no chemicals, no odor, no refill).
- Competes against: sprays (toxic, temporary), mosquito coils (smoke, fire risk), nets (bulky).
- Stock: 100 units available (see ASSET.md A-002 for current inventory).
- Previous version (V1) sold 2,000 units at 2,500 FCFA by the same supplier — demand validated.

---

## Cross-Project Patterns

### Zoclo Livraison (Archived)

- Complete content operation: 30-day calendar, 21 scripts, brand guide.
- Content structure (hook→problem→solution→proof→CTA) is a reusable pattern.
- Strongest hooks were pattern-interrupt questions and local targeting ("Si t'es a Lome...").
- Key lesson: TikTok content for sensitive products (contraception) risks platform restriction. Physical products (pest control) have lower regulatory risk.

---

## Continuous Improvement Pattern

### Review Questions (apply after any project or workflow)

- What worked?
- What failed?
- What surprised us?
- What repeated?
- What should change?

### When a pattern repeats 2+ times

1. Observe the pattern across projects
2. Validate it (does it hold in different contexts?)
3. Extract it into PLAYBOOK.md as a strategic pattern
4. Reference it from KNOWLEDGE.md as evidence

### Trigger

Every completed project triggers improvement review. The lessons are stored here before the project is archived.

---

---

## Doodle Animation YouTube Pipeline (Master Prompt — saved 2026-06-19)

**Full prompt sauvegarde dans :** `KnowledgeAssets/doodle_youtube_master_prompt.txt`

### Shorts Viral Pipeline (saved 2026-06-19)

**Full prompt :** `KnowledgeAssets/shorts_viral_master_prompt.txt`

- Format: 30-60s vertical (9:16), hand-drawn doodle
- One idea per Short. Hook in first 1-2s.
- 5-8 scenes per Short, fast cuts (2-5s per scene)
- Text overlay mandatory (90% watch first loop on mute)
- Loopable ending → first frame
- Sound: trending audio + voiceover on top

### Channel DNA

- **Niche:** Human history, evolution, anthropology, psychology
- **Format:** 10-14 min educational explainer, 2nd-person narration, hand-drawn doodle 2D animation
- **Hook formula:** Relatable modern moment → "but the real answer is far stranger" → reframe
- **Script rhythm:** Short sentence. Short sentence. Longer sentence. Short sentence. Question.
- **Narrative arc:** Hook → Reframe → Deep Dive → Counterintuitive Twist → Modern Mirror → Echo close

### Visual DNA

- Hand-drawn 2D doodle, flat colors, bold black outlines, sketchy marker lines
- Characters: Stick figures, large circular heads, dot eyes, thick brow lines
- Backgrounds: Flat solid color blocks only — no gradients, no shadows, no textures
- Text: Bold ALL CAPS, marker font, RED/BLACK/YELLOW, top of frame
- Color palette: Orange #F5820D · Cobalt #2D5FBF · Green #3A9E3A · Yellow #F5C518 · Red #D94040 · Brown #8B5E3C · Blue #6EB5E8 · Tan #C4965A · White #FFFFFF
- Aspect ratio: Always 16:9

### Production Stages

1. Generate 5 viral topic ideas → user selects
2. Generate 1,800-2,500 word narration script → delivered as `.txt` file
3. Generate image prompts (1 per timestamp) → delivered in batches of 20 → combine into `.txt` file on request
4. Generate viral metadata (title, description, tags) → ready to paste into YouTube

### Key Rules

- Never skip stages. Always wait for user input.
- Script = plain text only (no markdown, no stage directions, no headers inside file)
- One timestamp = one image prompt. Hold scenes across consecutive timestamps.
- All prompts begin with style anchor, end with style lock.
- Metadata = 3 separate copyable code blocks (title, description, tags).

---

## Footer

Last updated: 2026-06-24 (refreshed stale marker)

Knowledge should be reviewed quarterly.

Entries older than 1 year without revalidation should be flagged.

New lessons from every project should be added here before the project is closed.
