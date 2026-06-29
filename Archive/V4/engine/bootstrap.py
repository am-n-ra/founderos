"""Reads FRE_SPEC.md and SYSTEM_PROMPT.md, returns combined prompt for LLM injection.

Usage:
    from engine.bootstrap import build_system_prompt
    prompt = build_system_prompt("/path/to/founderhq")
    llm = LLM(system_prompt=prompt)
"""

import os
from pathlib import Path


FRE_SPEC_PATH = "Runtime/FRE_SPEC.md"
SYSTEM_PROMPT_PATH = "SYSTEM_PROMPT.md"


def read_file(path: str) -> str:
    """Read a file and return its content. File not found -> empty string."""
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


def build_system_prompt(base_dir: str = ".") -> str:
    """Build a combined system prompt from FRE_SPEC and SYSTEM_PROMPT.

    Args:
        base_dir: Root directory of FounderHQ.

    Returns:
        Combined system prompt string.
    """
    fre_spec = read_file(os.path.join(base_dir, FRE_SPEC_PATH))
    sys_prompt = read_file(os.path.join(base_dir, SYSTEM_PROMPT_PATH))

    # If either file is missing, return whatever we have
    if not fre_spec and not sys_prompt:
        return ""

    parts = []

    if fre_spec:
        parts.append(f"# FRE SPEC — Constitutive Contracts\n\n{fre_spec}")

    if sys_prompt:
        parts.append(f"# SYSTEM PROMPT — Active Execution\n\n{sys_prompt}")

    return "\n\n---\n\n".join(parts)


def list_missing_files(base_dir: str = ".") -> list[str]:
    """Return list of expected files that are missing."""
    expected = [
        FRE_SPEC_PATH,
        SYSTEM_PROMPT_PATH,
        "State/CURRENT_STATE.md",
        "State/PRIORITY_MATRIX.md",
    ]
    missing = []
    for rel_path in expected:
        full = os.path.join(base_dir, rel_path)
        if not os.path.exists(full):
            missing.append(rel_path)
    return missing
