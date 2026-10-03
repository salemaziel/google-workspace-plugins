---
name: sanitize-prompt
description: "Sanitize user prompt using Google Model Armor safety templates"
---

Evaluate prompt text against Google Model Armor security and safety policies.

## Usage
- `/sanitize-prompt "<promptText>" --template "<templateResourceName>"`

## Workflow
1. Parse prompt text and Model Armor template resource name (`projects/.../locations/.../templates/...`).
2. Run sanitization via `gws`:
   ```bash
   gws modelarmor +sanitize-prompt --template "<template>" --text "<promptText>"
   ```
3. Report filter status:
   - PASS / BLOCKED
   - Matched filter categories (PII, hate speech, prompt injection, etc.)
   - Sanitized prompt output (if redaction applied)
