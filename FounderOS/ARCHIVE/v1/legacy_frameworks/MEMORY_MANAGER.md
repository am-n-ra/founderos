# MEMORY_MANAGER V1

## Purpose
Separate temporary operational context from permanent knowledge. Without this, FounderOS mixes "what's happening this week" with "what is always true."

## Distinction
- KNOWLEDGE: validated truths, lessons, patterns, playbooks (permanent)
- MEMORY: current focus, active decisions, session context, weekly priorities (temporary)
- STATE: current reality, cash, projects, mode (updated each session)

## Memory Structure
Stored in: MEMORY/

FILES:
- CURRENT_FOCUS.md — what we're working on right now (this week)
- ACTIVE_DECISIONS.md — choices made this session, pending decisions
- SESSION_LOG.md — what happened this session (raw timeline)
- WEEKLY_CONTEXT.md — goals for this week, blocking issues

## Rules
1. MEMORY is temporary — archive after project milestone or weekly review
2. MEMORY overrides KNOWLEDGE when in conflict (current reality beats past truth)
3. MEMORY is loaded at boot, summarized in brief, archived at shutdown
4. MEMORY/MEMORY_INDEX.md lists all active memory files

## Memory vs Knowledge Example
- Memoire: "Cette semaine on priorise Stop Nuisibles Video 2"
- Connaissance: "Les hooks problem-first performent mieux que feature-first"
- State: "Cash: 1,077 FCFA, SURVIVAL Day 2"

Les trois sont differents. Ne pas les melanger.
