# VAOS — 21 CONSTRAINT MAP

## Purpose

What is blocking us?

## Constraint Categories

| Category | Constraint | Severity | Can We Remove It? | How? | By When? |
|----------|------------|----------|-------------------|------|----------|
| Capital | Cash < 10,000 FCFA | Critical | Oui | EA Trading, HAIDI, petits contrats | J-19 (HAIDI) |
| Compute | Pas de GPU pour 1B+ | High | Oui | ST Digital, HAIDI pour locatif | J-19 ou confirmation ST |
| Donnees | Zero donnees Ewe structurees | High | Oui | Collecte: Bible Ewe, scraping, voice | 2 semaines |
| Talent | ML natif absent | Medium | Partiellement | AI copilote compense | — |
| Carte bancaire | Impossible de payer cloud | High | Non sans solution | Alternative: compute gratuit (Kaggle, HF) | — |
| Distribution | Zero canal | High | Oui | DIOS framework | Mois 2-3 |

## The Binding Constraint

**Binding constraint:** CASH.

Si le cash est resolue (HAIDI ou EA stable), TOUS les autres constraints deviennent solubles :
- Compute → on peut payer du locatif
- Donnees → on peut payer des annotateurs
- Talent → on peut embaucher
- Distribution → on peut payer des campagnes

## Constraints We Cannot Remove

- Pas de carte bancaire (doit etre contourne)
- Puissance de calcul limitee sur Kaggle (doit etre accepte pour le premier modele)
- Pas de reseau investisseurs (doit etre construit)

## Footer

| Field | Value |
|-------|-------|
| Document | VAOS Document 21 |
| Phase | V — Capital Architecture |
| Owner | Kheir Lissi |
