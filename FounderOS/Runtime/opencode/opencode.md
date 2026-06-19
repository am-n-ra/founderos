# OpenCode Runtime Adapter

## Detection

FounderHQ is auto-detected when the working directory contains `FounderOS/`. The protocol boots automatically via `Protocols/FOUNDEROS_PROTOCOL.md`.

## Fichier de configuration

`.opencode/instructions.md` contient les regles specifiques a l'environnement OpenCode.

## Particularites

- **Shell:** Windows PowerShell 5.1
- **Fuseau horaire:** Systeme local (detecte automatiquement par `Get-Date`). Conversion vers Lome UTC+0 chaque session.
- **Fichiers:** CRLF (Windows)
- **DST:** `[System.TimeZoneInfo]::Local.GetUtcOffset((Get-Date))` pour detecter le decalage effectif.

## Boot sequence (resume)

1. OpenCode charge `Protocols/FOUNDEROS_PROTOCOL.md` via instructions systeme
2. Le protocole guide toutes les operations subsequentes
3. `DECISION_GATES` est charge avant chaque action
4. `TEMPORAL_AWARENESS` verifie le temps a chaque reponse
5. Les frameworks sont charges a la demande via DECISION_GATES

## Limitations connues

- Pas de detection d'evenements automatique (session-based uniquement)
- Pas d'automation native (workflows executes manuellement par le LLM)
- Pas de multi-session awareness au-dela des fichiers
