---
name: gws-chat
description: "Google Chat spaces, cards v2 interactive messages, direct messages, and team announcements via gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-chat — Google Chat CLI Integration

Manage spaces, post messages, render interactive Cards v2 widgets, and broadcast team announcements through the `gws` CLI.

## Quick Workflow
1. **Discover Spaces**: List available spaces via `gws chat spaces list`.
2. **Compose & Format**: Format plain text or build Cards v2 JSON payloads with `chat_card_builder.py`.
3. **Dispatch**: Send messages to spaces or direct message threads.

## Core Commands

```bash
# List joined spaces
gws chat spaces list

# Send a plain text message to a space
gws chat +send --space <spaceId> --message "Hello team!"

# Build and send an interactive Cards v2 message
./scripts/chat_card_builder.py \
  --title "Sprint 14 Deployed" \
  --subtitle "Environment: Production" \
  --kv "Deployer=salemaziel" \
  --kv "Status=Active" \
  --button "Dashboard=https://monitoring.example.com" > card.json

gws chat spaces messages create \
  --params '{"parent": "<spaceId>"}' \
  --json "$(cat card.json)"
```

## Safety & Best Practices
- **Explicit Target**: Verify `<spaceId>` before posting announcements.
- **Broadcast Mentions**: Avoid unsolicited `<users/all>` (@all) mentions unless publishing critical emergency alerts.

## Progressive Disclosure & References
- **Card Formatting**: See [references/card-formatting.md](references/card-formatting.md) for Cards v2 schemas and text markdown syntax.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for space membership and organization policy errors.
- **Card Builder Script**: Use [scripts/chat_card_builder.py](scripts/chat_card_builder.py) to construct structured JSON card payloads.
- **Templates**: See [templates/incident-alert.json](templates/incident-alert.json) and [templates/standup-summary.md](templates/standup-summary.md).
