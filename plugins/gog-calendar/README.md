# Google Suite CLI — Calendar (`gog-calendar`)

Google Calendar scheduling, agenda inspection, free/busy slot queries, and conflict-free meeting creation with the `gog` CLI.

## Installation

### Claude Code
```bash
claude plugin install gog-calendar --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gog-calendar@google-workspace-plugins
```

## Architecture & Components

- **Commands** (`commands/`):
  - `/calendar-agenda` — View daily or weekly agenda.
  - `/calendar-create` — Schedule a calendar event with confirmation safeguards.
  - `/calendar-freebusy` — Find open meeting slots across team members.
  - `/calendar-cancel` — Delete an event with verification preview.
- **Agents** (`agents/`):
  - `schedule-coordinator` — Autonomous calendar & meeting coordination agent.
- **Modular Skills** (`skills/`):
  - `gog-calendar` — Progressive disclosure with `references/date-time-schemas.md`, `references/troubleshooting.md`, deterministic free-slot calculator `scripts/find_free_slots.py`, and templates (`templates/agenda-daily.md`, `templates/event-proposal.md`).
  - **Agnostic Calendar Recipes** (supports `gog` and `gws`):
    - `recipe-batch-invite-to-event` — Bulk invite attendees with notification dispatch.
    - `recipe-block-focus-time` — Native focus blocks with auto-decline and DND.
    - `recipe-create-events-from-sheet` — Ingest spreadsheet rows into calendar schedules.
    - `recipe-find-free-time` — Cross-attendee free/busy window analysis.
    - `recipe-plan-weekly-schedule` — 7-day agenda audit and deep-work slot protection.
    - `recipe-reschedule-meeting` — Move events safely with participant notification modes.
    - `recipe-schedule-recurring-event` — RFC 5545 RRULE recurring meetings with Google Meet.
    - `recipe-share-event-materials` — Grant Drive file permissions to all meeting attendees.

## License
MIT
