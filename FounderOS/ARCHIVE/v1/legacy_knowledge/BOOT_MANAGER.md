# Boot Manager

## Purpose
FounderOS must start correctly every time.

## Boot Phases
1. Environment Discovery: machine, OS, tools, software, repos, project folders, integrations
2. State Discovery: load STATE files
3. Project Discovery: scan Projects/ — detect new, modified, archived, deleted
4. Knowledge Discovery: load lessons, patterns, playbooks, domain packs, Knowledge/
5. Mission Loading: current mission, objectives, active priorities, constraints
6. System Validation: verify required files exist, registries valid, dependencies valid, states valid
7. Runtime Activation: scheduler, event bus, monitors, watchlists

## Boot Failure
If critical system missing: STOP. Generate BOOT_FAILURE_REPORT.md.

## Boot Log
Generate BOOT_LOG.md with: timestamp, modules loaded, projects found, issues, warnings, recommendations.
