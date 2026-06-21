# KORA LAB — WEBSITE BUILD PROMPT + CONTENT GUIDELINES
## Two Documents in One: What to Build, What to Write, How to Show Up

---

# DOCUMENT 1: WEBSITE BUILD PROMPT

## How to Use This Prompt

Copy everything in the block below and paste it into Claude, ChatGPT, v0.dev, or any AI web builder. It will generate a complete multi-page website for Kora Lab that you can deploy on Vercel or Netlify for free.

---

```
Build a complete, production-ready website for Kora Lab — Africa's sovereign AI lab. The site serves three audiences simultaneously: governments and institutions, investors and accelerators, and technical talent. It must feel like a research institution, not a startup landing page.

STRICT WRITING RULE — APPLY EVERYWHERE ON THE SITE
Never use em dashes (—) or double hyphens (--) anywhere in any text, heading, label, description, or copy on the site. Replace any em dash usage with a colon, a comma, a period, or restructure the sentence. This applies to all pages, all sections, all auto-generated placeholder text.

DESIGN SYSTEM
Colors: Black (#0A0A0A), White (#FFFFFF), three grays (#1A1A1A for dark panels, #6B6B6B for mid labels, #ABABAB for subdued text). No other colors. No gradients. No color accents anywhere.
Typography: Inter or system sans-serif. Weights: 400 body, 700 labels and subheadings, 900 display headlines. Line height: 1.55 for body, 1.1 for headlines.
Style: Modern, minimal, premium. Research institution feel. No emoji. No decorative icons. No rounded corners on buttons or cards. Sharp edges only.
Motion: Subtle fade-in on scroll using Intersection Observer. No parallax. No looping animations. Nothing distracting.
Layout: Full-width sections, content constrained to max 1100px, generous whitespace between sections. Mobile-first, fully responsive down to 375px. No horizontal scroll on any viewport.

SITE STRUCTURE — MULTIPLE PAGES
Build the following pages with full navigation between them:
- Home (/)
- Approach (/approach)
- Research (/research)
- Blog (/blog and /blog/[slug])
- About (/about)
- Contact (/contact)

GLOBAL ELEMENTS

Navigation (sticky, minimal, present on all pages):
- Left: KORA LAB wordmark (font-weight 900, letter-spacing -1.5px, font-size 20px)
- Center links: Mission / Approach / Research / Blog / About / Contact
- Right: "Get in Touch" button (black fill, white text, sharp corners, padding 10px 20px)
- On mobile: hamburger menu, full-screen overlay with the same links in large type on black background
- Active page link has a thin black underline indicator

Footer (present on all pages):
- Left column: KORA LAB wordmark + tagline "Africa's Sovereign AI Lab" + location "Lome, Togo"
- Center column: Navigation links repeated
- Right column: "Building for the continent." + links to kora-lab.com and edenvallie.com
- Bottom bar: thin top border + copyright line + "All rights reserved"
- Background: black. Text: white and grays.

PAGE 1: HOME (/)

Section 1.1 — Hero
Background: Black (#0A0A0A)
Headline structure (very large, stacked, font-weight 900, font-size responsive 56px to 80px):
  Line 1 white: "Africa doesn't just"
  Line 2 white: "consume AI."
  Line 3 color #ABABAB: "Africa builds AI."
Thin white horizontal rule (width 80px, height 1px) between headline and subheadline
Subheadline (gray #ABABAB, font-size 18px, max-width 600px): "Kora Lab is Africa's sovereign AI research and product lab. Closing the gap, building the models, uniting the continent under one flag."
Two CTA buttons below: "Our Approach" (white fill, black text) and "Contact the Founder" (white outline, white text, transparent fill)

Section 1.2 — Ticker
Full-width, black background, overflow hidden
Slow horizontal scroll (CSS animation, no JS), white text, font-size 13px, letter-spacing 2px, uppercase
Text repeating: "54 NATIONS / $60B AFRICA AI FUND / AU CONTINENTAL AI STRATEGY / AFDB AI 10B INITIATIVE / DIGITAL TOGO 2025-2030 / SMART AFRICA / ONE FLAG / "

Section 1.3 — The Problem
Background: #E8E8E8
Section label: "THE PROBLEM" (9px, uppercase, letter-spacing 3px, gray #6B6B6B)
Headline: "Africa Is Being Left Out of the AI Race" (font-weight 900, large)
Three equal columns, each with a label and paragraph:
  ACCESS GAP: Frontier AI tools are built for Western users. African end users face language, UX, and affordability barriers that make these tools impractical in their context.
  SOVEREIGNTY GAP: All large-scale AI models and infrastructure are owned by non-African entities. Africa has no seat at the table in shaping the models that will define its future.
  EXECUTION GAP: Governments have signed declarations. Billions are pledged. The AU Continental AI Strategy is live. What is missing is a technical lab capable of executing the vision at ground level. That is what Kora Lab is.
Each column has a thin black top border and padding above the label.

Section 1.4 — The Moment
Background: Black
Section label: "THE MOMENT"
Headline: "The Continent Has Spoken. Now It Needs Builders."
Four stacked rows, each with a date label (dark gray box on left) and event text (right):
  APRIL 2025: 54 African nations sign the Africa Declaration on AI in Kigali. A $60 billion Africa AI Fund is announced.
  FEBRUARY 2026: The African Union and Google sign a landmark AI sovereignty partnership. The AfDB and UNDP launch the AI 10 Billion Initiative.
  2025-2026: Togo activates Digital Strategy 2025-2030. At least 15 African countries now have national AI roadmaps.
  THE GAP: All of this political will and capital exists without a unified technical lab to execute it. Kora Lab is that lab.
Closing italic line (gray, font-size 20px): "We are not competing with these institutions. We are completing them."

Section 1.5 — Stats
Background: White
Four large stat blocks in a 2x2 grid, separated by 1px black lines (creating a grid effect with no spacing between cells):
  54 / Nations that signed the Kigali AI Declaration
  $60B / Africa AI Fund pledged
  2,000+ / African languages almost entirely absent from frontier AI training data
  4% / Africa's current share of the global AI workforce
Each block: stat value in 56px font-weight 900, label in 11px uppercase gray below.

Section 1.6 — Latest from the Blog (preview, 3 cards)
Background: #E8E8E8
Section label: "LATEST WRITING"
Headline: "From the Kora Lab Blog"
Three blog post preview cards in a row. Each card:
  Category label (small uppercase)
  Title (font-weight 700, 18px)
  Excerpt (2 sentences, gray)
  Date and read time (small gray)
  "Read Article" link with arrow
Link below cards: "View All Articles" pointing to /blog

Section 1.7 — Latest Research (preview, 2 items)
Background: White
Section label: "RESEARCH"
Headline: "From the Lab"
Two research item rows. Each row:
  Research type tag (WORKING PAPER / ANALYSIS / DATASET)
  Title
  One-line description
  Date + "Read Paper" link
Link below: "View All Research" pointing to /research

Section 1.8 — Contact CTA
Background: Black
Headline: "Build With Us."
Subheadline: "Whether you are a government, an institution, an investor, or a technical builder who believes in this mission, we want to hear from you."
Single "Get in Touch" button (white fill, black text, sharp corners)

PAGE 2: APPROACH (/approach)

Hero: Black background, headline "A Two-Axis Strategy for Africa's AI Sovereignty", subheadline describing the two axes briefly.

Section — Axis 01: Accessibility Layer
Black background left panel / white background right panel (50/50 split)
Large "01" numeral in dark gray (decorative)
Title: ACCESSIBILITY LAYER
Full description of what this axis involves: adapting frontier AI tools, building culturally relevant products, creating data pipelines that generate jobs, no technical knowledge required for end users.
List of product types: AI agents, no-code interfaces, developer tooling, African-language adaptations, data collection pipelines.

Section — Axis 02: Sovereign Model Lab
White background left panel / black background right panel (reversed)
Large "02" numeral
Title: SOVEREIGN MODEL LAB
Full description: building Africa's own language models and multimodal models, training on African data, publishing research, competing in the global AI race.
List of activities: African language dataset construction, model training, research publication, institutional partnerships, AI safety research.

Section — Institutional Alignment
Light gray background
Headline: "Aligned With Every Major African AI Mandate"
Table or card list of institutions and mandates:
  African Union Continental AI Strategy / Phase 1 active
  Smart Africa and Africa AI Council / 40 Heads of State board
  AfDB and UNDP AI 10 Billion Initiative / $10B target by 2035
  Togo MENTD Digital Strategy 2025-2030 / World Bank IDA backed
  Africa AI Fund $60B / Announced Kigali 2025

PAGE 3: RESEARCH (/research)

Hero: White background, black headline "Research and Papers", subheadline "Kora Lab publishes working papers, analyses, and datasets on African AI, language models, and digital sovereignty."

Filters row: All / Working Papers / Analyses / Datasets / Policy Briefs (tab-style filter, plain text, active filter has a black underline)

Research item list: Each item in a row with:
  Left: Type tag (small uppercase label in a light gray box)
  Center: Title (font-weight 700) + one-line description + authors + date
  Right: "Read Paper" link + optional PDF download icon
Use placeholder items for now with [TITLE], [DATE], [TYPE] clearly marked for easy replacement.

Call to action at bottom: "Collaborate With Us" section with short text inviting researchers, institutions, and universities to partner, plus a mailto link.

PAGE 4: BLOG (/blog and /blog/[slug])

Blog index (/blog):
Hero: Small, clean. Headline "Writing" subheadline "Analysis, perspectives, and updates from Kora Lab."
Filter tabs: All / Analysis / Institutional / Technical / Updates
Grid of blog post cards (3 columns desktop, 1 column mobile). Each card:
  Category label
  Title
  Excerpt (2 sentences)
  Author (Kheir Lissi) + Date + Estimated read time
  "Read" link

Blog post page (/blog/[slug]):
Clean reading layout, max-width 720px centered.
Top: Category label + Title (large, bold) + Author + Date + Read time
Body: Proper typographic hierarchy. h2 and h3 headings for structure. Generous line height (1.7). No em dashes anywhere.
Bottom: Author card (brief bio + link to About page) + "More from the Blog" section (3 related post cards)
SEO: Each blog post page must include unique title tag, meta description, Open Graph tags (og:title, og:description, og:image), and canonical URL.

PAGE 5: ABOUT (/about)

Section — Founder
Large name display: KHEIR LISSI (font-weight 900, large)
Role: Founder, Kora Lab / Lome, Togo
Full founder bio in first person (see content below — use the complete bio, not a truncated version)
Links: kora-lab.com and edenvallie.com

Section — The Mission
Black background, white text
Headline: "Why Kora Lab Exists"
Long-form mission statement explaining the problem, the vision, the two axes, and the continental mandate. 4 to 6 paragraphs.

Section — Advisors / Team (placeholder)
Light gray background
Headline: "The Team"
Placeholder card grid with [Name], [Role], [Institution] clearly marked so real people can be added later.
Note visible in code comments: "Replace placeholder cards with real advisor names and bios as they are confirmed."

PAGE 6: CONTACT (/contact)

Hero: Black background, white headline "Get in Touch"
Subheadline: "We welcome conversations with governments, institutions, investors, researchers, and builders."

Four contact categories with descriptions:
  Governments and Institutions: "For partnership discussions, government contracts, and institutional alignment around continental AI mandates."
  Investors and Accelerators: "For funding conversations, accelerator applications, and strategic partnerships."
  Researchers and Technical Builders: "For research collaboration, advisory roles, and joining the Kora Lab mission."
  Press and Media: "For interviews, background briefings, and press inquiries about Kora Lab."

Contact form fields: Name, Organization, Category (dropdown matching the four above), Message, Send button
Success state: Replace form with a thank you message on submit.
Direct contact: Email address displayed in gray below the form.

SEO REQUIREMENTS (APPLY TO ALL PAGES)

Every page must include in the HTML head:
  <title> tag: unique per page, format "Page Name | Kora Lab"
  <meta name="description"> tag: unique per page, 140 to 160 characters, includes primary keyword
  <meta property="og:title"> Open Graph title
  <meta property="og:description"> Open Graph description
  <meta property="og:image"> placeholder path for social share image
  <meta property="og:url"> canonical URL
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title">
  <meta name="twitter:description">
  <link rel="canonical"> tag

Structured data (JSON-LD) in the head of the home page:
  Organization schema: name, url, logo, description, founder, location
  WebSite schema with SearchAction

Robots.txt file: allow all crawlers, point to sitemap.xml
Sitemap.xml: include all page URLs with lastmod dates

On-page SEO per page:
  One H1 per page only
  H2 and H3 used correctly for section hierarchy
  Alt text on every image (descriptive, keyword-relevant)
  Internal links between pages using descriptive anchor text (not "click here")
  Page load under 2 seconds (no heavy assets, no unoptimized images)
  All images use lazy loading (loading="lazy" attribute)

Target keywords by page:
  Home: "African AI lab", "Africa sovereign AI", "AI Africa"
  Approach: "African language AI models", "AI accessibility Africa"
  Research: "African AI research", "African language models research"
  Blog: varies per article, each post targets its own keyword
  About: "Kheir Lissi", "Kora Lab founder"
  Contact: "AI partnership Africa", "African AI collaboration"

TECHNICAL REQUIREMENTS

Framework: React (Next.js preferred for SEO with server-side rendering) OR plain HTML with multiple files.
If Next.js: use App Router, generateMetadata for dynamic SEO per page, and static generation for blog posts.
If plain HTML: create separate HTML files per page, include all meta tags manually.
No external UI libraries. Use only CSS for styling.
Font loading: Google Fonts Inter via @import in CSS, with font-display: swap.
Form handling: On submit, prevent default, show inline success state. No backend required initially.
No em dashes (--) anywhere in any generated code, comments, placeholder text, or copy.
Deploy-ready: include a vercel.json or netlify.toml configuration file for one-click deployment.
Include a README.md with deployment instructions (3 steps maximum).
```

---

## Deployment (Free, No Credit Card)

**Recommended: Vercel with Next.js**
1. Push generated code to a GitHub repository.
2. Go to vercel.com, create a free account, import the repository.
3. Click Deploy. Live in 60 seconds at a vercel.app URL.
4. Add your custom domain (kora-lab.com) in Vercel settings. Free SSL included.

**Alternative: Netlify**
1. Go to netlify.com. Create a free account.
2. Drag your build folder onto the Netlify dashboard.
3. Add custom domain in settings.

**Domain:** Register kora-lab.com at Namecheap or Cloudflare Registrar for approximately $10 to $12 per year.

---

# DOCUMENT 2: CONTENT GUIDELINES FOR VISIBILITY

## The Core Strategy

Your content has one job at this stage: make you known and taken seriously by the three audiences that can change everything for Kora Lab. Governments and institutions. Investors and accelerators. Technical builders who could join or advise you.

You do not need to sell yet. You need to be found, read, and remembered. The internet is your proof of existence, your public track record, and your legal prior art simultaneously.

---

## THE FIVE CHANNELS (PRIORITY ORDER)

---

### Channel 1: LinkedIn (Highest Priority)

LinkedIn is where the people who can open doors for Kora Lab spend professional time. Government officials, AfDB program officers, accelerator partners, researchers, and investors are all active here. This is your primary channel.

**Profile setup:**
- Headline: Founder, Kora Lab | Building Africa's Sovereign AI Lab | Lome, Togo
- About section: Your founder bio condensed to 5 to 7 sentences, first person.
- Featured section: Pin your one-pager (as PDF), your founding essay link, and your website.
- Profile photo: Clear, professional. Neutral background.
- Banner: Black background, KORA LAB in white, tagline below.

**Posting frequency:** 3 times per week.

**Format 1: The Observation (2x per week)**
5 to 10 short lines. Open with a specific, verifiable fact. Add your perspective in 2 to 3 lines. End with one clear point.

Example:
"The AfDB AI 10 Billion Initiative targets 40 million jobs by 2035.

That is 40 million jobs that need AI tools, training, and infrastructure built specifically for African contexts.

No existing AI lab is building that infrastructure at the ground level. Not OpenAI. Not Anthropic. Not DeepMind.

This is what Kora Lab is being built to do.

The mandate exists. The capital is forming. The execution layer is what is missing."

**Format 2: The Progress Post (1x per week)**
Honest, short update on what you did this week. No spin. No fake momentum.

Example:
"Week 3 of building Kora Lab.

What I did:
Submitted the position paper to MENTD Togo.
Registered on the Smart Africa SANIA platform.
Shipped the first version of the website.
Started the Google for Startups Africa application.

No salary. No team. No compute credits yet.

But 54 nations have made the declaration. The AfDB is running a roadshow right now. Togo's digital strategy is active.

All I have to do is be the lab that executes it."

**What never to post on LinkedIn:**
Motivational quotes. Reposted news with no perspective. More than 2 hashtags. Anything that sounds like a press release.

---

### Channel 2: Medium (Long-Form Essays)

Medium is where you build intellectual credibility and generate search traffic. One strong essay here reaches people inside institutions in ways that social media posts never do. Each essay also becomes a blog post on your own site and a LinkedIn long-form article.

**Essay 1: The Founding Essay (Publish within 2 weeks)**

Title: "What Africa's AI Declarations Need That Nobody Is Talking About"

Structure:
1. Open with the specific declarations by name and date. Not an opinion. A fact.
2. Name the execution gap: declarations without a technical lab are unfulfillable.
3. Describe what the execution layer must do (your two axes, without pitching).
4. Introduce Kora Lab as the lab being built to fill that gap.
5. End with a direct call to action for the three audiences.

Length: 1,200 to 1,800 words. No longer.
Tone: Confident, specific, unspun. Closer to a policy brief than a blog post.
Cross-post: Wait one week after publishing on Medium, then post as a LinkedIn Article. Then add to your website blog.

**Essay 2 (Month 2):** "What African Language AI Actually Requires and Why Nobody Is Building It"
Technical credibility through research and analysis. Does not require a PhD. Requires reading and synthesis.

**Essay 3 (Month 3):** "The $60 Billion Africa AI Fund Has a Deployment Problem. Here Is How to Solve It"
Written explicitly for fund managers and institutional readers. Frames Kora Lab as the solution.

---

### Channel 3: YouTube (Medium Priority, Build Audience Over Time)

YouTube is the highest-leverage channel for building a technical and institutional audience that stays with you. One well-made video drives more trust than 50 posts. You do not need expensive equipment. A good phone, natural light, and a clean background is enough to start.

**Content types for Kora Lab on YouTube:**

Type 1: The Founder Video Series (most important, start here)
Short videos (5 to 12 minutes) where you speak directly to camera about the African AI landscape, the work Kora Lab is doing, and what you are building. These build personal trust at scale.

Episode ideas:
- "Why I left college mid third year to build Africa's AI lab" (your story, authentic)
- "What the Kigali Declaration actually commits to and what is missing"
- "What African language AI requires that Western models cannot provide"
- "How I am building a sovereign AI lab with no funding yet"
- "What the AfDB AI 10 Billion Initiative means for African startups"

Type 2: Research Breakdowns (once you have papers)
10 to 20 minute walkthroughs of your own research papers or significant AI papers with an African relevance lens. Builds technical credibility.

Type 3: Lab Updates (monthly)
5 to 8 minute honest monthly update on what Kora Lab accomplished, what is next, and what you need. Transparency builds supporters.

**Production on zero budget:**
- Phone camera, propped up at eye level.
- Window light on your face. Black or plain white wall behind you.
- Free editing: DaVinci Resolve (free, professional-grade) or CapCut (free, fast).
- Subtitles: Use YouTube's auto-caption feature and correct any errors.
- Thumbnail: Design in Canva free. Black background, bold white text, your face.

**YouTube SEO:**
- Video title: include the primary keyword in the first 5 words.
- Description: first 2 sentences are the most important (shown before "show more"). Include your website link in the first line.
- Tags: 8 to 12 relevant tags. Include "African AI", "AI Africa", "Kora Lab", and the specific topic.
- Chapters: add timestamps in the description for every video over 5 minutes.
- Post frequency: start with 2 videos per month. Consistency beats volume.

**Cross-platform:** Every YouTube video becomes a LinkedIn post (link + key takeaway), a Twitter thread (key points in 5 tweets), and if long enough, a blog post (transcript lightly edited).

---

### Channel 4: TikTok (Lower Priority, Highest Reach Potential)

TikTok reaches a completely different audience than LinkedIn or YouTube: young African professionals, students, and the global creator economy. The audience here will not fund you directly, but they become advocates, spread your name, and attract the attention of people who will. Africa has some of the highest TikTok growth rates in the world.

The format is different. TikTok rewards authenticity, speed, and hooks. The first 3 seconds determine everything.

**Content types for Kora Lab on TikTok:**

Type 1: Fast Facts (30 to 60 seconds)
One surprising or counterintuitive fact about African AI, delivered fast and direct to camera.

Example:
"Did you know that 2,000 African languages are almost completely absent from ChatGPT, Claude, and every other major AI model? That is not a gap. That is a crisis. And it is exactly what Kora Lab is being built to fix."

Type 2: Process Clips (15 to 30 seconds)
Short clips of you working, researching, writing. No narration needed. Text overlay does the work.

Type 3: Response Videos
When major AI news drops (new model release, new investment, new policy), record a 60-second reaction from an African perspective. This captures trending search traffic.

Type 4: The Build Journey
Honest clips of building with no money, no team, and a clear vision. This content performs because it is real. People root for the underdog who is building something bigger than themselves.

**TikTok SEO:**
- First line of caption is the most important. Lead with the hook, not the hashtag.
- Use 3 to 5 relevant hashtags: #AfricanAI #AIAfrica #TechAfrica #KoraLab and a trending topic tag.
- Post at times when your target audience is active (experiment with 7am to 9am and 7pm to 9pm WAT).
- Reply to every comment in the first hour of posting. The algorithm rewards engagement velocity.

**TikTok to LinkedIn pipeline:** Your best-performing TikTok content tells you what your LinkedIn audience wants to see. Ideas that get views on TikTok become long-form posts on LinkedIn. Every viral clip has a longer essay inside it.

---

### Channel 5: X / Twitter (Lightweight, For Amplification Only)

X is not a primary channel. Use it to amplify your LinkedIn and Medium content, engage with the global AI research community, and be discoverable when journalists and researchers search for African AI perspectives.

Post 1 to 2 times per week. Short observations, links to essays, and genuine replies to AI and Africa tech conversations.

Follow and engage with: researchers working on low-resource language models, African tech journalists, Smart Africa and AfDB accounts, and other African founders in the AI space.

---

## THE CONTENT FORMULA (APPLIES ACROSS ALL CHANNELS)

Every piece of content you produce should follow this five-part structure, adapted to the length and format of each platform:

1. Open with a specific, verifiable fact. Never start with an opinion or a rhetorical question.
   "In April 2025, 54 African nations signed the Africa Declaration on Artificial Intelligence."

2. Name the tension or gap. What is missing or broken in that fact?
   "None of the signatories is a technical AI lab."

3. Widen the lens. Connect it to the larger pattern.
   "This is the same pattern that appears every time Africa makes an ambitious commitment: vision and capital without an execution layer."

4. Your clear, non-hedged perspective. One sentence. No qualifications.
   "Kora Lab exists to be that execution layer."

5. The call. Who should act on this and how.
   "If you are an AfDB program officer, a government contact, or a builder who wants to work on this, reach out."

---

## CONTENT RAILS: ALWAYS AND NEVER

**Always:**
- Open with a specific fact, number, or named event. Never a question or "I think."
- Name institutions, declarations, and amounts specifically.
- Write in first person. Stay in first person until you have a team.
- End every post with a clear action: follow, reply, visit the site, or email.
- Be honest about where you are. Building without funding is not weakness. It is credibility.
- Avoid em dashes and double hyphens in all written content. Use colons, commas, or sentence breaks instead.

**Never:**
- Exaggerate traction you do not have.
- Write content that requires a disclaimer.
- Post the same content on all platforms without adapting the format and length to the channel.
- Attack or dismiss other organizations publicly.
- Use more than 2 hashtags on LinkedIn or Twitter.

---

## 60-DAY CONTENT CALENDAR

| Week | LinkedIn (3x) | Medium | YouTube | TikTok (2x) | X |
|---|---|---|---|---|---|
| Week 1 | Profile setup. First observation post. First progress post. | Draft founding essay. | Film intro video (no edit needed yet). | First fact video. First build clip. | Account setup. Follow 30 key accounts. |
| Week 2 | 2 observations, 1 progress. | Publish founding essay. | Edit and publish intro video. | 2 short clips. | Share essay. Reply to 5 posts. |
| Week 3 | 2 observations, 1 progress. | Draft essay 2. | Film second video (Kigali Declaration breakdown). | 2 clips. | Amplify LinkedIn posts. |
| Week 4 | Share one-pager as PDF post. 2 observations. | Finish essay 2. | Publish second video. | 2 clips. | Share essay 1 again with a new angle. |
| Week 5 | 2 observations, 1 progress. Feature institutional alignment. | Publish essay 2. | Film lab update video (month 1). | 2 clips. | Share essay 2. |
| Week 6 | First milestone post: what happened since week 1. 2 observations. | Outline essay 3. | Publish lab update video. | 2 clips. | Engage with AI Africa conversation. |
| Week 7 | 2 observations, 1 progress. Feature position paper angle. | Draft essay 3. | Film technical video. | 2 clips. | Light amplification. |
| Week 8 | 2 observations. Feature digital product income as proof of resourcefulness. | Publish essay 3. | Publish technical video. | 2 clips. | Share essay 3. |

By end of week 8: 24 LinkedIn posts, 3 published essays, 4 YouTube videos, 16 TikTok clips, and an established presence in the African AI conversation. That is the credibility baseline that makes every subsequent outreach land differently.

---

## THE ONE SENTENCE TEST

Before posting anything on any channel, ask: "If the AfDB program officer, the Smart Africa director, and the best ML engineer in West Africa all saw this, would each of them find something worth their time?"

If yes: publish it.
If no: rewrite it.

---

*Kheir Lissi / Founder / kora-lab.com / May 2026*
