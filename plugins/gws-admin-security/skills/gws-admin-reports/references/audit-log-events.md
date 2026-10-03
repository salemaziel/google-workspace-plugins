# Google Workspace Admin SDK Audit Log Events Reference

Reference for filtering activities via `gws admin-reports activities list`.

## Common `applicationName` Filters

| Application | Description | Monitored Threat Vectors |
|---|---|---|
| `admin` | Admin Console actions | User creation, role assignments, password resets |
| `login` | Authentication events | Failed passwords, 2SV challenges, suspicious logins |
| `drive` | Drive access & modifications | External file sharing, public link generation, downloads |
| `token` | Third-party OAuth grants | Unauthorized third-party apps, excessive scope permissions |
| `rules` | DLP & Rule matches | Data loss prevention policy triggers |

## Querying Activities via `gws`

```bash
# Query recent login events
gws admin-reports activities list \
  --params '{"userKey": "all", "applicationName": "login", "maxResults": 20}'

# Query Admin privilege modifications
gws admin-reports activities list \
  --params '{"userKey": "all", "applicationName": "admin", "eventName": "ASSIGN_ROLE"}'

# Query external sharing events on Google Drive
gws admin-reports activities list \
  --params '{"userKey": "all", "applicationName": "drive", "eventName": "change_user_access"}'
```
