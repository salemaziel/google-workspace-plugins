---
name: send-message
description: "Send a message or alert to a Google Chat space"
---

Send plain text or structured messages to a Google Chat space.

## Usage
- `/send-message "<message>"`
- `/send-message "<message>" --space "<spaceId>"`

## Workflow
1. Parse message text and space ID (if not provided, ask or query default active space).
2. If space ID is missing, list active spaces:
   ```bash
   gws chat spaces list --format table
   ```
3. Send message via `gws`:
   ```bash
   gws chat +send --space "${SPACE_ID}" --text "<message>"
   ```
4. Confirm message delivery status and target space.
