---
name: sanitize-response
description: "Sanitize model output response using Google Model Armor safety templates"
---

Evaluate and sanitize model response text against safety policies before publishing.

## Usage
- `/sanitize-response "<responseText>" --template "<templateResourceName>"`

## Workflow
1. Parse response text and Model Armor template resource name.
2. Run response sanitization:
   ```bash
   gws modelarmor +sanitize-response --template "<template>" --text "<responseText>"
   ```
3. Report filter verdict, detected categories, and sanitized output.
