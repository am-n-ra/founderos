import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import { SiteLayout, SectionLabel } from "@/components/site-layout";
import { POSTS } from "@/lib/blog-data";

const SITE_URL = "https://koralab.org";

export const Route = createFileRoute("/blog/")({
  component: BlogIndex,
  head: () => ({
    meta: [
      { title: "Blog | Sovereign AI Analysis from Africa" },
      { name: "description", content: "Analysis, perspectives, and updates from Kora Lab on African AI sovereignty, the Kigali Declaration, African language models, and continental research." },
      { property: "og:title", content: "Blog | Sovereign AI Analysis from Africa" },
      { property: "og:description", content: "Analysis and perspectives from Kora Lab on sovereign AI in Africa." },
      { property: "og:url", content: `${SITE_URL}/blog` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { property: "og:image:width", content: "1216" },
      { property: "og:image:height", content: "640" },
      { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
      { name: "twitter:title", content: "Blog | Kora Lab" },
      { name: "twitter:description", content: "Sovereign AI analysis from Africa." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/blog` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Blog",
          name: "Kora Lab Blog",
          url: `${SITE_URL}/blog`,
          description: "Analysis and perspectives on sovereign AI in Africa.",
          publisher: { "@type": "Organization", name: "Kora Lab", url: SITE_URL },
          blogPost: POSTS.map((p) => ({
            "@type": "BlogPosting",
            headline: p.title,
            description: p.excerpt,
            author: { "@type": "Person", name: "Kheir Lissi" },
            datePublished: p.date,
            url: `${SITE_URL}/blog/${p.slug}`,
            articleSection: p.category,
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
            { "@type": "ListItem", position: 2, name: "Blog", item: `${SITE_URL}/blog` },
          ],
        }),
      },
    ],
  }),
});

const FILTERS = ["All", "Analysis", "Institutional", "Technical", "Updates"] as const;

function BlogIndex() {
  const [filter, setFilter] = useState<(typeof FILTERS)[number]>("All");
  const items = filter === "All" ? POSTS : POSTS.filter((p) => p.category === filter);

  return (
    <SiteLayout>
      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:py-28">
          <SectionLabel>Writing</SectionLabel>
          <h1 className="kora-reveal mt-4 text-4xl font-black tracking-[-0.03em] md:text-6xl">Writing</h1>
          <p className="kora-reveal mt-6 max-w-2xl text-lg text-[#6B6B6B]">
            Analysis, perspectives, and updates from Kora Lab on sovereign AI in Africa.
          </p>
        </div>
      </section>

      <section className="border-y border-[#E8E8E8]">
        <div className="mx-auto max-w-[1100px] px-6">
          <div className="flex flex-wrap gap-6 py-4">
            {FILTERS.map((f) => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`text-xs font-bold uppercase tracking-wider transition-colors ${filter === f ? "border-b border-[#0A0A0A] pb-1 text-[#0A0A0A]" : "text-[#6B6B6B] hover:text-[#0A0A0A]"}`}
              >
                {f}
              </button>
            ))}
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-16 md:py-24">
          <div className="grid gap-8 md:grid-cols-3">
            {items.map((p) => (
              <article key={p.slug} className="kora-reveal flex flex-col border-t border-[#0A0A0A] pt-6">
                <p className="text-[10px] font-bold uppercase tracking-[0.25em] text-[#6B6B6B]">{p.category}</p>
                <h2 className="mt-3 text-xl font-bold leading-tight text-[#0A0A0A]">{p.title}</h2>
                <p className="mt-3 flex-1 text-sm leading-relaxed text-[#1A1A1A]">{p.excerpt}</p>
                <p className="mt-4 text-xs text-[#6B6B6B]">Kheir Lissi · {p.date} · {p.readTime}</p>
                <Link to="/blog/$slug" params={{ slug: p.slug }} className="mt-3 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] hover:opacity-60">
                  Read →
                </Link>
              </article>
            ))}
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
