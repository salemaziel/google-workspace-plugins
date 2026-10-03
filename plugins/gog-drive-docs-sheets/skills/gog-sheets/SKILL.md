---
name: gog-sheets
description: "Read, write, create, and append Google Sheets spreadsheets using gog CLI. Use when querying tabular spreadsheet data, appending log entries, or populating spreadsheets with gog."
---

# gog-sheets — Google Sheets Automation with gog CLI

Automate reading ranges, creating workbooks, appending log records, and updating cells in Google Sheets using `gog`.

## Quick Workflow
1. **Inspect / Query**: Read existing tabular ranges into JSON for agent reasoning.
2. **Transform**: Format structured data or CSV records into 2D JSON arrays.
3. **Persist**: Safely append new rows or write explicit cell ranges.

## Core Commands

```bash
# Create a new spreadsheet
gog sheets create --title "Q3 Metrics Tracking" --json

# Read range as JSON for structured processing
gog sheets read <spreadsheetId> --range "Sheet1!A1:D20" --json

# Convert CSV to 2D JSON array
cat metrics.csv | ./scripts/csv_to_sheets_json.py > payload.json

# Append a row to the end of a sheet
gog sheets append <spreadsheetId> --range "Sheet1!A1" --values '[["2026-10-03","Deploy success","salemaziel"]]'

# Update a specific range
gog sheets write <spreadsheetId> --range "Sheet1!A1:C2" --values '[["Metric","Target","Actual"],["MRR",100000,105000]]'
```

## Safety & Data Integrity
- **Mandatory Read-Before-Write**: `gog sheets write` overwrites existing cells without undo. Always inspect the current range before writing.
- **Append for Safety**: When logging records or events, prefer `gog sheets append`.

## Progressive Disclosure & References
- **A1-Notation Guide**: See [references/a1-notation.md](references/a1-notation.md) for bounded rectangles, column ranges, and quoting rules.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for range parsing errors and payload validation.
- **CSV Converter Script**: Use [scripts/csv_to_sheets_json.py](scripts/csv_to_sheets_json.py) to format CSV/TSV into valid 2D JSON arrays.
- **Templates**: See [templates/table-schema.json](templates/table-schema.json) and [templates/metric-log.json](templates/metric-log.json) for standard layouts.
