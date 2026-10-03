---
name: gog-drive
description: "Manage Google Drive files, search directories, upload assets, download files, and manage sharing permissions with gog CLI. Use when searching Drive, sharing links, or uploading files using gog."
---

# gog-drive — Google Drive Management with gog CLI

Automate Google Drive file search, folder management, uploads, downloads, and access permissions using the `gog` CLI.

## Quick Workflow
1. **Search/List**: Locate target files using keywords or structured queries.
2. **Transfer**: Upload local assets or download cloud files by ID.
3. **Collaborate**: Grant read/write permissions to users or groups.

## Core Commands

```bash
# Search files with JSON output
gog drive search "quarterly report" --json

# Filter search output using helper script
gog drive search "type:pdf" --json | ./scripts/drive_search_filter.py --mime-type pdf --format links

# Upload local file to a target folder
gog drive upload ./project-spec.pdf --title "Q4 Spec" --folder <folderId>

# Download file by ID
gog drive download <fileId> --out ./downloaded-spec.pdf

# Share file (roles: reader, commenter, writer)
gog drive share <fileId> --email user@example.com --role reader
```

## Safety & Best Practices
- **JSON Pipes**: Always pass `--json` to `gog drive search` in automated subagent workflows to cleanly parse `id`, `name`, and `webViewLink`.
- **Least Privilege**: Default to `--role reader` unless the user explicitly requests edit rights (`writer`).

## Progressive Disclosure & References
- **Query Syntax & MIME Types**: Read [references/query-syntax.md](references/query-syntax.md) for full-text operators, file types, and date comparisons.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for resolution of 404, 403, and invalid parameter errors.
- **Filtering Script**: Use [scripts/drive_search_filter.py](scripts/drive_search_filter.py) for filtering, tabular formatting, or markdown link generation.
- **Share Template**: Use [templates/share-notification.md](templates/share-notification.md) to draft share messages for team communication.
