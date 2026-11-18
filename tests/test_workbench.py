import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        self.fixture = json.loads((ROOT / 'data/workbench.json').read_text())
        self.save()

    def save(self):
        (self.root / 'workbench.json').write_text(json.dumps(self.fixture))

    def run_action(self, action, key=None, succeeds=True):
        args = [sys.executable, '-m', 'app', action, '--data', str(self.root),
                '--ledger', str(self.root / 'receipts.sqlite3')]
        if key is not None:
            args.extend(['--key', key])
        proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, timeout=5)
        if succeeds:
            self.assertEqual(proc.returncode, 0, proc.stderr)
            return json.loads(proc.stdout)
        self.assertEqual(proc.returncode, 2, proc.stderr)
        return proc.stderr

    def test_gate_closure_updates_staffing_without_erasing_survey(self):
        self.assertEqual(self.run_action('attendance')['2026-05-01/am'], 4)
        self.assertEqual(self.run_action('staffing')['2026-05-01/am'], 'review')
        self.fixture['calendar'][0]['gates'] = ['east']
        self.save()
        self.assertEqual(self.run_action('attendance')['2026-05-01/am'], 3)
        self.assertEqual(self.run_action('staffing')['2026-05-01/am'], 'normal')
        self.assertEqual(self.run_action('survey', '2026-05-01')['f2'], {'invited': 2, 'replies': 1})
