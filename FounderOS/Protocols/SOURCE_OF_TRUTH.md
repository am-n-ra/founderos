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
| Lecons validees, patterns confirmes | concepts/KNOWLEDGE.md |
| Evenements, decisions, outcomes | concepts/TIMELINE.md |
| Processus, etapes d'execution | concepts/WORKFLOW.md |
| Methodes validees (3+ contextes differents) | concepts/PLAYBOOK.md |
| Fonctionnement interne de FounderHQ | concepts/SYSTEM.md |
| Historique des decisions (contexte, raison, resultat) | concepts/TIMELINE.md |
| Quand charger quel framework | Protocols/DECISION_GATES.md |
| Demarrage et sequence de boot | Protocols/FOUNDEROS_PROTOCOL.md |
| Heure, age des informations, fraicheur | Protocols/TEMPORAL_AWARENESS.md |
| Graphe de dependances entre concepts | Protocols/RELATIONSHIP_MODEL.md |
| Priorisation : quoi faire MAINTENANT | Protocols/PRIORITIZATION_PROTOCOL.md |
| Marketing, campagne (lentille) | Frameworks/Content/MAOS.md |
| Automation, agents (lentille) | Frameworks/AI/AAOS.md |
| Production video entites (lentille) | Frameworks/AI/AI_VIDEO_MASTER_DOMAIN.md |
| Ce fichier (carte des verites) | Protocols/SOURCE_OF_TRUTH.md |

## Regle de maintenance

Si on ajoute une nouvelle verite au systeme, on doit :
1. Determiner son proprietaire unique
2. L'ajouter a cette carte
3. Verifier qu'aucun autre document ne la possede deja
