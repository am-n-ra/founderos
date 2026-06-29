# Stratégie — Capture du Renversement de Tendance

**EURUSD | BACKTEST SÉANCES 24 & 25 | SPREAD 0-1 | SYMÉTRIQUE HAUSSE / BAISSE**

---

## Objectif

Identifier précisément le moment où une tendance prend fin et où une nouvelle commence — et capturer exactement la bougie qui initie ce nouveau mouvement. En entrant à l'aube du mouvement, le potentiel de gain est maximal : le marché part du point zéro dans la nouvelle direction.

---

## Les 3 piliers

| Pilier | Concept |
|--------|---------|
| **PILIER 01 — Sweep de liquidité** | La mèche de B2 balaye les liquidités dans la direction opposée à son corps, piégeant les derniers acteurs de la tendance précédente. |
| **PILIER 02 — Price Gap / Imbalance** | L'ouverture de B2 présente un écart par rapport à la clôture de B1, signalant un déséquilibre de pression directionnelle. |
| **PILIER 03 — Engulfing** | Le corps de B2 engloutit entièrement B1 (corps + mèches), signalant une domination franche dans la nouvelle direction. |

---

## Définitions

- **B1** — bougie de référence (la précédente).
- **B2** — bougie signal qui génère le setup. La direction du trade est toujours celle de B2.

---

## Les 6 conditions d'un setup valide

Toutes les conditions doivent être remplies simultanément. La stratégie s'applique à la hausse et à la baisse.

### 1. Opposition directionnelle

B2 doit être dans la direction opposée à B1.

| | Condition |
|---|---------|
| **B2 BAISSIÈRE** | B1 était haussière |
| **B2 HAUSSIÈRE** | B1 était baissière |

### 2. Engulfing — B2 engloutit B1

La range complète de B2 (corps + mèches) doit englober entièrement la range de B1. **Le corps de B2 doit dépasser d'au moins 1 point** le haut et le bas de B1. Si le corps s'arrête pile au high ou low de B1 → pas setup.

| | Condition |
|---|---------|
| **B2 BAISSIÈRE** | Corps de B2 < Bas de B1 **- 1 point minimum** |
| **B2 HAUSSIÈRE** | Corps de B2 > Haut de B1 **+ 1 point minimum** |

### 3. Sweep de liquidité — mèche de B2

La mèche de B2 se balaye dans la direction **inverse** de son corps, **au-delà de l'extrême correspondant de B1**. Le sens de la mèche importe : si B2 est haussière, on veut une mèche baissière (lower wick). Si B2 est baissière, on veut une mèche haussière (upper wick). **Au-delà signifie strictement plus loin** — pas au même prix.

| | Condition |
|---|---------|
| **B2 BAISSIÈRE** | Mèche haute de B2 dépasse le haut de B1 |
| **B2 HAUSSIÈRE** | Mèche basse de B2 descend sous le bas de B1 |

### 4. Price Gap — ouverture de B2

L'ouverture de B2 présente un gap dans le sens de B2 par rapport à la clôture de B1.

| | Condition |
|---|---------|
| **B2 BAISSIÈRE** | Ouverture B2 < Clôture B1 |
| **B2 HAUSSIÈRE** | Ouverture B2 > Clôture B1 |

### 5. Clôture confirmatrice — B2 sort de la range de B1

B2 clôture au-delà de l'extrême de B1 dans sa direction de mouvement.

| | Condition |
|---|---------|
| **B2 BAISSIÈRE** | Clôture B2 < Bas de B1 |
| **B2 HAUSSIÈRE** | Clôture B2 > Haut de B1 |

### 6. Confirmation de fin de tendance — les 3 bougies précédant B1

Examine les 3 bougies immédiatement antérieures à B1. Si aucune ne dépasse l'extrême dans le sens inverse, c'est un vrai renversement, pas une correction.

| | Condition |
|---|---------|
| **B2 BAISSIÈRE** | Aucune des 3 bougies précédentes n'a un plus haut supérieur au haut de B1 — B1 est un sommet isolé |
| **B2 HAUSSIÈRE** | Aucune des 3 bougies précédentes n'a un plus bas inférieur au bas de B1 — B1 est un creux isolé |

---

## Gestion du trade

### Entrée

À la clôture de B2, dans la direction de B2.

### Stop Loss

**SL = 10 points** (fixe, quel que soit le size de B2).

**Note :** En points (pas pips). 10 points = 1 pip sur MT5 5-digit.

### Take Profit

**TP = 34.1 points** (fixe, corrélation avec le 8, sous la limite max de 35 points).

**Note :** 34.1 points = 3.41 pips.

RR = 3.41:1

Le spread peut consommer 0.5-1 pip (5-10 points), donc 34.1 laisse une marge par rapport au 35 max. Le marché réalise généralement un minimum de 36 points dans la direction déterminée avant tout renversement.

### Résumé de gestion

| Paramètre | Valeur | Conversion |
|-----------|--------|------------|
| **SL** | 10 points | = 1 pip |
| **TP** | 34.1 points | = 3.41 pips |
| **RR** | 3.41:1 | — |
| **Entrée** | Clôture de B2 | — |

---

## Résultats du backtest

**Résultats avec SL=10 points, TP=34.1 points (RR 3.41:1)**

### Séance du 24 — 8 setups

| # | Résultat | RR | Observation |
|---|---------|-----|-------------|
| 1 | Perte | -1R | SL touché |
| 2 | Gain | +3.41R | TP atteint |
| 3 | Gain | +3.41R | TP atteint |
| 4 | Gain | +3.41R | TP atteint |
| 5 | Gain | +3.41R | TP atteint |
| 6 | Perte | -1R | SL touché |
| 7 | Gain | +3.41R | TP atteint |
| 8 | Gain | +3.41R | TP atteint |

### Séance du 25 — 3 setups

| # | Résultat | RR | Observation |
|---|---------|-----|-------------|
| 1 | Gain | +3.41R | TP atteint |
| 2 | Perte | -1R | SL touché |
| 3 | Perte | -1R | SL touché |

### Bilan

| Métrique | Valeur |
|----------|--------|
| **Total trades** | 11 |
| **Wins** | 7 |
| **Losses** | 4 |
| **Win Rate** | 63.6% |
| **RR fixe** | 3.41:1 |
| **Net total** | 7 × 3.41 - 4 × 1 = **19.87R** |
| **Gain moyen par win** | 3.41R |
| **Perte moyenne par loss** | 1.00R |

---

## Observations clés

- Chaque paire de bougies consécutives est une opportunité potentielle — les 6 conditions seules valident ou invalident l'entrée. Aucun jugement subjectif.
- La stratégie est entièrement symétrique : les 6 règles s'appliquent de façon identique à la hausse et à la baisse.
- La combinaison sweep + gap + engulfing élimine les simples corrections pour ne retenir que les vrais renversements de tendance.
- Le SL fixe à 10 pips et le TP à 34.1 pips offrent un RR constant de 3.41:1, sans jugement sur la taille de la bougie.
- Le mouvement minimum de 36 points fournit un TP naturel et défendable sans jugement subjectif sur la cible finale.

---

*Document créé le 2026-06-25 | Stratégie EURUSD | Backtest séances 24-25 juin*
