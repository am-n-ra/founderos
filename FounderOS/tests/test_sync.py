import pytest
import json
from pathlib import Path
from Runtime.engine.sync import Snapshot


class TestSnapshot:
    def test_from_state_minimal(self):
        state = {
            "date": "2026-06-22 14:00 Lome UTC+0",
            "mode": "SURVIVAL",
            "cash": 2679,
            "top_priority": "Find client",
            "bottleneck": "Cash",
        }
        cadence = {"session_start": "08:00", "session_end": "14:00"}
        timeline = [{"date": "2026-06-22", "event": "Boot", "decision": "Start", "outcome": "OK"}]
        projects = {"SOJACO": {"phase": "VALIDATION"}}

        snap = Snapshot(state=state, cadence=cadence, timeline=timeline, projects=projects)
        assert snap.version == 1
        assert snap.state["mode"] == "SURVIVAL"
        assert snap.state["cash"] == 2679

    def test_to_from_json_roundtrip(self):
        original = Snapshot(
            state={"date": "test", "mode": "GROWTH", "cash": 5000, "top_priority": "X", "bottleneck": "Y"},
            cadence={"session_start": "09:00", "session_end": "17:00"},
            timeline=[{"date": "T1", "event": "E1", "decision": "D1", "outcome": "O1"}],
            projects={"P1": {"phase": "LAUNCH"}},
        )
        data = original.to_dict()
        restored = Snapshot.from_dict(data)
        assert restored.state == original.state
        assert restored.cadence == original.cadence
        assert restored.timeline == original.timeline
        assert restored.projects == original.projects

    def test_missing_fields_default(self):
        snap = Snapshot(state={"date": "x", "mode": "x", "cash": 0, "top_priority": "x", "bottleneck": "x"})
        assert snap.cadence == {}
        assert snap.timeline == []
        assert snap.projects == {}
