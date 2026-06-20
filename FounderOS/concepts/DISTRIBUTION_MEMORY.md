# DISTRIBUTION MEMORY

## Concept

Defined in CONCEPT_REGISTRY.md — Concept 10.

## Role

Store campaign performance data for distribution intelligence.

Every campaign is recorded with its strategy and results. DIOS queries this before every new campaign to find patterns. Over time, DISTRIBUTION MEMORY accumulates market intelligence that makes DIOS more effective.

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

## Empty State

No campaigns recorded yet.

## Footer

Last updated: 2026-06-20 (created — initial schema)

Memory compounds over time.

Each campaign makes the system smarter.

An empty memory is expected at first. It fills with every campaign.
