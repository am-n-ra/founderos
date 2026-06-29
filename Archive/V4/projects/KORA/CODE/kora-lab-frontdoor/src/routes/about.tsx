import { createFileRoute } from "@tanstack/react-router";
import { SiteLayout, SectionLabel } from "@/components/site-layout";

const SITE_URL = "https://koralab.org";

export const Route = createFileRoute("/about")({
  component: AboutPage,
  head: () => ({
    meta: [
      { title: "About Kora Lab & Founder Kheir Lissi" },
      { name: "description", content: "Kora Lab is Africa's sovereign AI lab, founded by Kheir Lissi in Lome, Togo. Building the continent's own models, datasets, and research." },
      { property: "og:title", content: "About Kora Lab & Founder Kheir Lissi" },
      { property: "og:description", content: "Kheir Lissi, founder of Kora Lab, on building Africa's sovereign AI infrastructure from Lome, Togo." },
      { property: "og:url", content: `${SITE_URL}/about` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { property: "og:image:width", content: "1216" },
      { property: "og:image:height", content: "640" },
      { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
      { property: "og:type", content: "profile" },
      { name: "twitter:title", content: "About Kora Lab & Founder Kheir Lissi" },
      { name: "twitter:description", content: "Kheir Lissi, founder of Kora Lab." },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}/about` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Person",
          "@id": `${SITE_URL}/about#kheir-lissi`,
          name: "Kheir Lissi",
          jobTitle: "Founder of Kora Lab",
          worksFor: { "@type": "Organization", name: "Kora Lab", url: SITE_URL },
          nationality: { "@type": "Country", name: "Togo" },
          homeLocation: { "@type": "Place", name: "Lome, Togo" },
          knowsAbout: [
            "Artificial Intelligence",
            "African language models",
            "Sovereign AI",
            "Big data",
            "African AI policy",
            "Kigali Declaration on AI",
          ],
          sameAs: ["https://edenvallie.com", "https://koralab.org"],
          url: `${SITE_URL}/about`,
        }),
      },
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          itemListElement: [
            { "@type": "ListItem", position: 1, name: "Home", item: `${SITE_URL}/` },
            { "@type": "ListItem", position: 2, name: "About", item: `${SITE_URL}/about` },
          ],
        }),
      },
    ],
  }),
});

function AboutPage() {
  return (
    <SiteLayout>
      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <SectionLabel>The Founder</SectionLabel>
          <div className="mt-12 grid gap-12 md:grid-cols-[1fr_1.5fr] md:gap-20">
            <div className="kora-reveal">
              <h1 className="text-4xl font-black tracking-[-0.03em] md:text-6xl">KHEIR LISSI</h1>
              <p className="mt-6 text-sm font-bold uppercase tracking-[0.2em] text-[#6B6B6B]">Founder, Kora Lab</p>
              <p className="mt-2 text-sm text-[#6B6B6B]">Lome, Togo</p>
            </div>
            <div className="kora-reveal kora-prose text-base text-[#1A1A1A] md:text-lg">
              <p>
                I studied computer science with a specialization in AI and big data in college before making the deliberate decision to leave mid third year. The pace of academic training was incompatible with the speed at which the world was moving, and with the urgency of what I am building.
              </p>
              <p>
                I identified early that Africa's greatest risk in the AI era is not a lack of talent, but a lack of infrastructure, ownership, and narrative. Rather than waiting for the system to produce what Africa needs, I chose to build it directly.
              </p>
              <p>
                I am also the founder of edenvallie.com, an incubator for ADHD and neurodivergent entrepreneurs who have the vision but need the right ecosystem to execute.
              </p>
              <p className="font-bold text-[#0A0A0A]">
                I am not waiting for permission to build Africa's AI lab. I am building it.
              </p>
              <div className="mt-6 flex flex-wrap gap-6 text-sm font-bold uppercase tracking-wider">
                <a href="https://koralab.org" className="border-b border-[#0A0A0A] pb-1 text-[#0A0A0A]">koralab.org</a>
                <a href="https://edenvallie.com" className="border-b border-[#0A0A0A] pb-1 text-[#0A0A0A]">edenvallie.com</a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal max-w-3xl">
            <SectionLabel>The Mission</SectionLabel>
            <h2 className="mt-4 text-4xl font-black tracking-[-0.03em] md:text-6xl">Why Kora Lab Exists</h2>
          </div>
          <div className="kora-reveal kora-prose mt-12 max-w-3xl text-lg text-[#ABABAB]">
            <p>
              Africa stands at the most consequential technological inflection point in its modern history. Artificial intelligence will reshape labor, governance, education, finance, and culture across the continent within a decade. The question is not whether AI will arrive in Africa. It already has. The question is who builds it, who owns it, and whose worldview it encodes.
            </p>
            <p>
              Today, every frontier AI system in production is owned and governed by entities outside of Africa. African languages are largely absent from training data. African contexts are largely absent from evaluation benchmarks. African researchers are largely absent from the labs that set the global agenda. This is not a sustainable position for a continent of 1.4 billion people.
            </p>
            <p>
              Kora Lab exists to change that, on two axes simultaneously. The first axis is accessibility: meeting African users where they are with frontier AI tools that are adapted, affordable, and useful in their daily context. The second axis is sovereignty: building the African models, datasets, and research capacity that the continent will own outright.
            </p>
            <p>
              We are not duplicating the work of the African Union, the AfDB, Smart Africa, or any national digital strategy. We are completing it. The political will exists. The capital is being committed. What is missing is a focused technical lab capable of executing the vision at the level of code, models, and infrastructure.
            </p>
            <p>
              Kora Lab is that lab. Based in Lome, building for the continent, accountable to its mandate.
            </p>
          </div>
        </div>
      </section>

      <section className="bg-[#E8E8E8]">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal">
            <SectionLabel>The Team</SectionLabel>
            <h2 className="mt-4 text-4xl font-black tracking-[-0.03em] md:text-5xl">Advisors and Team</h2>
            <p className="mt-4 max-w-2xl text-base text-[#6B6B6B]">
              We are assembling a team of researchers, engineers, and institutional partners. Confirmed members will be announced here.
            </p>
          </div>
          <div className="mt-12 grid gap-px bg-[#0A0A0A] md:grid-cols-3">
            {[1, 2, 3].map((i) => (
              <div key={i} className="kora-reveal bg-[#E8E8E8] p-8">
                <p className="text-sm font-bold uppercase tracking-[0.2em] text-[#6B6B6B]">[Role]</p>
                <p className="mt-3 text-2xl font-black text-[#0A0A0A]">[Name]</p>
                <p className="mt-2 text-sm text-[#1A1A1A]">[Institution]</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
