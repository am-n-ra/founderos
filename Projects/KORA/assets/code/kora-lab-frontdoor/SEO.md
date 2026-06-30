# Kora Lab — SEO & Discoverability Checklist

This document covers the off-site actions needed to fully realize the on-site SEO work shipped in the codebase. The code-side foundations (per-route metadata, JSON-LD structured data, dynamic sitemap, robots policy, AI-crawler allowlist, FAQ schema, glossary, branded OG image) are all in place. The items below require action outside the repository.

## 1. Submit to search engines (do this first)

1. **Google Search Console** — https://search.google.com/search-console
   - Add property: `https://koralab.org`
   - Verify ownership via DNS TXT record (preferred) or HTML meta tag. If you choose the meta-tag method, paste the tag content into a new `{ name: "google-site-verification", content: "..." }` entry in `src/routes/__root.tsx` head meta.
   - Submit sitemap: `https://koralab.org/sitemap.xml`
   - Request indexing of: `/`, `/approach`, `/research`, `/blog`, `/about`, `/glossary`, `/contact`

2. **Bing Webmaster Tools** — https://www.bing.com/webmasters
   - Import directly from Google Search Console (one click)
   - This also feeds ChatGPT and Copilot search.

3. **IndexNow** (optional but fast) — once on Bing Webmaster, push new URLs the moment you publish a blog post.

## 2. Build authoritative backlinks

Search ranking and AI-citation quality are dominated by who links to you. Get listed on:

- **Smart Africa** member directory
- **African Union AI Strategy** partner / contributor pages
- **AfDB** AI initiative project pages
- **Crunchbase** (create Kora Lab organization profile, link to koralab.org)
- **LinkedIn Company Page** for Kora Lab (link in About → Website)
- **GitHub Organization** `koralab` (pin a public repo, link homepage)
- **Hugging Face Organization** `koralab` (publish the Open African Languages Corpus v0.1, link homepage)
- **arXiv** when working papers are released, with author affiliation "Kora Lab, Lome, Togo"
- **Wikipedia** — once there are 3+ independent secondary sources, create or seed a Kora Lab article and a Kheir Lissi article (do not self-edit; use Articles for Creation)

## 3. Wire social handles into the JSON-LD `sameAs`

Once social presences exist, add their URLs to the `sameAs` array of the Organization schema in `src/routes/index.tsx` and the Person schema in `src/routes/about.tsx`. Suggested handles:

- `https://twitter.com/koralab` (and `/kheirlissi`)
- `https://linkedin.com/company/koralab`
- `https://github.com/koralab`
- `https://huggingface.co/koralab`
- `https://youtube.com/@koralab`

`sameAs` is the single highest-leverage entity-disambiguation signal for both Google's Knowledge Graph and AI answer engines.

## 4. Press, PR, and earned mentions

AI answer engines (ChatGPT, Perplexity, Claude, Gemini) cite Kora Lab when reputable third-party publications mention "Kora Lab" alongside the key phrases ("Africa's sovereign AI lab", "Kigali Declaration", "Kheir Lissi"). Pitch:

- **TechCabal, Rest of World, Semafor Africa, The Continent, Jeune Afrique** — African tech press
- **MIT Technology Review, Wired, The Verge** — AI press
- **Reuters Africa, AFP, Bloomberg Africa** — wire services
- **Ventures Africa, Disrupt Africa** — startup/funding press

Provide each with the press contact email and a one-page background brief.

## 5. Domain configuration

- Ensure `koralab.org` and `www.koralab.org` both serve the site, with one canonical (the `<link rel="canonical">` tags emitted by every route already point at the non-www apex).
- Configure 301 redirect from any legacy domain (`kora-lab.com`) to `https://koralab.org/{path}` so existing backlinks consolidate authority.
- Enforce HTTPS sitewide.

## 6. Ongoing publishing cadence

Every new blog post and research item:
1. Is automatically added to `/sitemap.xml` (dynamic route reads from `src/lib/blog-data.ts` and `src/lib/research-data.ts`).
2. Gets its own Article schema via `src/routes/blog.$slug.tsx`.
3. Should be cross-posted (canonical link back) to LinkedIn Articles and Medium where appropriate.

A consistent publishing rhythm (one substantive post every 2–3 weeks) is the single strongest ongoing signal to both Google and AI engines that the site is an active authority on the topic.

## 7. Quick sanity-check commands

After deploy:

- View structured data: paste any URL into https://search.google.com/test/rich-results
- View AI/social previews: https://www.opengraph.xyz/url/https%3A%2F%2Fkoralab.org
- Verify sitemap: open https://koralab.org/sitemap.xml
- Verify robots: open https://koralab.org/robots.txt
