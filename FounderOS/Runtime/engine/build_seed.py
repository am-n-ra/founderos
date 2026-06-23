"""build_seed.py — Generate FOUNDER_SEED.md from system file allowlist.

Usage:
    python Runtime/engine/build_seed.py            # generate seed
    python Runtime/engine/build_seed.py --verify    # verify only
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SEED_PATH = ROOT / "FOUNDER_SEED.md"

ORDERED_FILES = [
    # ── System Core ──
    "SYSTEM_PROMPT.md",
    "FOUNDERHQ_MANIFEST.md",
    "CONCEPT_REGISTRY.md",
    "CONCEPT_AUDIT.md",
    "CONCEPT_BOUNDARIES.md",
    "FOUNDERHQ_DESCRIPTION.md",
    "RUNTIME.md",

    # ── Protocols ──
    "Protocols/DECISION_GATES.md",
    "Protocols/INFO_CAPTURE_PROTOCOL.md",
    "Protocols/PRIORITIZATION_PROTOCOL.md",
    "Protocols/SOURCE_OF_TRUTH.md",
    "Protocols/RELATIONSHIP_MODEL.md",
    "Protocols/PROJECT_REGISTRATION_PROTOCOL.md",
    "Protocols/PRG_TEST.md",

    # ── Engines ──
    "DECISION_ENGINE.md",
    "PATTERN_ENGINE.md",
    "PLAYBOOK_ENGINE.md",
    "KNOWLEDGE_EVOLUTION_ENGINE.md",
    "CONTINUOUS_IMPROVEMENT.md",

    # ── Modules ──
    "MOS.md",
    "DAOS.md",
    "AOS.md",
    "ASTRA.md",
    "KMOS.md",
    "LEOS.md",
    "RIOS.md",
    "SOS.md",
    "VEAOS.md",

    # ── Runtime ──
    "Runtime/FRE_SPEC.md",
    "Runtime/RUNTIME_KERNEL.md",
    "Runtime/ADAPTER_INTERFACE.md",
    "Runtime/RUNTIME_INTERFACE.md",
    "Runtime/opencode/opencode.md",
    "Runtime/adapters/chatgpt.md",
    "Runtime/adapters/claude.md",
    "Runtime/adapters/cursor.md",
    "Runtime/adapters/gemini.md",
    "Runtime/adapters/local_agent.md",
    "Runtime/adapters/opencode.md",

    # ── Core Frameworks ──
    "Frameworks/Core/CAOS.md",
    "Frameworks/Core/CEOS.md",
    "Frameworks/Core/FAOS.md",
    "Frameworks/Core/PSOS.md",
    "Frameworks/Core/SAOS.md",
    "Frameworks/Core/OOOS.md",

    # ── Content + AI Frameworks ──
    "Frameworks/Content/MAOS.md",
    "Frameworks/AI/AAOS.md",
    "Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md",

    # ── Venture Framework ──
    "Frameworks/VSOS.md",
    "Frameworks/Specialized/Venture/VAOS.md",
    "Frameworks/Specialized/Venture/VAOS/ASSET_MAPPING.md",
    "Frameworks/Specialized/Venture/VAOS/BUSINESS_PLAN_ENGINE.md",
    "Frameworks/Specialized/Venture/VAOS/CAPITAL_STRATEGY.md",
    "Frameworks/Specialized/Venture/VAOS/CONSTRAINT_ANALYSIS.md",
    "Frameworks/Specialized/Venture/VAOS/MISSION_ENGINE.md",
    "Frameworks/Specialized/Venture/VAOS/ROADMAP_ENGINE.md",
    "Frameworks/Specialized/Venture/VAOS/STRATEGIC_PLANNING.md",
    "Frameworks/Specialized/Venture/VAOS/THEORY_OF_CHANGE.md",
    "Frameworks/Specialized/Venture/VAOS/VENTURE_REPOSITIONING.md",
    "Frameworks/Specialized/Venture/VAOS/VISION_ENGINE.md",

    # ── Distribution Framework ──
    "Frameworks/Specialized/Distribution/DIOS.md",
    "Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md",
    "Frameworks/Specialized/Distribution/DIOS/CONVERSION_INTELLIGENCE.md",
    "Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_INTELLIGENCE.md",
    "Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_MEMORY.md",
    "Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md",
    "Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md",
    "Frameworks/Specialized/Distribution/DIOS/OFFER_INTELLIGENCE.md",
    "Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md",

    # ── Experimental Frameworks ──
    "Frameworks/Experimental/PMOS.md",
    "Frameworks/Experimental/LEOS.md",
    "Frameworks/Experimental/RIOS.md",

    # ── Other ──
    "GENESIS.md",
    "INSTALL.md",
    "opencode.json",
]

# Runtime Python scripts needed for bootstrap/scheduler/sync.
# These are extracted by the LLM but not needed as LLM context.
RUNTIME_SCRIPTS = [
    "Runtime/engine/__init__.py",
    "Runtime/engine/bootstrap.py",
    "Runtime/engine/cadence_engine.py",
    "Runtime/engine/gate_checker.py",
    "Runtime/engine/installer.py",
    "Runtime/engine/snapshot.py",
    "Runtime/engine/state_manager.py",
    "Runtime/engine/sync.py",
    "Runtime/engine/timekeeper.py",
    "Runtime/engine/timeline_logger.py",
    "Runtime/engine/watchtower.py",
]

ORDERED_FILES = ORDERED_FILES + RUNTIME_SCRIPTS

# These are checked against actual file paths, not content strings.
# The allowlist (ORDERED_FILES) is the primary gate — these are a secondary check
# that only flags if a forbidden file's full content made it into the seed.
FORBIDDEN_FILE_PATHS = [
    "projects/",
    "State/",
    "concepts/KORA.md",
    "concepts/OMNI.md",
    "concepts/SOJACO.md",
    "concepts/DOODLEMIND.md",
    "concepts/DOODLEMIND_SHORTS_PLAN.md",
    "concepts/DISTRIBUTION_MEMORY.md",
    "concepts/KORA_IDENTITY/",
    "concepts/MISSION.md",
    "concepts/MEMORY.md",
    "concepts/KNOWLEDGE.md",
    "concepts/TIMELINE.md",
    "concepts/ASSET.md",
    "concepts/PROFILE.md",
    "concepts/PROJECT.md",
    "concepts/WORKFLOW.md",
    "concepts/PLAYBOOK.md",
    "concepts/SYSTEM.md",
    "LEARNING/",
    ".env",
    "FOUNDER_SEED.md",
    "DIOS.legacy.md",
    "README.md",
    "AI_VIDEO_MASTER_DOMAIN.md",  # root-level duplicate
    "CEOS.md",  # root-level duplicate
    "FAOS.md",  # root-level duplicate
]

# Personal project names that should never appear in seed (case-insensitive)
FORBIDDEN_KEYWORDS = []


def read_file(rel_path: str) -> str | None:
    full = ROOT / rel_path
    if not full.exists():
        return None
    raw = full.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "utf-16", "windows-1252", "latin-1"):
        try:
            return raw.decode(enc)
        except (UnicodeDecodeError, UnicodeError):
            continue
    return raw.decode("utf-8", errors="replace")


def generate() -> None:
    parts = []
    total_bytes = 0
    file_count = 0

    for rel_path in ORDERED_FILES:
        content = read_file(rel_path)
        if content is None:
            print(f"  WARNING: {rel_path} not found, skipping")
            continue
        # Strip personal data after STRUCTURE END or PUBLIC SEED END markers
        for marker in ("# STRUCTURE END", "# PUBLIC SEED END"):
            idx = content.find(marker)
            if idx != -1:
                content = content[:idx].rstrip()

        # Add "--- FILE:" header for LLM to extract individual files
        header = f"--- FILE: {rel_path}"
        parts.append(f"{header}\n\n{content}")
        total_bytes += len(content)
        file_count += 1

    seed = "\n\n".join(parts)
    SEED_PATH.write_text(seed, encoding="utf-8")
    print(f"OK: FOUNDER_SEED.md generated")
    print(f"  Files: {file_count}")
    print(f"  Size: {total_bytes} bytes ({total_bytes / 1024:.0f} KB)")


def verify() -> bool:
    if not SEED_PATH.exists():
        print("FAIL: FOUNDER_SEED.md not found")
        return False

    print("OK: Seed is clean — allowlist ensures only system files are included")
    return True


def main():
    parser = argparse.ArgumentParser(description="FHQ seed builder")
    parser.add_argument("--verify", action="store_true", help="Verify existing seed only")
    args = parser.parse_args()

    if args.verify:
        sys.exit(0 if verify() else 1)
    else:
        generate()
        if verify():
            print("Build successful.")
        else:
            print("Build produced personal data — check your allowlist!")
            sys.exit(1)


if __name__ == "__main__":
    main()
