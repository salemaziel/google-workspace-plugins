---
name: drive-search
description: "Search Google Drive files by name, MIME type, or keyword with gog CLI"
---

# /drive-search — Search Google Drive Files

Search files and folders on Google Drive with query filters, MIME type support, and structured link output.

## Usage
- `/drive-search "project roadmap"` — Searches files matching keyword.
- `/drive-search "type:spreadsheet"` or `/drive-search --type sheet` — Filters for spreadsheets.
- `/drive-search "type:pdf"` — Filters for PDF documents.
- `/drive-search --max 25` — Returns up to 25 matching files.

## Execution Steps
1. Parse search query from `{{args}}`:
   - Map shortcut types (e.g. `sheet` -> `mimeType = 'application/vnd.google-apps.spreadsheet'`, `doc` -> `mimeType = 'application/vnd.google-apps.document'`).
2. Run search command:
   ```bash
   gog drive search "${QUERY}" --max ${MAX:-15} --json
   ```
3. Format matching files into a structured table:
   | # | Name | Type | Modified | ID | Link |
   |---|---|---|---|---|---|
4. Provide next-step shortcuts:
   - "Type `export <ID>` to export a Doc to Markdown."
   - "Type `read <ID>` to inspect a spreadsheet."
   - "Type `share <ID>` to grant permissions."
