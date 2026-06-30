# KORA STRATEGIC PLAN — V4.0
## Mission-Driven Strategy (Step 5)

---

## Nature de KORA

KORA est un laboratoire de recherche en IA. Pas un studio de fine-tuning.

On entraine nos propres modeles. Toutes categories :
- **LLM** — text generation, raisonnement, code (Claude Opus 4.6, GPT-5.5, Qwen, DeepSeek V4)
- **Image** — generation, edition (Flux 2, Midjourney)
- **Video** — generation, comprehension (Veo, Sora)
- **Audio** — voice, music, TTS (Coqui, ElevenLabs)

On s'inspire des papiers de recherche pour l'architecture. On ne copie pas. On ne fine-tune pas.

---

## Pourquoi l'entrainement est la seule voie

Le fine-tuning ne produit pas des modeles au niveau mondial. Il adapte un modele existant a une tache specifique. Il ne rivalise pas avec les frontier.

Entrainer ses propres modeles permet :
1. **Architecture originale** — pas limite par les decisions d'un autre labo
2. **Performance native** — le modele nait performant, il ne le devient pas par adaptation
3. **Controle total** — donnees, architecture, poids, distribution
4. **Souverainete reelle** — un modele fine-tune reste lie au modele de base etranger

---

## Le Defi: Compute

Entrainer un LLM frontier demande des milliers de GPU-hours. Les assets actuelles :
- **Kaggle T4x2, 30h/sem par compte** — avec 10 comptes = 300h/sem. Suffisant pour entrainer un modele 300-500M params (MoE) depuis zero en 1-2 semaines. Pas assez pour 1B+ ou image/video sans ST Digital.
- **ST Digital GPU** — accord verbal, a concretiser
- **HAIDI $38K** — J-19, peut debloquer du compute locatif (vast.ai, runpod)

**La strategie compute :** Commencer par ce qui tient dans les ressources disponibles. Prouver l'approche sur des modeles plus petits. Puis scale up quand le compute arrive.

---

## L'Interface: Deux Entrees, Meme Modeles

Nos modeles sont utilisables comme tout modele mondial — **via texte**. API, CLI, chat, interface developpeur. Comme Claude, GPT, DeepSeek.

**La voix est notre surcouche d'inclusion.** Elle ne remplace pas le texte. Elle s'y ajoute.

| Interface | Public | Usage |
|-----------|--------|-------|
| **Texte** | Instruits, devs, API, entreprises | Standard mondial. Prompt → response. |
| **Voix** | Non-instruits, analphabetes, inclusion | Parle → modele comprend → modele repond en voix. |

**Pourquoi c'est notre avantage :** Les frontier labs font du texte (ou ajoutent la voix comme feature). Nous faisons les deux nativement. Un etudiant a Lome utilise KORA en texte. Un paysan a Kpalime utilise KORA en voix. Meme modele. Deux interfaces.

---

## Strategie: 3 Boucles, Pas 3 Phases

Pas de "public 1 d'abord, public 2 ensuite". Les deux boucles avancent en parallele car elles partagent le meme moteur : entrainer des modeles.

### Boucle A: Entrainement (le moteur)

| Categorie | Priorite | Compute necessaire | Comment |
|-----------|----------|-------------------|---------|
| LLM (small 1-7B) | Haute | Modere | Premiere preuve. Architecture efficiente. |
| LLM (large 70B+) | Haute | Massif | Quand compute ST Digital ou HAIDI confirme |
| Audio/TTS | Haute | Faible | Priorite voix. Entrainable sur Kaggle. |
| Image | Moyenne | Eleve | Apres LLM etabli |
| Video | Faible | Tres eleve | Derniere, car la plus couteuse |

**Premier modele :** Un LLM de 1-7B parametres entraine depuis zero, focalise sur :
- Performance multilingue + cross-lingual (input ewe → output ewe, input ewe → output anglais/chinois, etc.)
- Architecture inspiree de DeepSeek (MoE) ou Qwen
- Entrainable sur les ressources disponibles (ST Digital ou locatif)

**Cross-lingual natif :** Un utilisateur parle en ewe → reponse en ewe, ou document genere en anglais/chinois. Pas de pipeline traduction. Capacite native du modele.

### Boucle B: Distribution (l'acces)

Les deux publics en parallele, meme interface vocale :

| Canal | Public | Cout |
|-------|--------|------|
| Smartphone app | Tous | Developpement |
| Smart wearables | Urbains | Partenariat hardware |
| Dispositifs fixes | Institutions reculees | Partenariat institutionnel |
| Voice API | Devs / entreprises | API |

**Premiere distribution :** API texte pour devs/entreprises (standard) + app smartphone avec interface vocale pour inclusion. Meme backend. Deux frontends.

---

## Sequence d'Execution

### Sprint 1: Demarrer le Labo (Jours 1-14)

1. **Setup compute** — Confirmer ST Digital GPU. Preparer environnement d'entrainement.
2. **Architecture paper** — Choisir l'architecture inspiree de recherche pour le premier modele.
3. **Dataset** — Commencer la collecte de donnees pour l'entrainement (pas pour fine-tuning).
4. **Prototype voix** — POC interface vocale (STT/TTS).

### Sprint 2: Premier Entrainement (Jours 15-30)

1. **Lancer l'entrainement** — Premier modele KORA depuis zero.
2. **HAIDI grant** — Soumettre (J-19).
3. **Benchmark** — Comparer le modele entraine aux frontier sur les taches prevues.
4. **Publier** — Annoncer le labo, le premier modele, les resultats.

### Sprint 3: Distribution (Mois 2-3)

1. **API texte publique** — Pour devs, API standard (comme OpenAI).
2. **App vocale** — Surcouche voix pour inclusion.
3. **Early adopters** — Les instruits testent via texte, les non-instruits via voix.
4. **Iteration architecture** — Le deuxieme modele tire les lecons du premier.

### Sprint 4: Scale (Mois 3-6)

1. **Modele suivant** — Plus grand, meilleure architecture.
2. **Image ou Audio** — Deuxieme categorie de modele.
3. **Partenaires distribution** — Telecoms, institutions, hardware.
4. **Revenue** — API payante pour entreprises, freemium pour particuliers.

---

## Revenue

L'entrainement de modeles coute de l'argent. Le revenue doit arriver avant ou en parallele.

| Source | Potentiel | Delai |
|--------|-----------|-------|
| HAIDI grant | $38K | J-19 |
| EA Trading | $20-200/mo | Immédiat (test 2j) |
| API entreprises | $500-5000/mo | Mois 3+ |
| Consulting/formation | $200-1000/mission | Des qu'un modele existe |

---

## Decisions Immediates

| Decision | Pour avancer |
|----------|-------------|
| 1ere categorie de modele a entrainer ? | LLM small (1-7B) recommande |
| Architecture de reference ? | DeepSeek MoE / Qwen / Llama architecture paper |
| ST Digital GPU : relancer ? | Oui, confirmer le compute |
| HAIDI : commencer l'application ? | J-19, priorite |

---

## Footer

| Field | Value |
|-------|-------|
| Document | KORA Strategic Plan |
| Version | 4.0 — Lab Strategy |
| Owner | Kheir Lissi |
| Last Updated | 2026-06-28 |
