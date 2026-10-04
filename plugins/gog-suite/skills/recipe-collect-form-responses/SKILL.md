---
name: recipe-collect-form-responses
description: "Retrieve and review responses from a Google Form using either gog or gws CLI."
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

# Check Google Form Responses

Retrieve and review responses from a Google Form using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Inspect form metadata
gog forms get <FORM_ID> --json

# 2. Retrieve submitted responses
gog forms responses list <FORM_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Inspect form details
gws forms forms get --params '{"formId": "<FORM_ID>"}'

# 2. List submitted responses
gws forms forms responses list --params '{"formId": "<FORM_ID>"}' --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/summarize_responses.py](scripts/summarize_responses.py)
