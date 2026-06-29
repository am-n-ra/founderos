# Anchored Summary — Session 2026-06-29

## Mission
KORA builds sovereign frontier intelligence as world-class as the best global labs, accessible to every African regardless of language or literacy.

## Complete Paper Library (73 papers, 223.3 MB | 34 from 2026, 14 from 2025)

### CORE: Frontier Training Recipes (11 papers) — HOW TO TRAIN FROM SCRATCH
| # | Paper | Year | Why |
|---|-------|------|-----|
| 37 | Llama 3 Herd of Models (9.4 MB) | 2024 | Most complete open frontier recipe |
| 38 | DeepSeek-V3 | 2024 | 671B MoE for $5.6M — FP8 blueprint |
| 39 | DeepSeek-V3 Scaling Challenges | 2025 | Hardware-aware engineering |
| 40 | Phi-4 | 2024 | 14B surpasses teacher via synthetic data |
| 42 | DeepSeek-R1 (4.8 MB) | 2025 | Pure RL elicits reasoning + reflection |
| 43 | TULU 3 (7.9 MB) | 2024 | Complete open post-training: SFT→DPO→RLVR |
| 44 | DAPO | 2025 | Open RL — 50 on AIME |
| S1 | DeepSeek V4 | 2026 | 1.6T MoE, 1M ctx — latest frontier |
| S2 | Qwen3.5-Omni | 2026 | Multimodal MoE from Alibaba |
| S3 | Kimi K2.5 | 2026 | Moonshot's frontier model |
| S4 | Ministral 3 | 2026 | Mistral's small model recipe |

### CORE: Post-Training & Reasoning (7 papers) — 2026 focus
| # | Paper | Key insight |
|---|-------|-------------|
| 41 | DeepSeekMath/GRPO (2024) | RL algorithm behind reasoning revolution |
| 50 | s1: Test-Time Scaling (2025) | Reproduce o1 with 1,000 examples |
| S5 | PostTraining is Supervised Learning (2606.07527) | **2026** — Unifies all post-training as supervised |
| S6 | LLM PostTraining Unified Survey (2604.07941) | **2026** — Comprehensive survey |
| S7 | Anatomy of PostTraining (2606.12360) | **2026** — Interpretability of post-training |
| S8 | InferenceCompute Shapes Frontier Eval (2606.17930) | **2026** — How test-time compute changes eval |
| S9 | MoE-GRPO (2603.24984) | **2026** — RL for expert routing in MoE |

### CORE: Mixture-of-Experts Architecture (15 papers)
| # | Paper | Year | Key insight |
|---|-------|------|-------------|
| 06 | MoE Survey | 2024 | Comprehensive overview |
| 07 | AquilaMoE | 2024 | Efficient MoE training |
| 08 | BigMac | 2024 | Communication-efficient MoE |
| 12 | DeepSeek V2 MoE | 2024 | Production MoE reference |
| 30 | MoE Surpass Dense | 2026 | MoE beats dense under equal resource |
| 31 | Orthogonal Growth MoE (ICML 2026) | 2026 | Recycle checkpoints, grow params |
| 32 | SYMI MoE | 2025 | 30% faster training |
| 33 | MoE Comprehensive Survey (10.6 MB) | 2025 | Complete reference |
| 49 | MegaScale MoE | 2025 | 352B MoE on 1,440 GPUs |
| S10 | SymbioticMoE (2604.07753) | **2026** | Multimodal MoE architecture |
| S11 | Routing Distraction MoE (2604.08541) | **2026** | Router problems in multimodal MoE |
| S12 | Lightweight MoE LiME (2604.02338, 13.5 MB) | **2026** | Efficient MoE design |
| S14 | Scaling Laws MoE (2507.17702) | 2025 | 300+ models for MoE scaling laws |

### CORE: Data & Synthetic Data (12 papers)
| # | Paper | Year | Key insight |
|---|-------|------|-------------|
| 18 | Multilingual Data Selection (NeurIPS 2025) | 2025 | Model-based selection |
| 19 | Train Data-Efficient LLMs (AskLLM) | 2024 | Reject 90% data |
| 24 | Curriculum Learning | 2024 | Data ordering |
| 25 | Synthetic Data Robustness | 2025 | When it helps vs hurts |
| 36 | D4: Data Dedup | 2023 | 20% efficiency gain |
| 47 | Demystifying Synthetic Data (5.9 MB) | 2025 | Optimal ratio ~30% |
| 51 | SynthLLM Scaling Laws | 2025 | Predictable synthetic scaling |
| S15 | DataConstrained Pretraining + SoftQ (2606.06888) | **2026** | Training with limited data |
| S16 | Scaling Laws Distillation (2606.24747) | **2026** | Scaling laws for distillation |
| S17 | Scaling Laws Data Composition (2606.19781) | **2026** | How data mix affects scaling |

### CORE: World Models & Multimodal (9 papers)
| # | Paper | Year | Key insight |
|---|-------|------|-------------|
| 13 | LLaDA | 2025 | Language diffusion models |
| 45 | Genie (40.4 MB) | 2024 | First foundation world model |
| 46 | Scaling Laws Native Multimodal (Apple ICCV 2025) | 2025 | Early-fusion > late-fusion |
| S18 | Beyond Language Modeling (2603.03276, 12.5 MB) | **2026** | Multimodal pretraining at scale |
| S19 | Looped World Models (2606.18208) | **2026** | Survey of world model architectures |
| S20 | MultimodalPretraining (2603.03276) | **2026** | Full multimodal pretraining pipeline |
| S21 | Qwen3.5-Omni | **2026** | Alibaba's native multimodal MoE |

### CORE: Efficiency & Optimization (9 papers)
| # | Paper | Year | Key insight |
|---|-------|------|-------------|
| 01 | Foundations of LLMs | 2023 | Core knowledge |
| 02 | Understanding LLMs | 2024 | Training pipeline |
| 03 | M3 Scaling Law | 2024 | Scaling for efficient LMs |
| 04 | Efficient Continual Pretraining | 2024 | CPT methodology |
| 20 | Compact LMs (Minitron) | 2024 | Pruning + distillation |
| 48 | BitNet b1.58 | 2025 | Native 1-bit LLM |
| S22 | ROSE Pruning (2603.05878, 8.3 MB) | **2026** | One-shot LLM pruning |
| S23 | MOCAP LLM Inference (2606.22968) | **2026** | Efficient inference methods |
| S24 | Morpheus Tokenizer (2606.18717) | **2026** | Morphology-aware tokenization |

### CORE: African Context (8 papers) — for Mission 2 (accessibility)
| # | Paper | Year | Relevance |
|---|-------|------|-----------|
| 05 | State of LLMs for African Languages | 2024 | Landscape |
| 09 | AfroBench | 2025 | 64 languages benchmark |
| 10 | ASR for African Languages | 2023 | Voice interfaces |
| 14 | AfriqueLLM | 2026 | CPT for African languages |
| 15 | SozKZ | 2026 | 50M-600M template |
| 17 | MzansiLM | 2026 | South African LM |
| 34 | IrokoBench (NAACL 2025) | 2025 | 17 languages benchmark |
| 35 | Lugha-Llama | 2025 | Adapting LLMs for African languages |
| S25 | African NLI Scaling (2606.03219) | **2026** | Data scaling for African NLI |

## Documents Updated/Created
- `projects/KORA/02_MISSION.md` — EN V1.0 (mission-driven, sovereign frontier)
- `projects/KORA/11_STRATEGIC_PRINCIPLES.md` — 20 permanent principles
- `projects/KORA/12_NORTH_STAR.md` — "Increase Africa's Sovereign AI Capability"
- `concepts/TIMELINE.md` — Event added
- `concepts/KNOWLEDGE.md` — Frontier training recipe added
- `State/CURRENT_STATE.md` — Refocused
- `ANCHORED_SUMMARY.md` — This file

## Reading Order
1. **Foundation**: 02_MISSION → 11_STRATEGIC_PRINCIPLES → 12_NORTH_STAR
2. **Frontier Recipe**: 37 (Llama 3) → 38 (DeepSeek-V3) → S1 (DeepSeek V4)
3. **Post-training 2026**: S5→S6→S7→S8 (all 2026 papers)
4. **MoE 2026**: S10→S11→S12→30→31
5. **Data 2026**: S15→S16→S17→47
6. **Multimodal 2026**: S18→S19→S20→S21
7. **Efficiency 2026**: S22→S23→48→20
