#!/usr/bin/env python3
"""Export all price_points_*.jsonl files to a single CSV for analysis."""
import json
import csv
import glob
from pathlib import Path

FIELDS = [
    "id", "provider", "model_name", "model_version_note",
    "effective_date", "input_price_usd_per_mtokens", "output_price_usd_per_mtokens",
    "price_type", "price_tier_note", "context_window_tokens",
    "source_url", "source_type", "notes", "retrieved_at", "retrieved_by",
]

out_path = Path("kb/all_price_points.csv")
rows = []
for path in sorted(glob.glob("kb/price_points_*.jsonl")):
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        rows.append([r.get(f, "") for f in FIELDS])

with out_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(FIELDS)
    w.writerows(rows)

print(f"Wrote {out_path} — {len(rows)} data rows + header")
