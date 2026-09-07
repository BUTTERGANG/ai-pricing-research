# AI Pricing Research — Data Index

## Dataset

- `kb/price_points_*.jsonl` — canonical structured datasets (one JSONL file per provider):
  - `price_points_openai.jsonl` (37 entries, 2020-2026)
  - `price_points_anthropic.jsonl` (27 entries, 2023-2026)
  - `price_points_google.jsonl` (31 entries, 2023-2026)
  - `price_points_deepseek.jsonl` (11 entries, 2023-2026)
  - `price_points_xai.jsonl` (5 entries, 2025-2026)
  - `price_points_mistral.jsonl` (TBD)
  - `price_points_cohere.jsonl` (TBD)
  - `price_points_meta_llama.jsonl` (TBD — open-weight, hosted pricing)
  - `price_points_alibaba_qwen.jsonl` (TBD)
  - `price_points_moonshot_kimi.jsonl` (TBD)
  - `price_points_openrouter_free.jsonl` (TBD — free-tier models)
- `PRICE_POINTS_SPEC.md` — field definitions, version-tracking rules, price-type taxonomy, effective-date rules, source attribution, and maintenance conventions.
- `CONVENTIONS.md` — project-level accuracy instructions (originally supplied by the user).

## Reports

- `reports/` — formatted markdown reports derived from the dataset.

## Notes

- `notes/` — source digests, extraction notes, and per-provider timelines.
- `scripts/` — fetchers, parsers, loaders, and helpers.

## Sources (initial set, to be expanded)

### Provider pricing pages (canonical)
- OpenAI: https://developers.openai.com/api/docs/pricing
- Anthropic: https://platform.claude.com/docs/en/about-claude/pricing
- Google Gemini: https://ai.google.dev/gemini-api/docs/pricing
- DeepSeek: https://api-docs.deepseek.com/quick_start/pricing/
- xAI: https://docs.x.ai/developers/pricing

### Aggregators
- CloudZero: https://www.cloudzero.com/blog/openai-pricing/
- CloudZero Claude: https://www.cloudzero.com/blog/claude-pricing/
- Metacto Gemini: https://www.metacto.com/blogs/the-true-cost-of-google-gemini-a-guide-to-api-pricing-and-integration
- Metacto OpenAI: https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance
- IntuitionLabs: https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025
- TokenCost: https://tokencost.app/blog/ai-price-index
- APIScout: https://apiscout.dev/guides/llm-api-pricing-comparison-2026
- ChatForest: https://chatforest.com/guides/llm-api-pricing-comparison-2026/
- DeployBase: https://deploybase.ai/articles/cost-per-token-over-time-how-llm-api-pricing-has-dropped
- TokenMix: https://tokenmix.ai/blog/ai-pricing-trends-history

### Market data
- Grand View Research AI market: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market
- Anthropic Economic Index (March 2026): https://www.anthropic.com/research/economic-index-march-2026-report
- Zylo AI cost: https://zylo.com/blog/ai-cost
- Josh Bersin AI pricing: https://joshbersin.com/2026/05/ai-prices-are-going-up-up-up-and-what-this-means-for-enterprise-ai
- IEEE Spectrum Stanford AI Index 2026: https://spectrum.ieee.org/state-of-ai-index-2026
- Tropic AI pricing trends: https://www.tropicapp.io/blog/ai-pricing-trends
- Token price collapse (Substack): https://thegtmnewsletter.substack.com/p/ai-token-price-collapse-costs-rising
- White House CEA report: https://www.whitehouse.gov/wp-content/uploads/2026/01/Artificial-Intelligence-and-the-Great-Divergence-5.pdf

## Retrieval metadata

All entries in this initial load were retrieved on 2026-09-07 by Hermes Agent (Solar Pro4 via Nous Portal), for the AI Pricing Research knowledge base.
