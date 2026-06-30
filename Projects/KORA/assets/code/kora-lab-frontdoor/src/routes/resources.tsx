import { createFileRoute } from "@tanstack/react-router";
import { SiteLayout, SectionLabel } from "@/components/site-layout";

const GUIDE_CHECKOUT_URL = "https://vknmhcsb.mychariow.shop/prd_d5vsf5lh";

const SITE_URL = "https://koralab.org";

export const Route = createFileRoute("/resources")({
  component: ResourcesPage,
  head: () => ({
    meta: [
      { title: "Ressources | Kora Lab" },
      { name: "description", content: "Des guides pratiques par Kora Lab pour naviguer l'ere de l'IA." },
      { property: "og:title", content: "Ressources | Kora Lab" },
      { property: "og:description", content: "Des guides pratiques par Kora Lab pour naviguer l'ere de l'IA." },
      { property: "og:url", content: `${SITE_URL}/resources` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { name: "twitter:title", content: "Ressources | Kora Lab" },
      { name: "twitter:description", content: "Des guides pratiques par Kora Lab pour naviguer l'ere de l'IA." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/resources` }],
  }),
});

type Product = {
  slug: string;
  to: string;
  title: string;
  description: string;
  price: string;
  badge?: string;
};

const PRODUCTS: Product[] = [
  {
    slug: "parent-ia",
    to: "/resources/guides/parent-ia",
    title: "Votre enfant face a l'IA",
    description:
      "Le guide que chaque parent africain doit lire en 2026. 15 competences, des outils concrets, et un programme de 100 jours.",
    price: "19 900 FCFA",
    badge: "Nouveau",
  },
];

function ProductCard({ p }: { p: Product }) {
  return (
    <article className="kora-reveal group flex flex-col border border-[#1A1A1A] bg-[#0A0A0A] transition-colors hover:border-white">
      <div className="relative flex aspect-[4/3] items-center justify-center overflow-hidden border-b border-[#1A1A1A] bg-[#111]">
        {p.badge && (
          <span className="absolute left-4 top-4 bg-white px-2.5 py-1 text-[9px] font-bold uppercase tracking-[0.3em] text-[#0A0A0A]">
            {p.badge}
          </span>
        )}
        <div className="flex h-full w-full flex-col items-center justify-center px-8 text-center">
          <p className="text-[9px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">Kora Lab Guides</p>
          <h3 className="mt-4 text-2xl font-black leading-[1.05] tracking-[-0.02em] text-white">{p.title}</h3>
          <p className="mt-3 text-[10px] uppercase tracking-[0.25em] text-[#6B6B6B]">PDF / 2026</p>
        </div>
      </div>
      <div className="flex flex-1 flex-col p-6">
        <h2 className="text-xl font-black tracking-[-0.02em] text-white">{p.title}</h2>
        <p className="mt-3 text-sm leading-relaxed text-[#ABABAB]">{p.description}</p>
        <div className="mt-6 flex items-center justify-between border-t border-[#1A1A1A] pt-6">
          <span className="text-lg font-bold text-white">{p.price}</span>
          <a
            href={GUIDE_CHECKOUT_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block bg-white px-5 py-2.5 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] transition-opacity hover:opacity-80"
          >
            Voir l'apercu
          </a>
        </div>
      </div>
    </article>
  );
}

function ResourcesPage() {
  return (
    <SiteLayout>
      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal">
            <SectionLabel>Resources</SectionLabel>
            <h1 className="mt-4 max-w-3xl text-5xl font-black tracking-[-0.03em] md:text-7xl">
              Ressources
            </h1>
            <p className="mt-6 max-w-2xl text-lg text-[#ABABAB] md:text-xl">
              Des guides pratiques par Kora Lab pour naviguer l'ere de l'IA.
            </p>
          </div>
        </div>
      </section>

      <section className="bg-[#0A0A0A] pb-32 text-white">
        <div className="mx-auto max-w-[1100px] px-6">
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {PRODUCTS.map((p) => (
              <ProductCard key={p.slug} p={p} />
            ))}
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
