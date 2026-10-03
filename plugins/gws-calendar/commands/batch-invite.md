---
name: batch-invite
description: "Add a list of attendees to an existing Google Calendar event via gws recipe"
---

# /batch-invite — Batch Invite Attendees

Add multiple colleagues or guests to an existing calendar event in one step.

## Usage
- `/batch-invite <eventId> --attendees "a@co.com,b@co.com,c@co.com"`
- `/batch-invite "All Hands" --attendees "contractor@partner.com"`

## Execution Steps
1. Parse event identifier and attendee emails from `{{args}}`.
2. Preview updated attendee list with user.
3. Execute batch invite recipe:
   ```bash
   gws recipe run batch-invite-to-event --params '{"eventId": "<id>", "attendees": ["<email1>", "<email2>"]}'
   ```
4. Confirm invitations sent.
