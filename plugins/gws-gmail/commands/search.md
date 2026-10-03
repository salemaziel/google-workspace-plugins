---
name: search
description: "Search Gmail messages by query, sender, or label using gws CLI"
---

# /search — Search Gmail Messages

Search messages in Gmail with query filtering, structured output formatting, and result snippet summaries.

## Usage
- `/search "is:unread"` — Lists unread messages.
- `/search "from:billing@company.com"` — Finds messages from a specific sender.
- `/search "label:SUPPORT has:attachment"` — Searches within specific labels.
- `/search --max 25 --format table` — Renders formatted tabular output.

## Execution Steps
1. Parse search query and flags from `{{args}}` (defaults to `is:unread` with `--max 15`).
2. Run search command:
   ```bash
   gws gmail users.messages.list --params '{"q": "${QUERY:-is:unread}", "maxResults": ${MAX:-15}}' --format "${FORMAT:-table}"
   ```
   Or use the helper command:
   ```bash
   gws gmail +search "${QUERY:-is:unread}"
   ```
3. Output messages table:
   | # | Message ID | From | Subject | Date | Snippet |
   |---|---|---|---|---|---|
4. Offer immediate follow-ups:
   - "Type `/read <ID>` to inspect full body."
   - "Type `/reply <ID>` to compose a threaded reply."
