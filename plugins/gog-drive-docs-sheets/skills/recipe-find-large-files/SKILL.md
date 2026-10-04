---
name: recipe-find-large-files
description: "Identify large Google Drive files consuming storage quota using either gog or gws CLI."
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

# Find Largest Files in Google Drive

Identify large Google Drive files consuming storage quota using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Search files sorted by storage quota used
gog drive ls --order-by "quotaBytesUsed desc" --page-size 20 --json

# 2. Or run directory disk usage analysis
gog drive du --json
```

### Option B: Using `gws` CLI
```bash
# 1. Query files ordered by quota bytes
gws drive files list \
  --params '{"orderBy": "quotaBytesUsed desc", "pageSize": 20, "fields": "files(id,name,size,mimeType,owners)"}' \
  --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/format_bytes.py](scripts/format_bytes.py)
