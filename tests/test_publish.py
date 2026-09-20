import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('publish', Path(__file__).resolve().parents[1]/'scripts/publish.py')
publish = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish)

class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'registry').mkdir()
        self.entry = {'id':'test','title':'Test','status':'in_progress','date':None,'date_note':'Unrecorded','scope':'Research scope'}
        self.write_registry()

    def write_registry(self):
        (self.root/'registry/timeline.json').write_text(json.dumps({'schema_version':1,'entries':[self.entry]}), encoding='utf-8')

    def test_deterministic_build_and_stale_check(self):
        publish.build(self.root)
        original = (self.root/'TIMELINE.md').read_bytes()
        publish.build(self.root)
        self.assertEqual(original, (self.root/'TIMELINE.md').read_bytes())
        publish.build(self.root, True)
        (self.root/'TIMELINE.md').write_text('stale')
        with self.assertRaises(ValueError): publish.build(self.root, True)

    def test_in_progress_cannot_leak_results(self):
        for field in ('metrics','results','summary','evidence','experiment_ids'):
            self.entry[field] = ['unfinished']
            self.write_registry()
            with self.assertRaises(ValueError): publish.load(self.root)
            del self.entry[field]

    def test_traversal_rejected(self):
        for path in ('../private','/absolute','C:/private','foo/../../private','foo\\private'):
            with self.assertRaises(ValueError): publish.safe_path(self.root, path)

    def test_symlink_rejected(self):
        try: (self.root/'linked').symlink_to(self.root/'registry', target_is_directory=True)
        except OSError: self.skipTest('Symlinks unavailable on this host')
        with self.assertRaises(ValueError): publish.safe_path(self.root, 'linked/timeline.json')

    def test_unknown_dates_need_note(self):
        self.entry.pop('date_note')
        with self.assertRaises(ValueError): publish.common(self.entry)

    def test_private_bundle_file_rejected(self):
        folder = self.root/'bundle'
        folder.mkdir()
        (folder/'checkpoint.pt').write_bytes(b'private')
        with self.assertRaises(ValueError): publish.inspect_bundle(folder)

    def test_secret_rejected(self):
        path = self.root/'secret.json'
        path.write_text(json.dumps({'key':'AKIA'+'A'*16}))
        with self.assertRaises(ValueError): publish.read_json(path)

    def make_bundle(self):
        folder = self.root/'bundle'
        folder.mkdir()
        record = dict(self.entry, id='completed-result', schema_version=1, status='completed', summary='Negative result retained', outcome='negative', metrics=[{'name':'IoU difference','value':-0.01,'scope':'Development cases only'}], limitations=['Small development cohort'], evidence=[{'summary':'Reviewed historical log', 'source_path':'logs/research.log', 'sha256':'a'*64}], citations=[])
        (folder/'experiment.json').write_text(json.dumps(record), encoding='utf-8')
        return folder

    def test_negative_result_import_and_no_overwrite(self):
        source = self.make_bundle()
        destination = publish.import_bundle(self.root, source, ['experiment.json'])
        self.assertTrue((destination/'experiment.json').exists())
        entries, records = publish.load(self.root)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[-1]['experiment_ids'], ['completed-result'])
        self.assertIn('completed-result', (self.root/'EXPERIMENTS.md').read_text(encoding='utf-8'))
        publish.build(self.root, True)
        with self.assertRaises(ValueError): publish.import_bundle(self.root, source, ['experiment.json'])

    def test_import_duplicate_timeline_id_changes_nothing(self):
        source = self.make_bundle()
        self.entry['id'] = 'completed-result'
        self.write_registry()
        before = (self.root/'registry/timeline.json').read_bytes()
        with self.assertRaises(ValueError): publish.import_bundle(self.root, source, ['experiment.json'])
        self.assertEqual(before, (self.root/'registry/timeline.json').read_bytes())
        self.assertFalse((self.root/'experiments/completed-result').exists())

    def test_import_invalid_existing_state_changes_nothing(self):
        source = self.make_bundle()
        self.entry['metrics'] = [123]
        self.write_registry()
        before = (self.root/'registry/timeline.json').read_bytes()
        with self.assertRaises(ValueError): publish.import_bundle(self.root, source, ['experiment.json'])
        self.assertEqual(before, (self.root/'registry/timeline.json').read_bytes())
        self.assertFalse((self.root/'experiments/completed-result').exists())
        self.assertFalse((self.root/'.publish-import.lock').exists())

    def test_import_replacement_failure_rolls_back_all_outputs(self):
        source = self.make_bundle()
        publish.build(self.root)
        names = ['registry/timeline.json','TIMELINE.md','EXPERIMENTS.md']
        before = {name:(self.root/name).read_bytes() for name in names}
        original = Path.replace
        def fail_once(path, target):
            if path.name == 'TIMELINE.md':
                raise OSError('simulated replacement failure')
            return original(path, target)
        with patch.object(Path, 'replace', fail_once):
            with self.assertRaises(OSError): publish.import_bundle(self.root, source, ['experiment.json'])
        self.assertEqual(before, {name:(self.root/name).read_bytes() for name in names})
        self.assertFalse((self.root/'experiments/completed-result').exists())

    def test_milestone_provenance_and_undated_section(self):
        dated = dict(self.entry, id='dated', date='2026-03-28', title='Dated milestone', status='completed', evidence=[{'summary':'Public evidence summary','source_path':'docs/history.md','sha256':'a'*64,'public_url':'https://example.org/evidence'}])
        (self.root/'registry/timeline.json').write_text(json.dumps({'schema_version':1,'entries':[self.entry,dated]}))
        content = publish.render(self.root)['TIMELINE.md']
        self.assertLess(content.index('2026-03-28'), content.index('## Undated records'))
        self.assertIn('Public evidence summary', content)
        self.assertIn('[Public source](https://example.org/evidence)', content)
        self.assertIn('Source label: `docs/history.md`', content)
        self.assertNotIn('](docs/history.md)', content)

    def test_import_requires_explicit_all_files(self):
        source = self.make_bundle()
        (source/'config.json').write_text('{}')
        with self.assertRaises(ValueError): publish.import_bundle(self.root, source, ['experiment.json'])
        with self.assertRaises(ValueError): publish.import_bundle(self.root, source, ['../secret'])
        self.assertFalse((self.root/'experiments').exists())

    def test_broken_local_evidence_link_rejected(self):
        folder = self.make_bundle()
        (folder/'README.md').write_text('[private source](../../private/log.txt)')
        with self.assertRaises(ValueError): publish.inspect_bundle(folder)

    def test_nonfinite_metric_rejected(self):
        record = publish.inspect_bundle(self.make_bundle())
        record['metrics'][0]['value'] = float('nan')
        with self.assertRaises(ValueError): publish.experiment(record)

    def test_invalid_citation_rejected(self):
        record = publish.inspect_bundle(self.make_bundle())
        record['citations'] = [{'title':'Private','url':'file:///private/results'}]
        with self.assertRaises(ValueError): publish.experiment(record)

if __name__ == '__main__': unittest.main()
