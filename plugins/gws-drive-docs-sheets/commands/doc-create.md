---
name: doc-create
description: "Create a new Google Document with optional initial body text and folder placement"
---

Create a blank or pre-populated Google Document.

## Usage
- `/doc-create "<title>"`
- `/doc-create "<title>" --body "<initial text>"`

## Workflow
1. Create a blank Google Document:
   ```bash
   gws docs documents create --json '{"title": "<title>"}'
   ```
2. Extract the generated `documentId`.
3. If `--body` text is provided, append the initial content:
   ```bash
   gws docs +write --document <documentId> --text "<initial text>"
   ```
4. Output the document title, ID, and clickable URL:
   `https://docs.google.com/document/d/<documentId>/edit`
