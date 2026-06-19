# State Synchronization

## Purpose
FounderOS must always know the current truth. Never operate on stale state.

## State Categories
Mission State, Project State, Knowledge State, Learning State, Runtime State, Asset State, Market State.

## Synchronization Cycle
Detect Changes → Validate → Update State → Notify Dependencies → Log Changes.

## Conflict Rule
If two states disagree: generate STATE_CONFLICT_REPORT.md.

## State Snapshot
Generate STATE_SNAPSHOT.md daily.
