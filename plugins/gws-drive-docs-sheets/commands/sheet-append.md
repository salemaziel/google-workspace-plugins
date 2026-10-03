---
name: sheet-append
description: "Append a row or multiple rows of values to a Google Sheet"
---

Append rows of data to a spreadsheet.

## Usage
- `/sheet-append <spreadsheetId> --values "val1,val2,val3"`
- `/sheet-append <spreadsheetId> --json-values '[["row1_col1","row1_col2"],["row2_col1","row2_col2"]]'`

## Workflow
1. Parse spreadsheet ID and values from arguments.
2. If `--json-values` is provided:
   ```bash
   gws sheets +append --spreadsheet <spreadsheetId> --json-values '<json-array>'
   ```
3. If `--values` is provided:
   ```bash
   gws sheets +append --spreadsheet <spreadsheetId> --values "<comma-separated-values>"
   ```
4. Confirm number of appended rows and provide spreadsheet link.
