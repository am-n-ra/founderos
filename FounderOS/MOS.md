# FounderOS V4 — MOS (Mission Orchestrator)

## Purpose

MOS is the mission orchestration engine. It owns the what and why — translating high-level mission into concrete objectives, projects, and daily priorities.

## Position in FounderHQ

MOS sits at the top of the execution stack. It is loaded when the agent needs to determine what to pursue. It feeds priorities to DAOS (daily execution) and context to PROJECT (project state).

## Inputs
- `concepts/MISSION.md` — mission definitions, hierarchy, active/paused/archived status
- `State/CURRENT_STATE.md` — cash position, bottlenecks, current operating mode
- `concepts/TIMELINE.md` — recent events that affect priorities

## Outputs
- Priority list — ranked actions serving the highest mission
- Strategic recommendations — Stop/Pause/Accelerate/Delegate/Automate/Kill for each project
- Drift detection — when projects consume resources without mission progress

## Relations
- **DAOS** — receives priorities and generates daily action modules
- **PROJECT** — updates project status based on priority shifts
- **DECISION_ENGINE** — called when tradeoffs between missions need structured analysis

## Workflow

### Responsibilities

1. Maintain mission coherence across all projects
2. Map every project to a mission
3. Detect mission drift (projects that no longer serve a mission)
4. Prioritize projects by mission impact vs. resource cost
5. Recommend when to start, pause, or kill a project

### Mission Hierarchy

```
FounderHQ (Venture)
└── Mission 1: Soya Supply Chain (survival → stability)
└── Mission 2: DoodleMind Content (growth → brand)
└── Mission 3: FounderOS (infrastructure → leverage)
```

### Operating Principles

- **One mission at a time as top priority.** Currently: Mission 1 (cash constraints).
- **Every project must answer:** What mission does this serve? If none, kill it.
- **Mission can change.** When it does, update MISSION.md, TIMELINE.md, and all affected projects.
- **Rescue missions** (survival) trump growth missions. Growth missions trump infrastructure.

### Interface with DAOS

MOS decides what to do. DAOS decides how to do it today.

- MOS: "Soya supply chain is top priority. We need to call supplier X."
- DAOS: "Here is the call script. Here is what we learned from last call. Here is the optimal time to call."

## Footer

| Field | Value |
|---|---|
| OS Version | V4 |
| Last Verified | 2026-06-20 |
| Owner | System |
