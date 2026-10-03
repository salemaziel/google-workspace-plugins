---
name: gog-slides
description: "Create and manage Google Slides presentations using gog CLI. Use when generating slide decks, pitch presentations, or executive briefings via gog."
---

# gog-slides — Google Slides Automation with gog CLI

Automate slide deck creation, presentation management, and template generation using `gog`.

## Quick Workflow
1. **Scaffold**: Create presentation shells with titles and capture JSON identifiers.
2. **Structure**: Plan narrative arc using standardized deck outlines.
3. **Distribute**: Share deck links with collaborators or stakeholders.

## Core Commands

```bash
# Create a new presentation
gog slides create --title "Q4 Roadmap Review"

# Create and retrieve JSON presentation structure
gog slides create --title "Product Demo Deck" --json

# Distribute to viewers
gog drive share <presentationId> --email team@example.com --role reader
```

## Progressive Disclosure & References
- **Presentation Guidelines**: See [references/presentation-guidelines.md](references/presentation-guidelines.md) for executive briefing and pitch deck archetypes.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for parameter handling and authentication scope verification.
- **Pitch Deck Outline**: Use [templates/pitch-deck-outline.md](templates/pitch-deck-outline.md) for standard 10-slide narrative structuring.
- **Executive Briefing Outline**: Use [templates/executive-briefing.md](templates/executive-briefing.md) for concise status decks.
