import { SectionLabel } from "@/components/site-layout";

export type FaqItem = { q: string; a: string };

export function FaqSection({
  label = "FAQ",
  heading,
  items,
  theme = "light",
}: {
  label?: string;
  heading: string;
  items: FaqItem[];
  theme?: "light" | "dark";
}) {
  const isDark = theme === "dark";
  const bg = isDark ? "bg-[#0A0A0A]" : "bg-white";
  const text = isDark ? "text-white" : "text-[#0A0A0A]";
  const muted = isDark ? "text-[#ABABAB]" : "text-[#1A1A1A]";
  const divider = isDark ? "border-[#1A1A1A]" : "border-[#E8E8E8]";

  return (
    <section className={`${bg} ${text}`}>
      <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
        <div className="kora-reveal">
          <SectionLabel>{label}</SectionLabel>
          <h2 className={`mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] md:text-5xl ${text}`}>
            {heading}
          </h2>
        </div>
        <div className={`mt-12 divide-y border-y ${divider}`}>
          {items.map((it) => (
            <details key={it.q} className="kora-reveal group py-6">
              <summary className={`flex cursor-pointer items-start justify-between gap-6 text-lg font-bold tracking-[-0.01em] md:text-xl ${text}`}>
                <span>{it.q}</span>
                <span className={`shrink-0 text-2xl font-black ${muted} transition-transform group-open:rotate-45`}>+</span>
              </summary>
              <p className={`mt-4 max-w-3xl text-base leading-relaxed ${muted}`}>{it.a}</p>
            </details>
          ))}
        </div>
      </div>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            mainEntity: items.map((it) => ({
              "@type": "Question",
              name: it.q,
              acceptedAnswer: { "@type": "Answer", text: it.a },
            })),
          }),
        }}
      />
    </section>
  );
}
