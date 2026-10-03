---
name: gog-sheets
description: "Read, write, create, and append Google Sheets spreadsheets using gog CLI. Use when querying tabular spreadsheet data, appending log entries, or populating spreadsheets with gog."
---

# gog-sheets — Google Sheets Automation with gog CLI

Automate reading ranges, creating spreadsheets, appending log records, and updating cells in Google Sheets.

## Prerequisites
- `gog` CLI installed and authenticated.

## A1-Notation Syntax Guide

| Range Format | Target Scope |
|---|---|
| `Sheet1!A1:D10` | Specific bounded rectangular matrix |
| `Sheet1!A:D` | Entire columns A through D |
| `Sheet1!1:5` | Entire rows 1 through 5 |
| `'Financial Overview'!B2` | Single cell in a named sheet with spaces |
| `A1` | Defaults to the first tab in the spreadsheet |

## Core Commands

### Create a Spreadsheet
```bash
# Create a new spreadsheet
gog sheets create --title "Q3 Metrics Tracking" --json
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
# Write specific cell values (JSON array of row arrays)
gog sheets write <spreadsheetId> --range "Sheet1!A1" --values '[["Metric","Target","Actual"],["MRR",100000,105000]]'

# Append a row to the bottom of a sheet
gog sheets append <spreadsheetId> --range "Sheet1!A1" --values '[["2026-10-03","Deploy success","salemaziel"]]'
```

## Safety & Data Integrity
- **Mandatory Confirmation**: Writing cells (`gog sheets write`) overwrites existing data without undo. Always preview the target range and values to the user before executing.
- **Header Preservation**: Verify header row locations (typically row 1) before appending to avoid inserting records in header positions.
- **Type Handling**: Numbers, booleans, and dates should be formatted as standard JSON literals in `--values`.
