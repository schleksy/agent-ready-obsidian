# Platform onboarding and access

This framework works through Markdown and links. It does not require a particular model or vendor. Platform discovery and permissions still have to be configured and tested.

## Optional skill entry

Agents supporting the Agent Skills format can use the root `SKILL.md` as a task router. Install or copy the complete toolkit directory, retaining all referenced resources. The user's vault remains at its own selected path. A skill entry does not provide filesystem permission, install a connector, or configure persistent onboarding by itself.

## Access modes

| Mode | What is possible | What must not be claimed |
| --- | --- | --- |
| Full vault access | Read and authorized local edits | That all external actions are also authorized |
| Read-only vault access | Research, retrieval, plans, audits | That notes were changed |
| Capture-only access | Submit a new capture through a configured service | That existing knowledge was inspected, merged, or organized |
| No vault access | Work on supplied material and prepare instructions | That live vault rules, state, or saves were verified |

Record actual effective access per session and per source. A connected tool can fail, have narrower scopes, or operate on a different account. Test a harmless read instead of relying on the connector's displayed name.

## Minimal persistent bootstrap

Adapt only the local path and stable entry names. Store this in the platform's supported persistent instruction location with the user's authorization:

```text
My knowledge vault is at <VAULT_PATH>.
For vault-related work, read AGENTS.md at that root, then the linked onboarding note and Vault Hub.
Use the access mode this session actually has. Assemble the governing Hub chain before writing or claiming facts.
For short commands, use the onboarding router. Use capture-only access only for captures and report its limits honestly.
Do not duplicate the full rulebook in this configuration.
```

A path is not a permission grant or a credential. Do not put passwords or bearer tokens into this text.

## File-based agents

For tools that support `AGENTS.md`, place the compact entry at the vault root and work within the correct mounted folder. Some platforms use different instruction filenames or have their own scope rules. Use their current documented mechanism; do not assume one filename is universal.

When build code lives outside the vault, add a small project pointer to the governing vault Hub when authorized. Do not copy the whole vault into a code repository. Do not put a private absolute path into a public repository; use a locally configured pointer or non-committed bootstrap.

## Claude Code example

Use the platform's instruction mechanism to point to the vault entry. Optional `PreToolUse` hooks can deliver a reminder for `Write` and `Edit`. The exact JSON schema and event behavior must be verified against the current [official hooks documentation](https://code.claude.com/docs/en/hooks).

A successful reminder hook uses structured stdout, such as `hookSpecificOutput.additionalContext` for `PreToolUse`; ordinary stderr is not a substitute for model-visible context. This repository does not auto-install a hook or change global settings.

A matcher for `Write|Edit` misses shell/script writes and tool-specific connectors. A reminder that exits successfully does not block or prove grounding. Test both an in-vault and an outside-vault case through the actual installed tool. Record configuration status separately from live integration verification.

## ChatGPT, other chat agents, and connectors

Supply the bootstrap plus access to the actual named files through the available filesystem or read connector. A chat session without that access can use uploaded copies, but those copies are snapshots. State their freshness and do not claim edits reached the original vault.

If only a remote capture action is exposed, use the capture-only protocol. No endpoint is supplied by this repository. A user must deliberately provision and test one if needed.

## New-agent acceptance test

Start a fresh session, without relying on the setup conversation. Ask the agent:

1. What can you actually access, and what is the root entry point?
2. Which Hubs and rules govern a sample task?
3. Starting from a deep note, how do you reach its root contract?
4. What would you read before organizing Inbox? Do not write yet.
5. What would you do with an uncertain owner or repeated capture ID?
6. Which actions remain unauthorized?

Then test one harmless authorized write and validate its metadata, parent registration, and links. Separately open the main Hubs in Obsidian to inspect their appearance. Repeat onboarding when changing host, tool, mount, or permissions. Never mark another device configured because the first one works.

## Source and tool index

Maintain a local index with source purpose, authority, verified read/write capabilities, account/workspace scope, verification date, restrictions, known gaps, and a pointer to secure configuration. Do not include secret values. Decide which source owns tasks, calendar facts, meeting wording, files, code, published content, and durable context.

An old inventory is historical. Recheck callability for the current task. Read the user-named authoritative source instead of a convenient summary in another app.
