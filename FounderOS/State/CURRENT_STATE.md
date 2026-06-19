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

**Date:** 2026-06-18 — Lomé (UTC+0)

**Operating Mode:** SURVIVAL — cash = 1,118 FCFA, zero revenue

**Cash (FCFA):** 1,118

**Active Products:**
- Pest Repeller (Stop Nuisibles) — 100 units, 5,900 FCFA, TikTok
- Soya (Soja) — 0 stock, pre-vente a dame 2: 1 sac/semaine (40 bols), besoin fournisseur < 900 FCFA/bol

**Current Bottleneck:** Fournisseur soja — dame 2 prete a acheter 40 bols/semaine si prix < 900 FCFA. Il faut trouver un fournisseur moins cher (petite quantite 1 sac/100kg).

**Top Priority:** FHQ-001 (premiere vente Stop Nuisibles) + trouver fournisseur soja (leverage: 4,000-8,000 FCFA/semaine potentiel avec 3 dames).

**Session Objective:** Analyser l'opportunite soja, calculer l'unite economique, proposer strategie fournisseur, puis retourner sur les 3 concepts video.

**Last Decision:** FounderHQ V2 architecture freeze. FHQ-001 launched. Sprint 30 jours : premiere vente → 5 ventes → pattern → playbook. Aucune modification architecturale pendant 30 jours.

**Last Updated:** 2026-06-18 — Lomé UTC+0
