---
name: recipe-bulk-download-folder
description: "List and download all files from a Google Drive folder using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Bulk Download Drive Folder

List and download all files from a Google Drive folder using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. List all files residing in target folder
gog drive ls --parent <FOLDER_ID> --json

# 2. Download specific file to local path
gog drive download <FILE_ID> --out "./downloads/file.ext"
```

### Option B: Using `gws` CLI
```bash
# 1. List files in folder
gws drive files list --params '{"q": "'''<FOLDER_ID>''' in parents"}' --format json

# 2. Download binary media
gws drive files get --params '{"fileId": "<FILE_ID>", "alt": "media"}' -o filename.ext

# 3. Export Docs/Sheets to PDF
gws drive files export --params '{"fileId": "<FILE_ID>", "mimeType": "application/pdf"}' -o doc.pdf
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/bulk_downloader.py](scripts/bulk_downloader.py)
