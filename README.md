# Agent-Ready Obsidian

Instructions and tools for an AI agent to set up and maintain its user's Obsidian knowledge base.

## Agent entry point

Read [SKILL.md](SKILL.md) first. Treat this repository as the setup method, then learn the current user's actual context and configure their vault. The user does not need to read these guides or perform setup commands you can run yourself.

If the user has only supplied this repository, establish their vault location and your effective access. Inspect what exists before asking questions. Ask only for decisions the evidence cannot answer, one at a time, and complete the authorized setup.

## Read by task

| Task | Instructions |
| --- | --- |
| New or adapted vault | [Setup brief](prompts/setup-agent.md) and [complete setup guide](docs/setup-guide.md) |
| Every durable write | [Operating contract](docs/operating-contract.md) and [routing and maintenance](docs/routing-and-maintenance.md) |
| Existing-vault migration | [Migration and recovery](docs/migration.md) |
| Inbox and capture | [Capture workflow](docs/capture-workflow.md) |
| Imported chats and memories | [Context and provenance](docs/context-and-provenance.md) |
| Agent access and persistent entry | [Platform onboarding](docs/platforms.md) |
| Build accountability, if relevant | [Build workflow](docs/build-workflow.md) |
| Verification and completion | [Validation](docs/validation.md) |
| Starting files | [Vault template](vault-template/) |
| Optional collection views | [Base examples](examples/) |

## Build around the user

Use the user's real responsibilities, names, organizations, projects, messages, meeting notes, schedules, preferences, and source material when relevant and authorized. Do not substitute generic placeholders for their useful context. Preserve evidence, decision reasons, and adopted boundaries.

Use these default roots for a new vault. Map an existing structure deliberately instead of replacing it blindly.

| Root | Role |
| --- | --- |
| `00 Inbox` | Temporary unresolved capture |
| `10 Areas` | Ongoing responsibilities and current truth |
| `20 Projects` | Committed outcomes with finish conditions |
| `30 Incubator` | Possibilities that are not commitments |
| `40 Resources` | Reusable knowledge |
| `90 Archive` | Inactive history |
| `99 System` | Rules, navigation, schemas, and templates |

Create only the subject structure the user actually needs. Search before creating, follow governing Hub chains, retain one canonical explanation linked to its original source, and reconcile affected notes, templates, views, and generators together.

## Tools

Run these from the toolkit directory. Use the host's available Python executable; Python 3.10 or later is required for the tools, and the auditor requires PyYAML from `requirements.txt`.

```bash
# New, absent or empty destination: preview first.
python scripts/init_vault.py --destination "<ABSOLUTE_VAULT_PATH>"
# Apply only for an authorized new-vault setup.
python scripts/init_vault.py --destination "<ABSOLUTE_VAULT_PATH>" --apply
# Audit the actual vault, including an existing one.
python scripts/audit_vault.py "<ABSOLUTE_VAULT_PATH>"
```

Never run the initializer over an existing vault. Inspect and use the migration procedure instead. If a tool or connector is unavailable, state the specific limit, complete the independent possible work, and do not claim installation or verification succeeded.

## Completion

Deliver a working personalized vault with connected entry points, complete adopted rules, useful templates, preserved sources, a tested agent bootstrap, and an honest verification report. Give the user the short handoff they need; keep implementation work with the agent. A scaffold or a passing script alone is insufficient.

Structural checks cannot prove source comprehension or factual accuracy. Reminder hooks are advisory; effective permissions come from the host. Follow the validation guide to test those boundaries separately.

## Skill packaging and maintenance

The complete repository is the skill bundle. Keep `docs/`, `prompts/`, `scripts/`, and `vault-template/` alongside `SKILL.md` when installing it through a compatible skill mechanism. Skill installation does not supply filesystem access or configure onboarding by itself.

For toolkit changes, follow [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md). See [SECURITY.md](SECURITY.md) and [LICENSE](LICENSE). This project is independent of Obsidian and agent vendors.
