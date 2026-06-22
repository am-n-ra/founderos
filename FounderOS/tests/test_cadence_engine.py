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
