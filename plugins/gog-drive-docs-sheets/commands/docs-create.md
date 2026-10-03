---
name: docs-create
description: "Create a new Google Doc with optional title and initial content using gog CLI"
---

# /docs-create — Create New Google Document

Initialize a new Google Doc and return its direct editing URL.

## Usage
- `/docs-create --title "Engineering Spec"` — Creates empty document.
- `/docs-create --title "Meeting Minutes" --content "Initial agenda items..."` — Creates and initializes document.

## Execution Steps
1. Parse title and content from `{{args}}`.
2. Run creation command:
   ```bash
   gog docs create --title "${TITLE}" --json
   ```
3. Capture new Document ID and URL.
4. Output document card:
   - **Title**: Engineering Spec
   - **Doc ID**: `1xyz...`
   - **Edit Link**: `https://docs.google.com/document/d/1xyz.../edit`
