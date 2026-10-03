# Google Docs Troubleshooting Guide

Common error codes and resolutions when executing Docs operations with `gog docs`.

## 1. 404 Document Not Found
- **Cause**: The `<docId>` does not exist or account lacks view permissions.
- **Resolution**:
  - Run `gog drive search "name contains '...'" --json` to find the exact document ID.
  - Verify account permissions via `gog auth list`.

## 2. Export Format Not Supported
- **Cause**: Specified `--format` is invalid.
- **Resolution**:
  - Valid formats: `markdown`, `txt`, `pdf`, `html`, `docx`.
  - For complex drawings or embedded sheets, PDF export guarantees visual preservation.

## 3. Empty Content on Export
- **Cause**: Document is empty or document body contains unsupported embedded elements.
- **Resolution**:
  - Check file metadata using `gog drive search "id = '<docId>'"` to ensure the file is indeed an `application/vnd.google-apps.document`.
