# Google Drive Search Query Syntax Reference

This reference documents the query syntax for `gog drive search "<query>"` and Google Drive API v3.

## Standard Query Operators

| Operator | Supported Fields | Example | Description |
|---|---|---|---|
| `=` | `mimeType`, `name`, `starred`, `trashed` | `mimeType = 'application/pdf'` | Exact match equality |
| `!=` | `mimeType`, `name`, `starred`, `trashed` | `mimeType != 'application/vnd.google-apps.folder'` | Inequality |
| `contains` | `name`, `fullText` | `name contains 'Q3 Report'` | Case-insensitive substring match |
| `in` | `parents`, `owners`, `readers`, `writers` | `'me' in owners` | Collection membership test |
| `>` / `>=` | `modifiedTime`, `viewedByMeTime`, `createdTime` | `modifiedTime > '2026-09-01T00:00:00'` | Date comparison (RFC 3339 format) |
| `<` / `<=` | `modifiedTime`, `viewedByMeTime`, `createdTime` | `modifiedTime < '2026-10-01T00:00:00'` | Date comparison |
| `and` | All | `name contains 'Budget' and trashed = false` | Logical AND |
| `or` | All | `mimeType = 'application/pdf' or mimeType = 'text/plain'` | Logical OR |
| `not` | All | `not name contains 'Draft'` | Logical NOT |

## Common MIME Types

| MIME Type | Google / File Format |
|---|---|
| `application/vnd.google-apps.document` | Google Docs |
| `application/vnd.google-apps.spreadsheet` | Google Sheets |
| `application/vnd.google-apps.presentation` | Google Slides |
| `application/vnd.google-apps.folder` | Google Drive Folder |
| `application/vnd.google-apps.form` | Google Forms |
| `application/pdf` | PDF Document |
| `text/plain` | Plain Text |
| `text/csv` | CSV Spreadsheet |
| `image/png` | PNG Image |
| `image/jpeg` | JPEG Image |
| `application/zip` | Zip Archive |

## Common Query Recipes

### 1. Find Only Google Docs Owned by Me
```text
mimeType = 'application/vnd.google-apps.document' and 'me' in owners and trashed = false
```

### 2. Find Files Inside a Specific Folder
```text
'<folderId>' in parents and trashed = false
```

### 3. Find Recently Modified Spreadsheets
```text
mimeType = 'application/vnd.google-apps.spreadsheet' and modifiedTime > '2026-09-01T00:00:00' and trashed = false
```

### 4. Search Content Across Files (Full Text)
```text
fullText contains 'confidential' and trashed = false
```
