---
name: sheets-write
description: "Write or append tabular data into Google Sheets with confirmation using gog CLI"
---

# /sheets-write — Write or Append Spreadsheet Data

Update cell ranges or append new rows to Google Sheets with mandatory preview safeguards.

## Usage
- `/sheets-write <spreadsheetId> --range "Sheet1!A1" --values '[["Name","Score"],["Alice",95]]'`
- `/sheets-write <spreadsheetId> --append --range "Sheet1!A1" --values '[["2026-10-03","New Entry"]]'`

## Mandatory Execution Procedure
1. Parse spreadsheet ID, target range, mode (`write` vs `append`), and values from `{{args}}`.
2. Display data modification preview:
   ```markdown
   ==================================================
   ⚠️ SPREADSHEET WRITE CONFIRMATION REQUIRED
   ==================================================
   Spreadsheet ID: 1a2b3c...
   Target Range:   Sheet1!A1:B2
   Operation:      Write (Overwrites cells in range)
   Values Preview:
   | Column 1 | Column 2 |
   | Alice    | 95       |
   ==================================================
   ```
3. Require explicit confirmation ("yes", "confirm") from the user.
4. Execute command:
   ```bash
   gog sheets write <spreadsheetId> --range "<range>" --values '<jsonArray>'
   ```
5. Report updated cells and status.
