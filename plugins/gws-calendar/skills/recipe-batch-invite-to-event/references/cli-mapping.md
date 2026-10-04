# Batch Invite CLI Comparison & Reference

### CLI Syntax Matrix
| Feature | `gog` CLI | `gws` CLI |
| :--- | :--- | :--- |
| **Inspect Event** | `gog calendar event <calId> <eventId>` | `gws calendar events get --params '{"calendarId": "...", "eventId": "..."}'` |
| **Append Attendees** | `--add-attendee "user1@corp.com,user2@corp.com"` | Patch JSON `attendees` array |
| **Send Updates** | `--send-updates all` | `--params '{"sendUpdates": "all"}'` |
| **Output Format** | `--json` or TSV | `--format json` or `--format table` |

### Error Recovery
- **404 Not Found**: Verify event ID exists on primary or specified calendar.
- **403 Forbidden**: Ensure user credentials possess write ACL permissions.
- **Invalid Email**: Ensure domain syntax passes standard RFC 5322 validation.
