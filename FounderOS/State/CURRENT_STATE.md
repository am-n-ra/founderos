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

**Date:** 2026-06-20 19:29 — Lomé (UTC+0)

**Operating Mode:** SURVIVAL — cash under 3,000 FCFA, zero revenue from sales

**Cash (FCFA):** ~2,679 accessible (1,229 account + 350 leftover + 1,100 growth set-aside). Plus 1,800 allocated for connectivity until Tuesday. Tomorrow: dame 1 paie 4,875 FCFA (5 bols × 975) à 17h.

**Active Products:**
- Pest Repeller (Stop Nuisibles) — 100 units, 5,900 FCFA, TikTok
- Soya (Soja) — 0 stock. Seule dame 1 confirmée (5 bols × 975 FCFA, demain 17h).
- DoodleMind (YouTube Shorts) — Short #1 published, 366 views (YouTube) + 65 views (TikTok)

**Current Bottleneck:** Dame 2 fonctionne en consignation (vend puis paie) — impossible sans cash flow. Seulement 5 bols confirmés (dame 1). Trouver acheteurs cash supplémentaires ou stocker.

**Top Priority:** Sécuriser la vente des 5 bols à dame 1 demain 17h. Trouver d'autres acheteurs cash pour augmenter le volume. Renégocier Atakpamé.

**Session Objective:** Redéfinir la stratégie soya après l'échec du modèle consignation.

**Last Decision:** Dame 2 = consignation, pas viable. Seule dame 1 confirmée (5 bols, 975 FCFA, 17h). Recherche autres acheteurs cash.

**Last Updated:** 2026-06-20 19:29 — Lomé UTC+0
