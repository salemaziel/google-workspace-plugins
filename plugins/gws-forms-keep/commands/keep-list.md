---
name: keep-list
description: "List notes and checklists in Google Keep"
---

List active notes and task lists stored in Google Keep.

## Usage
- `/keep-list`
- `/keep-list --limit 20`

## Workflow
1. Parse optional page size limit.
2. Query notes via `gws`:
   ```bash
   gws keep notes list --format table
   ```
3. Display table:
   - Note ID / Name (`notes/...`)
   - Title
   - Body preview / Checklist count
   - Create Time / Update Time
