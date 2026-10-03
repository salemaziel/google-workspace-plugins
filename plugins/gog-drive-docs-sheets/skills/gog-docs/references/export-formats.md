# Google Docs Export Formats Reference

Reference for formats supported by `gog docs export <docId> --format <format>`.

## Supported Formats

| Format | Extension | Description | Best For |
|---|---|---|---|
| `markdown` | `.md` | Markdown text with standard headings, lists, tables | LLM ingestion, agent context, git docs |
| `txt` | `.txt` | Plain text stripped of all styling | Quick terminal inspection, simple search |
| `pdf` | `.pdf` | Adobe Portable Document Format | Archiving, printing, formal external distribution |
| `html` | `.html` | Zipped HTML document with inline image references | Web publishing, static site import |
| `docx` | `.docx` | Microsoft Word OpenXML format | Enterprise handoff, legacy tools |

## Usage Examples

```bash
# Export directly to markdown stdout
gog docs export <docId> --format markdown > documentation.md

# Export binary PDF to specified output file
gog docs export <docId> --format pdf --out release-notes.pdf
```
