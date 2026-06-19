# PRIORITIZATION PROTOCOL

## Concept

Parmi 100 actions possibles, quelle est la seule qui merite d'etre faite maintenant ?

Ce protocole repond a cette question.

Il n'y a pas de "priorites" multiples. Il y a UNE priorite a la fois.

---

## Regle fondamentale

Le bottleneck est la contrainte unique qui empeche tout le systeme d'avancer.

Si on resout le bottleneck, tout le systeme progresse.

Si on travaille sur autre chose, on est occupe mais on n'avance pas.

---

## Arbre de decision

### Etape 1 : Etat actuel

1. Cash > 0 ?
   - NON → Priorite absolue : generer du revenu. Tout le reste est secondaire.
   - OUI → continuer.

2. Un produit est-il en vente ?
   - NON → Priorite : mettre un produit en vente. Un produit qui n'existe pas ne peut pas generer de revenu.
   - OUI → continuer.

3. Le produit a-t-il des clients ?
   - NON → Priorite : acquerir le premier client. La distribution est le bottleneck.
   - OUI → continuer.

4. Les clients existants sont-ils satisfaits ?
   - NON → Priorite : resoudre les problemes clients. La retention avant l'acquisition.
   - OUI → continuer.

5. Le produit a-t-il atteint le product-market fit ?
   - NON → Priorite : iterer jusqu'a ce que les clients reviennent ou referent.
   - OUI → Scale.

### Etape 2 : Charger le contexte

Lire les concepts suivants pour verifier l'arbre de decision :

- State/CURRENT_STATE.md (cash, bottleneck, priorite actuelle)
- Concepts/MISSION.md (direction strategique)
- Concepts/TIMELINE.md (evenements recents)

### Etape 3 : Appliquer la lentille

Si DECISION_GATES recommande un framework, le charger et appliquer ses questions au contexte.

### Etape 4 : Reduire a UNE action

Poser la question :

```
Si je ne fais qu'une seule chose aujourd'hui,
laquelle a le plus grand impact sur le bottleneck ?
```

Si la reponse est vague, la question n'a pas ete assez specific.

Reformuler jusqu'a obtenir UNE action concrete.

---

## Verification

Avant de commencer l'action, verifier :

- [ ] Cette action sert-elle directement le bottleneck identifie ?
- [ ] Cette action est-elle la plus haute leverage disponible ?
- [ ] Cette action peut-elle etre executee dans le temps disponible ?
- [ ] Cette action n'est-elle pas de l'activite deguisee en progres ?

Si les 4 reponses sont "oui" → executer.
Si une reponse est "non" → re-evaluer.

---

## Anti-patterns

- Travailler sur 3 priorites en meme temps (aucune n'avance vraiment)
- Choisir une action facile au lieu de l'action impactante
- Confondre urgence et importance
- Planifier sans executer
- Re-prioriser avant d'avoir termine la priorite actuelle
- Utiliser la planification comme echappatoire a l'execution

---

## Integration avec DECISION_GATES

Quand un type d'action est identifie via DECISION_GATES, PRIORITIZATION_PROTOCOL s'assure que c'est la BONNE action a faire maintenant.

Les deux protocoles fonctionnent en sequence :

```
DECISION_GATES     →  Quoi faire ?
PRIORITIZATION     →  Quoi faire MAINTENANT ?
```
