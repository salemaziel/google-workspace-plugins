---
name: recipe-share-folder-with-team
description: "Share a Google Drive folder and all its contents with collaborators using either gog or gws CLI."
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

# Share a Google Drive Folder with a Team

Share a Google Drive folder and all its contents with collaborators using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Share folder as editor
gog drive share <FOLDER_ID> --email "eng-team@company.com" --role writer --json

# 2. Share folder as viewer
gog drive share <FOLDER_ID> --email "stakeholders@company.com" --role reader --json

# 3. List active permissions
gog drive permissions <FOLDER_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Grant editor access
gws drive permissions create \
  --params '{"fileId": "<FOLDER_ID>"}' \
  --json '{"role": "writer", "type": "user", "emailAddress": "eng-team@company.com"}'

# 2. Grant viewer access
gws drive permissions create \
  --params '{"fileId": "<FOLDER_ID>"}' \
  --json '{"role": "reader", "type": "user", "emailAddress": "stakeholders@company.com"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/audit_folder_perms.py](scripts/audit_folder_perms.py)
