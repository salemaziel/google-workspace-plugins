---
name: email-send
description: "Send an email safely with gog CLI after mandatory user preview and confirmation"
---

# /email-send — Send Email with Mandatory Safeguards

Send an email or reply via the `gog` CLI. Enforces a strict two-step verification gate before invoking network send calls.

## Usage
- `/email-send --to "recipient@example.com" --subject "Title" --body "Message text"`
- `/email-send --reply-to <messageId> --body "Message text"`
- `/email-send --attach ./report.pdf`

## Mandatory Safety Procedure
1. Verify inputs from `{{args}}` or prior draft context:
   - Recipient email address(es).
   - Subject line.
   - Exact message body.
   - Attachment existence and file size.
2. Present verification panel to the user:
   ```markdown
   ==================================================
   ⚠️ EMAIL SENDING CONFIRMATION REQUIRED
   ==================================================
   To:          recipient@domain.com
   Subject:     Quarterly Review
   Attachments: ./Q3_Report.pdf (1.2 MB)
   Account:     user@company.com

   Body:
   --------------------------------------------------
   Hi Team,

   Attached is the Q3 performance report for review.
   --------------------------------------------------
   ==================================================
   ```
3. Await explicit positive confirmation:
   - Accept: "yes", "send", "confirm".
   - If user says anything else or asks for edits, abort send and return to draft state.
4. Execute send command:
   ```bash
   gog gmail send --to "<recipient>" --subject "<subject>" --body "<body>" [--attach "<file>"]
   ```
5. Confirm output delivery ID and report completion.
