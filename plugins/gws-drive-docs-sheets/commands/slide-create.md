---
name: slide-create
description: "Create a new Google Slides presentation deck"
---

Create a blank presentation deck in Google Slides.

## Usage
- `/slide-create "<title>"`

## Workflow
1. Call Google Slides API via `gws`:
   ```bash
   gws slides presentations create --json '{"title": "<title>"}'
   ```
2. Parse presentation ID from response.
3. Return presentation title, ID, and clickable editing URL:
   `https://docs.google.com/presentation/d/<presentationId>/edit`
