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

**Date:** 2026-06-21 06:50 — Lomé (UTC+0)

**Operating Mode:** SURVIVAL — cash under 3,000 FCFA

**Cash (FCFA):** ~2,679 accessible. Aujourd'hui 17h: encaissement 4,875 FCFA de dame 1 (cash va au fournisseur, pas à toi).

**Active Products:**
- Pest Repeller (Stop Nuisibles) — 100 units, 5,900 FCFA, TikTok
- Soya (Soja) — Dame 1 confirmée (5 bols × 975 FCFA, 17h). Fournisseur Lomé réduit à 5 bols sample lundi. Atakpamé (360 FCFA/kg) en attente.
- DoodleMind (YouTube Shorts) — Short #1 published
- **KORA Lab** — AI lab, pré-seed, documents complets, Herlog envoyé, ST Digital en attente

**KORA Status:**
- Data Room: ✅ Complete (Vision → BP → Annexes, 20+ docs)
- Herlog: Envoyé, retour en attente
- ST Digital: Estimation compute envoyée, suivi demain
- Phase: Pre-Seed Validation (Éwé)
- Prochaine action: Relancer ST Digital demain

**Current Bottleneck:** Modèle soya : cash va au fournisseur, pas à toi. Marge nulle ou minime.

**Top Priority:** Aujourd'hui 17h — collecter 4,875 FCFA de dame 1 + confirmer fournisseur Lomé pour 5 bols lundi + attendre retour Atakpamé.

**Session Objective:** Migration complète de KORA dans FounderOS + mise à jour dossiers.

**Last Decision:** Herlog envoyé. Suivi ST Digital demain. KORA docs migrés dans projects/KORA/.

**Last Updated:** 2026-06-21 06:50 — Lomé UTC+0
