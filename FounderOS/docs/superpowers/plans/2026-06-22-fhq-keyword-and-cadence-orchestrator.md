# `fhq` Keyword & Cadence Orchestrator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the implicit "always-boot" pattern with explicit keyword triggers (`fhq`, `boot`, `shutdown`) so the user controls when the full kernel cycle runs, and integrate cadence/lifecycle awareness into the ORIENT phase.

**Architecture:** Three user-facing keywords (`fhq`, `boot`, `shutdown`) control kernel execution depth. `fhq` at message start triggers the full BOOT->OBSERVE->ORIENT->DECIDE->ACT->LEARN->UPDATE cycle (BOOT skipped if already active today). `boot` explicitly restarts the day. `shutdown` ends the session with time tracking. No keyword -> DIRECT mode (response only, no cycle). Background scripts (watchtower, timekeeper) run independently via Windows Task Scheduler. Cadence (life->year->month->week->day->hour) and lifecycle (phase per project) enrich the ORIENT phase through new state files.

**Tech Stack:** Python 3.13, markdown state files, Windows Task Scheduler, BurntToast (optional)

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `FounderOS/SYSTEM_PROMPT.md` | MODIFY | Add `fhq`/`boot`/`shutdown` keyword detection to Intent Classification; add Cadence+Lifecycle to Boot Sequence |
| `FounderOS/Runtime/RUNTIME_KERNEL.md` | MODIFY | Enrich ORIENT phase with CADENCE x LIFECYCLE x frameworks cross; add conditional BOOT (skip if day already active) |
| `FounderOS/Protocols/SOURCE_OF_TRUTH.md` | MODIFY | Register CADENCE.md, LIFECYCLE.md, ALERTS.md, WATCH_REPORT.md |
| `FounderOS/Runtime/engine/__init__.py` | MODIFY | Document new cadence_engine module |
| `FounderOS/State/CADENCE.md` | CREATE | Temporal hierarchy: life->year->month->week->day->hour with current values |
| `FounderOS/State/LIFECYCLE.md` | CREATE | Phase of each project (IDEA, VALIDATION, LAUNCH, GROWTH, SCALE, MATURE) with gates |
| `FounderOS/State/ALERTS.md` | CREATE | Notifications stored by background scripts, read at boot |
| `FounderOS/State/WATCH_REPORT.md` | CREATE | Watch results formatted for LLM consumption, bridge between scripts and session |
| `FounderOS/Runtime/engine/cadence_engine.py` | CREATE | Python module: compute current cadence from datetime, determine active lifecycle phases, suggest which frameworks to load |
| `FounderOS/Runtime/engine/watchtower.py` | CREATE | Background script: scheduled every 6h, reads WATCH_REGISTRY, runs websearch/webfetch, updates registry + writes WATCH_REPORT.md |
| `FounderOS/Runtime/engine/timekeeper.py` | CREATE | Background script: every 30min, checks deadlines, SOS timer (pause reminder every 90min), sends Windows toast notifications |
| `FounderOS/Runtime/engine/installer.py` | CREATE | First-run setup: create Windows Task Scheduler tasks for watchtower and timekeeper, verify BurntToast availability |
| `FounderOS/tests/test_cadence_engine.py` | CREATE | Tests for cadence_engine.py |

---

### Task 1: Create `State/CADENCE.md`

**Files:**
- Create: `FounderOS/State/CADENCE.md`

- [ ] **Create CADENCE.md**

```markdown
# CADENCE

## Purpose

Hierarchy temporelle de FounderOS : vie -> annee -> mois -> semaine -> jour -> heure. Chaque niveau porte un objectif, une evaluation, et un lien vers le niveau suivant.

Lue en phase BOOT pour contextualiser ORIENT. Mise a jour par le LLM quand les objectifs evoluent.

---

## Life (Vie)

> **Objectif:** [objectif de vie]

**Evaluation:** [auto-evaluation: 0-10]

---

## Year (Annee) - 2026

> **Objectif:** [objectif 2026]

**Evaluation:** [auto-evaluation 0-10]

**Trimestre en cours:** Q2 (Avril-Juin)

---

## Month (Mois) - Juin 2026

> **Objectif:** [objectif juin]

**Evaluation:** [auto-evaluation 0-10]

**Semaines:**
- S24 (Juin 9-15): [objectif / resultat]
- S25 (Juin 16-22): [objectif / resultat]
- S26 (Juin 23-29): [objectif / resultat]
- S27 (Juin 30-Juil 6): [objectif / resultat]

---

## Week (Semaine) - S26 (Juin 23-29)

> **Objectif:** [objectif semaine]

**Deadlines cette semaine:**
- [date] - [description]

---

## Day (Jour) - 2026-06-22

> **Objectif:** [objectif du jour]

**Session start:** [HH:MM - filled at boot]
**Session end:** [HH:MM - filled at shutdown]
**Duration:** [calculated]

**Top 3 actions:**
1. [action]
2. [action]
3. [action]

---

## Hour (Heure) - Now

> **Lome (UTC+0):** [dynamique - computed at every `fhq`]

**Next actionable:** [what to do in the next 60 min]

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Temporal hierarchy for FounderOS cadence |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/CADENCE.md
git commit -m "feat: create CADENCE.md with temporal hierarchy (life->year->month->week->day->hour)"
```

---

### Task 2: Create `State/LIFECYCLE.md`

**Files:**
- Create: `FounderOS/State/LIFECYCLE.md`

- [ ] **Create LIFECYCLE.md**

```markdown
# LIFECYCLE

## Purpose

Phase actuelle de chaque projet actif. Determine quel framework activer en phase ORIENT. Chaque phase a des gates de sortie - conditions precises pour passer a la phase suivante.

Mise a jour par le LLM quand un projet franchit un gate.

---

## Phases

| Phase | Description | Gate de Sortie | Frameworks Actifs |
|-------|-------------|----------------|-------------------|
| IDEA | Idee non validee | Prototype ou enquete client faite | CAOS |
| VALIDATION | Solution testee, client cherche | 3+ clients prets a payer | VAOS, DIOS |
| LAUNCH | Premier client, livraison manuelle | Process reproductible | DIOS, CEOS |
| GROWTH | Revenu regulier, equipe building | Process automatises/outsources | PSOS, FAOS, SAOS |
| SCALE | Croissance acceleree, fundraising | Metriques unitaires saines | FAOS, SAOS |
| MATURE | Cash-flow stable, optimisation | - | SAOS |

---

## Projets Actifs

| Projet | Phase | Depuis | Gate de Sortie Atteint ? | Prochaine Action |
|--------|-------|--------|--------------------------|-----------------|
| SOJACO | VALIDATION | 2026-06-21 | Non - Pas encore de client payant | Trouver client mais ou soja |
| OMNI | LAUNCH | 2026-06-15 | Non - MVP deploye, 0 client payant | Pitch Day + acquisition premiers utilisateurs |
| SOYA (Bolsoja) | LAUNCH | 2026-05-XX | Non - 1 client (dame 1), pas encore reproductible | Livraison quotidienne + trouver d'autres clients |
| KORA | VALIDATION | 2026-06-01 | Non - Pre-seed docs ok, pas de financement | Relancer ST Digital + Herlog |
| DOODLEMIND | IDEA | 2026-06-10 | Non - Short #1 publie, 0 monetization | Produire Short #2 |
| PEST REPELLER | IDEA | 2026-05-XX | Non - Stock disponible, 0 vente | Creer contenu TikTok |
| SOLAR KIT | IDEA | 2026-06-15 | Non - Pas encore de prototype | Definir modele + fournisseur |

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | System |
| Purpose | Project lifecycle phase tracking for framework selection |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/LIFECYCLE.md
git commit -m "feat: create LIFECYCLE.md with per-project phase tracking and gate conditions"
```

---

### Task 3: Create `State/ALERTS.md` and `State/WATCH_REPORT.md`

**Files:**
- Create: `FounderOS/State/ALERTS.md`
- Create: `FounderOS/State/WATCH_REPORT.md`

- [ ] **Create ALERTS.md**

```markdown
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
```

- [ ] **Create WATCH_REPORT.md**

```markdown
# WATCH REPORT

## Purpose

Formatted findings from watchtower.py runs. One section per watch that triggered. Read by LLM at BOOT.

---

## Reports

<!-- watchtower appends here at each run -->

---

## Footer

| Field | Value |
|-------|-------|
| OS Version | V4 |
| Created | 2026-06-22 |
| Owner | watchtower.py |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/State/ALERTS.md FounderOS/State/WATCH_REPORT.md
git commit -m "feat: create ALERTS.md and WATCH_REPORT.md as script-to-LLM bridge files"
```

---

### Task 4: Create and test `Runtime/engine/cadence_engine.py`

**Files:**
- Create: `FounderOS/Runtime/engine/cadence_engine.py`
- Create: `FounderOS/tests/test_cadence_engine.py`

- [ ] **Write the failing tests**

Create `FounderOS/tests/test_cadence_engine.py`:

```python
import pytest
from datetime import datetime
from Runtime.engine.cadence_engine import get_week_of_month, get_cadence_context, get_active_frameworks


class TestGetWeekOfMonth:
    def test_first_week(self):
        d = datetime(2026, 6, 1, 12, 0)
        assert get_week_of_month(d) == 1

    def test_third_week(self):
        d = datetime(2026, 6, 15, 12, 0)
        assert get_week_of_month(d) == 3

    def test_last_week_june(self):
        d = datetime(2026, 6, 29, 12, 0)
        assert get_week_of_month(d) == 5


class TestGetCadenceContext:
    def test_returns_all_levels(self):
        d = datetime(2026, 6, 22, 14, 30)
        ctx = get_cadence_context(d)
        assert ctx["year"] == 2026
        assert ctx["month"] == 6
        assert ctx["day"] == 22
        assert ctx["hour"] == 14
        assert ctx["minute"] == 30
        assert ctx["week_of_month"] == 4
        assert ctx["day_of_week"] == 1

    def test_contains_iso_week(self):
        d = datetime(2026, 6, 22, 12, 0)
        ctx = get_cadence_context(d)
        assert "iso_week" in ctx
        assert 1 <= ctx["iso_week"] <= 53


class TestGetActiveFrameworks:
    def test_validation_phase_returns_vaos_dios(self):
        ctx = {"lifecycle_phase": "VALIDATION"}
        frameworks = get_active_frameworks(ctx)
        assert "VAOS" in frameworks
        assert "DIOS" in frameworks

    def test_idea_phase_returns_caos(self):
        ctx = {"lifecycle_phase": "IDEA"}
        frameworks = get_active_frameworks(ctx)
        assert "CAOS" in frameworks
        assert "VAOS" not in frameworks

    def test_survival_mode_prioritizes_revenue_frameworks(self):
        ctx = {"lifecycle_phase": "VALIDATION", "mode": "SURVIVAL"}
        frameworks = get_active_frameworks(ctx)
        assert "DIOS" in frameworks
        assert "DAOS" in frameworks
```

- [ ] **Run test to verify it fails**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_cadence_engine.py -v
```

Expected: 6 FAILED with "ModuleNotFoundError: No module named 'Runtime.engine.cadence_engine'"

- [ ] **Write minimal implementation**

Create `FounderOS/Runtime/engine/cadence_engine.py`:

```python
"""Compute cadence context and active frameworks from datetime + lifecycle state.

Usage:
    from engine.cadence_engine import get_cadence_context, get_active_frameworks
    ctx = get_cadence_context(datetime.now())
    frameworks = get_active_frameworks(ctx)
"""

from datetime import datetime


def get_week_of_month(dt: datetime) -> int:
    """Return which week of the month this date falls in (1-based)."""
    first_day = dt.replace(day=1)
    days_from_monday = first_day.weekday()
    first_monday = first_day.replace(day=1 - days_from_monday)
    delta = dt - first_monday
    return (delta.days // 7) + 1


def get_cadence_context(dt: datetime) -> dict:
    """Return dict with all cadence levels for the given datetime."""
    return {
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "hour": dt.hour,
        "minute": dt.minute,
        "week_of_month": get_week_of_month(dt),
        "iso_week": dt.isocalendar()[1],
        "day_of_week": dt.weekday(),
        "day_name": dt.strftime("%A"),
        "month_name": dt.strftime("%B"),
        "quarter": (dt.month - 1) // 3 + 1,
    }


FRAMEWORKS_BY_PHASE = {
    "IDEA": ["CAOS"],
    "VALIDATION": ["VAOS", "DIOS"],
    "LAUNCH": ["DIOS", "CEOS"],
    "GROWTH": ["PSOS", "FAOS", "SAOS"],
    "SCALE": ["FAOS", "SAOS"],
    "MATURE": ["SAOS"],
}

SURVIVAL_FRAMEWORKS = ["DAOS", "DIOS"]


def get_active_frameworks(ctx: dict) -> list[str]:
    """Return list of frameworks to load based on lifecycle phase and mode.

    Args:
        ctx: Context dict with at minimum 'lifecycle_phase' and optionally 'mode'.

    Returns:
        List of framework short names to load (e.g. ['VAOS', 'DIOS']).
    """
    phase = ctx.get("lifecycle_phase", "IDEA")
    mode = ctx.get("mode", "GROWTH")

    frameworks = list(FRAMEWORKS_BY_PHASE.get(phase, ["CAOS"]))

    if mode == "SURVIVAL":
        for fw in SURVIVAL_FRAMEWORKS:
            if fw not in frameworks:
                frameworks.append(fw)

    return frameworks
```

- [ ] **Run tests to verify they pass**

Run:
```cmd
cd C:\Users\junio\Desktop\FounderHQ
python -m pytest FounderOS/tests/test_cadence_engine.py -v
```

Expected: 6 PASSED

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/cadence_engine.py FounderOS/tests/test_cadence_engine.py
git commit -m "feat: add cadence_engine.py with week/month computation and framework selection per lifecycle phase"
```

---

### Task 5: Create `Runtime/engine/watchtower.py`

**Files:**
- Create: `FounderOS/Runtime/engine/watchtower.py`

- [ ] **Write watchtower.py**

```python
"""watchtower.py - Scheduled veille script. Run every 6h via Windows Task Scheduler.

Reads State/WATCH_REGISTRY.md, checks items where Next Check <= today,
executes websearch/webfetch, updates registry Last Result, appends to WATCH_REPORT.md.

Usage:
    python Runtime/engine/watchtower.py --base-dir /path/to/FounderHQ
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Optional


def parse_watch_registry(path: Path) -> list[dict]:
    """Parse WATCH_REGISTRY.md table and return list of watch items due for check.

    Returns items where Next Check <= today.
    """
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    items = []
    in_table = False
    headers = []

    for line in lines:
        if line.startswith("| Watch Item |"):
            in_table = True
            headers = [h.strip() for h in line.strip("|").split("|")]
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            in_table = False
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 7:
            continue

        item = dict(zip(headers, cols))
        next_check_str = item.get("Next Check", "")
        if not next_check_str or next_check_str == "-":
            continue

        try:
            next_check = datetime.strptime(next_check_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        if next_check <= date.today():
            items.append(item)

    return items


def execute_watch(item: dict, base_dir: str) -> str:
    """Execute a single watch item. Returns result string."""
    source_method = item.get("Source / Method", "")
    watch_item = item.get("Watch Item", "")

    if source_method.startswith("websearch"):
        query = source_method.replace("websearch ", "", 1)
        result = f"[websearch] {query} - manual check required (no API key configured)"
    elif source_method.startswith("webfetch"):
        url = source_method.replace("webfetch ", "", 1)
        result = f"[webfetch] {url} - manual check required"
    else:
        result = f"[manual] {watch_item} - no automated check method"

    return result


def update_registry(path: Path, item: dict, result: str) -> None:
    """Update WATCH_REGISTRY.md with new Last Checked, Last Result, and Next Check."""
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    watch_item = item.get("Watch Item", "")
    today_str = date.today().strftime("%Y-%m-%d")

    freq = item.get("Frequency", "Weekly")
    freq_days = {"Daily": 1, "Weekly": 7, "Monthly": 30}
    next_check_days = freq_days.get(freq, 7)
    next_check_date = date.today() + timedelta(days=next_check_days)
    next_check_str = next_check_date.strftime("%Y-%m-%d")

    safe_result = result.replace("|", "/")

    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if watch_item in line and line.startswith("|"):
            cols = line.split("|")
            if len(cols) >= 7:
                cols[5] = f" {next_check_str} "
                cols[6] = f" {safe_result} "
                cols[4] = f" {today_str} "
                line = "|".join(cols)
        new_lines.append(line)

    path.write_text("\n".join(new_lines), encoding="utf-8")


def append_watch_report(base_path: Path, item: dict, result: str) -> None:
    """Append watch result to WATCH_REPORT.md."""
    report_path = base_path / "State" / "WATCH_REPORT.md"
    if not report_path.exists():
        report_path.write_text("# WATCH REPORT\n\n## Reports\n\n", encoding="utf-8")

    today_str = date.today().strftime("%Y-%m-%d %H:%M UTC+0")
    entry = (
        f"### {item.get('Watch Item', 'Unknown')} - {today_str}\n\n"
        f"**Project:** {item.get('Project', 'N/A')}\n\n"
        f"**Method:** {item.get('Source / Method', 'N/A')}\n\n"
        f"**Result:** {result}\n\n---\n\n"
    )

    with open(report_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Watchtower - veille script for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    args = parser.parse_args()

    base_path = Path(args.base_dir)
    registry_path = base_path / "State" / "WATCH_REGISTRY.md"

    if not registry_path.exists():
        print(f"WATCH_REGISTRY.md not found at {registry_path}")
        sys.exit(0)

    due_items = parse_watch_registry(registry_path)
    if not due_items:
        print("No watch items due for check today.")
        sys.exit(0)

    for item in due_items:
        print(f"Checking: {item.get('Watch Item', 'Unknown')}")
        result = execute_watch(item, args.base_dir)
        update_registry(registry_path, item, result)
        append_watch_report(base_path, item, result)
        print(f"  Result: {result[:80]}...")

    print(f"Checked {len(due_items)} watch items.")


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/watchtower.py
git commit -m "feat: create watchtower.py - scheduled veille script (6h) for WATCH_REGISTRY checks"
```

---

### Task 6: Create `Runtime/engine/timekeeper.py`

**Files:**
- Create: `FounderOS/Runtime/engine/timekeeper.py`

- [ ] **Write timekeeper.py**

```python
"""timekeeper.py - Scheduled time and alert script. Run every 30min via Windows Task Scheduler.

Checks:
1. Deadlines in PRIORITY_MATRIX.md - alerts for any deadline <= 48h
2. SOS timer - if no session start found in CURRENT_STATE.md or session > 90min, send pause reminder
3. ALERTS.md - appends any triggered alerts

Usage:
    python Runtime/engine/timekeeper.py --base-dir /path/to/FounderHQ
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


def send_toast(title: str, message: str) -> bool:
    """Send Windows toast notification using BurntToast PowerShell module.

    Returns True if sent, False if BurntToast not available.
    """
    ps_script = (
        f'New-BurntToastNotification -Text "{title}", "{message}"'
    )
    try:
        result = subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=15,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def parse_deadlines(base_path: Path) -> list[dict]:
    """Parse PRIORITY_MATRIX.md for rows with deadlines within 48h."""
    matrix_path = base_path / "State" / "PRIORITY_MATRIX.md"
    if not matrix_path.exists():
        return []

    text = matrix_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    deadlines = []
    in_table = False

    for line in lines:
        if line.startswith("| Projet |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            in_table = False
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 6:
            continue

        project = cols[0]
        deadline_str = cols[4]
        if not deadline_str or deadline_str == "-":
            continue

        deadline = None
        if deadline_str.lower() == "today":
            deadline = datetime.now().date()
        elif deadline_str.lower() == "tomorrow":
            deadline = datetime.now().date() + timedelta(days=1)
        else:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            except ValueError:
                continue

        if deadline is not None:
            days_until = (deadline - datetime.now().date()).days
            if 0 <= days_until <= 2:
                deadlines.append({
                    "project": project,
                    "deadline": deadline_str,
                    "days_until": days_until,
                    "action": cols[2],
                })

    return deadlines


def check_sos_timer(base_path: Path) -> Optional[str]:
    """Check SOS timer. If session > 90min, return alert message."""
    current_state_path = base_path / "State" / "CADENCE.md"
    if not current_state_path.exists():
        return None

    text = current_state_path.read_text(encoding="utf-8")
    match = re.search(r"\*\*Session start:\*\*\s*([\d:]+)", text, re.IGNORECASE)
    if not match:
        return None

    session_start_str = match.group(1)
    try:
        now = datetime.now()
        session_start = datetime.strptime(session_start_str, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
    except ValueError:
        return None

    elapsed_minutes = (now - session_start).total_seconds() / 60
    if elapsed_minutes > 90:
        return f"Session active depuis {elapsed_minutes:.0f} min. Pause recommandee (SOS)."

    return None


def append_alert(base_path: Path, severity: str, message: str) -> None:
    """Append alert to ALERTS.md."""
    alerts_path = base_path / "State" / "ALERTS.md"
    if not alerts_path.exists():
        alerts_path.write_text(
            "# ALERTS\n\n## Active Alerts\n\n"
            "| Timestamp | Source | Severity | Message |\n"
            "|-----------|--------|----------|---------|\n",
            encoding="utf-8",
        )

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M UTC+0")
    entry = f"| {now_str} | timekeeper | {severity} | {message} |\n"

    with open(alerts_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    parser = argparse.ArgumentParser(description="Timekeeper - time and alert script for FounderHQ")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--no-toast", action="store_true", help="Skip toast notifications")
    args = parser.parse_args()

    base_path = Path(args.base_dir)

    deadlines = parse_deadlines(base_path)
    for d in deadlines:
        msg = f"{d['project']}: deadline {d['deadline']} dans {d['days_until']} jour(s)"
        print(f"[ALERT] {msg}")
        append_alert(base_path, "HIGH", msg)
        if not args.no_toast:
            sent = send_toast("FounderHQ Deadline", f"{d['project']} - {d['deadline']}")
            if sent:
                print("  Toast sent.")

    sos_msg = check_sos_timer(base_path)
    if sos_msg:
        print(f"[SOS] {sos_msg}")
        append_alert(base_path, "MEDIUM", sos_msg)
        if not args.no_toast:
            sent = send_toast("FounderHQ SOS", "Pause recommandee - session > 90 min")
            if sent:
                print("  Toast sent.")

    print("Timekeeper run complete.")


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/timekeeper.py
git commit -m "feat: create timekeeper.py - scheduled time/alert script (30min) with deadline checks and SOS timer"
```

---

### Task 7: Create `Runtime/engine/installer.py`

**Files:**
- Create: `FounderOS/Runtime/engine/installer.py`

- [ ] **Write installer.py**

```python
"""installer.py - First-run setup for FounderHQ background scripts.

Creates Windows Task Scheduler tasks for:
1. watchtower - runs every 6 hours
2. timekeeper - runs every 30 minutes

Usage:
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ
    python Runtime/engine/installer.py --base-dir /path/to/FounderHQ --uninstall
"""

import argparse
import subprocess
import sys
from pathlib import Path


def task_exists(task_name: str) -> bool:
    """Check if a Windows Scheduled Task exists."""
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", task_name],
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.returncode == 0


def create_task(task_name: str, script_path: str, base_dir: str, interval_minutes: int) -> bool:
    """Create a Windows Scheduled Task."""
    python_exe = sys.executable
    if not python_exe:
        python_exe = "python"

    cmd = [
        "schtasks", "/Create", "/SC", "MINUTE",
        "/MO", str(interval_minutes),
        "/TN", task_name,
        "/TR", f'"{python_exe}" "{script_path}" --base-dir "{base_dir}"',
        "/F",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode != 0:
        print(f"ERROR creating task {task_name}: {result.stderr.strip()}")
        return False

    print(f"Task '{task_name}' created (every {interval_minutes} min).")
    return True


def remove_task(task_name: str) -> bool:
    """Remove a Windows Scheduled Task."""
    if not task_exists(task_name):
        print(f"Task '{task_name}' does not exist, skipping.")
        return True

    cmd = ["schtasks", "/Delete", "/TN", task_name, "/F"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        print(f"ERROR removing task {task_name}: {result.stderr.strip()}")
        return False

    print(f"Task '{task_name}' removed.")
    return True


def check_burnt_toast() -> bool:
    """Check if BurntToast PowerShell module is available."""
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Get-Module -ListAvailable -Name BurntToast",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    available = "BurntToast" in result.stdout
    if available:
        print("BurntToast: available")
    else:
        print("BurntToast: NOT available - toast notifications disabled")
    return available


def install_burnt_toast() -> bool:
    """Install BurntToast PowerShell module."""
    cmd = [
        "powershell.exe", "-NoProfile", "-Command",
        "Install-Module -Name BurntToast -Force -Scope CurrentUser",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"BurntToast install failed: {result.stderr.strip()}")
        return False
    print("BurntToast installed.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Installer for FounderHQ background scripts")
    parser.add_argument("--base-dir", default=".", help="FounderHQ root directory")
    parser.add_argument("--uninstall", action="store_true", help="Remove all scheduled tasks")
    parser.add_argument("--install-burnttoast", action="store_true", help="Install BurntToast PowerShell module")
    args = parser.parse_args()

    base_path = Path(args.base_dir).resolve()
    scripts_dir = base_path / "Runtime" / "engine"

    if args.uninstall:
        remove_task("FounderHQ-Watchtower")
        remove_task("FounderHQ-Timekeeper")
        print("Uninstall complete.")
        return

    if args.install_burnttoast:
        install_burnt_toast()
        return

    check_burnt_toast()

    watchtower_path = scripts_dir / "watchtower.py"
    if not watchtower_path.exists():
        print(f"ERROR: {watchtower_path} not found")
        sys.exit(1)

    create_task("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)

    timekeeper_path = scripts_dir / "timekeeper.py"
    if not timekeeper_path.exists():
        print(f"ERROR: {timekeeper_path} not found")
        sys.exit(1)

    create_task("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)

    print("\nInstallation complete.")
    print("  FounderHQ-Watchtower: runs every 6 hours (veille)")
    print("  FounderHQ-Timekeeper: runs every 30 minutes (deadlines + SOS)")


if __name__ == "__main__":
    main()
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/installer.py
git commit -m "feat: create installer.py - Windows Task Scheduler setup for watchtower + timekeeper"
```

---

### Task 8: Modify `Runtime/engine/__init__.py`

**Files:**
- Modify: `FounderOS/Runtime/engine/__init__.py`

- [ ] **Read current file**

```cmd
type FounderOS\Runtime\engine\__init__.py
```

- [ ] **Replace with updated version**

```python
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
    installer: First-run setup - creates Windows Task Scheduler tasks
"""
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/engine/__init__.py
git commit -m "docs: document cadence_engine, watchtower, timekeeper, installer in __init__.py"
```

---

### Task 9: Modify `SYSTEM_PROMPT.md` - Add `fhq` / `boot` / `shutdown` Keywords

**Files:**
- Modify: `FounderOS/SYSTEM_PROMPT.md`

- [ ] **Read current file**

```cmd
type FounderOS\SYSTEM_PROMPT.md
```

- [ ] **Replace Intent Classification section**

Replace the Intent Classification table (between `## Intent Classification` and `## Pre-Response Gate (PRG)`) with:

```
## Intent Classification

Before responding, classify intent using this table. Then execute PRG. Never reply before both steps complete.

| Pattern | Classify as | Action |
|---|---|---|
| Message starts with **"boot"** or **"boot "** | BOOT | Full session initialization. Set session start time in CADENCE.md. Load ALL state files + frameworks. Execute ORIENT enriched with CADENCE + LIFECYCLE. |
| Message starts with **"shutdown"** or **"shutdown "** | SHUTDOWN | End session. Log session duration to CADENCE.md (Day -> Session End). Save ALL state. Record TIMELINE entry. Do NOT continue after shutdown. |
| Message starts with **"fhq"** or **"fhq "** | FHQ_MODE | Full kernel cycle: BOOT (if first `fhq` today) -> OBSERVE -> ORIENT (enriched with CADENCE x LIFECYCLE x frameworks) -> DECIDE -> ACT -> LEARN -> UPDATE. Execute Get-Date automatically. Apply PRG. Track time since last `fhq` in session. |
| Strategy, vision, long-term | STRATEGIC | Load VEAOS.md. If venture creation/restructuring/BP -> also load Frameworks/VSOS.md |
| Daily execution, task planning | EXECUTION | Load DAOS.md |
| Content creation, video, script | CONTENT | Load CEOS.md + AI_VIDEO_MASTER_DOMAIN.md |
| Reflection, stuck, uncertainty | REFLECTION | Load ASTRA.md |
| Research, investigate | RESEARCH | Load RIOS.md |
| Learning, skill, knowledge gap | LEARNING | Load LEOS.md |
| Fundraising, revenue, partnerships | FUNDRAISING | Load FAOS.md |
| Health, energy, burnout | SELF | Load SOS.md |
| Architecture, organization | ARCHITECTURE | Load AOS.md |
| Decision, tradeoffs | DECISION | Load DECISION_ENGINE.md |
| Pattern, recurring | PATTERN | Load PATTERN_ENGINE.md |
| Playbook, process documentation | PLAYBOOK | Load PLAYBOOK_ENGINE.md |
| Mission, priorities | MISSION | Load MOS.md |
| Distribution, campaign, audience | DISTRIBUTION | Load Frameworks/Specialized/Distribution/DIOS.md |
| Venture creation, business plan, project structure | VENTURE | Load Frameworks/Specialized/Venture/VAOS.md |
| Simple update, ambiguous, no keyword | DIRECT | SURVIVAL -> load DAOS.md, propose 1 action module. Otherwise -> respond directly |
```

- [ ] **Replace Boot Sequence section**

Replace the Boot Sequence section (from "## Boot Sequence" to the next ## header) with:

```
## Boot Sequence

Execute at session start (triggered by `boot` or first `fhq` of the day):
1. **Load Protocols + FRE** - SOURCE_OF_TRUTH.md + DECISION_GATES.md + INFO_CAPTURE_PROTOCOL.md + Runtime/FRE_SPEC.md
2. **Temporal Context** - Get-Date, compute Lome UTC+0. Load TIMELINE.md, CURRENT_STATE.md, CADENCE.md
3. **Load Cadence + Lifecycle** - Load State/CADENCE.md, State/LIFECYCLE.md. Determine current temporal position and project phases.
4. **Load Priority Matrix** - Load State/PRIORITY_MATRIX.md to establish unified view of ALL active projects/actions
5. **Load Alerts + Watch Reports** - Load State/ALERTS.md, read and clear active alerts. Load State/WATCH_REPORT.md for any background script findings since last session.
6. **Execute Watch Registry** - Load State/WATCH_REGISTRY.md, check each item where Next Check <= today, run websearch/webfetch, report findings, update registry
7. **Freshness Check** - Scan all concept footers. Flag any > 48h (WF-007)
8. **Set Session Start** - Record current time as Session Start in CADENCE.md (Day section). Log to TIMELINE.
9. **Load Concepts** - In order: CURRENT_STATE -> MISSION -> MEMORY -> KNOWLEDGE -> TIMELINE -> PROJECT -> WORKFLOW -> ASSET -> PLAYBOOK -> SYSTEM
10. **Build World Model** - Synthesize: what exists, what matters, what changed, what is blocked, what should happen next
11. **Report Awareness** - State: datetime, mode, top priority, cadence (week/month), lifecycle phases, watch results, what changed, stale concepts, PRG status. MUST state next action.
12. **Integrity Check** - All critical files loaded? Temporal context established? No contradictions?
13. **Daily Kickoff** - Execute RUNTIME Phase 1-2 (Assess cash/state -> Decide top action). State today's single most important action.
```

- [ ] **Update PRG Step 1**

Change PRG table Step 1 from:
`| 1 | Temporal Check | Run \`Get-Date\`. Compute Lome UTC+0. State CURRENT_DATETIME as first line of response. |`

To:
`| 1 | Temporal Check | Run \`Get-Date\`. Compute Lome UTC+0. If message starts with \`fhq\`, \`boot\`, or \`shutdown\`: reload CADENCE.md current day section, compute elapsed time since session start or last \`fhq\`. State CURRENT_DATETIME as first line of response. |`

- [ ] **Update output format section**

Replace the `**Output format:**` block with:

```
**Output format (default - no keyword or DIRECT):**
```
**[datetime Lome UTC+0]**
- Projets actifs: [top 3 priorities from PRIORITY_MATRIX]
- [single highest-priority action]
---
[response content]
```

**Output format (fhq mode):**
```
**[datetime Lome UTC+0] | Session: [HH:MM since boot] | Cadence: [Week SXX, Month YYYY]**
- Projets actifs: [top 3 priorities]
- Lifecycle: [active phases]
- [single highest-priority action]
---
[response content]
```

**Output on `boot`:**
```
**[datetime Lome UTC+0] | Day started at [HH:MM]**
- Full initialization complete.
---
[awareness report + next action]
```

**Output on `shutdown`:**
```
**[datetime Lome UTC+0] | Session ended. Duration: [Xh YYm]**
- State saved.
---
[summary of what was done, last action, next session entry point]
```
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/SYSTEM_PROMPT.md
git commit -m "feat: add fhq/boot/shutdown keywords to Intent Classification + enrich boot sequence with cadence/lifecycle/alerts"
```

---

### Task 10: Modify `Runtime/RUNTIME_KERNEL.md` - Conditional BOOT + Enriched ORIENT

**Files:**
- Modify: `FounderOS/Runtime/RUNTIME_KERNEL.md`

- [ ] **Read current file**

```cmd
type FounderOS\Runtime\RUNTIME_KERNEL.md
```

- [ ] **Replace Phase 1: BOOT section**

Replace the old BOOT section with:

```
## Phase 1: BOOT

Execute at session start - triggered by user message starting with `boot` or first `fhq` of the day. If the session is already active (a prior `fhq` or `boot` was processed today), BOOT is skipped and the cycle starts at OBSERVE.

### Full Boot (triggered by `boot` or first daily `fhq`):

Operations:
1. Load State/CURRENT_STATE.md
2. Load State/PRIORITY_MATRIX.md
3. Load State/CADENCE.md
4. Load State/LIFECYCLE.md
5. Load State/WATCH_REGISTRY.md
6. Load State/ALERTS.md - read and clear
7. Load State/WATCH_REPORT.md
8. Compute datetime in Lome UTC+0
9. Set Session Start timestamp in CADENCE.md (Day -> Session Start)
10. Scan all concept footers for staleness (>48h)
11. Report: datetime, mode (SURVIVAL/GROWTH/SCALE), cadence context, lifecycle phases, top priority, stale concepts, active alerts

Output: Session awareness established.

### Quick Boot (triggered by subsequent `fhq` same day):

Operations:
1. Re-read CURRENT_STATE.md (may have changed since last cycle)
2. Re-read LIFECYCLE.md (project phases may have shifted)
3. Compute current datetime, update CADENCE.md Hour section
4. Check ALERTS.md for new entries from background scripts

Output: Updated temporal awareness, skipping full initialization.
```

- [ ] **Replace Phase 3: ORIENT section**

Replace the old ORIENT section with:

```
## Phase 3: ORIENT

Understand what the input means in the current context. Cross-reference cadence, lifecycle, and active frameworks.

Operations:
1. Load relevant concepts for the classified action type
2. Verify freshness of loaded concepts
3. **Cross CADENCE x LIFECYCLE**: Determine current temporal position (week, month, quarter) and active project phases. Select frameworks matching lifecycle phase from LIFECYCLE.md phase-to-framework mapping.
4. Scan all active projects in PRIORITY_MATRIX for data room completeness
5. Flag any contradictions between files
6. Check current constraints: cash, energy, time, blockers
7. **Check ALERTS.md** for any background script notifications since last cycle
8. **Check WATCH_REPORT.md** for any new veille findings

Output: Situational awareness with flagged risks, cadence context, lifecycle-informed framework selection.
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Runtime/RUNTIME_KERNEL.md
git commit -m "feat: enrich ORIENT with CADENCE x LIFECYCLE x frameworks cross + conditional BOOT"
```

---

### Task 11: Modify `Protocols/SOURCE_OF_TRUTH.md`

**Files:**
- Modify: `FounderOS/Protocols/SOURCE_OF_TRUTH.md`

- [ ] **Read current file**

```cmd
type FounderOS\Protocols\SOURCE_OF_TRUTH.md
```

- [ ] **Find the relevant table/section** and add these rows:

```
| CADENCE.md | State/ | System | Temporal hierarchy (life->year->month->week->day->hour). Session timestamps. |
| LIFECYCLE.md | State/ | System | Per-project lifecycle phase. Gates. Framework mapping. |
| ALERTS.md | State/ | Scripts->LLM | Bridge file. Background script alerts read and cleared at boot. |
| WATCH_REPORT.md | State/ | watchtower.py | Veille findings from watchtower, consumed at boot. |
```

- [ ] **Commit**

```bash
cd C:/Users/junio/Desktop/FounderHQ
git add FounderOS/Protocols/SOURCE_OF_TRUTH.md
git commit -m "docs: register CADENCE.md, LIFECYCLE.md, ALERTS.md, WATCH_REPORT.md in SOURCE_OF_TRUTH"
```

---

## Self-Review Checklist

### 1. Spec Coverage
- `fhq` keyword - Task 9 (Intent Classification) + Task 10 (conditional BOOT)
- `boot` keyword - Task 9 + Task 10 (full BOOT)
- `shutdown` keyword - Task 9 (tracks session duration, saves state)
- No keyword - Task 9 (DIRECT mode, no cycle)
- CADENCE.md - Task 1
- LIFECYCLE.md - Task 2
- ALERTS.md + WATCH_REPORT.md - Task 3
- cadence_engine.py - Task 4 (week/month computation, framework selection)
- watchtower.py - Task 5 (6h veille script)
- timekeeper.py - Task 6 (30min deadlines + SOS timer)
- installer.py - Task 7 (Windows Task Scheduler setup)
- ORIENT enrichment - Task 10 (CADENCE x LIFECYCLE x frameworks cross)
- SOURCE_OF_TRUTH - Task 11
- `__init__.py` - Task 8

### 2. Placeholder Scan
No placeholders found. All code blocks are complete. All file paths are exact. All commands are exact.

### 3. Type Consistency
- `get_week_of_month(dt: datetime) -> int` - defined and tested in Task 4, used in `get_cadence_context`
- `get_cadence_context(dt: datetime) -> dict` - defined and tested in Task 4
- `get_active_frameworks(ctx: dict) -> list[str]` - defined and tested in Task 4
- `parse_watch_registry(path: Path) -> list[dict]` - defined in Task 5
- `execute_watch(item: dict, base_dir: str) -> str` - defined in Task 5
- `update_registry(path: Path, item: dict, result: str) -> None` - defined in Task 5
- `append_watch_report(base_path: Path, item: dict, result: str) -> None` - defined in Task 5
- `send_toast(title: str, message: str) -> bool` - defined in Task 6
- `parse_deadlines(base_path: Path) -> list[dict]` - defined in Task 6
- `check_sos_timer(base_path: Path) -> Optional[str]` - defined in Task 6
- `append_alert(base_path: Path, severity: str, message: str) -> None` - defined in Task 6
- `task_exists(task_name: str) -> bool` - defined in Task 7
- `create_task(...) -> bool` - defined in Task 7
- `remove_task(task_name: str) -> bool` - defined in Task 7
- `check_burnt_toast() -> bool` - defined in Task 7

All method signatures consistent across tasks.
