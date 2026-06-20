# Distribution Memory

## Purpose

Structured campaign memory that accumulates market intelligence over time. Every campaign is recorded with its strategy and performance. DIOS queries this before every new campaign.

## Structure

Each campaign entry follows this schema:

```yaml
## Campaign: [ID]

- Date: YYYY-MM-DD
- Product: [name]
- Price: [price FCFA]
- Objective: [views / leads / sales]
- Market: [country, city]
- Audience: [segment name]
- Language: [language]
- Platform: [platform name]
- Hook: "exact hook text used"
- Angle: [description of angle]
- CTA: "exact call to action"
- Views: N
- Likes: N
- Comments: N
- Shares: N
- Messages: N
- Leads: N
- Conversions: N
- Revenue: N FCFA
- Cost: N FCFA
- ROI: N.Nx
- Learnings: "what worked and what didn't"
- Next: "what to try next time"
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

| Field | Value |
|-------|-------|
| Last Verified | 2026-06-20 |
| Owner | System |
| Maintained By | DIOS (writes after each campaign) |
