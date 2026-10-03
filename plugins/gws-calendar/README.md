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

## Included Components
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
- **Skills & Recipes**:
  - `gws-calendar` (core Calendar operations)
  - `gws-calendar-agenda`, `gws-calendar-insert`
  - `recipe-batch-invite-to-event`, `recipe-block-focus-time`, `recipe-create-events-from-sheet`, `recipe-find-free-time`, `recipe-plan-weekly-schedule`, `recipe-reschedule-meeting`, `recipe-schedule-recurring-event`, `recipe-share-event-materials`

## License
MIT
