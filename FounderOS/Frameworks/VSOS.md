# FounderOS V4 — VSOS
## Venture Structuring Operating System

### Transformer toute idée, projet ou opportunité en système exécutable

---

## 1. Qu'est-ce que VSOS ?

VSOS est la méthodologie de transformation stratégique de FounderHQ. Elle prend une entrée floue (idée, projet, opportunité, problème) et produit une sortie structurée : une cascade complète de documents, de la Vision au système d'exécution.

VSOS n'est pas un module quotidien. C'est une **lentille** chargée quand tu dois créer un nouveau projet, restructurer un projet existant, préparer une levée de fonds, ou transformer une vision en exécution.

VSOS a déjà été utilisé sur KORA et Omni (sans être nommé). C'est maintenant un framework explicite.

---

## 2. Quand utiliser VSOS

| Situation | Action |
|-----------|--------|
| Nouvelle idée / nouveau projet | VSOS complet (Phase 1 → 3) |
| Projet existant sans structure | VSOS Audit + Phase 2 → 3 |
| Restructuration / reframe | VSOS Audit + Mission Extraction |
| Préparation levée de fonds | VSOS Phase 3 (Capital Roadmap + BP) |
| Blocage stratégique | VSOS Gap Analysis |

**Ne pas utiliser :** pour les opérations quotidiennes (DAOS), les décisions rapides (DECISION_ENGINE), le contenu (CEOS).

---

## 3. Architecture VSOS

### Entrée
```
Idée
Projet existant
Entreprise
Opportunité
Problème
```

### Les 3 Phases

```
PHASE 1: DIAGNOSTIC
├── Reality Assessment
├── Mission Extraction
└── Gap Analysis

PHASE 2: STRATEGIC CASCADE
├── Vision
├── Mission
├── Theory of Change
├── Strategic Assets Map
└── Master Plan

PHASE 3: EXECUTION FRAMEWORK
├── Strategic Roadmap
├── Capital Roadmap
├── Business Plan
└── Execution System (KPIs, milestones)
```

### Sortie
```
Data Room complète dans projects/<PROJECT>/
├── 01_VISION.md
├── 02_MISSION.md
├── 03_THEORY_OF_CHANGE.md
├── 04_STRATEGIC_ASSETS_MAP.md
├── 05_MASTER_PLAN.md
├── 06_STRATEGIC_ROADMAP.md
├── 07_CAPITAL_ROADMAP.md
├── 08_EXECUTIVE_SUMMARY.md
├── 09_BUSINESS_PLAN.md
├── 10_PITCH_DECK.md
└── annexes/
```

---

## 4. Phase 1 — Diagnostic

À faire avant toute cascade stratégique. Comprendre où on est avant de décider où on va.

### 4.1 Reality Assessment

Questions à回答 :
- Quel est l'état actuel du projet / de l'idée ?
- Qu'est-ce qui existe déjà ? (MVP, équipe, traction, revenus, docs)
- Quelles sont les contraintes ? (cash, temps, compétences, marché)
- Quel est le problème fondamental résolu ?

**Output :** Une section dans CURRENT_STATE.md ou un memo diagnostic.

### 4.2 Mission Extraction

Extraire la mission du projet, qu'elle soit explicite ou implicite :
- Pourquoi ce projet existe ?
- Pour qui ?
- Quel est le changement désiré ?
- Dans 5-10-20 ans, à quoi ressemble le succès ?

**Output :** Une ébauche de mission (sera raffinée en Phase 2).

### 4.3 Gap Analysis

Identifier l'écart entre l'état actuel et la mission :
- Qu'est-ce qui manque ? (données, équipe, financement, traction)
- Quels sont les blocages ?
- Quel est le risque principal ?
- Quelle est la prochaine action la plus importante ?

**Output :** Gap list + priorisation.

**Modules associés :** RIOS.md (recherche) peut être invoqué pour creuser les gaps.

---

## 5. Phase 2 — Strategic Cascade

Construire les 5 documents fondamentaux qui forment l'armature stratégique du projet.

### 5.1 Vision (projects/X/01_VISION.md)

**Horizon :** 10-25 ans. Indépendante des produits, des technologies, des financements.

**Éléments :**
- Vision Statement (1 paragraphe, le futur désiré)
- Le futur que nous voulons créer (pourquoi le statu quo est inacceptable)
- Notre conviction fondamentale (pourquoi notre approche est la bonne)
- Notre vision de l'infrastructure (ce qu'on construit)
- Notre vision de l'impact sociétal (éducation, santé, économie, culture)
- Horizon de réussite (quand saurons-nous qu'on a réussi ?)
- OODA Critique (pourquoi cette vision survivra aux changements technologiques)

**Template section OODA Critique :**
```
Cette vision est volontairement indépendante des [technologies/marchés] actuels.
Elle reste valable même si [X, Y, Z] disparaissent.
Une bonne vision doit survivre à plusieurs générations technologiques.
```

### 5.2 Mission (projects/X/02_MISSION.md)

**Ce que l'organisation fait chaque jour.**

**Éléments :**
- Déclaration de mission (1 phrase)
- Pourquoi nous existons
- Ce que nous faisons (5 capacités fondamentales)
- Ce que nous NE SOMMES PAS (pour éviter le scope creep)
- Nos principes d'exécution (5 max)
- Comment nous mesurons le succès
- Priorité actuelle

### 5.3 Theory of Change (projects/X/03_THEORY_OF_CHANGE.md)

**La chaîne logique : comment la vision devient réalité.**

**Éléments :**
- Les déficits structuraux (pourquoi le problème existe)
- Hypothèse centrale (SI... ALORS...)
- Les relations de causalité (chaîne : pas de X → pas de Y)
- La chaîne de transformation (étape par étape)
- Les résultats attendus (court, moyen, long terme)
- L'hypothèse fondamentale (le vrai pari qu'on fait)

### 5.4 Strategic Assets Map (projects/X/04_STRATEGIC_ASSETS_MAP.md)

**Ce qu'on accumule, pourquoi c'est difficile à reproduire.**

**Éléments :**
- Liste des actifs par difficulté de réplication
- Pour chaque actif : ce qu'il est, pourquoi il est dur à copier
- Tableau : Actif / Difficulté / Temps / Avantage Concurrentiel
- L'actif le plus important (le "château fort")

### 5.5 Master Plan (projects/X/05_MASTER_PLAN.md)

**Le cadre de développement global.**

**Éléments :**
- Résumé exécutif
- Thèse stratégique
- Les 6 (ou X) couches stratégiques
- Chronologie d'exécution par phase
- Principes stratégiques (5 max)

---

## 6. Phase 3 — Execution Framework

Transformer la stratégie en plans concrets, finançables et mesurables.

### 6.1 Strategic Roadmap (projects/X/06_STRATEGIC_ROADMAP.md)

**Quand on fait quoi.**

**Éléments :**
- North Star (la direction)
- Phases avec pour chacune : période, objectif, livrables, budget
- Jalons clés avec dates cibles et indicateurs

### 6.2 Capital Roadmap (projects/X/07_CAPITAL_ROADMAP.md)

**Comment on finance chaque phase.**

**Éléments :**
- Thèse de capital
- Architecture de financement (5 couches : fondateur, non-dilutif, partenariats, revenus, equity)
- Utilisation des fonds (tableau détaillé)
- Règle de financement (ne pas lever tant que le palier précédent n'est pas prouvé)

### 6.3 Business Plan (projects/X/09_BUSINESS_PLAN.md)

**Phase 1 : le plan pour le premier palier.**

**Éléments :**
- Executive Summary (1 page)
- Le problème (détaillé)
- L'opportunité
- La solution
- Les objectifs Phase 1
- Le business model
- La roadmap Phase 1
- Use of Funds
- Risques et mitigations
- Demande d'investissement

### 6.4 Execution System (projects/X/annexes/A3_KPIS_MILESTONES.md)

**Comment on mesure et on suit.**

**Éléments :**
- Jalons avec mois cibles
- KPIs avec objectifs chiffrés
- Fréquence de revue
- Qui est responsable

---

## 7. VSOS dans l'Écosystème FounderHQ

### Modules invoqués pendant VSOS

| Module | Rôle pendant VSOS |
|--------|------------------|
| **VEAOS** | Raffinement vision/mission, scénarios stratégiques |
| **RIOS** | Recherche de marché, concurrents, gaps |
| **FAOS** | Stratégie fundraising (Phase 3) |
| **DIOS** | Stratégie de distribution (après VSOS) |
| **CEOS** | Stratégie de contenu (après VSOS) |

### Post-VSOS

Une fois VSOS terminé, le projet est enregistré via PROJECT_REGISTRATION_PROTOCOL.md :
1. Créer `concepts/<PROJECT>.md`
2. Ajouter à `State/CURRENT_STATE.md`
3. Ajouter à `State/PRIORITY_MATRIX.md`
4. Ajouter les relations dans les concepts pertinents

---

## 8. Cas d'Usage (déjà exécutés)

### KORA — AI Lab (African languages)
- Entrée : Idée d'infrastructure IA pour langues africaines
- VSOS : Complet (Phase 1 → 3)
- Sortie : 20 fichiers dans `projects/KORA/`
- Statut : Pre-Seed ready

### OMNI — Index du commerce de proximité
- Entrée : MVP existant + pitch deck
- VSOS : Phase 2 → 3 (Diagnostic sauté car projet déjà avancé)
- Sortie : 20 fichiers dans `projects/Omni/`
- Statut : Dossier Djanta Tech Hub prêt

### Financial Literacy Program
- Entrée : Cours générique à personnaliser
- VSOS : Audit + Reframe (adapter au contexte FounderHQ)
- Sortie : 28 concepts réécrits avec exemples réels
- Statut : 2/28 complétés

---

## 9. Template : Quick VSOS (1 heure)

Pour les projets rapides (ex: Pest Repeller, Solar Kit, chaîne TikTok) :

```
1. Reality Assessment (5 min) — Où j'en suis ?
2. Mission (5 min) — Pourquoi ce projet existe ?
3. Assets (5 min) — Qu'est-ce que j'ai déjà ?
4. Roadmap (10 min) — Les 3 prochaines actions
5. BP 1-pager (15 min) — Modèle économique simple
6. KPIs (5 min) — Comment je sais si ça marche ?
7. Enregistrer (15 min) — Créer concept + entrée PRIORITY_MATRIX
```

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Type | Framework |
| Owner | System |
| Dependencies | VEAOS, RIOS, FAOS, PROJECT_REGISTRATION_PROTOCOL |
