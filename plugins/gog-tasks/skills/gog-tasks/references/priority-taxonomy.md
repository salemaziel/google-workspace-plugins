# Task Priority & Category Taxonomy

Standard taxonomy for prioritizing and categorizing tasks within Google Tasks via `gog`.

## Priority Levels (P0–P3)

| Priority | Level | Action Horizon | Trigger Conditions |
|---|---|---|---|
| **P0** | Critical | Immediate / Today | Outages, hard deadlines within hours, blocking team delivery, customer escalations |
| **P1** | High | 1–3 Days | Sprint commitments, client deliverables, high impact if delayed |
| **P2** | Medium | 1–2 Weeks | Routine improvements, backlog items with moderate impact, flexible scheduling |
| **P3** | Low | Someday / Backlog | Nice-to-haves, exploratory spikes, no urgent deadline |

### Priority Inflation Prevention
- A maximum of 1–2 tasks should be designated **P0** on any given day.
- If more than 5 tasks are marked **P1**, force a trade-off re-ranking.
- Default to **P2** when priority is ambiguous and non-blocking.

## Category Classification

- **Work**: Engineering, product specs, client deliverables, team meetings.
- **Personal**: Learning, family, health, personal projects.
- **Errands**: Phone calls, purchases, off-screen chores.
- **Admin**: Invoicing, receipts, compliance, tax filings, account management.

## Metadata Encoding in Google Tasks
Because Google Tasks API does not natively store custom priority enum fields, encode metadata in the task notes or title prefix:
- **Title Prefix**: `[P1][Work] Update API rate limit documentation`
- **Notes Format**:
  ```text
  Priority: P1
  Category: Work
  SourceEmail: msg_abc123
  Due: 2026-10-05
  ---
  Description details here...
  ```
