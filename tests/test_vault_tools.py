"""Synthetic regression tests. No user's live vault is read or uploaded."""
import contextlib
import io
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_vault import audit
from init_vault import ROOT, SOURCE, checked_destination, initialize
from privacy_scan import scan
from check_repo import check, check_skill, check_workflow


class VaultToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name).resolve()
        self.vault = self.base / 'vault'
        shutil.copytree(SOURCE, self.vault)
        (self.vault / '.obsidian').mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def write_note(self, name, parent='10 Areas/Areas Hub', extra='', body='Synthetic evidence.'):
        path = self.vault / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('---\ntype: note\nstatus: active\nupdated: 2026-01-01\ntags: []\naliases: []\n'
                        + f'hub: "[[{parent}]]"\n' + extra + '---\n\n# Synthetic\n\n' + body, encoding='utf-8')
        with (self.vault / (parent + '.md')).open('a', encoding='utf-8') as p:
            p.write('\n[[' + name.removesuffix('.md') + ']]\n')
        return path

    def test_starter_and_generated_docs_are_consistent(self):
        self.assertEqual(check(), [])
        self.assertEqual(audit(self.vault), [])

    def test_preview_makes_no_destination(self):
        dest = self.base / 'new'
        with contextlib.redirect_stdout(io.StringIO()):
            initialize(str(dest))
        self.assertFalse(dest.exists())

    def test_initializer_creates_valid_new_vault(self):
        dest = self.base / 'new'
        with contextlib.redirect_stdout(io.StringIO()):
            initialize(str(dest), True)
        self.assertEqual(audit(dest), [])

    def test_initializer_refuses_existing_nonempty_and_preserves_bytes(self):
        before = (self.vault / 'Vault Hub.md').read_bytes()
        with self.assertRaises(ValueError):
            initialize(str(self.vault), True)
        self.assertEqual((self.vault / 'Vault Hub.md').read_bytes(), before)

    def test_initializer_refuses_public_repo_destination(self):
        with self.assertRaises(ValueError):
            checked_destination(str(ROOT / 'private-test'))

    def test_initializer_refuses_symlink_parent(self):
        link = self.base / 'linked'
        try:
            link.symlink_to(self.vault, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Symlinks unavailable in this environment')
        with self.assertRaises(ValueError):
            checked_destination(str(link / 'child'))

    def test_broken_link_and_heading_are_reported(self):
        self.write_note('10 Areas/Check.md', body='[[Missing]]\n[[Vault Hub#Not a real heading]]')
        findings = '\n'.join(audit(self.vault))
        self.assertIn('unresolved or ambiguous', findings)
        self.assertIn('unresolved heading', findings)

    def test_valid_heading_and_block_resolve(self):
        self.write_note('10 Areas/Target.md', body='## Real heading\n\nAn exact block. ^sample')
        self.write_note('10 Areas/Link.md', body='[[10 Areas/Target#Real heading]]\n[[10 Areas/Target#^sample]]')
        self.assertEqual(audit(self.vault), [])

    def test_parent_cycle_is_detected(self):
        path = self.vault / '10 Areas/Areas Hub.md'
        path.write_text(path.read_text().replace('hub: "[[Vault Hub]]"', 'hub: "[[10 Areas/Areas Hub]]"'))
        self.assertTrue(any('cycle' in e for e in audit(self.vault)))

    def test_orphan_parent_registration_is_detected(self):
        self.write_note('10 Areas/Orphan.md')
        parent = self.vault / '10 Areas/Areas Hub.md'
        parent.write_text(parent.read_text().replace('[[10 Areas/Orphan]]', ''))
        self.assertTrue(any('not registered' in e for e in audit(self.vault)))

    def test_duplicate_capture_ids_include_archive(self):
        self.write_note('00 Inbox/Agent Inbox/Capture.md', parent='00 Inbox/Agent Inbox/Agent Inbox', extra='capture_id: synthetic-message-1\n')
        self.write_note('90 Archive/Agent Inbox Processed/Capture.md', parent='90 Archive/Agent Inbox Processed/Processed Captures Hub', extra='capture_id: synthetic-message-1\n')
        self.assertTrue(any('duplicate envelope' in e for e in audit(self.vault)))

    def test_raw_source_does_not_require_frontmatter_but_needs_wrapper_link(self):
        raw = self.vault / '40 Resources/Sources/evidence.md'
        raw.parent.mkdir(parents=True)
        raw.write_bytes(b'Original bytes, no metadata.\n')
        self.assertTrue(any('explicit extension' in e for e in audit(self.vault)))
        self.write_note('40 Resources/Guide.md', parent='40 Resources/Resources Hub', body='[[40 Resources/Sources/evidence.md]]')
        self.assertEqual(audit(self.vault), [])
        self.assertEqual(raw.read_bytes(), b'Original bytes, no metadata.\n')

    def test_duplicate_yaml_key_is_rejected(self):
        self.write_note('10 Areas/Duplicate.md', extra='status: pending\n')
        self.assertTrue(any('invalid or missing YAML' in e for e in audit(self.vault)))

    def test_unresolved_template_token_outside_template_is_rejected(self):
        self.write_note('10 Areas/Unfilled.md', body='{{UNFILLED}}')
        self.assertTrue(any('unresolved template token' in e for e in audit(self.vault)))

    def test_privacy_findings_do_not_echo_secret(self):
        folder = self.base / 'public'
        folder.mkdir()
        secret = 'gh' + 'p_' + 'A' * 40
        (folder / 'sample.md').write_text(secret + '\nConfidential Synthetic Name\n')
        result = '\n'.join(scan(folder, ['Confidential Synthetic Name']))
        self.assertIn('github-token', result)
        self.assertIn('private-term-1', result)
        self.assertNotIn(secret, result)
        self.assertNotIn('Confidential Synthetic Name', result)

    def test_ambiguous_basename_does_not_silently_pick(self):
        self.write_note('10 Areas/Target.md')
        self.write_note('40 Resources/Target.md', parent='40 Resources/Resources Hub')
        self.write_note('10 Areas/Link.md', body='[[Target]]')
        self.assertTrue(any('ambiguous' in e for e in audit(self.vault)))

    def test_private_vault_accepts_real_personal_context(self):
        address = 'morgan' + chr(64) + 'example.test'
        self.write_note('10 Areas/People.md', extra='owner: Morgan Reed\n',
                        body='A client contact: ' + address + '\nMeeting notes and schedules belong here.')
        self.assertEqual(audit(self.vault), [])

    def test_skill_entry_requires_discoverable_metadata(self):
        folder = self.base / 'skill'
        folder.mkdir()
        (folder / 'SKILL.md').write_text('---\nname: Invalid_Name\ndescription: ""\n---\n# Entry\n')
        self.assertEqual(len(check_skill(folder)), 2)

    def test_workflow_rejects_movable_action_tag(self):
        path = self.base / 'workflow.yml'
        path.write_text('permissions: {contents: read}\njobs:\n  validate:\n    steps:\n      - uses: actions/checkout@v7\n        with: {persist-credentials: false}\n')
        self.assertTrue(any('immutable' in e for e in check_workflow(path)))

    def test_workflow_rejects_write_permission_and_saved_credentials(self):
        path = self.base / 'workflow.yml'
        path.write_text('permissions: {contents: write}\njobs:\n  validate:\n    steps:\n      - uses: actions/checkout@' + 'a' * 40 + '\n')
        findings = check_workflow(path)
        self.assertTrue(any('read-only' in e for e in findings))
        self.assertTrue(any('persist' in e for e in findings))

    def test_file_symlink_is_rejected(self):
        link = self.vault / '10 Areas/linked.md'
        try:
            link.symlink_to(self.vault / 'Vault Hub.md')
        except (OSError, NotImplementedError):
            self.skipTest('Symlinks unavailable in this environment')
        self.assertTrue(any('symlink' in e for e in audit(self.vault)))


if __name__ == '__main__':
    unittest.main()
