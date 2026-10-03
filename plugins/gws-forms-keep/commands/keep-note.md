---
name: keep-note
description: "Create a note or checklist in Google Keep"
---

Create a new plain text or checklist note in Google Keep.

## Usage
- `/keep-note "<title>" --text "<content>"`

## Workflow
1. Parse note title and body text from arguments.
2. Create note via `gws`:
   ```bash
   gws keep notes create --json '{"title": "<title>", "body": {"text": {"text": "<content>"}}}'
   ```
3. Confirm note creation and display Note ID and preview.
