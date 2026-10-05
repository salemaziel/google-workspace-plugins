# Google Workspace — Chat & Meet (`gws-chat-meet`)

Google Workspace Chat and Meet operations: space messaging, participant logs, conference creation, and team announcements via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-chat-meet --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-chat-meet@google-workspace-plugins
```

## Architecture & Components (v1.2.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-chat` (spaces and card messages)
    - References: `references/card-formatting.md`, `references/troubleshooting.md`
    - Scripts: `scripts/chat_card_builder.py` (executable Google Chat Cards v2 payload generator)
    - Templates: `templates/incident-alert.json`, `templates/standup-summary.md`
  - Additional Skills: `gws-chat-send`, `gws-meet`, `gws-workflow-file-announce`
  - Recipes: `recipe-create-meet-space`, `recipe-post-mortem-setup`, `recipe-review-meet-participants`, `recipe-send-team-announcement`
- **Commands**:
  - `/list-spaces` — Discover accessible Google Chat spaces and rooms.
  - `/send-message` — Dispatch messages and alerts to a Chat space.
  - `/create-meeting` — Provision a new Google Meet space with custom access control.
  - `/team-announce` — Broadcast announcements across Chat spaces and email lists simultaneously.
  - `/post-mortem` — Orchestrate incident retrospectives (Doc + Calendar + Chat notification).
  - `/review-participants` — Audit conference attendance and participant duration logs.
- **Agents**: `team-lead` moved to [`gws-workflows-core`](../gws-workflows-core), which installs this plugin as a dependency.

## License
MIT
