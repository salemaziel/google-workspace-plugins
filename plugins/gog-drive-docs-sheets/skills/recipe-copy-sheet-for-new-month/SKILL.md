---
name: recipe-copy-sheet-for-new-month
description: "Duplicate a Google Sheets template tab for a new month of tracking using either gog or gws CLI."
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

# Copy a Google Sheet for a New Month

Duplicate a Google Sheets template tab for a new month of tracking using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Add new tab for the new month
gog sheets add-tab <SPREADSHEET_ID> "April 2026" --json

# 2. Copy template contents to the new tab
gog sheets copy <SPREADSHEET_ID> "April 2026 Tracking" --json
```

### Option B: Using `gws` CLI
```bash
# 1. Copy sheet tab within spreadsheet
gws sheets spreadsheets sheets copyTo \
  --params '{"spreadsheetId": "<SPREADSHEET_ID>", "sheetId": 0}' \
  --json '{"destinationSpreadsheetId": "<SPREADSHEET_ID>"}'

# 2. Rename tab to new month
gws sheets spreadsheets batchUpdate \
  --params '{"spreadsheetId": "<SPREADSHEET_ID>"}' \
  --json '{
    "requests": [{"updateSheetProperties": {"properties": {"sheetId": 123, "title": "April 2026"}, "fields": "title"}}]
  }' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/next_month_namer.py](scripts/next_month_namer.py)
