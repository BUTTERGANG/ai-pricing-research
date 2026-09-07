# Price Points Knowledge Base

## Purpose

Single source of truth for historical and current AI model pricing, maintained as a structured dataset for trend analysis and sentiment correlation.

## Data format

Each entry is a JSON object in `price_points.jsonl`, one line per price point. Fields:

| Field | Required | Description |
|---|---|---|
| `id` | yes | Unique integer id, monotonic. |
| `provider` | yes | Lowercase provider id: `openai`, `anthropic`, `google`, `deepseek`, `xai`, `openrouter`, `meta`, `mistral`, `cohere`, `alibaba`, `moonshot`, `other`. |
| `model_name` | yes | Exact model name as published (e.g. `GPT-4`, `claude-3-opus`, `gemini-1.5-pro`, `deepseek-v3`). |
| `model_version_note` | no | Human note on version/generation transitions, deprecations, renames. |
| `effective_date` | yes | ISO date (`YYYY-MM-DD`) when the price took effect. Not article/publication date. |
| `input_price_usd_per_mtokens` | yes | Standard list input price per 1M tokens, in USD. Use `null` if free or not applicable. |
| `output_price_usd_per_mtokens` | yes | Standard list output price per 1M tokens, in USD. Use `null` if free or not applicable. |
| `price_type` | yes | One of: `standard_list`, `promo`, `batch`, `cache`, `contributor`, `blended`, `free`, `tiered`. |
| `price_tier_note` | no | If `tiered`, describe the tiers (e.g. "≤200K input: $1.25; >200K: $2.50"). |
| `context_window_tokens` | no | Context window at this price point, if known (e.g. `200000`). |
| `source_url` | yes | URL where this price was read. |
| `source_type` | yes | One of: `provider_pricing_page`, `openrouter_listing`, `third_party_aggregator`, `news_article`, `press_release`, `other`. |
| `notes` | no | Free-text notes, caveats, effective-date vs publication-date discrepancies, etc. |
| `retrieved_at` | yes | ISO timestamp when this entry was added to the KB. |
| `retrieved_by` | yes | Identifier for whoever/whatever added this entry. |

## Version tracking rules

- Pin the exact model name and version to each price entry — not just provider + date.
- When a model is deprecated, renamed, or replaced, note the transition explicitly in `model_version_note` rather than letting the series continue silently under a different underlying model.
- Don't let a price series imply continuity across different model generations (e.g. Gemini Flash today vs Gemini Flash a year ago are not the same product).

## Price type rules

- **Primary series basis**: `standard_list` (input and output tokens priced separately).
- Track separately as annotations, not as the main price line:
  - `promo` — limited-time or introductory discounts.
  - `contributor` — reduced pricing in exchange for allowing training on user data.
  - `batch` — batch processing rates.
  - `cache` — cached-token rates.
  - `blended` — only when a source reports a blended rate; label explicitly and note the assumed input/output ratio.
  - `free` — $0/token (e.g. free tiers, free models).
  - `tiered` — when the price depends on context length or other dimension.

## Effective date rules

- Record when a price actually took effect, not when a news article or blog post about it was published.
- Publication can lag the actual change by days or weeks; this matters for sentiment correlation.
- When only a publication date is known, record it in `notes` and flag the uncertainty.

## Source attribution

Record whether each price came from:
- `provider_pricing_page` — the provider's own pricing page (canonical).
- `openrouter_listing` — OpenRouter's listed price.
- `third_party_aggregator` — a third-party pricing aggregator.
- `news_article` — a news article or blog post.
- `press_release` — an official press release.
- `other` — anything else.

These occasionally disagree; knowing which source was used helps resolve conflicts later.

## Blended rates

If a source only reports a blended rate, label it `blended` and note the assumed input/output ratio behind it in `notes`.

## Maintenance

- Entries are appended, never overwritten. Corrections are new entries with a `notes` reference to the prior entry.
- The canonical dataset is `price_points.jsonl`. Views and reports are derived from it.
