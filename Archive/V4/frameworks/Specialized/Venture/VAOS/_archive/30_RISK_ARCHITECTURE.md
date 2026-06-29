# VAOS — 30 RISK ARCHITECTURE

## Purpose

What could go wrong?

## Risk Categories

| Risk | Probability | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| Cash epuise avant revenue | Haute | Fatal | EA Trading, HAIDI, petits contrats | Kheir |
| Premier modele ne converge pas | Moyenne | Retard | Architecture plus simple, plus petit modele | Kheir |
| Kaggle suspendu/compte bloque | Moyenne | Retard | Multi-comptes, fallback Colab | Kheir |
| ST Digital GPU jamais confirme | Haute | Compute bloque | Locatif via HAIDI ou EA | Kheir |
| HAIDI refuse | Haute | Perte $38K | Autres grants, API revenue rapide | Kheir |
| EA Trading perd > 20% | Moyenne | Perte oxygen | Stop-loss a -10% | Kheir |
| Concurrent (etranger) cible Afrique | Faible | Competition | Nos donnees locales sont notre avantage | Kheir |
| Burnout fondateur solo | Moyenne | Arret | Rythme soutenable, IA copilote | Kheir |

## Top 5 Risks

1. **Cash epuise** — La seule qui peut tuer le projet. Mitigation: priorite revenue avant tout.
2. **HAIDI rate + EA echoue** — Scenario de crise. Mitigation: petits contrats, consulting.
3. **Premier modele ne marche pas** — Risque technique reel. Mitigation: commencer petit.
4. **ST Digital ne confirme pas** — Compute bloque. Mitigation: Kaggle x10 + locatif.
5. **Burnout** — Solo, mission intense. Mitigation: IA copilote, rythme, pas de crunch inutile.

## Kill Criteria

- Cash negatif et aucune source de revenue visible a 30 jours → STOP
- Aucun modele fonctionnel apres 6 mois → STOP
- Sante mentale/physique degradee → STOP

## Risk Monitoring

- **Daily:** Trading P&L, cash restant
- **Weekly:** Entrainement progression, blockers
- **Monthly:** Revenue check, runway update

## Footer

| Field | Value |
|-------|-------|
| Document | VAOS Document 30 |
| Phase | VI — Scaling Architecture |
| Owner | Kheir Lissi |
