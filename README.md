# AI Pricing Research

Historical and current AI model pricing data — LLM API costs, market landscape, free models, and provider comparisons. Built as a local knowledge base for trend analysis and sentiment correlation.

## Structure

- `kb/price_points_*.jsonl` — canonical structured datasets (one JSONL file per provider):
  - `price_points_openai.jsonl` (37 entries, 2020-2026)
  - `price_points_anthropic.jsonl` (27 entries, 2023-2026)
  - `price_points_google.jsonl` (31 entries, 2023-2026)
  - `price_points_deepseek.jsonl` (9 entries, 2023-2026)
  - `price_points_xai.jsonl` (5 entries, 2025-2026)
- `kb/market_data.md` — market-level context (sizing, spend, infrastructure, adoption)
- `kb/PRICE_POINTS_SPEC.md` — data contract and field definitions
- `kb/INDEX.md` — source registry and retrieval metadata
- `kb/CONVENTIONS.md` — project-level accuracy instructions
- `reports/` — formatted markdown reports derived from the dataset
- `notes/` — source digests and extraction notes
- `scripts/` — fetchers, parsers, loaders

## Current totals

- **111 price points** across 5 providers (OpenAI 37, Anthropic 27, Google 31, DeepSeek 11, xAI 5)
- **17 sources** catalogued (provider pricing pages, aggregators, market analysts)
- Time span: **2020 through projected 2027** (Gemini 3.8 Flash Jan 2027 rate)

## Quick start

```bash
cd ~/code/BUTTERGANG/ai-pricing-research

# Inspect the dataset
wc -l kb/price_points_*.jsonl
head -5 kb/price_points_openai.jsonl

# Convert to CSV for analysis
python3 -c "
import json, csv, glob
with open('kb/all_price_points.csv', 'w', newline='') as out:
    w = csv.writer(out)
    w.writerow(['id','provider','model_name','effective_date','input_price','output_price','price_type','context_window','source_url'])
    for f in sorted(glob.glob('kb/price_points_*.jsonl')):
        for line in open(f):
            d = json.loads(line)
            w.writerow([d.get(k) for k in ['id','provider','model_name','effective_date','input_price_usd_per_mtokens','output_price_usd_per_mtokens','price_type','context_window_tokens','source_url']])
"
cat kb/all_price_points.csv | head -5
```

## Accuracy conventions

See `kb/CONVENTIONS.md` and `kb/PRICE_POINTS_SPEC.md` for the data-quality rules we follow (model/version tracking, list vs effective price, effective-date timestamps, source attribution, blended-rate handling).

## Adding new data

1. Pick the right provider file (or add a new `price_points_<provider>.jsonl` if the provider doesn't exist).
2. Find the next available `id` (highest in the file + 1).
3. Follow the field spec in `kb/PRICE_POINTS_SPEC.md`.
4. Prefer `provider_pricing_page` as `source_type` when available; note any discrepancies in `notes`.
5. Commit with a message like `Add <Provider> price points (N entries)`.

## Sources — canonical pricing pages

- OpenAI: https://developers.openai.com/api/docs/pricing
- Anthropic: https://platform.claude.com/docs/en/about-claude/pricing
- Google Gemini: https://ai.google.dev/gemini-api/docs/pricing
- DeepSeek: https://api-docs.deepseek.com/quick_start/pricing/
- xAI: https://docs.x.ai/developers/pricing

## Sources — aggregators and market data

See `kb/INDEX.md` for the full registry.
