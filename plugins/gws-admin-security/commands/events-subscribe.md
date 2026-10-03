---
name: events-subscribe
description: "Subscribe to real-time Google Workspace events and stream updates as NDJSON"
---

Listen to real-time domain event streams (e.g. Drive, Chat, Calendar updates).

## Usage
- `/events-subscribe --topic "<pubsubTopic>" --types "<eventTypes>"`

## Workflow
1. Parse Cloud Pub/Sub topic and event types.
2. Initialize subscription via `gws`:
   ```bash
   gws events-subscribe --topic "<pubsubTopic>" --event-types "<eventTypes>"
   ```
3. Stream incoming events and parse change payloads.
