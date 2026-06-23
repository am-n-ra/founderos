# GENESIS Bootstrap Pipeline Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix 5 bugs found in the GENESIS first-run install pipeline so a new user can bootstrap FounderHQ from the public Gist and get a fully functional system (sync, scheduler, profile) in one flow.

**Architecture:** The public bootstrap Gist at `am-n-ra/5b7b5c366` serves as the single entry point. `sync.py`'s `cmd_create_public_gist` uploads the bootstrap files. `installer.py` runs post-fetch to set up .venv, scheduler, and marker. GENESIS in `SYSTEM_PROMPT.md` defines the LLM-driven setup steps. Fixes span all three.

**Tech Stack:** Python 3.13+, GitHub Gist API, `requests`, `python-dotenv`, `schtasks`/`cron`/`launchd`.

---

## File Map

| File | Responsibility | Change |
|------|---------------|--------|
| `Runtime/engine/sync.py` | Gist sync (public + private) | Add engine scripts to `cmd_create_public_gist` + `cmd_update_public_gist` |
| `Runtime/engine/installer.py` | First-run setup (venv, deps, scheduler, marker) | Fix summary message to be accurate; accept `--no-scheduler` flag |
| `SYSTEM_PROMPT.md` | Master entry point, defines GENESIS procedure | Fix double .venv + path ambiguity; update step order |
| `Runtime/engine/watchtower.py` | Background watch loop | Add to public Gist |
| `Runtime/engine/timekeeper.py` | Session duration monitoring | Add to public Gist |

**No new files.** All changes modify existing files.

---

### Task 1: Add engine scripts to public Gist creation

**Files:**
- Modify: `Runtime/engine/sync.py:286-297` (inside `cmd_create_public_gist`)
- Modify: `Runtime/engine/sync.py:473-515` (PUBLIC_GIST_ID, BOOTSTRAP_CONTENT, `cmd_update_public_gist`)

The public Gist currently only includes `FOUNDER_SEED.md`, `installer.py`, and `opencode.json`. It needs `sync.py`, `watchtower.py`, and `timekeeper.py` so that a new user has all engine scripts after fetching.

- [ ] **Step 1: Write the failing test for `cmd_create_public_gist`**

```python
# tests/test_sync.py — add to TestSnapshot class
def test_gist_includes_engine_scripts(self):
    """cmd_create_public_gist must include sync.py, watchtower.py, timekeeper.py."""
    # We can't call the real API, but we can verify the file list construction
    from Runtime.engine.sync import _get_public_gist_files
    # Mock paths
    from pathlib import Path
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "FOUNDER_SEED.md").write_text("# seed")
        (root / "Runtime" / "engine").mkdir(parents=True)
        for f in ["installer.py", "sync.py", "watchtower.py", "timekeeper.py"]:
            (root / "Runtime" / "engine" / f).write_text(f"# {f}")
        (root / "opencode.json").write_text("{}")
        files = _get_public_gist_files(root)
        required = {"FOUNDER_SEED.md", "installer.py", "opencode.json",
                     "sync.py", "watchtower.py", "timekeeper.py"}
        for name in required:
            assert name in files, f"Missing {name} in public Gist files"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd FounderOS
python -m pytest tests/test_sync.py::TestSnapshot::test_gist_includes_engine_scripts -v
```
Expected: `FAILED` — `ImportError` or `NameError` because `_get_public_gist_files` doesn't exist yet.

- [ ] **Step 3: Extract file-list logic from `cmd_create_public_gist`**

Extract the file list builder into a standalone function, then update `cmd_create_public_gist` to call it. Add `sync.py`, `watchtower.py`, `timekeeper.py`.

```python
# In Runtime/engine/sync.py, add after ROOT_DIR definition (~line 140)

def _get_public_gist_files(base_dir: Path) -> dict:
    """Build the files dict for the public bootstrap Gist.
    
    Returns a dict mapping filename -> {"content": str} for every file
    that should be in the public Gist.
    """
    engine_dir = base_dir / "Runtime" / "engine"
    seed_path = base_dir / "FOUNDER_SEED.md"
    opencode_path = base_dir / "opencode.json"

    files = {}

    if seed_path.exists():
        files["FOUNDER_SEED.md"] = {"content": seed_path.read_text(encoding="utf-8")}

    engine_scripts = ["installer.py", "sync.py", "watchtower.py", "timekeeper.py"]
    for name in engine_scripts:
        path = engine_dir / name
        if path.exists():
            files[name] = {"content": path.read_text(encoding="utf-8")}

    if opencode_path.exists():
        files["opencode.json"] = {"content": opencode_path.read_text(encoding="utf-8")}

    return files
```

- [ ] **Step 4: Update `cmd_create_public_gist` to use the new function**

```python
def cmd_create_public_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"

    files = _get_public_gist_files(ROOT_DIR)
    if "FOUNDER_SEED.md" not in files:
        return "ERROR: FOUNDER_SEED.md not found"
    if "installer.py" not in files:
        return "ERROR: installer.py not found"

    try:
        resp = requests.post(
            "https://api.github.com/gists",
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={
                "description": "FounderHQ V4 — Bootstrap Seed. Clone to install FHQ on any machine.",
                "public": True,
                "files": files,
            },
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: Gist POST returned {resp.status_code}: {resp.text[:200]}"
        data = resp.json()
        gist_url = data.get("html_url", "")
        return f"OK: Public Gist created at {gist_url} ({len(files)} files)"
    except Exception as e:
        return f"ERROR: {e}"
```

Replace lines 279-311 (old `cmd_create_public_gist`) with this.

- [ ] **Step 5: Update `cmd_update_public_gist` to also push engine scripts**

Currently `cmd_update_public_gist` only uploads `BOOTSTRAP.md`. Change it to push ALL files using `_get_public_gist_files`.

```python
def cmd_update_public_gist(env: dict) -> str:
    token = env.get("FHQ_GIST_TOKEN", "")
    if not token:
        return "ERROR: FHQ_GIST_TOKEN not configured"
    if requests is None:
        return "ERROR: requests library not installed"

    files = _get_public_gist_files(ROOT_DIR)
    if not files:
        return "ERROR: No files to upload"

    url = f"https://api.github.com/gists/{PUBLIC_GIST_ID}"
    try:
        resp = requests.patch(
            url,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
            json={"files": files},
            timeout=30,
        )
        if resp.status_code not in (200, 201):
            return f"ERROR: PATCH returned {resp.status_code}: {resp.text[:200]}"
        return f"OK: Public Gist updated ({len(files)} files)"
    except Exception as e:
        return f"ERROR: {e}"
```

Also remove the `BOOTSTRAP_CONTENT` constant (lines 475-495) since `BOOTSTRAP.md` no longer needs special handling — it will be included via `_get_public_gist_files` if it exists at the root.

- [ ] **Step 6: Run test to verify it passes**

```bash
cd FounderOS
python -m pytest tests/test_sync.py::TestSnapshot::test_gist_includes_engine_scripts -v
```
Expected: PASS

- [ ] **Step 7: Run existing tests to verify no regressions**

```bash
cd FounderOS
python -m pytest tests/test_sync.py -v
```
Expected: All 4 tests pass (3 existing + 1 new)

- [ ] **Step 8: Commit**

```bash
git add Runtime/engine/sync.py tests/test_sync.py
git commit -m "fix: add sync.py, watchtower.py, timekeeper.py to public bootstrap Gist"
```

---

### Task 2: Fix installer.py "Scheduler: configured" message

**Files:**
- Modify: `Runtime/engine/installer.py:342-370`

The installer prints "Scheduler: configured" even when no scheduler tasks were created. It needs to report what actually happened.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_installer.py — new file

import pytest
import subprocess
from pathlib import Path


def test_installer_reports_scheduler_accuracy(tmp_path: Path):
    """Installer must report whether scheduler tasks were actually created."""
    # Create minimal skeleton that installer expects
    (tmp_path / "Runtime" / "engine").mkdir(parents=True)
    (tmp_path / "Runtime" / "engine" / "watchtower.py").write_text("")
    (tmp_path / "Runtime" / "engine" / "timekeeper.py").write_text("")

    result = subprocess.run(
        ["python", "-m", "Runtime.engine.installer",
         "--base-dir", str(tmp_path),
         "--skip-venv", "--skip-env"],
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0
    # Must mention both watchtower and timekeeper by name
    assert "watchtower" in result.stdout.lower() or "Watchtower" in result.stdout
    assert "timekeeper" in result.stdout.lower() or "Timekeeper" in result.stdout
    # Must NOT say "Scheduler: configured" as a blanket statement
    assert "Scheduler: configured" not in result.stdout
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd FounderOS
python -m pytest tests/test_installer.py -v
```
Expected: FAIL — message still says "Scheduler: configured"

- [ ] **Step 3: Fix the summary message in `main()`**

Replace lines 365-370 in installer.py with an accurate summary that reports per-script status:

```python
    watchtower_created = False
    timekeeper_created = False

    watchtower_path = scripts_dir / "watchtower.py"
    if watchtower_path.exists():
        watchtower_created = setup_scheduler("FounderHQ-Watchtower", str(watchtower_path), str(base_path), 360)
    else:
        print(f"WARNING: {watchtower_path} not found, skipping watchtower")

    timekeeper_path = scripts_dir / "timekeeper.py"
    if timekeeper_path.exists():
        timekeeper_created = setup_scheduler("FounderHQ-Timekeeper", str(timekeeper_path), str(base_path), 30)
    else:
        print(f"WARNING: {timekeeper_path} not found, skipping timekeeper")

    create_marker(base_path)

    print("\nInstallation complete.")
    print(f"  Platform: {get_platform_label()}")
    print("  - .venv: ready")
    print("  - Dependencies: installed")
    if watchtower_created:
        print("  - Watchtower scheduler: configured (every 360 min)")
    else:
        print("  - Watchtower scheduler: NOT configured (script missing)")
    if timekeeper_created:
        print("  - Timekeeper scheduler: configured (every 30 min)")
    else:
        print("  - Timekeeper scheduler: NOT configured (script missing)")
    print("  - .founderhq_installed: created")
```

Make sure `main()` captures return values from `setup_scheduler` calls and stores them in the booleans. The existing `setup_scheduler` already returns `bool`, so this is just capturing the result.

- [ ] **Step 4: Run test to verify it passes**

```bash
cd FounderOS
python -m pytest tests/test_installer.py -v
```
Expected: PASS

- [ ] **Step 5: Run full test suite**

```bash
cd FounderOS
python -m pytest tests/ -v
```
Expected: All tests pass

- [ ] **Step 6: Commit**

```bash
git add Runtime/engine/installer.py tests/test_installer.py
git commit -m "fix: installer.py reports accurate per-script scheduler status"
```

---

### Task 3: Fix GENESIS documentation in SYSTEM_PROMPT.md

**Files:**
- Modify: `SYSTEM_PROMPT.md:44-52`

Two bugs to fix:
- **BUG-4:** GENESIS step (f) says `python Runtime/engine/installer.py` but the bootstrap Gist places `installer.py` at root (not in `Runtime/engine/`)
- **BUG-5:** GENESIS step (b) creates .venv manually, then installer.py creates it again — double work

- [ ] **Step 1: Read current GENESIS section**

Already read — lines 44-52 of SYSTEM_PROMPT.md.

- [ ] **Step 2: Edit the GENESIS steps in SYSTEM_PROMPT.md**

Replace lines 44-53 with:

```markdown
0. **First-Run Check** - Check if `.founderhq_installed` exists in FounderOS root. If absent, skip boot and execute **GENESIS**:
   - (a) **Fetch Gist**: Download all files from the public bootstrap Gist. Move `installer.py` + `sync.py` + `watchtower.py` + `timekeeper.py` to `Runtime/engine/`. FOUNDER_SEED.md stays at root. opencode.json stays at root.
   - (b) **Token**: Tell the user to create a GitHub fine-grained token at `https://github.com/settings/tokens?type=beta` with scope `gist:write` + `gist:read`, then paste it. Explain it's for multi-device sync (state, concepts, projects between machines). Only needed if they want sync — they can type `skip` to configure later.
   - (c) **.env**: If token provided, write `FHQ_GIST_TOKEN=<token>` to .env (never read the value back, never expose it). If skipped, skip this step.
   - (d) **Private Gist pull**: run `python Runtime/engine/sync.py pull` to restore personal data
   - If pull succeeds (existing user on new device): State, projects, concepts restored → skip profile → go to (f)
   - If pull fails (new user, 404/no Gist): run `python Runtime/engine/sync.py create-private-gist` (creates empty private Gist, auto-writes URL to .env) → then **(e) Build Profile**
   - (e) **Build Profile** (new users only): ask the user (in their language) about domain, role, tech stack, strategic needs, constraints, active projects, and geographic focus. Generate or update concepts/PROFILE.md from answers. Then run `python Runtime/engine/sync.py push` to upload profile + initial state to the new private Gist.
   - (f) `python Runtime/engine/installer.py --skip-env` creates .venv, installs deps, configures scheduler (schtasks/cron/launchd for watchtower + timekeeper), and creates `.founderhq_installed` marker. The `--skip-env` flag prevents duplicate .env prompts (already handled in step c).
   After GENESIS completes, proceed to step 1.
```

Key changes:
- Step (a) now explicitly says to fetch files AND move installer.py to `Runtime/engine/` (fixes BUG-4)
- Step (b) and (c) are reordered — fetch comes first, then token
- Step (f) uses `--skip-env` to avoid duplicate prompts (fixes BUG-5)
- No more manual .venv creation (step (b) was removed, installer.py handles it)
- Engine scripts are explicitly listed so the LLM knows what to move

- [ ] **Step 3: Verify the edit**

Read the edited section to confirm it's correct.

- [ ] **Step 4: Commit**

```bash
git add SYSTEM_PROMPT.md
git commit -m "fix: GENESIS docs — fix path, remove double .venv, add engine script list"
```

---

### Task 4: Update public Gist with fixed files

**Files:**
- Run: `sync.py update-public-gist` to push all changes

After Tasks 1-3 are committed, push the updated files to the live public Gist so a new user gets everything in one fetch.

- [ ] **Step 1: Run the update-public-gist command**

```bash
cd FounderOS
python Runtime/engine/sync.py update-public-gist
```
Expected: `OK: Public Gist updated (6 files)`

This pushes FOUNDER_SEED.md, installer.py, opencode.json, sync.py, watchtower.py, timekeeper.py.

If this fails (no token), fall back:
```bash
python Runtime/engine/sync.py create-public-gist
```
Expected: `OK: Public Gist created at ...` — note this creates a NEW Gist, so update the Gist ID in `sync.py` and any config files.

- [ ] **Step 2: Verify the Gist contents**

```bash
python Runtime/engine/sync.py pull-public
```
Expected: `OK: Public bootstrap version checked (6 files, latest X bytes)`

- [ ] **Step 3: Commit**

```bash
git add Runtime/engine/sync.py
git commit -m "fix: update public Gist with engine scripts"
```

---

### Task 5: End-to-end test in temp directory

**Files:**
- Run: Full GENESIS simulation in temp dir

- [ ] **Step 1: Create test directory**

```bash
$tmp = "C:\Users\junio\AppData\Local\Temp\opencode\fhq-test-v2"
New-Item -ItemType Directory -Path $tmp -Force
```

- [ ] **Step 2: Download updated Gist files**

```bash
$gistRaw = "https://gist.githubusercontent.com/am-n-ra/5b7b5c36610cc1076c798c716c7560e6/raw"
Invoke-WebRequest -Uri "$gistRaw/FOUNDER_SEED.md" -OutFile "$tmp\FOUNDER_SEED.md"
Invoke-WebRequest -Uri "$gistRaw/installer.py" -OutFile "$tmp\installer.py"
Invoke-WebRequest -Uri "$gistRaw/opencode.json" -OutFile "$tmp\opencode.json"
Invoke-WebRequest -Uri "$gistRaw/sync.py" -OutFile "$tmp\Runtime\engine\sync.py"
Invoke-WebRequest -Uri "$gistRaw/watchtower.py" -OutFile "$tmp\Runtime\engine\watchtower.py"
Invoke-WebRequest -Uri "$gistRaw/timekeeper.py" -OutFile "$tmp\Runtime\engine\timekeeper.py"
```

- [ ] **Step 3: Move installer.py to correct path (simulating GENESIS step a)**

```bash
Move-Item "$tmp\installer.py" "$tmp\Runtime\engine\installer.py"
```

- [ ] **Step 4: Run installer**

```bash
Set-Location $tmp
python Runtime/engine/installer.py --skip-env
```
Expected: .venv created, deps installed, watchtower + timekeeper scheduler configured, .founderhq_installed created. Summary shows both schedulers as "configured".

- [ ] **Step 5: Verify all artifacts exist**

```bash
Test-Path "$tmp\.venv"                              # True
Test-Path "$tmp\.venv\Scripts\python.exe"           # True (Windows)
Test-Path "$tmp\Runtime\engine\sync.py"              # True
Test-Path "$tmp\Runtime\engine\watchtower.py"         # True
Test-Path "$tmp\Runtime\engine\timekeeper.py"         # True
Test-Path "$tmp\.founderhq_installed"                 # True
```

- [ ] **Step 6: Verify pip packages installed**

```bash
& "$tmp\.venv\Scripts\python.exe" -c "import requests; import dotenv; print('OK: deps available')"
```
Expected: `OK: deps available`

- [ ] **Step 7: Clean up test directory**

```bash
Remove-Item -Recurse -Force $tmp
```

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "test: end-to-end GENESIS bootstrap verified in temp dir"
```
