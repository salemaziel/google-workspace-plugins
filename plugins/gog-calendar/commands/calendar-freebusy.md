---
name: calendar-freebusy
description: "Find free meeting windows across team members using gog CLI"
---

# /calendar-freebusy — Query Availability & Meeting Windows

Search mutual open slots across one or more colleagues over a specified multi-day window.

## Usage
- `/calendar-freebusy --emails "alice@example.com,bob@example.com"`
- `/calendar-freebusy --emails "partner@client.com" --days 5`
- `/calendar-freebusy "find time with Alex this week"`

## Execution Steps
1. Parse email addresses and search horizon from `{{args}}` (default: 3 days).
2. Query free/busy status via `gog`:
   ```bash
   gog calendar freebusy --emails "<comma-separated-emails>" --days ${DAYS:-3}
   ```
3. Filter open periods against standard business hours (09:00 to 17:00).
4. Identify 3 optimal meeting slots with appropriate buffer time.
5. Format recommendation:
   - **Option 1**: [Date], [Start Time] - [End Time]
   - **Option 2**: [Date], [Start Time] - [End Time]
   - **Option 3**: [Date], [Start Time] - [End Time]
6. Prompt user: "Would you like to book one of these options using `/calendar-create`?"
