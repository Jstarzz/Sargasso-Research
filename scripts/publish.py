#!/usr/bin/env python3
"""Validate and render curated public research. No network access or git push."""
from __future__ import annotations
import argparse
import datetime as dt
import json
import math
import re
import shutil
import tempfile
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = frozenset({'experiment.json', 'config.json', 'README.md', 'results.json', 'metrics.json', 'evidence.md'})
SECRET = re.compile(r'-----BEGIN .*PRIVATE KEY-----|\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|\bgh[pousr]_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}', re.I)
ID = re.compile(r'[a-z0-9][a-z0-9_-]*\Z')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def safe_path(root, relative):
    require(not root.is_symlink(), 'Root symlink forbidden')
    if hasattr(root, 'is_junction'):
        require(not root.is_junction(), 'Root junction forbidden')
    require(isinstance(relative, str) and '\\' not in relative, 'Use relative POSIX paths')
    parts = PurePosixPath(relative)
    require(not parts.is_absolute() and bool(parts.parts) and all(x not in ('.', '..') and ':' not in x for x in parts.parts), 'Unsafe path')
    path = root
    for part in parts.parts:
        path = path / part
        require(not path.is_symlink(), f'Symlink forbidden: {path}')
        if hasattr(path, 'is_junction'):
            require(not path.is_junction(), f'Junction forbidden: {path}')
    require(path.resolve().is_relative_to(root.resolve()), 'Path escapes root')
    return path

def read_json(path):
    raw = path.read_text(encoding='utf-8-sig')
    require(not SECRET.search(raw), f'Potential secret: {path.name}')
    return json.loads(raw)

def nonempty(value):
    return isinstance(value, str) and bool(value.strip())

def common(record):
    require(isinstance(record, dict), 'Record must be an object')
    require(isinstance(record.get('id'), str) and ID.fullmatch(record['id']), 'Invalid id')
    for key in ('title', 'scope'):
        require(nonempty(record.get(key)), f'{record["id"]}: missing {key}')
    date = record.get('date')
    if date is None:
        require(nonempty(record.get('date_note')), 'Unknown date requires date_note')
    else:
        require(isinstance(date, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}', date), 'Date must be YYYY-MM-DD')
        dt.date.fromisoformat(date)
    require(record.get('status') in ('completed', 'in_progress'), 'Invalid status')

def evidence(records):
    require(isinstance(records, list) and records, 'Completed evidence must be nonempty')
    for item in records:
        require(isinstance(item, dict) and nonempty(item.get('summary')), 'Evidence needs public summary')
        if 'source_path' in item:
            source = item['source_path']
            require(isinstance(source, str) and not PurePosixPath(source).is_absolute() and '..' not in PurePosixPath(source).parts and ':' not in source and '\\' not in source, 'Evidence path must be sanitized relative provenance, never a private link')
        if item.get('sha256') is not None:
            require(bool(re.fullmatch(r'[a-fA-F0-9]{64}', item['sha256'])), 'Invalid SHA-256')
        if item.get('commit') is not None:
            require(bool(re.fullmatch(r'[a-fA-F0-9]{7,40}', item['commit'])), 'Invalid commit')
        if 'public_url' in item:
            url(item['public_url'])

def url(value):
    parsed = urlparse(value)
    require(parsed.scheme in ('https', 'http') and bool(parsed.netloc) and not parsed.username and not parsed.password, 'Invalid public URL')

def experiment(record):
    common(record)
    require(record.get('schema_version') == 1 and record['status'] == 'completed', 'Only completed experiment bundles may publish')
    require(nonempty(record.get('summary')), 'Experiment needs summary')
    require(record.get('outcome') in ('positive', 'negative', 'mixed', 'inconclusive'), 'Experiment outcome required')
    require(isinstance(record.get('limitations'), list) and record['limitations'] and all(nonempty(x) for x in record['limitations']), 'Explicit limitations required')
    evidence(record.get('evidence'))
    require(isinstance(record.get('metrics'), list), 'Metrics must be a list; empty is allowed for qualitative outcomes')
    for metric in record['metrics']:
        require(isinstance(metric, dict) and nonempty(metric.get('name')), 'Metric needs name')
        value = metric.get('value')
        require(isinstance(value, (str, int, float)) and not isinstance(value, bool), 'Metric needs scalar value')
        require(not isinstance(value, float) or math.isfinite(value), 'Nonfinite metric')
        require(nonempty(metric.get('provenance')) or nonempty(metric.get('scope')), 'Metric requires provenance or evidence-qualified scope')
    require(isinstance(record.get('citations'), list), 'Citations must be a list')
    for citation in record['citations']:
        require(nonempty(citation.get('title')), 'Citation title missing')
        url(citation['url'])

def inspect_bundle(folder):
    require(folder.is_dir() and not folder.is_symlink(), 'Bundle must be a real directory')
    if hasattr(folder, 'is_junction'):
        require(not folder.is_junction(), 'Bundle junction forbidden')
    for item in folder.iterdir():
        require(item.name in ALLOWED and item.is_file() and not item.is_symlink(), f'Unapproved bundle file: {item.name}')
        require(item.stat().st_size <= 2_000_000, f'Curated text file too large: {item.name}')
        raw = item.read_text(encoding='utf-8-sig')
        require(not SECRET.search(raw), f'Potential secret: {item.name}')
        if item.suffix == '.json':
            read_json(item)
        if item.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', raw):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                require(safe_path(folder, target.split('#')[0]).is_file(), f'Broken/nonlocal bundle link: {target}')
    record = read_json(folder / 'experiment.json')
    experiment(record)
    return record

def load(root):
    registry = read_json(safe_path(root, 'registry/timeline.json'))
    require(isinstance(registry, dict) and registry.get('schema_version') == 1 and isinstance(registry.get('entries'), list), 'Invalid registry')
    seen, records = set(), {}
    folder = safe_path(root, 'experiments')
    if folder.exists():
        for path in sorted(folder.iterdir()):
            safe_path(root, path.relative_to(root).as_posix())
            record = inspect_bundle(path)
            require(path.name == record['id'], 'Experiment folder/id mismatch')
            records[record['id']] = record
    for entry in registry['entries']:
        common(entry)
        require(entry['id'] not in seen, 'Duplicate timeline id')
        seen.add(entry['id'])
        if entry['status'] == 'in_progress':
            require(set(entry) <= {'id','title','status','date','date_note','scope','category'}, 'In-progress entries cannot publish unfinished results or evidence')
        else:
            evidence(entry.get('evidence'))
            for ident in entry.get('experiment_ids', []):
                require(ident in records, f'Unknown experiment: {ident}')
            if 'experiment_path' in entry:
                target = safe_path(root, entry['experiment_path'])
                require(target.is_file() and target.name == 'experiment.json' and target.parent.name in records, 'Invalid experiment link')
    return registry['entries'], records

def escape(value):
    return str(value).replace('|', '\\|').replace('\r', ' ').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')

def render(root):
    entries, records = load(root)
    timeline = ['# Research timeline', '', 'Generated from curated public records. Unknown dates are explicitly marked. IN PROGRESS entries describe scope only.', '']
    ordered = sorted(entries, key=lambda x: (x.get('date') is None, x.get('date') or '', x['id']))
    undated_started = False
    timeline += ['## Dated milestones', '']
    for entry in ordered:
        if entry.get('date') is None and not undated_started:
            timeline += ['## Undated records', '', 'These records have no established date. Their placement here implies no chronological order relative to dated milestones.', '']
            undated_started = True
        date = entry.get('date') or f'Undated ({escape(entry["date_note"])})'
        timeline += [f'### {date} — {escape(entry["title"])}', '', f'**{entry["status"].upper().replace("_", " ")}** · {escape(entry["scope"])}', '']
        if entry['status'] == 'completed':
            if entry.get('summary'):
                timeline += [escape(entry['summary']), '']
            for ident in entry.get('experiment_ids', []):
                timeline += [f'- [{escape(records[ident]["title"])}](experiments/{ident}/experiment.json)']
            timeline += ['', '**Provenance**', '']
            for item in entry['evidence']:
                details = [escape(item['summary'])]
                if item.get('source_path'):
                    details += [f'Source label: `{escape(item["source_path"])}` (private historical source; provenance only)']
                if item.get('sha256'):
                    details += [f'SHA-256: `{item["sha256"]}`']
                if item.get('commit'):
                    details += [f'Source commit: `{item["commit"]}`']
                if item.get('public_url'):
                    details += [f'[Public source]({item["public_url"]})']
                timeline += ['- ' + '; '.join(details)]
            timeline += ['']
    index = ['# Completed experiments', '', 'Historical research evidence; metrics are meaningful only within their stated scope and limitations.', '', '| Experiment | Date | Outcome | Scope |', '|---|---|---|---|']
    for ident, record in sorted(records.items(), key=lambda p: (p[1].get('date') or '0000', p[0])):
        index += [f'| [{escape(record["title"])}](experiments/{ident}/experiment.json) | {record.get("date") or "Undated"} | {record["outcome"]} | {escape(record["scope"])} |']
    index += ['']
    return {'TIMELINE.md': '\n'.join(timeline).rstrip()+'\n', 'EXPERIMENTS.md': '\n'.join(index)}

def build(root, check=False):
    require(not safe_path(root, '.publish-import.lock').exists(), 'Import lock present; wait for import to finish before building')
    for name, content in render(root).items():
        path = safe_path(root, name)
        if check:
            require(path.exists() and path.read_text(encoding='utf-8') == content, f'{name} is stale; run build')
        else:
            path.write_text(content, encoding='utf-8', newline='\n')

def import_bundle(root, source, selected):
    require(set(selected) <= ALLOWED and 'experiment.json' in selected and len(set(selected)) == len(selected), 'Explicit file allowlist required, including experiment.json')
    record = inspect_bundle(source)
    require(set(selected) == {p.name for p in source.iterdir()}, 'Select every reviewed bundle file explicitly; extra files are not silently copied')
    destination = safe_path(root, f'experiments/{record["id"]}')
    registry_path = safe_path(root, 'registry/timeline.json')
    lock = safe_path(root, '.publish-import.lock')
    # Exclusive import lock; every candidate is validated before public files change.
    # Each replacement is atomic, with rollback on exceptions. This is not a
    # crash-proof filesystem-wide transaction; inspect the lock after power loss.
    with lock.open('x', encoding='utf-8') as handle:
        handle.write('Curated import in progress; do not run concurrent builds/imports.\n')
    try:
        entries, _ = load(root)
        require(not destination.exists(), 'Destination already exists')
        require(record['id'] not in {entry['id'] for entry in entries}, 'Timeline id already exists')
        registry = read_json(registry_path)
        entry = {key: record[key] for key in ('id','title','status','date','scope','summary','evidence')}
        if record.get('date_note'):
            entry['date_note'] = record['date_note']
        entry['experiment_ids'] = [record['id']]
        registry['entries'].append(entry)
        with tempfile.TemporaryDirectory(prefix='.publish-stage-', dir=root) as temporary:
            stage = Path(temporary)
            (stage/'registry').mkdir()
            staged_registry = stage/'registry/timeline.json'
            staged_registry.write_text(json.dumps(registry, indent=2, ensure_ascii=False)+'\n', encoding='utf-8', newline='\n')
            if (root/'experiments').exists():
                shutil.copytree(root/'experiments', stage/'experiments')
            else:
                (stage/'experiments').mkdir()
            staged_bundle = stage/'experiments'/record['id']
            staged_bundle.mkdir()
            for name in selected:
                shutil.copyfile(safe_path(source, name), staged_bundle/name)
            build(stage)
            targets = [registry_path, safe_path(root, 'TIMELINE.md'), safe_path(root, 'EXPERIMENTS.md')]
            backups = {target: target.read_bytes() if target.exists() else None for target in targets}
            moved = False
            replaced = []
            try:
                destination.parent.mkdir(exist_ok=True)
                staged_bundle.replace(destination)
                moved = True
                for target in targets:
                    staged = stage/target.relative_to(root)
                    staged.replace(target)
                    replaced.append(target)
            except BaseException:
                for target in reversed(replaced):
                    if backups[target] is None:
                        target.unlink(missing_ok=True)
                    else:
                        restore = stage/('restore-'+target.name)
                        restore.write_bytes(backups[target])
                        restore.replace(target)
                if moved:
                    destination.replace(staged_bundle)
                raise
    finally:
        lock.unlink(missing_ok=True)
    return destination

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    commands = parser.add_subparsers(dest='command', required=True)
    for action in ('validate', 'build', 'check'):
        commands.add_parser(action)
    importer = commands.add_parser('import')
    importer.add_argument('source', type=Path)
    importer.add_argument('--files', nargs='+', required=True, choices=sorted(ALLOWED))
    scaffold = commands.add_parser('scaffold')
    scaffold.add_argument('id')
    scaffold.add_argument('--output', type=Path, required=True, help='Review staging directory, outside experiments/')
    args = parser.parse_args()
    try:
        if args.command == 'validate':
            entries, records = load(args.root)
            print(f'Valid: {len(entries)} timeline entries; {len(records)} completed experiments')
        elif args.command in ('build', 'check'):
            build(args.root, args.command == 'check')
            print(args.command + ': OK')
        elif args.command == 'import':
            print(import_bundle(args.root, args.source, args.files))
        else:
            require(ID.fullmatch(args.id), 'Invalid id')
            require(not args.output.exists(), 'Output already exists')
            require(not args.output.resolve().is_relative_to((args.root/'experiments').resolve()), 'Scaffold outside published experiments')
            template = read_json(ROOT/'templates/experiment/experiment.json')
            template['id'] = args.id
            args.output.mkdir(parents=True)
            (args.output/'experiment.json').write_text(json.dumps(template, indent=2)+'\n', encoding='utf-8')
            print(f'Staged {args.output}; complete and review before import')
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, f'Validation failed: {exc}\n')

if __name__ == '__main__':
    main()
