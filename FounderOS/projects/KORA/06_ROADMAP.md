# KORA ROADMAP — V4.0
## Mission-Driven Strategy (Step 6)

---

## Structure

Roadmap derivee de la Vision (toutes categories LLM/image/video/audio), Mission (modele aussi performant, accessible sans barriere), et assets reels.

Pas de biais. Pas de "commencer par le langage parce que c'est plus facile". Le labo construit tout.

---

## Compute Reality

| Source | GPU | Capacite | Quand |
|--------|-----|----------|-------|
| Kaggle (1 compte) | T4x2 | 30h/sem | Maintenant |
| Kaggle (10 comptes) | T4x2 | 300h/sem | Immediate (multi comptes) |
| ST Digital | A confirmer | H100/A100 | Accord verbal |
| Locatif (vast/runpod) | Variable | Pay-as-you-go | Si HAIDI ou revenue |

**Premier entrainement :** 300-500M params, architecture MoE, ~1-2 semaines sur 10 comptes Kaggle.
**Prochain saut :** 1B+ params, image, video → necessite ST Digital ou compute payant.

---

## Sprint 1: Labo Foundation (Jours 1-14)

Pas de biais vers une categorie. Tout est prepare pour TOUS les types de modeles.

| # | Livrable | Description |
|---|----------|-------------|
| 1.1 | Multi-compte Kaggle | Creer 10 comptes Kaggle, automatiser le lancement parallele. Infrastructure d'entrainement distribuee. |
| 1.2 | Architecture research | Etudier papiers pour TOUTES categories: LLM (DeepSeek MoE, Qwen), Image (DiT, Flux), Audio (Coqui), Video (Veo). Selectionner la premiere architecture. |
| 1.3 | Dataset pipeline | Pipeline de collecte pour TOUTES les categories: texte multilingue (ewe, fr, en, mina, kabye), images, audio, video. |
| 1.4 | ST Digital confirmation | Relancer l'accord GPU. Estimer le compute disponible. |
| 1.5 | HAIDI application | Soumettre le grant $38K (J-19). |

**Gate :** Infrastructure multi-compte fonctionnelle, architecture selected, dataset pipeline pret.

---

## Sprint 2: Premier Modele (Jours 15-30)

Le premier modele depend de ce qui est le plus viable avec le compute disponible et la data collectee.

**Candidates (ordre non determine — decision au moment du gate) :**

| Categorie | Taille possible sur Kaggle 10x | Temps estime |
|-----------|-------------------------------|--------------|
| LLM 300-500M MoE | Oui | 1-2 semaines |
| Small TTS/voice model | Oui | 1 semaine |
| Small image model (DiT tiny) | Possible mais long | 4-6 semaines |
| Video model | Non (besoin ST Digital) | — |

**Decision :** Au lancement du Sprint 2, on choisit LA categorie ou on a le plus de chances d'atteindre le niveau frontier avec le compute disponible.

| # | Livrable | Description |
|---|----------|-------------|
| 2.1 | Premier modele KORA | Entraine depuis zero dans la categorie choisie. |
| 2.2 | API publique | Interface standard (texte) pour le modele. |
| 2.3 | Interface vocale (surcouche) | Distribution pour non-instruits. Meme modele, entre vocale. |
| 2.4 | Benchmark public | Comparer aux frontier. Toutes competences du modele, pas juste langue. |
| 2.5 | Annonce labo | KORA existe. Premier modele. Benchmark. Vision. |

**Gate :** Modele qui tient la comparaison avec les frontier sur au moins un axe. API publique. Benchmark publie.

---

## Sprint 3: Deuxieme & Troisieme Categorie (Mois 2-3)

| # | Livrable | Description | Dependance |
|---|----------|-------------|------------|
| 3.1 | Modele suivant | Prochaine categorie (ex: si LLM en sprint 2, image ou audio en sprint 3). | Compute ST Digital ou HAIDI |
| 3.2 | App multi-entree | Smartphone app: texte + voix. Les deux interfaces sur tous les modeles. | Modeles + API |
| 3.3 | 100 premiers utilisateurs | Instruits via texte, non-instruits via voix. Feedback. | App |
| 3.4 | Revenue debutant | API payante, freemium. | API stable |

**Gate :** Deux categories de modeles fonctionnelles. 100 utilisateurs. Revenue > $0.

---

## Sprint 4: Couverture Complete (Mois 3-6)

| # | Livrable | Description |
|---|----------|-------------|
| 4.1 | Toutes categories | LLM + image + audio + video si compute permis. |
| 4.2 | Partenaires distribution | Telecoms, hardware, institutions. |
| 4.3 | Scale | Modele plus grand, architecture amelioree. |

**Gate :** Couverture multi-categorie. Partenaires actifs. Revenue stable.

---

## Timeline

```
Semaine 1-2         Semaine 3-4         Mois 2-3           Mois 3-6
──────────────────────────────────────────────────────────────────────────
Kaggle x10          PREMIER MODELE      Deuxieme modele    Toutes categories
Architecture        API + Voix          App mobile         Partenaires
Dataset pipeline    Benchmark           Users > 100        Revenue stable
HAIDI               Annonce labo        Revenue > $0
ST Digital confirm
```

---

## Gestion des Risques

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Compute insuffisant pour la categorie choisie | Retard | Commencer par la categorie qui tient dans le compute (LLM small ou audio) |
| Haidi refuse | Perte $38K | EA Trading + petits contrats |
| Pas de donnees pour une categorie | Impossible d'entrainer | Pipeline data sprint 1 obligatoire |

---

## Footer

| Field | Value |
|-------|-------|
| Document | KORA Roadmap |
| Version | 4.0 — Multi-Category |
| Owner | Kheir Lissi |
| Last Updated | 2026-06-28 |
