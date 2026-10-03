# Email Triage Classification Matrix & Heuristics

Reference guide for evaluating unread emails, classifying urgency and category, and recommending actionable next steps.

---

## 1. Urgency Levels

| Level | SLA / Window | Key Signals & Patterns | Examples |
|---|---|---|---|
| **`urgent`** | Immediate (< 2h) | Keywords: "urgent", "ASAP", "immediately", "emergency". From VIPs, executives, critical clients, outage alerts. Severe operational blocker. | Production outage alert, CEO approval request for today's board meeting. |
| **`high`** | Today (EOD) | Requires decision or action by end of day. Upcoming meeting in < 24h needing confirmation. Direct client inquiry. | Client demo attendee confirmation, code review blocking release. |
| **`medium`** | 2–3 Days | Standard business inquiries, non-urgent project updates, collaborative reviews. | Design feedback request for next week's sprint. |
| **`low`** | No time pressure | Automated digests, newsletters, cold marketing, informational FYIs. | Weekly industry newsletter, automated status dashboard summary. |

---

## 2. Category Taxonomy

- **`action-required`**: Explicit request or question demanding a decision, deliverable, or response.
- **`meeting`**: Meeting invitation, calendar reschedule request, or availability poll.
- **`fyi`**: Informational notice where no response is expected.
- **`newsletter`**: Periodic subscription content or broadcast update.
- **`social`**: Personal correspondence, congratulations, or team banter.
- **`spam`**: Unsolicited marketing, suspicious sender, or irrelevant promotion.

---

## 3. Recommended Actions

- **`reply`**: Compose contextual response (invoke `gog-email-draft`).
- **`reply-all`**: Compose group response when all stakeholders must remain aligned.
- **`forward`**: Delegate message to a team member or owner.
- **`create-task`**: Convert action item into to-do item (invoke `gog-tasks`).
- **`schedule-meeting`**: Propose calendar slot or confirm invite (invoke `gog-calendar`).
- **`archive`**: Mark processed and clear from inbox.
- **`block-sender`**: Filter or block recurring unwanted sender.
