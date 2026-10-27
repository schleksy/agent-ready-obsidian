#!/usr/bin/env python3
"""Generate installed rule copies from the public canonical specifications."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    'operating-contract.md': 'Operating Contract',
    'routing-and-maintenance.md': 'Routing and Maintenance',
    'capture-workflow.md': 'Capture Workflow',
    'context-and-provenance.md': 'Context and Provenance',
    'build-workflow.md': 'Build Workflow',
    'platforms.md': 'Platform Onboarding',
    'migration.md': 'Migration and Recovery',
    'validation.md': 'Validation and Enforcement',
}


def rendered(source: str) -> str:
    body = (ROOT / 'docs' / source).read_text(encoding='utf-8')
    return ('---\ntype: agent-rule\nstatus: active\nupdated: 2026-10-27\n'
            'tags: [agent-rules]\naliases: []\n'
            'hub: "[[99 System/Rules/Rules Hub]]"\n---\n\n'
            '> Framework source: `docs/' + source + '`. This installed copy is the '
            'local rule after adoption. Personalize only with the user’s actual decisions; '
            'keep changes coherent across local entry points.\n\n' + body)


def main() -> None:
    for source, name in RULES.items():
        target = ROOT / 'vault-template' / '99 System' / 'Rules' / (name + '.md')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered(source), encoding='utf-8')
    print(f'Updated {len(RULES)} generated rule copies.')


if __name__ == '__main__':
    main()
