# OMNI — Code Repository

## Status: ❌ No repository yet

## Setup

```bash
# After creating the GitHub repo:
gh repo create am-n-ra/omni --private --description "OMNI - L'index du commerce de proximité"
git submodule add https://github.com/am-n-ra/omni.git FounderOS/projects/Omni/CODE/omni
```

## Tech Stack (planned from Windsurf specs)

- Frontend: React + TypeScript + Vite
- Map: 3D map integration
- Auth: Neon Auth + Magic Links
- Chat: WebSocket
- Routing: OSRM
- Database: Neon (PostgreSQL)

## Pitch Decks

Pitch deck PDFs available in `../docs/`. See Omni README for details.

## Rules
- All OMNI code belongs in `CODE/` as a git submodule
- Never commit code directly into the project folder
