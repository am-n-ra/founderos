# AAOS — Automation & Agents Operating System

## Quand utiliser cette lentille

Conception d'agents, automatisation de workflows, reduction de tache manuelle repetitive.

## Questions obligatoires

1. Cette tache est-elle repetitive ? (frequence, duree, cout humain)
2. Peut-elle etre standardisee en etapes deterministes ?
3. Quelle est la tolerance a l'erreur de l'automation ?
4. L'effort d'automation est-il inferieur au cout de la repetition manuelle ?
5. Quel est le niveau de surveillance necessaire (auto / approuve / supervisé) ?
6. L'automation cree-t-elle un levier ou une dette technique ?

## Principes

- Automatiser seulement ce qui est standardise et compris.
- Hierarchie : Documentation → Standardisation → Automation → Delegation.
- Ne pas automatiser ce qui change chaque semaine.
- L'automation sans surveillance genere du bruit.
- Un agent mal defini est pire que pas d'agent du tout.

## Antipatterns

- Automatiser avant de standardiser
- Automatiser un processus qu'on ne comprend pas
- Creer un agent sans limites claires (scope, autorite, escalation)
- Confondre automation et delegation humaine
