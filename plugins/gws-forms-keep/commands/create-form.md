---
name: create-form
description: "Create a Google Form for surveys, onboarding, or feedback"
---

Provision a new Google Form and retrieve public responder and editor URLs.

## Usage
- `/create-form "<title>"`
- `/create-form "<title>" --doc-title "<documentTitle>"`

## Workflow
1. Parse title and document title from arguments.
2. Call Forms API via `gws`:
   ```bash
   gws forms forms create --json '{"info": {"title": "<title>", "documentTitle": "${DOC_TITLE:-<title>}"}}'
   ```
3. Extract:
   - Form ID
   - `responderUri` (public link for participants)
   - Edit URL for form administrators
4. Return both links with next steps for adding question items.
