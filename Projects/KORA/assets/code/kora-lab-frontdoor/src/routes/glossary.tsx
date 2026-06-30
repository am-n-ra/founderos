import { createFileRoute } from "@tanstack/react-router";
import { SiteLayout, SectionLabel } from "@/components/site-layout";

const SITE_URL = "https://koralab.org";

type Term = { term: string; definition: string };

const TERMS: Term[] = [
  { term: "Sovereign AI", definition: "Artificial intelligence systems whose models, training data, compute infrastructure, and governance are owned and controlled within a specific jurisdiction or continent, rather than rented from foreign providers." },
  { term: "African Language Model", definition: "A large language model whose training corpus, tokenizer, and evaluation benchmarks include substantial coverage of African languages and African cultural contexts." },
  { term: "Kigali Declaration on AI", definition: "The continental agreement signed in April 2025 by 54 African nations establishing a unified African position on artificial intelligence and announcing the $60 billion Africa AI Fund." },
  { term: "Africa AI Fund", definition: "The $60 billion continental investment vehicle announced at the Kigali AI summit in April 2025 to finance African AI infrastructure, talent, and applications." },
  { term: "AU Continental AI Strategy", definition: "The African Union's official policy framework for AI development across the continent, covering ethics, infrastructure, skills, applications, and continental cooperation." },
  { term: "AfDB AI 10 Billion Initiative", definition: "The African Development Bank and UNDP joint initiative targeting $10 billion in AI investment across Africa by 2035." },
  { term: "Smart Africa", definition: "The continental policy alliance of 40 African heads of state and 1.4 billion citizens coordinating digital transformation, including AI policy, across member states." },
  { term: "Low-Resource Language", definition: "A language for which limited digital text, audio, and labeled data exist, making conventional model training difficult. Most African languages are low-resource in current frontier AI systems." },
  { term: "Accessibility Layer", definition: "Kora Lab's product workstream that adapts frontier AI tools for African end users through cultural localization, multilingual interfaces, and affordable delivery." },
  { term: "Sovereign Model Lab", definition: "Kora Lab's research workstream that trains, evaluates, and releases African-owned language and multimodal models, datasets, and benchmarks." },
  { term: "Open African Languages Corpus", definition: "Kora Lab's open dataset of curated text across African languages, released under permissive licenses for use by researchers and institutions." },
];

export const Route = createFileRoute("/glossary")({
  component: GlossaryPage,
  head: () => ({
    meta: [
      { title: "Glossary | African AI & Sovereignty Terms" },
      { name: "description", content: "Definitions of key terms in African AI sovereignty: Kigali Declaration, sovereign AI, African language models, AU Continental AI Strategy, and more." },
      { property: "og:title", content: "Glossary | African AI & Sovereignty Terms" },
      { property: "og:description", content: "Key terms in African AI sovereignty, defined." },
      { property: "og:url", content: `${SITE_URL}/glossary` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { property: "og:image:width", content: "1216" },
      { property: "og:image:height", content: "640" },
      { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
      { name: "twitter:title", content: "Glossary | Kora Lab" },
      { name: "twitter:description", content: "Key African AI terms, defined." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/glossary` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "DefinedTermSet",
          name: "Kora Lab Glossary of African AI Sovereignty",
          url: `${SITE_URL}/glossary`,
          hasDefinedTerm: TERMS.map((t) => ({
            "@type": "DefinedTerm",
            name: t.term,
            description: t.definition,
            inDefinedTermSet: `${SITE_URL}/glossary`,
          })),
        }),
      },
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          itemListElement: [
            { "@type": "ListItem", position: 1, name: "Home", item: `${SITE_URL}/` },
            { "@type": "ListItem", position: 2, name: "Glossary", item: `${SITE_URL}/glossary` },
          ],
        }),
      },
    ],
  }),
});

function GlossaryPage() {
  return (
    <SiteLayout>
      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <SectionLabel>Glossary</SectionLabel>
          <h1 className="kora-reveal mt-4 text-4xl font-black tracking-[-0.03em] md:text-6xl">African AI Sovereignty, Defined</h1>
          <p className="kora-reveal mt-6 max-w-2xl text-lg text-[#6B6B6B]">
            A working glossary of the institutions, instruments, and technical concepts that shape Africa's AI agenda.
          </p>
        </div>
      </section>

      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 pb-24">
          <dl className="divide-y divide-[#E8E8E8] border-y border-[#E8E8E8]">
            {TERMS.map((t) => (
              <div key={t.term} className="kora-reveal grid gap-3 py-8 md:grid-cols-[260px_1fr] md:gap-12">
                <dt className="text-lg font-black uppercase tracking-wider text-[#0A0A0A]">{t.term}</dt>
                <dd className="text-base leading-relaxed text-[#1A1A1A]">{t.definition}</dd>
              </div>
            ))}
          </dl>
        </div>
      </section>
    </SiteLayout>
  );
}
