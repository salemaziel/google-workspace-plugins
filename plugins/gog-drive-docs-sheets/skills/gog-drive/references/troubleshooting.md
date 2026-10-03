# Google Drive Troubleshooting Guide

Common error codes and resolutions when executing Drive operations with `gog drive`.

## 1. 404 File Not Found (`notFound`)
- **Cause**: The specified `<fileId>` does not exist or was deleted.
- **Resolution**:
  - Run `gog drive search "<filename>"` to locate the active ID.
  - Verify that the authenticated account has access to the file.
  - Check if the file is in the Trash: `trashed = true`.

## 2. 403 Forbidden / Insufficient Permissions
- **Cause**: The account lacks permissions for the target file or parent folder.
- **Resolution**:
  - Check active account: `gog auth list` or inspect `$GOG_ACCOUNT`.
  - For uploads: ensure write permission on the target `--folder <folderId>`.
  - For sharing: only file owners or editors with sharing rights can grant access.

## 3. Invalid Query Syntax (`invalidParameter`)
- **Cause**: Drive query string has syntax errors (e.g. unescaped single quotes, misspelled field names).
- **Resolution**:
  - String literals must be enclosed in single quotes `'...'`.
  - Field names are case-sensitive (`mimeType`, not `mimetype`).
  - Dates must follow RFC 3339 format: `'YYYY-MM-DDTHH:MM:SS'`.

## 4. File Upload Failure / File Size Limits
- **Cause**: File does not exist locally or exceeds Drive API limits.
- **Resolution**:
  - Verify local file path: `test -f <path>`.
  - Standard files have a 5 TB limit per single file on Google Drive.
