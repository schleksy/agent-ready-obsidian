# Contributing

Improve the setup method, documentation, templates, and tooling. Use small, focused pull requests with a clear problem, resulting behavior, and verification.

## Examples and issue reports

Use synthetic examples in issues, pull requests, test fixtures, and screenshots. Do not submit someone else's private notes, credentials, exports, or account configuration. These contribution guidelines apply to this repository; users decide what personal or confidential knowledge belongs in their own vaults.

## Make a change

Edit the canonical specification in `docs/`, then run `python scripts/sync_rules.py` to refresh the installed rule copies. Keep setup prompts, templates, schemas, note generators, and validators consistent. Do not hand-edit generated copies or weaken grounding requirements to make a check pass.

Keep `SKILL.md` concise and link directly to the complete references. The whole repository is the skill bundle; do not leave it depending on unbundled private files or a particular person's tools.

## Verify

```bash
python -m unittest discover -s tests -v
python scripts/check_repo.py
python scripts/privacy_scan.py .
```

The scanner checks repository files for likely sensitive patterns. An optional `--deny-file` can supply additional literals from a file outside the checkout. It is a heuristic, does not audit Git history, and is not a validator for the contents of a user's private vault. Use `scripts/audit_vault.py` for vault structure.

Describe what was actually tested and any limitations. Add focused regression coverage for meaningful behavior changes. Do not claim a platform integration works without testing it.

## Pull requests

Changes to `main` go through a pull request and the required validation check. Keep dependency pins current. See `SECURITY.md` for sensitive reports.
