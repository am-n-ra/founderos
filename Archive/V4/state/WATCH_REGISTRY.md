# WATCH REGISTRY

## Purpose

Liste centralisée de tout ce que FounderOS surveille pour toi : deadlines, appels à projets, news, opportunités, follow-ups. Checké automatiquement à chaque heure. Les résultats sont scorés et seule l'essentiel remonte à la session.

## Rules

1. Watchtower tourne toutes les **1 heure** (Windows Task Scheduler)
2. Chaque résultat est scoré (🔴/🟡/🟢/⚪)
3. 🔴 et 🟡 sont écrits dans ALERTS.md — lus au prochain boot
4. 🟢 et ⚪ seulement dans WATCH_REPORT.md (consultable si besoin)
5. Next Check est mis à jour automatiquement après chaque run

---

## Active Watches

| Watch Item | Project | Query / Method | Frequency | Priority | Next Check | Last Result | Status |
|------------|---------|---------------|-----------|----------|------------|-------------|--------|
| Djanta Tech Hub Innov'Action | OMNI | webfetch "https://djantatechhub.gouv.tg" | Daily | 🟡 | 2026-06-27 | 2026-06-26: ERROR: webfetch "https://djantatechhub.gouv.tg" - No connection adapters were fo | ⚪ |
| ST Digital — compute partnership status | KORA | manual | Daily | 🔴 | 2026-06-27 | 2026-06-26: [manual] ST Digital — compute partnership status - no automated check method | 🟡 |
| Herlog — response | KORA | manual | Daily | 🔴 | 2026-06-27 | 2026-06-26: [manual] Herlog — response - no automated check method | 🟡 |
| Radcliffe Fellowship | KORA | manual | Weekly | 🔴 | 2026-06-28 | Deadline Sep/Oct 2026. $78k + $5k + housing. Harvard. | 🟢 |
| KORA Government Positioning — ATD/Cina Lawson | KORA | manual prep | Weekly | 🟡 | 2026-06-28 | À préparer | 🟢 |
| ST Digital subsidiaries / compute infra news | KORA | ddgs "ST Digital Africa compute partnership 2026 news" | Daily | 🔴 | 2026-06-27 | 2026-06-26: [manual] ST Digital subsidiaries / compute infra news - no automated check metho | 🟡 |
| Herlog Holding impact investment news | KORA | ddgs "Herlog Holding impact investment Africa 2026" | Daily | 🟡 | 2026-06-27 | 2026-06-26: [manual] Herlog Holding impact investment news - no automated check method | 🟡 |
| Lacuna Fund — new call for proposals | KORA | ddgs "Lacuna Fund call for proposals 2026 African languages" | Daily | 🔴 | 2026-06-27 | 2026-06-26: [manual] Lacuna Fund — new call for proposals - no automated check method | 🟡 |
| AI4D Africa — next call | KORA | ddgs "AI4D Africa call for proposals 2026 deadline" | Daily | 🔴 | 2026-06-27 | 2026-06-26: [manual] AI4D Africa — next call - no automated check method | 🟡 |
| Éwé ASR dataset & speech resources | KORA | ddgs "Ewe language ASR dataset speech recognition" | Daily | 🟡 | 2026-06-27 | 2026-06-26: [manual] Éwé ASR dataset & speech resources - no automated check method | 🟡 |
| Éwé text corpus / lexicon | KORA | ddgs "Ewe language dictionary text corpus download" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| Common Voice Éwé | KORA | ddgs "Common Voice Ewe language dataset" | Weekly | 🟢 | 2026-06-28 | PDF Building Ewe Language Dataset trouvé. | 🟢 |
| KORA mention/press/web | KORA | ddgs "KORA Lab Togo AI" | Weekly | 🟢 | 2026-06-28 | Togo AI Labs + Facebook AI Kora Lab (24.9k likes). | 🟢 |
| Google for Startups AI / cloud credits | KORA | ddgs "Google for Startups AI Africa cloud credits 2026 deadline" | Weekly | 🔴 | 2026-06-28 | — | 🟢 |
| AWS Activate / Microsoft AI4Good Africa | KORA | ddgs "AWS Activate OR Microsoft AI4Good Africa startup compute credits eligibility 2026" | Weekly | 🔴 | 2026-06-28 | — | 🟢 |
| OpenAI startup credits | KORA | ddgs "OpenAI startup credits Africa apply deadline 2026" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| Masakhane grants / African NLP | KORA | ddgs "Masakhane grant funding NLP African languages 2026 call" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| AfDB AI innovation prize | KORA | ddgs "African Development Bank AI innovation challenge 2026 deadline" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| Mastercard Foundation AI Africa | KORA | ddgs "Mastercard Foundation AI Africa grant startup 2026 deadline" | Weekly | 🟢 | 2026-06-28 | — | 🟢 |
| Togo digital economy policy | KORA | ddgs "Togo digital economy Cina Lawson ARCEP AI startup 2026" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| EURUSD London/NY session overlap | TRADING | ddgs "EURUSD London New York overlap session time UTC forex hours" | Hourly | 🔴 | 2026-06-26 | 2026-06-26: [manual] EURUSD London/NY session overlap - no automated check method | 🟡 |
| Forex high-impact economic events | TRADING | ddgs "forex economic calendar high impact events this week EURUSD" | Daily | 🔴 | 2026-06-27 | 2026-06-26: [manual] Forex high-impact economic events - no automated check method | 🟡 |
| Backtesting platform free | TRADING | ddgs "free forex backtesting platform EURUSD historical data download" | Weekly | 🔴 | 2026-06-28 | — | 🟢 |
| Funded trader community EURUSD | TRADING | ddgs "FTMO funded trader EURUSD strategy tips 2026" | Weekly | 🟢 | 2026-06-28 | — | 🟢 |
| Togo startup competition prize | OMNI | ddgs "Togo startup competition prize Lomé 2026 entrepreneur digital" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| IDRC / SIDA African NLP grant | KORA | ddgs "IDRC SIDA African NLP speech dataset grant 2026 deadline low resource languages" | Weekly | 🟡 | 2026-06-28 | — | 🟢 |
| Soya prix Atakpamé | SOJACO | manual | Weekly | 🟢 | 2026-06-28 | 350 FCFA/kg. Deal 750/bol non viable. | 🟡 |

---

## Priority Levels

| Priority | Meaning | Action | Shown at boot |
|----------|---------|--------|--------------|
| 🔴 CRITICAL | Deadline imminente, funding direct, action requise | Do it this session | ✅ Yes |
| 🟡 IMPORTANT | Nouvelle opportunité, follow-up chaud, valeur haute | Review this week | ✅ Yes |
| 🟢 OPPORTUNITY | Track, pas d'urgence | Monitor only | ❌ No |
| ⚪ NO ACTION | Résultat vide, erreur, pas de changement | Ignore | ❌ No |

---

## Archive

(Watch items completed or no longer relevant moved here.)

---

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Created | 2026-06-21 |
| Last Updated | 2026-06-25 |
| Owner | System |