---
name: forward
description: "Forward an email thread to new recipients with body preservation using gws CLI"
---

# /forward — Forward Email Thread

Forward a message or entire conversation to another address while preserving original sender and timestamp attribution.

## Usage
- `/forward <messageId> --to "colleague@example.com"`
- `/forward <messageId> --to "team@example.com" --note "FYI regarding recent issue"`

## Execution Steps
1. Parse message ID, recipient email, and optional introductory note from `{{args}}`.
2. Inspect original message via `gws gmail +read <messageId>`.
3. Preview forwarded message with user.
4. Execute forward command:
   ```bash
   gws gmail +forward <messageId> --to "<recipient>" [--note "<note>"]
   ```
5. Confirm delivery.
