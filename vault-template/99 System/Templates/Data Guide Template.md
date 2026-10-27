---
type: template
status: active
updated: 2026-10-26
tags: [template]
aliases: []
hub: "[[99 System/Templates/Templates Hub]]"
---

# Data Guide Template

Replace all double-brace tokens in a new note; do not overwrite this template. The sample metadata below belongs on line 1 of the new note. Use the nearest real governing Hub and the date of the meaningful edit.

```yaml
---
type: data-guide
status: "{{APPROPRIATE_STATUS}}"
updated: "{{YYYY-MM-DD}}"
tags: []
aliases: []
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

# {{TITLE}}

## Source and preserved asset
{{ASSET_LINK_WITH_EXTENSION}}

## Source authority and represented date
{{SOURCE_AND_SNAPSHOT_DATE}}

## Retrieval method, filters, and scope
{{METHOD}}

## Field meanings and units
{{SCHEMA}}

## Counts, missing data, and irregularities
{{COUNTS_AND_GAPS}}

## Verification and freshness
{{VERIFIED_CLAIMS_AND_DATE}}

## Related canonical interpretation
{{CANONICAL_LINK}}

Do not alter preserved bytes to conform to this format. This guide governs them.
