---
name: agent-ready-obsidian
description: Set up, adapt, audit, or maintain a personalized Obsidian vault for humans and AI agents. Use when building an agent-ready knowledge base, organizing an existing vault, configuring agent onboarding, migrating notes, or establishing grounded capture and maintenance workflows.
---

# Agent-Ready Obsidian

Act as the setup agent for the current user. Read this toolkit, inspect their existing setup, resolve missing decisions with them, build the personalized system, and verify it. Do not make the user study the repository or run setup commands you can run. Preserve their context and decision history and leave reliable entry points for future agents.

Resolve every path below relative to this skill directory. Retain the complete bundle; the references, scripts, and starter are part of the skill.

## Start

1. Identify the user's actual vault path, requested outcome, and effective access mode. A named connector is not proof of access.
2. Read the vault's existing entry points and governing Hubs. Reuse adopted decisions and conventions; do not overwrite an established setup with the starter.
3. Read [the operating contract](docs/operating-contract.md) and [routing and maintenance](docs/routing-and-maintenance.md) before durable writes.
4. Use the task route below. Ask only consequential questions the existing evidence does not answer, one at a time. Continue independent authorized work.

## Route by task

| Task | Read and use |
| --- | --- |
| New or substantially adapted setup | [Setup brief](prompts/setup-agent.md), [complete setup guide](docs/setup-guide.md), [starter vault](vault-template/) |
| Existing-vault migration | [Migration and recovery](docs/migration.md), then the relevant destination Hubs |
| Inbox or remote capture | [Capture workflow](docs/capture-workflow.md), plus routing and maintenance |
| Imported conversations and memories | [Context and provenance](docs/context-and-provenance.md) |
| Agent or connector onboarding | [Platform onboarding](docs/platforms.md) |
| Software-build accountability, if relevant | [Build workflow](docs/build-workflow.md) |
| Audit, acceptance, or closeout | [Validation](docs/validation.md) and the actual evidence |

Keep the full instructions in their references and installed canonical rules. This entry point does not replace them.

## Personalize

Use the user's real names, organizations, projects, messages, meeting notes, schedules, preferences, and other useful context when relevant and authorized. Preserve ownership and evidence. Generic toolkit examples are not a restriction on private knowledge. Put authentication secrets in a proper credential store and follow the user's sharing permissions.

Use the seven-root model for a new vault. For an existing vault, establish and document an approved mapping. Create only the Areas, subjects, templates, views, and integrations the user actually needs. Keep possibilities separate from commitments and maintain one canonical explanation linked to its preserved original.

## Execute and verify

Run toolkit commands from this skill directory. The initializer is optional and only supports an absent or empty destination:

```bash
python scripts/init_vault.py --destination "<ABSOLUTE_VAULT_PATH>"
# Review the preview; use --apply only for an authorized new-vault setup.
python scripts/audit_vault.py "<ABSOLUTE_VAULT_PATH>"
```

The scripts require Python 3.10 or later; the auditor requires PyYAML from `requirements.txt`. If those capabilities are unavailable, state the limitation and do the possible work rather than claiming installation or verification succeeded. Never run the initializer over an existing vault.

Before completion, reconcile affected notes, metadata, navigation, sources, templates, views, and generators. Report the real access, work performed, checks passed, remaining gaps, and usable next entry point. A scaffold or a passing script alone is not a personalized setup, and a reminder is not a hard permission gate.
