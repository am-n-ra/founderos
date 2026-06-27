# DISTRIBUTION MEMORY

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 10.

## Role

Store campaign performance data for distribution intelligence.

Every campaign is recorded with its strategy and results. DIOS queries this before every new campaign to find patterns. Over time, DISTRIBUTION MEMORY accumulates market intelligence that makes DIOS more effective.

**Status:** ⚠️ STALE — needs review. Schema defined but initial campaign entries being added below.

**Last Updated:** 2026-06-24

## Structure

Each campaign entry follows this schema:

```yaml
Campaign:
  ID: "C001"
  Date: YYYY-MM-DD
  Product: "product name"
  Price: "price FCFA"
  Objective: "views | leads | sales"
  Market:
    Country: "country"
    City: "city"
  Audience: "segment name"
  Language: "language"
  Platform: "platform name"
  Hook: "exact hook text used"
  Angle: "description of angle"
  CTA: "call to action"
  Views: 0
  Likes: 0
  Comments: 0
  Shares: 0
  Messages: 0
  Leads: 0
  Conversions: 0
  Revenue: 0
  Cost: 0
  ROI: 0.0
  Learnings: "what worked and what didn't"
  Next: "what to try next time"
```

## Usage

DIOS queries DISTRIBUTION_MEMORY at step 1 of its workflow.

Query patterns:
- "Which hooks won for audience X?"
- "Which language converted best for product Y?"
- "Which platform distributed furthest in market Z?"
- "Which CTA performed best on platform W?"

## Campaign Entries

### C001 — DoodleMind Short #1
- **Date:** 2026-06-20
- **Product:** DoodleMind YouTube Short
- **Title:** "Trillion Dollar Question"
- **Platforms:** YouTube, TikTok
- **YouTube Results:** 366 views, 72.6% retention, 87.5% likes, 97% Shorts feed, 40s avg
- **TikTok Results:** 65 views, 10.43s avg, 2.8% full watch, 2 followers, drop at 0:02
- **Learnings:** Short #1 performed better on YouTube than TikTok. Audio/visual hook layer identified as bottleneck.
- **Next:** Apply Hook Layer Priority fix (audio > visual > text) to Short #2

### C002 — DoodleMind Short #2
- **Date:** 2026-06-24
- **Product:** DoodleMind YouTube Short
- **Title:** "Your Body Has a Second Brain"
- **Platforms:** YouTube, TikTok
- **Script:** 180 words ~65s, 12 scenes, 27 image prompts
- **Thumbnail:** Silhouette doodle with second brain in belly (orange)
- **Metadata:** Title A/B, tags neuroscience, bilingual description
- **Status:** Published today — awaiting analytics
- **Learnings:** Pending
- **Next:** Produce Short #3

### C003 — Meta Ads (Blocked)
- **Date:** 2026-06-20
- **Product:** Pest Repeller
- **Platform:** Meta (Facebook Ads)
- **Status:** ❌ Blocked — account restricted. 0.77$ debt outstanding.
- **Budget:** 1,100 FCFA growth budget blocked
- **Learnings:** Meta ad account needs to be cleared before any paid campaigns. Cannot run ads with outstanding balance or restrictions.
- **Next:** Resolve Meta ad account restriction. Focus on organic TikTok as primary channel.

### C004 — Marketplace (Under Review)
- **Date:** 2026-06-24
- **Status:** 🔍 Under review — channel not yet activated
- **Notes:** Marketplace distribution channel identified but not yet operational. Further investigation needed.
- **Next:** Evaluate which marketplace (TikTok Shop, YouTube Shopping, local) is viable given constraints.

## Footer

Last updated: 2026-06-24 (campaign entries C001-C004 added; marked STALE)

Memory compounds over time.

Each campaign makes the system smarter.

An empty memory is expected at first. It fills with every campaign.
