---
name: upload
description: "Upload local files or assets to Google Drive with automatic MIME detection and destination folder support"
---

Upload local files to Google Drive.

## Usage
- `/upload <local-filepath>`
- `/upload <local-filepath> --folder <folder-id>`

## Workflow
1. Verify local file path existence and read permissions:
   ```bash
   test -f "<filepath>" || { echo "File not found: <filepath>"; exit 1; }
   ```
2. Upload file via `gws`:
   ```bash
   gws drive +upload "<filepath>"
   ```
   If a destination folder is specified, use Drive API files create or move:
   ```bash
   gws drive files create --json '{"name": "<filename>", "parents": ["<folder-id>"]}'
   ```
3. Return:
   - Upload status
   - Drive File ID
   - Direct web view URL
