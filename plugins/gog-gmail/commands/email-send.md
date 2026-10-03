---
name: email-send
description: "Compose and safely send an email with gog CLI after user confirmation"
---

Send an email safely:
1. Confirm recipient, subject, attachments, and exact body text.
2. Require user confirmation before proceeding.
3. Once confirmed, execute `gog gmail send --to "<recipient>" --subject "<subject>" --body "<body>"`.
4. Confirm delivery status and output message ID.
