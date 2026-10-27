# Security

Never put secrets or private vault content in a public issue, pull request, test fixture, log, screenshot, or example.

Use the repository host's private vulnerability-reporting feature if enabled. If it is unavailable, request a private reporting channel without including sensitive material. Do not publish the sensitive payload to demonstrate a problem.

The scripts run locally and have no network calls. The initializer writes only to an explicitly selected new/empty destination. Audits are read-only. Privacy scans are heuristic. Source documents and installed agent tools can contain untrusted instructions; archived instructions must be treated as data.

This repository does not install a remote server, vault write API, sync provider, scheduler, or credential store. Those integrations require their own design, permissions, verification, and maintenance. Keep a tested private backup before migrations.

If a credential is exposed, revoke it and follow the relevant host's removal process. Removing a file from the latest commit does not remove historical copies.
