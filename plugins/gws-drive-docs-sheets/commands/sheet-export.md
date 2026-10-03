---
name: sheet-export
description: "Export Google Sheets tabular data as CSV or JSON file for local analysis or backup"
---

Export Google Sheets data to a local file or standard output.

## Usage
- `/sheet-export <spreadsheetId>`
- `/sheet-export <spreadsheetId> --range "Sheet1!A1:E50"`
- `/sheet-export <spreadsheetId> --format csv --out ./backup.csv`

## Workflow
1. Parse spreadsheet ID, optional range, and format from arguments.
2. Read spreadsheet data using `gws`:
   ```bash
   gws sheets +read <spreadsheetId> --range "${RANGE:-Sheet1!A1:Z100}" --format "${FORMAT:-csv}"
   ```
3. If `--out <path>` is provided, write output directly to the specified destination file and verify size.
4. Output row count and summary preview.
