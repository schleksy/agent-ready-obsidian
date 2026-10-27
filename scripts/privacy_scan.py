#!/usr/bin/env python3
"""Heuristic public-package scan. Never prints a matched sensitive value."""
import argparse
from pathlib import Path
import re
import sys

SKIP = {'.git', '.venv', '__pycache__', '.pytest_cache'}
TEXT_EXTENSIONS = {'.md', '.py', '.txt', '.yml', '.yaml', '.json', '.base', '.sha256'}
TEXT_NAMES = {'LICENSE', '.gitignore', '.gitattributes'}
BLOCKED = {'.env', 'credentials.json', 'cookies', 'cookies.sqlite', 'settings.local.json', 'id_rsa', 'id_ed25519'}
PATTERNS = {
    'private-key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'github-token': re.compile(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{30,}\b'),
    'cloud-access-key': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'provider-key': re.compile(r'\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{32,}\b'),
    'slack-token': re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b'),
    'local-user-path': re.compile(r'(?:/Users/|/home/)[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\[A-Za-z0-9._-]+\\'),
    'bearer-literal': re.compile(r'Bearer\s+[A-Za-z0-9._-]{32,}'),
    'email-address': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
}


def scan(root, deny_terms=()):
    root = Path(root).resolve()
    findings = []
    stack = [root]
    while stack:
        directory = stack.pop()
        for path in directory.iterdir():
            rel = path.relative_to(root).as_posix()
            if path.name in SKIP:
                continue
            if path.is_symlink():
                findings.append(f'{rel}: symlink must be removed from public package')
                continue
            if path.is_dir():
                if path.name == '.obsidian':
                    findings.append(f'{rel}: private application configuration directory')
                else:
                    stack.append(path)
                continue
            if path.name.lower() in BLOCKED or path.name.startswith('.env.'):
                findings.append(f'{rel}: forbidden private configuration filename')
            if path.suffix not in TEXT_EXTENSIONS and path.name not in TEXT_NAMES:
                findings.append(f'{rel}: unexpected binary or unreviewed file type')
                continue
            try:
                content = path.read_text(encoding='utf-8')
            except UnicodeError:
                findings.append(f'{rel}: non-text bytes require separate review')
                continue
            for label, pattern in PATTERNS.items():
                for match in pattern.finditer(content):
                    line = content.count('\n', 0, match.start()) + 1
                    findings.append(f'{rel}:{line}: {label}')
            folded = content.casefold()
            for number, term in enumerate(deny_terms, 1):
                if term and term.casefold() in rel.casefold():
                    findings.append(f'{rel}: private-term-{number} in filename')
                start = 0
                while term and (offset := folded.find(term.casefold(), start)) >= 0:
                    line = content.count('\n', 0, offset) + 1
                    findings.append(f'{rel}:{line}: private-term-{number}')
                    start = offset + len(term)
    return sorted(set(findings))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--deny-file', type=Path)
    args = parser.parse_args()
    terms = []
    try:
        if args.deny_file:
            deny = args.deny_file.resolve()
            root = args.directory.resolve()
            if deny == root or root in deny.parents:
                parser.error('The private deny file must be outside the public package.')
            terms = [line.strip() for line in deny.read_text(encoding='utf-8').splitlines()
                     if line.strip() and not line.lstrip().startswith('#')]
        findings = scan(args.directory, terms)
    except OSError:
        print('Scan failed: a scoped file could not be read.', file=sys.stderr)
        return 2
    for finding in findings:
        print(finding)
    print(f'{len(findings)} heuristic finding(s). Manual content and history review still required.')
    return 1 if findings else 0


if __name__ == '__main__':
    raise SystemExit(main())
