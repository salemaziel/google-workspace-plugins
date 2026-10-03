# Email Triage Summary

📧 **Total Unread**: {{TOTAL_COUNT}} messages
⚠️  **Urgent**: {{URGENT_COUNT}} | 🔴 **High**: {{HIGH_COUNT}} | 🟡 **Medium**: {{MEDIUM_COUNT}} | 🟢 **Low**: {{LOW_COUNT}}

## Top Priorities

1. **{{PRIORITY_1_SUBJECT}}** from {{PRIORITY_1_SENDER}}
   - Urgency: {{PRIORITY_1_URGENCY}}
   - Suggested Action: {{PRIORITY_1_ACTION}}
   - Rationale: {{PRIORITY_1_RATIONALE}}

## All Messages

| ID | From | Subject | Urgency | Category | Action |
|---|---|---|---|---|---|
{{TABLE_ROWS}}

## Suggested Next Actions

- [ ] Reply to {{URGENT_COUNT}} urgent/high priority emails (IDs: {{HIGH_PRIORITY_IDS}})
- [ ] Create tasks for action items
- [ ] Archive newsletters and informational FYIs
