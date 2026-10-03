# Google Suite CLI — Calendar (`gog-calendar`)

Google Calendar scheduling, agenda inspection, free/busy slot queries, and conflict-free meeting creation with the gog CLI.

## Installation

### Claude Code
```bash
claude plugin install gog-calendar --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gog-calendar@google-workspace-plugins
```

## Included Components
- **Commands**:
  - `/calendar-agenda` — View daily or weekly agenda.
  - `/calendar-create` — Schedule a calendar event with confirmation safeguards.
  - `/calendar-freebusy` — Find open meeting slots across team members.
  - `/calendar-cancel` — Delete an event with verification preview.
- **Agents**:
  - `schedule-coordinator` — Autonomous calendar & meeting coordination agent.
- **Skills**:
  - `gog-calendar` — Heuristics, agenda formatting templates, and availability algorithms.

## License
MIT
