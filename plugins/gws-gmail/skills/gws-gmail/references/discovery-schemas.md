# Google Workspace CLI (`gws`) Schema & Discovery Guide

Guide to discovering and inspecting Gmail API v1 schemas dynamically with the `gws` CLI.

## Discovery Workflow

```bash
# 1. Browse top-level resources and methods
gws gmail --help

# 2. Inspect a specific method's request schema
gws schema gmail.users.messages.send

# 3. Inspect query/filter parameters for list endpoints
gws schema gmail.users.messages.list
```

## Constructing Method Invocations

### Using `--params` (URL Path & Query Parameters)
`--params` accepts a JSON string defining query parameters such as `userId`, `q`, `maxResults`, or `labelIds`:
```bash
gws gmail users messages list --params '{"userId": "me", "q": "is:unread is:important", "maxResults": 10}'
```

### Using `--json` (Request Body Payloads)
When calling methods that require an HTTP request body (e.g. `users.messages.send` or `users.labels.create`), supply the JSON payload via `--json`:
```bash
gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Client-Urgent", "labelListVisibility": "labelShow"}'
```

## Schema Caching & Offline Use
The `gws` CLI caches Google Discovery documents locally in `~/.config/gws/discovery/`.
If you are working offline or behind a proxy, pre-populate discovery schemas using `gws schema --sync`.
