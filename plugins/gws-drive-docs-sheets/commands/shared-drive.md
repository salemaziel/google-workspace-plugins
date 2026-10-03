---
name: shared-drive
description: "Provision a Google Shared Drive and manage team access permissions"
---

Create a shared drive and add initial team collaborators.

## Usage
- `/shared-drive "<drive-name>"`
- `/shared-drive "<drive-name>" --member "<email>" --role "<role>"`

## Workflow
1. Generate unique request ID and create shared drive:
   ```bash
   REQUEST_ID="drive-$(date +%s)"
   gws drive drives create --params "{\"requestId\": \"$REQUEST_ID\"}" --json "{\"name\": \"<drive-name>\"}"
   ```
2. If `--member` is provided:
   ```bash
   gws drive permissions create --params "{\"fileId\": \"<drive-id>\", \"supportsAllDrives\": true}" --json "{\"role\": \"${ROLE:-writer}\", \"type\": \"user\", \"emailAddress\": \"<email>\"}"
   ```
3. Return shared drive name, ID, and member access status.
