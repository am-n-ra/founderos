# FOUNDEROS SPECIFICATION V1

## 1. PURPOSE

FounderOS est un systeme permettant a une personne ou une equipe de poursuivre une mission sur plusieurs annees sans perdre:

* le contexte
* les decisions
* les connaissances
* les projets
* les apprentissages
* les opportunites

independamment:

* du LLM utilise
* de la machine utilisee
* de l IDE utilise
* de la duree des sessions

---

## 2. CORE PRINCIPLES

### Principle 1

Mission First

Toujours optimiser:

```text
Mission Success Probability
```

---

### Principle 2

Persistence First

Toute information importante doit etre persistee.

Jamais uniquement dans le contexte du LLM.

---

### Principle 3

State Awareness

Le systeme doit toujours savoir:

```text
Qui

Quoi

Pourquoi

Ou

Quand

Comment

Et ensuite ?
```

---

### Principle 4

Change Awareness

Le systeme doit detecter automatiquement:

```text
Nouveaux projets

Nouveaux fichiers

Nouvelles opportunites

Nouveaux risques

Nouveaux apprentissages
```

---

### Principle 5

Proactive Assistance

Le systeme ne doit pas uniquement repondre.

Il doit:

```text
Observer

Detecter

Questionner

Proposer

Relancer
```

---

## 3. SYSTEM LAYERS

### Layer 1

FounderOS Specification

Decrit:

```text
Architecture

Flux

Regles

Standards
```

---

### Layer 2

PSOS

Constitution.

Decrit:

```text
Comment penser

Comment decider

Comment prioriser
```

---

### Layer 3

MOS

Gouvernement.

Decrit:

```text
Comment piloter
```

---

### Layer 4

Specialized Systems

```text
DAOS
VEAOS
LEOS
PMOS
RIOS
CEOS
FAOS
CAOS
SOS
AOS
ASTRA
KMOS
```

---

### Layer 5

Automation Layer

Scripts.

Agents.

Watchers.

Cron Jobs.

Hooks.

---

## 4. DIRECTORY STRUCTURE

```text
FounderOS/
```

### System

```text
FounderOS/System/
```

Contient:

```text
PSOS.md

MOS.md

DAOS.md

VEAOS.md

LEOS.md

PMOS.md

RIOS.md

CEOS.md

FAOS.md

CAOS.md

SOS.md

AOS.md

ASTRA.md

KMOS.md
```

---

### State

```text
FounderOS/State/
```

Contient:

```text
PERSONAL_PROFILE.md

MISSION.md

CURRENT_STATE.md

DASHBOARD.md

THIS_YEAR.md

THIS_QUARTER.md

THIS_MONTH.md

THIS_WEEK.md

TODAY.md
```

---

### Projects

```text
FounderOS/Projects/
```

Chaque projet:

```text
PROJECT_NAME/
```

Contient:

```text
README.md

PROJECT_PROFILE.md

PROJECT_STATE.md

ROADMAP.md

TASKS.md

DECISIONS.md

RESEARCH.md

PARTNERSHIPS.md
```

---

### Knowledge

```text
FounderOS/Knowledge/
```

Contient:

```text
Research

Learning

Frameworks

References

Notes
```

---

### Logs

```text
FounderOS/Logs/
```

Contient:

```text
DECISION_LOG.md

EXECUTION_LOG.md

OUTREACH_LOG.md

LEARNING_LOG.md

SYSTEM_LOG.md
```

---

### Automation

```text
FounderOS/Automation/
```

Contient:

```text
cron/

watchers/

hooks/

scripts/

agents/
```

---

## 5. STATES

Le systeme maintient toujours:

### User State

```text
Identite

Competences

Contraintes

Ressources
```

---

### Mission State

```text
Mission

Objectifs

Phase actuelle
```

---

### Financial State

```text
Cash

Runway

Revenue

Funding
```

---

### Project State

```text
Actif

En pause

Archive
```

---

### Learning State

```text
Competences

Gaps

Plans
```

---

## 6. CHANGE DETECTION

A chaque lancement:

MOS compare:

```text
Etat precedent

vs

Etat actuel
```

---

Detecte:

### Nouveau projet

Exemple:

```text
KORA

EDENVALLEY
```

Declenche:

```text
PROJECT DISCOVERY
```

---

### Nouveau depot Git

Questionne l utilisateur.

---

### Nouveau document

Classe automatiquement.

---

### Nouveau partenaire

Met a jour:

```text
PARTNERSHIPS.md
```

---

## 7. GENESIS MODE

Si aucun etat n existe:

Creer:

```text
FounderOS/
```

---

Puis interroger:

```text
Qui etes-vous ?

Que construisez-vous ?

Pourquoi ?

Quels projets ?

Quelles contraintes ?

Quels revenus ?

Quelles competences ?
```

---

Creer ensuite tous les fichiers necessaires.

---

## 8. DAILY MODE

Au demarrage:

Charger:

```text
CURRENT_STATE.md

TODAY.md

THIS_WEEK.md

MISSION.md
```

---

Produire:

```text
Priorites

Blocages

Opportunites

Actions du jour
```

---

## 9. WEEKLY MODE

Chaque semaine:

Creer:

```text
WEEKLY_REVIEW.md
```

---

Contenu:

```text
Succes

Echecs

Lecons

Metriques

Prochaines actions
```

---

## 10. MONTHLY MODE

Creer:

```text
MONTHLY_REVIEW.md
```

---

Contenu:

```text
Mission

Projets

Finances

Competences

Sante

Risques
```

---

## 11. PROJECT DISCOVERY MODE

Lorsqu un nouveau projet apparait:

MOS:

1. detecte
2. analyse
3. pose les questions manquantes

Puis genere:

```text
PROJECT_PROFILE.md
```

---

## 12. LEARNING MODE

MOS doit detecter:

```text
Objectif

vs

Competences actuelles
```

---

Creer:

```text
LEARNING_TRACK.md
```

---

Exemple:

```text
Objectif

Construire un modele ASR
```

---

Competences manquantes:

```text
Python

PyTorch

Speech Processing
```

---

## 13. WATCHTOWER MODE

Surveille:

```text
Concurrents

Technologies

Marches

Financements

Partenaires
```

---

Produit:

```text
WATCHTOWER_REPORT.md
```

---

## 14. AUTOMATION MODE

MOS peut creer:

```text
Scripts

Cron Jobs

Hooks

Watchers
```

---

Lorsque necessaire.

Mais seulement apres validation explicite.

---

## 15. DIGITAL TWIN OBJECTIVE

L objectif ultime n est pas:

```text
Creer un assistant.
```

L objectif est:

```text
Creer une representation operationnelle persistante
du fondateur,
de sa mission,
de ses projets,
de ses connaissances,
de ses decisions,
et de son environnement.
```
