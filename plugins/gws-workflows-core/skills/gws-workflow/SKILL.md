---
name: gws-workflow
description: "Google Workspace cross-service productivity workflows: standup summaries, meeting preparation, and weekly digests via gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-workflow — Cross-Service Productivity Pipelines

Orchestrate composite workflows spanning Google Calendar, Gmail, Google Drive, Google Tasks, and Google Chat through the `gws` CLI.

## Quick Workflow
1. **Prepare Meetings**: Execute `+meeting-prep` to fetch attendees, agendas, and linked Drive specs.
2. **Daily Standup**: Run `+standup-report` to synthesize commitments and open tasks.
3. **Weekly Synthesis**: Generate executive progress overviews with `+weekly-digest`.

## Core Commands

```bash
# Generate today's standup summary (Calendar + Tasks)
gws workflow +standup-report

# Prepare briefing for next upcoming meeting
gws workflow +meeting-prep

# Generate weekly executive digest
gws workflow +weekly-digest

# Convert email to task
gws workflow +email-to-task --message-id <msgId>

# Announce Drive file to Chat space
gws workflow +file-announce --file-id <fileId> --space <spaceId>
```

## Progressive Disclosure & References
- **Pipeline Architecture**: Read [references/pipeline-patterns.md](references/pipeline-patterns.md) for data flow across cross-service workflows.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for multi-service authentication and error handling.
- **Doctor & Diagnostic Tools**: Run `../../scripts/gws_doctor.py` to audit environment and token scopes.
- **Templates**: See `../../templates/standup-report.md`, `../../templates/meeting-prep.md`, and `../../templates/weekly-digest.md`.
