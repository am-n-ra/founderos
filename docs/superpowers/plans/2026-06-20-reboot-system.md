# Reboot System (WF-008) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Cold Reboot Protocol (WF-008) to FounderOS that lets the user apply OS updates mid-session by saying "reboot" or "applique".

**Architecture:** A single workflow in WORKFLOW.md that uses git diff to detect changed concept files, re-reads only modified files, generates a delta report, and rebuilds the world model. Falls back to full re-read if no git history exists. Git bootstrap (init) if git not available.

**Tech Stack:** No code — pure markdown documentation. Git for change detection.

---

### Task 1: Add WF-008 to WORKFLOW.md

**Files:**
- Modify: `FounderOS/concepts/WORKFLOW.md` (append before Footer section)

- [ ] **Step 1: Read current WORKFLOW.md Footer**

```bash
Get-Content -Path "FounderOS/concepts/WORKFLOW.md" -Tail 10
```
Expected: The Footer section starting with `## Footer` and ending with the file.

- [ ] **Step 2: Insert WF-008 section before Footer**

Insert this block before `## Footer` in `FounderOS/concepts/WORKFLOW.md`:

```markdown
---

**WORKFLOW_ID:** WF-008

**NAME:** Cold Reboot Protocol

**TRIGGER:** User says "reboot" or "applique" in any message

**INPUT:** Current session context (stale) + files on disk (fresh) + git history

**STEPS:**

1. **Freeze context** — Announce: "Rebooting — applying OS updates." Note current action to resume later if needed.

2. **Git change scan** — Run:
   ```
   git log --oneline -5
   git diff HEAD~1 --name-only
   ```
   If `git` not found: `git init` in FounderHQ root, then `git add . && git commit -m "founderos: initial state"`, then proceed to step 4 (full re-read).

3. **Identify changed files** — Parse `git diff HEAD~1 --name-only` output. Match against known concept files: `concepts/MEMORY.md`, `concepts/PROJECT.md`, `concepts/TIMELINE.md`, `concepts/ASSET.md`, `State/CURRENT_STATE.md`, `concepts/WORKFLOW.md`, `concepts/PLAYBOOK.md`, `concepts/KNOWLEDGE.md`.

4. **Re-read modified files** — Read each file identified in step 3. If no git history (first commit just made or fallback), re-read all active concept files from step 3's list.

5. **Detect deltas** — Compare new content against remembered old content. For each file, list what changed:
   ```
   Δ MEMORY — Priorities changed: old → new
   Δ PROJECT — Added: DM-001. FO-001 → Completed.
   ```

6. **Rebuild world model** — Synthesize: what exists, what matters, what changed, what's blocked, what's emerging, what should happen next. If deltas contradict each other (e.g., two files disagree on cash), flag the contradiction.

7. **Verify consistency** — File version wins over session memory. If a contradiction is found, report: "⚠️ Contradiction detected: MEMORY says X, CURRENT_STATE says Y. Using CURRENT_STATE (file wins)."

8. **Report awareness** — Output:
   ```
   Reboot complete. 3 files re-loaded.

   Δ MEMORY — priorities updated
   Δ PROJECT — DM-001 added, FO-001 completed
   Δ ASSET — A-009, A-010, A-011 added

   World model: SURVIVAL mode. Cash 1,118 FCFA. Top priority: call soya suppliers. No contradictions.

   Recommended next action: Call Ste SODJA (96 68 43 65) to confirm price and delivery terms.
   ```

**OUTPUT:** Fresh world model applied to session. Delta report displayed.

**ERROR HANDLING:**
- `git` not found → `git init`, first commit, full re-read. If user declines git init, use full re-read without git.
- File modified but unreadable → Use old in-memory version, flag as ERROR.
- Contradiction between old and new state → File version wins, flag contradiction.
- Reboot during active workflow → Complete current step first, defer reboot to next natural break.

**RELATED_KNOWLEDGE:** KNOWLEDGE — FounderOS Design Principles, TEMPORAL_AWARENESS.md
```

- [ ] **Step 3: Update Footer date**

Replace the Footer's `Last updated` line to include WF-008:
```
Last updated: 2026-06-20 (added: WF-007 Session Boot Freshness Check, WF-008 Cold Reboot Protocol)
```

- [ ] **Step 4: Verify the addition**

```bash
Get-Content -Path "FounderOS/concepts/WORKFLOW.md" -Tail 5
```
Expected: Footer with updated date. WF-008 section appears before it.

---

### Task 2: Add reboot reference to FOUNDEROS_PROTOCOL.md

**Files:**
- Modify: `FounderOS/Protocols/FOUNDEROS_PROTOCOL.md` (footer section)

- [ ] **Step 1: Read current Footer**

```bash
Get-Content -Path "FounderOS/Protocols/FOUNDEROS_PROTOCOL.md" -Tail 10
```
Expected: Footer section near the end.

- [ ] **Step 2: Add reboot reference**

Add this note before or in the Footer section:

```markdown
### Mid-Session Reboot

If the user says "reboot" or "applique" during a session, execute WF-008 (Cold Reboot Protocol) from WORKFLOW.md. This re-reads modified concept files, detects deltas, and rebuilds the world model without closing the session.
```

Insert this after the "Execution Mode" section, before the "Interaction Style" section.

---

### Task 3: Initialize git in FounderHQ (if not already)

**Files:**
- No file changes — shell commands

- [ ] **Step 1: Check git status**

```bash
git -C "C:\Users\junio\Desktop\FounderHQ" status
```

- [ ] **Step 2: If not a git repo, init**

```bash
git -C "C:\Users\junio\Desktop\FounderHQ" init
git -C "C:\Users\junio\Desktop\FounderHQ" add -A
git -C "C:\Users\junio\Desktop\FounderHQ" commit -m "founderos: pre-reboot state"
```

Expected: Initial commit created. All files tracked.

---

### Task 4: Verify the system works

- [ ] **Step 1: Test the trigger**

Simulate: modify a file (e.g., add a note to MEMORY.md). Then check that the reboot workflow steps 1-8 can be followed logically. No automated test possible since this is a manual LLM workflow.

- [ ] **Step 2: Test fallback**

Delete `.git` folder (backup first), run `git init` simulation. Verify that git bootstrap creates initial commit.

- [ ] **Step 3: Commit implementation**

```bash
git -C "C:\Users\junio\Desktop\FounderHQ" add docs/superpowers/specs/2026-06-20-reboot-system-design.md docs/superpowers/plans/2026-06-20-reboot-system.md FounderOS/concepts/WORKFLOW.md FounderOS/Protocols/FOUNDEROS_PROTOCOL.md
git -C "C:\Users\junio\Desktop\FounderHQ" commit -m "feat: add WF-008 cold reboot protocol"
```
