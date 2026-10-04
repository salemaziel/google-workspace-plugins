---
name: recipe-backup-sheet-as-csv
description: "Export a Google Sheets spreadsheet as a CSV file for local backup or processing using either gog or gws CLI."
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

# Export a Google Sheet as CSV

Export a Google Sheets spreadsheet as a CSV file for local backup or processing using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Export spreadsheet to local CSV file
gog sheets export <SPREADSHEET_ID> --format csv --out "./backup.csv"

# 2. Or read raw tabular values as JSON
gog sheets get <SPREADSHEET_ID> "Sheet1!A1:Z100" --json
```

### Option B: Using `gws` CLI
```bash
# 1. Export via Drive API export endpoint
gws drive files export \
  --params '{"fileId": "<SPREADSHEET_ID>", "mimeType": "text/csv"}' -o backup.csv

# 2. Or read values directly as CSV
gws sheets +read --spreadsheet <SPREADSHEET_ID> --range "Sheet1" --format csv
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/csv_row_counter.py](scripts/csv_row_counter.py)
