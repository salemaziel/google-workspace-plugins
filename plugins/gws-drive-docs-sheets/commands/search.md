---
name: search
description: "Search Google Drive files and folders by name, type, or full-text with gws CLI"
---

Search Google Drive assets matching the given query or criteria.

## Usage
- `/search <query>`
- `/search "type:folder <name>"`
- `/search "mimeType:spreadsheet <name>"`

## Workflow
1. Parse query argument from `$*` or interactive prompt.
2. Execute Drive search:
   ```bash
   gws drive +search "$*"
   ```
3. If specific file types are requested, filter via query terms (e.g. `mimeType = 'application/vnd.google-apps.document'`).
4. Output structured table of results:
   - File Name
   - File ID
   - MIME Type / Category
   - Last Modified Date
   - Web View Link
