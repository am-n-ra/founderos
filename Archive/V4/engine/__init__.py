"""Founder Runtime Engine - optional automation layer.

This package provides code that automates FRE_SPEC contract execution.
It is NOT required - FounderHQ runs on markdown alone. These modules
accelerate local agent deployments.

Modules:
    bootstrap: Loads FRE_SPEC + SYSTEM_PROMPT for LLM injection
    state_manager: Reads/writes CURRENT_STATE, TIMELINE, PRIORITY_MATRIX
    gate_checker: Validates LLM responses against PRG contracts
    timeline_logger: Appends events to TIMELINE.md
    cadence_engine: Computes cadence context (week/month/quarter) and active frameworks per lifecycle phase
    watchtower: Scheduled script (6h) - checks WATCH_REGISTRY, runs websearch/webfetch
    timekeeper: Scheduled script (30min) - deadlines, SOS timer, toast notifications
    installer: First-run setup - creates .venv, .env, Task Scheduler tasks, .founderhq_installed
    sync: Gist push/pull/merge for state synchronization across devices
    snapshot: Portable markdown snapshot for token-less environments
"""
