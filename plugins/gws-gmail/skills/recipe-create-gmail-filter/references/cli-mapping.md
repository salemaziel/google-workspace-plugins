# Gmail Filter Criteria & Actions Reference

### Criteria Supported
- `from`: Sender email or pattern
- `to`: Recipient email
- `subject`: Words in subject line
- `query`: Freeform Gmail search query syntax (`has:attachment`, `larger:5M`)

### Actions Supported
- `addLabel`: Attach a label to incoming messages
- `removeLabel`: Remove label (e.g. `INBOX` to archive)
- `star`: Star matching messages
- `forward`: Forward to specified address
