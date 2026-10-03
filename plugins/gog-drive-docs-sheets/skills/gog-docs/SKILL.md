---
name: gog-docs
description: "Create and export Google Docs, convert markdown documents to Docs, and retrieve document text with gog CLI. Use when authoring or converting Google Docs via gog."
---

# gog-docs — Google Docs Automation with gog CLI

Create, inspect, and export Google Docs documents directly from the terminal or AI agent workflows.

## Prerequisites
- `gog` CLI installed and authenticated.

## Core Commands

### Create a Google Doc
```bash
# Create a new empty doc
gog docs create --title "Sprint 14 Retrospective"

# Create a doc and return JSON metadata
gog docs create --title "API Design Document" --json
```

### Export Documents
```bash
# Export as Markdown
gog docs export <docId> --format markdown > spec.md

# Export as plain text or PDF
gog docs export <docId> --format txt > notes.txt
gog docs export <docId> --format pdf --out document.pdf
```

## Best Practices
- Combine `gog docs export --format markdown` with local tools for easy documentation mining and agent analysis.
- Track document IDs after creation to link them across issues, tasks, or calendar events.
