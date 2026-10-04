---
name: recipe-organize-drive-folder
description: "Create a Google Drive folder structure and move files into the right locations using either gog or gws CLI."
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

# Organize Files into Google Drive Folders

Create a Google Drive folder structure and move files into the right locations using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create project parent folder
gog drive mkdir "Q2 Projects" --json

# 2. Create subfolder inside parent
gog drive mkdir "Design Specs" --parent <PARENT_FOLDER_ID> --json

# 3. Move file into folder
gog drive move <FILE_ID> --parent <TARGET_FOLDER_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create folder
gws drive files create \
  --json '{"name": "Q2 Projects", "mimeType": "application/vnd.google-apps.folder"}'

# 2. Move file
gws drive files update \
  --params '{"fileId": "<FILE_ID>", "addParents": "<TARGET_FOLDER_ID>", "removeParents": "<OLD_PARENT_ID>"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/folder_tree_builder.py](scripts/folder_tree_builder.py)
