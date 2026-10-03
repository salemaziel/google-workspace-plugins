---
name: list-groups
description: "List contact groups and labels configured in Google Contacts"
---

Display contact groups used to categorize personal contacts.

## Usage
- `/list-groups`

## Workflow
1. Query contact groups via `gws`:
   ```bash
   gws people contactGroups list --format table
   ```
2. Display:
   - Resource Name (`contactGroups/...`)
   - Group Name
   - Formatted Name
   - Member Count
