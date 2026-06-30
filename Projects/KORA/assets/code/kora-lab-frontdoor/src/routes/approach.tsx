import { createFileRoute } from "@tanstack/react-router";
import { SiteLayout, SectionLabel } from "@/components/site-layout";
import { FaqSection } from "@/components/faq-section";
import { APPROACH_FAQ } from "@/lib/faq-data";

const SITE_URL = "https://koralab.org";

export const Route = createFileRoute("/approach")({
  component: ApproachPage,
  head: () => ({
    meta: [
      { title: "Approach | Sovereign Models + Accessibility for Africa" },
      { name: "description", content: "Kora Lab's two-axis strategy: an accessibility layer that adapts frontier AI for African users and a sovereign model lab building African language LLMs." },
      { property: "og:title", content: "Approach | Sovereign Models + Accessibility for Africa" },
      { property: "og:description", content: "Two-axis strategy: African accessibility layer and sovereign African language model lab." },
      { property: "og:url", content: `${SITE_URL}/approach` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { property: "og:image:width", content: "1216" },
      { property: "og:image:height", content: "640" },
      { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
      { name: "twitter:title", content: "Approach | Kora Lab" },
      { name: "twitter:description", content: "A two-axis strategy for African AI sovereignty." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/approach` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          itemListElement: [
            { "@type": "ListItem", position: 1, name: "Home", item: `${SITE_URL}/` },
            { "@type": "ListItem", position: 2, name: "Approach", item: `${SITE_URL}/approach` },
          ],
        }),
      },
    ],
  }),
});

function ApproachPage() {
  return (
    <SiteLayout>
      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <SectionLabel>Approach</SectionLabel>
          <h1 className="kora-reveal mt-4 text-4xl font-black tracking-[-0.03em] md:text-6xl">
            A Two-Axis Strategy for Africa's AI Sovereignty
          </h1>
          <p className="kora-reveal mt-6 max-w-2xl text-lg text-[#ABABAB]">
            One axis makes frontier AI genuinely usable for African users today. The other builds the African models, datasets, and research capacity that the continent will own tomorrow.
          </p>
        </div>
      </section>

      <section>
        <div className="grid md:grid-cols-2">
          <div className="kora-reveal bg-[#0A0A0A] p-10 text-white md:p-16">
            <p className="text-7xl font-black text-[#1A1A1A] md:text-8xl">01</p>
            <h2 className="mt-6 text-2xl font-black uppercase tracking-wider md:text-3xl">Accessibility Layer</h2>
            <p className="mt-6 leading-relaxed text-[#ABABAB]">
              Making the latest AI from Anthropic, OpenAI, DeepMind, and others genuinely usable for African and global users. Culturally adapted, multilingual, no technical knowledge required. Data pipelines that create real jobs across the continent.
            </p>
          </div>
          <div className="kora-reveal bg-white p-10 text-[#0A0A0A] md:p-16">
            <p className="text-sm font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">Product types</p>
            <ul className="mt-6 space-y-4 text-base">
              <li className="border-b border-[#E8E8E8] pb-3">AI agents tailored to African workflows</li>
              <li className="border-b border-[#E8E8E8] pb-3">No-code interfaces for non-technical users</li>
              <li className="border-b border-[#E8E8E8] pb-3">Developer tooling for African builders</li>
              <li className="border-b border-[#E8E8E8] pb-3">African-language adaptations of frontier tools</li>
              <li>Data collection pipelines that create jobs</li>
            </ul>
          </div>
        </div>
      </section>

      <section>
        <div className="grid md:grid-cols-2">
          <div className="kora-reveal order-2 bg-white p-10 text-[#0A0A0A] md:order-1 md:p-16">
            <p className="text-sm font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">Activities</p>
            <ul className="mt-6 space-y-4 text-base">
              <li className="border-b border-[#E8E8E8] pb-3">African language dataset construction</li>
              <li className="border-b border-[#E8E8E8] pb-3">Model training and evaluation</li>
              <li className="border-b border-[#E8E8E8] pb-3">Open research publication</li>
              <li className="border-b border-[#E8E8E8] pb-3">Institutional and university partnerships</li>
              <li>AI safety research grounded in African contexts</li>
            </ul>
          </div>
          <div className="kora-reveal order-1 bg-[#0A0A0A] p-10 text-white md:order-2 md:p-16">
            <p className="text-7xl font-black text-[#1A1A1A] md:text-8xl">02</p>
            <h2 className="mt-6 text-2xl font-black uppercase tracking-wider md:text-3xl">Sovereign Model Lab</h2>
            <p className="mt-6 leading-relaxed text-[#ABABAB]">
              Building Africa's own large language and multimodal models. Trained on African languages, history, and contexts. Authored by African researchers. Owned by the continent. This is the technical execution of the Kigali Declaration.
            </p>
          </div>
        </div>
      </section>

      <section className="bg-[#E8E8E8]">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal">
            <SectionLabel>Institutional Alignment</SectionLabel>
            <h2 className="mt-4 text-4xl font-black tracking-[-0.03em] md:text-5xl">Aligned With Every Major African AI Mandate</h2>
          </div>
          <div className="mt-12 divide-y divide-[#0A0A0A] border-y border-[#0A0A0A]">
            {[
              ["African Union Continental AI Strategy", "Phase 1 active"],
              ["Smart Africa and Africa AI Council", "40 Heads of State board"],
              ["AfDB and UNDP AI 10 Billion Initiative", "$10B target by 2035"],
              ["Togo MENTD Digital Strategy 2025-2030", "World Bank IDA backed"],
              ["Africa AI Fund $60B", "Announced Kigali 2025"],
            ].map(([name, status]) => (
              <div key={name} className="kora-reveal grid gap-2 py-6 md:grid-cols-[1.5fr_1fr]">
                <p className="text-base font-bold text-[#0A0A0A] md:text-lg">{name}</p>
                <p className="text-sm text-[#1A1A1A] md:text-right">{status}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <FaqSection
        label="Approach FAQ"
        heading="How Kora Lab Builds"
        items={APPROACH_FAQ}
      />
    </SiteLayout>
  );
}
