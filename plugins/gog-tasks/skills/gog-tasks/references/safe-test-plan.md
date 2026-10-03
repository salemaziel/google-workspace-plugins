# Google Tasks Safe Test Plan

Procedures for validating task workflows without corrupting user production lists.

## Test 1: Task List Discovery (Read-Only)
```bash
# Retrieve task lists in JSON format
gog tasks lists --json
```
Verify that at least one task list is returned with a valid ID string.

## Test 2: Safe Create, Query, and Delete Cycle
1. Create a transient test task:
   ```bash
   TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
   TASK_OUT=$(gog tasks add "$TASKLIST_ID" --title "[TEST] Verification Task" --notes "P3 | Admin | Self-test" --json)
   TASK_ID=$(echo "$TASK_OUT" | jq -r '.id')
   ```
2. Verify task existence:
   ```bash
   gog tasks list "$TASKLIST_ID" --json | jq --arg id "$TASK_ID" '.tasks[] | select(.id == $id)'
   ```
3. Complete or delete the task:
   ```bash
   gog tasks delete "$TASKLIST_ID" "$TASK_ID" --json
   ```

## Test 3: Daily Review Dry Run
```bash
TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
gog tasks list "$TASKLIST_ID" --json | ./scripts/task_filter.py --review
```
Confirm that tasks are correctly categorized into P0–P3 buckets without modifying remote state.
