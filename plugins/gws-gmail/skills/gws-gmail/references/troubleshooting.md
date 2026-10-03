# gws Gmail Troubleshooting Guide

Common failure modes and fixes when interacting with Gmail via `gws`.

## 1. Authentication Required (`unauthenticated`)
- **Symptom**: `Error: credentials not found` or `token expired`.
- **Resolution**:
  - Run `gws auth login` or verify default account in `~/.config/gws/config.json`.
  - In headless setups, use `gws auth login --no-browser`.

## 2. Insufficient API Scopes
- **Symptom**: `403 Request had insufficient authentication scopes`.
- **Resolution**:
  - Verify that the Gmail API scope `https://mail.google.com/` or `https://www.googleapis.com/auth/gmail.modify` was granted during authorization.
  - Re-run `gws auth login --scopes full`.

## 3. Large Attachment Failure
- **Symptom**: Out of memory or 400 Bad Request when attaching files.
- **Resolution**:
  - Gmail API enforces a strict 25 MB limit for total MIME message size (including base64 overhead, roughly 18 MB raw file size).
  - For files exceeding 18 MB, upload the file to Google Drive and attach a sharing link instead.

## 4. Dry Run Verification
- Always execute `--dry-run` before issuing unfamiliar commands:
  ```bash
  gws gmail +send --to user@example.com --subject "Test" --body "Hello" --dry-run
  ```
