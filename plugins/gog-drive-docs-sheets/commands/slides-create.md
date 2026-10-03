---
name: slides-create
description: "Create a new Google Slides presentation deck using gog CLI"
---

# /slides-create — Create Google Slides Presentation

Provision a new presentation slide deck and return its direct editing URL.

## Usage
- `/slides-create --title "Q4 Roadmap Presentation"`
- `/slides-create "Product Launch Review Deck"`

## Execution Steps
1. Parse presentation title from `{{args}}`.
2. Run creation command:
   ```bash
   gog slides create --title "${TITLE}" --json
   ```
3. Output presentation card:
   - **Title**: Q4 Roadmap Presentation
   - **Presentation ID**: `1s2l...`
   - **Edit Link**: `https://docs.google.com/presentation/d/1s2l.../edit`
