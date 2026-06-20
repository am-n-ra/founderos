# CURRENT_STATE

## Concept

CURRENT_STATE is the single source of operational truth.

All session-level state lives here and only here.

No other file should contain "current X" — if it does, it creates divergence.

---

## Rules

1. **Single source.** All session state lives here. If it's in CURRENT_STATE, it's authoritative. If it contradicts another file, CURRENT_STATE wins.
2. **Updated every session exit.** Before any session ends, CURRENT_STATE is updated.
3. **Read every session start.** Before any action, CURRENT_STATE is loaded.
4. **Max age = 1 session.** If loaded and the session date/time ≠ current session, it must be re-verified before use.

---

## Fields

### Date
> The current datetime in Lomé (UTC+0).

### Operating Mode
> One of: SURVIVAL, GROWTH, SCALE. Determined by cash position and revenue state.

### Cash (FCFA)
> Current cash position. Last verified by founder. Source of truth for all cash-dependent decisions.

### Active Product
> The product currently being sold/promoted. The one that must generate revenue.

### Current Bottleneck
> The single constraint preventing progress. Only one. If you list more than one, the real bottleneck is hiding behind the others.

### Top Priority
> The single next outcome that matters. If this outcome is achieved, the bottleneck is resolved or the mission advances measurably.

### Session Objective
> What this session must accomplish to serve the Top Priority. Written at session start. Verified at session end.

### Last Decision
> The most recent decision made. Prevents re-debating settled questions.

### Last Updated
> When this file was last modified. If > 1 session old, flag as stale.

---

## Current State

**Date:** 2026-06-20 — Lomé (UTC+0)

**Operating Mode:** SURVIVAL — cash = 1,118 FCFA, zero revenue

**Cash (FCFA):** 1,118

**Active Products:**
- Pest Repeller (Stop Nuisibles) — 100 units, 5,900 FCFA, TikTok
- Soya (Soja) — 0 stock, pre-vente a 2 dames: ~60 bols/semaine, besoin fournisseur < 800 FCFA/bol
- DoodleMind (YouTube Shorts) — nouvelle chaine, 0 abonnes, visee monetisation

**Current Bottleneck:** Cash = 1,118 FCFA. Can't buy stock, can't pay for image generation. Need either a supplier who accepts post-delivery payment or a zero-cash revenue channel (DoodleMind).

**Top Priority:** Call soya suppliers (Ste SODJA priority) to find a ≤ 700 FCFA/bol deal with post-delivery payment. If impossible, pivot to publishing DoodleMind Short #1 as zero-cash path.

**Session Objective:** Implement DIOS module + complete V4 consolidation.

**Last Decision:** DIOS cree comme systeme nerveux commercial. V4 consolidation completee — SYSTEM_PROMPT.md absorbe KERNEL, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS. Prochaine action : appeler fournisseurs soja ou executer reboot test (WF-008).

**Last Updated:** 2026-06-20 (DIOS + V4 session) — Lomé UTC+0
