---
name: drive-share
description: "Share Google Drive file or folder with email and permission role using gog CLI"
---

# /drive-share — Share Drive Assets

Grant reader, commenter, or writer permissions to teammates on Google Drive assets.

## Usage
- `/drive-share <fileId> --email user@example.com --role writer`
- `/drive-share <fileId> --email client@company.com --role reader`

## Execution Steps
1. Parse file ID, recipient email, and role from `{{args}}` (roles: `reader`, `commenter`, `writer`).
2. Display sharing preview:
   - Target File: `fileId`
   - Recipient: `email`
   - Permission: `role`
3. Execute share command:
   ```bash
   gog drive share <fileId> --email "<email>" --role "${ROLE:-reader}"
   ```
4. Confirm permission granted.
