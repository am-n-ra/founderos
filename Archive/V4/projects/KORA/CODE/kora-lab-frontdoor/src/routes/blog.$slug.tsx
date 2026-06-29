import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { SiteLayout } from "@/components/site-layout";
import { POSTS } from "@/lib/blog-data";

const SITE_URL = "https://koralab.org";
const GUIDE_SLUG = "votre-enfant-face-a-lia-guide-parent-afrique-2026";
const GUIDE_PATH = "/resources/guides/parent-ia";

export const Route = createFileRoute("/blog/$slug")({
  loader: ({ params }) => {
    const post = POSTS.find((p) => p.slug === params.slug);
    if (!post) throw notFound();
    return { post };
  },
  head: ({ loaderData }) => {
    const post = loaderData?.post;
    const title = post ? `${post.title} | Kora Lab` : "Article | Kora Lab";
    const desc = post?.excerpt ?? "An article from Kora Lab.";
    const url = post ? `${SITE_URL}/blog/${post.slug}` : `${SITE_URL}/blog`;
    return {
      meta: [
        { title },
        { name: "description", content: desc },
        { name: "keywords", content: post ? `${post.category}, sovereign AI Africa, Kora Lab, African AI, ${post.title}` : "Kora Lab, African AI" },
        { property: "og:title", content: title },
        { property: "og:description", content: desc },
        { property: "og:type", content: "article" },
        { property: "og:url", content: url },
        { property: "og:image", content: `${SITE_URL}/og-default.jpg` },
        { property: "og:image:width", content: "1216" },
        { property: "og:image:height", content: "640" },
        { property: "og:image:alt", content: "Kora Lab — Africa's Sovereign AI Lab" },
        { property: "article:author", content: "Kheir Lissi" },
        { property: "article:published_time", content: post?.date ?? "" },
        { property: "article:section", content: post?.category ?? "" },
        { name: "twitter:title", content: title },
        { name: "twitter:description", content: desc },
        { name: "twitter:image", content: `${SITE_URL}/og-default.jpg` },
      ],
      links: [{ rel: "canonical", href: url }],
      scripts: post
        ? [
            {
              type: "application/ld+json",
              children: JSON.stringify({
                "@context": "https://schema.org",
                "@type": "Article",
                headline: post.title,
                description: post.excerpt,
                image: `${SITE_URL}/og-default.jpg`,
                datePublished: post.date,
                dateModified: post.date,
                author: {
                  "@type": "Person",
                  name: "Kheir Lissi",
                  url: `${SITE_URL}/about`,
                },
                publisher: {
                  "@type": "Organization",
                  name: "Kora Lab",
                  url: SITE_URL,
                  logo: { "@type": "ImageObject", url: `${SITE_URL}/og-default.jpg` },
                },
                mainEntityOfPage: { "@type": "WebPage", "@id": url },
                articleSection: post.category,
                inLanguage: "en",
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
                  { "@type": "ListItem", position: 3, name: post.title, item: url },
                ],
              }),
            },
          ]
        : [],
    };
  },
  component: BlogPost,
  notFoundComponent: () => (
    <SiteLayout>
      <div className="mx-auto max-w-[720px] px-6 py-32 text-center">
        <h1 className="text-4xl font-black">Article not found</h1>
        <Link to="/blog" className="mt-6 inline-block text-xs font-bold uppercase tracking-wider underline">Back to Blog</Link>
      </div>
    </SiteLayout>
  ),
});

function renderBody(body: string) {
  return body.split("\n\n").map((block, i) => {
    if (block.startsWith("### ")) return <h3 key={i}>{block.slice(4)}</h3>;
    if (block.startsWith("## ")) return <h2 key={i}>{block.slice(3)}</h2>;
    return <p key={i}>{block}</p>;
  });
}

function BlogPost() {
  const { post } = Route.useLoaderData();
  const related = POSTS.filter((p) => p.slug !== post.slug).slice(0, 3);
  return (
    <SiteLayout>
      <article className="bg-white">
        <div className="mx-auto max-w-[720px] px-6 py-20 md:py-28">
          <p className="text-[10px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">{post.category}</p>
          <h1 className="mt-4 text-3xl font-black leading-tight tracking-[-0.02em] md:text-5xl">{post.title}</h1>
          <p className="mt-6 text-sm text-[#6B6B6B]">By Kheir Lissi · {post.date} · {post.readTime}</p>
          <hr className="my-10 border-t border-[#E8E8E8]" />
          <div className="kora-prose text-[17px] text-[#1A1A1A]">
            {renderBody(post.body)}
          </div>
          {post.slug === GUIDE_SLUG && (
            <div className="mt-10">
              <Link
                to={GUIDE_PATH}
                className="inline-block bg-[#0A0A0A] px-8 py-4 text-xs font-bold uppercase tracking-wider text-white transition-opacity hover:opacity-80"
              >
                Acheter le guide →
              </Link>
            </div>
          )}
        </div>
      </article>

      <section className="border-t border-[#E8E8E8] bg-[#E8E8E8]">
        <div className="mx-auto max-w-[720px] px-6 py-12">
          <p className="text-[10px] font-bold uppercase tracking-[0.3em] text-[#6B6B6B]">About the Author</p>
          <h2 className="mt-3 text-xl font-bold">Kheir Lissi</h2>
          <p className="mt-3 text-sm text-[#1A1A1A]">
            Founder of Kora Lab, building Africa's sovereign AI infrastructure from Lome, Togo.
          </p>
          <Link to="/about" className="mt-4 inline-block text-xs font-bold uppercase tracking-wider underline">Read More on About</Link>
        </div>
      </section>

      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20">
          <h2 className="text-2xl font-black tracking-[-0.02em]">More from the Blog</h2>
          <div className="mt-8 grid gap-8 md:grid-cols-3">
            {related.map((p) => (
              <article key={p.slug} className="border-t border-[#0A0A0A] pt-6">
                <p className="text-[10px] font-bold uppercase tracking-[0.25em] text-[#6B6B6B]">{p.category}</p>
                <h3 className="mt-3 text-lg font-bold">{p.title}</h3>
                <p className="mt-3 text-sm text-[#1A1A1A]">{p.excerpt}</p>
                <Link to="/blog/$slug" params={{ slug: p.slug }} className="mt-4 inline-block text-xs font-bold uppercase tracking-wider hover:opacity-60">Read →</Link>
              </article>
            ))}
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
