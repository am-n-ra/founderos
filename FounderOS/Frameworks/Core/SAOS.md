# SAOS — Systems Analysis Operating System

## Quand utiliser cette lentille

Conception, audit ou debug d'un systeme (architecture, projet, workflow, organisation).

## Questions obligatoires

1. Quels sont les composants du systeme ?
2. Quelles sont les dependances entre composants ?
3. Quelle est la frontiere de chaque composant ?
4. Quelle est la verite que chaque composant possede ?
5. Quelle verite chaque composant ne possede-t-il PAS ?
6. Quel est le bottleneck unique ?
7. Qu'est-ce qui casse si on retire X ?
8. Quelle est la source unique de verite pour chaque donnee ?
9. Le composant peut-il etre reconstruit si perdu ?
10. Quel est le cout de sa suppression ?

## Principes

- Un systeme sain a des frontieres claires entre ses composants.
- Chaque composant possede UNE verite et UNE seule.
- Le bottleneck est la contrainte unique qui limite tout le systeme.
- Un composant qui peut etre reconstruit facilement a moins de valeur qu'un composant qui ne peut pas l'etre.
- La separation des responsabilites est le premier rempart contre l'entropie.

## Etapes d'analyse

1. Cartographier tous les composants et leurs frontieres
2. Identifier les verites que chaque composant possede
3. Tracer les dependances entre composants
4. Trouver le bottleneck (le composant qui limite le debit du systeme)
5. Tester la resilience : supprimer chaque composant mentalement et evaluer l'impact
6. Verifier la Regle 0 : chaque verite a exactement un proprietaire

## Anti-patterns

- Composants qui possedent la meme verite → duplication, contradiction
- Composants sans frontiere claire → incoherence
- Composants sans verite propre → morte, inutile
- Systeme sans bottleneck identifie → priorisation impossible
- Ajouter des composants sans verifier les frontieres avec les existants
