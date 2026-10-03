---
name: reply
description: "Send a threaded reply to an email message using gws CLI"
---

# /reply — Threaded Email Reply

Reply to an existing message while automatically preserving conversation headers (`In-Reply-To` and `References`).

## Usage
- `/reply <messageId> --body "Thanks, will review today."`
- `/reply <messageId> --all --body "Acknowledged by team."`

## Execution Steps
1. Parse message ID and reply body from `{{args}}`.
2. Inspect target message details via `gws gmail +read <messageId>`.
3. Preview reply:
   - Recipient(s): original sender (or all if `--all`)
   - Subject: `Re: <original_subject>`
   - Body preview
4. Await user confirmation.
5. Execute reply command:
   ```bash
   gws gmail +reply <messageId> --body "<body>"
   ```
6. Confirm delivery status.
