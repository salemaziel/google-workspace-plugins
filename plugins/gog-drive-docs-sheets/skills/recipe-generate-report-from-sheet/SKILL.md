---
name: recipe-generate-report-from-sheet
description: "Read data from a Google Sheet and create a formatted Google Docs report using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Generate a Google Docs Report from Sheet Data

Read data from a Google Sheet and create a formatted Google Docs report using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Extract metrics from Sheet
gog sheets get <SPREADSHEET_ID> "Sales!A1:D20" --json > sales_data.json

# 2. Create target report document
gog docs create "Sales Report - Q1 2026" --json

# 3. Write formatted report body
gog docs write <DOC_ID> --file report_summary.md --json
```

### Option B: Using `gws` CLI
```bash
# 1. Read sheet data
gws sheets +read --spreadsheet <SPREADSHEET_ID> --range "Sales!A1:D20"

# 2. Create document
gws docs documents create --json '{"title": "Sales Report - Q1 2026"}'

# 3. Write summary
gws docs +write \
  --document-id <DOC_ID> \
  --text "## Sales Report - Q1 2026\n\n### Key Metrics\nTotal deals closed: 45\nRevenue: $125,000"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/sheet_to_summary.py](scripts/sheet_to_summary.py)
