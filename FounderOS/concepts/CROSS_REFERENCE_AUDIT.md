# Cross-Reference Audit Report

**Date:** 2026-06-24  
**Scope:** All `.md` files under `FounderOS/`  
**Method:** Grep for `.md` links, file paths, TODO/FIXME, "À définir", legacy references

---

## 1. Files referencing directories that do not exist

| File | Line | Broken Path | Note |
|------|------|-------------|------|
| `concepts/ASSET.md` | 93 | `Projects/Stop Nuisibles/CONTENT/` | No `Projects/` dir at root; `projects/` (lowercase) exists but `Stop Nuisibles` not inside it |
| `concepts/ASSET.md` | 183 | `Archive/Zoclo Livraison/` | Directory does not exist (only `ARCHIVE/kora-lab/`, `ARCHIVE/v1/`, `ARCHIVE/V4/` exist) |
| `concepts/ASSET.md` | 219 | `Projects/Stop Nuisibles/SUPPLIER/` | Same as above - does not exist |
| `concepts/ASSET.md` | 255 | `Projects/` | Should be `projects/` (lowercase) |
| `concepts/PROJECT.md` | 113 | `Projects/Stop Nuisibles/CONTENT/` | Does not exist |
| `concepts/PROJECT.md` | 181 | `Projects/Stop Nuisibles/CONTENT/PRODUCT_SHEET.md` | Does not exist |
| `Protocols/RELATIONSHIP_MODEL.md` | 200 | `Runtime/chatgpt/` | Directory does not exist (adapter files exist as `.md` in `Runtime/adapters/`) |
| `Protocols/RELATIONSHIP_MODEL.md` | 201 | `Runtime/claude/` | Same as above |
| `Protocols/SOURCE_OF_TRUTH.md` | 17 | `State/Scripts->LLM/ALERTS.md` | Path contains illegal `->` chars; actual file is `State/ALERTS.md` |
| `Protocols/SOURCE_OF_TRUTH.md` | 18 | `State/System/CADENCE.md` | No `State/System/` subdir; actual file is `State/CADENCE.md` |
| `Protocols/SOURCE_OF_TRUTH.md` | 19 | `State/System/LIFECYCLE.md` | No `State/System/` subdir; actual file is `State/LIFECYCLE.md` |
| `Protocols/SOURCE_OF_TRUTH.md` | 20 | `State/watchtower.py/WATCH_REPORT.md` | No `State/watchtower.py/` subdir; actual file is `State/WATCH_REPORT.md` |

## 2. Files referencing files that do not exist

| File | Line | Broken Reference | Note |
|------|------|-----------------|------|
| `concepts/ASSET.md` | 201 | `TEMPORAL_AWARENESS` | Listed as root-level file; archived to `ARCHIVE/V4/TEMPORAL_AWARENESS.md` |
| `concepts/ASSET.md` | 201 | `AUDIT` | No `AUDIT.md` at root; `CONCEPT_AUDIT.md` exists but name mismatch |
| `concepts/ASSET.md` | 201 | `PROTOCOL` | No `PROTOCOL.md`; should specify which protocol |
| `concepts/PROJECT.md` | 283 | `PROTOCOL` | Same as above |
| `concepts/PROJECT.md` | 283 | `TEMPORAL_AWARENESS` | Archived to `ARCHIVE/V4/` |
| `concepts/SYSTEM.md` | 161 | `AUDIT_LOG.md` | Does not exist anywhere |
| `concepts/MISSION.md` | 100 | `DRIFT_REPORT.md` | Does not exist anywhere |
| `Runtime/RUNTIME_INTERFACE.md` | 169 | `RUNTIME/opencode/SETUP.md` | File does not exist; only `Runtime/opencode/opencode.md` exists |
| `Runtime/RUNTIME_INTERFACE.md` | 175 | `Protocols/FOUNDEROS_PROTOCOL.md` | Archived to `ARCHIVE/V4/FOUNDEROS_PROTOCOL.md` |
| `Runtime/RUNTIME_INTERFACE.md` | 54 | `FOUNDEROS_PROTOCOL` | Archived to `ARCHIVE/V4/` |
| `Protocols/RELATIONSHIP_MODEL.md` | 219 | `FOUNDEROS_PROTOCOL` | Archived to `ARCHIVE/V4/` |
| `concepts/TIMELINE.md` | 115 | `FounderOS/DIOS.md` | Root file is `DIOS.legacy.md`; real DIOS is at `Frameworks/Specialized/Distribution/DIOS.md` |

## 3. References to archived content that should be updated

| File | Line | Reference | Should Point To |
|------|------|-----------|----------------|
| `concepts/TIMELINE.md` | 33 | `FOUNDEROS_PROTOCOL.md` | `ARCHIVE/V4/FOUNDEROS_PROTOCOL.md` or remove |
| `concepts/TIMELINE.md` | 76,79,93 | `TEMPORAL_AWARENESS` / `TEMPORAL_AWARENESS.md` | `ARCHIVE/V4/TEMPORAL_AWARENESS.md` |
| `concepts/WORKFLOW.md` | 409 | `TEMPORAL_AWARENESS.md` | `ARCHIVE/V4/TEMPORAL_AWARENESS.md` |
| `Runtime/RUNTIME_INTERFACE.md` | 54,175 | `FOUNDEROS_PROTOCOL` / `Protocols/FOUNDEROS_PROTOCOL.md` | Archived — update or remove |
| `Protocols/RELATIONSHIP_MODEL.md` | 219 | `FOUNDEROS_PROTOCOL` | Archived |
| `concepts/ASSET.md` | 201 | `TEMPORAL_AWARENESS` | Archived |
| `concepts/PROJECT.md` | 283 | `TEMPORAL_AWARENESS` | Archived |
| `Protocols/SOURCE_OF_TRUTH.md` | 88 | `ARCHIVE/V4/` is correct | ✓ (only one that's correct) |

## 4. "À définir" (unfilled) markers

| File | Line | Content |
|------|------|---------|
| `State/CADENCE.md` | 62 | `1. [À définir]` |
| `State/CADENCE.md` | 63 | `2. [À définir]` |
| `State/CADENCE.md` | 64 | `3. [À définir]` |

## 5. Legacy / v1 file references

| File | Line | Reference | Issue |
|------|------|-----------|-------|
| `concepts/TIMELINE.md` | 115 | `FounderOS/DIOS.md` | "DIOS module cree" says `FounderOS/DIOS.md` but actual file is `DIOS.legacy.md` at root, and the active DIOS is at `Frameworks/Specialized/Distribution/DIOS.md` |

## 6. Case-inconsistency issues (Windows-tolerant, breaks on Linux)

| File | Line | Written As | Actual |
|------|------|-----------|--------|
| `concepts/MISSION.md` | 63 | `Archive/` | `ARCHIVE/` (all caps on disk) |
| `Protocols/RELATIONSHIP_MODEL.md` | 177-181 | `FRAMEWORKS/Core/` | `Frameworks/Core/` (lowercase 'f' on disk) |

## 7. Additional notes

- **`Projects/Stop Nuisibles/`** does **NOT** exist at all — neither as `Projects/` (uppercase) nor as `Stop Nuisibles/` under `projects/` (lowercase). The `projects/` dir contains only `KORA/`, `Omni/`, `SOJACO/`.
- **TODO / FIXME markers:** None found anywhere in the codebase.
- **Empty/incomplete sections in `CADENCE.md`:** Lines 62-64 have `[À définir]` as placeholder for top 3 actions — these appear to be a template that was never filled.

## Summary of Findings

**Total broken references:** 30  
**By severity:**
- **Broken directory paths:** 12 (mostly stale `Projects/Stop Nuisibles/` and wrong `State/` subpaths)
- **Missing files:** 10 (mostly archived `FOUNDEROS_PROTOCOL` and `TEMPORAL_AWARENESS`)
- **Archived content not updated:** 10
- **Unfilled placeholders:** 3 (`[À définir]` in CADENCE.md)
- **Case inconsistencies:** 2 (`Archive/` vs `ARCHIVE/`, `FRAMEWORKS/` vs `Frameworks/`)
