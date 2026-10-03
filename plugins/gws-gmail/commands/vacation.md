---
name: vacation
description: "Enable or configure Gmail out-of-office vacation auto-responder using gws recipe"
---

# /vacation — Out-of-Office Vacation Responder

Configure Gmail automated vacation responder with date boundaries and custom notification messages.

## Usage
- `/vacation --enable --subject "Out of Office" --body "I will return on Monday."`
- `/vacation --disable` — Turns off vacation auto-reply immediately.

## Execution Steps
1. Parse parameters from `{{args}}`: enable/disable flag, subject line, message body, start/end dates.
2. If enabling, display vacation preview settings.
3. Execute recipe:
   ```bash
   gws recipe run create-vacation-responder --params '{"enable": true, "responseSubject": "<subject>", "responseBodyHtml": "<body>"}'
   ```
4. Confirm vacation settings applied in Gmail settings.
