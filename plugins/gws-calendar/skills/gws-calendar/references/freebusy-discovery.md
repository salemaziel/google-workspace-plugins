# Google Calendar Free/Busy Discovery Reference

How to query calendar availability and calculate open slots using the `gws calendar freebusy query` API method.

## API Endpoint
Method: `calendar.freebusy.query`

```bash
gws calendar freebusy query --json '{
  "timeMin": "2026-10-05T09:00:00Z",
  "timeMax": "2026-10-05T18:00:00Z",
  "timeZone": "America/New_York",
  "items": [
    {"id": "user1@company.com"},
    {"id": "user2@company.com"}
  ]
}'
```

## Response Schema
The API returns busy intervals for each queried calendar:
```json
{
  "calendars": {
    "user1@company.com": {
      "busy": [
        {
          "start": "2026-10-05T10:00:00Z",
          "end": "2026-10-05T11:00:00Z"
        }
      ]
    },
    "user2@company.com": {
      "busy": [
        {
          "start": "2026-10-05T14:30:00Z",
          "end": "2026-10-05T15:30:00Z"
        }
      ]
    }
  }
}
```

## Calculating Overlapping Availability
To compute available slots:
1. Define the search window (e.g. 09:00 to 17:00 local time).
2. Union all `busy` intervals across all attendees.
3. Compute the complement (unoccupied intervals) whose duration $\ge$ requested meeting duration.
4. Use `find_free_slots_gws.py` to automate this calculation.
