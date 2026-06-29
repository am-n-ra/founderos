# PRG Compliance Test

Run this test after any modification to SYSTEM_PROMPT.md.

## Test 1: Critical Rules in First 30 Lines
- Read SYSTEM_PROMPT.md
- Verify "Get-Date" appears within first 30 lines
- PASS if Get-Date found in lines 1-30

## Test 2: PRG Section Present
- Search for "Pre-Response Gate (PRG)"
- PASS if section exists with all 3 steps (Temporal Check, Absorb Updates, Freshness Flag)

## Test 3: PRG Referenced in Classification Rules
- Search for "Classification Rules"
- PASS if rule 5 references PRG

## Test 4: PRG in Standard Session
- Search for "Standard Session"
- PASS if PRG appears as step in the session loop

## Test 5: PRG Output Format
- Search for PRG section
- PASS if `**[datetime Lomé UTC+0]**` output format specified

## Test 6: RUNTIME.md Has Temporal Awareness
- Read RUNTIME.md
- PASS if Temporal Awareness section exists with State Aging table and Staleness Thresholds

## Test 7: Total Lines
- Count lines in SYSTEM_PROMPT.md
- PASS if <= 130 lines
