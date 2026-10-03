---
name: filter
description: "Create automated Gmail filter and label rules using gws recipe"
---

# /filter — Create Gmail Filter & Label Rule

Automatically label, star, or archive incoming emails matching criteria.

## Usage
- `/filter --from "alerts@monitoring.com" --label "Monitoring" --archive`
- `/filter --subject "Invoice" --label "Finance"`

## Execution Steps
1. Parse filter conditions from `{{args}}`: sender, recipient, subject, label name, action (star, archive, label).
2. Preview filter configuration with user.
3. Execute filter creation recipe:
   ```bash
   gws recipe run create-gmail-filter --params '{"from": "<sender>", "label": "<label>", "archive": <true|false>}'
   ```
4. Confirm filter successfully installed in Gmail.
