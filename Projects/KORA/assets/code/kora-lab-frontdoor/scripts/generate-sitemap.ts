import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectRoot = path.resolve(__dirname, "..");

const BASE_URL = "https://koralab.org";

interface SitemapEntry {
  path: string;
  lastmod?: string;
  changefreq?: "always" | "hourly" | "daily" | "weekly" | "monthly" | "yearly" | "never";
  priority?: string;
}

const today = new Date().toISOString().slice(0, 10);

const staticEntries: SitemapEntry[] = [
  { path: "/", changefreq: "weekly", priority: "1.0", lastmod: today },
  { path: "/approach", changefreq: "monthly", priority: "0.9", lastmod: today },
  { path: "/research", changefreq: "weekly", priority: "0.9", lastmod: today },
  { path: "/blog", changefreq: "weekly", priority: "0.8", lastmod: today },
  { path: "/about", changefreq: "monthly", priority: "0.8", lastmod: today },
  { path: "/glossary", changefreq: "monthly", priority: "0.7", lastmod: today },
  { path: "/resources", changefreq: "monthly", priority: "0.8", lastmod: today },
  { path: "/resources/guides/parent-ia", changefreq: "monthly", priority: "0.8", lastmod: today },
  { path: "/contact", changefreq: "yearly", priority: "0.6", lastmod: today },
];

let blogEntries: SitemapEntry[] = [];
try {
  const { POSTS } = await import("../src/lib/blog-data.ts");
  blogEntries = POSTS.map((p: { slug: string; date: string }) => ({
    path: `/blog/${p.slug}`,
    lastmod: p.date,
    changefreq: "monthly" as const,
    priority: "0.7",
  }));
} catch {
  console.warn("⚠ Could not load blog-data.ts, sitemap will only contain static pages");
}

const entries = [...staticEntries, ...blogEntries];

const urls = entries
  .map((e) =>
    [
      `  <url>`,
      `    <loc>${BASE_URL}${e.path}</loc>`,
      e.lastmod ? `    <lastmod>${e.lastmod}</lastmod>` : null,
      e.changefreq ? `    <changefreq>${e.changefreq}</changefreq>` : null,
      e.priority ? `    <priority>${e.priority}</priority>` : null,
      `  </url>`,
    ]
      .filter(Boolean)
      .join("\n"),
  )
  .join("\n");

const xml = [
  `<?xml version="1.0" encoding="UTF-8"?>`,
  `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`,
  urls,
  `</urlset>`,
].join("\n");

const outPath = path.join(projectRoot, "public", "sitemap.xml");
fs.writeFileSync(outPath, xml, "utf-8");
console.log(`✅ Sitemap generated: ${outPath} (${entries.length} entries)`);
