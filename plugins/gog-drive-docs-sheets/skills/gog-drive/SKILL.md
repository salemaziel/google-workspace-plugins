---
name: gog-drive
description: "Manage Google Drive files, search directories, upload assets, download files, and manage sharing permissions with gog CLI. Use when searching Drive, sharing links, or uploading files using gog."
---

# gog-drive — Google Drive Management with gog CLI

Automate Google Drive file search, folder management, uploads, downloads, and access permissions using the `gog` CLI.

## Prerequisites
- `gog` CLI installed and authenticated (`gog auth add you@example.com` or `export GOG_ACCOUNT=...`).

## Core Commands

### Search and List Files
```bash
# List files in root or recent
gog drive list

# Search files by keyword or title
gog drive search "quarterly report"
gog drive search "type:pdf" --max 20 --json
```

### Upload and Download
```bash
# Upload a local file
gog drive upload ./project-spec.pdf

# Upload with specific title and target folder
gog drive upload ./data.csv --title "Q3 Sales Data" --folder <folderId>

# Download a file by ID
gog drive download <fileId> --out ./downloaded-spec.pdf
```

### Sharing and Permissions
```bash
# Share file with a user
gog drive share <fileId> --email user@example.com --role writer

# Share with view-only permission
gog drive share <fileId> --email client@example.com --role reader
```

## Best Practices
- Use `--json` to inspect structured metadata including `id`, `name`, `mimeType`, and `webViewLink`.
- Check existing files before uploading to avoid duplicate versions.
