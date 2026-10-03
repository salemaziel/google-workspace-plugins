---
name: gws-drive
description: "Google Drive, Docs, Sheets, and Slides management, file tree inspection, permissions, and upload/download via gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-drive — Google Drive CLI Integration

Manage files, folders, shared drives, permissions, and content export across Google Workspace using the `gws` CLI.

## Quick Workflow
1. **Search & Hierarchy**: Query files or map the directory hierarchy with `drive_folder_tree.py`.
2. **Transfer**: Upload local assets with `+upload` or export Docs/Sheets to local formats.
3. **Collaborate & Mutate**: Manage permissions or perform structural updates via `batchUpdate`.

## Core Commands

```bash
# Upload a file with automatic metadata
gws drive +upload --file ./report.pdf --name "Q3 Report"

# Search files in Drive
gws drive files list --params '{"q": "name contains '\''Report'\'' and trashed = false"}'

# Visualize directory hierarchy using helper script
gws drive files list --params '{"q": "trashed = false", "fields": "files(id, name, mimeType, parents)"}' | ./scripts/drive_folder_tree.py

# Export a Google Doc to markdown or plain text
gws drive files export --params '{"fileId": "<docId>", "mimeType": "text/plain"}'

# Share a file with a teammate
gws drive permissions create --params '{"fileId": "<fileId>"}' --json '{"role": "reader", "type": "user", "emailAddress": "colleague@example.com"}'
```

## Safety & Best Practices
- **Shared Drives**: Include `supportsAllDrives: true` and `includeItemsFromAllDrives: true` when accessing shared team drives.
- **Export Limits**: `files.export` has a 10 MB output payload limit. Use PDF export for large documents.

## Progressive Disclosure & References
- **Batch Update Schemas**: See [references/batch-update-schemas.md](references/batch-update-schemas.md) for structural modifications in Docs and Slides.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for export limits, field queries, and shared drive permissions.
- **Folder Tree Visualizer**: Run [scripts/drive_folder_tree.py](scripts/drive_folder_tree.py) to render an ASCII hierarchy of Drive folders.
- **Templates**: See [templates/project-spec.md](templates/project-spec.md) and [templates/slide-deck.md](templates/slide-deck.md).
