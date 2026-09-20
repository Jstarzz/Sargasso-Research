# Completed experiment staging template

Use `python scripts/publish.py scaffold example-id --output PATH` to create a staging record outside `experiments/`. The blank template deliberately fails validation until it is completed.

Required experiment fields: schema_version (1), id, title, status (`completed`), date (`YYYY-MM-DD` or null with date_note), summary, scope, outcome (`positive`, `negative`, `mixed`, `inconclusive`), metrics, limitations, evidence, citations.

Metrics require name, scalar value, and provenance or an evidence-qualified scope. Limitations must be explicit. Evidence requires a public summary; optional source_path is a sanitized relative provenance label, not a clickable private proof link. Optional SHA-256 and commit identify historical sources without publishing them. Citations are titled public HTTP(S) links. Empty metric and citation lists are allowed for qualitative outcomes. Unknown dates stay unknown.

Review every file for privacy and scope. The importer allows only explicitly selected experiment.json, config.json, README.md, results.json, metrics.json, and evidence.md. Each is curated text up to 2 MB. No datasets, checkpoints, code, infrastructure, subdirectories, or symlinks are accepted. Pattern scanning catches some obvious credentials, but never substitutes for human review of curated content.

`python scripts/publish.py import PATH --files experiment.json config.json README.md`

Add a timeline entry, then run `validate`, `build`, and `check`. Nothing pushes to GitHub. IN PROGRESS timeline entries contain only id/title/status/date/date_note/scope/category; no unfinished metrics, results, evidence, or experiment links.
