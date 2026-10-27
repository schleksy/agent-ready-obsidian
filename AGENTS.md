# Repository agent instructions

For a task to set up, adapt, audit, or maintain a user's Obsidian vault, read `SKILL.md` and follow its task route. Perform the setup for the user rather than asking them to read the repository or run commands you can run.

The rules below govern changes to the toolkit itself. The user's separate vault is governed by its own adopted rules.

1. Read `README.md` before changes. For changes to vault behavior, read `docs/operating-contract.md` and the relevant specification.
2. Follow `CONTRIBUTING.md` for examples and reports. Keep credentials out of the checkout.
3. `docs/` holds the canonical specifications. `vault-template/99 System/Rules/` contains generated installation copies. Run `python scripts/sync_rules.py` after changing a mapped specification; do not hand-edit generated copies.
4. Keep the grounding, provenance, routing, duplicate-prevention, and maintenance gates intact. Personalize the user's vault with their real context; do not apply repository contribution restrictions to private notes.
5. Keep `SKILL.md` short, use relative links, and bundle every referenced resource. No specific provider, paid account, or personal folder layout is required.
6. Run `python -m unittest discover -s tests -v`, `python scripts/check_repo.py`, and `python scripts/privacy_scan.py .` before delivery.
7. Use synthetic test fixtures. Never upload a user's vault as a test artifact.
8. Respect the user's applicable authorization for publishing and external actions. Use pull requests and required checks for changes to `main`.
9. Report actual verification. Structural tests cannot prove source comprehension, factual accuracy, or live platform behavior.
