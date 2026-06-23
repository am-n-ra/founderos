# OpenCode Runtime Adapter

## Detection

FounderHQ is auto-detected when the working directory contains FounderOS/. The protocol boots automatically via Protocols/FOUNDEROS_PROTOCOL.md.

## Configuration File

.opencode/instructions.md contains the rules specific to the OpenCode environment.

## Specificities

- **Shell:** Windows PowerShell 5.1
- **Timezone:** Local system (auto-detected by Get-Date). Conversion to Lome UTC+0 each session.
- **Files:** CRLF (Windows)
- **DST:** [System.TimeZoneInfo]::Local.GetUtcOffset((Get-Date)) to detect the actual offset.

## Boot sequence (summary)

1. OpenCode loads Protocols/FOUNDEROS_PROTOCOL.md via system instructions
2. The protocol guides all subsequent operations
3. DECISION_GATES is loaded before each action
4. TEMPORAL_AWARENESS checks the time with each response
5. Frameworks are loaded on demand via DECISION_GATES

## Known limitations

- No automatic event detection (session-based only)
- No native automation (workflows executed manually by the LLM)
- No multi-session awareness beyond files
