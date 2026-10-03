---
name: doc-append
description: "Append structured text, notes, or section headers to an existing Google Document"
---

Append text content to the end of a Google Document body.

## Usage
- `/doc-append <documentId> "<text>"`

## Workflow
1. Validate document ID and input text.
2. Append text using the `gws docs +write` helper:
   ```bash
   gws docs +write --document <documentId> --text "<text>"
   ```
3. Confirm successful insertion and display the updated document link:
   `https://docs.google.com/document/d/<documentId>/edit`
