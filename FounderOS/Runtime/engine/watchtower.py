"""watchtower.py - Scheduled veille script. Run every 6h via Windows Task Scheduler.

Reads State/WATCH_REGISTRY.md, checks items where Next Check <= today,
executes websearch/webfetch, updates registry Last Result, appends to WATCH_REPORT.md.

Usage:
    python Runtime/engine/watchtower.py --base-dir /path/to/FounderOS
"""

import argparse
import sys
from datetime import datetime, date, timedelta, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None

try:
    from ddgs import DDGS
except ImportError:
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        DDGS = None


_this_dir = Path(__file__).resolve().parent
_workspace_root = _this_dir.parent.parent
ENV_PATH = _workspace_root / ".env"


def read_env() -> dict:
    if not ENV_PATH.exists():
        return {}
    env = {}
    raw = ENV_PATH.read_text(encoding="utf-8-sig")
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip()
    return env


def parse_watch_registry(path: Path) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8-sig")
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
        parts = line.split("|")
        cols = [parts[i].strip() for i in range(1, min(len(parts), len(headers) + 1))]
        if len(cols) < len(headers):
            continue
        item = dict(zip(headers, cols))
        freq = item.get("Frequency", "Weekly")
        # Hourly items are always due
        if freq == "Hourly":
            items.append(item)
            continue
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


def _do_webfetch(url: str) -> str:
    if requests is None:
        return "ERROR: requests library not installed"
    try:
        resp = requests.get(url, timeout=15, allow_redirects=True)
        content_type = resp.headers.get("Content-Type", "")
        summary = ""
        if "text" in content_type or "json" in content_type or "xml" in content_type:
            body = resp.text
            summary = body[:500] + "..." if len(body) > 500 else body
        elif "image" in content_type:
            summary = f"[image {len(resp.content)} bytes]"
        else:
            summary = f"[binary {len(resp.content)} bytes]"
        return f"[webfetch] {url} -> HTTP {resp.status_code} ({summary})"
    except requests.exceptions.Timeout:
        return f"ERROR: webfetch timeout after 15s - {url}"
    except requests.exceptions.ConnectionError:
        return f"ERROR: webfetch connection failed - {url}"
    except Exception as e:
        return f"ERROR: webfetch {url} - {e}"


def _do_websearch(query: str, max_results: int = 3) -> str:
    if DDGS is not None:
        try:
            ddgs = DDGS()
            results = ddgs.text(query, max_results=max_results)
            if results:
                lines = []
                for r in results:
                    title = r.get("title", "?")
                    snippet = r.get("body", r.get("snippet", ""))[:200]
                    link = r.get("href", r.get("link", ""))
                    lines.append(f"{title}: {snippet}")
                return f"[websearch] {query}\n" + "\n".join(lines)
            return f"[websearch] {query} - no results"
        except Exception as e:
            return f"ERROR: duckduckgo-search failed: {e}"
    env = read_env()
    api_key = env.get("FHQ_SEARCH_API_KEY", "")
    if api_key and requests is not None:
        search_url = env.get(
            "FHQ_SEARCH_URL",
            "https://serpapi.com/search?q={query}&api_key={key}",
        ).format(query=query, key=api_key)
        try:
            resp = requests.get(search_url, timeout=15)
            if resp.status_code != 200:
                return f"ERROR: search API returned HTTP {resp.status_code}"
            data = resp.json()
            results = data.get("organic_results", data.get("results", []))
            if not results:
                return f"[websearch] {query} - no results"
            top = results[0]
            snippet = top.get("snippet", top.get("title", top.get("link", "")))
            return f"[websearch] {query} - {snippet[:500]}"
        except Exception as e:
            return f"ERROR: websearch {query} - {e}"
    return "[websearch] no search backend available (install duckduckgo-search)"


def execute_watch(item: dict, base_dir: str) -> str:
    source_method = item.get("Source / Method") or item.get("Query / Method") or ""
    watch_item = item.get("Watch Item", "")
    if source_method.startswith("websearch"):
        query = source_method.replace("websearch ", "", 1)
        return _do_websearch(query)
    elif source_method.startswith("webfetch"):
        url = source_method.replace("webfetch ", "", 1)
        return _do_webfetch(url)
    return f"[manual] {watch_item} - no automated check method"


def update_registry(path: Path, item: dict, result: str, priority_emoji: str = "🟢") -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8-sig")
    watch_item = item.get("Watch Item", "")
    today_str = datetime.now().strftime("%Y-%m-%d")
    freq = item.get("Frequency", "Weekly")
    if freq == "Hourly":
        # Hourly: next check = today (always due)
        next_check_str = today_str
    else:
        freq_days = {"Daily": 1, "Weekly": 7, "Monthly": 30}
        next_check_days = freq_days.get(freq, 7)
        next_check_date = datetime.now() + timedelta(days=next_check_days)
        next_check_str = next_check_date.strftime("%Y-%m-%d")
    safe_result = result.replace("|", "/")[:80]
    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if f"| {watch_item} |" in line and line.startswith("|"):
            cols = line.split("|")
            # Expected: [0]"" [1]Watch Item [2]Project [3]Query/Method [4]Frequency [5]Priority [6]Next Check [7]Last Result [8]Status [9]""
            if len(cols) >= 10:
                cols[6] = f" {next_check_str} "     # Next Check
                cols[7] = f" {today_str}: {safe_result} "  # Last Result
                cols[8] = f" {priority_emoji} "      # Status
                line = "|".join(cols)
        new_lines.append(line)
    path.write_text("\n".join(new_lines), encoding="utf-8")


def append_watch_report(base_path: Path, item: dict, result: str) -> None:
    report_path = base_path / "State" / "WATCH_REPORT.md"
    if not report_path.exists():
        report_path.write_text("# WATCH REPORT\n\n## Reports\n\n", encoding="utf-8")
    today_str = datetime.now().strftime("%Y-%m-%d %H:%M UTC+0")
    method = item.get("Source / Method") or item.get("Query / Method") or "N/A"
    entry = (
        f"### {item.get('Watch Item', 'Unknown')} - {today_str}\n\n"
        f"**Project:** {item.get('Project', 'N/A')}\n\n"
        f"**Method:** {method}\n\n"
        f"**Result:** {result}\n\n---\n\n"
    )
    with open(report_path, "a", encoding="utf-8") as f:
        f.write(entry)


def _is_empty_result(result: str) -> bool:
    """True if result is a 'no data' placeholder (manual item, no results, etc.)."""
    lowered = result.lower()
    if not result or len(result) < 20:
        return True
    if "no automated check" in lowered or "no results" in lowered or "error" in lowered:
        return True
    return False


def score_result(item: dict, result: str) -> tuple[str, int, str]:
    """Score a watch result by priority. Returns (emoji, score, reason)."""
    import re
    result_lower = result.lower()
    project = item.get("Project", "")
    score = 0
    reasons = []
    is_empty = _is_empty_result(result)
    source = (item.get("Source / Method") or item.get("Query / Method") or "").lower()

    if is_empty:
        # Minimal score for empty results (manual items need human attention)
        if "manual" in source or project in ("KORA", "TRADING"):
            return ("🟡", 4, "manual_followup_needed")
        return ("⚪", 0, "no_action")

    # Direct funding / grant call detected (only if result has real data)
    if any(kw in result_lower for kw in ["call for proposals", "call for applications", "grant", "funding", "deadline"]):
        score += 9
        reasons.append("direct_funding")
    # New opportunity discovered
    if len(result) > 100:
        score += 3
        reasons.append("fresh_data")
    # Error condition
    if "error" in result_lower:
        score += 5
        reasons.append("error_condition")
    # Deadline within 30 days
    deadline_match = re.search(r"deadline[:\s]*(\w+\s+\d{1,2},?\s*\d{4})", result, re.IGNORECASE)
    if deadline_match:
        score += 10
        reasons.append("deadline_detected")
    # Manual follow-up due (meaningful)
    if "manual" in source:
        score += 2
        reasons.append("manual_item")
    # Project weight
    if project == "KORA":
        score += 2
    elif project == "TRADING":
        score += 2
    elif project == "OMNI":
        score += 1
    # Survival mode: double funding scores
    cs_path = Path(item.get("_base_dir", ".")) / "State" / "CURRENT_STATE.md"
    if cs_path.exists() and "SURVIVAL" in cs_path.read_text(encoding="utf-8"):
        if any(kw in reasons for kw in ["direct_funding", "deadline_detected"]):
            score = int(score * 1.5)
            reasons.append("survival_x1.5")

    score = min(score, 15)
    if score >= 8:
        return ("🔴", score, "; ".join(reasons))
    elif score >= 4:
        return ("🟡", score, "; ".join(reasons))
    elif score >= 1:
        return ("🟢", score, "; ".join(reasons))
    return ("⚪", 0, "no_action")


def append_alert(base_path: Path, priority: str, message: str) -> None:
    """Append alert to ALERTS.md (same pattern as timekeeper.py)."""
    alerts_path = base_path / "State" / "ALERTS.md"
    if not alerts_path.exists():
        alerts_path.write_text("# ALERTS\n\n## Active Alerts\n\n| Priority | Alert | Source | Status |\n|----------|-------|--------|--------|\n", encoding="utf-8")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    alert_line = f"| {priority} | {message} | watchtower | {now_str} |"
    text = alerts_path.read_text(encoding="utf-8")
    # Find the Active Alerts section and append after the last data row before the next section
    lines = text.splitlines()
    insert_idx = None
    in_active = False
    for i, line in enumerate(lines):
        if "## Active Alerts" in line:
            in_active = True
            continue
        if in_active and line.startswith("## ") and "Active" not in line:
            insert_idx = i
            break
        if in_active and line.startswith("|") and "|---" not in line:
            insert_idx = i + 1
    if insert_idx is not None:
        lines.insert(insert_idx, alert_line)
    else:
        lines.append(alert_line)
    alerts_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_heartbeat(base_path: Path, task_name: str, interval_minutes: int) -> None:
    hb_path = base_path / "State" / "_HEARTBEAT.md"
    now_utc = datetime.now(timezone.utc)
    now_str = now_utc.strftime("%Y-%m-%d %H:%M")
    next_str = (now_utc + timedelta(minutes=interval_minutes)).strftime("%Y-%m-%d %H:%M")
    if not hb_path.exists():
        hb_path.write_text(
            "# HEARTBEAT\n\n"
            "| Task | Last Run (UTC) | Status | Next Expected (UTC) |\n"
            "|------|---------------|--------|---------------------|\n",
            encoding="utf-8",
        )
    lines = hb_path.read_text(encoding="utf-8").splitlines()
    new_lines = []
    found = False
    for line in lines:
        if line.startswith(f"| {task_name} |"):
            new_lines.append(f"| {task_name} | {now_str} | OK | {next_str} |")
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f"| {task_name} | {now_str} | OK | {next_str} |")
    hb_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
    parser = argparse.ArgumentParser(description="Watchtower - veille script for FounderHQ")
    parser.add_argument("--base-dir", default=str(_workspace_root), help="FounderOS root directory")
    args = parser.parse_args()
    base_path = Path(args.base_dir)
    registry_path = base_path / "State" / "WATCH_REGISTRY.md"
    if not registry_path.exists():
        print(f"WATCH_REGISTRY.md not found at {registry_path}")
        sys.exit(0)
    due_items = parse_watch_registry(registry_path)
    if not due_items:
        print("No watch items due for check today.")
        write_heartbeat(base_path, "FounderHQ-Watchtower", interval_minutes=360)
        sys.exit(0)
    for item in due_items:
        item["_base_dir"] = args.base_dir
        print(f"Checking: {item.get('Watch Item', 'Unknown')}")
        result = execute_watch(item, args.base_dir)
        emoji, score, reasons = score_result(item, result)
        update_registry(registry_path, item, result, emoji)
        append_watch_report(base_path, item, result)
        if emoji in ("🔴", "🟡"):
            alert_msg = f"[{emoji} score={score}] {item.get('Watch Item')} | {reasons} | {result[:100]}"
            append_alert(base_path, emoji, alert_msg)
        print(f"  [{emoji}] score={score} {reasons}")
        print(f"  Result: {result[:80]}...")
    write_heartbeat(base_path, "FounderHQ-Watchtower", interval_minutes=60)
    print(f"Checked {len(due_items)} watch items.")


if __name__ == "__main__":
    main()
