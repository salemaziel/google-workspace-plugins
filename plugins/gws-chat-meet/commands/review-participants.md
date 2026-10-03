---
name: review-participants
description: "Review attendance and duration logs for a completed Google Meet conference"
---

Audit who attended a Google Meet conference session and for what duration.

## Usage
- `/review-participants <conferenceRecordId>`

## Workflow
1. Parse conference record ID from arguments.
2. Query participant logs via `gws meet`:
   ```bash
   gws meet conferenceRecords participants list --params '{"parent": "conferenceRecords/<conferenceRecordId>"}' --format table
   ```
3. Format output:
   - Participant display name / email
   - Earliest join time
   - Latest leave time
   - Total active duration
