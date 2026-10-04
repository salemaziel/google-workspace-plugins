---
name: recipe-create-expense-tracker
description: "Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries using either gog or gws CLI."
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

# Create a Google Sheets Expense Tracker

Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create a new spreadsheet
gog sheets create "Expense Tracker 2026" --json

# 2. Append header row
gog sheets append <SPREADSHEET_ID> "Sheet1!A1" \
  "Date" "Category" "Description" "Amount" "Vendor" \
  --json

# 3. Append initial expense record
gog sheets append <SPREADSHEET_ID> "Sheet1!A1" \
  "2026-03-24" "Travel" "Flight to SF" "450.00" "United Airlines" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create spreadsheet file
gws drive files create \
  --json '{"name": "Expense Tracker 2026", "mimeType": "application/vnd.google-apps.spreadsheet"}'

# 2. Append header row
gws sheets +append \
  --spreadsheet <SPREADSHEET_ID> \
  --range "Sheet1" \
  --values '["Date", "Category", "Description", "Amount", "Vendor"]'

# 3. Append initial record
gws sheets +append \
  --spreadsheet <SPREADSHEET_ID> \
  --range "Sheet1" \
  --values '["2026-03-24", "Travel", "Flight to SF", "450.00", "United Airlines"]' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/expense_row_builder.py](scripts/expense_row_builder.py)
