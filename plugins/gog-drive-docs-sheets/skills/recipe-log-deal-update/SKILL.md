---
name: recipe-log-deal-update
description: "Append a deal status update to a Google Sheets sales tracking spreadsheet using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "sales"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Log Deal Update to Google Sheets

Append a deal status update to a Google Sheets sales tracking spreadsheet using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Append deal status update row
gog sheets append <SPREADSHEET_ID> "Pipeline!A1" \
  "2026-03-24" "Acme Corp" "Proposal Delivered" "$75,000" "Q2" "salem" \
  --json

# 2. Inspect latest 5 rows
gog sheets get <SPREADSHEET_ID> "Pipeline!A100:F105" --json
```

### Option B: Using `gws` CLI
```bash
# 1. Append deal update
gws sheets +append \
  --spreadsheet <SPREADSHEET_ID> \
  --range "Pipeline" \
  --values '["2026-03-24", "Acme Corp", "Proposal Delivered", "$75,000", "Q2", "salem"]' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/validate_deal_fields.py](scripts/validate_deal_fields.py)
