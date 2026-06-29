# KORA — Key Decisions

## Strategic Decisions

### 1. KORA is a research laboratory, not a fine-tuning studio
- KORA trains original models from scratch across all categories: LLM, image, video, audio
- Fine-tuning does not produce world-class models. Training from scratch allows original architecture, native performance, total control, real sovereignty.
- Source: 05_STRATEGIC_PLAN.md

### 2. First model: LLM small (1-7B parameters) trained from scratch
- Architecture inspired by DeepSeek MoE or Qwen
- Focused on multilingual + cross-lingual performance (input Ewe → output Ewe, input Ewe → output English/Chinese, etc.)
- Trainable on available resources (ST Digital or rental)
- Architecture efficient, MoE from day one
- Source: 05_STRATEGIC_PLAN.md

### 3. Voice is the inclusion layer, not a replacement for text
- Text interface for educated users, developers, enterprises (standard global: prompt → response)
- Voice interface for non-literate users, inclusion (speak → model understands → model responds in voice)
- Same backend model, two frontends
- Source: 05_STRATEGIC_PLAN.md

### 4. Two loops in parallel, not two phases
- Loop A (Training): Build models — the engine
- Loop B (Distribution): Access — smartphones, wearables, fixed devices, voice API
- Both advance in parallel because they share the same engine: training models
- Source: 05_STRATEGIC_PLAN.md

### 5. Asset mapping: compute is no longer the bottleneck
- Kaggle T4x2 at 30h/week per account, 10 accounts = 300h/week
- Sufficient to train 300-500M params MoE model in 1-2 weeks
- The real gaps are: Ewe data collection and stable revenue
- Source: 04_ASSET_MAPPING.md

### 6. Capital philosophy: mission before money
- Raise only when additional capital creates additional capability
- Founder revenue → services → products → grants → strategic partnerships → compute sponsorship → mission-aligned investment → institutional capital
- Never optimize for valuation over capability
- Source: 17_CAPITAL_ROADMAP.md

### 7. 20 Strategic Principles adopted
- Including: Mission Before Company, Capability Before Valuation, Train Before Fine-Tune, World-Class Or Nothing, Compound Everything, Build Infrastructure Before Applications
- Source: 11_STRATEGIC_PRINCIPLES.md

### 8. North Star defined
- "Increase Africa's Sovereign Artificial Intelligence Capability until importing frontier AI is no longer a strategic necessity"
- Measured across 5 dimensions: Frontier Capability, Sovereignty, Accessibility, Ecosystem Growth, Institutional Strength
- Source: 12_NORTH_STAR.md

## Operational Decisions

### 9. First language: Ewe
- Founder speaks Ewe → direct entry point for Link 2
- Urgent need: structured Ewe data collection
- Source: 04_ASSET_MAPPING.md

### 10. Hiring philosophy: prioritize local African talent
- African local talent > African diaspora > global specialists
- First hires: Lead ML Engineer (Month 1), Data Engineer (Month 2), Field Operations Lead (Month 2), Linguistic Consultant Network
- Source: annexes/A2_HIRING_PLAN.md

### 11. Language expansion stages
- Stage 1 (2026-27): Ewe validation
- Stage 2 (2027-29): 5-10 languages (Ewe, Kabye, Fon, Yoruba, Twi, Wolof)
- Stage 3 (2029-32): 20-50 languages
- Stage 4 (2032+): global underrepresented languages
- Source: annexes/A6_LANGUAGE_EXPANSION.md

### 12. Pre-seed target: $100K-250K at 5-10%
- Purpose: team, Language Acquisition Engine validation, ASR + TTS, dataset
- Max acceptable dilution: 10%
- Source: annexes/A_CAP_TABLE.md, A8_FUNDING_DILUTION.md

### 13. Phase 1 budget: $250K allocation
- Team (54%): $135K
- Data Collection (20%): $50K
- Infrastructure (5%): $12.5K
- Legal/Corporate (5%): $12.5K
- Operations (6%): $15K
- Research/Experimentation (4%): $10K
- Reserve (6%): $15K
- Source: annexes/A1_BUDGET.md

### 14. Sprint 1 priorities (Days 1-14)
- Setup compute (confirm ST Digital GPU)
- Architecture research (select architecture for first model)
- Dataset pipeline (start training data collection, not fine-tuning)
- Voice prototype (STT/TTS POC)
- Source: 06_ROADMAP.md

## Partnership Decisions

### 15. ST Digital partnership pursued
- GPU compute access, strategic alignment on African technological autonomy
- Status: estimation sent, awaiting formalization
- Multi-provider strategy to avoid single point of failure
- Source: annexes/A4_ST_DIGITAL_PARTNERSHIP.md

### 16. HAIDI grant as primary funding target
- $38K, deadline July 17, 2026 (J-19 as of June 28)
- Would unlock compute, data collection, development
- Priority absolute until deadline
- Source: 04_ASSET_MAPPING.md

---

| Field | Value |
|-------|-------|
| Source | All V4 documents |
| Last Updated | 2026-06-29 |
