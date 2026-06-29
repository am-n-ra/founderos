import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import { SiteLayout, SectionLabel } from "@/components/site-layout";

const SITE_URL = "https://koralab.org";
const PRODUCT_PATH = "/resources/guides/parent-ia";

// =============================================================
// CHARIOW SNAP WIDGET INTEGRATION
// =============================================================
// 1. Go to Chariow dashboard > Products > Votre enfant face a l'IA > Snap.
// 2. Copy the full HTML snippet Chariow gives you (it contains a <div>
//    placeholder + a <script src="https://...chariow..."></script> line).
// 3. Paste the snippet between the backticks below — that's it. The page
//    will mount the widget where it sees CHARIOW_MOUNT_ID, and the floating
//    Buy buttons will trigger it. Keep the snippet exactly as Chariow
//    provides; do not edit attributes.
// 4. Optional: set CHARIOW_CHECKOUT_URL to your hosted Chariow checkout
//    link as a fallback for users on browsers that block third-party scripts.
//    The ?ref=CODE query is appended automatically.
// =============================================================
const CHARIOW_PRODUCT_ID = "prd_d5vsf5lh";
const CHARIOW_AFFILIATE_ID = "prd_5xn05el3";
const CHARIOW_STORE = "vknmhcsb.mychariow.shop";
const CHARIOW_SNAP_HTML = `<!-- Chariow Widget -->
<div id="chariow-widget" data-product-id="${CHARIOW_PRODUCT_ID}"
    data-store-domain="${CHARIOW_STORE}"
    data-style="tap"
    data-border-style="rounded"
    data-cta-width="xs"
    data-background-color="#FFFFFF"
    data-cta-animation="shine"
    data-locale="en"
    data-primary-color="#ffcc00"></div>
<script>
(function() {
  var script = document.createElement('script');
  script.src = 'https://js.chariowcdn.com/v1/widget.min.js';
  script.async = true;
  document.head.appendChild(script);

  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = 'https://js.chariowcdn.com/v1/widget.min.css';
  document.head.appendChild(link);
})();
</script>`;
const CHARIOW_CHECKOUT_URL = `https://${CHARIOW_STORE}/${CHARIOW_PRODUCT_ID}`;
const CHARIOW_AFFILIATE_URL = `https://${CHARIOW_STORE}/${CHARIOW_AFFILIATE_ID}`;
const CHARIOW_MOUNT_ID = "chariow-widget";

export const Route = createFileRoute("/resources/guides/parent-ia")({
  component: ParentIaPage,
  head: () => ({
    meta: [
      { title: "Votre enfant face a l'IA | Kora Lab" },
      {
        name: "description",
        content:
          "Le guide que chaque parent africain doit lire en 2026. 15 competences, outils IA gratuits, protocole anti-deepfake, et programme de 100 jours. Par Kheir Lissi, Kora Lab.",
      },
      { name: "keywords", content: "IA enfants Afrique, parent IA, guide IA famille, deepfake enfant, tutorat IA Afrique, ChatGPT enfants, Kora Lab, Kheir Lissi" },
      { property: "og:title", content: "Votre enfant face a l'IA | Kora Lab" },
      {
        property: "og:description",
        content:
          "Le guide que chaque parent africain doit lire en 2026. 15 competences, outils IA gratuits, et programme de 100 jours.",
      },
      { property: "og:type", content: "product" },
      { property: "og:url", content: `${SITE_URL}${PRODUCT_PATH}` },
      { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
      { name: "twitter:title", content: "Votre enfant face a l'IA | Kora Lab" },
      {
        name: "twitter:description",
        content: "Le guide que chaque parent africain doit lire en 2026.",
      },
      { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
    ],
    links: [{ rel: "canonical", href: `${SITE_URL}${PRODUCT_PATH}` }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          name: "Votre enfant face a l'IA",
          description:
            "Le guide que chaque parent africain doit lire en 2026. 15 competences, outils IA gratuits, et programme de 100 jours.",
          brand: { "@type": "Organization", name: "Kora Lab" },
          author: { "@type": "Person", name: "Kheir Lissi" },
          offers: {
            "@type": "Offer",
            price: "19900",
            priceCurrency: "XOF",
            url: `${SITE_URL}${PRODUCT_PATH}`,
            availability: "https://schema.org/InStock",
          },
        }),
      },
    ],
  }),
});

const INSIDE = [
  "L'etat de l'IA en mai 2026 : GPT-5.5, Claude 4.7, Gemini 3.1 Pro, DeepSeek V4",
  "Les metiers en Afrique : donnees reelles de l'OIT, McKinsey, et la Banque Mondiale",
  "Securite familiale : protocole anti-deepfake et clonage vocal",
  "15 competences que l'IA ne peut pas reproduire, avec des activites par age",
  "La boite a outils IA : 9 outils gratuits avec strategie de rotation",
  "Le calendrier des 100 jours : une action par jour, entierement detaillee",
];

const TOC = [
  { n: "01", t: "Pourquoi ce guide, maintenant", p: "p. 4" },
  { n: "02", t: "L'etat de l'IA en mai 2026", p: "p. 12" },
  { n: "03", t: "Les metiers en Afrique d'ici 2035", p: "p. 28" },
  { n: "04", t: "Securite familiale et deepfakes", p: "p. 44" },
  { n: "05", t: "15 competences profondement humaines", p: "p. 58" },
  { n: "06", t: "Boite a outils : 9 outils gratuits", p: "p. 92" },
  { n: "07", t: "Le programme de 100 jours", p: "p. 110" },
  { n: "08", t: "Devenir partenaire Kora Lab", p: "p. 148" },
];

const SAMPLE_EXCERPT = `Trois secondes. C'est ce qu'il faut a un modele de clonage vocal grand public, en mai 2026, pour reproduire la voix de votre enfant avec une fidelite suffisante pour tromper un grand-parent au telephone. Trois secondes prelevees sur une story Instagram, un message WhatsApp transfere, ou une video TikTok publique.

La premiere reaction d'un parent est generalement de vouloir tout effacer. C'est la mauvaise reaction. Vos enfants vivront leur vie sociale en ligne, comme la votre se vit en partie hors ligne. La bonne reaction est de construire, en famille, un protocole simple qui rend le clonage inutile.

Ce protocole tient en une phrase : un mot de passe verbal partage que personne en dehors du foyer ne connait. Pas un mot complique. Un mot anodin, choisi ensemble, et change tous les six mois. Si un appel arrive avec la voix de votre enfant en detresse, vous demandez le mot. Pas de mot, pas d'action.`;

const STATS = [
  {
    n: "2 ans",
    label: "de progres scolaire en 6 semaines grace au tutorat IA",
    source: "Banque Mondiale, Nigeria",
  },
  {
    n: "+56 %",
    label: "de salaire en plus pour les travailleurs qui maitrisent l'IA",
    source: "PwC",
  },
  {
    n: "97 %",
    label: "des parents craignent l'impact de l'IA sur la carriere de leur enfant",
    source: "Zety",
  },
];

const FAQ = [
  {
    q: "C'est pour quel age ?",
    a: "Le guide couvre les 3-7 ans, 8-12 ans, 13-17 ans, et les jeunes adultes de 18 ans et plus. Chaque activite est adaptee par tranche d'age.",
  },
  {
    q: "J'ai besoin de competences techniques ?",
    a: "Non. Le guide est ecrit pour des parents sans formation technique. Tous les outils recommandes sont gratuits et les tutoriels sont pas a pas.",
  },
  {
    q: "Comment je recois le guide ?",
    a: "Immediatement apres le paiement, par email. Le guide est un fichier PDF optimise pour la lecture sur telephone.",
  },
  {
    q: "Comment fonctionne le lien partenaire ?",
    a: "Inscrivez-vous gratuitement sur affiliate.chariow.com, recuperez votre lien personnalise, et partagez-le. Chaque achat via votre lien rapporte 2 970 FCFA (30 % de commission). Les gains sont verses sur votre Mobile Money chaque mois.",
  },
  {
    q: "Qui est Kheir Lissi ?",
    a: "Ingenieur en IA et fondateur de Kora Lab, un laboratoire de recherche en intelligence artificielle base a Lome, au Togo. Ce guide est la premiere publication du laboratoire.",
  },
];

const REF_STORAGE_KEY = "koralab_ref_code";

function useRefCode() {
  const [refCode, setRefCode] = useState("");

  useEffect(() => {
    try {
      const url = new URL(window.location.href);
      const fromUrl = url.searchParams.get("ref");
      const stored = localStorage.getItem(REF_STORAGE_KEY);
      const code = fromUrl || stored || "";
      if (fromUrl) {
        localStorage.setItem(REF_STORAGE_KEY, fromUrl);
      }
      if (code) setRefCode(code);
    } catch {
      // ignore
    }
  }, []);

  const update = (val: string) => {
    setRefCode(val);
    try {
      if (val) localStorage.setItem(REF_STORAGE_KEY, val);
      else localStorage.removeItem(REF_STORAGE_KEY);
    } catch {
      // ignore
    }
  };

  return { refCode, setRefCode: update };
}

function ChariowMount() {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!CHARIOW_SNAP_HTML || !ref.current) return;
    ref.current.innerHTML = CHARIOW_SNAP_HTML;
    const scripts = Array.from(ref.current.querySelectorAll("script"));
    scripts.forEach((old) => {
      const s = document.createElement("script");
      Array.from(old.attributes).forEach((a) => s.setAttribute(a.name, a.value));
      s.text = old.text;
      old.parentNode?.replaceChild(s, old);
    });
  }, []);
  if (!CHARIOW_SNAP_HTML) return null;
  return <div ref={ref} className="kora-reveal mt-10" />;
}

function buyClick(ref: string) {
  if (typeof window === "undefined") return;
  // With ref: open affiliate checkout in new tab
  if (ref) {
    const url = `${CHARIOW_AFFILIATE_URL}?ref=${encodeURIComponent(ref)}`;
    window.open(url, "_blank", "noopener,noreferrer");
    return;
  }
  // Without ref: scroll to inline widget (direct product 19 900 FCFA)
  if (CHARIOW_SNAP_HTML) {
    const el = document.getElementById(CHARIOW_MOUNT_ID);
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      return;
    }
  }
  window.open(CHARIOW_CHECKOUT_URL, "_blank", "noopener,noreferrer");
}

function scrollToPreview() {
  if (typeof window === "undefined") return;
  window.open(CHARIOW_CHECKOUT_URL, "_blank", "noopener,noreferrer");
}

function ParentIaPage() {
  const { refCode, setRefCode } = useRefCode();
  const hasRef = refCode.trim().length > 0;

  return (
    <SiteLayout>
      {/* HERO */}
      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:py-28">
          <div className="kora-reveal">
            <SectionLabel>Guide Kora Lab</SectionLabel>
            <h1 className="mt-4 max-w-3xl text-5xl font-black leading-[1.02] tracking-[-0.03em] md:text-7xl">
              Votre enfant face a l'IA
            </h1>
            <p className="mt-6 max-w-2xl text-lg text-[#ABABAB] md:text-xl">
              Le guide que chaque parent africain doit lire en 2026.
            </p>
            <p className="mt-3 text-sm uppercase tracking-[0.2em] text-[#6B6B6B]">
              Par Kheir Lissi, fondateur de Kora Lab
            </p>
            <div className="kora-reveal mt-8 flex flex-wrap gap-3">
              <button
                type="button"
                onClick={scrollToPreview}
                className="inline-block border border-white px-6 py-3 text-xs font-bold uppercase tracking-wider text-white transition-colors hover:bg-white hover:text-[#0A0A0A]"
              >
                Apercu du guide
              </button>
              <button
                type="button"
                onClick={() => buyClick(refCode)}
                className="inline-block bg-white px-6 py-3 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] transition-opacity hover:opacity-80"
              >
                {hasRef ? "Acheter a 9 900 FCFA" : "Acheter le guide"}
              </button>
            </div>
          </div>

          {/* PRICING */}
          <div className="mt-12 grid gap-6 md:grid-cols-2">
            {/* Standard */}
            <div
              className={`kora-reveal flex flex-col border bg-[#111] p-8 ${
                hasRef ? "border-[#1A1A1A] opacity-70" : "border-[#1A1A1A]"
              }`}
            >
              <p className="text-[9px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">Prix standard</p>
              <p className="mt-4 text-4xl font-black tracking-[-0.02em] text-white">
                {hasRef ? <span className="line-through opacity-50">19 900 FCFA</span> : "19 900 FCFA"}
              </p>
              <p className="mt-3 text-sm text-[#ABABAB]">PDF, livraison immediate par email.</p>
              <button
                type="button"
                onClick={() => buyClick("")}
                className="mt-auto pt-8 text-left"
              >
                <span className="inline-block bg-white px-6 py-3 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] transition-opacity hover:opacity-80">
                  Acheter le guide
                </span>
              </button>
            </div>

            {/* Partner */}
            <div className="kora-reveal relative flex flex-col border-2 border-white bg-white p-8 text-[#0A0A0A]">
              <span className="absolute -top-3 left-8 bg-[#0A0A0A] px-2.5 py-1 text-[9px] font-bold uppercase tracking-[0.3em] text-white">
                Recommande
              </span>
              <p className="text-[9px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">
                Prix avec lien partenaire
              </p>
              <p className="mt-4 text-4xl font-black tracking-[-0.02em]">9 900 FCFA</p>
              <p className="mt-3 text-sm text-[#1A1A1A]">Vous avez un code partenaire ?</p>
              <input
                type="text"
                value={refCode}
                onChange={(e) => setRefCode(e.target.value)}
                placeholder="Entrez votre code"
                className="mt-3 w-full border border-[#0A0A0A] bg-white px-4 py-3 text-sm text-[#0A0A0A] placeholder:text-[#6B6B6B] focus:outline-none"
              />
              <button
                type="button"
                onClick={() => buyClick(refCode)}
                className="mt-6 text-left"
              >
                <span className="inline-block bg-[#0A0A0A] px-6 py-3 text-xs font-bold uppercase tracking-wider text-white transition-opacity hover:opacity-80">
                  Acheter a 9 900 FCFA
                </span>
              </button>
            </div>
          </div>

          <p className="kora-reveal mt-8 max-w-2xl text-sm text-[#ABABAB]">
            Inscrivez-vous gratuitement sur affiliate.chariow.com et gagnez 2 970 FCFA par vente.
          </p>
        </div>
      </section>

      {/* PREVIEW */}
      <section id="preview" className="bg-white text-[#0A0A0A]">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal">
            <SectionLabel>Apercu du guide</SectionLabel>
            <h2 className="mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] md:text-5xl">
              Regardez avant d'acheter.
            </h2>
            <p className="mt-6 max-w-2xl text-base text-[#1A1A1A] md:text-lg">
              Voici la table des matieres complete et un extrait integral du chapitre sur la securite familiale.
            </p>
          </div>

          <div className="mt-12 grid gap-8 md:grid-cols-2">
            {/* TOC mock page */}
            <div className="relative border border-[#0A0A0A] bg-[#F7F5F1] p-10 shadow-[12px_12px_0_0_#0A0A0A]">
              <div className="flex items-start justify-between border-b border-[#0A0A0A] pb-6">
                <div>
                  <p className="text-[9px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">Kora Lab Guides</p>
                  <p className="mt-2 text-lg font-black tracking-[-0.02em]">Votre enfant face a l'IA</p>
                </div>
                <span className="text-[10px] uppercase tracking-[0.25em] text-[#6B6B6B]">2026</span>
              </div>
              <p className="mt-6 text-[10px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">
                Table des matieres
              </p>
              <ul className="mt-4 divide-y divide-[#0A0A0A]/15">
                {TOC.map((row) => (
                  <li key={row.n} className="flex items-baseline justify-between gap-4 py-3 text-sm">
                    <span className="flex items-baseline gap-3">
                      <span className="text-[10px] font-bold tabular-nums text-[#6B6B6B]">{row.n}</span>
                      <span className="font-medium text-[#0A0A0A]">{row.t}</span>
                    </span>
                    <span className="text-[10px] uppercase tracking-[0.2em] text-[#6B6B6B]">{row.p}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Sample chapter mock page */}
            <div className="relative border border-[#0A0A0A] bg-[#F7F5F1] p-10 shadow-[12px_12px_0_0_#0A0A0A]">
              <div className="flex items-start justify-between border-b border-[#0A0A0A] pb-6">
                <div>
                  <p className="text-[9px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">Chapitre 4 / Extrait</p>
                  <p className="mt-2 text-lg font-black tracking-[-0.02em]">Trois secondes</p>
                </div>
                <span className="text-[10px] uppercase tracking-[0.25em] text-[#6B6B6B]">p. 44</span>
              </div>
              <div className="mt-6 space-y-4 text-[14px] leading-relaxed text-[#0A0A0A]">
                {SAMPLE_EXCERPT.split("\n\n").map((p) => (
                  <p key={p.slice(0, 24)}>{p}</p>
                ))}
              </div>
              <p className="mt-6 border-t border-[#0A0A0A]/20 pt-4 text-[10px] uppercase tracking-[0.25em] text-[#6B6B6B]">
                Extrait. Le chapitre complet contient le protocole, le script d'appel, et 4 cas reels.
              </p>
            </div>
          </div>

          <div className="mt-10 flex flex-wrap items-center gap-4">
            <button
              type="button"
              onClick={() => buyClick(refCode)}
              className="inline-block bg-[#0A0A0A] px-6 py-3 text-xs font-bold uppercase tracking-wider text-white transition-opacity hover:opacity-80"
            >
              {hasRef ? "Acheter a 9 900 FCFA" : "Acheter le guide"}
            </button>
            <p className="text-xs text-[#6B6B6B]">Livraison immediate par email.</p>
          </div>

          {/* Chariow Snap inline checkout (renders only when CHARIOW_SNAP_HTML is set) */}
          <ChariowMount />
        </div>
      </section>

      {/* WHAT'S INSIDE */}
      <section className="bg-white text-[#0A0A0A]">
        <div className="mx-auto max-w-[1100px] px-6 pb-24 md:pb-32">
          <div className="kora-reveal">
            <SectionLabel>Ce que contient le guide</SectionLabel>
            <h2 className="mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] md:text-5xl">
              Tout ce dont vous avez besoin, en un seul document.
            </h2>
          </div>
          <ul className="mt-12 grid gap-px border border-[#E8E8E8] bg-[#E8E8E8] md:grid-cols-2">
            {INSIDE.map((item, i) => (
              <li
                key={item}
                className="kora-reveal flex gap-4 bg-white p-6"
              >
                <span className="text-xs font-bold tabular-nums text-[#6B6B6B]">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <p className="text-base leading-relaxed text-[#0A0A0A]">{item}</p>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* STATS */}
      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal">
            <SectionLabel>Les chiffres</SectionLabel>
            <h2 className="mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] md:text-5xl">
              Pourquoi ce guide, maintenant.
            </h2>
          </div>
          <div className="mt-12 grid gap-px border border-[#1A1A1A] bg-[#1A1A1A] md:grid-cols-3">
            {STATS.map((s) => (
              <div key={s.n} className="kora-reveal flex flex-col bg-[#0A0A0A] p-8">
                <p className="text-5xl font-black tracking-[-0.03em] text-white md:text-6xl">{s.n}</p>
                <p className="mt-4 text-base leading-relaxed text-[#ABABAB]">{s.label}</p>
                <p className="mt-4 text-[10px] uppercase tracking-[0.25em] text-[#6B6B6B]">{s.source}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="bg-white text-[#0A0A0A]">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal">
            <SectionLabel>FAQ</SectionLabel>
            <h2 className="mt-4 max-w-3xl text-4xl font-black tracking-[-0.03em] md:text-5xl">
              Questions frequentes.
            </h2>
          </div>
          <div className="mt-12 divide-y border-y border-[#E8E8E8]">
            {FAQ.map((it) => (
              <details key={it.q} className="kora-reveal group py-6">
                <summary className="flex cursor-pointer items-start justify-between gap-6 text-lg font-bold tracking-[-0.01em] md:text-xl">
                  <span>{it.q}</span>
                  <span className="shrink-0 text-2xl font-black text-[#6B6B6B] transition-transform group-open:rotate-45">
                    +
                  </span>
                </summary>
                <p className="mt-4 max-w-3xl text-base leading-relaxed text-[#1A1A1A]">{it.a}</p>
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
              mainEntity: FAQ.map((it) => ({
                "@type": "Question",
                name: it.q,
                acceptedAnswer: { "@type": "Answer", text: it.a },
              })),
            }),
          }}
        />
      </section>

      {/* FINAL CTA */}
      <section className="bg-[#0A0A0A] text-white">
        <div className="mx-auto max-w-[1100px] px-6 py-24 md:py-32">
          <div className="kora-reveal flex flex-col items-start gap-8 border border-[#1A1A1A] bg-[#111] p-10 md:flex-row md:items-center md:justify-between md:p-14">
            <div className="max-w-xl">
              <h2 className="text-3xl font-black tracking-[-0.02em] md:text-4xl">
                Pret a commencer ?
              </h2>
              <p className="mt-4 text-base text-[#ABABAB]">
                Ce guide est cree par Kora Lab, le laboratoire souverain d'IA de l'Afrique.
              </p>
              <Link to="/blog/$slug" params={{ slug: "votre-enfant-face-a-lia-guide-parent-afrique-2026" }} className="mt-4 inline-block text-xs font-bold uppercase tracking-wider text-[#ABABAB] underline hover:text-white">
                Lire l'article du blog sur ce guide
              </Link>
            </div>
            <button
              type="button"
              onClick={() => buyClick(refCode)}
              className="inline-block bg-white px-8 py-4 text-xs font-bold uppercase tracking-wider text-[#0A0A0A] transition-opacity hover:opacity-80"
            >
              {hasRef ? "Acheter a 9 900 FCFA" : "Acheter le guide"}
            </button>
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
