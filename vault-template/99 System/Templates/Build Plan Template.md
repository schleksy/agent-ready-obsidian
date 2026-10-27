---
type: template
status: active
updated: 2026-10-26
tags: [template]
aliases: []
hub: "[[99 System/Templates/Templates Hub]]"
---

# Build Plan Template

Replace all double-brace tokens in a new note; do not overwrite this template. The sample metadata below belongs on line 1 of the new note. Use the nearest real governing Hub and the date of the meaningful edit.

```yaml
---
type: build-plan
status: "{{APPROPRIATE_STATUS}}"
updated: "{{YYYY-MM-DD}}"
tags: []
aliases: []
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

# {{TITLE}}

## Decisions blocking dependent work
{{DECISIONS_WITH_RECOMMENDATIONS}}

## Acceptance criteria
{{CRITERIA}}

## Ordered phases
| Phase | Request Log IDs | Dependencies | Planned work | Verification | Actual status |
| --- | --- | --- | --- | --- | --- |

## Plan stress-test
{{ASSUMPTIONS_EDGE_CASES_AND_RESOLVED_QUESTIONS}}

## Drift and reasons
{{ACTUAL_CHANGES}}

## Remaining work and handoff
{{REMAINING_WORK}}
