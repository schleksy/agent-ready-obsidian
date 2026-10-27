---
type: portable-guide
status: active
updated: 2026-10-26
tags:
  - ai-agent/guide
  - obsidian
  - knowledge-management
  - vault-setup
aliases:
  - Agent-Ready Obsidian Blueprint
  - Portable Obsidian Setup Guide
  - Build My Obsidian Vault
---

# Build an Agent-Ready Obsidian Vault

> This is the complete architecture and discovery guide. Read it together with [Operating contract](operating-contract.md), [Routing and maintenance](routing-and-maintenance.md), [Capture workflow](capture-workflow.md), and [Validation](validation.md). Those files define the stricter operational gates added to this blueprint. Do not install only this guide and omit them. The public starter uses `99 System/Rules/` for those canonical installed rules. Reuse equivalent stable paths in an existing vault.

> [!important] How to use this file
> Give this entire Markdown file to an AI agent and tell it where your Obsidian vault is. The agent should inspect what already exists, learn how you actually work, ask the discovery questions below, propose a personalized map, and then build the system after you approve the structure.

This is a blueprint, not a folder pack everyone must copy blindly. A founder, student, bookkeeper, creator, healthcare operator, researcher, and family will have different Areas and sources. The root system stays predictable; the contents are designed around the person.

---

## The outcome

The finished vault should work for two readers:

1. **The human** should understand where something belongs without memorizing a complicated methodology.
2. **The agent** should understand the person’s goals, reasoning, boundaries, source material, and read/write rules before acting.

The vault should become the durable context system behind task tools such as a to-do app, project manager, calendar, or coding agent.

```text
Task system     = what needs to happen
Obsidian vault  = why it matters, what is true, what was tried, and how to act
```

Do not turn Obsidian into a second task manager unless the user explicitly wants that. Projects can contain outcomes and next steps, but detailed execution may still live in the user’s preferred task tool.

---

## Why this model works

This blueprint combines a few useful ideas without forcing a pure methodology:

- **PARA contributes actionability:** Areas, Projects, Resources, and Archive answer whether something is ongoing, finishable, reusable, or inactive.
- **A dedicated Incubator protects possibilities:** ideas remain visible without pretending they are active commitments.
- **Light Johnny.Decimal numbering creates stable root order:** numbers are used for the main folders, not every note.
- **Focused-note thinking keeps context maintainable:** goals, decisions, voice, workflows, and data guides can be updated independently.
- **Obsidian links create relationships:** related information can stay with its correct owner while still being connected.
- **Properties describe type and state:** folders do not need to multiply for every status.
- **Bases provide dynamic views only when notes behave like records.**
- **Hub notes make the vault agent-readable:** every important folder explains its purpose, reading order, and writing rules.

The system is deliberately hybrid. Pure PARA has no strong home for a large idea pipeline. Full Johnny.Decimal creates too much numbering for many people. A pure link-only system can make operational state unclear. This structure keeps the useful distinctions without making the vault a hobby to maintain.

---

# Part 1: Instructions to the Setup Agent

## Non-negotiable operating rules

Before changing anything:

1. Confirm the exact vault root. A real Obsidian vault normally contains a `.obsidian` folder.
2. Inspect the existing files, folders, links, properties, attachments, and configuration read-only.
3. Make or confirm a backup before a broad migration or reorganization.
4. Do not delete, overwrite, merge, or normalize existing material without explicit approval.
5. Do not store passwords, API keys, tokens, cookies, or private authentication data in notes.
6. Preserve raw exports, original documents, timestamps, and source wording when they are evidence.
7. Treat the user’s current instruction as more authoritative than this blueprint.
8. Ask only questions that cannot be answered safely from the existing files.
9. Present the proposed personalized map before moving a large number of files.
10. Prefer a simple useful system over a theoretically perfect one.

If the user has no existing vault, create a new empty vault and continue. If the user has an existing vault, adapt it carefully rather than pretending it is blank.

---

## Discovery questions

Ask these in a short, conversational way. Do not dump twenty questions at once. Ask the first group, inspect the answers, then ask only the follow-ups that matter.

### A. What the person actually does

1. What responsibilities do you maintain continuously?
2. What active outcomes are you trying to finish?
3. What kinds of ideas do you save for later?
4. What knowledge, references, or frameworks do you reuse?
5. Which responsibilities belong to you personally, and which belong to a company, client, family, school, or team?

### B. Existing sources

6. Where does your current information live: Notion, Google Drive, Dropbox, Apple Notes, WhatsApp, email, a task manager, code repositories, or local folders?
7. Which source is authoritative for each important topic?
8. Which sources contain raw evidence such as exports, analytics, contracts, meeting transcripts, PDFs, images, or spreadsheets?
9. Are there old systems that should be imported, preserved as historical material, or left alone?

### C. How agents will use the vault

10. What should agents be allowed to read and update?
11. What should agents never publish, send, delete, or change without approval?
12. Which facts or styles are easy for agents to confuse?
13. What repeated work would benefit from a dedicated workflow or template?

### D. Devices, privacy, and maintenance

14. Which devices need the vault?
15. What sync method do you already use or prefer?
16. What is the separate backup method?
17. Does any company or client require strict separation or a different vault?
18. How much maintenance will you realistically do: daily, weekly, or rarely?

---

## Decide whether to use one vault or several

Prefer **one vault** when:

- The same person owns the contexts.
- Cross-links between personal, work, learning, and projects are useful.
- Access and confidentiality rules are compatible.
- One agent may need to reason across those contexts.

Prefer **separate vaults** when:

- Different companies or clients have strict confidentiality boundaries.
- Different teams need different access.
- A regulated environment requires separation.
- One vault will be shared while another remains private.
- Combining the material would create a real security or ownership problem.

Do not create separate vaults merely because topics are different. Folders and Hubs usually handle different topics. Use separate vaults for meaningful access or ownership boundaries.

---

# Part 2: The Root System

Use these seven default roots for a new vault. For an established vault, inspect and document an approved equivalent map before changing it:

```text
00 Inbox
10 Areas
20 Projects
30 Incubator
40 Resources
90 Archive
99 System
```

## What each root means

| Folder | Purpose | Simple test |
|---|---|---|
| `00 Inbox` | Temporary capture whose correct home is not known yet | “I need to save this before deciding.” |
| `10 Areas` | Ongoing responsibilities, identities, standards, and current truth | “I maintain this.” |
| `20 Projects` | Active efforts with a specific outcome and finish condition | “I will finish this.” |
| `30 Incubator` | Possibilities for later that are not current commitments | “I may do this.” |
| `40 Resources` | Reusable knowledge, frameworks, references, and tools | “I may reuse this.” |
| `90 Archive` | Completed, cancelled, retired, or inactive material worth keeping | “This is no longer current.” |
| `99 System` | Rules, templates, navigation, schemas, and agent instructions | “This controls how the vault works.” |

## Why the numbers exist

- `00` keeps capture first.
- `10–40` keep normal working categories in a predictable order.
- `90` keeps inactive history near the end.
- `99` keeps the operating system last.
- The gaps allow a future major root without renaming everything.

The numbers are not priorities, dates, note IDs, or a reason to number every subfolder. Use numbering lightly.

---

## Personalize the Areas

Do not create generic app, social-media, or company folders unless the user actually has those responsibilities.

Possible Area maps:

### Independent professional

```text
10 Areas/
  Career/
  Clients/
  Finance/
  Health/
  Personal Brand/
```

### Student

```text
10 Areas/
  Courses/
  Career/
  Research/
  Health/
  Personal/
```

### Creator

```text
10 Areas/
  Personal Brand/
  Content/
  Audience/
  Products/
  Operations/
```

### Multi-company operator

```text
10 Areas/
  Organizations/
    Company A/
    Company B/
  Personal/
  Finance/
  Professional Development/
```

### Family or household

```text
10 Areas/
  Household/
  Family/
  Finance/
  Health/
  Travel/
```

These are examples, not presets. Use the user’s own vocabulary. If they call customers “members,” locations “facilities,” or work streams “practices,” preserve those terms.

---

## Route information by operational role, not subject alone

The same subject can appear in several roots:

```text
10 Areas/Company A/        Current company truth and ongoing operations
20 Projects/Company A Rebrand/  Finite rebrand effort
30 Incubator/New Service Idea/  Possible future offering
40 Resources/Brand Research/    Reusable branding knowledge
90 Archive/Old Rebrand/         Completed historical work
```

Links connect these notes. Do not mix them into one folder merely because they mention the same company.

---

# Part 3: Required Markdown Files

The setup is not complete when the folders exist. Each root must explain itself.

Create:

```text
Vault Hub.md

00 Inbox/
  Inbox.md

10 Areas/
  Areas Hub.md

20 Projects/
  Projects Hub.md

30 Incubator/
  Incubator Hub.md

40 Resources/
  Resources Hub.md

90 Archive/
  Archive Hub.md

99 System/
  System Hub.md
  How to Use This Vault.md
  Rules/
    Operating Contract.md
    Routing and Maintenance.md
    Capture Workflow.md
    Context and Provenance.md
    Platform Onboarding.md
    Migration and Recovery.md
    Validation and Enforcement.md
  Source and Tool Access Index.md
  Accuracy Change Log.md
  Templates/
    Hub Template.md
    Durable Note Template.md
    Project Template.md
    Idea Template.md
    Data Snapshot Guide Template.md
```

If the user already has equivalent notes, improve and link them rather than creating duplicates.

---

## What the root Vault Hub must contain

The root `Vault Hub.md` is the starting point for humans and agents.

Include:

1. The vault’s purpose.
2. The owner or organization.
3. The local vault path, stored privately. Never publish a real user path in the framework.
4. A table linking every root Hub.
5. A table linking the person’s real Areas.
6. The source-of-truth order.
7. Known limitations and stale data.
8. A fast handoff instruction containing the absolute path to this Hub.

Recommended opening:

```markdown
> [!important] Primary agent entry point
> Read this note first when no more specific Hub is named. Follow the relevant Hub before drafting, analyzing, updating, or retrieving information. Do not mix personal, company, client, or project rules unless a Hub explicitly connects them.
```

---

## What every root Hub must contain

Each root Hub should answer:

- What is this folder for?
- What belongs here?
- What does not belong here?
- How should an agent read it?
- How should an agent write to it?
- What are its important subfolders or views?
- Which other Hubs are related?

Use this minimum structure:

```markdown
---
type: hub
status: active
updated: YYYY-MM-DD
tags:
  - knowledge-management
aliases:
  - Alternate Hub Name
hub: "{{GOVERNING_HUB_WIKILINK}}"
---

# Folder Hub

> [!important] Purpose
> Explain the operational role of this folder.

## What belongs here

## What does not belong here

## Read rules

## Write rules

## Current entry points

## Related notes
```

---

## When a topic deserves its own Hub

Create a topic Hub when a subject has several durable notes, workflows, or source files.

A useful topic Hub includes:

- One-paragraph context.
- Goal or current operating model.
- A short “read in this order” table.
- Quick facts.
- Non-negotiable rules and permissions.
- Links to raw source files.
- Limitations and freshness.
- A fast handoff instruction.

Do not create a Hub for one small note. A Hub should orient the reader, not duplicate every detail.

---

# Part 4: Notes, Properties, Links, and Bases

## Give durable notes a clear job

Useful note types include:

- `hub`
- `guide`
- `workflow`
- `strategy`
- `decision`
- `project`
- `idea`
- `data-guide`
- `snapshot`
- `source`

Do not split every paragraph into a separate note. Create a focused note when the concept will be linked, reused, updated, or governed independently.

---

## Properties

Use YAML properties at the top of structured notes:

```yaml
---
type: guide
status: active
updated: YYYY-MM-DD
tags:
  - topic
aliases:
  - Alternate Name
hub: "{{GOVERNING_HUB_WIKILINK}}"
---
```

Properties should contain small structured facts, not paragraphs. Every maintained note except the root Hub needs a valid `hub:` up-pointer. Replace the template token with the actual nearest governing Hub; do not add metadata to exact raw evidence bytes.

Common properties:

| Property | Use |
|---|---|
| `type` | The note’s role |
| `status` | Current lifecycle state |
| `created` | Creation date |
| `updated` | Last meaningful update |
| `hub` | Full-path wikilink to the nearest governing Hub, except on the root Hub itself |
| `owner` | Person or organization responsible, only when evidenced |
| `area` | Owning Area |
| `outcome` | Finished result for a Project |
| `next_step` | Smallest useful next action |
| `snapshot_date` | Date represented by point-in-time data |
| `tags` | Cross-cutting filtering |
| `aliases` | Alternate names people may search |

Do not invent a universal schema before seeing the user’s real collections. Standardize repeated note types, not every note in the vault.

---

## Links

Use a link when opening the destination would provide useful context.

```text
[[Note Name]]
[[Folder/Note Name]]
[[Folder/Note Name#Section]]
[[Folder/Note Name|Readable label]]
```

Use links for:

- A Project to its owning Area.
- An Idea to the audience or problem it serves.
- A decision to its evidence.
- A current note to an older replaced version.
- A Hub to its focused context and raw sources.

Do not link every mention of every word. Links should create a useful reading path.

---

## Definitive Base rule

A Base is a dynamic view of Markdown notes. It is not where the information lives.

Create a Base only when all three are true:

1. Several notes represent the same kind of item.
2. The notes share useful properties.
3. The user repeatedly benefits from sorting, filtering, grouping, or viewing them together.

Good uses:

- Projects.
- Ideas.
- Meetings.
- Content records.
- Books.
- Contacts.
- Research sources.

Do not use a Base for:

- A guide or strategy note.
- A small unrelated collection.
- One long note.
- Information that only needs a Hub.
- Raw archives better stored as CSV, JSON, or one searchable file.
- Making the vault look advanced.

A Hub explains. A Base displays a changing inventory. A Hub may link or embed a Base when both are useful.

Before creating a Base:

- Search for an existing related Base.
- Define the property schema.
- Keep filters narrow.
- Verify expected notes appear.
- Verify unrelated notes do not appear.

---

# Part 5: Projects, Ideas, Sources, and Decisions

## Project rule

A Project must have a finish condition.

Minimum Project properties:

```yaml
---
type: project
status: planned
created: YYYY-MM-DD
updated: YYYY-MM-DD
hub: "{{GOVERNING_HUB_WIKILINK}}"
area:
  - "[[10 Areas/Relevant Area Hub]]"
outcome: A concrete finished result
next_step: The next physical action
tags:
  - project
---
```

Minimum Project sections:

- Outcome.
- Why now.
- Included and not included.
- Current state.
- Decisions.
- Sources and dependencies.
- Next step.
- Completion criteria.

If there is no finish condition, it is probably an Area, Resource, or Incubator item.

---

## Incubator rule

The Incubator is for possibilities, not commitments.

One substantive idea gets one note. The note should preserve:

- The original idea.
- The problem or opportunity.
- The proposed direction without pretending it is decided.
- Evidence or references.
- Open questions.
- The smallest useful next step.

Use idea types that match the user. Possible values include:

```text
business
content
product
feature
research
experiment
career
travel
other
```

Do not assume everyone has apps, content, or product ideas. Define the values after inspecting the user’s actual idea pipeline.

When an idea becomes active:

1. Create or link the Project or Area that owns it.
2. Mark the idea `promoted`.
3. Preserve the original idea note as decision history.

---

## Decision and dead-end rule

Agents understand context better when the vault preserves why something changed.

For important decisions, record:

- What was decided.
- Why.
- What alternatives were considered.
- What evidence supported it.
- What was rejected or reversed.
- When the decision may need review.

Do not erase a dead end merely because it failed. Preserve useful learning, but do not keep every trivial thought forever. A failed direction deserves a note when it could prevent repeated work or explain a later decision.

---

## Raw source rule

When exact wording, metrics, IDs, timestamps, or evidence matter:

1. Keep the raw export unchanged.
2. Add a date to snapshot filenames.
3. Write a data guide explaining fields, source, filters, freshness, and gaps.
4. Link summaries back to raw evidence.
5. Preserve older snapshots when history matters.
6. Do not silently “clean up” source records.

Possible structure:

```text
Topic/
  Topic Hub.md
  Topic Goal and Positioning.md
  Topic Voice and Tone.md
  Topic Workflow.md
  Topic Data and Sources.md
  Data/
    Topic Export YYYY-MM-DD.csv
    Topic Raw Response YYYY-MM-DD.json
```

Use only the notes the topic actually needs. Do not create empty categories.

---

# Part 6: Recommended Obsidian Features and Tools

## Start with core features

Enable these when useful:

- File Explorer.
- Search.
- Quick Switcher.
- Backlinks.
- Outgoing Links.
- Properties.
- Tags.
- Page Preview.
- Templates.
- Bases for repeated record-like notes.
- File Recovery.
- Automatic internal-link updates.

Core features are preferable when they solve the need. Add community plugins only for a real workflow gap.

---

## Sync and backup are different

> [!warning]
> Sync is not backup. A destructive change can sync to every device.

Choose one primary sync method:

### Obsidian Sync

- Official paid service.
- Supports end-to-end encryption and version history.
- Consider it when the user wants the official service; confirm current features and requirements before choosing it.

### Remotely Save

- Optional community plugin.
- Check the current project documentation for supported providers, compatibility, and configuration requirements. No provider is required by this framework.
- Useful when the user already prefers one of those providers.
- Back up the vault before first configuration.
- Review encryption and provider permissions.
- Do not describe it as official Obsidian Sync.

Maintain a separate backup:

- Time Machine or another computer backup.
- A periodic copy or archive on another disk.
- Versioned cloud backup.
- Git for users who understand it and configure private storage correctly.

Test recovery, not only syncing.

---

## Migration

### Importer

Use the official Obsidian Importer plugin when migrating from Notion or another supported app.

For Notion:

- Check the current Importer documentation for the available API and file import capabilities, including database handling. Test with representative records before promising fidelity.
- File import avoids an API token but preserves less database behavior.
- Choose the export format recommended by the current official Notion import documentation, and preserve the original export.
- Import into a staging folder first.
- Preserve the original export.
- Reconcile links, attachments, database properties, missing records, and duplicates before reorganizing.
- Store API tokens in a password manager, never in the vault.

Do not assume the imported folder structure should become the final structure. Import first, understand it, then map it into Areas, Projects, Incubator, Resources, or Archive.

---

## Search and capture

Optional community plugins:

- **Omnisearch:** stronger full-vault search when core Search is not enough.
- **QuickAdd:** repeatable captures and templates after the user has a stable workflow.
- **Calendar:** useful when daily notes and dates are central.
- **Kanban:** useful for people who truly work from visual boards.

Do not install workflow plugins before the workflow exists.

---

## Appearance

Appearance should make the vault pleasant enough that the human returns to it.

- **Border** is a clean, customizable optional theme.
- A theme does not affect the information architecture.
- Test readability, mobile behavior, and plugin compatibility.
- Avoid spending more time styling the vault than using it.

---

## Community-plugin rule

Every community plugin adds maintenance and security surface.

Before recommending one:

1. Confirm core Obsidian cannot already solve the need.
2. Check that the plugin is currently maintained.
3. Read its permissions, documentation, and issue tracker.
4. Back up before installation or major configuration.
5. Install the smallest set needed.
6. Document why the plugin exists in `99 System`.

Do not copy another person’s plugin list as a default.

---

# Part 7: Implementation Sequence

The setup agent should work in this order:

## Phase 1: Audit

- Confirm the vault root.
- List current folders and files.
- Identify existing Hubs, guides, templates, Bases, and raw sources.
- Inspect backlinks before moving notes.
- Inspect `.obsidian` configuration read-only.
- Count important imported collections.
- Record missing attachments and broken links.

## Phase 2: Personalize

- Ask the discovery questions.
- Identify real Areas and confidentiality boundaries.
- Identify active Projects and future possibilities.
- Identify reusable Resources and authoritative sources.
- Decide one vault versus several.
- Propose the final map with examples from the user’s actual work.

## Phase 3: Approve

Show:

- Root structure.
- Area map.
- Planned Hubs.
- Planned templates.
- Any Bases and why each passes the Base rule.
- Migration and archive plan.
- Plugin recommendations grouped as required or optional.
- Anything that will be moved, renamed, merged, archived, or removed.

Get approval before broad or destructive changes.

## Phase 4: Build

- Create the seven roots.
- Create the root Vault Hub.
- Create a Hub in every root.
- Create real Area Hubs.
- Create the human guide.
- Create the agent guide and organization contract.
- Create only the useful templates.
- Create approved Bases.
- Configure the Templates folder if authorized.
- Enable approved core features.
- Install optional tools only when authorized.

## Phase 5: Migrate

- Import into a staging folder.
- Preserve the original export.
- Reconcile counts and attachments.
- Move information according to operational role.
- Preserve source irregularities.
- Add links from summaries to raw sources.
- Archive superseded material instead of deleting it.

## Phase 6: Validate

- Parse YAML.
- Resolve internal links.
- Check backlinks for moved notes.
- Confirm Base filters.
- Reconcile source-data counts.
- Confirm no secrets were stored.
- Confirm no unexpected top-level folders exist.
- Confirm sync and backup are separate.
- Open the main Hubs in Obsidian and check that they are readable.

---

# Part 8: Source-of-Truth and Agent Behavior

When sources disagree, use this order:

1. The user’s current explicit instruction.
2. A source the user explicitly named for the task.
3. The topic’s Hub or Guide.
4. The focused note dedicated to the fact or rule.
5. The newest verified raw source or dated snapshot.
6. Older notes and historical snapshots.
7. Agent inference.

Label inference. Never store an inference as confirmed fact without evidence.

## Read protocol

1. Start with the path or topic the user named.
2. If none is named, open the root Vault Hub.
3. Follow the nearest topic Hub.
4. Read its short reading order.
5. Use raw sources when precision matters.
6. Check freshness and limitations.

## Write protocol

1. Choose the correct root.
2. Search for an existing note on the same subject.
3. Read the destination Hub.
4. Preserve existing naming and properties.
5. Write the smallest durable note that solves the need.
6. Link it to its Hub and evidence.
7. Validate after writing.

## Permission boundary

Writing to the vault does not authorize an agent to:

- Publish.
- Post.
- Send messages.
- Contact people.
- Deploy.
- Change external tools.
- Delete source data.

Those actions require their own authorization.

---

# Part 9: Human-Friendly Daily Use

The finished human guide should stay simple:

```text
1. Capture unclear things in Inbox.
2. Move them to the right home.
3. Link only useful relationships.
4. Give Projects and Ideas a next step.
5. Review Inbox and active Projects regularly.
```

The easiest routing test:

```text
I maintain this   → Area
I will finish this → Project
I may do this      → Incubator
I may reuse this   → Resource
It is no longer current → Archive
It controls the vault → System
I do not know yet  → Inbox
```

Do not require the human to think about schemas and metadata every time they write. Templates and agents should carry that burden.

---

# Part 10: Final Validation Checklist

The setup is complete only when:

- [ ] The exact vault root is documented.
- [ ] A backup exists before broad migration.
- [ ] The seven roots exist or deviations are documented.
- [ ] Every root has a Hub.
- [ ] Every maintained note has a governing `hub:` pointer and reaches the root without a cycle.
- [ ] Every Hub registers its maintained children, and templates/generators emit the same schema.
- [ ] The root Vault Hub links the whole system.
- [ ] Real Areas match the user’s life and work.
- [ ] Projects have finish conditions.
- [ ] Incubator items are not presented as commitments.
- [ ] Resources are reusable, not disguised active work.
- [ ] System contains rules and templates, not subject matter.
- [ ] Important topics have readable Hubs and short reading orders.
- [ ] Raw sources are preserved.
- [ ] Source-of-truth and permission rules are explicit.
- [ ] Properties are consistent within repeated note types.
- [ ] Every Base passes the three-part Base rule.
- [ ] All internal links resolve.
- [ ] Imported record counts reconcile.
- [ ] Missing files and stale facts are documented.
- [ ] No secrets are stored.
- [ ] Sync and backup are separate.
- [ ] Optional plugins each have a documented reason.
- [ ] The human guide is short enough to use.
- [ ] The agent guide is complete enough to prevent guessing.

---

# Fast instruction to give the setup agent

```text
Use this entire file as the setup contract. First inspect my Obsidian vault read-only and identify what already exists. Ask me the discovery questions in small groups, using my existing files to avoid unnecessary questions. Then propose a personalized map based on the seven-root system. Do not invent Areas such as apps, social media, or companies unless they match my real work. Explain every proposed folder, Hub, template, Base, migration, and optional plugin. Get my approval before broad moves or destructive changes. After approval, build the system, preserve raw sources and original wording, link every Hub, validate YAML and internal links, reconcile imported data, and give me a short human guide plus a fast handoff instruction for future agents.
```

---

# Research basis

## Obsidian

- [How Obsidian stores data](https://obsidian.md/help/data-storage) explains that a vault is a normal local folder containing Markdown files.
- [Properties](https://obsidian.md/help/properties) provides structured, human- and machine-readable note data.
- [Internal links](https://obsidian.md/help/links) connects related knowledge without requiring one folder.
- [Backlinks](https://obsidian.md/help/backlinks) reveals notes that refer to the current note.
- [Bases](https://obsidian.md/help/bases) provides database-like views over local Markdown files and properties.
- [Templates](https://obsidian.md/help/plugins/templates) supports repeatable note structures.
- [Import from Notion](https://obsidian.md/help/import/notion) explains API and file migration through the official Importer plugin.
- [Back up your Obsidian files](https://obsidian.md/help/backup) explains why syncing is not a backup.
- [Obsidian Sync security and privacy](https://help.obsidian.md/Obsidian%20Sync/Security%20and%20privacy) describes its encryption options.

## Organization methods

- [PARA](https://fortelabs.com/blog/para/) organizes information by actionability through Projects, Areas, Resources, and Archives.
- [Johnny.Decimal](https://johnnydecimal.com/10-19-concepts/11-core/11.02-areas-and-categories/) supports stable bounded organization; this blueprint uses only light root numbering.
- [Zettelkasten introduction](https://zettelkasten.de/introduction/) supports focused, independently linkable notes; this blueprint adopts that principle without requiring a full slip-box method.

## Optional tool references

- [Remotely Save](https://github.com/remotely-save/remotely-save) is an optional community sync plugin that supports Dropbox and other providers. It is not official Obsidian Sync.

The methods above explain organization mechanics. The user’s actual filesystem, work, vocabulary, sources, and operating boundaries must determine the final personalized structure.



# Current implementation requirements

The discovery and architecture above remain useful, but a folder scaffold is insufficient. The current complete implementation includes:

- Compact `AGENTS.md` discovery plus a separately installed persistent platform bootstrap.
- Four honest access modes, with no false filing claims from a capture-only tool.
- A parent `hub:` on every maintained note; Hub registration and root reachability.
- Grounding gates before durable edits, source claims, identity decisions, and classification.
- A single canonical explanation connected to one preserved original.
- Source authority, adoption, verification, dates, and assistant interpretation kept distinct.
- Whole-vault duplicate and capture-ID searches, including Archive.
- Safe old-to-new path maps and complete link repair on moves.
- Reconciliation of metadata, body, status, next step, scope, names, placement, views, templates, instructions, generators, and useful output.
- Complete inbox sweeps across all file types, a final re-list, mixed-meaning routing, and transcript uncertainty that blocks only uncertain details.
- Accuracy corrections with evidence and preserved supersession history.
- A dated source/tool-access index with capabilities actually checked.
- Optional build accountability with Request Logs, Build Plans, plan stress-testing, phase gates, and real outcome verification.
- Automated structural checks, privacy preflight, behavioral acceptance tests, and explicit limits on enforcement.

Read the linked specifications and use the complete starter. Do not treat this list as a replacement for their full instructions. Personalize the installed vault with the user's real context, chosen integrations, sources, preferences, and responsibilities.
