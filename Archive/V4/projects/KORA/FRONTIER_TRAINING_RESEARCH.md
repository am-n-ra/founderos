# Frontier Training Methodologies — Research Synthesis (2026)

Sources: Anthropic system cards, Google model cards + I/O keynotes, OpenAI technical reports, interviews, leaked details.

---

## Executive Summary: How Each Lab Actually Trains

| Dimension | Anthropic | Google DeepMind | OpenAI |
|-----------|-----------|-----------------|--------|
| **Compute** | Multi-cloud: AWS Trainium + GCP TPU + NVIDIA GPU. Project Rainier: 500K Trainium2 chips. $6.8B/yr. | In-house: TPU v4→v5p→v6e→v7 Ironwood→v8. JAX+Pathways. $180B/yr CapEx. | NVIDIA partnership. Stargate: 450K GB200 GPUs, $500B. GB200 NVL72 racks. |
| **Architecture** | Dense (Claude 1-3.5) → MoE (Mythos 5). ~10T params, 800B-1.2T active. 1M ctx. | Native multimodal MoE. Unified embedding space. Genie+Veo+Nano Banana fusion. 1M-10M ctx. | Sparse MoE since GPT-4. 2.4T total, 8-15% active. Native omnimodal. Planner-Executor-Reflector. |
| **Precision** | BF16 mixed → FP8 adopting | BF16 primary, FP8 on Ironwood | FP16→BF16→FP8→FP4 inference |
| **Data** | Proprietary crawler + licensed + synthetic. Safety-first filtering BEFORE pretraining. | YouTube + Search + Books + Workspace. Unmatched data moat. Semantic dedup. | 45TB internet → 1-2T tokens. MinHash dedup + perplexity filtering. 11% synthetic. |
| **Post-training** | Constitutional AI (SL-CAI→RLHF→RLAIF→Character). 9-layer safety stack. Two-track release. | Traditional RLHF (PPO) + WARP. 3 stages: SFT→RM→RLHF. Frontier Safety Framework. | RLHF (PPO). Process reward models (o1). Instruction Hierarchy. Deliberative alignment. Router-based. |
| **Safety** | Constitutional Classifiers (Gen 2: 1% overhead). Two-track: Fable/Mythos. ASL framework. | SynthID watermarking. Automated red-teaming. Frontier Safety Framework. | Preparedness Framework. 5-tier risk. Deliberative alignment. System Cards. |
| **Differentiator** | Constitutional AI. Pretraining data filtering. Two-track release. | Native multimodal. World models (Genie). Full vertical integration (chip→model→product). | Reasoning models (o1/o3). Test-time compute scaling. Stargate infrastructure. |

---

## The 10-Point Recipe (Common Across All 3)

### 1. Architecture: Sparse MoE Is The Standard
All three labs use **Sparse Mixture-of-Experts** as their primary architecture (except Anthropic's pre-Mythos models). 8-15% activation ratio. Top-2 or Top-4 routing. Load balancing loss is critical.

**KORA takeaway**: Start with MoE from day one. Even 4 experts × 7B = 28B total / 7B active outperforms a dense 7B.

### 2. Data: Quality Trumps Quantity
| Lab | Data Approach |
|-----|---------------|
| Anthropic | Safety-filtered pretraining data. Constitutional classifiers applied during preprocessing. 33% harm reduction with 0% benchmark loss. |
| Google | YouTube + Search + Books creates an unassailable data moat. Semantic dedup at all levels. |
| OpenAI | Aggressive dedup (40% reduction). Perplexity-based quality scoring. 11% synthetic data. |

**KORA takeaway**: Invest in data filtering before training. A clean 500B tokens beats a noisy 2T tokens.

### 3. Post-training: Multiple Stages, Not One
All three use multi-stage post-training. The pipeline is:
SFT → Reward Model → RLHF (PPO) → Additional alignment stages

Anthropic adds: Constitutional AI self-critique + Character training
OpenAI adds: Process Reward Models + Instruction Hierarchy + Deliberative Alignment
Google adds: WARP (3-stage RLHF with merging)

**KORA takeaway**: Post-training is where the real differentiation happens. Don't stop at SFT. Implement at least 3 rounds of RLHF.

### 4. Reasoning: Test-Time Compute Is The New Scaling
OpenAI pioneered it with o1 (Sep 2024). Anthropic followed with Claude Opus 4 extended thinking. Google followed with Gemini 2.5 Pro Deep Think.

The formula: train with process reward models (per-step rewards) → at inference, allow the model to "think" longer for harder problems.

**KORA takeaway**: Process reward models + budget forcing (s1 paper) is replicable at any scale.

### 5. Precision: FP8 Is Production, FP4 Is Coming
- DeepSeek-V3 validated FP8 at 671B scale
- NVIDIA H100/GB200 natively support FP8 with Transformer Engine
- Google's Ironwood TPU supports FP8 natively
- FP4 is coming (Blackwell, Vera Rubin)

**KORA takeaway**: Use BF16 mixed precision now, plan FP8 migration. Don't wait for FP4.

### 6. Curriculum: WSD Schedule + Data Annealing
Warmup-Stable-Decay (WSD) has replaced Cosine as the default schedule. All labs anneal on high-quality data at the end of training.

**KORA takeaway**: Implement WSD schedule. Reserve 5-10% of training budget for high-quality data anneal.

### 7. Hardware Co-Design
- **OpenAI + NVIDIA**: Co-designed GB200 NVL72 around GPT-5 requirements
- **Anthropic + AWS Annapurna**: Daily engineering communication on Trainium design
- **Google**: Full vertical stack (TPU → JAX → Pathways → Gemini)

**KORA takeaway**: At small scale, this doesn't apply. But understanding the HW-SW co-design principle informs future cluster design.

### 8. Safety Infrastructure
Anthropic's 9-layer safety stack is the gold standard. Two-track release (Fable/Mythos) is innovative. OpenAI's Preparedness Framework and Deliberative Alignment are also strong.

**KORA takeaway**: Build safety infrastructure from day one. Even basic input/output classifiers + red teaming.

### 9. Agentic Architecture
OpenAI's Planner-Executor-Reflector (GPT-5.5) is the most advanced. Anthropic's Claude Code + MCP protocol is the most open. Google's Vertex AI Agent Builder is the most integrated.

**KORA takeaway**: Agentic capabilities are becoming the primary interaction paradigm. Design for agents, not chat.

### 10. Synthetic Data Is Load-Bearing
Phi-4 proved textbook-quality synthetic data can surpass the teacher model. OpenAI uses 11% synthetic in pretraining. DeepSeek-R1 uses reasoning trace distillation.

**KORA takeaway**: Invest in synthetic data generation pipelines. The optimal ratio is ~30% synthetic.

---

## Cost Comparison: What A Training Run Costs

| Scale | Approx. Cost | Approx. Hardware | What You Get |
|-------|-------------|-------------------|--------------|
| KORA Phase 1 | $50K-200K | 8-32 GPUs | 1-7B model, prototype |
| KORA Phase 2 | $200K-2M | 32-256 GPUs | 7-70B model, production |
| Mini-frontier | $2-10M | 256-2K GPUs | 70-200B MoE, competitive |
| GPT-4 class | $63-100M | 25K A100s | ~1.7T MoE |
| Mythos class | $1B+ | 100K+ Trainium2 | 10T MoE, frontier |
| Stargate class | $100B+ | 2M+ chips | Zettascale |

---

## Files
- `02_MISSION.md` — Mission V1.0 (sovereign frontier intelligence)
- `11_STRATEGIC_PRINCIPLES.md` — 20 permanent principles
- `12_NORTH_STAR.md` — "Increase Africa's Sovereign AI Capability"
- `13_STRATEGIC_ASSETS_MAP.md` — 12 asset classes to accumulate
- `FRONTIER_TRAINING_RESEARCH.md` — This file (full comparative research)
- `papers/` — 73 papers, 223.3 MB (34 from 2026)
