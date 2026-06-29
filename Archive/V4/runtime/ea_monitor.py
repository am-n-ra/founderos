#!/usr/bin/env python3
"""
EA Monitor — M1 Loop + SQLite Logging
Detects reversal setups on EURUSD M1, logs to SQLite.
No live trading in Phase 1 (detection only).
"""

import sys
import os
import time
import json
import sqlite3
from datetime import datetime
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from strategy_rules import (
    Candle, detect_setup, Direction, Setup
)

# --- Config ---
SYMBOL = "EURUSD"
TIMEFRAME = "M1"
DB_PATH = Path(__file__).parent.parent.parent / "State" / "ea_setups.db"
STATE_PATH = Path(__file__).parent.parent.parent / "State" / "_ea_state.json"

# Position sizing
BASE_RISK = 0.50
SL_POINTS = 10
TP_POINTS = 34.1
POINT_VALUE = 0.00001


def init_db():
    """Create SQLite database and table if not exists."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS setups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            direction TEXT NOT NULL,
            entry_price REAL NOT NULL,
            sl_price REAL NOT NULL,
            tp_price REAL NOT NULL,
            b1_open REAL, b1_high REAL, b1_low REAL, b1_close REAL,
            b2_open REAL, b2_high REAL, b2_low REAL, b2_close REAL,
            rules_passed TEXT,
            logged_at TEXT NOT NULL
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS state (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def log_setup(conn, setup: Setup):
    """Log a detected setup to SQLite."""
    c = conn.cursor()
    now = datetime.utcnow().isoformat()
    c.execute("""
        INSERT INTO setups (
            timestamp, direction, entry_price, sl_price, tp_price,
            b1_open, b1_high, b1_low, b1_close,
            b2_open, b2_high, b2_low, b2_close,
            rules_passed, logged_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        setup.timestamp,
        setup.direction.value,
        setup.entry_price,
        setup.sl_price,
        setup.tp_price,
        setup.b1.open, setup.b1.high, setup.b1.low, setup.b1.close,
        setup.b2.open, setup.b2.high, setup.b2.low, setup.b2.close,
        json.dumps(setup.rules_passed),
        now,
    ))
    conn.commit()
    print(f"[{now}] SETUP LOGGED: {setup.direction.value} @ {setup.entry_price}")
    print(f"  SL: {setup.sl_price} | TP: {setup.tp_price}")
    print(f"  Rules: {', '.join(setup.rules_passed)}")


def load_state() -> dict:
    """Load persistent state."""
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"last_candle_time": None, "setups_today": 0, "total_setups": 0}


def save_state(state: dict):
    """Save persistent state."""
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def get_mt5_candles(symbol=SYMBOL, count=6):
    """
    Get last N candles from MT5.
    Returns list of Candle objects, newest last.
    Returns empty list if MT5 not available.
    """
    try:
        import MetaTrader5 as mt5

        if not mt5.initialize():
            print(f"MT5 init failed: {mt5.last_error()}")
            return []

        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, count)
        mt5.shutdown()

        if rates is None or len(rates) == 0:
            return []

        candles = []
        for r in rates:
            ts = datetime.fromtimestamp(r['time']).isoformat()
            candles.append(Candle(
                open=r['open'],
                high=r['high'],
                low=r['low'],
                close=r['close'],
                timestamp=ts,
            ))
        return candles

    except ImportError:
        print("MetaTrader5 package not available (Windows only)")
        return []
    except Exception as e:
        print(f"MT5 error: {e}")
        return []


def get_simulated_candles():
    """
    Generate simulated M1 candles for testing.
    Returns 6 candles with realistic EURUSD data.
    """
    import random
    base = 1.0850
    candles = []
    for i in range(6):
        o = base + random.uniform(-0.0005, 0.0005)
        c = o + random.uniform(-0.0008, 0.0008)
        h = max(o, c) + random.uniform(0, 0.0003)
        l = min(o, c) - random.uniform(0, 0.0003)
        ts = datetime.utcnow().isoformat()
        candles.append(Candle(open=o, high=h, low=l, close=c, timestamp=ts))
        base = c
    return candles


def run_monitor(use_simulation=False):
    """Main monitoring loop."""
    print("=" * 60)
    print(f"EA Monitor — {SYMBOL} {TIMEFRAME}")
    print(f"SL: {SL_POINTS} points | TP: {TP_POINTS} points")
    print(f"Base risk: ${BASE_RISK}")
    print(f"Database: {DB_PATH}")
    print("=" * 60)

    conn = init_db()
    state = load_state()

    print("\nMonitoring... (Ctrl+C to stop)\n")

    try:
        while True:
            # Get candles
            if use_simulation:
                candles = get_simulated_candles()
            else:
                candles = get_mt5_candles()

            if not candles:
                print(f"[{datetime.utcnow().isoformat()}] No candles available, retrying...")
                time.sleep(10)
                continue

            # Check for new candle
            current_time = candles[-1].timestamp
            if current_time == state.get("last_candle_time"):
                time.sleep(5)  # Wait 5s before next check
                continue

            state["last_candle_time"] = current_time

            # Detect setup
            setup = detect_setup(candles, sl_points=SL_POINTS, tp_points=TP_POINTS)

            if setup:
                log_setup(conn, setup)
                state["setups_today"] += 1
                state["total_setups"] += 1
                save_state(state)

                # Print summary
                print(f"  Total setups: {state['total_setups']}")
                print()

            # Sleep until next candle close (~55s)
            time.sleep(55)

    except KeyboardInterrupt:
        print("\n\nMonitor stopped.")
        print(f"Total setups logged: {state.get('total_setups', 0)}")
    finally:
        conn.close()
        save_state(state)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="EA Monitor EURUSD M1")
    parser.add_argument("--simulate", action="store_true",
                        help="Use simulated candles instead of MT5")
    args = parser.parse_args()

    run_monitor(use_simulation=args.simulate)
