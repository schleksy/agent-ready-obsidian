#!/usr/bin/env python3
"""Read-only audit of the documented default vault contract. Not a fact checker."""
import argparse
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path, PurePosixPath
import re
import sys
import unicodedata

import yaml

ROOTS = {'00 Inbox', '10 Areas', '20 Projects', '30 Incubator', '40 Resources', '90 Archive', '99 System'}
SKIP = {'.obsidian', '.git', '.trash', '__pycache__'}
TEMPLATE = '99 System/Templates/'
REQUIRED = {'type', 'status', 'updated', 'tags', 'aliases'}
WIKI = re.compile(r'!?\[\[([^\]\n]+)\]\]')
TOKEN = re.compile(r'\{\{[^\n{}]+\}\}')


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError('duplicate YAML key')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def frontmatter(text):
    if not text.startswith('---\n'):
        raise ValueError('YAML frontmatter must start on line 1')
    parts = text[4:].split('\n---', 1)
    if len(parts) != 2 or (parts[1] and not parts[1].startswith('\n')):
        raise ValueError('missing frontmatter closing delimiter')
    metadata = yaml.load(parts[0], Loader=UniqueLoader)
    if not isinstance(metadata, dict):
        raise ValueError('frontmatter must be a mapping')
    return metadata, parts[1].lstrip('\n')


def without_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = (mark[0], len(mark))
            elif mark[0] == fence[0] and len(mark) >= fence[1]:
                fence = None
            lines.append('')
        else:
            lines.append(line if fence is None else '')
    return '\n'.join(lines)


def clean_heading(value):
    value = re.sub(r'[`*_~]', '', value.strip().rstrip('#').strip())
    return unicodedata.normalize('NFC', value).casefold()


def raw_asset(path):
    return bool({'Sources', 'Data', 'Raw'} & set(PurePosixPath(path).parts))


def audit(root, template=False):
    root = Path(root)
    errors = []
    if not root.is_dir() or root.is_symlink():
        return ['root: expected a real vault directory']
    if not template and not (root / '.obsidian').is_dir():
        errors.append('root: missing .obsidian; confirm the actual vault root')
    actual = {p.name for p in root.iterdir() if p.is_dir() and not p.name.startswith('.')}
    for name in sorted(ROOTS - actual):
        errors.append(f'root: missing required root {name}')
    for name in sorted(actual - ROOTS):
        errors.append(f'root: unexpected content root {name}')
    files = {}
    # Walk explicitly without following links. Hidden app/git directories are not source notes.
    stack = [root]
    while stack:
        directory = stack.pop()
        for p in directory.iterdir():
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                errors.append(f'{rel}: symlink not audited')
            elif p.name in SKIP or p.name == '.DS_Store':
                continue
            elif p.is_dir():
                stack.append(p)
            elif p.is_file():
                files[rel] = p
    for required in ('Vault Hub.md', 'AGENTS.md', 'README.md', '99 System/Agent Onboarding.md'):
        if required not in files:
            errors.append(f'root: missing entry {required}')
    metas, texts, bodies, parents, links = {}, {}, {}, {}, {}
    incoming = defaultdict(list)
    capture_ids = defaultdict(list)

    def resolve(target, source):
        # Full vault-relative paths are preferred. Bare names resolve only if unique.
        target = unicodedata.normalize('NFC', target.strip())
        if not target:
            return source
        if target.startswith('/') or '..' in PurePosixPath(target).parts:
            return None
        candidates = [target] if PurePosixPath(target).suffix else [target + '.md', target]
        for candidate in candidates:
            if candidate in files:
                return candidate
        if '/' not in target:
            matched = [name for name in files if PurePosixPath(name).name == target
                       or (not PurePosixPath(target).suffix and PurePosixPath(name).stem == target)]
            if len(matched) == 1:
                return matched[0]
        return None

    for rel, p in sorted(files.items()):
        if p.suffix.lower() != '.md':
            continue
        try:
            text = p.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'{rel}: Markdown is not valid UTF-8')
            continue
        texts[rel] = text
        if raw_asset(rel):
            continue
        try:
            meta, body = frontmatter(text)
            metas[rel], bodies[rel] = meta, body
        except (ValueError, yaml.YAMLError, TypeError):
            errors.append(f'{rel}: invalid or missing YAML frontmatter')
            continue
        for key in sorted(REQUIRED - set(meta)):
            errors.append(f'{rel}: missing property {key}')
        for key in ('type', 'status'):
            if key in meta and (not isinstance(meta[key], str) or not meta[key].strip()):
                errors.append(f'{rel}: {key} must be a non-empty string')
        for key in ('tags', 'aliases'):
            if key in meta and (not isinstance(meta[key], list) or any(not isinstance(x, str) for x in meta[key])):
                errors.append(f'{rel}: {key} must be a list of strings')
        updated = meta.get('updated')
        try:
            if isinstance(updated, datetime):
                raise ValueError()
            date.fromisoformat(str(updated))
        except (ValueError, TypeError):
            errors.append(f'{rel}: updated must be an ISO date')
        is_template = rel.startswith(TEMPLATE) and rel != TEMPLATE + 'Templates Hub.md'
        if not is_template and TOKEN.search(text):
            errors.append(f'{rel}: unresolved template token')
        if rel == 'Vault Hub.md':
            if meta.get('type') != 'hub':
                errors.append(f'{rel}: root must have type hub')
            if 'hub' in meta:
                errors.append(f'{rel}: root must not have a parent')
        else:
            hub = meta.get('hub')
            match = re.fullmatch(r'\[\[([^\]|#]+)\]\]', hub) if isinstance(hub, str) else None
            if not match:
                errors.append(f'{rel}: hub must be one path-qualified wikilink')
            else:
                target = resolve(match.group(1), rel)
                if not target:
                    errors.append(f'{rel}: parent Hub does not resolve')
                elif '/' not in match.group(1) and target != 'Vault Hub.md':
                    errors.append(f'{rel}: parent Hub must use its full vault path')
                else:
                    parents[rel] = target
        cid = meta.get('capture_id')
        if cid is not None:
            if not isinstance(cid, str) or not cid.strip():
                errors.append(f'{rel}: capture_id must be a non-empty string')
            else:
                capture_ids[cid].append(rel)
        scan = without_fences(text)
        links[rel] = []
        for match in WIKI.finditer(scan):
            specification = match.group(1).split('|', 1)[0]
            target, sep, fragment = specification.partition('#')
            resolved = resolve(target, rel)
            if not resolved:
                errors.append(f'{rel}: unresolved or ambiguous wikilink target {target}')
                continue
            incoming[resolved].append((rel, target))
            links[rel].append(resolved)
            if sep:
                content = files[resolved].read_text(encoding='utf-8') if resolved.endswith('.md') else ''
                if fragment.startswith('^'):
                    if not re.search(r'(?:^|\s)\^' + re.escape(fragment[1:]) + r'(?:\s|$)', content):
                        errors.append(f'{rel}: unresolved block reference in {resolved}')
                else:
                    headings = [clean_heading(m.group(1)) for m in re.finditer(r'^#{1,6}\s+(.+)$', without_fences(content), re.M)]
                    if clean_heading(fragment) not in headings:
                        errors.append(f'{rel}: unresolved heading in {resolved}')
    for rel, parent in parents.items():
        if metas.get(parent, {}).get('type') != 'hub':
            errors.append(f'{rel}: parent target is not a maintained Hub')
        if rel not in links.get(parent, []):
            errors.append(f'{rel}: not registered in its parent Hub')
        seen, current = set(), rel
        while current != 'Vault Hub.md':
            if current in seen:
                errors.append(f'{rel}: cycle in Hub ancestry')
                break
            seen.add(current)
            current = parents.get(current)
            if current is None:
                errors.append(f'{rel}: ancestry does not reach Vault Hub')
                break
    for members in capture_ids.values():
        if len(members) > 1:
            errors.append('capture_id: duplicate envelope ownership in ' + ', '.join(members))
    for rel in files:
        if rel.endswith('.md') and not raw_asset(rel):
            continue
        if not any(PurePosixPath(target).suffix for _, target in incoming[rel]):
            errors.append(f'{rel}: source asset needs a governing link with explicit extension')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('vault', type=Path)
    parser.add_argument('--template', action='store_true', help='Audit the bundled scaffold without .obsidian.')
    args = parser.parse_args()
    try:
        errors = audit(args.vault, args.template)
    except OSError:
        print('Audit could not read all scoped paths.', file=sys.stderr)
        return 2
    for error in errors:
        print(error)
    print(f'{len(errors)} structural finding(s). Semantic correctness and live app behavior are not verified.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
