---
name: gog-drive
description: "Manage Google Drive files, search directories, upload assets, download files, and manage sharing permissions with gog CLI. Use when searching Drive, sharing links, or uploading files using gog."
---

# gog-drive — Google Drive Management with gog CLI

Automate Google Drive file search, folder management, uploads, downloads, and access permissions using the `gog` CLI.

## Prerequisites
- `gog` CLI installed and authenticated (`gog auth add you@example.com` or `export GOG_ACCOUNT=...`).

## Search Query Syntax & Filtering

| Query Example | Description |
|---|---|
| `name contains 'Q3 Report'` | Matches files containing phrase in filename |
| `mimeType = 'application/vnd.google-apps.document'` | Matches Google Docs |
| `mimeType = 'application/vnd.google-apps.spreadsheet'` | Matches Google Sheets |
| `mimeType = 'application/vnd.google-apps.presentation'` | Matches Google Slides |
| `mimeType = 'application/pdf'` | Matches PDF documents |
| `'me' in owners` | Files owned by the authenticated account |
| `starred = true` | Only starred files |
| `trashed = false` | Excludes deleted/trashed files |
| `modifiedTime > '2026-09-01T00:00:00'` | Modified after specified ISO 8601 date |

## Core Commands

### Search and List Files
```bash
# List files in root or recent
gog drive list

# Search files by keyword or title
gog drive search "quarterly report"

# Structured search with max results
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
# Share file with a user (role: reader, commenter, writer)
gog drive share <fileId> --email user@example.com --role writer

# Share with view-only permission
gog drive share <fileId> --email client@example.com --role reader
```

## Best Practices & Safety
- **Always use `--json`** in automated agent pipelines to inspect `id`, `name`, `mimeType`, and `webViewLink`.
- Check file existence before upload to avoid duplicate uploads.
- Never grant `writer` permissions unless explicitly instructed by the user.
