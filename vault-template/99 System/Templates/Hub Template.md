---
type: template
status: active
updated: 2026-10-26
tags: [template]
aliases: []
hub: "[[99 System/Templates/Templates Hub]]"
---

# Hub Template

Replace all double-brace tokens in a new note; do not overwrite this template. The sample metadata below belongs on line 1 of the new note. Use the nearest real governing Hub and the date of the meaningful edit.

```yaml
---
type: hub
status: "{{APPROPRIATE_STATUS}}"
updated: "{{YYYY-MM-DD}}"
tags: []
aliases: []
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

# {{TITLE}}

## Purpose
{{PURPOSE}}

## Up
{{PARENT_HUB_LINK}}

## Rules that apply here
Inherit the root contract. Record only supported narrower rules and permissions.

## What belongs / what does not
{{BOUNDARIES}}

## Read by need
| Need | Note | Why |
| --- | --- | --- |

## Write rules
Search canonical subjects; source facts; register notes; validate parent links and dependencies.

## Sources, freshness, and limitations
{{SOURCE_AND_LIMITS}}
