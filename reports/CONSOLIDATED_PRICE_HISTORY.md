# AI Pricing Research — Consolidated Report

**Generated:** 2026-09-07 — from `kb/price_points_*.jsonl` (116 entries across 5 providers)

---

## Table of Contents

- [1. How to read this report](#1-how-to-read-this-report)
- [2. OpenAI pricing history](#2-openai-pricing-history)
- [3. Anthropic pricing history](#3-anthropic-pricing-history)
- [4. Google / Gemini pricing history](#4-google--gemini-pricing-history)
- [5. DeepSeek pricing history](#5-deepseek-pricing-history)
- [6. xAI / Grok pricing history](#6-xai--grok-pricing-history)
- [7. Cross-provider comparison — current prices (late 2026 snapshot)](#7-cross-provider-comparison--current-prices-late-2026-snapshot)
- [8. Market data](#8-market-data)
- [9. Sources](#9-sources)

---

## 1. How to read this report

Each price entry is presented as a row in a table. The columns are:

| Field | Meaning |
|-------|---------|
| **Model** | Exact model name and version as published |
| **Effective date** | When the price took effect (not article date) |
| **Input $/M tok** | Standard list input price per 1M tokens |
| **Output $/M tok** | Standard list output price per 1M tokens |
| **Price type** | `standard_list`, `batch`, `cache`, `promo`, `tiered`, `free` |
| **Context** | Context window at this price point (if known) |
| **Source** | URL where this price was read |
| **Notes** | Version notes, caveats, source-type, discrepancies |

**Important conventions:**

- Price series are **not** treated as continuous across model generations. Each model name/version is pinned explicitly.
- List prices (input and output separate) are the primary basis. Batch, cache, promo, and blended rates are tagged separately.
- Effective dates are used, not publication dates.
- Source URLs are attached to every entry.

---

## 1. OpenAI pricing history

**37 price points** loaded from `kb/price_points_openai.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| GPT-3 | 2020-06-11 | $6.00 | $12.00 | standard_list | 2,049 | https://www.deploybase.ai/articles/cost-per-token-over-time-how-llm-api-pricing-has-dropped | $0.006 per 1K prompt tokens, $0.012 per 1K completion tokens. Cited by DeployBase historical timeline. No OpenAI pricing |
| GPT-3.5 Turbo | 2022-11-14 | $2.00 | $2.00 | standard_list | 4,096 | https://kickllm.com/research/llm-pricing-history.html | Pricing remained relatively stable through early 2022 per DeployBase. GPT-3.5 Turbo launched Nov 2022. Cited by multiple |
| GPT-3.5 Turbo | 2023-01-?? | $1.50 | $2.00 | standard_list | — | https://tokencost.app/blog/ai-price-index | GPT-3.5 Turbo price cut in early 2023. Output unchanged at $2.00. DeployBase cites $0.0015 per prompt token ($1.50/M) at |
| GPT-4 | 2023-03-14 | $30.00 | $60.00 | standard_list | 8,192 | https://tokencost.app/blog/ai-price-index | GPT-4 launch at $30/$60 per 1M tokens. Universal consensus across all sources as the baseline for the price-collapse nar |
| GPT-3.5 Turbo | 2023-03-?? | $0.50 | $1.50 | standard_list | — | https://tokencost.app/blog/ai-price-index | GPT-3.5 Turbo cut to $0.50/$1.50 per 1M around March 2023. TokenMix cites this as 60x cheaper than GPT-4's launch input  |
| GPT-4 Turbo | 2023-11-06 | $10.00 | $30.00 | standard_list | 128,000 | https://tokencost.app/blog/ai-price-index | Announced at OpenAI DevDay Nov 6 2023. 3x cheaper than original GPT-4. Context window expanded to 128K. |
| GPT-3.5 Turbo | 2024-01-01 | $0.50 | $1.50 | standard_list | 16,385 | https://deploybase.ai/articles/cost-per-token-over-time-how-llm-api-pricing-has-dropped | GPT-3.5 Turbo at $0.0005 per prompt token. DeployBase timeline: 2024 saw continued cost-per-token decline. 60x cheaper t |
| GPT-4o | 2024-05-13 | $5.00 | $15.00 | standard_list | 128,000 | https://pecollective.com/tools/gpt-4o-pricing/ | GPT-4o launched May 13 2024 at $5/$15 per 1M tokens. Multimodal (text+image input, text output). 50% cheaper than GPT-4  |
| GPT-4o Mini | 2024-07-18 | $0.15 | $0.60 | standard_list | 128,000 | https://pecollective.com/tools/gpt-4o-pricing/ | GPT-4o mini launched July 18 2024 at $0.15/$0.60 per 1M tokens. 97% cheaper than original GPT-4 with comparable quality  |
| GPT-4o | 2024-10-01 | $2.50 | $10.00 | standard_list | 128,000 | https://pecollective.com/tools/gpt-4o-pricing/ | GPT-4o price cut Oct 2024 to $2.50/$10 per 1M tokens. Made GPT-4o competitive with Claude 3.5 Sonnet at the time. Has no |
| GPT-4.1 | 2025-01-?? | $2.00 | $8.00 | standard_list | 1,000,000 | https://pecollective.com/tools/gpt-4o-pricing/ | GPT-4.1 launched Jan 2025 at $2/$8 per 1M tokens. Replaced GPT-4o. 1M context window. PE Collective cites this date. |
| GPT-4.1 Nano | 2025-01-?? | $0.10 | $0.40 | standard_list | — | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | GPT-4.1 Nano at $0.10/$0.40. Cited as cheapest text model in May 2026 pricing guide. Exact launch date not confirmed. |
| GPT-5 | 2026-04-?? | $1.25 | $10.00 | standard_list | 272,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html | GPT-5 launched April 2026 at $1.25/$10 per 1M tokens, 272K context. Compared to Claude 4 Opus ($15/$75). Pricing page: h |
| GPT-5 mini | 2026-04-?? | $0.25 | $2.00 | standard_list | 272,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html | GPT-5 mini at $0.25/$2.00, 272K context. Cheaper than GPT-4o with more context. |
| GPT-5.4 | 2026-04-?? | $2.50 | $15.00 | standard_list | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.4 at $2.50/$15. Cited as previous standard model. Pricing page lists it as active as of April 2026. |
| GPT-5.4 Mini | 2026-04-?? | $0.75 | $4.50 | standard_list | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.4 Mini at $0.75/$4.50. Cached input $0.075. Budget tier entry in the GPT-5.4 family. |
| GPT-5.4 Nano | 2026-04-?? | $0.20 | $1.25 | standard_list | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.4 Nano at $0.20/$1.25. Cached input $0.02. Cheapest legacy OpenAI tier per CloudZero. |
| GPT-5.4 Codex | 2026-04-?? | $1.75 | $14.00 | standard_list | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.4 Codex at $1.75/$14.00. Code-specialized. Cached input $0.175. |
| GPT-5.5 | 2026-04-24 | $5.00 | $30.00 | standard_list | 272,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | GPT-5.5 launched April 24 2026 at $5/$30 per 1M tokens. Prompts over 272K input tokens billed at 2x input / 1.5x output. |
| GPT-5.5 Pro | 2026-04-24 | $30.00 | $180.00 | standard_list | 128,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | GPT-5.5 Pro at $30/$180 per 1M tokens. Maximum capability. Source: Metacto May 2026. |
| o3 | 2025-01-?? | $2.00 | $8.00 | standard_list | 200,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | o3 at $2/$8 per 1M tokens, 200K context. Advanced reasoning, multi-step problem solving. |
| o3-mini | 2025-01-?? | $1.10 | $4.40 | standard_list | 200,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | o3-mini at $1.10/$4.40 per 1M tokens. Lightweight reasoning tasks. May 2026 pricing. |
| o3-pro | 2025-01-?? | $20.00 | $80.00 | standard_list | 200,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | o3-pro at $20/$80 per 1M tokens. Max reasoning. May 2026 pricing. |
| o4-mini-2025-04-16 | 2025-04-16 | $4.00 | $16.00 | standard_list | — | https://developers.openai.com/api/docs/pricing | Training at $100/hour. With data sharing: $2.00/$0.50/$8.00. Source: OpenAI pricing page (current). |
| GPT-5.5 Pro | 2026-04-24 | $30.00 | $180.00 | standard_list | 128,000 | https://developers.openai.com/api/docs/pricing | Current OpenAI pricing page lists GPT-5.5 Pro at $30/$180. May 2026. |
| GPT-5.6 Sol | 2026-07-09 | $5.00 | $30.00 | standard_list | 1,050,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Sol launched July 9 2026 GA at $5/$30 per 1M tokens, 1.05M context. Flagship held at same price as GPT-5.5. Clou |
| GPT-5.6 Terra | 2026-07-09 | $2.00 | $12.00 | standard_list | 1,050,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Terra at $2/$12, 1.05M context. July 30 2026: 20% cut. Undercuts GPT-5.4 ($2.50/$15). 'If your production worklo |
| GPT-5.6 Luna | 2026-07-09 | $0.20 | $1.20 | standard_list | 1,050,000 | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Luna at $0.20/$1.20, 1.05M context. July 30 2026: 80% cut — largest price move since GPT-5 launch. 4x cheaper th |
| GPT-5.6 Sol | 2026-07-09 | $10.00 | $45.00 | tiered | — | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Sol long-context pricing. Input doubles above standard context window. |
| GPT-5.6 Terra | 2026-07-09 | $4.00 | $18.00 | tiered | — | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Terra long-context pricing. |
| GPT-5.6 Luna | 2026-07-09 | $0.40 | $1.80 | tiered | — | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Luna long-context pricing. |
| GPT-5.6 Sol | 2026-07-09 | $0.50 | — | cache | — | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 family: cache reads at 10% of standard input. Cache writes bill at 1.25x input rate. |
| GPT-5.5 Pro | 2026-04-24 | $15.00 | $90.00 | batch | — | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance | GPT-5.5 Pro batch: $15/$90 per 1M tokens. All OpenAI models get 50% batch discount. |
| GPT-5.6 Luna | 2026-07-30 | $0.10 | $0.60 | batch | — | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.6 Luna batch: $0.10/$0.60. Combined with cache can yield up to 95% total savings on qualifying workloads per APISc |
| chat-latest | 2026-04-?? | $5.00 | $30.00 | standard_list | — | https://developers.openai.com/api/docs/pricing | ChatGPT model endpoint: $5/$30 per 1M tokens. Cached input $0.50. |
| gpt-5.3-codex | 2026-04-?? | $1.75 | $14.00 | standard_list | — | https://developers.openai.com/api/docs/pricing | Current OpenAI pricing page: GPT-5.3 Codex at $1.75/$14.00. Cached input $0.175. |
| GPT-5.5 | 2026-04-24 | $2.50 | $15.00 | batch | — | https://www.cloudzero.com/blog/openai-pricing/ | GPT-5.5 batch: $2.50/$15 — identical to standard GPT-5.4. If latency is not critical (results in 24h), batch is the high |

---

## 2. Anthropic pricing history

**27 price points** loaded from `kb/price_points_anthropic.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Claude 1 | 2023-03-14 | $11.02 | $32.68 | standard_list | 9,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html | Claude 1 API beta opened to early partners March 2023. 9K context window. Pricing reflected limited availability. Deploy |
| Claude 1.3 / Claude 2 | 2023-07-11 | $11.02 | $32.68 | standard_list | 100,000 | https://claudearchive.com/pricing-history | Claude 2 API offered at same price as Claude 1.3 per claudearchive.com pricing history. 100K context window. Claude 2 la |
| Claude Instant 1.x | 2023-07-?? | $0.80 | $2.40 | standard_list | — | https://tokencost.app/blog/ai-price-index | Claude Instant 1.x at $0.80/$2.40 per 1M tokens. Cited by TokenCost AI Price Index July 2023 entry. Exact launch date no |
| Claude 2.1 | 2023-11-21 | $8.00 | $24.00 | standard_list | 200,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html | Claude 2.1 announced Nov 21 2023. Expanded context to 200K tokens. 27% price cut on input tokens ($11.02 -> $8.00). Tool |
| Claude 3 Opus | 2024-03-04 | $15.00 | $75.00 | standard_list | 200,000 | https://tokencost.app/blog/ai-price-index | Claude 3 Opus launched March 2024 at $15/$75 per 1M tokens. Frontier model. 200K context window. Part of Claude 3 family |
| Claude 3 Sonnet | 2024-03-04 | $3.00 | $15.00 | standard_list | 200,000 | https://tokencost.app/blog/ai-price-index | Claude 3 Sonnet launched March 2024 at $3/$15 per 1M tokens. Balanced model. 200K context window. Most popular Anthropic |
| Claude 3 Haiku | 2024-03-04 | $0.25 | $1.25 | standard_list | 200,000 | https://tokencost.app/blog/ai-price-index | Claude 3 Haiku launched March 2024 at $0.25/$1.25 per 1M tokens. Budget tier. 200K context window. Price increased with  |
| Claude 3.5 Sonnet | 2024-06-21 | $3.00 | $15.00 | standard_list | 200,000 | https://claudearchive.com/pricing-history | Claude 3.5 Sonnet launched June 21 2024 at $3/$15 per 1M tokens. Same price as Claude 3 Sonnet but improved coding and t |
| Claude 3.5 Haiku | 2024-10-?? | $0.80 | $4.00 | standard_list | 200,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html | Claude 3.5 Haiku introduced October 2024 at $0.80/$4.00 per 1M tokens. This is the ONLY time Anthropic raised API prices |
| Claude 3.5 Sonnet (updated) | 2024-10-?? | $3.00 | $15.00 | standard_list | 200,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html | Updated Claude 3.5 Sonnet released October 2024 alongside Claude 3.5 Haiku. Same $3/$15 price as original Claude 3.5 Son |
| Claude Opus 4 | 2025-05-?? | $15.00 | $75.00 | standard_list | 200,000 | https://tokencost.app/blog/ai-price-index | Claude Opus 4 launched May 2025 at $15/$75 per 1M tokens. Frontier model. 200K context window at launch. Later expanded  |
| Claude Sonnet 4 | 2025-09-?? | $3.00 | $15.00 | standard_list | 200,000 | https://tokencost.app/blog/ai-price-index | Claude Sonnet 4 at $3/$15 per 1M tokens. Maintained same price as Claude 3.5 Sonnet. 200K context window at launch, late |
| Claude Opus 4.5 | 2025-11-24 | $5.00 | $25.00 | standard_list | 200,000 | https://claudearchive.com/pricing-history | Claude Opus 4.5 launched November 24 2025 at $5/$25 per 1M tokens. 67% cut from Opus 4's $15/$75. 200K context window at |
| Claude Sonnet 4.5 | 2025-09-29 | $3.00 | $15.00 | standard_list | 200,000 | https://claudearchive.com/pricing-history | Claude Sonnet 4.5 announced September 29 2025. Kept Sonnet 4 pricing at $3/$15 per 1M tokens. 200K context window. Later |
| Claude Opus 4.6 | 2026-03-13 | $5.00 | $25.00 | standard_list | 1,000,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | Claude Opus 4.6 GA March 13 2026 at $5/$25 per 1M tokens. 1M context window at standard pricing — flat rate, no surcharg |
| Claude Sonnet 4.6 | 2026-03-13 | $3.00 | $15.00 | standard_list | 1,000,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | Claude Sonnet 4.6 at $3/$15 per 1M tokens. 1M context window at standard pricing — flat rate, no surcharge above 200K to |
| Claude Haiku 4.5 | 2026-03-13 | $1.00 | $5.00 | standard_list | 200,000 | https://www.cloudzero.com/blog/claude-pricing/ | Claude Haiku 4.5 at $1/$5 per 1M tokens. 200K context window. Recently updated from Claude 3.5 Haiku ($0.80/$4.00). Offe |
| Claude Sonnet 5 | 2026-06-30 | $2.00 | $10.00 | promo | 1,000,000 | https://claudearchive.com/pricing-history | Claude Sonnet 5 launched June 30 2026 with introductory pricing of $2/$10 per 1M tokens through August 31 2026. Was sche |
| Claude Sonnet 5 | 2026-08-11 | $2.00 | $10.00 | standard_list | 1,000,000 | https://www.cloudzero.com/blog/claude-pricing/ | Anthropic made Claude Sonnet 5's $2/$10 rate PERMANENT on August 11 2026. Cancelled the planned September 1 increase to  |
| Claude Opus 5 | 2026-08-?? | $5.00 | $25.00 | standard_list | 1,000,000 | https://www.cloudzero.com/blog/claude-pricing/ | Claude Opus 5 at $5/$25 per 1M tokens. Same rate across five straight releases (Opus 4.5 through Opus 5). 1M context win |
| Claude Fable 5 | 2026-08-?? | $10.00 | $50.00 | standard_list | 1,000,000 | https://www.cloudzero.com/blog/claude-pricing/ | Claude Fable 5 at $10/$50 per 1M tokens. Premium tier. 1M context window. Shares rates with limited-availability Mythos  |
| Claude Opus 5 | 2026-08-?? | $2.50 | $12.50 | batch | — | https://www.cloudzero.com/blog/claude-pricing/ | Claude Opus 5 batch rate: $2.50/$12.50 per 1M tokens. 50% off standard $5/$25. Nightly pipelines, bulk classification, c |
| Claude Haiku 4.5 | 2026-08-?? | $0.50 | $2.50 | batch | — | https://www.cloudzero.com/blog/claude-pricing/ | Claude Haiku 4.5 batch rate: $0.50/$2.50 per 1M tokens. 50% off standard $1/$5. Source: CloudZero Claude pricing. |
| Claude Sonnet 4.6 | 2026-03-13 | $0.30 | — | cache | — | https://www.cloudzero.com/blog/claude-pricing/ | Claude Sonnet 4.6 cached reads at $0.30 per 1M tokens — 90% discount from standard $3.00 input. Applies to cached prompt |
| Claude Opus 4.8 | 2026-08-?? | $30.00 | $150.00 | promo | — | https://www.cloudzero.com/blog/claude-pricing/ | Claude Opus 4.8 fast mode at $30/$150 per 1M tokens — 6x standard rates. For latency-sensitive workloads. Source: CloudZ |
| Claude Opus 4.8 | 2026-08-?? | $5.50 | $27.50 | tiered | — | https://mem0.ai/blog/anthropic-claude-pricing | US-only inference premium: 1.1x standard rates. Source: Mem0 Anthropic Claude pricing. |
| Claude (web search tool) | 2026-05-?? | — | — | other | — | https://mem0.ai/blog/anthropic-claude-pricing | Anthropic web search tool: $10 per 1,000 searches. Separate from model token pricing. Source: Mem0 Anthropic Claude pric |

---

## 3. Google / Gemini pricing history

**31 price points** loaded from `kb/price_points_google.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Gemini 1.0 Pro | 2023-12-06 | $0.50 | $1.50 | standard_list | 32,768 | https://tokencost.app/blog/ai-price-index | Gemini 1.0 Pro launched December 6 2023 at $0.50/$1.50 per 1M tokens. Google's first Gemini API pricing. 32K context win |
| Gemini 1.0 Pro | 2024-01-01 | $0.25 | $0.50 | standard_list | 32,768 | https://deploybase.ai/articles/llm-pricing-history-how-costs-dropped-99-since-2023 | Gemini 1.0 Pro cut to $0.00025 per 1K input tokens ($0.25/M) and $0.0005 per 1K output tokens ($0.50/M) in Q1 2024. Depl |
| Gemini 1.5 Pro | 2024-02-01 | $1.25 | $5.00 | standard_list | 128,000 | https://tokencost.app/blog/ai-price-index | Gemini 1.5 Pro launched February 2024 at $1.25/$5.00 per 1M tokens, 128K context window. Later expanded to 2M+ context w |
| Gemini 1.5 Flash | 2024-02-01 | $0.35 | $0.53 | standard_list | 128,000 | https://tokencost.app/blog/ai-price-index | Gemini 1.5 Flash launched February 2024 at $0.35/$0.53 per 1M tokens. 128K context window. Fast, cheap. Later underwent  |
| Gemini 1.5 Flash | 2024-08-01 | $0.07 | $0.30 | standard_list | 128,000 | https://tokencost.app/blog/ai-price-index | Gemini 1.5 Flash cut to $0.075/$0.30 per 1M tokens in August 2024. 78% reduction from $0.35/$0.53. Source: TokenCost AI  |
| Gemini 1.5 Pro | 2024-10-01 | $1.25 | $5.00 | standard_list | 2,000,000 | https://tokencost.app/blog/ai-price-index | Gemini 1.5 Pro pricing noted at $1.25/$5.00 in October 2024 AI Price Index. 64% reduction in output from original $1.25/ |
| Gemini 2.0 Flash | 2025-12-01 | $0.10 | $0.40 | standard_list | 1,000,000 | https://tokencost.app/blog/ai-price-index | Gemini 2.0 Flash at $0.10/$0.40 per 1M tokens, 1M context window. Very cheap. Launched December 2025. Source: TokenCost  |
| Gemini 2.0 Flash-Lite | 2025-12-?? | $0.07 | $0.30 | standard_list | 1,000,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | Gemini 2.0 Flash-Lite at $0.075/$0.30 per 1M tokens. Ultra-budget. 1M context window. Cheaper than Gemini 2.0 Flash but  |
| Gemini 2.5 Pro | 2025-06-?? | $1.25 | $10.00 | standard_list | 1,000,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html | Gemini 2.5 Pro at $1.25/$10 per 1M tokens, 1M context window. Best value premium model — 12x cheaper than Claude 4 Opus  |
| Gemini 2.5 Pro | 2025-06-?? | $2.50 | $15.00 | tiered | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Pro long-context pricing from Google developer pricing page. Input doubles from $1.25 to $2.50 above 200K; ou |
| Gemini 2.5 Flash | 2025-06-?? | $0.30 | $2.50 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Flash at $0.30/$2.50 per 1M tokens. 1M context window. Text/image/video input at $0.30; audio input at $1.00. |
| Gemini 2.5 Flash-Lite | 2025-06-?? | $0.10 | $0.40 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Flash-Lite at $0.10/$0.40 per 1M tokens, 1M context window. Cheapest model — $0.01 per 1K input. Text/image/v |
| Gemini 2.5 Flash | 2025-06-?? | $0.03 | — | cache | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Flash cached input at $0.03 per 1M tokens. 90% discount from $0.30 standard input. Context caching storage: $ |
| Gemini 2.5 Pro | 2025-06-?? | $0.12 | — | cache | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Pro cached input at $0.125 per 1M tokens (≤200K tier). 90% discount from $1.25 standard input. Above 200K cac |
| Gemini 2.5 Flash-Lite | 2025-06-?? | $0.01 | — | cache | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Flash-Lite cached input at $0.01 per 1M tokens. 90% discount from $0.10 standard input. Source: https://ai.go |
| Gemini 2.5 Pro | 2025-06-?? | $0.62 | $5.00 | batch | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Pro batch: 50% off standard. ≤200K input: $0.625/$5.00 (50% of $1.25/$10.00). >200K input: $1.25/$7.50 (50% o |
| Gemini 2.5 Flash-Lite | 2025-06-?? | $0.05 | $0.20 | batch | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 2.5 Flash-Lite batch: $0.05/$0.20 per 1M tokens. 50% off standard $0.10/$0.40. Cheapest batch rate of any major p |
| Gemini 3.1 Pro Preview | 2026-04-?? | $2.00 | $12.00 | standard_list | 2,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.1 Pro Preview at $2.00/$12.00 per 1M tokens (≤200K input). 2M context window. Tiered above 200K: $4.00/$18.00.  |
| Gemini 3.1 Pro Preview | 2026-04-?? | $4.00 | $18.00 | tiered | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.1 Pro Preview long-context pricing. Input doubles from $2.00 to $4.00 above 200K; output increases from $12.00  |
| Gemini 3 Flash Preview | 2026-04-?? | $0.50 | $3.00 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3 Flash Preview at $0.50/$3.00 per 1M tokens. Text/image/video input at $0.50; audio input at $1.00. 1M context w |
| Gemini 3.5 Flash | 2026-05-19 | $1.50 | $9.00 | standard_list | 1,000,000 | https://www.metacto.com/blogs/the-true-cost-of-google-gemini-a-guide-to-api-pricing-and-integration | Gemini 3.5 Flash launched May 19 2026 (Google I/O) at $1.50/$9.00 per 1M tokens. 1M context window, 64K output, free tie |
| Gemini 3.5 Flash | 2026-05-19 | $0.15 | — | cache | — | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | Gemini 3.5 Flash cached input at $0.15 per 1M tokens — 90% discount from $1.50 standard input. 1M context window. Source |
| Gemini 3.5 Flash | 2026-05-19 | $0.75 | $4.50 | batch | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.5 Flash batch/flex rate: $0.75/$4.50 per 1M tokens. 50% off standard $1.50/$9.00. Source: https://ai.google.dev |
| Gemini 3.1 Pro Preview | 2026-04-?? | $1.00 | $6.00 | batch | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.1 Pro Preview batch: 50% off standard. Source: https://ai.google.dev/gemini-api/docs/pricing (Gemini 3.1 Pro se |
| Gemini 3.1 Flash-Lite | 2026-04-?? | $0.25 | $1.50 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.1 Flash-Lite at $0.25/$1.50 per 1M tokens. Text/image/video input at $0.25; audio input at $0.50. 1M context wi |
| Gemini 3.8 Flash | 2026-04-?? | $0.75 | $3.75 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.8 Flash Standard tier: $0.75/$3.75 per 1M tokens through December 31 2026. Text/image/video input at $0.75; aud |
| Gemini 3.8 Flash | 2027-01-01 | $1.50 | $7.50 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.8 Flash starting January 1 2027: $1.50/$7.50 per 1M tokens (up from $0.75/$3.75). Input doubles; output doubles |
| Gemini 3.8 Flash | 2026-04-?? | $0.07 | — | cache | — | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.8 Flash cached input rate: $0.075/1M tokens through Dec 31 2026 (90% discount from $0.75). Starting Jan 1 2027: |
| Gemini 3.8 Flash | 2026-04-?? | $1.35 | $6.75 | standard_list | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing | Gemini 3.8 Flash Priority tier through Dec 31 2026: $1.35/$6.75 per 1M tokens. Starting Jan 1 2027: $2.70/$13.50 (double |
| Gemini 3.1 Pro Preview | 2026-04-01 | $2.00 | $12.00 | standard_list | — | — | Gemini 3.1 Pro and 2.5 Pro removed from free tier April 1 2026 — now paid-only. Original free tier had been available fo |
| Gemini 2.5 Flash-Lite | 2026-04-01 | $0.10 | $0.40 | free | — | — | Gemini 2.5 Flash-Lite free tier: 1,500 RPD (requests per day) since April 2026 free tier restrictions. Text/image/video  |

---

## 4. DeepSeek pricing history

**11 price points** loaded from `kb/price_points_deepseek.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| DeepSeek V2 | 2023-12-01 | $0.14 | $0.28 | standard_list | 128,000 | https://deploybase.ai/articles/llm-pricing-history-how-costs-dropped-99-since-2023 | DeepSeek V2 launched December 2023 at $0.14/$0.28 per 1M tokens. 128K context window. Cheaper than GPT-4o ($5/$15) by 35 |
| DeepSeek V3 | 2024-12-01 | $0.27 | $1.10 | standard_list | 128,000 | https://tokencost.app/blog/ai-price-index | DeepSeek V3 launched December 2024 at $0.27/$1.10 per 1M tokens. 128K context window. Frontier-quality open-weight model |
| DeepSeek V3.2 | 2025-12-?? | $0.28 | $0.42 | standard_list | 128,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | DeepSeek V3.2 at $0.28/$0.42 per 1M tokens. 128K context window. 90% prompt cache discount drops effective input cost to |
| DeepSeek V3.2 | 2025-12-?? | $0.03 | — | cache | — | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | DeepSeek V3.2 90% cache discount: effective input $0.028/MTok vs $0.28 standard. Comparable to Gemini 3 Flash cached rat |
| DeepSeek R1 | 2025-01-?? | $0.55 | $2.19 | standard_list | 128,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | DeepSeek R1 at $0.55/$2.19 per 1M tokens. Reasoning model. 128K context window. Cheaper reasoning than OpenAI's o-series |
| DeepSeek V4 Pro | 2026-01-01 | $0.66 | $1.98 | standard_list | 1,000,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | DeepSeek V4 Pro launched early 2026 at $0.66/$1.98 per 1M tokens, 1M context window. Near-budget pricing with premium ca |
| DeepSeek V4 Pro | 2026-05-25 | $0.43 | $0.87 | standard_list | 1,000,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | DeepSeek V4 Pro permanent rate: $0.435/$0.87 per 1M tokens, 1M context window. 34% cut from $0.66/$1.98. Permanent rate  |
| DeepSeek V4 Flash | 2026-01-01 | $0.22 | $0.28 | standard_list | 1,000,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html | DeepSeek V4 Flash at $0.22/$0.28 per 1M tokens, 1M context window. Highest throughput/cost ratio. Source: APIpulse State |
| DeepSeek V4 Flash | 2026-01-?? | $0.14 | $0.28 | standard_list | 1,000,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | DeepSeek V4 Flash cut to $0.14/$0.28 per 1M tokens. 1M context window. Output matches GPT-4o mini's $0.60 but at less th |
| DeepSeek V4 Flash | 2026-01-?? | $0.07 | $0.14 | batch | — | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | DeepSeek V4 Flash batch: $0.07/$0.14 per 1M tokens. 50% off standard. 1M context. Source: ChatForest LLM API pricing com |
| DeepSeek V4 Pro | 2026-05-25 | $0.22 | $0.43 | batch | — | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | DeepSeek V4 Pro batch: $0.2175/$0.435 per 1M tokens. 50% off permanent rate. 1M context. Undercuts GPT-5 batch ($0.625/$ |

---

## 5. xAI / Grok pricing history

**5 price points** loaded from `kb/price_points_xai.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Grok 3 | 2025-04-01 | $3.00 | $15.00 | standard_list | 128,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 | Grok 3 launched April 2025 at $3/$15 per 1M tokens, 128K context window. xAI's flagship model. Included real-time web ac |
| Grok 3 | 2026-05-02 | $30.00 | $150.00 | standard_list | 128,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html | Grok 3 increased 10x on May 2 2026 from $3/$15 to $30/$150 per 1M tokens — the BIGGEST price hike in the market at that  |
| Grok 3 Mini | 2026-04-?? | $3.00 | $5.00 | standard_list | 128,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html | Grok 3 Mini at $3/$5 per 1M tokens, 128K context window. Cheaper output than Grok 3 at $30/$150 post-increase. But input |
| Grok 4.3 | 2026-05-?? | $0.20 | $0.80 | standard_list | 2,000,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | Grok 4.3 at $0.20/$0.80 per 1M tokens, 2M context window. Largest context window among priced models at time of launch.  |
| Grok Build 0.1 | 2026-05-?? | $1.00 | $2.00 | standard_list | 256,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ | Grok Build 0.1 at $1/$2 per 1M tokens, 256K context window. Agentic coding only variant. Competes with GPT-5.3 Codex ($1 |

---

## 6. Mistral AI pricing history

**26 price points** loaded from `kb/price_points_mistral.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Mistral Large 3 (2512) | 2025-12-?? | $0.50 | $1.50 | standard_list | 262,144 | https://mistral.ai/pricing/api/ | Mistral Large 3 2512 launched December 2025. Current flagship. $0.50/$1.50 per 1M tokens, 262K context window. Open-weig |
| Mistral Large 2.1 (2411) | 2024-11-?? | $2.00 | $6.00 | standard_list | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Large 2.1 2411 at $2.00/$6.00 per 1M tokens, 131K context window. Predecessor to Mistral Large 3 (2512). Source: |
| Mistral Large 2.0 (2407) | 2024-07-?? | $2.00 | $6.00 | standard_list | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Large 2.0 2407 at $2.00/$6.00 per 1M tokens, 131K context window. First Mistral Large 2. Deprecated November 29  |
| Mistral Large 1.0 (2402) | 2024-02-?? | $2.00 | $6.00 | standard_list | 128,000 | https://docs.mistral.ai/models | Mistral Large 1.0 2402 launched February 2024. First Mistral Large model. $2.00/$6.00 per 1M tokens, 128K context window |
| Mistral Medium 3.5 | 2026-04-?? | $1.50 | $7.50 | standard_list | 256,000 | https://mistral.ai/pricing/api/ | Mistral Medium 3.5 launched April 2026 at $1.50/$7.50 per 1M tokens, 256K context window. Open-weight (Modified MIT). De |
| Mistral Medium 3.1 (2508) | 2025-08-?? | $0.40 | $2.00 | standard_list | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Medium 3.1 2508 at $0.40/$2.00 per 1M tokens, 131K context window. Predecessor to Mistral Medium 3 (launched May |
| Mistral Medium 3 (2505) | 2025-05-?? | $0.40 | $2.00 | standard_list | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Medium 3 2505 launched May 2025 at $0.40/$2.00 per 1M tokens, 131K context window. Predecessor to Mistral Medium |
| Mistral Medium 1.0 (2312) | 2023-12-?? | $0.40 | $2.00 | standard_list | 131,072 | https://docs.mistral.ai/models | Mistral Medium 1.0 2312 launched December 2023. First Mistral Medium model. $0.40/$2.00 per 1M tokens (same price mainta |
| Mistral Small 4 (2603) | 2026-03-?? | $0.15 | $0.60 | standard_list | 128,000 | https://mistral.ai/pricing/api/ | Mistral Small 4 2603 launched March 2026 at $0.15/$0.60 per 1M tokens, 128K context window. Open-weight, Apache 2.0. Mul |
| Mistral Small 3.2 (2506) | 2025-06-?? | $0.08 | $0.20 | standard_list | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Small 3.2 2506 at $0.08/$0.20 per 1M tokens, 128K context window. Cheapest Small model at launch. Deprecated Apr |
| Mistral Small 3.1 (2503) | 2025-03-?? | $0.10 | $0.30 | standard_list | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Small 3.1 2503 at $0.10/$0.30 per 1M tokens, 128K context window. Predecessor to Mistral Small 3.2 (June 2025).  |
| Mistral Small 3.0 (2501) | 2025-01-?? | $0.10 | $0.30 | standard_list | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Small 3.0 2501 at $0.10/$0.30 per 1M tokens, 128K context window. Predecessor to Mistral Small 3.1 (March 2025). |
| Mistral Small 2.0 (2409) | 2024-09-?? | $0.10 | $0.30 | standard_list | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Small 2.0 2409 at $0.10/$0.30 per 1M tokens, 128K context window. Predecessor to Mistral Small 3.0 (January 2025 |
| Mistral Small 1.0 (2402) | 2024-02-?? | $0.10 | $0.30 | standard_list | 128,000 | https://docs.mistral.ai/models | Mistral Small 1.0 2402 launched February 2024. First Mistral Small model. $0.10/$0.30 per 1M tokens, 128K context window |
| Mistral Small 3.2 24B | 2025-06-?? | $0.07 | $0.20 | standard_list | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Mistral Small 3.2 24B at $0.075/$0.20 per 1M tokens, 131K context window. Pricepertoken model page lists this rate. NOTE |
| Mistral Nemo | 2024-07-?? | $0.02 | $0.03 | standard_list | 131,072 | https://mistral.ai/pricing/api/ | Mistral Nemo at $0.02/$0.03 per 1M tokens, 131K context window. 12B model, multilingual, budget tier. Cheapest generalis |
| Codestral 2508 | 2025-08-?? | $0.30 | $0.90 | standard_list | 256,000 | https://mistral.ai/pricing/api/ | Codestral 2508 at $0.30/$0.90 per 1M tokens, 256K context window. Premier coding model, low-latency, optimized for high- |
| Devstral 2 2512 | 2025-12-?? | $0.40 | $0.90 | standard_list | 262,144 | https://pricepertoken.com/pricing-page/provider/mistral-ai | Devstral 2 2512 at $0.40/$0.90 per 1M tokens, 262K context window. Agentic coding model launched December 2025. Deprecat |
| Ministral 3 8B (2512) | 2025-12-?? | $0.15 | $0.15 | standard_list | 262,144 | https://mistral.ai/pricing/api/ | Ministral 3 8B 2512 at $0.15/$0.15 per 1M tokens (input equals output), 262K context window. Open-weight, edge model, be |
| Ministral 3 3B (2512) | 2025-12-?? | $0.10 | $0.10 | standard_list | 262,144 | https://mistral.ai/pricing/api/ | Ministral 3 3B 2512 at $0.10/$0.10 per 1M tokens, 262K context window. Open-weight, smallest edge model. Source: Mistral |
| Mistral Small 4 (2603) | 2026-03-?? | $0.07 | $0.30 | batch | — | https://mistral.ai/pricing/api/ | Mistral Small 4 batch: $0.075/$0.30 per 1M tokens. 50% off standard. Source: Mistral API pricing page (standard + batch  |
| Mistral Large 3 (2512) | 2025-12-?? | $0.25 | $0.75 | batch | — | https://mistral.ai/pricing/api/ | Mistral Large 3 batch: $0.25/$0.75 per 1M tokens. 50% off standard. Source: Mistral API pricing page. |
| Mistral Medium 3.5 | 2026-04-?? | $0.15 | — | cache | — | https://mistral.ai/pricing/api/ | Mistral Medium 3.5 cached input at $0.15 per 1M tokens — 90% discount from $1.50 standard. Source: Mistral API pricing p |
| Mistral Large 3 (2512) | 2025-12-?? | $0.05 | — | cache | — | https://mistral.ai/pricing/api/ | Mistral Large 3 cached input at $0.05 per 1M tokens — 90% discount from $0.50 standard. Source: Mistral API pricing page |
| Mistral Small 4 (2603) | 2026-03-?? | $0.01 | — | cache | — | https://mistral.ai/pricing/api/ | Mistral Small 4 cached input at $0.015 per 1M tokens — 90% discount from $0.15 standard. Source: Mistral API pricing pag |
| Mistral Le Chat Pro | 2026-05-?? | — | — | other | — | https://mistral.ai/pricing/ | Mistral Le Chat Pro subscription: $14.99/month (normally $14.99, students $5.99). Separate from API billing. Includes Mi |

---

## 7. Cohere pricing history

**13 price points** loaded from `kb/price_points_cohere.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Command (legacy) | 2023-??-?? | $1.00 | $2.00 | standard_list | 4,096 | https://cohere.com/pricing | Legacy Command at $1.00/$2.00 per 1M tokens, 4K context. Deprecated September 15 2025. Source: Cohere pricing FAQ. This  |
| Command-light (legacy) | 2023-??-?? | $0.30 | $0.60 | standard_list | 4,096 | https://cohere.com/pricing | Legacy Command-light at $0.30/$0.60 per 1M tokens, 4K context. Deprecated September 15 2025. Source: Cohere pricing FAQ. |
| Command R 03-2024 | 2024-03-?? | $0.50 | $1.50 | standard_list | 128,000 | https://cohere.com/pricing | Command R 03-2024 launched March 2024 at $0.50/$1.50 per 1M tokens, 128K context window. First Cohere model with 128K co |
| Command R+ 04-2024 | 2024-04-?? | $3.00 | $15.00 | standard_list | 128,000 | https://cohere.com/pricing | Command R+ 04-2024 launched April 2024 at $3.00/$15.00 per 1M tokens, 128K context window. First Cohere flagship with 12 |
| Command R+ 08-2024 | 2024-08-?? | $2.50 | $10.00 | standard_list | 128,000 | https://cohere.com/pricing | Command R+ 08-2024 refresh launched August 2024 at $2.50/$10.00 per 1M tokens, 128K context window. ~50% higher throughp |
| Command R 08-2024 | 2024-08-?? | $0.15 | $0.60 | standard_list | 128,000 | https://cohere.com/pricing | Command R 08-2024 refresh at $0.15/$0.60 per 1M tokens, 128K context window. Dropped from $0.50/$1.50 at March 2024 laun |
| Command R7B 12-2024 | 2024-12-?? | $0.04 | $0.15 | standard_list | 128,000 | https://cohere.com/pricing | Command R7B 12-2024 launched December 2024 at $0.0375/$0.15 per 1M tokens, 128K context window. Budget tier — 3-27x chea |
| Command R+ 08-2024 | 2024-08-?? | $0.25 | — | cache | — | https://cohere.com/pricing | Command R+ 08-2024 cached input at $0.25 per 1M tokens — 90% discount from $2.50 standard input. Source: Cohere pricing  |
| Command R 08-2024 | 2024-08-?? | $0.01 | — | cache | — | https://cohere.com/pricing | Command R 08-2024 cached input at $0.015 per 1M tokens — 90% discount from $0.15 standard input. Source: Cohere pricing  |
| Command R7B 12-2024 | 2024-12-?? | $0.00 | — | cache | — | https://cohere.com/pricing | Command R7B 12-2024 cached input at $0.00375 per 1M tokens — 90% discount from $0.0375 standard. Source: Cohere pricing  |
| Command R+ 08-2024 | 2024-08-?? | $1.25 | $5.00 | batch | — | https://cohere.com/pricing | Command R+ 08-2024 batch: $1.25/$5.00 per 1M tokens. 50% off standard. Source: Cohere pricing (batch rates). |
| Command A | 2025-??-?? | $2.50 | $10.00 | standard_list | 256,000 | https://cohere.com/pricing | Command A at $2.50/$10.00 per 1M tokens, 256K context window. Newest Cohere flagship. Same rate card as Command R+ 08-20 |
| Aya Expanse 8B / 32B | 2025-??-?? | $0.50 | $1.50 | standard_list | 128,000 | https://cohere.com/pricing | Aya Expanse 8B and 32B on Cohere API at $0.50/$1.50 per 1M tokens, 128K context window. Source: Cohere pricing FAQ. NOTE |

---

## 8. Meta Llama (hosted) pricing history

**11 price points** loaded from `kb/price_points_meta_llama.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Llama 3.1 8B (hosted: Groq) | 2024-07-?? | $0.05 | $0.08 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.1 8B on Groq at $0.05/$0.08 per 1M tokens. Cheapest hosted Llama option. Meta does NOT sell first-party Llama AP |
| Llama 3.1 8B (hosted: Together AI) | 2024-07-?? | $0.18 | $0.18 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.1 8B on Together AI at $0.18/$0.18 per 1M tokens. Flat rate (input equals output). Source: AI Pricing Guru Meta  |
| Llama 3.1 8B (hosted: Fireworks) | 2024-07-?? | $0.20 | $0.20 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.1 8B on Fireworks at $0.20/$0.20 per 1M tokens. Slightly more expensive than Together AI. Source: AI Pricing Gur |
| Llama 3.3 70B (hosted: DeepInfra) | 2024-12-?? | $0.23 | $0.40 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.3 70B on DeepInfra at $0.23/$0.40 per 1M tokens. Cheapest host for Llama 3.3 70B — approximately 3x cheaper than |
| Llama 3.3 70B (hosted: Groq) | 2024-12-?? | $0.59 | $0.79 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.3 70B on Groq at $0.59/$0.79 per 1M tokens. Fastest host at 250+ tokens/sec output. About 10-19x cheaper than GP |
| Llama 3.3 70B (hosted: Together AI) | 2024-12-?? | $0.88 | $0.88 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.3 70B on Together AI at $0.88/$0.88 per 1M tokens (flat rate). Source: AI Pricing Guru Meta pricing comparison M |
| Llama 3.3 70B (hosted: Fireworks) | 2024-12-?? | $0.90 | $0.90 | standard_list | 128,000 | https://www.aipricing.guru/meta-pricing/ | Llama 3.3 70B on Fireworks at $0.90/$0.90 per 1M tokens (flat rate, >16B tier). Slightly more expensive than Together AI |
| Llama 3.1 405B (hosted: Fireworks) | 2024-07-?? | $3.00 | $3.00 | standard_list | 131,072 | https://www.aipricing.guru/meta-pricing/ | Llama 3.1 405B on Fireworks at $3.00/$3.00 per 1M tokens (flat rate). Cheapest host for 405B at time of writing. NOTE: T |
| Llama 3.1 405B (hosted: Together AI) | 2024-07-?? | $3.50 | $3.50 | standard_list | 131,072 | https://www.aipricing.guru/meta-pricing/ | Llama 3.1 405B on Together AI at $3.50/$3.50 per 1M tokens (flat rate). STALE — Together AI removed 405B from its server |
| Llama 4 Scout (hosted: Groq) | 2025-??-?? | $0.11 | $0.34 | standard_list | 10,000,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html | Llama 4 Scout on Groq at $0.11/$0.34 per 1M tokens, 10M context window. Latest Llama 4 Scout. 10M context is the largest |
| Llama 4 Maverick (hosted: Groq) | 2025-??-?? | $0.20 | $0.60 | standard_list | 10,000,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html | Llama 4 Maverick on Groq at $0.20/$0.60 per 1M tokens, 10M context window. Latest Llama 4 Maverick. Source: APIpulse Sta |

---

## 9. Alibaba / Qwen pricing history

**25 price points** loaded from `kb/price_points_alibaba_qwen.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Qwen3-Max | 2025-??-?? | $1.20 | $6.00 | standard_list | 262,144 | https://deepinfra.com/blog/qwen-api-pricing-2026-guide | Qwen3-Max at $1.20/$6.00 per 1M tokens, 262K context window. Proprietary flagship tier. Alibaba Cloud Model Studio (form |
| Qwen3-Max Thinking | 2025-??-?? | $0.78 | $3.90 | standard_list | 262,144 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3-Max Thinking at $0.78/$3.90 per 1M tokens, 262K context window. Thinking/reasoning variant of Qwen3-Max. Source: P |
| Qwen3 Max | 2026-??-?? | $2.00 | $6.00 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 Max (1M context) at $2.00/$6.00 per 1M tokens, 1M context window. Current flagship generation on Alibaba Cloud Mod |
| Qwen3.6 Max Preview | 2025-??-?? | $1.30 | $7.80 | standard_list | 262,144 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.6 Max Preview at $1.30/$7.80 per 1M tokens, 262K context window. Preview of Qwen3.6 Max generation. Source: Puter. |
| Qwen3.7 Plus | 2026-??-?? | $0.32 | $1.28 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.7 Plus at $0.32/$1.28 per 1M tokens, 1M context window. Multimodal agent tier: vision, video, agentic pipelines. S |
| Qwen3.7 Max | 2026-??-?? | $1.25 | $3.75 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.7 Max at $1.25/$3.75 per 1M tokens, 1M context window. Previous flagship — remains available after Qwen3.8 Max (Au |
| Qwen3.8 Max | 2026-08-03 | $2.00 | $6.00 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.8 Max launched August 3 2026 at $2.00/$6.00 per 1M tokens, 1M context window. Current flagship — coding and long-h |
| Qwen3.8 Flash | 2026-08-26 | $0.14 | $0.42 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.8 Flash launched August 26 2026 at $0.14/$0.42 per 1M tokens, 1M context window. Flat rate — no length tier. Cheap |
| Qwen3.7 Flash | 2026-??-?? | $0.03 | $0.13 | tiered | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.7 Flash at $0.03/$0.13 per 1M tokens under 32K tokens; rises to $0.20/$0.80 above 256K tokens. High-volume multimo |
| Qwen3.6 Flash | 2025-??-?? | $0.19 | $1.13 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.6 Flash at $0.19/$1.13 per 1M tokens, tiered by length (the $0.19/$1.13 is for the standard tier). High-volume sim |
| Qwen3.6 Plus | 2025-??-?? | $0.50 | $3.00 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.6 Plus at $0.50/$3.00 per 1M tokens, 1M context window. Balanced production workloads — multimodal. Source: Puter. |
| Qwen3.5 Plus | 2025-??-?? | $0.50 | $3.00 | standard_list | 1,000,000 | https://qwen.ai/apiplatform | Qwen3.5 Plus at $0.50/$3.00 per 1M tokens, 1M context window. Previous balanced generation. Source: Qwen API platform (q |
| Qwen3 Flash | 2025-??-?? | $0.05 | $0.40 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 Flash at $0.05/$0.40 per 1M tokens, 1M context window. High-volume simple tasks. Cheapest Qwen model on Alibaba pl |
| Qwen3 Coder Plus | 2025-??-?? | $1.00 | $5.00 | tiered | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 Coder Plus at $1.00/$5.00 for short contexts (<=32K input) but rises steeply to $6.00/$60.00 for 1M context. Agent |
| Qwen3 Coder 480B A35B | 2025-??-?? | $1.50 | $7.50 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 Coder 480B A35B at $1.50/$7.50 per 1M tokens, flat rate (no length tier). Large MoE coding model. Source: Puter.co |
| Qwen3 Coder Next | 2025-??-?? | $0.11 | $0.80 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 Coder Next at $0.11/$0.80 per 1M tokens, flat rate. Next-gen coding model — very cheap for coding tasks. Source: P |
| Qwen3 Coder Flash | 2025-??-?? | $0.30 | $1.50 | tiered | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 Coder Flash at $0.30/$1.50 for short contexts (<=32K input) rising to $1.60/$9.60 at 1M context. Flash coding mode |
| Qwen3-VL Plus | 2025-??-?? | $0.20 | $1.60 | standard_list | 131,027 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3-VL Plus at $0.20/$1.60 per 1M tokens, ~131K context window. Vision model — image and document understanding. Sourc |
| Qwen3 VL 235B A22B | 2025-??-?? | $0.70 | $2.80 | standard_list | 131,027 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3 VL 235B A22B at $0.70/$2.80 per 1M tokens, ~131K context window. Large vision MoE model. Source: Puter.com Qwen AP |
| Qwen3.5 Omni Flash | 2025-??-?? | $0.43 | $1.66 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen3.5 Omni Flash at $0.43 text input / $1.66 output per 1M tokens, 1M context window. Audio/video omni model (text, au |
| Qwen3.5 Omni Plus | 2026-??-?? | $1.00 | $6.00 | standard_list | 1,000,000 | https://www.alibabacloud.com/help/en/model-studio/models | Qwen3.5-Omni-Plus at Alibaba Cloud Model Studio — omni model (real-time audio/video). Source: Alibaba Cloud Model Studio |
| Qwen Image 2.0 | 2025-??-?? | — | — | other | — | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen Image 2.0 at $0.04 per image (standard) / $0.08 per image (Pro). Image generation model — NOT per-token pricing (pe |
| Qwen VL OCR | 2025-??-?? | $0.72 | $0.72 | standard_list | 131,027 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen VL OCR at $0.72/$0.72 per 1M tokens (flat rate, input equals output). Vision-language OCR model. Source: Puter.com  |
| Qwen-MT Turbo | 2025-??-?? | $0.16 | $0.49 | standard_list | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ | Qwen-MT Turbo at $0.16/$0.49 per 1M tokens, 1M context window. Translation model (machine translation). Source: Puter.co |
| Qwen2.5 72B (hosted: DeepInfra) | 2024-12-?? | $0.23 | $0.40 | standard_list | 128,000 | https://deepinfra.com/blog/qwen-api-pricing-2026-guide | Qwen2.5 72B on DeepInfra at $0.23/$0.40 per 1M tokens (same pricing as Llama 3.3 70B on DeepInfra). Open-weight model. S |

---

## 10. Moonshot / Kimi pricing history

**17 price points** loaded from `kb/price_points_moonshot_kimi.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Kimi K2 | 2025-01-01 | $0.60 | $2.50 | standard_list | 128,000 | https://benchlm.ai/moonshot/api-pricing | Kimi K2 at $0.60/$2.50 per 1M tokens, 128K context window. Original Moonshot API model. Approximate launch date: early 2 |
| Kimi K2.5 | 2025-06-09 | $0.15 | $0.75 | promo | 256,000 | https://openrouter.ai/moonshotai/kimi-k2.5 | Kimi K2.5 at $0.15/$0.75 (OpenRouter listed, Jun 9 2025) — introductory price. Price increased rapidly over the followin |
| Kimi K2.5 | 2025-06-24 | $0.30 | $1.50 | promo | 256,000 | https://openrouter.ai/moonshotai/kimi-k2.5 | Kimi K2.5 at $0.30/$1.50 — first price increase on OpenRouter (Jun 24 2025), doubling from $0.15. Output at 5x ratio. So |
| Kimi K2.5 | 2025-07-09 | $0.45 | $2.25 | promo | 256,000 | https://openrouter.ai/moonshotai/kimi-k2.5 | Kimi K2.5 at $0.45/$2.25 — second OpenRouter price increase (Jul 9 2025). Price held at $0.45 through Jul 24 per chart.  |
| Kimi K2.5 | 2025-07-24 | $0.60 | $3.00 | standard_list | 256,000 | https://benchlm.ai/moonshot/api-pricing | Kimi K2.5 at $0.60/$3.00 — final price increase on OpenRouter (~Jul 24-Aug 8 2025), reaching the standard rate that matc |
| Kimi K2.6 | 2025-11-01 | $0.95 | $4.00 | standard_list | 262,144 | https://benchlm.ai/moonshot/api-pricing | Kimi K2.6 at $0.95/$4.00 per 1M tokens, 256K context window. Moonshot's flagship model before K3 launch (Sep 2026). Appr |
| Kimi K2.7 Code | 2026-01-01 | $0.95 | $4.00 | standard_list | 262,144 | https://benchlm.ai/moonshot/api-pricing | Kimi K2.7 Code at $0.95/$4.00 per 1M tokens, 262K context window. Coding-specialist variant of K2.6 — same price as K2.6 |
| Kimi K2.7 Code Highspeed | 2026-01-01 | $1.90 | $8.00 | standard_list | 262,144 | https://www.chatbase.co/blog/kimi-k2-api | Kimi K2.7 Code Highspeed at $1.90/$8.00 per 1M tokens, 262K context window. High-speed variant of K2.7 Code — 2x the sta |
| Kimi K3 | 2026-09-01 | $3.00 | $15.00 | standard_list | 1,050,000 | https://benchlm.ai/moonshot/api-pricing | Kimi K3 at $3.00/$15.00 per 1M tokens (cache-miss input), cache-hit input at $0.30, 1.05M context window. Moonshot's new |
| Kimi K2.5 | 2025-07-24 | $0.36 | $1.80 | batch | 256,000 | https://benchlm.ai/moonshot/api-pricing | Kimi K2.5 batch API at $0.36/$1.80 per 1M tokens — 60% off standard rate. 24-hour SLA. Source: BenchLM Kimi API pricing  |
| Kimi K2.6 | 2025-11-01 | $0.57 | $2.40 | batch | 262,144 | https://benchlm.ai/moonshot/api-pricing | Kimi K2.6 batch API at $0.57/$2.40 per 1M tokens — 60% off standard rate. 24-hour SLA. Source: BenchLM Kimi API pricing  |
| Kimi K2.7 Code | 2026-01-01 | $0.57 | $2.40 | batch | 262,144 | https://benchlm.ai/moonshot/api-pricing | Kimi K2.7 Code batch API at $0.57/$2.40 per 1M tokens — 60% off standard rate. 24-hour SLA. Source: BenchLM Kimi API pri |
| Kimi K2.5 | 2025-07-24 | $0.15 | — | cache | 256,000 | https://openrouter.ai/moonshotai/kimi-k2.5 | Kimi K2.5 cached input at $0.15 per 1M tokens — 75% discount from $0.60 standard input. Source: OpenRouter Kimi K2.5 mod |
| Kimi K2.6 | 2025-11-01 | $0.16 | — | cache | 262,144 | https://www.chatbase.co/blog/kimi-k2-api | Kimi K2.6 cached input at $0.16 per 1M tokens — 83% discount from $0.95 standard input. Source: Chatbase Kimi K2 API gui |
| Kimi K2.7 Code | 2026-01-01 | $0.19 | — | cache | 262,144 | https://www.chatbase.co/blog/kimi-k2-api | Kimi K2.7 Code cached input at $0.19 per 1M tokens — 80% discount from $0.95 standard input. Source: Chatbase Kimi K2 AP |
| Kimi K2 | 2025-01-01 | $0.15 | — | cache | 128,000 | https://www.chatbase.co/blog/kimi-k2-api | Kimi K2 cached input at $0.15 per 1M tokens — 75% discount from $0.60 standard input. Source: Chatbase Kimi K2 API guide |
| Kimi K3 | 2026-09-01 | $0.30 | — | cache | 1,050,000 | https://benchlm.ai/moonshot/api-pricing | Kimi K3 cached input at $0.30 per 1M tokens — 90% discount from $3.00 standard input. Best cache discount ratio in Kimi  |

---

## 11. OpenRouter Free Models pricing history

**13 price points** loaded from `kb/price_points_openrouter_free.jsonl`.

| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |
|-------|---------------|---------------|----------------|------------|---------|--------|-------|
| Nvidia Nemotron 3 Ultra 550B A55B | 2026-09-07 | $0.00 | $0.00 | free_tier | 1,000,000 | https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free | NVIDIA Nemotron 3 Ultra 550B A55B:free. Largest free Nemotron. 550B/55B MoE 1M context. CONFIRMED WORKING. Most capable  |
| Nvidia Nemotron 3 Super 120B A12B | 2026-09-07 | $0.00 | $0.00 | free_tier | 262,144 | https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b:free | NVIDIA Nemotron 3 Super 120B A12B:free. Mid-tier free Nemotron. 120B/12B MoE 262K context. CONFIRMED WORKING. Currently  |
| Nvidia Nemotron 3 Nano Omni 30B A3B Reasoning | 2026-09-07 | $0.00 | $0.00 | free_tier | 256,000 | https://openrouter.ai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | NVIDIA Nemotron 3 Nano Omni 30B A3B Reasoning:free. Smallest WORKING free Nemotron. 30B/3B MoE reasoning-specialized 256 |
| Nvidia Nemotron 3.5 Lightning | 2026-09-07 | $0.00 | $0.00 | free_tier | 1,000,000 | https://openrouter.ai/nvidia/nemotron-3.5-lightning:free | NVIDIA Nemotron 3.5 Lightning:free. Newest Nemotron 3.5. 1M context. 429 on free tier. NOTE Nemotron 3 Super 120B and Ul |
| Google Gemma 4 31B Instruct | 2026-09-07 | $0.00 | $0.00 | free_tier | 1,000,000 | https://openrouter.ai/google/gemma-4-31b-it:free | google/gemma-4-31b-it:free. Google Gemma 4 31B IT. 1M context. 429 on free tier. Part of Google Gemma 4 family. Status m |
| Google Gemma 4 26B A4B Instruct | 2026-09-07 | $0.00 | $0.00 | free_tier | 1,000,000 | https://openrouter.ai/google/gemma-4-26b-a4b-it:free | google/gemma-4-26b-a4b-it:free. Google Gemma 4 26B A4B IT. 1M context. 26B/4B MoE. 429 same failure mode as Gemma 4 31B. |
| Poolside Laguna S 2.1 | 2026-09-07 | $0.00 | $0.00 | free_tier | — | https://openrouter.ai/poolside/laguna-s-2.1:free | poolside/laguna-s-2.1:free. Poolside coding-optimized model. 429 on free tier. Poolside is a coding-focused lab. Status  |
| Thinking Machines Inkling | 2026-09-07 | $0.00 | $0.00 | free_tier | 1,000,000 | https://openrouter.ai/thinkingmachines/inkling:free | thinkingmachines/inkling:free. Thinking Machines Inkling open-weight. 403 Forbidden API access requires approved agentic |
| Inclusive AI Ling 3.0 Flash Fin | 2026-09-07 | $0.00 | $0.00 | free_tier | — | https://openrouter.ai/inclusionai/ling-3.0-flash-fin:free | inclusionai/ling-3.0-flash-fin:free. Inclusive AI Ling 3.0 Flash Fin financial-domain. Returns EMPTY content accepts req |
| Inclusion AI Ling Flash | 2026-09-07 | $0.00 | $0.00 | free_tier | — | https://openrouter.ai/inclusionai/ling-flash:free | inclusionai/ling-flash:free. Inclusive AI Ling Flash lighter Ling variant. Returns EMPTY content same failure mode as Li |
| Cohere North Mini Code | 2026-09-07 | $0.00 | $0.00 | free_tier | — | https://openrouter.ai/cohere/north-mini-code:free | cohere/north-mini-code:free. Cohere North Mini Code code-specialized small model. Returns EMPTY content accepts request  |
| Dots Studio Dots 3 Note Preview | 2026-09-07 | $0.00 | $0.00 | free_tier | — | https://openrouter.ai/dots-studio/dots-3-note-preview:free | dots-studio/dots-3-note-preview:free. Dots Studio Dots 3 Note Preview note-taking summarization. Returns EMPTY content s |
| OpenRouter Free Router | 2026-09-07 | $0.00 | $0.00 | free_tier | — | https://openrouter.ai/openrouter/free | openrouter/free. OpenRouter meta-router for free models. Returns EMPTY content. Could mean a no free models available b  |

---

## 7. Cross-provider comparison — current prices (late 2026 snapshot)

These are the **latest standard_list price points** for each model as loaded in the KB. Batch, cache, promo, and tiered variants are excluded here for readability; see the per-provider sections above for those.

| Provider | Model | Effective date | Input $/M tok | Output $/M tok | Context | Source |
|----------|-------|----------------|---------------|----------------|---------|--------|
| OpenAI | GPT-3 | 2020-06-11 | $6.00 | $12.00 | 2,049 | https://www.deploybase.ai/articles/cost-per-token-over-time-how-llm-api-pricing-has-dropped |
| OpenAI | GPT-3.5 Turbo | 2022-11-14 | $2.00 | $2.00 | 4,096 | https://kickllm.com/research/llm-pricing-history.html |
| OpenAI | GPT-4 | 2023-03-14 | $30.00 | $60.00 | 8,192 | https://tokencost.app/blog/ai-price-index |
| OpenAI | GPT-4 Turbo | 2023-11-06 | $10.00 | $30.00 | 128,000 | https://tokencost.app/blog/ai-price-index |
| OpenAI | GPT-4o | 2024-05-13 | $5.00 | $15.00 | 128,000 | https://pecollective.com/tools/gpt-4o-pricing/ |
| OpenAI | GPT-4o Mini | 2024-07-18 | $0.15 | $0.60 | 128,000 | https://pecollective.com/tools/gpt-4o-pricing/ |
| OpenAI | GPT-4.1 | 2025-01-?? | $2.00 | $8.00 | 1,000,000 | https://pecollective.com/tools/gpt-4o-pricing/ |
| OpenAI | GPT-4.1 Nano | 2025-01-?? | $0.10 | $0.40 | — | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance |
| OpenAI | GPT-5 | 2026-04-?? | $1.25 | $10.00 | 272,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html |
| OpenAI | GPT-5 mini | 2026-04-?? | $0.25 | $2.00 | 272,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html |
| OpenAI | GPT-5.4 | 2026-04-?? | $2.50 | $15.00 | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | GPT-5.4 Mini | 2026-04-?? | $0.75 | $4.50 | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | GPT-5.4 Nano | 2026-04-?? | $0.20 | $1.25 | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | GPT-5.4 Codex | 2026-04-?? | $1.75 | $14.00 | 128,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | GPT-5.5 | 2026-04-24 | $5.00 | $30.00 | 272,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance |
| OpenAI | GPT-5.5 Pro | 2026-04-24 | $30.00 | $180.00 | 128,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance |
| OpenAI | o3 | 2025-01-?? | $2.00 | $8.00 | 200,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance |
| OpenAI | o3-mini | 2025-01-?? | $1.10 | $4.40 | 200,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance |
| OpenAI | o3-pro | 2025-01-?? | $20.00 | $80.00 | 200,000 | https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance |
| OpenAI | o4-mini-2025-04-16 | 2025-04-16 | $4.00 | $16.00 | — | https://developers.openai.com/api/docs/pricing |
| OpenAI | GPT-5.6 Sol | 2026-07-09 | $5.00 | $30.00 | 1,050,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | GPT-5.6 Terra | 2026-07-09 | $2.00 | $12.00 | 1,050,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | GPT-5.6 Luna | 2026-07-09 | $0.20 | $1.20 | 1,050,000 | https://www.cloudzero.com/blog/openai-pricing/ |
| OpenAI | chat-latest | 2026-04-?? | $5.00 | $30.00 | — | https://developers.openai.com/api/docs/pricing |
| OpenAI | gpt-5.3-codex | 2026-04-?? | $1.75 | $14.00 | — | https://developers.openai.com/api/docs/pricing |
| Anthropic | Claude 1 | 2023-03-14 | $11.02 | $32.68 | 9,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html |
| Anthropic | Claude 1.3 / Claude 2 | 2023-07-11 | $11.02 | $32.68 | 100,000 | https://claudearchive.com/pricing-history |
| Anthropic | Claude Instant 1.x | 2023-07-?? | $0.80 | $2.40 | — | https://tokencost.app/blog/ai-price-index |
| Anthropic | Claude 2.1 | 2023-11-21 | $8.00 | $24.00 | 200,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html |
| Anthropic | Claude 3 Opus | 2024-03-04 | $15.00 | $75.00 | 200,000 | https://tokencost.app/blog/ai-price-index |
| Anthropic | Claude 3 Sonnet | 2024-03-04 | $3.00 | $15.00 | 200,000 | https://tokencost.app/blog/ai-price-index |
| Anthropic | Claude 3 Haiku | 2024-03-04 | $0.25 | $1.25 | 200,000 | https://tokencost.app/blog/ai-price-index |
| Anthropic | Claude 3.5 Sonnet | 2024-06-21 | $3.00 | $15.00 | 200,000 | https://claudearchive.com/pricing-history |
| Anthropic | Claude 3.5 Haiku | 2024-10-?? | $0.80 | $4.00 | 200,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html |
| Anthropic | Claude 3.5 Sonnet (updated) | 2024-10-?? | $3.00 | $15.00 | 200,000 | https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html |
| Anthropic | Claude Opus 4 | 2025-05-?? | $15.00 | $75.00 | 200,000 | https://tokencost.app/blog/ai-price-index |
| Anthropic | Claude Sonnet 4 | 2025-09-?? | $3.00 | $15.00 | 200,000 | https://tokencost.app/blog/ai-price-index |
| Anthropic | Claude Opus 4.5 | 2025-11-24 | $5.00 | $25.00 | 200,000 | https://claudearchive.com/pricing-history |
| Anthropic | Claude Sonnet 4.5 | 2025-09-29 | $3.00 | $15.00 | 200,000 | https://claudearchive.com/pricing-history |
| Anthropic | Claude Opus 4.6 | 2026-03-13 | $5.00 | $25.00 | 1,000,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 |
| Anthropic | Claude Sonnet 4.6 | 2026-03-13 | $3.00 | $15.00 | 1,000,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 |
| Anthropic | Claude Haiku 4.5 | 2026-03-13 | $1.00 | $5.00 | 200,000 | https://www.cloudzero.com/blog/claude-pricing/ |
| Anthropic | Claude Sonnet 5 | 2026-08-11 | $2.00 | $10.00 | 1,000,000 | https://www.cloudzero.com/blog/claude-pricing/ |
| Anthropic | Claude Opus 5 | 2026-08-?? | $5.00 | $25.00 | 1,000,000 | https://www.cloudzero.com/blog/claude-pricing/ |
| Anthropic | Claude Fable 5 | 2026-08-?? | $10.00 | $50.00 | 1,000,000 | https://www.cloudzero.com/blog/claude-pricing/ |
| Google / Gemini | Gemini 1.0 Pro | 2023-12-06 | $0.50 | $1.50 | 32,768 | https://tokencost.app/blog/ai-price-index |
| Google / Gemini | Gemini 1.5 Pro | 2024-02-01 | $1.25 | $5.00 | 128,000 | https://tokencost.app/blog/ai-price-index |
| Google / Gemini | Gemini 1.5 Flash | 2024-02-01 | $0.35 | $0.53 | 128,000 | https://tokencost.app/blog/ai-price-index |
| Google / Gemini | Gemini 2.0 Flash | 2025-12-01 | $0.10 | $0.40 | 1,000,000 | https://tokencost.app/blog/ai-price-index |
| Google / Gemini | Gemini 2.0 Flash-Lite | 2025-12-?? | $0.07 | $0.30 | 1,000,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 |
| Google / Gemini | Gemini 2.5 Pro | 2025-06-?? | $1.25 | $10.00 | 1,000,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html |
| Google / Gemini | Gemini 2.5 Flash | 2025-06-?? | $0.30 | $2.50 | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing |
| Google / Gemini | Gemini 2.5 Flash-Lite | 2025-06-?? | $0.10 | $0.40 | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing |
| Google / Gemini | Gemini 3.1 Pro Preview | 2026-04-?? | $2.00 | $12.00 | 2,000,000 | https://ai.google.dev/gemini-api/docs/pricing |
| Google / Gemini | Gemini 3 Flash Preview | 2026-04-?? | $0.50 | $3.00 | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing |
| Google / Gemini | Gemini 3.5 Flash | 2026-05-19 | $1.50 | $9.00 | 1,000,000 | https://www.metacto.com/blogs/the-true-cost-of-google-gemini-a-guide-to-api-pricing-and-integration |
| Google / Gemini | Gemini 3.1 Flash-Lite | 2026-04-?? | $0.25 | $1.50 | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing |
| Google / Gemini | Gemini 3.8 Flash | 2026-04-?? | $0.75 | $3.75 | 1,000,000 | https://ai.google.dev/gemini-api/docs/pricing |
| DeepSeek | DeepSeek V2 | 2023-12-01 | $0.14 | $0.28 | 128,000 | https://deploybase.ai/articles/llm-pricing-history-how-costs-dropped-99-since-2023 |
| DeepSeek | DeepSeek V3 | 2024-12-01 | $0.27 | $1.10 | 128,000 | https://tokencost.app/blog/ai-price-index |
| DeepSeek | DeepSeek V3.2 | 2025-12-?? | $0.28 | $0.42 | 128,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 |
| DeepSeek | DeepSeek R1 | 2025-01-?? | $0.55 | $2.19 | 128,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 |
| DeepSeek | DeepSeek V4 Pro | 2026-01-01 | $0.66 | $1.98 | 1,000,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ |
| DeepSeek | DeepSeek V4 Flash | 2026-01-01 | $0.22 | $0.28 | 1,000,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html |
| xAI / Grok | Grok 3 | 2025-04-01 | $3.00 | $15.00 | 128,000 | https://apiscout.dev/guides/llm-api-pricing-comparison-2026 |
| xAI / Grok | Grok 3 Mini | 2026-04-?? | $3.00 | $5.00 | 128,000 | https://www.getapipulse.com/blog-q2-2026-pricing-report.html |
| xAI / Grok | Grok 4.3 | 2026-05-?? | $0.20 | $0.80 | 2,000,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ |
| xAI / Grok | Grok Build 0.1 | 2026-05-?? | $1.00 | $2.00 | 256,000 | https://chatforest.com/guides/llm-api-pricing-comparison-2026/ |
| Mistral AI | Mistral Large 3 (2512) | 2025-12-?? | $0.50 | $1.50 | 262,144 | https://mistral.ai/pricing/api/ |
| Mistral AI | Mistral Large 2.1 (2411) | 2024-11-?? | $2.00 | $6.00 | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Large 2.0 (2407) | 2024-07-?? | $2.00 | $6.00 | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Large 1.0 (2402) | 2024-02-?? | $2.00 | $6.00 | 128,000 | https://docs.mistral.ai/models |
| Mistral AI | Mistral Medium 3.5 | 2026-04-?? | $1.50 | $7.50 | 256,000 | https://mistral.ai/pricing/api/ |
| Mistral AI | Mistral Medium 3.1 (2508) | 2025-08-?? | $0.40 | $2.00 | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Medium 3 (2505) | 2025-05-?? | $0.40 | $2.00 | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Medium 1.0 (2312) | 2023-12-?? | $0.40 | $2.00 | 131,072 | https://docs.mistral.ai/models |
| Mistral AI | Mistral Small 4 (2603) | 2026-03-?? | $0.15 | $0.60 | 128,000 | https://mistral.ai/pricing/api/ |
| Mistral AI | Mistral Small 3.2 (2506) | 2025-06-?? | $0.08 | $0.20 | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Small 3.1 (2503) | 2025-03-?? | $0.10 | $0.30 | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Small 3.0 (2501) | 2025-01-?? | $0.10 | $0.30 | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Small 2.0 (2409) | 2024-09-?? | $0.10 | $0.30 | 128,000 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Small 1.0 (2402) | 2024-02-?? | $0.10 | $0.30 | 128,000 | https://docs.mistral.ai/models |
| Mistral AI | Mistral Small 3.2 24B | 2025-06-?? | $0.07 | $0.20 | 131,072 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Mistral Nemo | 2024-07-?? | $0.02 | $0.03 | 131,072 | https://mistral.ai/pricing/api/ |
| Mistral AI | Codestral 2508 | 2025-08-?? | $0.30 | $0.90 | 256,000 | https://mistral.ai/pricing/api/ |
| Mistral AI | Devstral 2 2512 | 2025-12-?? | $0.40 | $0.90 | 262,144 | https://pricepertoken.com/pricing-page/provider/mistral-ai |
| Mistral AI | Ministral 3 8B (2512) | 2025-12-?? | $0.15 | $0.15 | 262,144 | https://mistral.ai/pricing/api/ |
| Mistral AI | Ministral 3 3B (2512) | 2025-12-?? | $0.10 | $0.10 | 262,144 | https://mistral.ai/pricing/api/ |
| Cohere | Command (legacy) | 2023-??-?? | $1.00 | $2.00 | 4,096 | https://cohere.com/pricing |
| Cohere | Command-light (legacy) | 2023-??-?? | $0.30 | $0.60 | 4,096 | https://cohere.com/pricing |
| Cohere | Command R 03-2024 | 2024-03-?? | $0.50 | $1.50 | 128,000 | https://cohere.com/pricing |
| Cohere | Command R+ 04-2024 | 2024-04-?? | $3.00 | $15.00 | 128,000 | https://cohere.com/pricing |
| Cohere | Command R+ 08-2024 | 2024-08-?? | $2.50 | $10.00 | 128,000 | https://cohere.com/pricing |
| Cohere | Command R 08-2024 | 2024-08-?? | $0.15 | $0.60 | 128,000 | https://cohere.com/pricing |
| Cohere | Command R7B 12-2024 | 2024-12-?? | $0.04 | $0.15 | 128,000 | https://cohere.com/pricing |
| Cohere | Command A | 2025-??-?? | $2.50 | $10.00 | 256,000 | https://cohere.com/pricing |
| Cohere | Aya Expanse 8B / 32B | 2025-??-?? | $0.50 | $1.50 | 128,000 | https://cohere.com/pricing |
| Meta Llama (hosted) | Llama 3.1 8B (hosted: Groq) | 2024-07-?? | $0.05 | $0.08 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.1 8B (hosted: Together AI) | 2024-07-?? | $0.18 | $0.18 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.1 8B (hosted: Fireworks) | 2024-07-?? | $0.20 | $0.20 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.3 70B (hosted: DeepInfra) | 2024-12-?? | $0.23 | $0.40 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.3 70B (hosted: Groq) | 2024-12-?? | $0.59 | $0.79 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.3 70B (hosted: Together AI) | 2024-12-?? | $0.88 | $0.88 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.3 70B (hosted: Fireworks) | 2024-12-?? | $0.90 | $0.90 | 128,000 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.1 405B (hosted: Fireworks) | 2024-07-?? | $3.00 | $3.00 | 131,072 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 3.1 405B (hosted: Together AI) | 2024-07-?? | $3.50 | $3.50 | 131,072 | https://www.aipricing.guru/meta-pricing/ |
| Meta Llama (hosted) | Llama 4 Scout (hosted: Groq) | 2025-??-?? | $0.11 | $0.34 | 10,000,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html |
| Meta Llama (hosted) | Llama 4 Maverick (hosted: Groq) | 2025-??-?? | $0.20 | $0.60 | 10,000,000 | https://www.getapipulse.com/blog-state-of-llm-pricing-may-2026.html |
| Alibaba / Qwen | Qwen3-Max | 2025-??-?? | $1.20 | $6.00 | 262,144 | https://deepinfra.com/blog/qwen-api-pricing-2026-guide |
| Alibaba / Qwen | Qwen3-Max Thinking | 2025-??-?? | $0.78 | $3.90 | 262,144 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3 Max | 2026-??-?? | $2.00 | $6.00 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.6 Max Preview | 2025-??-?? | $1.30 | $7.80 | 262,144 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.7 Plus | 2026-??-?? | $0.32 | $1.28 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.7 Max | 2026-??-?? | $1.25 | $3.75 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.8 Max | 2026-08-03 | $2.00 | $6.00 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.8 Flash | 2026-08-26 | $0.14 | $0.42 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.6 Flash | 2025-??-?? | $0.19 | $1.13 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.6 Plus | 2025-??-?? | $0.50 | $3.00 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.5 Plus | 2025-??-?? | $0.50 | $3.00 | 1,000,000 | https://qwen.ai/apiplatform |
| Alibaba / Qwen | Qwen3 Flash | 2025-??-?? | $0.05 | $0.40 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3 Coder 480B A35B | 2025-??-?? | $1.50 | $7.50 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3 Coder Next | 2025-??-?? | $0.11 | $0.80 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3-VL Plus | 2025-??-?? | $0.20 | $1.60 | 131,027 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3 VL 235B A22B | 2025-??-?? | $0.70 | $2.80 | 131,027 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.5 Omni Flash | 2025-??-?? | $0.43 | $1.66 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen3.5 Omni Plus | 2026-??-?? | $1.00 | $6.00 | 1,000,000 | https://www.alibabacloud.com/help/en/model-studio/models |
| Alibaba / Qwen | Qwen VL OCR | 2025-??-?? | $0.72 | $0.72 | 131,027 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen-MT Turbo | 2025-??-?? | $0.16 | $0.49 | 1,000,000 | https://developer.puter.com/tutorials/qwen-api-pricing/ |
| Alibaba / Qwen | Qwen2.5 72B (hosted: DeepInfra) | 2024-12-?? | $0.23 | $0.40 | 128,000 | https://deepinfra.com/blog/qwen-api-pricing-2026-guide |
| Moonshot / Kimi | Kimi K2 | 2025-01-01 | $0.60 | $2.50 | 128,000 | https://benchlm.ai/moonshot/api-pricing |
| Moonshot / Kimi | Kimi K2.5 | 2025-07-24 | $0.60 | $3.00 | 256,000 | https://benchlm.ai/moonshot/api-pricing |
| Moonshot / Kimi | Kimi K2.6 | 2025-11-01 | $0.95 | $4.00 | 262,144 | https://benchlm.ai/moonshot/api-pricing |
| Moonshot / Kimi | Kimi K2.7 Code | 2026-01-01 | $0.95 | $4.00 | 262,144 | https://benchlm.ai/moonshot/api-pricing |
| Moonshot / Kimi | Kimi K2.7 Code Highspeed | 2026-01-01 | $1.90 | $8.00 | 262,144 | https://www.chatbase.co/blog/kimi-k2-api |
| Moonshot / Kimi | Kimi K3 | 2026-09-01 | $3.00 | $15.00 | 1,050,000 | https://benchlm.ai/moonshot/api-pricing |

---

## 8. Market data

See `kb/market_data.md` for the full dataset with source URLs. Key numbers below:

### Market sizing

| Metric | Value | Year |
|--------|-------|------|
| AI market size | $390.9 billion | 2025 |
| AI market size (projected) | $539.5 billion | 2026 |
| AI market size (projected) | $3,497.3 billion | 2033 |
| CAGR (2026–2033) | 30.2% | — |

### Enterprise spend

| Metric | Value | Period |
|--------|-------|--------|
| Enterprise LLM spend | $3.5 billion | Late 2024 |
| Enterprise LLM spend | $8.4 billion | Mid 2025 |
| AI-native software budget share | 2.3% | January 2025 |
| AI-native software budget share | 4.8% | July 2026 |

### Token volume

| Provider | Volume | Period |
|----------|--------|--------|
| Google Gemini | 9.7 trillion tokens/month | ~2023 |
| Google Gemini | 3.2 quadrillion tokens/month | 2026 |
| Google Gemini growth | ~330x in 2 years | 2023 → 2026 |

### Infrastructure investment

| Metric | Value | Year |
|--------|-------|------|
| Big 4 hyperscaler AI capex | $370B–$410B | 2025 |
| Big 4 hyperscaler AI capex (projected) | $650B | 2026 |
| Broader AI infrastructure run-rate | approaching $1 trillion | 2026 |
| Total AI infrastructure forecast | $6.3 trillion | 2030 |

### Price dynamics summary

- Frontier model output price: **$60/M tokens** (GPT-4, March 2023) → **$15/M tokens** (GPT-5.4, 2026) = **4x reduction** at the frontier.
- Conservative estimate: ~**100x** reduction at frontier tier and **500x+** at budget tier from 2023 to 2025.
- Token price collapse: **95%+ in 3 years** (2023–2026).
- DeepSeek V3 output: **$0.14/M tokens** vs GPT-4 launch $60/M — roughly **100x cheaper** for frontier-quality output.
- Price decline rates (Epoch AI): **9x annually** for basic models, **900x** for top-tier (2021–2025).

---

## 9. Sources

### Provider pricing pages (canonical)

- **OpenAI:** https://developers.openai.com/api/docs/pricing
- **Anthropic:** https://platform.claude.com/docs/en/about-claude/pricing
- **Google Gemini:** https://ai.google.dev/gemini-api/docs/pricing
- **DeepSeek:** https://api-docs.deepseek.com/quick_start/pricing/
- **xAI:** https://docs.x.ai/developers/pricing

### Aggregators (used for historical price points and cross-provider comparison)

- CloudZero (OpenAI): https://www.cloudzero.com/blog/openai-pricing/
- CloudZero (Claude): https://www.cloudzero.com/blog/claude-pricing/
- Metacto (Gemini): https://www.metacto.com/blogs/the-true-cost-of-google-gemini-a-guide-to-api-pricing-and-integration
- Metacto (OpenAI): https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance
- IntuitionLabs (LLM comparison): https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025
- TokenCost (AI Price Index): https://tokencost.app/blog/ai-price-index
- APIScout (LLM comparison): https://apiscout.dev/guides/llm-api-pricing-comparison-2026
- ChatForest (LLM comparison): https://chatforest.com/guides/llm-api-pricing-comparison-2026/
- DeployBase (cost-per-token over time): https://deploybase.ai/articles/cost-per-token-over-time-how-llm-api-pricing-has-dropped
- DeployBase (LLM pricing history): https://deploybase.ai/articles/llm-pricing-history-how-costs-dropped-99-since-2023
- TokenMix (AI API pricing history): https://tokenmix.ai/blog/ai-pricing-trends-history
- iapi.buzz (Anthropic pricing history): https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html
- claudearchive.com (Claude pricing history): https://claudearchive.com/pricing-history
- kickllm (LLM pricing history): https://kickllm.com/research/llm-pricing-history.html

### Market data (analysts and research)

- Grand View Research (AI market): https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market
- Tropic AI pricing trends: https://www.tropicapp.io/blog/ai-pricing-trends
- Zylo (AI cost): https://zylo.com/blog/ai-cost
- Josh Bersin (AI pricing / infrastructure): https://joshbersin.com/2026/05/ai-prices-are-going-up-up-up-and-what-this-means-for-enterprise-ai
- IEEE Spectrum (Stanford AI Index 2026): https://spectrum.ieee.org/state-of-ai-index-2026
- Token price collapse (Substack): https://thegtmnewsletter.substack.com/p/ai-token-price-collapse-costs-rising
- Coding Nexus (AI costs going down): https://medium.com/coding-nexus/ai-costs-are-going-down-where-is-market-going-abb054a6715a
- Anthropic Economic Index (March 2026): https://www.anthropic.com/research/economic-index-march-2026-report
- White House CEA report (Great Divergence): https://www.whitehouse.gov/wp-content/uploads/2026/01/Artificial-Intelligence-and-the-Great-Divergence-5.pdf

---

*Report generated from `kb/price_points_*.jsonl` by `scripts/generate_report.py`. All price points include source URLs and effective dates. See `kb/CONVENTIONS.md` and `kb/PRICE_POINTS_SPEC.md` for data-quality rules.*