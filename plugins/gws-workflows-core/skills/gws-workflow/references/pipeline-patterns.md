# Cross-Service Workflow Pipelines Reference

Patterns for chaining Google Workspace CLI operations into automated pipelines.

## Pipeline 1: Meeting Prep (`+meeting-prep`)
1. **Fetch Upcoming Event**: Query Google Calendar for next meeting:
   ```bash
   gws calendar events list --params '{"calendarId": "primary", "timeMin": "...", "maxResults": 1, "singleEvents": true, "orderBy": "startTime"}'
   ```
2. **Retrieve Context Documents**: Extract document attachments from event description or search Drive for attendee names.
3. **Inspect Attendee Profiles**: Look up attendees via `gws people people get` or `searchDirectoryPeople`.
4. **Render Briefing**: Populate `templates/meeting-prep.md`.

## Pipeline 2: Standup Report (`+standup-report`)
1. **Query Day's Meetings**: `gws calendar +agenda`
2. **Query Open Tasks**: `gws tasks tasks list --params '{"tasklist": "@default"}'`
3. **Synthesize**: Format into `templates/standup-report.md`.

## Pipeline 3: File Announcement (`+file-announce`)
1. **Verify Drive File**: `gws drive files get --params '{"fileId": "<id>", "fields": "name,webViewLink"}'`
2. **Post to Space**: `gws chat +send --space <spaceId> --message "Shared new asset: ..."`
