
# Kora Lab SEO Overhaul — koralab.org

Goal: rank Kora Lab at the top of both traditional search (Google) and AI-powered answer engines (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) for every keyword that maps to the lab's mission.

## 1. Canonical domain + global metadata fix

- Replace every `https://kora-lab.com` reference with `https://koralab.org` across the codebase:
  - `public/robots.txt` (sitemap URL)
  - `public/sitemap.xml` (all `<loc>` entries)
  - Per-route `head()` `og:url` + canonical links in `index.tsx`, `about.tsx`, `approach.tsx`, `research.tsx`, `blog.index.tsx`, `blog.$slug.tsx`, `contact.tsx`
  - JSON-LD `url` on home
- Add `<html lang="en">` confirmation in `__root.tsx` and `<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">` sitewide.
- Replace static `public/sitemap.xml` with a dynamic server route at `src/routes/sitemap[.]xml.ts` that auto-includes all routes + every blog slug from `blog-data.ts` (kept in sync forever).
- Move `robots.txt` to point at the new sitemap URL.

## 2. Keyword strategy (the terms we will own)

Group A — Identity / branded
- "kora lab", "koralab", "kora ai lab", "africa sovereign ai lab", "kheir lissi"

Group B — Mission / category
- "sovereign ai africa", "african ai lab", "african language models", "african llm", "ai research lab africa", "togo ai", "lome ai lab"

Group C — Institutional / policy
- "kigali declaration ai", "africa ai fund", "au continental ai strategy", "afdb ai 10 billion", "smart africa ai", "africa ai sovereignty"

Group D — Technical
- "african language dataset", "open african languages corpus", "swahili llm", "yoruba llm", "amharic llm", "low resource african nlp"

Group E — AI-search intent (long-tail questions)
- "who is building sovereign ai in africa", "what is the kigali declaration on ai", "best african ai research lab", "where is africa's ai infrastructure being built"

These get woven into headings, meta descriptions, and a new FAQ section (which doubles as FAQPage schema — heavily favored by AI answer engines).

## 3. Per-page metadata rewrite

Every route gets unique, keyword-rich, <60 char title and <160 char description, plus matching og:title / og:description / twitter:* and a canonical:

| Route | Title | Primary keywords |
|---|---|---|
| `/` | Kora Lab — Africa's Sovereign AI Lab | sovereign ai africa, african ai lab |
| `/approach` | Our Approach — Sovereign Models + Accessibility | african llm, accessibility ai |
| `/research` | Research — African Language Models & Datasets | african language dataset, african nlp |
| `/blog` | Blog — Sovereign AI Analysis from Africa | africa ai analysis, kigali declaration |
| `/blog/$slug` | {post.title} — Kora Lab | per-article |
| `/about` | About Kora Lab & Founder Kheir Lissi | kheir lissi, kora lab founder |
| `/contact` | Contact Kora Lab — Lome, Togo | contact kora lab |

## 4. Structured data (JSON-LD) — the AI-search multiplier

Add typed schemas so models can quote us verbatim:

- `__root.tsx`: `Organization` + `WebSite` (with `SearchAction` for sitelinks search box).
- `/` (home): `Organization` (expanded: founder, foundingDate, foundingLocation, sameAs links to social, knowsAbout array of all Group B–D keywords).
- `/about`: `Person` schema for Kheir Lissi (jobTitle, worksFor, knowsAbout, sameAs).
- `/blog/$slug`: `Article` schema (headline, datePublished, author, image, articleBody snippet, keywords).
- `/blog` and `/research`: `CollectionPage` + `ItemList`.
- New FAQ block on `/` and `/approach`: `FAQPage` schema (10–12 Q&A pairs mirroring Group E queries).
- `BreadcrumbList` on every non-home route.

## 5. New content surfaces for ranking

- **FAQ section on home + approach page** — directly answers the long-tail / AI-search questions in Group E. This is the single highest-leverage addition for AI answer engines.
- **"What is Kora Lab" hero subhead rewrite** — explicit one-sentence definition starting with the brand name (AI engines extract these).
- **`/glossary` (lightweight)** — short definitions: "Sovereign AI", "Kigali Declaration", "African Language Model", etc. Each becomes a `DefinedTerm` schema entry. Massive AI-search win for definitional queries.

## 6. Crawlability + performance

- `public/robots.txt`: explicitly allow GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, Applebot-Extended (opt-in to AI training/citation crawlers).
- Sitemap: add `<lastmod>`, `<changefreq>`, `<priority>` per URL.
- Add `prefetch` / `preconnect` for Google Fonts in `__root.tsx`.
- Confirm all images have descriptive `alt`, lazy-load below the fold, and any hero uses width/height attrs (CLS).
- Ensure semantic H1 (one per page), logical H2/H3 hierarchy.

## 7. Social / share previews

- Generate a single branded OG image (1200×630, black bg, white "KORA LAB" wordmark + tagline) at `public/og-default.jpg`.
- Wire `og:image` + `twitter:image` (absolute `https://koralab.org/og-default.jpg`) on each leaf route's `head()` — never on `__root.tsx`.
- `twitter:card = summary_large_image` everywhere.

## 8. Off-site signals checklist (delivered as a README note for the user)

Code can't do these — I'll include a `SEO.md` with the manual steps:
- Submit `https://koralab.org/sitemap.xml` to Google Search Console + Bing Webmaster.
- Verify domain (I'll add a placeholder meta tag slot in `__root.tsx` ready to receive the GSC verification string).
- List on: AU AI Strategy partner directories, Smart Africa, AfDB, GitHub org page, HuggingFace org page, LinkedIn company page, X/Twitter — each linking back to koralab.org with consistent NAP (name/address) to feed `sameAs`.
- Encourage backlinks from any institutional partner press releases.

## Technical details

Files to create:
- `src/routes/sitemap[.]xml.ts` (dynamic sitemap)
- `src/routes/glossary.tsx`
- `src/components/faq-section.tsx` (with embedded FAQPage JSON-LD)
- `public/og-default.jpg` (generated)
- `SEO.md` (manual steps)

Files to edit:
- `public/robots.txt` (AI crawlers + new sitemap URL)
- delete `public/sitemap.xml` (replaced by server route)
- `src/routes/__root.tsx` (sitewide meta defaults, Organization + WebSite JSON-LD, GSC verification slot, font preconnect)
- `src/routes/index.tsx` (new title/desc, expanded Organization schema, FAQ section, hero microcopy)
- `src/routes/about.tsx` (Person schema, BreadcrumbList)
- `src/routes/approach.tsx` (FAQ, BreadcrumbList, metadata)
- `src/routes/research.tsx`, `src/routes/blog.index.tsx` (CollectionPage + ItemList, metadata)
- `src/routes/blog.$slug.tsx` (Article schema with author/datePublished/image, BreadcrumbList)
- `src/routes/contact.tsx` (metadata, ContactPage schema)

No copy will use em dashes (existing project rule respected).

Will run the SEO scanner after the changes and address any remaining findings.
