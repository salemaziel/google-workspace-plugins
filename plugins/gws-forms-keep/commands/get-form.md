---
name: get-form
description: "Inspect schema, questions, and metadata for a Google Form"
---

Retrieve metadata, question structure, and responder URLs for a specific form.

## Usage
- `/get-form <formId>`

## Workflow
1. Parse form ID from arguments.
2. Query form details via `gws`:
   ```bash
   gws forms forms get --params '{"formId": "<formId>"}' --format json
   ```
3. Display:
   - Form Title & Description
   - Public Responder URL (`responderUri`)
   - List of Question items and types
