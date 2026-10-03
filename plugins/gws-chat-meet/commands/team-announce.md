---
name: team-announce
description: "Broadcast an announcement across both Google Chat and Gmail distribution lists"
---

Distribute critical team announcements across Chat spaces and email lists simultaneously.

## Usage
- `/team-announce "<headline>" --details "<message>" --space "<spaceId>" --to "<email>"`

## Workflow
1. Parse headline, message body, target space, and email recipients.
2. Confirm the broadcast payload with the user.
3. Post to Google Chat space:
   ```bash
   gws chat +send --space "<spaceId>" --text "📢 **<headline>**\n\n<details>"
   ```
4. If `--to` is provided, dispatch email:
   ```bash
   gws gmail +send --to "<email>" --subject "[Announcement] <headline>" --body "<details>"
   ```
5. Confirm broadcast across both channels.
