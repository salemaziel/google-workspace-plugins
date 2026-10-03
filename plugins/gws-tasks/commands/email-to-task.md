---
name: email-to-task
description: "Convert a Gmail message into a Google Tasks item using gws workflow"
---

Convert an incoming email message into an actionable Google Task.

## Usage
- `/email-to-task <messageId>`
- `/email-to-task <messageId> --tasklist <listId>`

## Workflow
1. Parse Gmail message ID and optional tasklist ID from arguments.
2. Execute the cross-service conversion command:
   ```bash
   gws workflow +email-to-task --message-id "<messageId>" --tasklist "${TASKLIST:-@default}"
   ```
3. Display the newly created task title (derived from email subject) and confirm the linked note.
