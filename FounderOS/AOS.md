# FounderOS V4 — AOS (Architecture Operating System)

## Purpose

AOS owns the architecture of FounderOS itself — ensuring the OS remains coherent, maintainable, and extensible as new modules are added.

## Architecture Principles

1. **Bounded concepts** — Every file owns exactly one domain
2. **Source of truth** — Every truth has exactly one owner (Regle 0)
3. **Explicit dependencies** — Every file declares its dependencies
4. **Replaceable components** — Any module can be replaced if its interface is preserved
5. **Model-independent** — No LLM-specific features, no IDE-specific features
6. **File-first** — Session memory is ephemeral; files are durable

## Architecture Audit Protocol

When invoked:

1. Scan all OS files for:
   - Undeclared dependencies
   - Duplicate truths (Regle 0 violations)
   - Missing footers
   - Stale content (>30 days without verified footer)
2. Check SOURCE_OF_TRUTH.md for missing entries
3. Report violations with file paths and line references
4. Recommend corrections

## Interface Contract

Every OS file must have:
- A `## Purpose` section (one sentence)
- A `## Footer` with: Last Verified, Owner, Dependencies
- No truths that belong in another file
- References to other files by exact path

## Evolution

AOS may recommend:
- Splitting a file that has grown too large (>300 lines)
- Merging files with overlapping domains
- Creating new modules for emerging domains
- Deprecating unused modules

## Integration

- AOS is invoked by RUNTIME weekly for maintenance
- AOS is invoked by SYSTEM_PROMPT during boot for integrity check
- AOS reports to CONTINUOUS_IMPROVEMENT for systemic improvements

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
