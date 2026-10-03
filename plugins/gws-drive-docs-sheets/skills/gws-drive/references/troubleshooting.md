# Google Drive, Docs & Sheets (`gws`) Troubleshooting Guide

Common error conditions and resolutions when operating Drive assets through `gws`.

## 1. Export Limit Exceeded (`responseTooLarge`)
- **Symptom**: `403 Forbidden: The export request is too large. Exported content is limited to 10 MB.`
- **Resolution**:
  - Documents containing many high-resolution inline images exceed the 10 MB limit for `files.export`.
  - Export as `application/pdf` or download specific media assets directly from Drive.

## 2. Invalid `fields` Parameter
- **Symptom**: `400 Bad Request: Invalid field selection`.
- **Resolution**:
  - Wrap field queries properly: `--params '{"fields": "files(id, name, mimeType, webViewLink)"}'`.
  - Nested properties must match exact Google Drive API v3 field paths.

## 3. Shared Drive Access Restrictions
- **Symptom**: File not found or 404 when querying a file inside a Shared Drive.
- **Resolution**:
  - You must pass `supportsAllDrives=true` and `includeItemsFromAllDrives=true`:
    ```bash
    gws drive files list --params '{"supportsAllDrives": true, "includeItemsFromAllDrives": true, "q": "name contains '\''Spec'\''"}'
    ```
