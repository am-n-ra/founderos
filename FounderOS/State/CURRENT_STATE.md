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

**Date:** 2026-06-27 09:51 — Lomé (UTC+0)

**Operating Mode:** SURVIVAL — cash under 3,000 FCFA

**Life Framework (2026-06-24 realization):**
Spirituality (ultimate) → Trading (independence tool, no clients) → KORA/OMNI (impact) → Retire 30-33. Money is fuel, not the goal.
**FounderHQ Vision (2026-06-27):** Centralized AI-powered mission workspace. Mentor/co-founder/team member role-flexible. All projects managed from single root chat. Persists beyond LLM context loss. No aimless days — guided by frameworks.

**Trading Account:**
- Funded: $2000 Next Instant (via uncle, late 2025)
- Current: $1904.28
- **Strategy optimisée:** EURUSD M1, 6 règles, SL=1pt TP=3pt (COMPO=7.6 | 210W/136L | WR=60.7% | PF=6.17)
- **EA:** ReversalDetector.mq5 v5.1 — scan + live trading
- **LiveTrading:** false (à activer sur VPS)
- **RiskPerTrade:** $0.50, lot calculé automatiquement
- **Spread guard:** max 1pt, trade skip si spread > 1

**Cash (FCFA):**
- YAS 1 (20% épargne): ~100 FCFA (700 envoyé à ami pour carte Meta Ads)
- YAS 2 (80% subsistance): ~100 FCFA
- Total utilisable: ~200 FCFA
- Besoin vital mensuel: ~41,000 FCFA/mois (15k nourriture + 8k cash power + 18k connexion)

**Active Products:**
- **SOJACO** — À L'ARRÊT.
- **KORA Lab** — AI lab, pré-seed. En attente retours ST Digital / DG West Africa / Herlog.
- **DoodleMind** — Chaînes YouTube/TikTok. Objectif: 1 vidéo/jour.
- **Stop Nuisibles** — 100 units dispo. Objectif: 1 vidéo/jour TikTok.
- **OMNI** — MVP déployé (omni.sparkafrika.online). Djanta Tech Hub soumis.

**VPS Oracle:** vm.standard indisponible, a1 refuse toujours. Solution locale OK tant que connecté. Bloqué.

**Google for Startups:** Déjà appliqué. Bloqué: besoin top-up $50 pour valider compte GCP (koralab).

**Current Bottleneck:** Aucune source de revenu active. Cash quasi nul. VPS Oracle indisponible.

**Top Priority:** Faire tourner l'EA 24/7 (local en attendant VPS) + débloquer GCP pour KORA compute.

**Next Action:** Sessions London/NY (samedi) — run EA local. Préparer FounderHQ vision + KORA vision.

**Last Updated:** 2026-06-27 09:51 — Lomé UTC+0
