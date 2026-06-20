# SOURCE OF TRUTH

## Regle 0

Chaque verite du systeme a EXACTEMENT un proprietaire.

Si deux documents contiennent la meme verite → violation.
Si un document contient une verite qu'il ne possede pas → violation.

## Carte des verites

| Verite | Proprietaire |
|--------|-------------|
| Mission, vision, principes strategiques | concepts/MISSION.md |
| Projets actifs, statut, outcome attendu | concepts/PROJECT.md |
| Etat operationnel actuel | State/CURRENT_STATE.md |
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
| Demarrage et sequence de boot | Protocols/FOUNDEROS_PROTOCOL.md |
| Heure, age des informations, fraicheur | Protocols/TEMPORAL_AWARENESS.md |
| Detection de fraicheur des concepts | concepts/WORKFLOW.md (WF-007) |
| Graphe de dependances entre concepts | Protocols/RELATIONSHIP_MODEL.md |
| Priorisation : quoi faire MAINTENANT | Protocols/PRIORITIZATION_PROTOCOL.md |
| Marketing, campagne (lentille) | Frameworks/Content/MAOS.md |
| Automation, agents (lentille) | Frameworks/AI/AAOS.md |
| Production video entites (lentille) | Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md |
| Master entry point, identity, primary directive | SYSTEM_PROMPT.md |
| Session mode, permissions, constraints | KERNEL.md |
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
| First-time setup procedure | GENESIS.md |
| Installation guide, troubleshooting | INSTALL.md |
| Ce fichier (carte des verites) | Protocols/SOURCE_OF_TRUTH.md |

## Regle de maintenance

Si on ajoute une nouvelle verite au systeme, on doit :
1. Determiner son proprietaire unique
2. L'ajouter a cette carte
3. Verifier qu'aucun autre document ne la possede deja
