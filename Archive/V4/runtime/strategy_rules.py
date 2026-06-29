#!/usr/bin/env python3
"""
Strategy Rules — EURUSD M1 Reversal Detection v2
6 rules: Opposition, Engulfing, Sweep, Gap, Close, Exhaustion
Corrected per user's actual interpretation.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Direction(Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"


@dataclass
class Candle:
    open: float
    high: float
    low: float
    close: float
    timestamp: str = ""

    @property
    def body_high(self) -> float:
        return max(self.open, self.close)

    @property
    def body_low(self) -> float:
        return min(self.open, self.close)

    @property
    def range_high(self) -> float:
        return self.high

    @property
    def range_low(self) -> float:
        return self.low

    @property
    def body_size(self) -> float:
        return abs(self.close - self.open)

    @property
    def total_range(self) -> float:
        return self.high - self.low

    @property
    def direction(self) -> Direction:
        if self.close > self.open:
            return Direction.BULLISH
        elif self.close < self.open:
            return Direction.BEARISH
        return Direction.BULLISH  # doji - treated as "no direction" for R1


@dataclass
class Setup:
    direction: Direction
    entry_price: float
    sl_price: float
    tp_price: float
    b1: Candle
    b2: Candle
    timestamp: str
    rules_passed: list


def check_opposition(b1: Candle, b2: Candle) -> bool:
    """R1: B2 direction opposite to B1.
    Doji B1 (open==close) = indecision, accept any clear B2 direction.
    """
    b1_bullish = b1.close > b1.open
    b1_bearish = b1.close < b1.open
    b2_bullish = b2.close > b2.open
    b2_bearish = b2.close < b2.open

    if b1.close == b1.open:  # doji
        return b2_bullish or b2_bearish
    return (b1_bullish and b2_bearish) or (b1_bearish and b2_bullish)


def check_engulfing(b1: Candle, b2: Candle) -> bool:
    """
    R2: Range of B2 > Range of B1 in both directions.
    B2 High > B1 High AND B2 Low < B1 Low.
    """
    return b2.high > b1.high and b2.low < b1.low


def check_sweep(b1: Candle, b2: Candle) -> bool:
    """
    R3: B2 wick exceeds B1 extreme in B2's direction.
    Bearish: B2 High > B1 High (long upper wick sweeps buyers)
    Bullish: B2 Low < B1 Low (long lower wick sweeps sellers)
    """
    if b2.direction == Direction.BEARISH:
        return b2.high > b1.high
    else:
        return b2.low < b1.low


def check_gap(b1: Candle, b2: Candle) -> bool:
    """
    R4: B2 open gapped in its direction from B1 close.
    Bearish: B2 Open < B1 Close (gap down)
    Bullish: B2 Open > B1 Close (gap up)
    """
    if b2.direction == Direction.BEARISH:
        return b2.open < b1.close
    else:
        return b2.open > b1.close


def check_close(b1: Candle, b2: Candle) -> bool:
    """
    R5: B2 close exceeds B1 extreme.
    Bearish: B2 Close < B1 Low (closes below B1 low)
    Bullish: B2 Close > B1 High (closes above B1 high)
    """
    if b2.direction == Direction.BEARISH:
        return b2.close < b1.low
    else:
        return b2.close > b1.high


def check_exhaustion(candles_before_b1: list, b1: Candle, is_bullish: bool) -> bool:
    """
    R6: None of the 3 candles before B1 exceeds B1's extreme.
    Bearish: no candle before B1 has HIGH > B1 High
    Bullish: no candle before B1 has LOW < B1 Low
    """
    if len(candles_before_b1) < 3:
        return False

    for c in candles_before_b1[-3:]:
        if is_bullish:
            if c.low < b1.low:
                return False
        else:
            if c.high > b1.high:
                return False

    return True


def detect_setup(candles: list, sl_points: int = 10,
                 tp_points: float = 34.1) -> Optional[Setup]:
    """
    Detect a reversal setup on the last 2 candles (B1, B2).
    candles must have at least 5 elements (3 before B1, B1, B2).

    Returns Setup if all 6 rules pass, None otherwise.
    """
    if len(candles) < 5:
        return None

    b1 = candles[-2]
    b2 = candles[-1]
    before_b1 = candles[:-2]

    # R1: Opposition
    if not check_opposition(b1, b2):
        return None

    is_bullish = b2.direction == Direction.BULLISH

    # R2: Engulfing (range B2 > range B1)
    if not check_engulfing(b1, b2):
        return None

    # R3: Sweep
    if not check_sweep(b1, b2):
        return None

    # R4: Gap
    if not check_gap(b1, b2):
        return None

    # R5: Close
    if not check_close(b1, b2):
        return None

    # R6: Exhaustion
    if not check_exhaustion(before_b1, b1, is_bullish):
        return None

    # Calculate entry, SL, TP
    entry = b2.close
    point = 0.00001

    if is_bullish:
        sl = entry - (sl_points * point)
        tp = entry + (tp_points * point)
    else:
        sl = entry + (sl_points * point)
        tp = entry - (tp_points * point)

    return Setup(
        direction=b2.direction,
        entry_price=entry,
        sl_price=sl,
        tp_price=tp,
        b1=b1,
        b2=b2,
        timestamp=b2.timestamp,
        rules_passed=["R1 Opposition", "R2 Engulfing", "R3 Sweep",
                      "R4 Gap", "R5 Close", "R6 Exhaustion"],
    )
