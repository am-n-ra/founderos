# KORA — Research

## Frontier Training Methodologies (2026)

Comparative analysis of how Anthropic, Google DeepMind, and OpenAI train frontier models. Source: system cards, technical reports, interviews.

### Key Takeaways for KORA

| Dimension | KORA Approach |
|-----------|---------------|
| Architecture | Start with Sparse MoE from day one. Even 4 experts x 7B = 28B total / 7B active outperforms dense 7B. |
| Data | Invest in data filtering before training. Clean 500B tokens beats noisy 2T tokens. |
| Post-training | Don't stop at SFT. Implement at least 3 rounds of RLHF. |
| Reasoning | Process reward models + budget forcing (s1 paper) is replicable at any scale. |
| Precision | Use BF16 mixed precision now, plan FP8 migration. |
| Curriculum | Implement WSD schedule. Reserve 5-10% for high-quality data anneal. |
| Safety | Build safety infrastructure from day one. Basic input/output classifiers + red teaming. |
| Agents | Agentic capabilities are becoming primary interaction paradigm. Design for agents, not chat. |
| Synthetic Data | Invest in synthetic data generation pipelines. Optimal ratio ~30% synthetic. |

### Cost Comparison for Training Runs

| Scale | Cost | Hardware | Result |
|-------|------|----------|--------|
| KORA Phase 1 | $50K-200K | 8-32 GPUs | 1-7B model, prototype |
| KORA Phase 2 | $200K-2M | 32-256 GPUs | 7-70B model, production |
| Mini-frontier | $2-10M | 256-2K GPUs | 70-200B MoE, competitive |
| GPT-4 class | $63-100M | 25K A100s | ~1.7T MoE |

### Ten-Point Frontier Recipe

1. **Sparse MoE is the standard** — 8-15% activation ratio, top-2 or top-4 routing, load balancing loss critical
2. **Quality trumps quantity** — safety-filtered pretraining data, aggressive dedup, perplexity-based scoring
3. **Multi-stage post-training** — SFT → Reward Model → RLHF (PPO) → Additional alignment
4. **Test-time compute is the new scaling** — Process reward models + budget forcing
5. **FP8 is production, FP4 is coming** — validated at 671B scale by DeepSeek-V3
6. **WSD schedule + data annealing** — Warmup-Stable-Decay has replaced Cosine
7. **Hardware co-design** — understand HW-SW co-design for future cluster design
8. **Safety infrastructure** — 9-layer safety stack is gold standard
9. **Agentic architecture** — Planner-Executor-Reflector most advanced
10. **Synthetic data is load-bearing** — textbook-quality synthetic data can surpass teacher model

## Theory of Change (V3.1)

### Three Causal Links

**Link 1 — Capability to Natural Switch:**
For Africans already using AI → IF KORA develops models as good as world's best → THEN they naturally switch to sovereign → BECAUSE it's equally capable, better adapted, more accessible.
*Falsifiable:* If models are world-class but educated users still prefer foreign models after 12 months, this link is false.

**Link 2 — Mother Tongue to First Access:**
For Africans not using AI → IF KORA makes models usable in their spoken language → THEN they use AI for the first time → BECAUSE barrier was language/education, not technology.
*Falsifiable:* If models available in local languages but adoption among non-literate < 5% after 2 years, this link is false.

**Link 3 — Massive Distribution to Universal Coverage:**
For both groups → IF KORA distributes via smartphones + wearables + fixed devices → THEN every African can access AI → BECAUSE infrastructure follows the user.
*Falsifiable:* If technology exists but doesn't reach remote populations (< 50% coverage in 5 years), this link is false.

### Complete Causality

```
Mission: World-class models, natural for educated, accessible for non-educated
    |
    v
[Link 1] Educated adopt naturally (equally good)
    |
    v
[Link 2] Non-educated access for first time (language)
    |
    v
[Link 3] Massive distribution via all channels
    |
    v
Vision: No more importation — because best choice is local and everyone can access it
```

## Research Papers Tracked

73 papers (223.3 MB, 34 from 2026) — see `FounderOS/projects/KORA/FRONTIER_TRAINING_RESEARCH.md` for details.

Key areas of study:
- DeepSeek MoE architecture
- Qwen model design
- DiT (Diffusion Transformer) for image
- Coqui TTS for audio
- Veo for video
- Process reward models (o1-style reasoning)
- Budget forcing (s1 paper)
- WSD learning rate schedule

## Domain Knowledge

- African AI ecosystem landscape
- Frontier model architecture and training requirements
- Language model adaptation for low-resource languages (Ewe, Fon, Yoruba)
- Compute partnership models in West Africa
- AI sovereignty policy landscape

---

| Field | Value |
|-------|-------|
| Source | FRONTIER_TRAINING_RESEARCH.md, 03_THEORY_OF_CHANGE.md, 05_STRATEGIC_PLAN.md |
| Last Updated | 2026-06-29 |
