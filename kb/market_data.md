# AI Pricing Research — Market Data

## Purpose

Market-level context for the pricing knowledge base: market sizing, enterprise spend, infrastructure investment, consumption volume trends, and adoption metrics. These provide the macro backdrop against which token-price dynamics should be interpreted.

## Data points

### Market sizing

| Metric | Value | Year | Source |
|---|---|---|---|
| AI market size | $390.9 billion | 2025 | Grand View Research |
| AI market size (projected) | $539.5 billion | 2026 | Grand View Research |
| AI market size (projected) | $3,497.3 billion | 2033 | Grand View Research |
| CAGR (2026-2033) | 30.2% | — | Grand View Research |

### Enterprise spend

| Metric | Value | Period | Source |
|---|---|---|---|
| Enterprise LLM spend | $3.5 billion | Late 2024 | Menlo research (cited in token collapse substack) |
| Enterprise LLM spend | $8.4 billion | Mid 2025 | Menlo research (cited in token collapse substack) |
| Enterprise LLM spend growth | 2.4x in 6 months | Late 2024 -> mid 2025 | Calculated from above |
| Average AI-native software budget share | 2.3% | January 2025 | Tropic AI pricing trends |
| Average AI-native software budget share | 4.8% | July 2026 | Tropic AI pricing trends |
| Top-decile AI-native budget share | 10% → 13% | June -> July 2026 | Tropic AI pricing trends |
| AI-native spend growth | Nearly 2x | 2025 (full year) | Zylo AI cost blog |

### Token consumption volume

| Provider | Volume | Period | Source |
|---|---|---|---|
| Google Gemini | 9.7 trillion tokens/month | ~2023 | Google I/O 2026 (Sundar Pichai cited in substack) |
| Google Gemini | 3.2 quadrillion tokens/month | 2026 | Google I/O 2026 (Sundar Pichai cited in substack) |
| Google Gemini volume growth | ~330x in 2 years | 2023 -> 2026 | Calculated from above |

### Infrastructure investment

| Metric | Value | Year | Source |
|---|---|---|---|
| Big 4 hyperscaler AI capex (Amazon, Alphabet, Microsoft, Meta) | $370B-$410B | 2025 | Josh Bersin / Bridgewater estimate |
| Big 4 hyperscaler AI capex (projected) | $650B | 2026 | Bridgewater estimate via Josh Bersin |
| Broader AI data-center builder universe (incl. Oracle, CoreWeave, xAI/SpaceX) | ~$500B annualized | 2026 | Josh Bersin analysis |
| Broader AI infrastructure run-rate (projected) | $6.3 trillion | 2030 | Gartner forecast via Josh Bersin |
| Practical AI infrastructure run-rate | approaching $1 trillion | 2026 | Calculated from above |

### Price dynamics

| Metric | Value | Period | Source |
|---|---|---|---|
| Frontier model output price: GPT-4 launch | $60/M tokens | March 2023 | Multiple sources |
| Frontier model output price: GPT-5.4 | $15/M tokens | 2026 | Multiple sources |
| Frontier price reduction | 4x | March 2023 -> 2026 | TokenMix |
| Frontier price reduction (conservative) | ~100x | 2023 -> 2025 | LLM Pricing History / DeployBase |
| Budget tier price reduction | 500x+ | 2023 -> 2025 | LLM Pricing History / DeployBase |
| Token price collapse | 95%+ in 3 years | 2023 -> 2026 | Token collapse substack |
| DeepSeek V3 vs GPT-4 output | $0.14 vs $60 | December 2024 vs March 2023 | DeployBase / token collapse substack |
| DeepSeek V3 output reduction | ~100x vs GPT-4 | December 2024 | Token collapse substack |
| Price reduction rate (frontier) | 9x annually | 2021 -> 2025 | Epoch AI via Coding Nexus |
| Price reduction rate (top-tier) | 900x | 2021 -> 2025 | Epoch AI via Coding Nexus |

### Adoption context

| Metric | Value | Period | Source |
|---|---|---|---|
| AI-native NDR peaked | 136% | April 2026 | Tropic AI pricing trends |
| AI-native NDR (post-peak) | Fell 2 months straight (May-June 2026) | May-June 2026 | Tropic AI pricing trends |
| Enterprise AI-native wallet share | 1.4% | January 2025 | Tropic AI pricing trends |
| Enterprise AI-native wallet share (top segments) | 5% | July 2026 | Tropic AI pricing trends |
| Software engineers using AI | All-in (majority adoption) | 2026 | Stanford AI Index 2026 via IEEE Spectrum |
| AI market growth note | Adoption plateaued; depth of use didn't | 2026 | Tropic AI pricing trends |

## Interpretation notes

- **Price collapse + volume explosion = total spend still rising.** The token price dropped 95%+ while Google's volume grew 330x — consumption rose far faster than prices fell. Enterprise LLM spend doubled in 6 months despite price drops.
- **The price floor is unclear.** DeepSeek V3 at $0.14/$0.28 per 1M tokens was frontier-quality output at 100x cheaper than GPT-4's launch price. OpenRouter free models go further (zero per-token cost) but with tight rate limits.
- **Consolidation and price wars are accelerating.** July 2026 saw major price cuts across OpenAI (GPT-5.6 family), Anthropic (Sonnet 5), and DeepSeek (V4 series). The GPT-5.6 Luna 80% cut was described as 'the largest price move since the GPT-5 launch.'
- **Context window race.** Context windows expanded from 9K (Claude 1, 2023) to 128K standard to 1M+ as the new baseline for frontier models. Long-context pricing models diverged: flat-rate (Anthropic) vs tiered surcharges (Google, OpenAI).
- **Infrastructure spending is the macro story.** $410B (2025) approaching $1T (2026) in AI infrastructure investment — this is the supply-side pressure that eventually enables cheaper inference, but it's also the capital that funds the price war.

## Sources

- Grand View Research: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market
- Token collapse substack: https://thegtmnewsletter.substack.com/p/ai-token-price-collapse-costs-rising
- Tropic AI pricing trends: https://www.tropicapp.io/blog/ai-pricing-trends
- Zylo AI cost: https://zylo.com/blog/ai-cost
- Josh Bersin AI pricing: https://joshbersin.com/2026/05/ai-prices-are-going-up-up-up-and-what-this-means-for-enterprise-ai
- IEEE Spectrum Stanford AI Index 2026: https://spectrum.ieee.org/state-of-ai-index-2026
- Coding Nexus AI costs: https://medium.com/coding-nexus/ai-costs-are-going-down-where-is-market-going-abb054a6715a
- Epoch AI (via Coding Nexus): included in above
- DeployBase LLM pricing history: https://deploybase.ai/articles/llm-pricing-history-how-costs-dropped-99-since-2023
- TokenMix AI API pricing history: https://tokenmix.ai/blog/ai-pricing-trends-history
