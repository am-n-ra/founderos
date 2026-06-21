# KORA LAB FIRST PRODUCT — DEEP RESEARCH AND BRAINSTORM PROMPT
## Paste This Into Any AI Tool to Drive a Full Product Discovery Session

---

## HOW TO USE THIS PROMPT

This is a self-contained research and brainstorm prompt. Paste it in full into Claude, ChatGPT, Gemini, or any capable AI tool. It will run a structured deep research and product design session for Kora Lab's first product without needing the master context document. All necessary context is embedded.

---

=== START OF PRODUCT RESEARCH PROMPT ===

I need you to conduct a deep research and brainstorm session on the first product Kora Lab will build. I will give you the context, the reference products, the technical constraints, and then I need you to deliver a complete product analysis and vision document.

Read everything before you start. Then deliver the full output in one response. Do not ask clarifying questions before starting. If you need to make assumptions, state them and proceed.

---

## ABOUT KORA LAB

Kora Lab is Africa's sovereign AI research and product lab, founded by Kheir Lissi in Lome, Togo. The lab operates on two axes: making frontier AI accessible to African and global users (Axis One), and building Africa's own sovereign AI models (Axis Two). The first product falls squarely on Axis One.

The core accessibility mission is global, not Africa-only. The product must be usable by anyone in the world with no technical knowledge. African contexts, languages, and use cases are prioritized in design, but the market is global.

The founder has no funding yet. This means the first product must be buildable with:
- Free and low-cost APIs (especially Pollinations AI which is free, open-source, and requires no API key for basic use)
- Kie AI API as an additional model layer (research this tool's current capabilities and pricing as part of your response)
- Minimal backend infrastructure initially
- No paid team at launch

---

## THE REFERENCE PRODUCTS (STUDY THESE)

Research each of these products deeply. Understand what they do, what makes them work, what their limitations are, and what gap Kora Lab's product could fill differently or better.

REFERENCE 1: ELEVENLABS FLOW (elevenlabs.io/flow)
ElevenLabs Flow is a no-code, node-based AI workflow builder where users connect blocks (text input, voice generation, language translation, audio output, web search, etc.) to create multi-step AI pipelines without writing code. Think of it as a visual programming environment where the "programs" are AI workflows. A user can build a podcast production pipeline, a voice-enabled customer service agent, or a multilingual audio translator by dragging and connecting blocks on a canvas.

Research and answer:
- What specific blocks and capabilities does ElevenLabs Flow currently offer?
- Who is the target user and what are the most common use cases?
- What are the limitations and pain points users report?
- What does it cost?
- What is missing that an African-context version would need to add?

REFERENCE 2: FREEPIK SPACES (freepik.com/ai/spaces)
Freepik Spaces is an AI creative workspace where users combine multiple AI generation tools (image generation, background removal, upscaling, editing, etc.) in one unified canvas. Users can chain AI operations together visually without leaving the platform or using technical tools. It abstracts away the complexity of prompt engineering and API calls behind a clean creative interface.

Research and answer:
- What specific tools and workflows does Freepik Spaces offer currently?
- Who uses it and for what?
- What are its limitations?
- What pricing model does it use?
- What would a version designed for African creators and businesses look like differently?

REFERENCE 3: NODEBASE (research the current state of nodebase AI tools, including tools like Flowise, LangFlow, and Dify which all follow a similar node-based AI builder pattern)
Node-based AI builders allow users to visually construct AI agent workflows by connecting nodes that represent different AI capabilities (LLM prompts, retrieval, web search, code execution, etc.). They are currently mostly technical tools aimed at developers. The opportunity is in making this pattern accessible to non-technical users.

Research and answer:
- What is the current state of node-based AI builder tools? Which ones are most used?
- What is the gap between current tools and true non-technical accessibility?
- What would it take to make a node-based AI builder genuinely usable by someone with no coding knowledge in an African context?

---

## THE TECHNICAL FOUNDATION

POLLINATIONS AI (pollinations.ai / gen.pollinations.ai):
Pollinations AI is a free, open-source generative AI platform. Key facts for this product design:
- Single unified API endpoint at gen.pollinations.ai for text, image, audio, and video generation
- No API key required for basic use
- Supports models including Flux (image), GPT Image, Seedream, Claude (text), Gemini (text), Mistral (text), and more
- No data storage, anonymous usage, privacy-first
- Actively maintained, 500+ community projects already built on it
- Commercial use permitted on appropriate tiers
- React hooks available for frontend integration

For this product, Pollinations AI provides:
- Text generation (via Claude, Gemini, Mistral, OpenAI models)
- Image generation (via Flux, GPT Image, Seedream)
- Audio generation (text-to-speech and sound)
- Video generation (emerging capability)

KIE AI API:
Research this tool thoroughly. Find out:
- What is Kie AI? What does its API offer?
- What models does it provide access to?
- What is the pricing model? Is there a free tier?
- How does it compare to Pollinations AI as a model layer?
- What specific capabilities would make it the right "core model layer" choice for an accessibility product?
- Are there limitations or risks to building a product core on this API?

---

## THE PRODUCT BRIEF

Design the first Kora Lab product based on your research above. The product should:

CORE CONCEPT:
A unified, no-code AI workspace where anyone with no technical knowledge can discover, combine, and deploy AI capabilities in a single interface. Think of it as the intersection of ElevenLabs Flow's workflow builder, Freepik Spaces' all-in-one creative canvas, and a simplified version of the node-based builder pattern — but designed from the ground up for accessibility, African contexts, and global users who have been left out of the current AI wave.

The product is NOT just another AI tool aggregator. It is a workspace where AI capabilities become composable actions that anyone can chain together to solve real problems in their life, work, or business.

ACCESSIBILITY REQUIREMENTS:
- Works entirely in the browser. No install.
- No coding required. Zero.
- Multilingual interface. Priority languages: English, French, Swahili, Hausa, Yoruba, and Arabic. (The product should be designed so more languages can be added as a module, not rebuilt for each language.)
- Works on low-bandwidth connections common in West Africa.
- Works on mobile (most African internet users are mobile-first).
- Priced accessibly. A free tier must be genuinely useful, not crippled.
- Culturally adapted defaults. When a user opens the product for the first time in Lome or Lagos or Nairobi, the suggested use cases, example projects, and default templates should reflect their context, not a San Francisco startup's context.

TECHNICAL CONSTRAINTS:
- Built primarily on Pollinations AI API (free, no-key required for the base layer)
- Kie AI API as additional or core model layer
- No paid backend infrastructure at launch (use Vercel free tier, Supabase free tier, or Cloudflare Workers free tier)
- Frontend: React or Next.js
- The founder is not a deep backend engineer. The architecture must be simple enough for a learning builder with AI coding assistance.

---

## WHAT I NEED YOU TO DELIVER

Deliver a complete, structured product discovery document covering all of the following sections. Do not summarize. Write each section fully.

SECTION 1: REFERENCE PRODUCT ANALYSIS
For each of the three reference products (ElevenLabs Flow, Freepik Spaces, node-based builders), provide:
- What it does and how it works
- Who uses it and why
- Its pricing model
- Its key limitations and gaps
- What Kora Lab's version should do differently or better

SECTION 2: KIE AI API RESEARCH
Everything you can find on Kie AI: capabilities, pricing, free tier, model access, limitations, risks, and how it pairs with Pollinations AI. If you cannot find sufficient information, state that clearly and recommend how the founder should validate it before building on it.

SECTION 3: POLLINATIONS AI TECHNICAL SUMMARY
A clear, builder-ready summary of what Pollinations AI provides, organized by capability:
- Text generation: models available, how to call them, limitations
- Image generation: models available, parameters, quality
- Audio generation: what is available
- Video generation: current state
- API endpoint structure and how to use it in a React/Next.js app without a backend
- Rate limits and free tier constraints
- What happens when Pollinations AI is down or rate-limited (fallback strategy)

SECTION 4: PRODUCT VISION
A full product vision for Kora Lab's first product covering:
- Product name options (with rationale for each)
- The one-sentence product description
- The core interaction model (how does a user actually use this product step by step)
- The workspace concept: what does the canvas or interface look like?
- The "blocks" or "capabilities" that users can combine. List every capability the product should launch with, every capability it should add in month 3, and every capability it should have by the end of year 1.
- The use case library: what are the 10 most compelling problems this product solves for African users? For global users?
- Template library: what are the 10 pre-built templates that ship with the product on day one?

SECTION 5: AFRICAN CONTEXT DESIGN DECISIONS
Specific design decisions that make this product genuinely different from what exists for African users:
- Which African languages are supported at launch and how (translation layer, native model, or hybrid)?
- What are the African-specific use cases that Western products do not address? Be specific and real.
- How does the product handle low-bandwidth environments technically?
- What pricing model works for African markets? What are comparable price points?
- What cultural adaptations are needed in the UX, examples, and default content?

SECTION 6: TECHNICAL ARCHITECTURE
A concrete, builder-readable architecture for the MVP. Cover:
- Frontend stack recommendation
- How Pollinations AI is called from the frontend (direct API calls, or via a thin serverless function)
- How Kie AI API is integrated
- Where state is stored (user sessions, saved workspaces, project files)
- Authentication approach (or no auth for MVP)
- Hosting and infrastructure (all free or near-zero cost)
- What the MVP scope is (exactly what is built in the first 4 to 6 weeks)
- What is deferred to month 3

SECTION 7: BUSINESS MODEL
How this product generates revenue for Kora Lab:
- Free tier: what is included, what are the limits
- Paid tiers: what do they unlock, what are the price points
- African market pricing vs. global pricing strategy
- Government and institutional licensing opportunity
- Estimated monthly revenue at 1,000 active users, 5,000 active users, and 20,000 active users

SECTION 8: GO-TO-MARKET STRATEGY
How Kora Lab launches and grows this product with zero marketing budget:
- Who are the first 100 users and exactly how do you get them?
- What content angles drive organic discovery for this product?
- What communities and platforms are the distribution channels?
- What partnerships would accelerate distribution?
- What does week 1, month 1, and month 3 look like in terms of launch sequence?

SECTION 9: RISKS AND MITIGATIONS
The real risks of building on Pollinations AI and Kie AI as the primary API layers. For each risk:
- State the risk clearly
- Assess its probability and severity
- State the specific mitigation

SECTION 10: COMPETITIVE MOAT
Why, over time, Kora Lab's version of this product becomes difficult to displace:
- What makes it specifically better for the users it serves?
- What data advantages accrue over time?
- What community or ecosystem effects develop?
- How does the sovereign model axis (Axis Two) eventually feed into this product?

---

## OUTPUT FORMAT REQUIREMENTS

- Write in full prose for all narrative sections. No bullet points in the main analysis.
- Tables are acceptable for structured comparisons (pricing tiers, capability lists, architecture stacks).
- No em dashes anywhere. Use colons, commas, or sentence breaks.
- Do not hedge excessively. Give your actual best assessment. If something is uncertain, say so and move on.
- Length: this should be a substantive document. Do not truncate sections to save space. Write each section completely.

---

This is the founding product research session for Kora Lab. The output of this session will shape what Africa's first sovereign AI lab builds first. Treat it with that weight.

=== END OF PRODUCT RESEARCH PROMPT ===

---

## NOTES ON THIS PROMPT

WHAT THIS PROMPT IS FOR: Paste it into a fresh AI session specifically for product research and design. It is separate from your master context prompt by design. Use the master context for day-to-day operational tasks. Use this prompt when you are ready to go deep on the product.

BEST TOOLS FOR THIS PROMPT:
- Claude (claude.ai): Best for nuanced analysis and long structured documents. Recommended first choice.
- ChatGPT with browsing enabled: Good for the research sections where current information matters.
- Perplexity: Use specifically for the Kie AI API research section where you need current web information.

VALIDATING KIE AI: Before building on any API, spend 30 minutes testing it manually. Generate 10 outputs. Check the rate limits. Read the terms of service for commercial use rights. Then decide whether it belongs at the core of the product or as a supplementary layer.

POLLINATIONS AI QUICK START: To test Pollinations AI immediately, open your browser and visit:
- Image: image.pollinations.ai/prompt/a beautiful sunset over Lagos Nigeria
- Text: text.pollinations.ai/What is the state of AI in West Africa?
- Unified: gen.pollinations.ai
No account needed. Results appear instantly. This is what your product users will experience under the hood.

---

*Built for Kheir Lissi / Kora Lab / kora-lab.com / May 2026*
