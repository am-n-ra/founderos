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
        "day_of_week": dt.isoweekday(),
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
