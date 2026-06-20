# Reboot System — Design Spec

> **WF-008:** Cold Reboot Protocol for applying OS updates mid-session

## Problem

FounderOS files (MEMORY.md, PROJECT.md, TIMELINE.md, ASSET.md, CURRENT_STATE.md) are modified during a session, but the LLM has the old versions loaded in context. There is no mechanism to re-read modified files and rebuild the world model without closing and reopening the session.

## Solution

A single workflow (WF-008) triggered by the user saying "reboot" or "applique". The workflow uses git to detect what changed, re-reads only modified files, detects deltas, rebuilds the world model, and reports what changed.

## Scope

Re-reads files that changed: MEMORY.md, PROJECT.md, TIMELINE.md, ASSET.md, CURRENT_STATE.md, WORKFLOW.md, PLAYBOOK.md, KNOWLEDGE.md. Does NOT re-read MISSION.md, SYSTEM.md, CONCEPT_REGISTRY.md, CONCEPT_BOUNDARIES.md, or protocol files (they change too rarely to justify mid-session reload).

## Detection Mechanism

Git-based (primary): `git log --oneline -5` for recent commits, `git diff HEAD~1 --name-only` for changed files.

Memory-based (fallback): If no git history exists, the LLM compares what it remembers against fresh file reads.

Git bootstrap: If git is not available, init local repo (`git init`) or prompt user to install git.

## WF-008 Steps

1. **Trigger detected** — User message contains "reboot" or "applique". Freeze current context. Announce: "Rebooting — applying OS updates."

2. **Git change scan** — Run `git log --oneline -5` then `git diff HEAD~1 --name-only`. If no commits: `git init` then fallback to full re-read.

3. **Identify changed files** — From git output, determine which concept files were modified since last commit. If git unavailable, assume all active concept files changed.

4. **Re-read modified files** — Read only the files identified in step 3. Do not re-read unchanged files.

5. **Detect deltas** — Compare new content against old (in-memory) content. Generate delta list:
   - `Δ MEMORY — Priorities changed: 'Monitor Variation #2' → 'Call soya suppliers'`
   - `Δ PROJECT — Added: DM-001, SS-001. FO-001 → Completed.`

6. **Rebuild world model** — Synthesize: what exists, what matters, what changed, what's blocked, what's emerging, what should happen next. Check for contradictions between old and new state.

7. **Verify consistency** — If deltas create contradictions (e.g., CURRENT_STATE says cash=2,000 but MEMORY says cash=1,118), flag them. File wins over session memory.

8. **Report awareness** — Output:
   - "Reboot complete. 3 files re-loaded."
   - Delta list
   - New world model summary
   - Recommended next action

## Git Bootstrap Rule

If `git` is not detected:
- `git init` in FounderHQ root
- First commit: `git add . && git commit -m "founderos: initial state"`
- Then proceed with normal reboot flow

If user prefers not to init git: fallback to full re-read of all concept files.

## Integration

WF-008 is added to WORKFLOW.md. Referenced from FOUNDEROS_PROTOCOL.md as a post-boot maintenance command.

Not part of mandatory boot sequence (WF-007 is for boot). WF-008 is on-demand, triggered by user.

## Error Handling

- **No git history:** Fallback to full re-read + offer git init
- **File modified but unreadable:** Flag as ERROR, use old in-memory version, report
- **Contradiction after reload:** Flag contradiction, file version wins, report discrepancy
- **Reboot during active workflow:** Complete current step first, defer reboot to next natural break

## Files Modified

- `FounderOS/concepts/WORKFLOW.md` — Add WF-008
- `FounderOS/Protocols/FOUNDEROS_PROTOCOL.md` — Add reboot reference in footer

## Future Considerations

- Hot reload of individual concepts (reboot MEMORY only) if WF-008 proves useful
- Cron-triggered reboot at session boundaries
- Auto-reboot on file save detection (requires runtime watcher)
