# Calendar Troubleshooting & Edge Cases

Diagnostic guide for scheduling, timezones, and conflict resolution.

---

## 1. Timezone Mismatch
- **Symptom**: Scheduled meeting lands on a different hour than expected.
- **Resolution**:
  1. Determine local system timezone offset: `date +%z`.
  2. Always display both UTC and local timezone times in confirmation summaries.

## 2. No Free Slots in Requested Window
- **Symptom**: User calendar is completely booked during business hours.
- **Resolution**:
  1. Offer adjacent alternatives:
     - Extend search horizon to the following week.
     - Propose shortening duration (e.g. 45m -> 25m).
     - Identify meetings where user is optional or tentative.

## 3. Double-Booking Warning
- **Symptom**: Desired meeting time overlaps with existing busy block.
- **Resolution**:
  1. Warn the user with the exact title and time of the conflicting event.
  2. Require explicit confirmation before creating an overlapping event.
