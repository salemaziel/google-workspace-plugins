# gogcli Environment Variables Reference

Reference for controlling `gogcli` runtime behavior, active accounts, and security sandboxes.

## Core Environment Variables

| Variable | Description | Example |
|---|---|---|
| `GOG_ACCOUNT` | Default Google account email to target for commands | `export GOG_ACCOUNT="user@company.com"` |
| `GOG_ALLOWED_COMMANDS` | Restricts agent or subagent execution to an explicit allowlist | `export GOG_ALLOWED_COMMANDS="gmail search,calendar list,drive search"` |
| `GOG_HELP` | Controls help output detail level (`full` shows all commands) | `export GOG_HELP="full"` |
| `GOG_CONFIG_DIR` | Custom directory path for credentials and tokens | `export GOG_CONFIG_DIR="$HOME/.config/gog"` |
| `GOG_LOG_LEVEL` | Verbosity for debugging (`debug`, `info`, `warn`, `error`) | `export GOG_LOG_LEVEL="debug"` |

## Security Sandboxing for AI Agents

To restrict autonomous agents from taking destructive actions (such as sending emails, deleting files, or modifying calendars), set `GOG_ALLOWED_COMMANDS` in the agent execution environment:

```bash
# Read-only safe workspace for analysis agents
export GOG_ALLOWED_COMMANDS="\
gmail search,\
gmail get,\
calendar list,\
calendar freebusy,\
drive search,\
drive list,\
docs export,\
sheets read,\
tasks list"
```
Any command outside this allowlist will immediately terminate with an authorization error.
