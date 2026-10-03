# Google Docs & Slides BatchUpdate Schema Reference

Reference for issuing structural batch updates to Docs and Slides via the `gws` CLI.

## Google Docs `batchUpdate`
Endpoint: `docs.documents.batchUpdate`

```bash
gws docs documents batchUpdate \
  --params '{"documentId": "<docId>"}' \
  --json '{
    "requests": [
      {
        "insertText": {
          "location": {"index": 1},
          "text": "Project Overview\n\n"
        }
      }
    ]
  }'
```

## Google Slides `batchUpdate`
Endpoint: `slides.presentations.batchUpdate`

```bash
gws slides presentations batchUpdate \
  --params '{"presentationId": "<presentationId>"}' \
  --json '{
    "requests": [
      {
        "createSlide": {
          "insertionIndex": 1,
          "slideLayout": {
            "predefinedLayout": "TITLE_AND_BODY"
          }
        }
      }
    ]
  }'
```

## Indexing Rules in Google Docs
- Document indices are 1-based and count characters (including newlines `\n`).
- When sending multiple update requests in a single batch, requests are applied sequentially. If inserting text changes document length, later indices must account for preceding insertions.
- For bulk append operations, consider reading the end index first via `gws docs documents get --params '{"documentId": "<docId>"}'`.
