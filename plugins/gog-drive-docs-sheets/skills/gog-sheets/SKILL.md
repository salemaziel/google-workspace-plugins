---
name: gog-sheets
description: "Read, write, create, and append Google Sheets spreadsheets using gog CLI. Use when querying tabular spreadsheet data, appending log entries, or populating spreadsheets with gog."
---

# gog-sheets — Google Sheets Automation with gog CLI

Automate reading ranges, creating spreadsheets, and writing tabular data into Google Sheets.

## Prerequisites
- `gog` CLI installed and authenticated.

## Core Commands

### Create a Spreadsheet
```bash
# Create a new spreadsheet
gog sheets create --title "Q3 Metrics Tracking"
```

### Read Data
```bash
# Read specific range in table format
gog sheets read <spreadsheetId> --range "Sheet1!A1:D20"

# Read range as JSON for structured processing
gog sheets read <spreadsheetId> --range "Sheet1!A1:D20" --json
```

### Write and Append Data
```bash
# Write specific cell values
gog sheets write <spreadsheetId> --range "Sheet1!A1" --values '[["Metric","Target","Actual"],["MRR",100000,105000]]'

# Append a row
gog sheets append <spreadsheetId> --range "Sheet1!A1" --values '[["2026-10-03","Deploy success","salemaziel"]]'
```

## Best Practices
- Always use `--json` when parsing spreadsheet data in automated scripts or subagents.
- Ensure sheet name and cell coordinates match target structure before bulk writing.
