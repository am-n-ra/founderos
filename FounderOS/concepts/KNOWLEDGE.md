# KNOWLEDGE

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 4.

## Role

Store validated truths, patterns, principles, and domain expertise.

Knowledge evolves slowly.

Knowledge compounds over time.

Nothing validated should be lost.

---

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

## Footer

Last updated: 2026-06-18 (added: continuous improvement pattern, redirected pricing to ASSET)

Knowledge should be reviewed quarterly.

Entries older than 1 year without revalidation should be flagged.

New lessons from every project should be added here before the project is closed.
