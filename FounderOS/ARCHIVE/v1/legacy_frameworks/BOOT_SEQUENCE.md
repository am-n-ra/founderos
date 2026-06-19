# Boot Sequence — FounderOS Complete File Inventory

## Phase 0 — Time
- `Get-Date` (system clock)

## Phase 1 — State (always load)
- `STATE/CURRENT_STATE.md` — current reality, metrics, finances, mode
- `STATE/CONFIG.md` — timezone (UTC+0), locale, paths
- `STATE/OPERATING_MODE.md` — current operating mode
- `STATE/ACTIVE_PRIORITIES.md` — top priorities this cycle
- `STATE/MISSION_PROFILE.md` — mission alignment
- `STATE/FOUNDER_PROFILE.md` — founder style, preferences, constraints
- `STATE/PRODUCT_PIPELINE.md` — all products and status
- `STATE/PROJECT_REGISTRY.md` — all projects and status
- `STATE/DIGITAL_TWIN.md` — founder state, energy, availability
- `STATE/BOOT_LOG.md` — last boot diagnostics
- `STATE/VIDEO_1_READY.md` — video production state

## Phase 2 — Memory (always load)
- `MEMORY/CURRENT_FOCUS.md` — what we're doing this week
- `MEMORY/ACTIVE_DECISIONS.md` — pending decisions
- `MEMORY/MEMORY_INDEX.md` — memory directory

## Phase 3 — Mission & Vision
- `Knowledge/VISION_2028.md` — long-term target
- `Knowledge/MISSION_2026.md` — immediate objectives
- `Knowledge/VALUES.md` — founding values
- `Knowledge/LEAN_CANVAS.md` — business model
- `Knowledge/EXECUTION_ROADMAP.md` — phased execution plan

## Phase 4 — Architecture & System
- `SYSTEM/DECISION_ENGINE.md` — how decisions are made
- `SYSTEM/WORKFLOW_REGISTRY.md` — registered workflows
- `SYSTEM/QUALITY_GATES.md` — quality standards
- `SYSTEM/DEPENDENCY_ENGINE.md` — dependency management
- `SYSTEM/MEMORY_MANAGER.md` — memory/knowledge separation
- `SYSTEM/STATE_ENGINE v1.md` — state management
- `SYSTEM/EVENT_ENGINE v1.md` — event handling
- `SYSTEM/AGENT_RUNTIME_ENGINE v1.md` — agent execution
- `SYSTEM/TEMPORAL_OPERATING_SYSTEM v1.md` — time-aware operations
- `SYSTEM/OPERATING_MODES_ENGINE v1.md` — mode switching
- `SYSTEM/MISSION_SCORE_ENGINE v1.md` — mission progress tracking
- `SYSTEM/PERSONAL_OPERATING_ENGINE v1.md` — personal optimization
- `SYSTEM/FOUNDEROS_KERNEL v1.md` — core kernel spec
- `SYSTEM/FOUNDEROS_RUNTIME v1.md` — runtime spec
- `SYSTEM/FOUNDEROS_EXECUTION_PROTOCOL.md` — execution protocol
- `SYSTEM/FOUNDEROS_FILE_CONVENTION.md` — file naming conventions
- `SYSTEM/FOUNDEROS_FILE_TEMPLATES v1.md` — file templates
- `SYSTEM/FOUNDEROS_AUDIT_REPORT.md` — audit findings

## Phase 5 — Agent Frameworks (load on demand per task)
- `SYSTEM/AAOS v2.md` — Agent Architecture OS
- `SYSTEM/AOS v1.md` — Analytics OS
- `SYSTEM/ASTRA v1.md` — Strategic OS
- `SYSTEM/CAOS v1.md` — Content Architecture OS
- `SYSTEM/CEOS v2.md` — Creative Execution OS
- `SYSTEM/DAOS v2.md` — Distribution Architecture OS
- `SYSTEM/DTOS v2.md` — Domain OS
- `SYSTEM/EOS v2.md` — Execution OS
- `SYSTEM/FAOS v2.md` — Feedback Architecture OS
- `SYSTEM/GOS v2.md` — Governance OS
- `SYSTEM/KMOS v2.md` — Knowledge Management OS
- `SYSTEM/LEOS v2.md` — Learning OS
- `SYSTEM/MAOS v2.md` — Measurement Architecture OS
- `SYSTEM/MOS v1.md` — Monitoring OS
- `SYSTEM/PMOS v2.md` — Project Management OS
- `SYSTEM/PSOS v3.md` — Personal System OS
- `SYSTEM/RIOS v2.md` — Research & Intelligence OS
- `SYSTEM/SOS v1.md` — Security OS
- `SYSTEM/VEAOS v1.md` — Video Editing Automation OS

## Phase 6 — Domain Knowledge
- `Knowledge/STORY_BIBLE.md` — product storytelling framework
- `Knowledge/SERIES_BIBLE.md` — video series framework
- `Knowledge/PATTERN_ENGINE.md` — reusable patterns
- `Knowledge/PLAYBOOK_ENGINE.md` — execution playbooks
- `Knowledge/KNOWLEDGE_EVOLUTION_ENGINE.md` — knowledge growth
- `Knowledge/CONTINUOUS_IMPROVEMENT.md` — improvement cycle
- `Knowledge/ASSET_REGISTRY.md` — all assets inventory
- `Knowledge/DESIGN_PHILOSOPHY.md` — OS design principles
- `Knowledge/AI_VIDEO_PRODUCTION_WORKFLOW.md` — video production workflow
- `Knowledge/BRAND_STRATEGY.md` — brand identity
- `Knowledge/CONTENT_PILLARS.md` — content strategy
- `Knowledge/SOCIAL_MEDIA_STRATEGY.md` — social media plan
- `Knowledge/WEBSITE_ARCHITECTURE.md` — website structure

## Phase 7 — OS Infrastructure Layers
- `Knowledge/RUNTIME_OPERATING_LAYER.md` — continuous operation
- `Knowledge/GOVERNANCE_PROTOCOL.md` — authority & risk
- `Knowledge/MISSION_CONTROL.md` — mission alignment
- `Knowledge/BOOT_MANAGER.md` — boot phases
- `Knowledge/EVENT_BUS.md` — event-driven architecture
- `Knowledge/STATE_SYNCHRONIZATION.md` — state consistency
- `Knowledge/CONNECTOR_FRAMEWORK.md` — external integrations
- `Knowledge/AUTOMATION_ENGINE.md` — automation framework

## Phase 8 — Critical Vulnerabilities
- `CVS/README.md` — critical vulnerability structure

## Phase 9 — Knowledge Subdirectories
- `Knowledge/Decisions/` — decision records
- `Knowledge/Frameworks/` — reusable frameworks
- `Knowledge/Insights/` — stored insights
- `Knowledge/Learning/` — learning materials
- `Knowledge/Research/` — research notes

## Phase 10 — Projects Scan
- `Projects/Stop Nuisibles/` — active product
- `Projects/Pillule/` — product in pipeline
- `Projects/KitSolaire/` — product in pipeline
- `Projects/Kit2USB/` — product in pipeline

## Phase 11 — Automation
- `AUTOMATIONS/Agents/` — agent definitions
- `AUTOMATIONS/Workflows/` — workflow definitions
- `AUTOMATIONS/Scripts/` — automation scripts
- `AUTOMATIONS/Logs/` — automation logs

## Post-Boot
Generate BOOT_LOG.md in STATE/ with:
- Timestamp
- Modules loaded
- Current state summary
- Mode determination
- Top priority
- Warnings (if any)
- Next action suggestion
