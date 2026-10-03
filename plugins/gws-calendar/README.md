# Google Workspace — Calendar (`gws-calendar`)

Google Workspace Calendar operations: agenda inspection, Meet links, attendee invites, focus blocks, and schedule conflict resolution via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-calendar --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-calendar@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-calendar` (core Calendar operations)
    - References: `references/freebusy-discovery.md`, `references/meet-config.md`, `references/troubleshooting.md`
    - Scripts: `scripts/find_free_slots_gws.py` (executable free slot finder across attendee busy matrices)
    - Templates: `templates/event-summary.md`
  - Helper & Agenda Skills: `gws-calendar-agenda`, `gws-calendar-insert`
  - Recipe Workflows: `recipe-batch-invite-to-event`, `recipe-block-focus-time`, `recipe-create-events-from-sheet`, `recipe-find-free-time`, `recipe-plan-weekly-schedule`, `recipe-reschedule-meeting`, `recipe-schedule-recurring-event`, `recipe-share-event-materials`
- **Commands**:
  - `/get-schedule` — Query upcoming agenda across personal and team calendars.
  - `/insert-event` — Create calendar events with Google Meet links and descriptions.
  - `/clear-schedule` — Free up calendar blocks by cancelling or declining meetings.
  - `/find-free-time` — Find overlapping free slots across multiple participants.
  - `/focus-time` — Block dedicated deep work / focus time slots.
  - `/reschedule` — Move an existing event to a new slot with attendee updates.
  - `/batch-invite` — Bulk invite attendees to an existing calendar event.
- **Agents**:
  - `event-coordinator` — Autonomous meeting scheduler, focus protector, and conflict resolver.

## License
MIT
