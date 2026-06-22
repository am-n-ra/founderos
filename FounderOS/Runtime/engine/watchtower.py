"""watchtower.py - Scheduled veille script. Run every 6h via Windows Task Scheduler.

Reads State/WATCH_REGISTRY.md, checks items where Next Check <= today,
executes websearch/webfetch, updates registry Last Result, appends to WATCH_REPORT.md.

Usage:
    python Runtime/engine/watchtower.py --base-dir /path/to/FounderHQ
"""

import argparse
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
