# FRE + DIOS + VAOS — Design Document

## Contexte

FounderHQ est un système de pilotage (pas un chatbot) pour un solo entrepreneur à Lomé, Togo.
Le système est opérationnel (V4) avec 9 concepts, 12 modules, 5 engines, et sert 7 projets actifs en mode SURVIVAL (cash ~2,679 FCFA).

L'audit révèle trois systèmes distincts à construire pour atteindre l'objectif "digital twin" :

1. **FRE** (Founder Runtime Ecosystem) — portabilité du runtime
2. **DIOS** (Distribution Intelligence OS) — moteur de croissance économique
3. **VAOS** (Venture Architecture OS) — industrialisation de la création de ventures

---

## Architecture cible

```
FounderHQ/
├── Concepts/
├── Protocols/
├── State/
├── Runtime/ (FRE)
│   ├── FRE_SPEC.md
│   ├── RUNTIME_KERNEL.md
│   ├── ADAPTER_INTERFACE.md
│   └── adapters/
├── Frameworks/
│   ├── Core/ (CAOS, CEOS, PSOS, FAOS, SAOS)
│   └── Specialized/
│       ├── Venture/VAOS/ (10 sous-modules)
│       └── Distribution/DIOS/ (8 sous-modules)
└── TIMELINE.md (décisions au format Decision Record)
```

---

## Priorité d'effort (30 prochains jours)

| Module | Effort | Rationale |
|--------|--------|-----------|
| DIOS | 80% | Bottleneck immédiat : distribution → attention → ventes → cash |
| VAOS | 15% | Industrialiser la méthode de structuration déjà utilisée |
| FRE | 5% | Infrastructure de portabilité, important mais pas urgent |

---

## 1. DIOS — Distribution Intelligence OS

### Objectif

Transformer une offre locale en contenu, en attention, en ventes.

### Principe fondamental

DIOS ne traduit pas. Il adapte : **Langue → Culture → Problème → Désir → Contexte économique**.

### Sous-modules (Frameworks/Specialized/DIOS/)

| Module | Rôle |
|--------|------|
| AUDIENCE_INTELLIGENCE.md | Segments, personas, listening |
| PLATFORM_INTELLIGENCE.md | TikTok, YouTube, WhatsApp, X — mécaniques, algorithmes, formats |
| LANGUAGE_INTELLIGENCE.md | Adaptation linguistique et culturelle (FR, EN, EW, PID) |
| HOOK_INTELLIGENCE.md | Pattern interrupt par plateforme, audience, produit |
| OFFER_INTELLIGENCE.md | Comment présenter le produit pour convertir |
| DISTRIBUTION_INTELLIGENCE.md | Calendrier, fréquence, cross-posting, amplification |
| CONVERSION_INTELLIGENCE.md | De l'attention à l'action (CTA, funnel, WhatsApp) |
| DISTRIBUTION_MEMORY.md | Résultats des campagnes → patterns → amélioration continue |

### Cycle DIOS

```
Offre → Audience → Langue → Hook → Contenu → Plateforme → Distribution → Conversion → Analyse → Apprentissage
```

---

## 2. VAOS — Venture Architecture OS

### Objectif

Transformer une idée en venture exécutable et finançable, étape par étape.

### Sous-modules (Frameworks/Specialized/VAOS/)

| Module | Rôle |
|--------|------|
| VISION_ENGINE.md | Définir la transformation de réalité visée |
| MISSION_ENGINE.md | Définir la raison d'être et l'approche |
| THEORY_OF_CHANGE.md | Si A → alors B → donc C |
| ASSET_MAPPING.md | Inventaire des actifs stratégiques |
| STRATEGIC_PLANNING.md | Plan d'attaque |
| ROADMAP_ENGINE.md | Phases et jalons dans le temps |
| CAPITAL_STRATEGY.md | Financement, dette, equity, grants |
| BUSINESS_PLAN_ENGINE.md | BP exécutable et finançable |
| CONSTRAINT_ANALYSIS.md | Identifier et débloquer les goulots |
| VENTURE_REPOSITIONING.md | Réparer un venture qui ne décolle pas |

### Cycle VAOS

```
Idée → Vision → Mission → Theory of Change → Assets → Plan → Roadmap → Capital → BP → Exécution → Audit → Repositioning
```

---

## 3. FRE — Founder Runtime Ecosystem

### Objectif

Rendre FounderHQ exécutable sur n'importe quelle plateforme LLM sans modification.

### Fichiers (Runtime/)

| Fichier | Rôle |
|---------|------|
| FRE_SPEC.md | Constitution du runtime — relation FRE / Adapter / Engine |
| RUNTIME_KERNEL.md | Cycle décisionnel universel : BOOT → OBSERVE → ORIENT → DECIDE → ACT → LEARN → UPDATE |
| ADAPTER_INTERFACE.md | Contrat qu'une plateforme implémente |
| adapters/*.md | ChatGPT, Claude, Gemini, OpenCode, Cursor, local LLM |

### Principe

Le LLM est un composant du runtime, pas le runtime lui-même.

---

## Standard Decision Record (intégré à TIMELINE)

Chaque décision importante produit une entrée suivant ce schéma :

```
## Decision YYYY-MM-DD
- Observation: contexte
- Analysis: ce que ça signifie
- Decision: choix fait
- Action: ce qui a été exécuté
- Outcome: résultat obtenu
- Lesson: ce qui a été appris
```

---

## Plan d'exécution

### Sprint 1 — DIOS Foundation
- AUDIENCE_INTELLIGENCE.md
- HOOK_INTELLIGENCE.md
- PLATFORM_INTELLIGENCE.md
- LANGUAGE_INTELLIGENCE.md

### Sprint 2 — DIOS Offensive
- OFFER_INTELLIGENCE.md
- DISTRIBUTION_INTELLIGENCE.md
- CONVERSION_INTELLIGENCE.md
- DISTRIBUTION_MEMORY.md

### Sprint 3 — VAOS
- VISION_ENGINE.md → MISSION_ENGINE.md → THEORY_OF_CHANGE.md
- ASSET_MAPPING.md → STRATEGIC_PLANNING.md → ROADMAP_ENGINE.md
- CAPITAL_STRATEGY.md → BUSINESS_PLAN_ENGINE.md
- CONSTRAINT_ANALYSIS.md → VENTURE_REPOSITIONING.md

### Sprint 4 — FRE
- RUNTIME_KERNEL.md
- ADAPTER_INTERFACE.md
- FRE_SPEC.md (réécriture)

---

## Non-négociables

1. **FounderHQ > outils** — doit survivre à la disparition de tout LLM ou plateforme
2. **Le LLM est un composant** — pas le centre du système
3. **Décision > conversation** — tout est orienté vers l'action et le pilotage
4. **Portabilité réelle** — couches 1-5 (Manifest à FRE) suffisent à tout reconstruire
