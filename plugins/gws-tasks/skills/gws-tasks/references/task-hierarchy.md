# Google Tasks Hierarchy & Structure Reference

Detailed guide to Google Tasks data structures, subtasks, and limits via the `gws` CLI.

## Object Hierarchy
1. **Tasklists**: The root container for tasks. Each user has a default `@default` tasklist.
2. **Tasks**: Top-level todo items within a tasklist.
3. **Subtasks**: Child tasks associated via `parent: "<parentTaskId>"` and sequenced using `previous: "<siblingTaskId>"`.

## Quotas & Constraints
- Maximum task lists per user: **2,000**
- Maximum non-hidden tasks per list: **20,000**
- Maximum tasks across all lists: **100,000**
- Maximum subtask nesting depth: 1 level (parent -> child)
- Maximum subtasks per task: **2,000**

## Reordering & Moving Tasks
Use `tasks.tasks.move`:
```bash
gws tasks tasks move \
  --params '{"tasklist": "<listId>", "task": "<taskId>", "parent": "<parentTaskId>", "previous": "<siblingTaskId>"}'
```
- Setting `parent` converts a task into a child subtask.
- Setting `previous` positions the task immediately below the referenced sibling.
