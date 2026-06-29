import { createFileRoute, Link } from "@tanstack/react-router";
import { SiteLayout, SectionLabel } from "@/components/site-layout";
import { FaqSection } from "@/components/faq-section";
import { HOME_FAQ } from "@/lib/faq-data";
import { POSTS } from "@/lib/blog-data";
import { RESEARCH } from "@/lib/research-data";

const SITE_URL = "https://koralab.org";

export const Route = createFileRoute("/")({
  component: Index,
  head: () => ({
    meta: [
      { title: "Kora Lab | Africa's Sovereign AI Lab" },
      { name: "description", content: "Kora Lab is Africa's sovereign AI research and product lab. Building African language models, datasets, and accessibility tools from Lome, Togo." },
      { property: "og:title", content: "Kora Lab | Africa's Sovereign AI Lab" },
      { property: "og:description", content: "Africa's sovereign AI research and product lab. African language models, datasets, and continental research from Lome, Togo." },
      { property: "og:url", content: `${SITE_URL}/` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { property: "og:image:width", content: "1216" },
      { property: "og:image:height", content: "640" },
      { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
      { name: "twitter:title", content: "Kora Lab | Africa's Sovereign AI Lab" },
      { name: "twitter:description", content: "Africa's sovereign AI research and product lab." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Organization",
          "@id": `${SITE_URL}/#organization`,
          name: "Kora Lab",
          alternateName: ["Koralab", "Kora AI Lab"],
          url: SITE_URL,
          logo: `${SITE_URL}/og-default.jpg`,
          image: `${SITE_URL}/og-default.jpg`,
          description: "Africa's sovereign AI research and product lab. Builds African language models, open datasets, and accessibility tools for the continent.",
          foundingDate: "2025",
          founder: {
            "@type": "Person",
            name: "Kheir Lissi",
            jobTitle: "Founder",
            sameAs: ["https://edenvallie.com"],
          },
          areaServed: { "@type": "Continent", name: "Africa" },
          location: {
            "@type": "Place",
            name: "Lome, Togo",
            address: { "@type": "PostalAddress", addressLocality: "Lome", addressCountry: "TG" },
          },
          knowsAbout: [
            "Sovereign AI",
            "African language models",
            "African large language models",
            "African NLP",
            "Low-resource language AI",
            "Kigali Declaration on AI",
            "Africa AI Fund",
            "AU Continental AI Strategy",
            "AfDB AI 10 Billion Initiative",
            "Smart Africa",
            "AI sovereignty",
            "AI accessibility",
            "African datasets",
            "Swahili LLM",
            "Yoruba LLM",
            "Hausa LLM",
            "Amharic LLM",
          ],
          sameAs: [
            "https://koralab.org",
            "https://edenvallie.com",
          ],
          contactPoint: {
            "@type": "ContactPoint",
            email: "hello@kora-lab.com",
            contactType: "general inquiries",
            areaServed: "Worldwide",
            availableLanguage: ["en", "fr"],
          },
        }),
      },
    ],
  }),
});

function Index() {
  return (
    <SiteLayout>
      <Hero />
      <Ticker />
      <Definition />
      <Problem />
      <Moment />
      <Stats />
      <FaqSection
        label="Frequently Asked"
        heading="What People Ask About Kora Lab"
        items={HOME_FAQ}
      />
      <BlogPreview />
      <ResearchPreview />
      <ContactCTA />
    </SiteLayout>
  );
}

function Hero() {
  return (
    <section className="bg-[#0A0A0A] text-white">
      <div className="mx-auto max-w-[1100px] px-6 py-28 md:py-40">
        <h1 className="kora-reveal text-[44px] font-black leading-[1.02] tracking-[-0.03em] sm:text-6xl md:text-[80px]">
          <span className="block text-white">Africa doesn't just</span>
          <span className="block text-white">consume AI.</span>
          <span className="block text-[#ABABAB]">Africa builds AI.</span>
        </h1>
        <hr className="kora-reveal my-10 w-20 border-0 border-t border-white" />
        <p className="kora-reveal max-w-[640px] text-[18px] text-[#ABABAB]">
          Kora Lab is Africa's sovereign AI research and product lab. We build African language models, open datasets, and accessibility tools so the continent owns the AI systems that will define its future.
        </p>
        <div className="kora-reveal mt-10 flex flex-col gap-3 sm:flex-row">
          <Link to="/approach" className="bg-white px-7 py-3.5 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] transition-opacity hover:opacity-80">Our Approach</Link>
          <Link to="/contact" className="border border-white px-7 py-3.5 text-xs font-bold uppercase tracking-wider text-white transition-colors hover:bg-white hover:text-[#0A0A0A]">Contact the Founder</Link>
        </div>
      </div>
    </section>
  );
}

function Ticker() {
  const text = "54 NATIONS / $60B AFRICA AI FUND / AU CONTINENTAL AI STRATEGY / AFDB AI 10B INITIATIVE / DIGITAL TOGO 2025-2030 / SMART AFRICA / ONE FLAG / ";
  const repeated = text.repeat(6);
  return (
    <div className="overflow-hidden border-y border-[#1A1A1A] bg-[#0A0A0A] py-3">
      <div className="kora-marquee-track flex whitespace-nowrap">
        <span className="px-4 text-[13px] font-bold uppercase tracking-[2px] text-white">{repeated}</span>
        <span className="px-4 text-[13px] font-bold uppercase tracking-[2px] text-white">{repeated}</span>
      </div>
    </div>
  );
}

function Definition() {
  return (
    <section className="bg-white">
      <div className="mx-auto max-w-[1100px] px-6 py-20 md:py-24">
        <div className="kora-reveal">
          <SectionLabel>What is Kora Lab</SectionLabel>
          <p className="mt-6 max-w-3xl text-2xl font-bold leading-snug tracking-[-0.02em] text-[#0A0A0A] md:text-3xl">
            Kora Lab is Africa's sovereign AI lab, headquartered in Lome, Togo. We build the African language models, open datasets, and accessibility tools that the African Union Continental AI Strategy, the Kigali Declaration, and the $60 billion Africa AI Fund assume already exist.
          </p>
        </div>
      </div>
    </section>
  );
}

function Problem() {
  const items = [
    { title: "ACCESS GAP", body: "Frontier AI tools are built for Western users. African end users face language, UX, and affordability barriers that make these tools impractical in their context." },
    { title: "SOVEREIGNTY GAP", body: "All large-scale AI models and infrastructure are owned by non-African entities. Africa has no seat at the table in shaping the models that will define its future." },
    { title: "EXECUTION GAP", body: "Governments have signed declarations. Billions are pledged. The AU Continental AI Strategy is live. What is missing is a technical lab capable of executing the vision at ground level. That is what Kora Lab is." },
  ];
  return (
    <section className="bg-[#E8E8E8] text-[#0A0A0A]">
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="kora-reveal">
          <SectionLabel>The Problem</SectionLabel>
          <h2 className="mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] md:text-6xl">Africa Is Being Left Out of the AI Race</h2>
        </div>
        <div className="mt-16 grid gap-12 md:grid-cols-3 md:gap-10">
          {items.map((it) => (
            <div key={it.title} className="kora-reveal border-t border-[#0A0A0A] pt-6">
              <h3 className="text-base font-black uppercase tracking-wider">{it.title}</h3>
              <p className="mt-4 text-base leading-relaxed text-[#1A1A1A]">{it.body}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Moment() {
  const events = [
    { date: "APRIL 2025", text: "54 African nations sign the Africa Declaration on AI in Kigali. A $60 billion Africa AI Fund is announced." },
    { date: "FEBRUARY 2026", text: "The African Union and Google sign a landmark AI sovereignty partnership. The AfDB and UNDP launch the AI 10 Billion Initiative." },
    { date: "2025-2026", text: "Togo activates Digital Strategy 2025-2030. At least 15 African countries now have national AI roadmaps." },
    { date: "THE GAP", text: "All of this political will and capital exists without a unified technical lab to execute it. Kora Lab is that lab." },
  ];
  return (
    <section className="bg-[#0A0A0A] text-white">
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="kora-reveal">
          <SectionLabel>The Moment</SectionLabel>
          <h2 className="mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] text-white md:text-6xl">The Continent Has Spoken. Now It Needs Builders.</h2>
        </div>
        <div className="mt-16 divide-y divide-[#1A1A1A] border-y border-[#1A1A1A]">
          {events.map((e) => (
            <div key={e.date} className="kora-reveal grid gap-4 py-8 md:grid-cols-[220px_1fr] md:gap-12">
              <p className="bg-[#1A1A1A] px-4 py-2 text-xs font-bold uppercase tracking-[0.2em] text-[#ABABAB] md:self-start">{e.date}</p>
              <p className="text-lg leading-relaxed text-white md:text-xl">{e.text}</p>
            </div>
          ))}
        </div>
        <p className="kora-reveal mt-16 max-w-3xl text-xl italic leading-relaxed text-[#ABABAB] md:text-2xl">
          "We are not competing with these institutions. We are completing them."
        </p>
      </div>
    </section>
  );
}

function Stats() {
  const stats = [
    { n: "54", t: "Nations that signed the Kigali AI Declaration" },
    { n: "$60B", t: "Africa AI Fund pledged" },
    { n: "2,000+", t: "African languages almost entirely absent from frontier AI training data" },
    { n: "4%", t: "Africa's current share of the global AI workforce" },
  ];
  return (
    <section className="bg-white text-[#0A0A0A]">
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="grid gap-px bg-[#0A0A0A] sm:grid-cols-2">
          {stats.map((s) => (
            <div key={s.n} className="kora-reveal bg-white p-8 md:p-12">
              <p className="text-5xl font-black tracking-[-0.04em] text-[#0A0A0A] md:text-[56px]">{s.n}</p>
              <p className="mt-5 text-[11px] font-bold uppercase tracking-[0.2em] text-[#6B6B6B]">{s.t}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function BlogPreview() {
  return (
    <section className="bg-[#E8E8E8]">
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="kora-reveal">
          <SectionLabel>Latest Writing</SectionLabel>
          <h2 className="mt-4 text-4xl font-black tracking-[-0.03em] md:text-5xl">From the Kora Lab Blog</h2>
        </div>
        <div className="mt-12 grid gap-8 md:grid-cols-3">
          {POSTS.slice(0, 3).map((p) => (
            <article key={p.slug} className="kora-reveal flex flex-col border-t border-[#0A0A0A] bg-white p-6">
              <p className="text-[10px] font-bold uppercase tracking-[0.25em] text-[#6B6B6B]">{p.category}</p>
              <h3 className="mt-3 text-lg font-bold leading-tight text-[#0A0A0A]">{p.title}</h3>
              <p className="mt-3 flex-1 text-sm leading-relaxed text-[#1A1A1A]">{p.excerpt}</p>
              <p className="mt-4 text-xs text-[#6B6B6B]">{p.date} · {p.readTime}</p>
              <Link to="/blog/$slug" params={{ slug: p.slug }} className="mt-4 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] hover:opacity-60">
                Read Article →
              </Link>
            </article>
          ))}
        </div>
        <Link to="/blog" className="mt-10 inline-block text-xs font-bold uppercase tracking-wider text-[#0A0A0A] underline underline-offset-4">
          View All Articles
        </Link>
      </div>
    </section>
  );
}

function ResearchPreview() {
  return (
    <section className="bg-white">
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="kora-reveal">
          <SectionLabel>Research</SectionLabel>
          <h2 className="mt-4 text-4xl font-black tracking-[-0.03em] md:text-5xl">From the Lab</h2>
        </div>
        <div className="mt-12 divide-y divide-[#E8E8E8] border-y border-[#E8E8E8]">
          {RESEARCH.slice(0, 2).map((r) => (
            <div key={r.title} className="kora-reveal grid gap-4 py-8 md:grid-cols-[160px_1fr_140px] md:items-start md:gap-8">
              <span className="inline-block w-fit bg-[#E8E8E8] px-3 py-1 text-[10px] font-bold uppercase tracking-[0.2em] text-[#0A0A0A]">{r.type}</span>
              <div>
                <h3 className="text-lg font-bold text-[#0A0A0A]">{r.title}</h3>
                <p className="mt-2 text-sm text-[#1A1A1A]">{r.description}</p>
                <p className="mt-2 text-xs text-[#6B6B6B]">{r.date}</p>
              </div>
              <Link to="/research" className="text-xs font-bold uppercase tracking-wider text-[#0A0A0A] hover:opacity-60 md:text-right">
                Read Paper →
              </Link>
            </div>
          ))}
        </div>
        <Link to="/research" className="mt-10 inline-block text-xs font-bold uppercase tracking-wider text-[#0A0A0A] underline underline-offset-4">
          View All Research
        </Link>
      </div>
    </section>
  );
}

function ContactCTA() {
  return (
    <section className="bg-[#0A0A0A] text-white">
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="kora-reveal max-w-3xl">
          <h2 className="text-4xl font-black tracking-[-0.03em] md:text-6xl">Build With Us.</h2>
          <p className="mt-6 max-w-2xl text-base leading-relaxed text-[#ABABAB] md:text-lg">
            Whether you are a government, an institution, an investor, or a technical builder who believes in this mission, we want to hear from you.
          </p>
          <Link to="/contact" className="mt-10 inline-block bg-white px-8 py-3.5 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] transition-opacity hover:opacity-80">
            Get in Touch
          </Link>
        </div>
      </div>
    </section>
  );
}
