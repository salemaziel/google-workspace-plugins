---
name: create-tasklist
description: "Create a new named task list in Google Tasks"
---

Provision a new task list for a project or category.

## Usage
- `/create-tasklist "<title>"`

## Workflow
1. Parse tasklist title from arguments.
2. Insert new tasklist via `gws`:
   ```bash
   gws tasks tasklists insert --json '{"title": "<title>"}'
   ```
3. Output the generated Tasklist ID and confirmed title.
