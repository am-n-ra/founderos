# Kora Lab — Infrastructure & Cost Analysis: Building from Lomé, Togo

> Based on 18+ searches across cost-of-living, cloud compute, mobile money, datasets, hosting, and regional benchmarks. June 2026.

---

## 1. MONTHLY BURN ESTIMATE (Minimum Viable)

| Category | Item | Cost (USD) | Cost (CFA) | Notes |
|---|---|---|---|---|
| **Living** | 1BR apartment (outside centre) | $74 | 45,000 CFA | Numbeo |
| **Living** | Utilities (electricity, water, garbage) | $140 | 85,905 CFA | Togo grid is unstable; includes cooling |
| **Living** | Food (basic, self-cook) | ~$80–120 | 50–75K CFA | Local markets are cheap |
| **Living** | Mobile phone plan (10GB+ data) | $20 | 12,500 CFA | Togocel / Moov |
| **Internet** | Broadband fiber/ADSL (60 Mbps) | $41 | 25,000 CFA | Togo Telecom / CAFE |
| **Hosting** | Render/Railway API backend | $7–25 | — | Standard tier web service |
| **Hosting** | PostgreSQL database (free tier) | $0 | — | Render/Neon free tiers exist |
| **Compute** | Hugging Face PRO (inference credits) | $9 | — | 20x inference credits included |
| **Compute** | Colab GPU (T4) — occasional training | ~$30–60 | — | ~20–40 hrs/mo @ $0.42/hr |
| **Storage** | HF Hub storage (public repos) | ~$0–2 | — | 10GB public is essentially free |
| **Domain** | Custom domain | ~$10/yr ($0.83/mo) | — | .tg or .com |
| **Total Burn** | **Lean / pre-revenue** | **~$402–492/mo** | **~245–300K CFA/mo** | |
| **Total Burn** | **Comfortable / faster dev** | **~$550–700/mo** | | More GPU time, redundant internet |

**Daily subsistence**: ~$8–12/day (local food, transport, incidentals).

### 1a. CHEAPER EXTREME BUDGET

| Item | Cost |
|---|---|
| Living with family / shared housing | $0–40/mo |
| Use coworking internet (skip home broadband) | $0 |
| Colab free tier + Kaggle + HF ZeroGPU only | $0–9 |
| API backend on PythonAnywhere free tier | $0 |
| Hugging Face Spaces free (CPU Basic) | $0 |
| **Extreme minimum** | **~$250–350/mo** |

---

## 2. ONE-TIME COSTS

| Item | Cost (USD) | Notes |
|---|---|---|
| **Company registration (Togo)** | ~$80–160 | CEPOD (Centre des Formalités); ~50–100K CFA |
| **Computer / laptop** | $400–800 | Used ThinkPad or MacBook Air M1 (imported) |
| **UPS / battery backup** | $100–200 | Essential for power instability |
| **Mobile data backup modem** | $30–60 | 4G dongle for grid-down internet |
| **Data collection (recording sessions)** | $200–1,000+ | Per language; recording equipment + speaker stipends |
| **Total One-Time** | **~$810–2,220** | Non-recurring setup |

---

## 3. INFRASTRUCTURE RISK MATRIX

| Risk | Severity | What breaks first | Mitigation |
|---|---|---|---|
| **Power outages** | HIGH | Grid drops 2–6 hrs/day in some areas; dev/training interrupted, corrupted writes | UPS (essential); laptop battery; work in coworking spaces |
| **Internet instability** | MEDIUM–HIGH | ADSL throttles; fiber cuts; latency spikes to EU/US cloud | Dual-WAN (fiber + 4G backup); work async/offline when needed |
| **Payment processing** | HIGH | No Stripe, no PayPal payouts. T-Money & Flooz only. Flutterwave/Telesom support varies | Use Flutterwave (Togo supported? partial); partner with a Nigerian entity for Stripe |
| **No local GPU compute** | HIGH | Can't train TTS models locally on laptop | Colab, Kaggle, Vast.ai, HF ZeroGPU (free), Lambda GPU |
| **Cloud latency** | MEDIUM | AWS Cape Town is ~4,000 km from Lomé vs. Europe ~5–6,000 km — similar | Use EU regions (Paris/Frankfurt); latency for TTS inference not critical |
| **Currency risk** | LOW–MEDIUM | XOF (CFA) pegged to EUR — stable; but paying USD cloud bills is FX friction | Wise/Revolut? Not available easily. Flutterwave USD card. |
| **Talent/community isolation** | MEDIUM | No deep AI community in Lomé; few meetups | Remote networking; join Zindi, Data Science Africa, HF Discord |
| **Device failure** | MEDIUM | Local repair shops exist but no official Apple/ThinkPad parts | Buy rugged/stick to common brands; have a backup plan |

---

## 4. COST COMPARISON: Building from Lomé vs. Alternatives

| Factor | **Lomé (Togo)** | **Lagos (Nigeria)** | **Nairobi (Kenya)** | **Remote (Europe/NA)** |
|---|---|---|---|---|
| **Monthly living cost** | $250–350 | $400–700 | $350–600 | $2,000–4,000+ |
| **Internet** | ADSL/fiber ~$41; 4G backup ~$20 | Fiber ~$50–80; 4G ~$25 | Fiber ~$60–100 | $50–100 |
| **Power reliability** | Unstable (grid drops) | Unstable + generator = $100+/mo fuel | Unstable + generator | Stable |
| **Payment processing** | Mobile money only (T-Money, Flooz) | Flutterwave, Paystack, Stripe (partial) | M-Pesa, Flutterwave, Stripe | Stripe, PayPal, full stack |
| **GPU access** | None local (all cloud) | Some local GPU rental | Some local GPU rental | Direct cloud, on-prem |
| **Closest AWS region** | EU (Paris/Frankfurt) or Cape Town | EU (Paris) ~6ms worse | Cape Town / EU | On-region |
| **Startup ecosystem** | Nascent (few incubators) | Strong (Y Combinator, CcHub) | Strong (iHub, Safaricom) | Mature |
| **Regulatory ease** | Simple registration (~$80–160) | Complex (CAC, tax, etc.) | Moderate | High |
| **Overall monthly burn (lean)** | **$400–500** | **$700–1,200** | **$600–1,000** | **$2,500–5,000+** |
| **Verdict** | Cheapest but riskiest | More stable, more options | Best balance | Cost-prohibitive |

**For a solo pre-revenue founder, Lomé gives you ~6–12 months runway on $3,000 savings vs. ~2–3 months in Lagos or Nairobi.**

---

## 5. FUNDING PATH: Bootstrapping Feasibility

### Bootstrapping: **Feasible but tight**

- You can survive on **~$400–500/mo**
- If Kheir has **$3,000–5,000 in savings**, that's **6–10 months of runway**
- Speed to **first revenue is critical** — don't aim for foundation model training, aim for an API service

### Grants Available (African AI/startup focused)

| Grant | Amount | Notes |
|---|---|---|
| **Google AI Accelerator (Africa)** | $100k–$250k + credits | Selective, but Africa-focused |
| **AWS Activate (startup credits)** | $1k–$100k in credits | Any registered startup |
| **Hugging Face Community GPU Grant** | Free GPU hours | For open-source TTS models |
| **Lacuna Fund** | $50k–$200k | African language datasets specifically |
| **Mozilla Technology Fund** | $50k–$100k | Open-source, Common Voice aligned |
| **Orange Digital Center (Togo)** | Incubator + small grants | Free coworking + mentoring in Lomé |
| **Fonds d'Appui aux PME (Togo)** | Local grants (converted) | ~$5,000–15,000 USD equiv |
| **AI4D Africa / IDRC** | $50k–$250k | AI research for development |
| **Zindi / Data Science Africa** | Prizes + grants | Competition-based |
| **GitHub / GitLab startup credits** | Free hosting | For the code stack |
| **Togolese diaspora angel investors** | Variable | Growing interest |

### Recommended funding strategy

1. **Month 1–3**: Bootstrap on savings ($400/mo). Build MVP on free tiers (HF Spaces, Colab, Render free, PythonAnywhere).
2. **Month 4–6**: Apply for Lacuna Fund + Orange Digital Center + HF GPU grants. Target $15k–50k.
3. **Month 6–9**: First revenue from API usage (mobile money payments). Prove traction.
4. **Month 9–12**: Apply to Y Combinator / Google AI Accelerator / AI4D with traction.

---

## 6. PAYMENT PROCESSING — THE ELEPHANT

This is the **most dangerous constraint**.

| Method | Works in Togo? | Estimated Fee |
|---|---|---|
| **Stripe** | ❌ No | N/A |
| **PayPal payouts** | ❌ No | N/A |
| **Flutterwave** | ✅ Partial (mobile money) | ~2.9% + $0.30 (card); 1.4% mobile money |
| **Paystack** | ❌ No (Nigeria only) | N/A |
| **T-Money API** | ✅ Direct (Togocel) | Negotiable with Togocel |
| **Flooz API** | ✅ Direct (Moov) | Negotiable with Moov |
| **Hub2** | ✅ (Fintech startup in Togo/Benin) | ~1.5–3% |
| **Direct Orange Money Africa** | ✅ | ~1–3% |
| **Stripe Atlas + US entity** | ✅ (costly) | ~$500/year + ongoing legal |

**Real talk**: Without Stripe, you cannot easily collect international payments. Your options:
1. **Flutterwave**: Supports mobile money (T-Money, Flooz) for African customers. For international, Flutterwave also takes Visa/MC.
2. **Hub2** (hub2.co): Built in West Africa specifically for Francophone Africa mobile money.
3. **Stripe Atlas**: Incorporate in Delaware ($500), get a US bank account, use Stripe. But you need a US address/someone stateside.
4. **Partnership**: Find a Nigerian or Kenyan co-founder who can use Paystack/Flutterwave Nigeria.

**Workaround for MVP**: Charge via Flutterwave mobile money links. Payout to T-Money/Flooz wallet.

---

## 7. DATA & MODEL TRAINING — KEY COST DRIVERS

### Datasets for African Language TTS

| Dataset | Languages | Size | Cost | Commercial Use? |
|---|---|---|---|---|
| **Mozilla Common Voice** | ~7 African languages (Ewe, Twi, Swahili, etc.) | ~10–100 hrs per lang | FREE | CC-0 (public domain) — safe commercially |
| **WAXAL** (West African cross-language) | Fon, Ewe, Yoruba, etc. | ~50–500 GB raw audio | FREE download | Check license (likely research-only) |
| **Alffa Dataset** | Amharic, Swahili, Hausa, Wolof | Variable | FREE | Check per-language |
| **Google Crowdsource** recordings | Various African | Limited | FREE | Not always commercial |
| **Custom recordings** | Ewe, Kabiyé, Mina, etc. | ~100 hrs per lang = ~50 GB | ~$500–2,000 | Full ownership |

**For MVP**: Start with Common Voice Ewe + transfer learning from English TTS.

### Training Cost Estimates (TTS model)

| Task | GPU Needed | Time | Cost |
|---|---|---|---|
| Fine-tune Coqui TTS (~80M params) | T4 (16GB) | 2–4 hrs | ~$1–2 |
| Train medium model (300M params) | L4 (24GB) or A10G | 8–24 hrs | ~$8–40 |
| Train XTTS v2 (1.6B params) | A100 (80GB) | 24–48 hrs | ~$60–120 |
| Inference (per 1M chars) | CPU or T4 | — | ~$0.50–5 on HF Inference API |

---

## 8. INFRASTRUCTURE STACK — RECOMMENDED FOR LOMÉ

```
┌─────────────────────────────────────────────┐
│  Model training:    Colab / Kaggle / Vast.ai │
│  Model storage:     Hugging Face Hub (free)  │
│  Inference API:     HF Spaces (ZeroGPU)      │
│                    or HF Inference Endpoints  │
│  App backend:       Render (Standard $25)    │
│  Database:          Render Postgres (free)   │
│  File storage:      HF Hub / Backblaze B2    │
│  Monitoring:        Sentry (free tier)       │
│  Auth:              Clerk / Supabase (free)  │
│  Payments:          Flutterwave / Hub2       │
│  Domain:            Namecheap or local .tg   │
│  CI/CD:             GitHub Actions (free)    │
│  Code:              GitHub (free)            │
└─────────────────────────────────────────────┘
```

---

## 9. VERDICT

### Is Togo a viable base for an AI startup in 2026?

**Yes — but with significant caveats.**

| Factor | Verdict |
|---|---|
| **Living cost** | ✅ Strong advantage. ~$400/mo all-in is world-class cheap. |
| **Power** | ⚠️ Must budget $100–200 for UPS + backup. Adds friction. |
| **Internet** | ⚠️ Marginal. ADSL works in Lomé but you need a 4G backup plan. |
| **GPU/compute** | ❌ Minimal issue — everything is in the cloud anyway. Colab, Vast.ai, HF work. |
| **Payments** | 🚨 **Most dangerous constraint.** Must solve Flutterwave/Hub2 integration before launch. |
| **Talent/community** | ⚠️ You're alone. Remote community is essential (Discord, Zindi, etc.) |
| **Fundraising** | 🔄 Grants exist but you'll compete globally for them. |

### Brutal truth

> Lomé gives you **runway advantage** (cheapest living on the continent for a tech founder). But it also gives you **payment isolation** and **infrastructure friction**. The best strategy is to stay in Lomé for the low burn, but structure the company (or partner) so you have a payment gateway that works.

**If Kheir has $5,000 saved and can survive on $400/mo, that's ~12 months to build, launch, and reach revenue. That is enough time to build a real business — if the payments problem is solved from day one.**

### Recommended action items (next 30 days)

1. [ ] Register Kora Lab at CEPOD in Lomé (~50K–100K CFA)
2. [ ] Buy a UPS (CyberPower / APC ~$100) — non-negotiable
3. [ ] Set up dual-WAN: fiber primary + 4G USB modem backup
4. [ ] Build MVP on free tiers only: Colab + HF Spaces + Render free + GitHub
5. [ ] Integrate Flutterwave mobile money (T-Money / Flooz) for first payments
6. [ ] Apply for Hugging Face Community GPU Grant + Orange Digital Center incubator
7. [ ] Join Zindi, HF Discord, Data Science Africa for remote community
8. [ ] Download Common Voice Ewe + start fine-tuning Coqui TTS on Colab free
9. [ ] Set up Stripe Atlas or find a partner for international payment processing
10. [ ] Target first paying API customer within 90 days
