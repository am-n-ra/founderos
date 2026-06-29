# FounderHQ V5 — Autopilot + Headquarter Design

> **Architecture:** SYSTEM_PROMPT.md (~200 lignes) contient TOUTE la logique. Frameworks chargés à la demande. Projets = dossiers knowledge/ + assets/ écrits par l'IA. **GitHub repo** (public/privé) = source of truth universelle. **Gist public** = bootstrap/distribution. **sync.py** (~100 lignes) = push/pull Git + Gist. 28 scripts Python supprimés, 560 .md supprimés.
>
> **Principe :** L'IA raisonne, les fichiers persistent via Git.

---

## Section 1 : Architecture Globale

### Les 4 piliers sacrés

| Pilier | Dans V4 | Dans V5 |
|--------|---------|---------|
| Classification 12 modules | cycle.py + diagnose.py + SYSTEM_PROMPT.md | **SYSTEM_PROMPT.md uniquement** |
| Cycle counter guard | cycle.py (529 lignes) + counter files | **Prompt rules** : Get-Date → vérifie CURRENT.md |
| State management fichiers | 27 fichiers + state_manager.py | **3 fichiers** : CURRENT.md, TIMELINE.md, DEADLINES.md |
| Sync multi-appareil | sync.py (564 lignes) + daemon | **Fast.io MCP** + sync.py (~100 lignes) |

### Ce qui est supprimé (28 scripts Python → 1)

| Script | Lignes | Remplacé par |
|--------|--------|--------------|
| cycle.py | 529 | Prompt rule: Get-Date + Read CURRENT.md |
| diagnose.py | 305 | Prompt rule: lecture directe des fichiers |
| kickoff.py | 275 | Prompt rule: autopilote check |
| state_manager.py | 100 | Write tool de l'IA |
| fhq_daemon.py | 439 | **Supprimé** (MCP stdio cassé sur Windows) |
| watchtower.py | 335 | Prompt rule: DEADLINES.md check |
| timekeeper.py | 218 | Prompt rule: Get-Date + DEADLINES.md |
| astra_core.py | 965 | Fichier ASTRA.md de référence + prompt rule |
| astra_reading.py | 610 | Fichier ASTRA.md de référence |
| astra_daily.py | 197 | Prompt rule simple |
| astra_forecast.py | 195 | Prompt rule simple |
| astra_birth.py | 149 | Prompt rule + calcul VIA web search |
| installer.py | 357 | README.md |
| build_seed.py | 212 | Supprimé |
| gate_checker.py | 135 | PRG dans le prompt |
| snapshot.py | 111 | Supprimé |
| venture_intake.py | 564 | Prompt rule + VAOS.md |
| persona_detect.py | 199 | Supprimé |
| aimless_check.py | 89 | Prompt rule |
| session_log.py | 71 | TIMELINE.md |
| cadence_engine.py | 53 | Supprimé |
| timeline_logger.py | 51 | TIMELINE.md |
| bootstrap.py | 48 | Supprimé |
| cycle_runner.py | 34 | Supprimé |
| deploy_pythonanywhere.py | 77 | Supprimé |
| deploy_railway.py | 59 | Supprimé |
| **Total supprimé** | **~6 000 lignes** | |

### Ce qui reste

| Fichier | Lignes | Rôle |
|---------|--------|------|
| `SYSTEM_PROMPT.md` | ~200 | Classification + autopilote + PRG |
| `state/CURRENT.md` | ~20 | État session (écrit par l'IA) |
| `state/TIMELINE.md` | ~variable | Événements globaux (écrit par l'IA) |
| `state/DEADLINES.md` | ~10 | Deadlines tous projets (écrit par l'IA) |
| `state/PROFILE.md` | ~30 | Profil fondateur |
| `frameworks/VAOS.md` | ~variable | Venture process (chargé à la demande) |
| `frameworks/DIOS.md` | ~variable | Distribution (chargé à la demande) |
| `frameworks/DAOS.md` | ~variable | Daily execution (chargé à la demande) |
| `frameworks/LEOS.md` | ~variable | Learning (chargé à la demande) |
| `references/ASTRA.md` | ~variable | Référence astrologique |
| `Runtime/sync.py` | ~100 | Backup vers GitHub |
| `projects/*/` | ~variable | Un dossier par projet |
| **Total fichiers système** | **~15** | (contre 927) |

---

## Section 2 : Distribution Universelle (One-Phrase Install)

### Le mécanisme : Bootstrap Gist

```
1. L'utilisateur dit : "Install FounderHQ"
2. L'IA reçoit l'instruction dans le prompt ou via web_fetch
3. L'IA charge le SYSTEM_PROMPT.md depuis l'URL publique
4. FounderHQ est actif
```

### Sur chaque plateforme

| Plateforme | Installation | Friction |
|------------|-------------|----------|
| **openode** | `opencode.json` → `"instructions": ["https://raw.githubusercontent.com/.../SYSTEM_PROMPT.md"]` | Fichier à créer une fois |
| **Cursor** | Cursor Settings → Rules → Add Remote Rule → coller l'URL GitHub | ~2 clics |
| **Claude Code** | Copier `SYSTEM_PROMPT.md` dans `.claude/` ou `CLAUDE.md` | 1 fichier à créer |
| **ChatGPT** | Custom GPT avec instructions + Actions GitHub API | Création GPT (+20$), puis lien partageable |
| **Gemini** | Gems → instructions système → lien partageable Google Drive | Création Gem, puis lien |
| **Claude AI (web)** | Projet → instructions système importées | 1 projet à créer |

### Auto-install pour coding agents (la phrase magique)

L'utilisateur tape dans n'importe quel coding agent :
```
Install FounderHQ
```

Si le `SYSTEM_PROMPT.md` commence par une instruction de bootstrap :
```markdown
## Bootstrap (première utilisation)

Si tu reçois l'instruction "Install FounderHQ" ou "Bootstrap FounderHQ" :
1. Fetch https://raw.githubusercontent.com/junio/FounderHQ/main/FounderOS/SYSTEM_PROMPT.md
2. Charge son contenu comme instructions système
3. Crée la structure de dossiers si elle n'existe pas
```

Cette instruction dit à l'IA **de se remplacer elle-même** par le vrai prompt.

### Distribution à n'importe qui

1. **GitHub public repo** : `github.com/junio/FounderHQ`
2. **Gist public** : `gist.github.com/.../fhq-bootstrap` (ce qu'on a déjà)
3. **skills.sh** : `npx skills add founderhq` (Vercel, 30+ agents)
4. **Custom GPT Store** : Lien ChatGPT partageable
5. **Gemini Gems** : Lien Google Drive partageable
6. **Claude Project Template** : Lien Claude partageable

---

## Section 3 : L'Autopilote (SYSTEM_PROMPT.md)

### Structure compacte (~200 lignes)

```
Lignes 1-20 : Bootstrap + identité
  - Si "Install FounderHQ" → fetch le vrai prompt depuis l'URL
  - Get-Date avant chaque réponse
  - Classification des messages (table)
  - Règles absolues (NE JAMAIS commit/submit sans approbation)

Lignes 21-80 : Classification + Autopilote
  - Table des 12 modules : fhq, fhqa, boot, shutdown, ideas, learning...
  - Règles de proactivité (deadlines, guidance, anti-roue-libre)
  - Règle "j'ai une idée" → active VAOS automatiquement
  - Règle "je dois apprendre" → active LEOS

Lignes 81-120 : Pre-Response Gate
  - Get-Date → CURRENT.md → DEADLINES.md → TIMELINE.md
  - Si deadline <24h : mentionner en premier
  - Si message >15min : refresh contexte

Lignes 121-160 : Headquarter (projets + persistance)
  - Structure des dossiers projets
  - Règles d'écriture : toute décision → knowledge/
  - Sync via Fast.io MCP (ou fichier local)
  
Lignes 161-180 : Rôles d'experts
  - Comment adapter son rôle (mentor, co-founder, CTO, CFO, CMO, COO)
  - Comment charger un framework (VAOS.md, DIOS.md, DAOS.md...)

Lignes 181-200 : Format de réponse + footer
```

### Règles autopilote clés

```
RÈGLE #1 : Proactivité
- Get-Date avant chaque réponse
- Si deadline <24h dans DEADLINES.md → mentionne-la en premier
- Si l'utilisateur n'a pas de direction → propose l'action la plus importante

RÈGLE #2 : Guidance venture (le "j'ai une idée" mode)
- L'utilisateur a une idée → tu le guides étape par étape via VAOS
- Il n'a pas besoin de connaître le processus
- À la fin : un projet structuré avec README.md + knowledge/ + deadlines

RÈGLE #3 : Équipe d'experts
- Adapte ton rôle : mentor (vision), co-founder (stratégie), CTO (tech), CFO (finance), CMO (marketing)
- Charge le framework correspondant à la tâche

RÈGLE #4 : Persistance absolue
- Toute décision, idée, changement → écris dans les fichiers
- CURRENT.md, TIMELINE.md, DEADLINES.md, projects/*/knowledge/
- NE JAMAIS présumer que le context window survivra

RÈGLE #5 : Anti-roue-libre
- Si hésitation → check DEADLINES.md + PRIORITY
- Ne finis JAMAIS sans proposer une prochaine action
```

---

## Section 4 : Le Headquarter (GitHub + Gist)

### Architecture de persistance

```
┌────────────────────────────────────────────────────────────────────────┐
│                     GITHUB PRIVATE REPO (source of truth)               │
│  github.com/junio/FounderHQ/ — tout le système + projets + état         │
│  Gratuit, illimité, versionné, accessible depuis TOUT LLM               │
└───────────────────┬────────────────────────────────────────────────────┘
                    │
           ┌────────┴────────┐
           │                 │
           ▼                 ▼
    Gist public          Gist privé
  (bootstrap)           (sync backup)
```

### Comment chaque LLM accède aux fichiers

| LLM | Méthode | Complexité |
|-----|---------|-----------|
| **openode** | `opencode.json` instructions + Read/Write tool | ✅ 0 code |
| **Cursor** | `.cursor/rules/` + file system | ✅ 0 code |
| **Claude Code** | File system + CLAUDE.md | ✅ 0 code |
| **ChatGPT Web** | Custom GPT Actions → GitHub REST API | ⚡ ~200 lignes OpenAPI |
| **Gemini Web** | Gems + Google Drive sync | ⚡ 1 clic |
| **ChatGPT/Claude Web** | Dropbox MCP → dossier local syncé | ⚡ Config Dropbox |

### Sync : sync.py (~100 lignes)

```python
# Runtime/sync.py
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

def git(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)

if sys.argv[1:2] == ["push"]:
    git("git add -A")
    git('git commit -m "auto: sync"')
    git("git push origin main")
    print("OK: pushed to GitHub")
elif sys.argv[1:2] == ["pull"]:
    git("git pull origin main")
    print("OK: pulled from GitHub")
elif sys.argv[1:2] == ["gist-push"]:
    # Backup vers le Gist privé (optionnel)
    print("OK: gist backup")
else:
    print("Usage: python sync.py push|pull|gist-push")
```

```python
# Runtime/sync.py — ~100 lignes
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

def git(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)

if sys.argv[1:2] == ["push"]:
    git("git add -A")
    git('git commit -m "auto: sync"')
    git("git push origin main")
    print("OK: pushed to GitHub")
elif sys.argv[1:2] == ["pull"]:
    git("git pull origin main")
    print("OK: pulled from GitHub")
```

---

## Section 5 : Structure Complète

```
FounderHQ/
├── SYSTEM_PROMPT.md          # ~200 lignes — le cerveau (autopilote + headquarter)
├── state/
│   ├── CURRENT.md            # État session (écrit par l'IA)
│   ├── TIMELINE.md           # Timeline globale
│   ├── DEADLINES.md          # Toutes deadlines
│   └── PROFILE.md            # Profil fondateur
├── projects/
│   ├── KORA/
│   │   ├── README.md         # Mission, vision, statut
│   │   ├── knowledge/        # Notes, décisions, recherches
│   │   └── assets/           # Code, docs, media
│   ├── DOODLEMIND/
│   ├── SOJACO/
│   └── ...
├── frameworks/
│   ├── VAOS.md               # Venture creation (chargé si classification VENTURE)
│   ├── DIOS.md               # Distribution (chargé si DISTRIBUTION)
│   ├── DAOS.md               # Daily execution (chargé si EXECUTION)
│   ├── LEOS.md               # Learning (chargé si LEARNING)
│   ├── CAOS.md               # Cash allocation (chargé si FUNDRAISING)
│   └── CEOS.md               # Content execution (chargé si CONTENT)
├── references/
│   └── ASTRA.md              # Référence astrologique (chargé si fhqa)
├── Runtime/
│   └── sync.py               # ~100 lignes — backup GitHub
├── opencode.json
└── .env
```

**~15 fichiers système** + N dossiers projets (contre 927 fichiers aujourd'hui)

---

## Section 6 : Plan de Migration

### Phase 1 : Bootstrap (1 session)
1. Écrire le nouveau `SYSTEM_PROMPT.md` (~200 lignes)
2. Créer les 3 state files : `CURRENT.md`, `TIMELINE.md`, `DEADLINES.md`
3. Écrire le nouveau `Runtime/sync.py` (~100 lignes)
4. Configurer GitHub repo + Gist
5. Publier le Gist bootstrap public

### Phase 2 : Migration projets (1-2 sessions)
6. Pour chaque projet : créer `README.md` + `knowledge/` + `assets/`
7. Copier les décisions clés, recherches, assets depuis V4
8. Vérifier que rien n'est perdu

### Phase 3 : Nettoyage (1 session)
9. Supprimer 28 scripts Python engine
10. Supprimer 560 .md obsolètes
11. Supprimer 27 vieux state files
12. Supprimer 15 protocoles (intégrés dans le prompt)
13. Archiver l'ancienne structure

### Phase 4 : Distribution (1 session)
14. Publier sur skills.sh (`npx skills add founderhq`)
15. Créer Custom GPT + Gemini Gem + Claude Project template
16. Tester "Install FounderHQ" sur chaque plateforme
17. Documenter le processus d'installation

---

## Section 7 : Tests

```
1.  "Install FounderHQ" → bootstrap → système actif
2.  fhq → classification EXECUTION → comportement quotidien
3.  fhqa → classification ASTRA → guidance astrologique
4.  "j'ai une idée" → VENTURE → process VAOS
5.  boot → BOOT → reset session
6.  shutdown → SHUTDOWN → save + sync
7.  Get-Date avant chaque réponse
8.  DEADLINES.md <24h → mentionné
9.  Nouvelle session → tout persisté (GitHub)
10. sync.py push → GitHub backup
11. Changement de LLM → mêmes données (via GitHub repo)
```

---

## Footer

| Field | Value |
|-------|-------|
| Version | V5 Design Spec |
| Date | 2026-06-29 |
| Approvals | Section 1 (Architecture) ✅, Section 2 (Distribution) ✅, Section 3 (Autopilote) ✅, Section 4 (Headquarter) ✅, Section 5 (Structure) ✅, Section 6 (Migration) ✅|
