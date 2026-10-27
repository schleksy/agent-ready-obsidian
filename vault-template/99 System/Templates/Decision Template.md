---
type: template
status: active
updated: 2026-10-26
tags: [template]
aliases: []
hub: "[[99 System/Templates/Templates Hub]]"
---

# Decision Template

Replace all double-brace tokens in a new note; do not overwrite this template. The sample metadata below belongs on line 1 of the new note. Use the nearest real governing Hub and the date of the meaningful edit.

```yaml
---
type: decision
status: "{{APPROPRIATE_STATUS}}"
updated: "{{YYYY-MM-DD}}"
tags: []
aliases: []
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

# {{TITLE}}

## Decision
{{ADOPTED_DECISION_OR_PROPOSAL_LABEL}}

## Authority, scope, and statement date
{{AUTHORITY_SCOPE_DATE}}

## Why
{{REASON}}

## Alternatives and evidence
{{ALTERNATIVES_AND_EVIDENCE}}

## Effective date and implementation evidence
{{EFFECTIVE_DATE_OR_UNKNOWN}}

## Supersedes / superseded by
{{PRECISE_SUPERSESSION}}

## Review condition
{{REVIEW_CONDITION}}
