---
name: sheets-read
description: "Read Google Sheets spreadsheet data into structured Markdown tables or JSON via gog CLI"
---

# /sheets-read — Read and Inspect Spreadsheet Data

Query ranges from Google Sheets and present them as formatted Markdown tables or JSON arrays.

## Usage
- `/sheets-read <spreadsheetId> --range "Sheet1!A1:D20"` — Reads range into tabular format.
- `/sheets-read <spreadsheetId> --range "A1:Z50" --format json` — Exports structured JSON.
- `/sheets-read "Q3 Sales"` — Resolves spreadsheet by title and reads the first sheet.

## Execution Steps
1. Parse spreadsheet ID and A1 range from `{{args}}` (defaults to first sheet A1:Z100 if range omitted).
2. Execute read command:
   ```bash
   gog sheets read <spreadsheetId> --range "${RANGE:-Sheet1!A1:Z100}" --json
   ```
3. Parse header row and values.
4. Render clean Markdown table:
   | Column A | Column B | Column C |
   |---|---|---|
   | Val 1 | Val 2 | Val 3 |
5. Provide data insights:
   - Total row count.
   - Null or missing value warnings.
   - Offer to update or append rows using `/sheets-write`.
