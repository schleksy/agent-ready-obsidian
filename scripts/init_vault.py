#!/usr/bin/env python3
"""Preview/create a new vault. Never migrate or overwrite existing content."""
import argparse
from datetime import date
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'vault-template'


def checked_destination(value: str) -> Path:
    raw = Path(value).expanduser()
    if not raw.is_absolute():
        raise ValueError('Destination must be an absolute path.')
    if any(p.is_symlink() for p in (raw, *raw.parents)):
        raise ValueError('Destination and its parents must not be symlinks.')
    dest = raw.resolve()
    if dest == ROOT or ROOT in dest.parents:
        raise ValueError('Keep the private vault outside the public repository.')
    if dest == Path(dest.anchor) or dest == Path.home():
        raise ValueError('Choose a dedicated vault directory, not a filesystem or home root.')
    if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
        raise ValueError('Destination must be absent or an empty directory; existing vaults require migration.')
    for source in SOURCE.rglob('*'):
        if source.is_symlink():
            raise ValueError('Starter contains a symlink; refusing to copy it.')
    return dest


def initialize(value: str, apply: bool = False) -> int:
    dest = checked_destination(value)
    files = sorted(p for p in SOURCE.rglob('*') if p.is_file())
    if not apply:
        print(f'PREVIEW ONLY: {len(files)} starter files plus an empty .obsidian directory.')
        print(f'Destination: {dest}')
        print('No files changed. Add --apply after reviewing the plan.')
        return len(files)
    dest.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.vault-stage-', dir=dest.parent))
    try:
        for source in files:
            target = stage / source.relative_to(SOURCE)
            target.parent.mkdir(parents=True, exist_ok=True)
            content = source.read_text(encoding='utf-8')
            if content.startswith('---\n'):
                head, body = content[4:].split('\n---\n', 1)
                head = '\n'.join('updated: ' + date.today().isoformat()
                                 if line.startswith('updated: ') else line
                                 for line in head.splitlines())
                content = '---\n' + head + '\n---\n' + body
            target.write_text(content, encoding='utf-8')
        (stage / '.obsidian').mkdir()
        # Check again after preparing. Never copy into an existing non-empty target.
        checked_destination(value)
        if dest.exists():
            dest.rmdir()  # succeeds only for the confirmed empty directory
        os.rename(stage, dest)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    print(f'Created {len(files)} starter files at {dest}.')
    print('Personalization, platform onboarding, app rendering, sync, and backup are not yet verified.')
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', required=True)
    parser.add_argument('--apply', action='store_true', help='Create after the preview has been reviewed.')
    args = parser.parse_args()
    try:
        initialize(args.destination, args.apply)
        return 0
    except (ValueError, OSError) as exc:
        print(f'Refused: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
