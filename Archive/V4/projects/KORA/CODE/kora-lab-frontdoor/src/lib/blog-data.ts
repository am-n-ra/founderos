export type BlogPost = {
  slug: string;
  title: string;
  category: "Analysis" | "Institutional" | "Technical" | "Updates";
  excerpt: string;
  date: string;
  readTime: string;
  body: string;
};

export const POSTS: BlogPost[] = [
  {
    slug: "votre-enfant-face-a-lia-guide-parent-afrique-2026",
    title: "Votre enfant face a l'IA : pourquoi chaque parent africain doit lire ce guide en 2026",
    category: "Analysis",
    excerpt:
      "Tutorat IA, deepfakes, metiers de demain, competences que l'IA ne peut pas reproduire. Le premier guide pratique pour les parents africains, ecrit depuis Lome.",
    date: "2026-05-20",
    readTime: "8 min",
    body: `## Une generation entiere grandit avec l'IA. Tres peu de parents savent quoi faire.

En 2026, un enfant ne de cette annee aura quinze ans en 2041. A ce moment-la, la plupart des metiers actuels auront ete transformes, deplaces, ou crees par l'intelligence artificielle. Les parents africains qui lisent ces lignes prennent aujourd'hui des decisions qui determineront si leur enfant sera acteur ou spectateur de cette transformation.

Le probleme n'est pas l'IA elle-meme. Le probleme est l'asymetrie d'information. Les parents en Californie ont acces a des dizaines de guides, podcasts, et conferences pour preparer leurs enfants. Les parents en Afrique francophone, eux, naviguent dans le noir avec des outils ecrits pour un autre contexte.

Ce guide existe pour combler ce vide.

## Ce que les chiffres disent vraiment

97 pour cent des parents interroges par Zety craignent l'impact de l'IA sur la carriere de leur enfant. Cette inquietude est justifiee, mais elle est aussi mal orientee. Les memes etudes montrent que les travailleurs qui maitrisent l'IA gagnent en moyenne 56 pour cent de plus que ceux qui l'ignorent, selon PwC.

Au Nigeria, une experience de la Banque Mondiale a demontre qu'un tutorat assiste par IA pendant six semaines produit l'equivalent de deux annees scolaires de progres. Cette donnee a une implication concrete pour les parents africains : l'IA n'est pas seulement un risque a contenir, c'est aussi le plus grand egalisateur educatif jamais construit, et il est gratuit.

La question n'est donc pas si vos enfants utiliseront l'IA. Ils l'utilisent deja. La question est de savoir s'ils l'utiliseront pour apprendre, ou s'ils se laisseront apprendre par elle.

## Les trois dangers que les parents sous-estiment

**Le clonage vocal.** En 2026, trois secondes d'audio suffisent pour cloner la voix d'un enfant. Des familles au Togo, au Senegal, et en Cote d'Ivoire ont deja recu des appels frauduleux utilisant la voix clonee de leur enfant pour reclamer une rancon ou un transfert Mobile Money. Le guide contient un protocole anti-deepfake familial avec un mot de passe verbal partage.

**La dependance cognitive.** Un enfant qui utilise ChatGPT pour ses devoirs sans cadre apprend a generer des reponses, pas a penser. Le guide propose un cadre simple : utiliser l'IA pour expliquer, jamais pour faire a la place.

**Le retard linguistique.** Les modeles d'IA actuels parlent mal le wolof, le yoruba, l'ewe, ou le swahili. Un enfant qui base son apprentissage uniquement sur ces outils risque de developper sa pensee dans une langue qui n'est pas la sienne. Le guide insiste sur l'equilibre linguistique a chaque age.

## Les quinze competences qui restent humaines

Le guide identifie quinze competences que l'IA, meme en 2030, ne pourra pas reproduire de maniere convaincante. Parmi elles : la presence physique reelle, la negociation face a face, le jugement ethique en situation ambigue, la creation artistique liee a une histoire personnelle, le leadership en periode de crise, et le soin direct aux personnes.

Pour chacune de ces quinze competences, le guide propose des activites concretes par tranche d'age : 3-7 ans, 8-12 ans, 13-17 ans, et 18 ans et plus. Pas de theorie. Des activites que vous pouvez commencer ce week-end.

## Pourquoi un guide ecrit depuis Lome, et pas traduit de l'anglais

La majorite des contenus parentaux sur l'IA disponibles aujourd'hui sont ecrits par et pour des familles americaines ou europeennes. Ils supposent un acces illimite a internet, un GPU dans le salon, une ecole qui integre Khan Academy, et une langue maternelle bien representee dans les modeles.

L'experience d'un parent a Lome, Cotonou, Dakar, ou Abidjan est differente. Le guide est ecrit a partir de cette realite : connexion intermittente, smartphones partages, ecoles publiques surchargees, plusieurs langues a la maison, et un budget reel.

C'est pourquoi tous les outils recommandes dans le guide sont gratuits, fonctionnent sur smartphone, et sont accessibles en franc CFA pour les versions payantes optionnelles.

## Le programme de 100 jours

La derniere partie du guide est un calendrier de cent jours, avec une action concrete par jour. Le premier jour : creer un compte famille sur un outil d'IA gratuit. Le centieme jour : votre enfant a construit, presente, et defendu son propre projet utilisant l'IA.

Entre les deux : cent micro-decisions qui transforment un foyer en environnement d'apprentissage actif.

## Pour qui ce guide n'est pas

Ce guide n'est pas pour les parents qui veulent interdire l'IA a leurs enfants. Cette strategie ne fonctionne pas, et le guide ne pretend pas le contraire. Il n'est pas non plus pour les parents qui pensent qu'il suffit de donner un telephone et de laisser faire.

Il est pour les parents qui veulent un cadre, des outils, et un plan. Il est ecrit pour etre lu en deux heures et applique en cent jours.

## Disponible maintenant

Le guide est disponible en format PDF, optimise pour la lecture sur telephone, et livre par email immediatement apres l'achat. Le prix standard est de 19 900 FCFA. Un programme partenaire permet d'acceder au guide a 9 900 FCFA via un lien de recommandation, et de gagner une commission sur chaque vente realisee grace a votre propre lien.

C'est la premiere publication grand public de Kora Lab. Toutes les recettes financent la recherche du laboratoire sur les modeles d'IA souverains pour l'Afrique.`,
  },
  {
    slug: "why-africa-needs-sovereign-ai",
    title: "Why Africa Needs Sovereign AI, Not Borrowed Tools",
    category: "Analysis",
    excerpt:
      "Frontier models reflect the data, languages, and assumptions of the regions that built them. For Africa, sovereignty is not a luxury, it is infrastructure.",
    date: "2026-04-12",
    readTime: "7 min",
    body: `## A continent absent from the training set

Every major frontier model has been trained on a corpus that is overwhelmingly English, Mandarin, and a handful of European languages. Of the more than two thousand languages spoken across Africa, almost none are represented at scale.

Consider this: Common Crawl, the most widely used text dataset for training large language models, contains less than 0.02 percent African language text despite Africa accounting for 18 percent of the global population. When African languages do appear, they are typically mixed with colonial languages in ways that models cannot distinguish. A model trained on "Wolof" data often receives a blend of Wolof and French that teaches it neither properly.

The result is predictable. A farmer in Senegal asking an LLM about crop disease in Wolof receives a hallucinated answer or a refusal. A policymaker in Abuja querying a model about Nigerian tax law in Hausa gets an answer trained on US IRS guidelines. The tools do not work because they were not built for the people who need them most.

## The economic cost of borrowed AI

The absence of African language models is not just a cultural problem. It is an economic liability with measurable consequences.

Current estimates place Africa's AI market at $18 billion by 2030. But that projection assumes the continent continues to import AI services. Under the current model, every API call to GPT-4 or Claude that originates from Africa sends revenue to US-based companies, trains their models on African data, and returns results that were not designed for African contexts.

The math is stark. If Africa spends $18 billion on AI by 2030 under the current import model, that is $18 billion in capital leaving the continent with no corresponding asset creation. No models are owned. No datasets are retained. No local talent is developed beyond prompt engineering.

Sovereignty changes this equation. When an African institution runs inference on an African model trained on African data using African compute, every part of that stack generates local value. The $18 billion becomes an investment in continental infrastructure, not an expense.

## What sovereignty looks like in practice

Sovereign AI is often misunderstood as isolationism. It is the opposite. Sovereignty means having the agency to choose integration on equitable terms.

In practice, sovereignty requires four conditions to be met simultaneously:

**African models.** Language models trained on corpora that include substantial African language data, with tokenizers that handle African language morphology efficiently, and evaluation benchmarks that measure performance on tasks relevant to African users.

**African datasets.** Training data that is collected, curated, and governed by African institutions, with consent frameworks that ensure contributors retain ownership of their linguistic and cultural assets.

**African infrastructure.** Compute capacity that is physically located on the continent or governed by African entities through sovereign cloud arrangements, so that data does not cross borders without clear agreements.

**African governance.** The institutions, policies, and standards that determine how AI systems are developed, deployed, and audited on the continent.

None of these four conditions are currently met at scale. That is the gap Kora Lab exists to close.

## The window is narrow

The frontier AI companies are moving fast. By 2027, the current generation of models will be obsolete, and the next generation will have been trained on even more data from even fewer sources. If Africa does not establish sovereign capability within the next 18 to 24 months, the cost of entry will only grow.

The political infrastructure is already in place. The African Union Continental AI Strategy provides the policy framework. The Kigali Declaration supplies the political mandate. The $60 billion Africa AI Fund promises the capital.

What is missing is the technical execution layer: the lab that trains the models, builds the datasets, benchmarks the results, and deploys them into real applications. That is what Kora Lab is.

## What Kora Lab is building

We are building the technical lab that the Kigali Declaration assumes already exists. The political will is there. The capital is committed. The execution layer is what is missing.

Our work proceeds along two tracks. The accessibility layer adapts frontier AI tools for African users today, bridging the gap while sovereign capability develops. The sovereign model lab builds the language models, datasets, and benchmarks that will give Africa its own seat at the AI table.

Both tracks are necessary. Neither alone is sufficient. Sovereignty without accessibility leaves African users behind. Accessibility without sovereignty leaves Africa dependent.

The continent has the talent, the data, and the political will. What it needs now is the infrastructure to connect them. We are building it.`,
  },
  {
    slug: "kigali-declaration-one-year-on",
    title: "The Kigali Declaration, One Year On",
    category: "Institutional",
    excerpt:
      "Fifty four nations signed. Sixty billion dollars was pledged. A year later, the question is no longer about intent. It is about execution.",
    date: "2026-04-02",
    readTime: "6 min",
    body: `## A unified continental position

The Africa Declaration on AI — signed in Kigali, Rwanda, in April 2025 by all 54 African Union member states — was a milestone without precedent. For the first time, the continent spoke with a single voice on artificial intelligence.

The declaration did not merely express aspiration. It committed signatories to specific principles: sovereign AI infrastructure, ethical deployment, continental cooperation, and a shared funding mechanism. It also announced the Africa AI Fund, a $60 billion continental investment vehicle designed to finance everything from compute infrastructure to talent pipelines.

A year later, the question is no longer about the declaration's content. It is about execution.

## What has been achieved

The year since Kigali has seen genuine progress on several fronts.

The African Union Commission activated a dedicated AI task force within three months of the declaration, charged with coordinating implementation across member states. The task force has published a preliminary continental AI infrastructure map identifying existing compute capacity, research centres, and data assets across 34 countries.

The AfDB and UNDP jointly launched the AI 10 Billion Initiative in February 2026, targeting $10 billion in blended finance for AI infrastructure by 2035. The initiative has already secured commitments from three African sovereign wealth funds and two multilateral development banks.

At the national level, at least 15 African countries now have active AI roadmaps, up from five at the time of the Kigali summit. Togo activated Digital Strategy 2025-2030, which includes AI-specific provisions for language technology and digital public infrastructure. Rwanda, Kenya, Nigeria, Ghana, and South Africa have all announced national AI compute procurement plans.

Smart Africa, the continental policy alliance of 40 heads of state, has integrated AI sovereignty into its digital transformation framework and is coordinating cross-border data governance standards.

## What remains to be done

Progress on policy has not been matched by progress on technical execution. The gap between declaration and delivery remains wide.

The Africa AI Fund, while politically transformative, has not yet disbursed a single dollar for model training or dataset development. The governance structure is still being negotiated among member states, and the technical criteria for funding allocation have not been published.

Continental compute capacity remains critically underdeveloped. Africa currently accounts for less than one percent of global data centre capacity. The AU task force's infrastructure map reveals that no country in sub-Saharan Africa outside South Africa has access to the GPU clusters required to train a large language model from scratch.

Talent pipelines are equally constrained. A 2025 study estimated that Africa produces fewer than 2,500 AI researchers with advanced degrees per year, compared to more than 30,000 in North America. The researchers who do graduate often leave for positions abroad because there are no continental labs to work in.

## The funding paradox

The $60 billion Africa AI Fund and the $10 billion AfDB-UNDP initiative represent unprecedented financial commitment. But there is a structural problem that neither addresses directly.

Both funds are designed to finance infrastructure and policy. They assume the existence of a technical lab capable of executing the research and development work that the infrastructure is meant to support. They allocate capital for GPUs but not for the models that run on them. They fund data centres but not the datasets that fill them.

This is not a criticism of the funds. A fund cannot train a model. A declaration cannot build a dataset. These are technical tasks that require a technical institution.

## Where Kora Lab fits

Kora Lab exists to close the gap between the political will expressed in Kigali and the technical execution required to realise it.

We are not a policy institution. We do not compete with the AU, the AfDB, Smart Africa, or national governments. Those bodies provide the framework and the capital. Kora Lab provides the technical layer: the models, the datasets, the benchmarks, and the trained researchers operating at continental scale.

The Kigali Declaration created the demand for African sovereign AI. Kora Lab exists to supply it.`,
  },
  {
    slug: "building-data-pipelines-that-create-jobs",
    title: "Building Data Pipelines That Create Jobs",
    category: "Technical",
    excerpt:
      "AI training data is labor. If that labor is sourced on the continent, the value chain shifts. Here is how we are designing it.",
    date: "2026-03-20",
    readTime: "7 min",
    body: `## The labor underneath the model

Every large language model that exists today is built on human labor. Before a single token is generated, thousands of people have written text, labelled data, ranked outputs, corrected errors, and reviewed quality. The model is the visible product of an invisible workforce.

The AI data labour market is estimated to employ more than one million workers globally, the majority in the Global South. Kenya, Nigeria, Ghana, Uganda, and the Philippines are major hubs for data annotation, content moderation, and reinforcement learning from human feedback. Workers label images, rank chatbot responses, transcribe audio, and filter toxic content for pennies per task.

The economics of this market are deeply extractive. A data annotator in Nairobi earns an average of $1.50 to $3.00 per hour for work that directly improves the capabilities of models whose market capitalisation exceeds one trillion dollars. The annotator's labour becomes the model's intelligence, but the annotator owns none of it. The value flows in one direction: out of the continent.

## What extraction looks like on the ground

The human cost of this model is well documented. A 2024 investigation by Time magazine revealed that OpenAI employed Kenyan workers earning less than $2 per hour to label toxic content for ChatGPT, including graphic descriptions of violence and abuse. Workers reported symptoms consistent with secondary trauma. Their labour made the model safer for Western users while exposing the workers to psychological harm with no ownership stake in the resulting product.

This is not unique to OpenAI. Every major AI company relies on a global supply chain of data labour that concentrates value at the top and distributes risk at the bottom. African workers are overrepresented in the lowest-paid, most psychologically demanding tiers of this supply chain.

The problem is structural, not incidental. The current model treats data as a raw material to be extracted and data workers as interchangeable labour. When the dataset is complete, the workers are dismissed and the value of the dataset accrues entirely to the company that commissioned it.

## A different design

Kora Lab's data pipelines are designed on a different premise: the dataset is the asset, and the contributor is a co-owner.

Our approach has three components:

**Co-ownership agreements.** Every contributor to a Kora Lab dataset signs an agreement that grants them a proportional stake in the dataset's value. If the dataset is licensed to third parties, if it is used to train a commercial model, or if it contributes to a research publication, the contributors share in the resulting revenue or recognition.

**Fair baseline compensation.** Contributors receive a base rate that exceeds local living wages, not the global minimum. Our target is $8 to $12 per hour for annotation and curation work in African countries, benchmarked to comparable skilled remote work rather than to the local poverty line.

**Career pathways.** Data work at Kora Lab is designed as an entry point to the AI economy, not a terminal occupation. Contributors receive training in machine learning fundamentals, dataset design, and quality assurance. The goal is that every contributor who completes twelve months of data work is qualified to apply for a junior research or engineering role in the lab.

## What this enables

This model turns a structural weakness into a strategic asset. Africa has the youngest population in the world, with a median age of 19. The continent produces millions of university graduates every year, many in STEM fields, but lacks the employment infrastructure to absorb them into the AI economy.

Data pipelines that pay fairly, train intentionally, and share ownership create a new economic sector. They transform AI data work from a low-wage extractive industry into a skilled knowledge profession that retains value on the continent.

For Kora Lab, this model also produces better data. Contributors who own a stake in the dataset produce higher-quality annotations, catch edge cases that hourly workers would ignore, and stay with the project long enough to develop expertise in specific language domains. A dataset built by co-owners is more accurate, more complete, and more culturally grounded than one built by anonymous contractors.

## The larger vision

If Kora Lab's model succeeds at scale, it creates a precedent that extends beyond our own datasets. It demonstrates that there is an alternative to the extractive data labour model, one in which the people who build the datasets share in the value they create.

A generation of African contributors participating in the AI economy as builders, not just as workers. That is what we are designing for.`,
  },
];
