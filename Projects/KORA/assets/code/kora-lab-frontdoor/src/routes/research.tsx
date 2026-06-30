import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import { SiteLayout, SectionLabel } from "@/components/site-layout";
import { RESEARCH, type ResearchItem } from "@/lib/research-data";

const SITE_URL = "https://koralab.org";

export const Route = createFileRoute("/research")({
  component: ResearchPage,
  head: () => ({
    meta: [
      { title: "Research | African Language Models & Open Datasets" },
      { name: "description", content: "Working papers, analyses, policy briefs, and open datasets from Kora Lab on African language models, sovereign AI, and continental research." },
      { property: "og:title", content: "Research | African Language Models & Open Datasets" },
      { property: "og:description", content: "African AI research, working papers, datasets, and policy briefs from Kora Lab." },
      { property: "og:url", content: `${SITE_URL}/research` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { property: "og:image:width", content: "1216" },
      { property: "og:image:height", content: "640" },
      { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
      { name: "twitter:title", content: "Research | Kora Lab" },
      { name: "twitter:description", content: "African AI research and datasets." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/research` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "CollectionPage",
          name: "Kora Lab Research",
          url: `${SITE_URL}/research`,
          description: "Open research from Kora Lab on African AI, language models, datasets, and policy.",
          mainEntity: {
            "@type": "ItemList",
            itemListElement: RESEARCH.map((r, i) => ({
              "@type": "ListItem",
              position: i + 1,
              item: {
                "@type": "CreativeWork",
                name: r.title,
                description: r.description,
                author: { "@type": "Person", name: r.authors },
                datePublished: r.date,
                genre: r.type,
              },
            })),
          },
        }),
      },
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          itemListElement: [
            { "@type": "ListItem", position: 1, name: "Home", item: `${SITE_URL}/` },
            { "@type": "ListItem", position: 2, name: "Research", item: `${SITE_URL}/research` },
          ],
        }),
      },
    ],
  }),
});

const FILTERS = ["All", "Working Paper", "Analysis", "Dataset", "Policy Brief"] as const;

function ResearchPage() {
  const [filter, setFilter] = useState<(typeof FILTERS)[number]>("All");
  const items: ResearchItem[] = filter === "All" ? RESEARCH : RESEARCH.filter((r) => r.type === filter);

  return (
    <SiteLayout>
      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <SectionLabel>Research</SectionLabel>
          <h1 className="kora-reveal mt-4 text-4xl font-black tracking-[-0.03em] md:text-6xl">Research and Papers</h1>
          <p className="kora-reveal mt-6 max-w-2xl text-lg text-[#6B6B6B]">
            Kora Lab publishes working papers, analyses, and datasets on African AI, language models, and digital sovereignty.
          </p>
        </div>
      </section>

      <section className="border-y border-[#E8E8E8] bg-white">
        <div className="mx-auto max-w-[1100px] px-6">
          <div className="flex flex-wrap gap-6 py-4">
            {FILTERS.map((f) => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`text-xs font-bold uppercase tracking-wider transition-colors ${filter === f ? "border-b border-[#0A0A0A] pb-1 text-[#0A0A0A]" : "text-[#6B6B6B] hover:text-[#0A0A0A]"}`}
              >
                {f === "All" ? "All" : f + "s"}
              </button>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-16 md:py-24">
          <div className="divide-y divide-[#E8E8E8] border-y border-[#E8E8E8]">
            {items.map((r) => (
              <article key={r.title} className="kora-reveal grid gap-4 py-8 md:grid-cols-[180px_1fr_160px] md:items-start md:gap-8">
                <span className="inline-block w-fit bg-[#E8E8E8] px-3 py-1 text-[10px] font-bold uppercase tracking-[0.2em] text-[#0A0A0A]">{r.type}</span>
                <div>
                  <h2 className="text-lg font-bold text-[#0A0A0A]">{r.title}</h2>
                  <p className="mt-2 text-sm text-[#1A1A1A]">{r.description}</p>
                  <p className="mt-2 text-xs text-[#6B6B6B]">{r.authors} · {r.date}</p>
                </div>
                <a href="#" className="text-xs font-bold uppercase tracking-wider text-[#0A0A0A] hover:opacity-60 md:text-right">
                  Read Paper →
                </a>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24">
          <div className="kora-reveal max-w-3xl">
            <SectionLabel>Collaborate</SectionLabel>
            <h2 className="mt-4 text-3xl font-black tracking-[-0.03em] md:text-5xl">Collaborate With Us</h2>
            <p className="mt-6 text-lg text-[#ABABAB]">
              We work with researchers, universities, and institutions across Africa and globally. If you are interested in joint research, dataset partnerships, or co-authored publications, reach out.
            </p>
            <a href="mailto:research@koralab.org" className="mt-8 inline-block bg-white px-7 py-3.5 text-xs font-bold uppercase tracking-wider text-[#0A0A0A]">
              research@koralab.org
            </a>
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
