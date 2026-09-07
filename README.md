# AI Pricing Research

Historical and current AI model pricing data — LLM API costs, market landscape, free models, and provider comparisons. Built as a local knowledge base for trend analysis and sentiment correlation.

## Structure

- `kb/` — knowledge base data (structured JSON + markdown reports)
- `reports/` — formatted markdown reports
- `notes/` — research notes and source digests
- `scripts/` — tooling (fetchers, parsers, loaders)

## Accuracy conventions

See `kb/CONVENTIONS.md` for the data-quality rules we follow (model/version tracking, list vs effective price, effective-date timestamps, source attribution).

## Quick start

```bash
cd ~/code/BUTTERGANG/ai-pricing-research
ls kb/ reports/
```

## Sources

Pricing pages and aggregators for OpenAI, Anthropic, Google, DeepSeek, xAI, OpenRouter, and market data (see report bibliographies).
