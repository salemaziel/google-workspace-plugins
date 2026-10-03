# Google Calendar Troubleshooting Guide

Common error conditions and resolutions when operating Google Calendar through `gws`.

## 1. Invalid Time Format (`badRequest`)
- **Cause**: The `start.dateTime` or `end.dateTime` is not in RFC 3339 format.
- **Resolution**:
  - Always include explicit UTC offset or timezone designation:
    `2026-10-06T14:00:00Z` or `2026-10-06T14:00:00-04:00`.
  - Ensure `start` is strictly earlier than `end`.

## 2. Missing `conferenceDataVersion`
- **Cause**: `conferenceData` is ignored or fails with validation error.
- **Resolution**:
  - When requesting Meet generation, `--params '{"calendarId": "primary", "conferenceDataVersion": 1}'` is mandatory.

## 3. External Calendar Access Denied (`notFound` / `forbidden`)
- **Cause**: Trying to query free/busy or insert events on an external user's private calendar without domain sharing.
- **Resolution**:
  - For external attendees, insert them in the `attendees` array on your own `primary` calendar. Google Calendar will dispatch invitation emails automatically.

## 4. Conflict Warning / Accidental Overwrite
- **Resolution**: Always query existing events or execute `gws calendar freebusy query` before scheduling.
