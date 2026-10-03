# Calendar Date & Time Formats and Schemas

Standards for timezone handling, RFC 3339 timestamps, and date-range calculations with `gog calendar`.

---

## 1. RFC 3339 Timestamps

The `gog calendar` commands require absolute RFC 3339 formatted timestamps:
- Format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS-07:00`
- Example: `2026-10-05T14:00:00Z`

## 2. Calculating Start and End Times
- When scheduling meetings, `--from` specifies the start time and `--to` specifies the end time:
  ```bash
  START="2026-10-05T14:00:00Z"
  END="2026-10-05T15:00:00Z"  # 1 hour duration
  gog calendar create primary --summary "Title" --from "$START" --to "$END" --with-meet
  ```

## 3. FreeBusy Query Range
- When checking availability across multiple days:
  ```bash
  gog calendar freebusy primary \
    --from "2026-10-05T00:00:00Z" \
    --to "2026-10-09T23:59:59Z" \
    --json
  ```
