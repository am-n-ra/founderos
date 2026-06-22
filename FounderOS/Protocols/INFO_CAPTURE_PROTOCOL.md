# INFO CAPTURE PROTOCOL

## Purpose

Toute information opérationnelle donnée en conversation est automatiquement capturée dans FHQ. Ce protocole définit quel type d'info va dans quel fichier, sans attendre une instruction explicite.

## Règle Fondamentale

**Si l'info est utile à une session future, elle doit être écrite maintenant.**

Ne pas demander "tu veux que je l'enregistre ?" — enregistrer directement.

---

## Mapping Type → Fichier

| Type d'Information | Exemple | Fichier Cible | Action |
|-------------------|---------|--------------|--------|
| **Deadline / date butoir** | "Le 22 juin à 16h59" | `State/PRIORITY_MATRIX.md` | Mettre à jour deadline + warning 🔴 |
| **Progrès projet** | "J'ai fini 1.1 Debt vs Equity" | `State/CURRENT_STATE.md` + `State/PRIORITY_MATRIX.md` | Update status section + dashboard |
| **Nouveau projet** | "Je lance Omni" | Appliquer PROJECT_REGISTRATION_PROTOCOL.md | Créer concept/ + projets/ + tous les liens |
| **Décision** | "On va sur Innov'Action pas Idée-Action" | `State/CURRENT_STATE.md` + concepts concernés | Mettre à jour Last Decision |
| **Chiffre / métrique** | "Encaissement 4,875 FCFA" | `State/CURRENT_STATE.md` | Update Cash + infos produit |
| **Blocage** | "Fournisseur pas de new" | `State/PRIORITY_MATRIX.md` | Mettre warning 🟡/🔴 |
| **Événement important** | "Herlog envoyé" | `TIMELINE.md` | Enregistrer Event → Decision → Outcome |
| **Nouvelle relation** | "OMNI lié à KORA" | Concepts concernés | Ajouter lien bidirectionnel |
| **Préférence / règle** | "Toujours tracker les deux" | `Protocols/INFO_CAPTURE_PROTOCOL.md` | Ajouter la règle |
| **Information veille** | "Résultat websearch X" | `State/WATCH_REGISTRY.md` | Update Last Result + Next Check |

---

## Cas Concrets (exemples récents)

| Ce que tu as dit | Ce qui a été capturé | Où |
|-----------------|---------------------|-----|
| "je viens de finir 1.1 Debt vs Equity" | Financial Literacy 1.1 → ✅ | `State/CURRENT_STATE.md` + `State/PRIORITY_MATRIX.md` |
| "societe pas encore enregistree" | Omni company status corrigé | `projects/Omni/annexes/A4_DJANTA_TECH_HUB.md` |
| "omni devrait se mettre dans innov action" | Programme confirmé | `concepts/OMNI.md` + annexes A4 |
| "pourquoi tu ne track pas tous mes objectifs" | PRIORITY_MATRIX.md créé | Nouveau fichier |

---

## Ce Qui N'est PAS Capturé

- Questions sans réponse opérationnelle
- Réflexions exploratoires non confirmées
- Conversations non liées à FHQ (sauf si pattern émergent)

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Owner | System |
