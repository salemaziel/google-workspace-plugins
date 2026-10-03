---
name: calendar-create
description: "Schedule a calendar event with confirmation using gog CLI"
---

Schedule calendar event:
1. Verify title, start time, duration, and attendee list.
2. Check for conflicts using `gog calendar freebusy`.
3. Require confirmation, then run `gog calendar create --title "<title>" --start "<ISO8601>" --duration <duration>`.
