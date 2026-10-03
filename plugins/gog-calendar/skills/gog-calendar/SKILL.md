---
name: gog-calendar
description: Review calendar agenda, find available meeting slots, and schedule events. Displays today's or week's schedule, suggests meeting times based on availability, creates calendar events with explicit user confirmation. Use when user mentions calendar, schedule, meetings, or availability. Never creates or modifies events without confirmation.
compatibility: Requires gog CLI tool with calendar access
metadata:
  author: gog-skills
  version: "1.1"
allowed-tools: Bash(gog:*) Read
---

# Calendar & Scheduling Assistant

Inspect upcoming agendas, query free/busy intervals, and schedule meetings safely using the `gog` CLI.

> [!NOTE]
> This skill **never** creates or modifies calendar events without explicit user confirmation ("yes, create").

## Workflow

### 1. Review Agenda
- **Today's Schedule**:
  ```bash
  gog calendar events --today --json
  ```
  Present using [Daily Agenda Template](templates/agenda-daily.md).
- **Week Schedule**:
  ```bash
  gog calendar events --from "$(date +%Y-%m-%d)" --to "$(date -d '+7 days' +%Y-%m-%d 2>/dev/null || date -v+7d +%Y-%m-%d)" --json
  ```

### 2. Query Free/Busy Slots
Check busy intervals across target dates:
```bash
gog calendar freebusy primary --from "<START_RFC3339>" --to "<END_RFC3339>" --json | python3 "$(dirname "$0")/scripts/find_free_slots.py" --duration 30
```
See [Date & Time Schemas](references/date-time-schemas.md) for RFC 3339 and timezone details.

### 3. Propose and Create Event
1. Present event proposal using [Event Proposal Template](templates/event-proposal.md).
2. Check for conflicts and ask for user confirmation.
3. Upon confirmation, execute event creation:
   ```bash
   gog calendar create primary \
     --summary "<Title>" \
     --from "<START_RFC3339>" \
     --to "<END_RFC3339>" \
     --attendees "<emails>" \
     --with-meet \
     --json
   ```

## Resources
- **Date & Time Formats**: [references/date-time-schemas.md](references/date-time-schemas.md)
- **Troubleshooting & Conflicts**: [references/troubleshooting.md](references/troubleshooting.md)
- **Free Slot Calculator**: [scripts/find_free_slots.py](scripts/find_free_slots.py)
- **Templates**:
  - [Daily Agenda](templates/agenda-daily.md)
  - [Event Proposal](templates/event-proposal.md)
