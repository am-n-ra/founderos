# Design — EA Capture du Renversement de Tendance

**Date:** 2026-06-25
**Stratégie:** Capture du Renversement de Tendance — EURUSD M1
**Statut:** En cours de validation

---

## 1. Objectif

Automatiser la détection des setups de renversement de tendance sur EURUSD M1, selon les 6 règles définies dans `docs/strategie-renversement-tendance.md`. Le bot doit tourner 24/7, surveiller les bougies, et journaliser les setups détectés.

---

## 2. Architecture

### Phase 1 — Détection locale (sans trading)

```
[PC Local — Python]
    │
    ├── Bot M1 Monitor
    │   ├── Connexion MT5 (MetaTrader5 package)
    │   ├── Lit les bougies EURUSD M1 toutes les minutes
    │   ├── Applique les 6 règles de détection
    │   ├── Journalise les setups dans SQLite
    │   └── Log les trades potentiels (SL=10, TP=34.1)
    │
    └── Dashboard local (optionnel)
        └── Streamlit ou terminal affichant les setups en temps réel
```

### Phase 2 — Déploiement Oracle Cloud (détection + logging)

```
[Oracle Cloud Always Free — $0/forever] ✅ COMPTE CRÉÉ
    │
    ├── Linux VM (4 OCPU ARM, 24GB RAM)
    │
    ├── Bot M1 Monitor (même code que Phase 1)
    │   ├── Connexion MT5 via Wine + RPyC bridge
    │   ├── Même logique de détection
    │   ├── Logging vers SQLite + stdout
    │   └── Alertes Telegram (optionnel)
    │
    └── Systemd service (auto-restart, persistence)
```

### Phase 3 — Trading live (funded account)

```
[Oracle Cloud Always Free]
    │
    ├── Bot M1 Trader (extension du monitor)
    │   ├── Connexion MT5 via Wine + RPyC
    │   ├── Détection des setups (même code)
    │   ├── Exécution des ordres
    │   │   ├── SL = 10 points fixe (= 1 pip)
    │   │   ├── TP = 34.1 points fixe (= 3.41 pips)
    │   │   └── RR = 3.41:1
    │   ├── Position sizing
    │   │   ├── Risque de base = $0.50 fixe
    │   │   ├── Double quand profit cumulé ≥ 10× risque actuel
    │   │   ├── Pas de reset après loss
    │   │   └── Max $4.00 (limite margin $2000)
    │   ├── Risk management
    │   │   ├── Max drawdown quotidien : respecter les règles prop firm
    │   │   ├── Max positions simultanées : 1
    │   │   └── Pas de trading pendant news haute volatilité (optionnel)
    │   └── Monitoring
    │       ├── Dashboard Telegram
    │       ├── Logs SQLite
    │       └── Métriques journalières (winrate, net R, drawdown)
```

---

## 3. Règles de détection (récapitulatif)

| # | Règle | Condition |
|---|-------|-----------|
| R1 | Opposition | B2 direction opposée à B1 |
| R2 | Engulfing | Range B2 (corps + mèches) engloutit B1. Corps dépasse d'au moins 1 point |
| R3 | Sweep | Mèche inverse du corps de B2 dépasse l'extrême de B1 |
| R4 | Gap | Open de B2 gapé dans sa direction par rapport à Close de B1 |
| R5 | Close | Close de B2 dépasse l'extrême de B1 |
| R6 | Exhaustion | Aucune des 3 bougies avant B1 n'a un extremum dépassant celui de B1 |

---

## 4. Position Sizing

**Note :** On travaille en **points** (pas pips). Sur MT5 5-digit :
- 1 pip = 10 points = 0.00010
- 1 point = 0.1 pip = 0.00001
- EURUSD 1 lot : 1 pip = $10, 1 point = $1

| Paramètre | Valeur |
|-----------|--------|
| Risque de base | **$0.50 fixe** (pas pourcentage) |
| SL | **10 points** (= 1 pip) |
| TP | **34.1 points** (= 3.41 pips) |
| RR | 3.41:1 |
| Lot size = Risque / (SL × point value) | $0.50 / (10 × $1) = **0.05 lot** |

**Règle de scaling — escalier sans reset :**

Le risque double quand le profit cumulé atteint 10× le risque actuel. **Pas de reset après loss.**

| Profit cumulé | Risque par trade | Lot size | Margin (1:30) |
|---------------|------------------|----------|---------------|
| $0 – $4.99 | $0.50 | 0.05 lot | $167 |
| $5.00 – $9.99 | $1.00 | 0.10 lot | $333 |
| $10.00 – $19.99 | $2.00 | 0.20 lot | $667 |
| $20.00 – $39.99 | $4.00 | 0.40 lot | $1,333 |
| $40.00+ | ⚠️ **STOP** | — | Pas assez de margin |

**⚠️ Limite du compte $2000 :** Le risque max est **$4.00** (0.40 lot). Au-delà, la margin dépasse le compte.

**Pertes nécessaires pour annuler 1 gain :** Toujours **3.4 losses** (car RR = 3.41:1). Indépendant du niveau de risque.

**Exemple concret :**
1. Trade 1 : $0.50 risk → loss → cumulé = -$0.50
2. Trade 2 : $0.50 risk → win → cumulé = $1.21
3. Trade 3 : $0.50 risk → win → cumulé = $2.91
4. Trade 4 : $0.50 risk → win → cumulé = $4.62
5. Trade 5 : $0.50 risk → win → cumulé = $6.32 → **≥ $5 → risque passe à $1.00**
6. Trade 6 : $1.00 risk → loss → cumulé = $5.32 (reste à $1.00, pas de reset)
7. Trade 7 : $1.00 risk → win → cumulé = $8.73
8. Trade 8 : $1.00 risk → win → cumulé = $12.14 → **≥ $10 → risque passe à $2.00**
9. Trade 9 : $2.00 risk → win → cumulé = $18.96
10. Trade 10 : $2.00 risk → loss → cumulé = $16.96
11. Trade 11 : $2.00 risk → loss → cumulé = $14.96
12. **Résultat : $14.96 profit, risque actuel = $2.00**

---

## 5. Risk Management (Prop Firm Rules)

Le bot doit respecter les règles du funded account Next Instant ($2000) :
- **Max drawdown quotidien** : à vérifier (typiquement 4-5% = $80-100)
- **Max drawdown total** : à vérifier (typiquement 8-10% = $160-200)
- **Profit target** : à vérifier (typiquement 8-10% = $160-200)
- **Max positions** : 1 simultanée
- **Trading hours** : 24/5 (fermé le weekend)
- **Max lot size** : déterminé par la margin disponible

**Protection margin :**
- Le bot calcule le lot size = risque / (SL_points × point_value)
- Vérifie que la margin requise < free margin
- Si margin insuffisante, réduit le lot size ou skip le trade
- Seuil d'alerte : < 30% de free margin ($600)

**Règles bot :**
1. Arrêter le trading si drawdown quotidien atteint le max
2. Arrêter le trading si drawdown total atteint le max
3. Ne pas dépasser le lot size maximum (limite margin)
4. Log chaque trade dans SQLite avec timestamp, lot, P&L

---

## 6. Stack technique

### Phase 1 (Local)

| Composant | Technologie |
|-----------|-------------|
| Language | Python 3.11+ |
| Broker API | MetaTrader5 (pip install MetaTrader5) |
| Base de données | SQLite (logs setups) |
| Monitoring | Terminal / Streamlit (optionnel) |
| Scheduler | Cron (Linux) ou Task Scheduler (Windows) |

### Phase 2 (Oracle Cloud)

| Composant | Technologie |
|-----------|-------------|
| VM | Oracle Cloud Always Free ARM Ampere A1 |
| OS | Ubuntu 22.04 / 24.04 LTS |
| Python | Python 3.11 (apt install) |
| MT5 | Wine + RPyC bridge (mt5linux package) |
| Process manager | Systemd (auto-restart) |
| Logging | SQLite + journalctl |
| Alertes | Telegram Bot API (optionnel) |

### Phase 3 (Live)

| Composant | Technologie |
|-----------|-------------|
| Broker | Next Instant MT5 |
| Order execution | MetaTrader5 package via Wine |
| Position sizing | Script Python (double après 2 wins) |
| Risk guard | Script Python (drawdown check avant chaque trade) |

---

## 7. Structure des fichiers

```
FounderHQ/
├── Runtime/
│   └── engine/
│       ├── ea_monitor.py          # Phase 1 : détection + logging
│       ├── ea_trader.py           # Phase 3 : exécution des ordres
│       ├── strategy_rules.py      # Les 6 règles de détection
│       ├── position_sizing.py     # Logique de sizing (double après 2 wins)
│       ├── risk_manager.py        # Drawdown check, prop firm rules
│       └── mt5_bridge.py          # Connexion MT5 (local ou Wine)
├── State/
│   ├── ea_setups.db               # SQLite : log des setups détectés
│   └── ea_trades.db               # SQLite : log des trades exécutés
└── docs/
    ├── strategie-renversement-tendance.md
    └── ea-design.md               # Ce fichier
```

---

## 8. Plan de développement

| Phase | Tâche | Durée estimée | Priorité |
|-------|-------|---------------|----------|
| **P1** | `strategy_rules.py` — Implémenter les 6 règles | 2-3h | Haute |
| **P1** | `ea_monitor.py` — Boucle M1 + détection + SQLite | 2-3h | Haute |
| **P1** | Test local — Vérifier les setups sur données historiques | 1-2h | Haute |
| **P2** | Oracle Cloud — Créer le compte + VM | 30min | Moyenne |
| **P2** | Déployer le monitor sur Oracle Cloud | 1-2h | Moyenne |
| **P2** | MT5 sur Wine — Installer + tester | 2-3h | Moyenne |
| **P3** | `ea_trader.py` — Exécution des ordres | 2-3h | Basse |
| **P3** | `position_sizing.py` — Double après 2 wins | 1h | Basse |
| **P3** | `risk_manager.py` — Prop firm rules | 1-2h | Basse |
| **P3** | Test sur demo account (Next Instant) | 1-2h | Basse |

**Total estimé : 15-20h de développement**

---

## 9. Prochaines étapes immédiates

1. **Créer le compte Oracle Cloud** (credit card requis pour vérification)
2. **Implémenter `strategy_rules.py`** — les 6 règles de détection
3. **Implémenter `ea_monitor.py`** — la boucle M1
4. **Tester en local** sur données historiques MT5
5. **Valider** que les setups détectés matchent le backtest

---

*Design créé le 2026-06-25 | EA Capture du Renversement de Tendance*
