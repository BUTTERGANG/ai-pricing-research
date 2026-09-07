# Historical AI Model Pricing Data — Accuracy Instructions

Context: compiling historical pricing data for AI models (Gemini, OpenAI, Anthropic, and others) back to 2023-2024. Since this history only spans a few years and comes from scattered sources, follow these rules to keep the data accurate and usable for later analysis (including correlation against news sentiment).

## 1. Track model version alongside every price point
Pin the exact model name and version to each price entry — not just the company and date. Don't let a price series imply continuity across different model generations (e.g. Gemini Flash today vs. Gemini Flash a year ago are not the same product). When a model is deprecated, renamed, or replaced, note that transition explicitly rather than letting the series continue silently under a different underlying model.

## 2. Distinguish list price from effective price
Capture **standard list price** (input and output tokens priced separately) as the primary basis for the historical series. Track separately, as annotations rather than part of the main price line:
- Promotional/limited-time discounts
- Contributor or data-sharing tiers (e.g. reduced pricing in exchange for allowing training on user data)
- Batch processing rates
- Cached-token rates

If a source only reports a blended rate, label it explicitly as blended and note the assumed input/output ratio behind it.

## 3. Timestamp by effective date, not publication date
Record when a price actually took effect, not when a news article, blog post, or announcement about it was published. Publication can lag the actual change by days or weeks. This matters especially if this data is later correlated against news sentiment timing — using article dates instead of effective dates would introduce false lead/lag signals.

## 4. Note the source for each price point
Record whether each price came from the provider's own pricing page, OpenRouter's listed price, or a third-party aggregator. These occasionally disagree, and knowing which source was used helps resolve conflicts later.
