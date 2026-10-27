---
type: template
status: active
updated: 2026-10-26
tags: [template]
aliases: []
hub: "[[99 System/Templates/Templates Hub]]"
---

# Request Log Template

Replace all double-brace tokens in a new note; do not overwrite this template. The sample metadata below belongs on line 1 of the new note. Use the nearest real governing Hub and the date of the meaningful edit.

```yaml
---
type: request-log
status: "{{APPROPRIATE_STATUS}}"
updated: "{{YYYY-MM-DD}}"
tags: []
aliases: []
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

# {{TITLE}}

## Rules
Record messages as they arrive, quote faithfully except secret redaction, preserve stable row IDs, never delete reversals, link evidence and successors. UI `done` requires rendered verification. This record is private.

## Requests
| ID | Message date/time | Exact user request | Notes and verification | Status | Successor |
| --- | --- | --- | --- | --- | --- |

## Open decisions and blockers
{{BLOCKERS}}

## Counts and remaining concentration
{{HONEST_COUNTS}}
