#!/usr/bin/env python3
"""Check documentation, generated rule copies, starter structure, and Base YAML."""
from pathlib import Path
import re
from urllib.parse import unquote
import yaml
from audit_vault import audit, without_fences
from sync_rules import RULES, ROOT, rendered


def check_skill(directory=ROOT):
    path = Path(directory) / 'SKILL.md'
    if not path.is_file():
        return ['skill: missing SKILL.md']
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        return ['skill: invalid frontmatter delimiters']
    try:
        data = yaml.safe_load(text[4:].split('\n---\n', 1)[0])
    except yaml.YAMLError:
        return ['skill: invalid YAML']
    if not isinstance(data, dict):
        return ['skill: metadata must be a mapping']
    errors = []
    name = data.get('name', '')
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append('skill: invalid lowercase hyphenated name')
    description = data.get('description', '')
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        errors.append('skill: description must contain 1-1024 characters')
    if len(text.splitlines()) > 500:
        errors.append('skill: entry exceeds 500 lines; move details to references')
    return errors


def check_workflow(path):
    try:
        data = yaml.load(Path(path).read_text(encoding='utf-8'), Loader=yaml.BaseLoader)
    except yaml.YAMLError:
        return ['workflow: invalid YAML']
    if not isinstance(data, dict):
        return ['workflow: expected mapping']
    errors = []
    if data.get('permissions') != {'contents': 'read'}:
        errors.append('workflow: expected read-only contents permission')
    for job in data.get('jobs', {}).values():
        for step in job.get('steps', []):
            action = step.get('uses')
            if action and not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+@[0-9a-f]{40}', action):
                errors.append('workflow: action must use an immutable full commit SHA')
            if action and action.startswith('actions/checkout@') and step.get('with', {}).get('persist-credentials') != 'false':
                errors.append('workflow: checkout must not persist credentials')
    return errors


def check():
    errors = check_skill() + check_workflow(ROOT / '.github' / 'workflows' / 'validate.yml')
    errors += audit(ROOT / 'vault-template', template=True)
    for source, title in RULES.items():
        target = ROOT / 'vault-template' / '99 System' / 'Rules' / (title + '.md')
        if not target.exists() or target.read_text(encoding='utf-8') != rendered(source):
            errors.append(f'generated rule stale: {title}; run scripts/sync_rules.py')
    for path in ROOT.rglob('*.md'):
        if set(path.relative_to(ROOT).parts) & {'.git', '.venv', '__pycache__'}:
            continue
        text = without_fences(path.read_text(encoding='utf-8'))
        for match in re.finditer(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
            link = match.group(1).split('#', 1)[0].strip('<>')
            if not link or re.match(r'[a-zA-Z]+:', link):
                continue
            if not (path.parent / unquote(link)).exists():
                errors.append(f'{path.relative_to(ROOT)}: broken local Markdown link {link}')
    for path in (ROOT / 'examples').rglob('*.base') if (ROOT / 'examples').exists() else []:
        try:
            data = yaml.safe_load(path.read_text(encoding='utf-8'))
            if not isinstance(data, dict) or not isinstance(data.get('views'), list):
                errors.append(f'{path.relative_to(ROOT)}: invalid Base document shape')
        except yaml.YAMLError:
            errors.append(f'{path.relative_to(ROOT)}: invalid Base YAML')
    return errors


if __name__ == '__main__':
    findings = check()
    for finding in findings:
        print(finding)
    print(f'{len(findings)} repository consistency finding(s).')
    raise SystemExit(1 if findings else 0)
