---
type: template
status: active
updated: 2026-10-26
tags: [template]
aliases: []
hub: "[[99 System/Templates/Templates Hub]]"
---

# Capture Template

Replace all double-brace tokens in a new note; do not overwrite this template. The sample metadata below belongs on line 1 of the new note. Use the nearest real governing Hub and the date of the meaningful edit.

```yaml
---
type: capture
status: "{{APPROPRIATE_STATUS}}"
updated: "{{YYYY-MM-DD}}"
tags: []
aliases: []
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

# {{TITLE}}

## Original supplied material
{{ORIGINAL_BODY_OR_ASSET_LINK}}

## Provenance
{{SOURCE_IDENTITY_AND_FIDELITY}}

## Processing
{{ACTUAL_PROCESSING_STATE}}

## Destinations
{{CANONICAL_DESTINATION_LINKS}}

## Uncertainty
{{UNCERTAIN_PART_ONLY}}

Keep a stable capture_id on this envelope only. Do not fabricate source timestamps or IDs. Preserve immutable payloads separately when required.
