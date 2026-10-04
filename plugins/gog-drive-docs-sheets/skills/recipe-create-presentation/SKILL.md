---
name: recipe-create-presentation
description: "Create a new Google Slides presentation and configure access for collaborators using either gog or gws CLI."
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

# Create a Google Slides Presentation

Create a new Google Slides presentation and configure access for collaborators using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create presentation deck
gog slides create "Q2 Engineering All-Hands" --json

# 2. Share deck with team
gog drive share <PRESENTATION_ID> --email "team@company.com" --role writer --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create presentation via Discovery API
gws slides presentations create --json '{"title": "Q2 Engineering All-Hands"}'

# 2. Share presentation with team
gws drive permissions create \
  --params '{"fileId": "<PRESENTATION_ID>"}' \
  --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/deck_manifest.py](scripts/deck_manifest.py)
