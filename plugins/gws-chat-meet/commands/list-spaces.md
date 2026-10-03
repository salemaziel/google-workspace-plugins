---
name: list-spaces
description: "List accessible Google Chat spaces and rooms"
---

Discover and display Google Chat spaces with their unique IDs and display names.

## Usage
- `/list-spaces`

## Workflow
1. Query Chat API via `gws`:
   ```bash
   gws chat spaces list --format table
   ```
2. Display:
   - Space Name / Resource Name (`spaces/...`)
   - Display Name
   - Space Type (DIRECT_MESSAGE, GROUP_CHAT, SPACE)
