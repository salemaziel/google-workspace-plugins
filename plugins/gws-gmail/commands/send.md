---
name: send
description: "Compose and safely send an email via gws with dry-run preview and mandatory confirmation"
---

# /send — Safe Email Composition & Sending

Compose and send email messages via `gws` with payload verification and mandatory user sign-off.

## Usage
- `/send --to "recipient@example.com" --subject "Title" --body "Message text"`
- `/send --to "team@example.com" --subject "Weekly Update" --attach ./report.pdf`

## Mandatory Execution Procedure
1. Parse parameters from `{{args}}`: To, CC, Subject, Body, Attachments.
2. Run dry-run payload verification:
   ```bash
   gws gmail +send --to "<recipient>" --subject "<subject>" --body "<body>" --dry-run
   ```
3. Display confirmation box:
   ```markdown
   ==================================================
   ⚠️ GMAIL SENDING VERIFICATION REQUIRED
   ==================================================
   To:          recipient@example.com
   Subject:     Project Deliverable
   Attachments: None / file.pdf
   Body Preview:
   --------------------------------------------------
   [Body Text Here]
   --------------------------------------------------
   ==================================================
   ```
4. Require explicit user confirmation ("yes", "send", "confirm").
5. Upon confirmation, execute:
   ```bash
   gws gmail +send --to "<recipient>" --subject "<subject>" --body "<body>"
   ```
6. Return delivery confirmation and message ID.
