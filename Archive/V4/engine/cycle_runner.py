#!/usr/bin/env python3
"""Cycle mode runner — alternates between fhq (most runs) and fhqa (hourly).
Scheduled every 15 min via FounderHQ-Cycle.
Every 4th run (hourly) uses fhqa mode for astral context refresh."""
import json
import os
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE / "State"
TRACKER = STATE_DIR / "_CYCLE_TRACKER.json"

data = {}
if TRACKER.exists():
    try:
        data = json.loads(TRACKER.read_text("utf-8"))
    except Exception:
        data = {}

counter = data.get("counter", -1) + 1
fhqa_every = 4

if counter >= fhqa_every:
    mode = "fhqa"
    counter = 0
else:
    mode = "fhq"

data["counter"] = counter
data["last_mode"] = mode
data["updated"] = __import__("datetime").datetime.now().isoformat()
TRACKER.write_text(json.dumps(data, indent=2), "utf-8")

os.chdir(str(BASE))
print(f"Cycle runner: mode={mode} run={counter+1}/{fhqa_every}")

ret = os.system(f'python Runtime\\engine\\cycle.py --mode {mode}')
code = (ret >> 8) if ret >= 0 else 1
print(f"cycle.py exit: {code}")
sys.exit(code)
