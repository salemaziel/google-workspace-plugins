# Google Meet Conference Configuration Reference

How to attach automated Google Meet video links when inserting calendar events via `gws calendar events insert`.

## Parameter Configuration

When creating an event with `conferenceData`, you must pass query parameter `conferenceDataVersion=1`:

```bash
gws calendar events insert \
  --params '{"calendarId": "primary", "conferenceDataVersion": 1}' \
  --json '{
    "summary": "Engineering Sync",
    "description": "Weekly technical architecture review",
    "start": {
      "dateTime": "2026-10-06T14:00:00-04:00",
      "timeZone": "America/New_York"
    },
    "end": {
      "dateTime": "2026-10-06T14:45:00-04:00",
      "timeZone": "America/New_York"
    },
    "attendees": [
      {"email": "dev1@example.com"},
      {"email": "dev2@example.com"}
    ],
    "conferenceData": {
      "createRequest": {
        "requestId": "sync-req-20261006",
        "conferenceSolutionKey": {
          "type": "hangoutsMeet"
        }
      }
    }
  }'
```

## Extracting the Meet Link
The response includes `hangoutLink`:
```json
{
  "id": "event_12345",
  "status": "confirmed",
  "htmlLink": "https://www.google.com/calendar/event?eid=...",
  "hangoutLink": "https://meet.google.com/abc-defg-hij"
}
```
Always output `hangoutLink` to the user upon confirmation.
