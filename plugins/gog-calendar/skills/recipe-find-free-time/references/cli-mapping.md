# FreeBusy Query Reference

### Timezone & RFC 3339 Requirements
Ensure all `--from` / `timeMin` and `--to` / `timeMax` timestamps include valid UTC offset or `Z` suffix.
Examples:
- `2026-03-23T09:00:00Z` (UTC)
- `2026-03-23T09:00:00-04:00` (EDT)
