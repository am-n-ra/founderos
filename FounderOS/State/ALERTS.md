# ALERTS

## Purpose

File bridge between background scripts (watchtower, timekeeper) and the LLM at session boot. Scripts write here, LLM reads here.

**Read at session start (BOOT). Cleared after reading.**

---

## Active Alerts

| Timestamp | Source | Severity | Message |
|-----------|--------|----------|---------|
| | | | |

---

## Rules

1. Scripts append alerts as they fire
2. LLM reads all alerts at BOOT, clears them after acknowledgment
3. Max 50 alerts - oldest auto-archived

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | Scripts -> LLM |
