---
name: sheet-read
description: "Read cell values or ranges from a Google Sheet"
---

Read and display tabular values from a Google Spreadsheet.

## Usage
- `/sheet-read <spreadsheetId>`
- `/sheet-read <spreadsheetId> --range "Sheet1!A1:D20"`

## Workflow
1. Parse spreadsheet ID and optional range (defaults to the first sheet).
2. Fetch data via `gws`:
   ```bash
   gws sheets +read <spreadsheetId> --range "${RANGE:-Sheet1!A1:Z100}"
   ```
3. Format output in an easy-to-read ASCII markdown table.
