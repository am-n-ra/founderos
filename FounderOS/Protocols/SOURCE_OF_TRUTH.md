# SOURCE OF TRUTH

## Rule 0

Every system truth has EXACTLY one owner.

If two documents contain the same truth → violation.
If a document contains a truth it does not own → violation.

## Truth Map

| Truth | Owner |
|--------|-------------|
| Mission, vision, principes strategiques | concepts/MISSION.md |
| Projets actifs, statut, outcome attendu | concepts/PROJECT.md |
| Etat operationnel actuel | State/CURRENT_STATE.md |
| Bridge file. Background script alerts read and cleared at boot. | State/Scripts->LLM/ALERTS.md |
| Temporal hierarchy (life->year->month->week->day->hour). Session timestamps. | State/System/CADENCE.md |
| Per-project lifecycle phase. Gates. Framework mapping. | State/System/LIFECYCLE.md |
| Veille findings from watchtower, consumed at boot. | State/watchtower.py/WATCH_REPORT.md |
| Prix, cout, stock, marques, audiences | concepts/ASSET.md |
| Contacts fournisseurs (tel, email, termes) | concepts/ASSET.md |
| Comptes reseaux sociaux, chaines YouTube | concepts/ASSET.md |
| Lecons validees, patterns confirmes | concepts/KNOWLEDGE.md |
| Pipeline contenu YouTube doodle long-form | concepts/KNOWLEDGE.md (KnowledgeAssets/) |
| Pipeline Shorts viraux doodle | concepts/KNOWLEDGE.md (KnowledgeAssets/) |
| Evenements, decisions, outcomes | concepts/TIMELINE.md |
| Processus, etapes d'execution | concepts/WORKFLOW.md |
| Methodes validees (3+ contextes differents) | concepts/PLAYBOOK.md |
| Fonctionnement interne de FounderHQ | concepts/SYSTEM.md |
| Historique des decisions (contexte, raison, resultat) | concepts/TIMELINE.md |
| Quand charger quel framework | Protocols/DECISION_GATES.md |
| Demarrage et sequence de boot, execution modes, permissions | SYSTEM_PROMPT.md |
| Heure, age des informations, fraicheur | SYSTEM_PROMPT.md |
| Detection de fraicheur des concepts | concepts/WORKFLOW.md (WF-007) |
| Graphe de dependances entre concepts | Protocols/RELATIONSHIP_MODEL.md |
| Priorisation : quoi faire MAINTENANT | Protocols/PRIORITIZATION_PROTOCOL.md |
| Marketing, campaigns (lens) | Frameworks/Content/MAOS.md |
| Automation, agents (lens) | Frameworks/AI/AAOS.md |
| Video production entities (lens) | Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md |
| Master entry point, identity, primary directive | SYSTEM_PROMPT.md |
| Classification automatique des intentions, routage des modules | SYSTEM_PROMPT.md |
| Session mode, permissions, constraints, integrity check | SYSTEM_PROMPT.md |
| Daily operating loop (Assess → Decide → Execute → Learn → Prepare) | RUNTIME.md |
| Mission orchestration, priorities | MOS.md |
| Daily execution, action modules | DAOS.md |
| Strategic vision, long-term thinking | VEAOS.md |
| Content engineering, video production | CEOS.md |
| Reflection, clarity, pattern awareness | ASTRA.md |
| Knowledge management, hygiene | KMOS.md |
| Learning pipeline, knowledge gaps | LEOS.md |
| External research, intelligence | RIOS.md |
| Fundraising, revenue, alliances | FAOS.md |
| Founder wellbeing, energy, mindset | SOS.md |
| OS architecture, coherence, audits | AOS.md |
| Structured decision-making (PROACT) | DECISION_ENGINE.md |
| Pattern detection across actions/outcomes | PATTERN_ENGINE.md |
| Playbook creation, validation, evolution | PLAYBOOK_ENGINE.md |
| Long-term knowledge evolution, decay | KNOWLEDGE_EVOLUTION_ENGINE.md |
| Meta-improvement of FounderOS itself | CONTINUOUS_IMPROVEMENT.md |
| Complete video production system | AI_VIDEO_MASTER_DOMAIN.md |
| FRE: runtime constitution and system contracts | Runtime/FRE_SPEC.md |
| FRE: universal execution cycle (BOOT → OBSERVE → ORIENT → DECIDE → ACT → LEARN → UPDATE) | Runtime/RUNTIME_KERNEL.md |
| FRE: adapter interface contract (4 mandatory questions) | Runtime/ADAPTER_INTERFACE.md |
| Distribution intelligence, audience, language, platform strategy | Frameworks/Specialized/Distribution/DIOS.md |
| Distribution: audience segmentation and targeting | Frameworks/Specialized/Distribution/DIOS/AUDIENCE_INTELLIGENCE.md |
| Distribution: language-market derivation and cultural adaptation | Frameworks/Specialized/Distribution/DIOS/LANGUAGE_INTELLIGENCE.md |
| Distribution: platform selection by audience behavior | Frameworks/Specialized/Distribution/DIOS/PLATFORM_INTELLIGENCE.md |
| Distribution: hook creation and testing | Frameworks/Specialized/Distribution/DIOS/HOOK_INTELLIGENCE.md |
| Distribution: offer design and presentation | Frameworks/Specialized/Distribution/DIOS/OFFER_INTELLIGENCE.md |
| Distribution: rhythm, cross-posting, campaign structure | Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_INTELLIGENCE.md |
| Distribution: CTA design, objection handling, WhatsApp closing | Frameworks/Specialized/Distribution/DIOS/CONVERSION_INTELLIGENCE.md |
| Distribution: campaign memory and learning loop | Frameworks/Specialized/Distribution/DIOS/DISTRIBUTION_MEMORY.md |
| Venture architecture, venture creation and structuring | Frameworks/Specialized/Venture/VAOS.md |
| Venture: vision definition and reality transformation | Frameworks/Specialized/Venture/VAOS/VISION_ENGINE.md |
| Venture: mission definition and approach | Frameworks/Specialized/Venture/VAOS/MISSION_ENGINE.md |
| Venture: theory of change and causal logic | Frameworks/Specialized/Venture/VAOS/THEORY_OF_CHANGE.md |
| Venture: strategic asset inventory and gap analysis | Frameworks/Specialized/Venture/VAOS/ASSET_MAPPING.md |
| Venture: strategic planning and bet sequencing | Frameworks/Specialized/Venture/VAOS/STRATEGIC_PLANNING.md |
| Venture: roadmap with phase gates and milestones | Frameworks/Specialized/Venture/VAOS/ROADMAP_ENGINE.md |
| Venture: capital strategy and funding sources | Frameworks/Specialized/Venture/VAOS/CAPITAL_STRATEGY.md |
| Venture: business plan generation from VAOS cascade | Frameworks/Specialized/Venture/VAOS/BUSINESS_PLAN_ENGINE.md |
| Venture: constraint analysis and bottleneck identification | Frameworks/Specialized/Venture/VAOS/CONSTRAINT_ANALYSIS.md |
| Venture: repositioning and venture repair | Frameworks/Specialized/Venture/VAOS/VENTURE_REPOSITIONING.md |
| Campaign performance data, hook/audience/language history | concepts/DISTRIBUTION_MEMORY.md |
| First-time setup procedure | GENESIS.md |
| Installation guide, troubleshooting | INSTALL.md |
| Archives V3/V4 (KERNEL, FOUNDEROS_PROTOCOL, TEMPORAL_AWARENESS) | ARCHIVE/V4/ |
| Gist-based sync (pull/push/merge) | Runtime/engine/sync.py |
| Portable markdown snapshot (no token) | Runtime/engine/snapshot.py |
| Secrets (GitHub token — NEVER read by LLM) | .env |
| First-run installation marker | .founderhq_installed |
| Single-file distribution of all core files | FOUNDER_SEED.md |
| Ce fichier (carte des verites) | Protocols/SOURCE_OF_TRUTH.md |

## Maintenance Rule

If a new truth is added to the system, we must:
1. Determine its unique owner
2. Add it to this map
3. Verify that no other document already owns it
