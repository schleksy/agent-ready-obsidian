# Build workflow

An optional module for users who build apps, sites, tools, or other substantial deliverables with agents. Once adopted for a project, its gates apply to every phase. Users with no build workflow do not need product folders or software tools.

## Start with the actual subject

Search existing product, Project, Hub, and tracker notes. Ongoing product truth belongs in its Area; a finite effort belongs in Projects; unapproved possibilities belong in Incubator. Do not invent a product Area just to hold the trackers.

For a multi-note build, establish a governing Hub and link it from the correct parent. Seed a Request Log and Build Plan from templates and connect both to the Hub.

## Request Log

Record each incoming user message when it arrives, before beginning the dependent work. Give rows stable IDs so later decisions and plan items can refer to them. Preserve exact wording, including typos, in a quote column and use a separate Notes column for clarification, evidence, and outcomes. If one message contains several requests, keep the full original and use traceable subrows or clearly enumerated acceptance items.

Never remove a request row. Keep reversals and link the successor. Questions, decisions, and feedback remain visible even when they do not require code. User messages containing secrets must be redacted at the sensitive span; never preserve credentials for the sake of literal quotation. Keep the record in the user's chosen project context and follow their access rules.

| Status | Meaning |
| --- | --- |
| `done` | Implemented and verified against its acceptance criteria |
| `partial` | Some criteria met; remaining criteria named |
| `pending` | Not started or unfinished |
| `blocked` | A named decision, credential, access, environment, or dependency prevents the next step |
| `reversed` | Superseded by a later user decision; reason and successor preserved |

For UI behavior, `done` requires inspecting and exercising the rendered result in a browser. A green build is insufficient. For non-UI work, use evidence appropriate to the outcome. Completion does not mean publication unless publication was requested and separately verified.

Group rows by surface or work area when useful, preserving original order/time metadata. Close with truthful counts for every status and where remaining work is concentrated.

## Build Plan

Trace every plan item to a Request Log row. Put decisions requiring the user at the top so they can be addressed efficiently, then order implementation by dependencies. Fix established failures before new scope where possible. Solve shared primitives before repeating surface patches.

Record actual drift and its reason rather than pretending the original sequence was followed. A new idea is recorded and raised, not silently added to the build.

## Stress-test before code

At the planning/building boundary, inspect assumptions, dependencies, missing decisions, edge cases, vocabulary, interface seams, failure modes, reversibility, and measurable acceptance criteria. Use suitable installed engineering skills if available. Do not require a private skill collection or invent unavailable tooling.

Answer questions from the codebase and evidence first. Ask one focused question at a time when a consequential answer is genuinely missing, with a recommended choice and tradeoff. Record durable decisions and definitions where the next agent will find them. Then proceed with authorized work.

## Every-phase operating protocol

### Before the phase

Read the applicable vault rules, design decisions, voice, measurements, architecture, current implementation, and prior reversals. Identify the rules that govern this surface. If a phase intentionally reverses an adopted choice, name it and preserve the reason.

### During the phase

Use the real sources: current repository, rendered app, reference implementation, actual API contract, and measured geometry. Match existing tokens, naming, idioms, and architecture. Do not invent personal statements, testimonials, evidence, production data, or user opinions.

Do not hide a failure with swallowed errors, unexplained delays, fake data, unsupported conversions, or a superficial workaround. If an honest fix needs a decision, dependency, migration, credential, or capability, make the missing requirement explicit and continue independent work. Authorized draft copy is allowed when requested, but must not masquerade as the user's actual words or opinions.

### After the phase

Verify the real outcome. Exercise UI behavior and judge its rendered appearance; measure motion when motion is part of the requirement. Run type checks, relevant tests, and regression checks appropriate to the actual codebase. Backend, configuration, and data changes need their own evidence.

Reconcile Request Log, Build Plan, canonical state, evidence, navigation, and affected templates or workflows. Record remaining gaps. A hard build may merit an agent-authored retrospective that separates the agent's errors from user decisions and avoids invented personal judgments.

## Release boundary

Local edits, local commits, pushed commits, preview deployment, production frontend, production backend, production data, app artifact, store upload, and store release are distinct states. Never collapse them into “shipped.” Respect the user's actual authorization at each boundary and do not repeatedly ask for permission already given.

## Repeated feedback becomes a maintained lesson

When the user identifies a recurring failure, preserve the exact project feedback in its Request Log. Add only supported reusable lessons to the canonical shared guide. Update affected templates or review instructions when justified. Do not turn a single taste preference into a universal rule for all users.
