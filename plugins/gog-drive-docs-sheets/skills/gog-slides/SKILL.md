---
name: gog-slides
description: "Create and manage Google Slides presentations using gog CLI. Use when generating slide decks, pitch presentations, or executive briefings via gog."
---

# gog-slides — Google Slides Automation with gog CLI

Automate slide deck creation, presentation management, and template generation using `gog`.

## Prerequisites
- `gog` CLI installed and authenticated.

## Core Commands

### Create a Presentation
```bash
# Create a new slide presentation
gog slides create --title "Q4 Roadmap Review"

# Create and retrieve JSON presentation structure
gog slides create --title "Product Demo Deck" --json
```

## Best Practices
- Combine with `gog drive share` to distribute links to teammates or stakeholders.
- Retain presentation IDs for updating slide titles and layout metadata.
