# FounderOS Automation Spec

## To be implemented progressively

### Cron ideal (quand un scheduler sera disponible)
- 07:00: generer TODAY_BRIEF.md
- 12:00: midday progress check
- 20:00: generer DAILY_LOG.md
- Dimanche: WEEKLY_REVIEW.md
- 1er du mois: MONTHLY_REVIEW.md

### Git local
- FounderOS entier dans un repo Git prive
- Commit a chaque fin de session avec le DAILY_LOG.md
- Push vers backup (GitHub prive ou cloud)

### Backups
- STATE/SNAPSHOTS/ a chaque shutdown
- Backup hebdomadaire du dossier FounderOS
- Minimum: local + cloud

### Monitoring (manuel pour l'instant)
- Chaque boot: verifier l'integrite des dossiers
- Detecter nouveaux projects dans PROJECTS/
- Verifier runway dans CURRENT_STATE.md
