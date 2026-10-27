# Capture workflow

This is a provider-neutral protocol, not a deployed service. No capture endpoint, importer, transcription service, account, schedule, or receipt integration is bundled.

## Choose the real mode

A full-access agent should use the governing Hubs to file known material correctly. Inbox is temporary, not an alternative to doing established routing. A capture-only agent submits a new source record and cannot browse, merge, edit, move, or delete existing notes.

Remote captures arrive in `00 Inbox/Agent Inbox/`. Do not let untrusted remote input write directly into canonical Areas, Projects, or System rules. A local authorized processor performs reconciliation.

## Capture record

A useful envelope carries a stable `capture_id`, actual capture timestamp with timezone, source type and source identity where supplied, title, original body or referenced payload, transcript status if applicable, processing state, and eventual destination links. Missing fields remain unknown. Do not fabricate a source ID or original timestamp.

Keep machine receipts and user-facing claims precise:

| State | What it establishes |
| --- | --- |
| Prepared | A payload exists locally |
| Accepted | The gateway durably saved it |
| Delivered | The importer wrote a local source record |
| Processed | Clear meanings were reconciled into canonical destinations |
| Verified | The named checks were actually performed |

A queue receipt is not proof of local delivery. A delivered record is not proof of correct filing. Do not acknowledge before durable acceptance. On failure, report the actual failure and retry state.

## Idempotency

Before importing or processing, search the entire vault, including Archive, for the exact `capture_id`. Do not create a second record for a transport retry. Preserve the identity through processing.

When processing completes, edit processing metadata on the existing envelope and move that original record into `90 Archive/Agent Inbox Processed/<Year>/`. Do not copy it into Archive while leaving an active Inbox original. After the move, confirm exactly one envelope owns that ID. Other notes should link to it rather than repeat its `capture_id` field.

Immutable source payloads retain their bytes; put processing metadata in the envelope or governing wrapper. Two distinct user messages may legitimately have different IDs and similar wording. Compare intent and content before treating them as duplicates.

## A complete inbox pass

1. List every file type in both the ordinary Inbox and Agent Inbox, including attachments and nested sources. Ignore only recognized operating-system cruft.
2. Keep permanent structural notes in place. Do not move or overwrite `Inbox.md` or `Agent Inbox.md` as though they were captures.
3. Read each unresolved capture in full, search canonical homes and IDs, and split distinct meanings for routing.
4. Route clear material, create genuinely required subject structure, register it, and preserve one original source.
5. Leave only the specifically unresolved part, with the decision needed and what was checked.
6. Re-list both inboxes before finishing. Handle arrivals or explicitly report the pass cutoff and remaining arrivals. Never call the inbox clear from one early scan.
7. Report processed, partial, unresolved, failed, and newly arrived items separately. Do not imply that an unbounded stream can stay empty forever.

## Voice and OCR are fallible sources

A `needs-review` transcript is not automatically a blocked capture. Route its clear intent and preserve the source and review status. Verify uncertain names, dates, numbers, wording, and directions against the original audio or image before relying on those details. Withhold only the uncertain content.

If transcription fails, record `failed`; do not invent text. An explicit user instruction to route without an audio review can remove that routing prerequisite, but it does not make uncertain wording a verified quote.

## Security requirements for an optional gateway

Implement only if the user requests and authorizes it. Authenticate each sender or client, validate provider signatures where applicable, enforce sender/recipient scope, and keep credentials in secure configuration. Separate capture permission from queue-delivery permission and canonical write permission. Minimize stored content, define retention and failure recovery, and use actual durable message IDs for retry deduplication.

There should be no remote delete or arbitrary vault-write endpoint merely to support capture. Test retries, malformed input, unauthorized input, importer downtime, acknowledgement ordering, ID preservation, and recovery. Verify user-facing receipts against durable storage and local delivery independently.

Store the adopted schedule in the automation system, not as duplicated execution configuration in notes. Record relevant source dates, decisions, verification dates, and audit evidence in the vault. No specific polling interval or retention period is universal.
