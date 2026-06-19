# FOUNDEROS V1 MASTER SPEC

## Autorite
Ce document est la source de verite unique. Tout conflit entre fichiers est resolve par ce mapping.

---

## Hierarchie

```
CONSTITUTION (PSOS)
    ↓
ORCHESTRATOR (MOS)
    ↓
KERNEL → RUNTIME → STATE_ENGINE
    ↓
SPECIALIZED OS + ENGINES
```

---

## Module Registry (v1.0)

### Core — requis au demarrage

| Module | Role |
|--------|------|
| PSOS | Constitution — valeurs, regles, identite |
| MOS | Orchestrator — coordonne tous les modules |
| KERNEL | Boot sequence — 12 phases, charge le contexte |
| RUNTIME | Boucle quotidienne — OODA, mission blocks |
| STATE_ENGINE | Persistance, deltas, snapshots, continuite |
| OPERATING_MODES_ENGINE | SURVIVAL/BUILD/LEARNING/FUNDRAISING/SCALE/RECOVERY |
| POE | Personal Operating Engine — ADHD, energie, burn-out |
| TOS | Temporal OS — 9 horizons, reverse planning, temps |
| EVENT_ENGINE | 8 categories d'evenements, cycle de vie |

### Support — actifs en v1.0

| Module | Role |
|--------|------|
| DAOS | Decision — briefs, logs, options |
| KMOS | Knowledge — apprentissage, indexation |
| FAOS | Focus/Action — taches, execution prioritaire |
| DTOS | Digital Twin — reflet de l'etat du founder |
| EOS | Energy — gestion d'energie, pauses |
| AGENT_RUNTIME_ENGINE | 4 niveaux d'agents, permissions |
| MISSION_SCORE_ENGINE | 8 dimensions, score 0-100, tendances |

### Secondaire — utilitaire

| Module | Role |
|--------|------|
| AOS | Attention — ce qui merite l'attention |
| CEOS | Continuous Execution — livraison continue |
| GOS | Goals — objectifs macro |
| LEOS | Learning — apprentissage guide |
| PMOS | Project Management — gestion de projet |
| RIOS | Research & Insights — recherche |
| SOS | Strategy — strategie long terme |
| AAOS | Automation & Agents (redondant avec ARE) |
| MAOS | Multi-Agent Orchestration (redondant avec MOS) |

---

## Audit des doublons (de l'audit original)

| Conflit | Decision |
|---------|----------|
| CAOS vs FAOS | CAOS archive, FAOS est le module actif |
| MOS vs MAOS vs AAOS | MOS est l'orchestrateur; MAOS et AAOS archives |
| DTOS vs KMOS | DTOS = etat du founder, KMOS = savoir externe — distincts |
| GOS vs DTOS vs DAOS | GOS = goals, DTOS = profil, DAOS = decisions — distincts |
| VEAOS | Phantom — archive |
| GOOS | Reference mort — supprimer |

---

## Hierarchy des fichiers

```
FounderHQ/
├── FounderOS/           ← SYSTEM files only
│   ├── SYSTEM/          ← Tous les modules OS
│   ├── STATE/           ← Etat courant (8 fichiers obligatoires)
│   ├── FOUNDEROS_AGENT_POLICY.md
│   ├── FOUNDEROS_EXECUTION_PROTOCOL.md
│   ├── FOUNDEROS_FILE_CONVENTION.md
│   ├── FOUNDEROS_AUTOMATION_SPEC.md
│   └── FOUNDEROS_V1_MASTER_SPEC.md    ← ce fichier
├── Projects/            ← Projets actifs
├── Knowledge/           ← Savoir permanent
├── Reports/             ← Briefs, reviews
├── Events/              ← Evenements externes
├── Workspace/           ← Brouillons, temporaire
└── Archive/             ← Inactif
```

---

## Etat des fichiers SYSTEM/ (32 fichiers)

| Groupe | Fichiers |
|--------|---------|
| Core (9) | PSOS, MOS, KERNEL, RUNTIME, STATE_ENGINE, OPERATING_MODES_ENGINE, POE, TOS, EVENT_ENGINE |
| Support (7) | DAOS, KMOS, FAOS, DTOS, EOS, AGENT_RUNTIME_ENGINE, MISSION_SCORE_ENGINE |
| Secondaire (10) | AOS, CEOS, GOS, LEOS, PMOS, RIOS, SOS, AAOS, MAOS, CAOS |
| Archive (3) | VEAOS, ASTRA, FOUNDEROS_AUDIT_REPORT |
| Specs (3) | FILE_TEMPLATES, IMPLEMENTATION_SPEC, FILE_CONVENTION |

Total: 32 fichiers. Core v1.0 = 16.

---

## Flux d'execution quotidien

```
1. KERNEL boot         → charge etat, detecte changements
2. MODE detection      → SURVIVAL/BUILD/etc
3. MISSION_SCORE       → evaluation rapide
4. EVENT_ENGINE        → check evenements manques
5. RUNTIME loop        → OODA blocks
6. STATE_ENGINE save   → snapshot + delta
```

---

## Regles d'evolution

1. Aucun nouveau module sans approbation du MASTER SPEC
2. Nouveau module = nouveau fichier dans SYSTEM/ + entree dans ce tableau
3. Module mort = archive, jamais supprime
4. MASTER SPEC est le seul index — mettre a jour si changement

---

## Fermeture v1.0

FounderOS v1.0 est SPECIFIE. 16 modules core + 10 secondaires. Tous les concepts sont couverts: temps, etat, mode, energie, evenements, decisions, connaissance, execution, agents, score de mission.

Prochaine version (v2.0) apres 30 jours d'utilisation reelle — les vrais bugs et manques seront visibles seulement sur le terrain.

**FIN DE LA PHASE D'ARCHITECTURE.**
