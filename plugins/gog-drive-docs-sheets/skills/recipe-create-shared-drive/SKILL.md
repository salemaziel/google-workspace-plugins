---
name: recipe-create-shared-drive
description: "Create a Google Shared Drive and add team members with appropriate roles using either gog or gws CLI."
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

# Create and Configure a Shared Drive

Create a Google Shared Drive and add team members with appropriate roles using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. List existing shared drives
gog drive drives --json

# 2. Grant permissions on shared drive root
gog drive share <DRIVE_ID> --email "eng-leads@company.com" --role writer --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create shared drive via Discovery API
gws drive drives create \
  --params '{"requestId": "drive-uuid-2026"}' \
  --json '{"name": "Core Engineering"}'

# 2. Add member with writer privileges
gws drive permissions create \
  --params '{"fileId": "<DRIVE_ID>", "supportsAllDrives": true}' \
  --json '{"role": "writer", "type": "user", "emailAddress": "member@company.com"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/drive_roles_check.py](scripts/drive_roles_check.py)
