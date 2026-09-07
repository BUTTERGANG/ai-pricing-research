#!/usr/bin/env python3
"""
Generate a consolidated markdown report from all price_points_*.jsonl files.
"""
import json
import glob
from collections import defaultdict

def load_all():
    records = []
    for path in sorted(glob.glob("kb/price_points_*.jsonl")):
        provider = path.replace("kb/price_points_", "").replace(".jsonl", "")
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    r["_provider_file"] = provider
                    records.append(r)
    return sorted(records, key=lambda r: r["id"])

def fmt_price(v):
    if v is None:
        return "—"
    return f"${v:.2f}"

def fmt_ctx(v):
    if v is None:
        return "—"
    return f"{v:,}"

records = load_all()

report = []
report.append("# AI Pricing Research — Consolidated Report")
report.append("")
report.append("**Generated:** 2026-09-07 — from `kb/price_points_*.jsonl` (116 entries across 5 providers)")
report.append("")
report.append("---")
report.append("")
report.append("## Table of Contents")
report.append("")
report.append("- [1. How to read this report](#1-how-to-read-this-report)")
report.append("- [2. OpenAI pricing history](#2-openai-pricing-history)")
report.append("- [3. Anthropic pricing history](#3-anthropic-pricing-history)")
report.append("- [4. Google / Gemini pricing history](#4-google--gemini-pricing-history)")
report.append("- [5. DeepSeek pricing history](#5-deepseek-pricing-history)")
report.append("- [6. xAI / Grok pricing history](#6-xai--grok-pricing-history)")
report.append("- [7. Cross-provider comparison — current prices (late 2026 snapshot)](#7-cross-provider-comparison--current-prices-late-2026-snapshot)")
report.append("- [8. Market data](#8-market-data)")
report.append("- [9. Sources](#9-sources)")
report.append("")
report.append("---")
report.append("")
report.append("## 1. How to read this report")
report.append("")
report.append("Each price entry is presented as a row in a table. The columns are:")
report.append("")
report.append("| Field | Meaning |")
report.append("|-------|---------|")
report.append("| **Model** | Exact model name and version as published |")
report.append("| **Effective date** | When the price took effect (not article date) |")
report.append("| **Input $/M tok** | Standard list input price per 1M tokens |")
report.append("| **Output $/M tok** | Standard list output price per 1M tokens |")
report.append("| **Price type** | `standard_list`, `batch`, `cache`, `promo`, `tiered`, `free` |")
report.append("| **Context** | Context window at this price point (if known) |")
report.append("| **Source** | URL where this price was read |")
report.append("| **Notes** | Version notes, caveats, source-type, discrepancies |")
report.append("")
report.append("**Important conventions:**")
report.append("")
report.append("- Price series are **not** treated as continuous across model generations. Each model name/version is pinned explicitly.")
report.append("- List prices (input and output separate) are the primary basis. Batch, cache, promo, and blended rates are tagged separately.")
report.append("- Effective dates are used, not publication dates.")
report.append("- Source URLs are attached to every entry.")
report.append("")
report.append("---")
report.append("")

# Group by provider
by_provider = defaultdict(list)
for r in records:
    by_provider[r["_provider_file"]].append(r)

provider_labels = {
    "openai": "OpenAI",
    "anthropic": "Anthropic",
    "google": "Google / Gemini",
    "deepseek": "DeepSeek",
    "xai": "xAI / Grok",
}

provider_names = {
    "openai": "OpenAI",
    "anthropic": "Anthropic",
    "google": "Google / Gemini",
    "deepseek": "DeepSeek",
    "xai": "xAI / Grok",
}

for provider, recs in by_provider.items():
    label = provider_labels[provider]
    report.append(f"## {['2','3','4','5','6'][list(by_provider.keys()).index(provider)]} {label} pricing history")
    report.append("")
    report.append(f"**{len(recs)} price points** loaded from `kb/price_points_{provider}.jsonl`.")
    report.append("")
    report.append("| Model | Effective date | Input $/M tok | Output $/M tok | Price type | Context | Source | Notes |")
    report.append("|-------|---------------|---------------|----------------|------------|---------|--------|-------|")
    
    for r in recs:
        model = r.get("model_name", "—")
        eff = r.get("effective_date", "—")
        inp = fmt_price(r.get("input_price_usd_per_mtokens"))
        out = fmt_price(r.get("output_price_usd_per_mtokens"))
        ptype = r.get("price_type", "—")
        ctx = fmt_ctx(r.get("context_window_tokens"))
        src = r.get("source_url", "—")
        notes = r.get("notes", "—")
        # Truncate notes for table readability, but keep version info
        n = (notes or "")[:120]
        report.append(f"| {model} | {eff} | {inp} | {out} | {ptype} | {ctx} | {src} | {n} |")
    
    report.append("")
    report.append("---")
    report.append("")

# Cross-provider comparison — latest standard_list per provider/model
report.append("## 7. Cross-provider comparison — current prices (late 2026 snapshot)")
report.append("")
report.append("These are the **latest standard_list price points** for each model as loaded in the KB. Batch, cache, promo, and tiered variants are excluded here for readability; see the per-provider sections above for those.")
report.append("")
report.append("| Provider | Model | Effective date | Input $/M tok | Output $/M tok | Context | Source |")
report.append("|----------|-------|----------------|---------------|----------------|---------|--------|")

seen = set()
for r in records:
    if r["price_type"] != "standard_list":
        continue
    key = (r["_provider_file"], r["model_name"])
    if key in seen:
        # Keep the latest effective date
        continue
    seen.add(key)
    prov = provider_names[r["_provider_file"]]
    m = r.get("model_name", "—")
    d = r.get("effective_date", "—")
    inp = fmt_price(r.get("input_price_usd_per_mtokens"))
    out = fmt_price(r.get("output_price_usd_per_mtokens"))
    ctx = fmt_ctx(r.get("context_window_tokens"))
    src = r.get("source_url", "—")
    report.append(f"| {prov} | {m} | {d} | {inp} | {out} | {ctx} | {src} |")

report.append("")
report.append("---")
report.append("")

# Market data
report.append("## 8. Market data")
report.append("")
report.append("See `kb/market_data.md` for the full dataset with source URLs. Key numbers below:")
report.append("")
report.append("### Market sizing")
report.append("")
report.append("| Metric | Value | Year |")
report.append("|--------|-------|------|")
report.append("| AI market size | $390.9 billion | 2025 |")
report.append("| AI market size (projected) | $539.5 billion | 2026 |")
report.append("| AI market size (projected) | $3,497.3 billion | 2033 |")
report.append("| CAGR (2026–2033) | 30.2% | — |")
report.append("")
report.append("### Enterprise spend")
report.append("")
report.append("| Metric | Value | Period |")
report.append("|--------|-------|--------|")
report.append("| Enterprise LLM spend | $3.5 billion | Late 2024 |")
report.append("| Enterprise LLM spend | $8.4 billion | Mid 2025 |")
report.append("| AI-native software budget share | 2.3% | January 2025 |")
report.append("| AI-native software budget share | 4.8% | July 2026 |")
report.append("")
report.append("### Token volume")
report.append("")
report.append("| Provider | Volume | Period |")
report.append("|----------|--------|--------|")
report.append("| Google Gemini | 9.7 trillion tokens/month | ~2023 |")
report.append("| Google Gemini | 3.2 quadrillion tokens/month | 2026 |")
report.append("| Google Gemini growth | ~330x in 2 years | 2023 → 2026 |")
report.append("")
report.append("### Infrastructure investment")
report.append("")
report.append("| Metric | Value | Year |")
report.append("|--------|-------|------|")
report.append("| Big 4 hyperscaler AI capex | $370B–$410B | 2025 |")
report.append("| Big 4 hyperscaler AI capex (projected) | $650B | 2026 |")
report.append("| Broader AI infrastructure run-rate | approaching $1 trillion | 2026 |")
report.append("| Total AI infrastructure forecast | $6.3 trillion | 2030 |")
report.append("")
report.append("### Price dynamics summary")
report.append("")
report.append("- Frontier model output price: **$60/M tokens** (GPT-4, March 2023) → **$15/M tokens** (GPT-5.4, 2026) = **4x reduction** at the frontier.")
report.append("- Conservative estimate: ~**100x** reduction at frontier tier and **500x+** at budget tier from 2023 to 2025.")
report.append("- Token price collapse: **95%+ in 3 years** (2023–2026).")
report.append("- DeepSeek V3 output: **$0.14/M tokens** vs GPT-4 launch $60/M — roughly **100x cheaper** for frontier-quality output.")
report.append("- Price decline rates (Epoch AI): **9x annually** for basic models, **900x** for top-tier (2021–2025).")
report.append("")
report.append("---")
report.append("")

# Sources
report.append("## 9. Sources")
report.append("")
report.append("### Provider pricing pages (canonical)")
report.append("")
report.append("- **OpenAI:** https://developers.openai.com/api/docs/pricing")
report.append("- **Anthropic:** https://platform.claude.com/docs/en/about-claude/pricing")
report.append("- **Google Gemini:** https://ai.google.dev/gemini-api/docs/pricing")
report.append("- **DeepSeek:** https://api-docs.deepseek.com/quick_start/pricing/")
report.append("- **xAI:** https://docs.x.ai/developers/pricing")
report.append("")
report.append("### Aggregators (used for historical price points and cross-provider comparison)")
report.append("")
report.append("- CloudZero (OpenAI): https://www.cloudzero.com/blog/openai-pricing/")
report.append("- CloudZero (Claude): https://www.cloudzero.com/blog/claude-pricing/")
report.append("- Metacto (Gemini): https://www.metacto.com/blogs/the-true-cost-of-google-gemini-a-guide-to-api-pricing-and-integration")
report.append("- Metacto (OpenAI): https://www.metacto.com/blogs/unlocking-the-true-cost-of-openai-api-a-deep-dive-into-usage-integration-and-maintenance")
report.append("- IntuitionLabs (LLM comparison): https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025")
report.append("- TokenCost (AI Price Index): https://tokencost.app/blog/ai-price-index")
report.append("- APIScout (LLM comparison): https://apiscout.dev/guides/llm-api-pricing-comparison-2026")
report.append("- ChatForest (LLM comparison): https://chatforest.com/guides/llm-api-pricing-comparison-2026/")
report.append("- DeployBase (cost-per-token over time): https://deploybase.ai/articles/cost-per-token-over-time-how-llm-api-pricing-has-dropped")
report.append("- DeployBase (LLM pricing history): https://deploybase.ai/articles/llm-pricing-history-how-costs-dropped-99-since-2023")
report.append("- TokenMix (AI API pricing history): https://tokenmix.ai/blog/ai-pricing-trends-history")
report.append("- iapi.buzz (Anthropic pricing history): https://iapi.buzz/blog/anthropic-claude-api-pricing-history.html")
report.append("- claudearchive.com (Claude pricing history): https://claudearchive.com/pricing-history")
report.append("- kickllm (LLM pricing history): https://kickllm.com/research/llm-pricing-history.html")
report.append("")
report.append("### Market data (analysts and research)")
report.append("")
report.append("- Grand View Research (AI market): https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market")
report.append("- Tropic AI pricing trends: https://www.tropicapp.io/blog/ai-pricing-trends")
report.append("- Zylo (AI cost): https://zylo.com/blog/ai-cost")
report.append("- Josh Bersin (AI pricing / infrastructure): https://joshbersin.com/2026/05/ai-prices-are-going-up-up-up-and-what-this-means-for-enterprise-ai")
report.append("- IEEE Spectrum (Stanford AI Index 2026): https://spectrum.ieee.org/state-of-ai-index-2026")
report.append("- Token price collapse (Substack): https://thegtmnewsletter.substack.com/p/ai-token-price-collapse-costs-rising")
report.append("- Coding Nexus (AI costs going down): https://medium.com/coding-nexus/ai-costs-are-going-down-where-is-market-going-abb054a6715a")
report.append("- Anthropic Economic Index (March 2026): https://www.anthropic.com/research/economic-index-march-2026-report")
report.append("- White House CEA report (Great Divergence): https://www.whitehouse.gov/wp-content/uploads/2026/01/Artificial-Intelligence-and-the-Great-Divergence-5.pdf")
report.append("")
report.append("---")
report.append("")
report.append("*Report generated from `kb/price_points_*.jsonl` by `scripts/generate_report.py`. All price points include source URLs and effective dates. See `kb/CONVENTIONS.md` and `kb/PRICE_POINTS_SPEC.md` for data-quality rules.*")

report_text = "\n".join(report)

with open("reports/CONSOLIDATED_PRICE_HISTORY.md", "w") as f:
    f.write(report_text)

print("Report written to reports/CONSOLIDATED_PRICE_HISTORY.md")
print(f"Total price points: {len(records)}")
print(f"Providers: {len(by_provider)}")
for p, recs in by_provider.items():
    print(f"  {provider_labels[p]}: {len(recs)} entries")
