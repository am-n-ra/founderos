# AI Video Production — Entity-Based Framework

## Quand utiliser cette lentille

Production video AI avec des entites recurrentes (personnages, produits, environnements).

## Principe fondamental

AI Video n'est pas une question de prompts. AI Video est une question d'entites. Les prompts sont generes a partir des entites.

Tout element visible a l'ecran est une entite. La coherence est obtenue par la persistence des entites.

## Structure requise avant production

1. **Entity Registry** — ENTITY_REGISTRY.md avec ENTITY_ID, Type, Name
2. **Entity Sheets** — PERSON_SHEET, PRODUCT_SHEET, LOCATION_SHEET par entite
3. **Environment System** — lumiere, atmosphere, meteo, mood, palette couleurs
4. **Action System** — actions reutilisables : Actor (ENTITY_ID), Action, Object, Emotion, Duree
5. **Scene System** — entites + environnement + actions + objectif narratif
6. **Frame System** — START_FRAME, END_FRAME obligatoires avant generation
7. **Video Prompt Generation** — en aval, seulement apres que toutes les dependances existent

## Quality gates

- Entity Sheets existent ✓
- Environment Sheets existent ✓
- Action Sheets existent ✓
- Scene Sheets existent ✓
- Frame Assets existent ✓

Si un gate est rouge : STOP. Generer les assets manquants avant de continuer.

## Regle FounderOS

Ne pense pas en prompts. Pense en entites.
Ne pense pas en clips. Pense en scenes.
Ne pense pas en videos. Pense en systemes.

## Content types supportes

ADVERTISEMENT, DOCUMENTARY, PODCAST, EDUCATIONAL, STORYTELLING, FOUNDER_JOURNAL, NEWS
