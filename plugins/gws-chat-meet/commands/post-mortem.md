---
name: post-mortem
description: "Orchestrate an incident post-mortem: creates Google Doc spec, schedules Calendar review, and notifies Chat"
---

Stand up all assets required for an incident retrospective.

## Usage
- `/post-mortem "<incident-name>" --start "<YYYY-MM-DDTHH:MM:SS>" --space "<spaceId>" --attendees "<emails>"`

## Workflow
1. Create Post-Mortem document with standard retro template:
   ```bash
   gws docs documents create --json '{"title": "Post-Mortem: <incident-name>"}'
   ```
2. Schedule review session on Google Calendar:
   ```bash
   gws calendar +insert --summary "Post-Mortem Review: <incident-name>" --start "<start-time>" --attendee "<attendees>"
   ```
3. Announce session in the incident Chat space:
   ```bash
   gws chat +send --space "<spaceId>" --text "🔍 Post-mortem scheduled for <incident-name>. Retro doc & Meet details linked on calendar invite."
   ```
4. Output all generated resource links (Doc URL, Calendar event link).
