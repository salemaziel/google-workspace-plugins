---
name: gog-docs
description: "Create and export Google Docs, convert markdown documents to Docs, and retrieve document text with gog CLI. Use when authoring or converting Google Docs via gog."
---

# gog-docs — Google Docs Automation with gog CLI

Create, inspect, and export Google Docs documents directly from the terminal or AI agent workflows using `gog`.

## Quick Workflow
1. **Create**: Initialize a new empty Google Doc or create from title.
2. **Export**: Convert Docs to local markdown, text, or PDF for LLM reasoning or git storage.
3. **Link**: Connect the generated Doc ID with issues, PRs, or Drive shares.

## Core Commands

```bash
# Create a new document and return metadata
gog docs create --title "Sprint 14 Retrospective" --json

# Export document to markdown (ideal for LLM context)
gog docs export <docId> --format markdown > spec.md

# Export as PDF for distribution
gog docs export <docId> --format pdf --out spec.pdf
```

## Progressive Disclosure & References
- **Export Formats**: See [references/export-formats.md](references/export-formats.md) for details on supported output formats and rendering fidelity.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for common error handling (404s, permissions).
- **Meeting Notes Template**: Use [templates/meeting-notes.md](templates/meeting-notes.md) when generating agendas and summaries.
- **Project Spec Template**: Use [templates/project-spec.md](templates/project-spec.md) for standard PRD / technical architecture docs.
