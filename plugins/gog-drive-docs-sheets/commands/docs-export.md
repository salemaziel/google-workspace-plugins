---
name: docs-export
description: "Export Google Docs documents as Markdown, plain text, or PDF using gog CLI"
---

# /docs-export — Export Google Docs to Markdown

Convert Google Docs into structured Markdown or plain text for easy local inspection, summarization, and agent processing.

## Usage
- `/docs-export <docId>` — Exports document to stdout as Markdown.
- `/docs-export <docId> --out ./spec.md` — Saves exported Markdown directly to a local file.
- `/docs-export <docId> --format pdf` — Exports document as PDF.
- `/docs-export "Sprint 14 Notes"` — Resolves document by title first, then exports.

## Execution Steps
1. Parse document ID or title query from `{{args}}`.
   - If title provided, execute `gog drive search "name contains '<title>'"` to resolve ID.
2. Run export command:
   ```bash
   gog docs export <docId> --format "${FORMAT:-markdown}" [--out "<filePath>"]
   ```
3. Return exported text or confirm file written to disk.
4. Provide immediate options:
   - "Summarize this document?"
   - "Extract action items and tasks?"
