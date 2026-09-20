# Publish a completed experiment

The publisher curates research bundles and regenerates the chronological timeline and experiment index. It never trains a model, retrieves private data, publishes to GitHub, or copies a private repository. Python 3.10+ is sufficient for archive maintenance; Matplotlib is optional for recreating the release figures.

## 1. Prepare a review bundle

Work outside `experiments/` until the run is complete and the public material has been reviewed:

```bash
python scripts/publish.py scaffold new-experiment-id --output ../research-review/new-experiment-id
```

Complete `experiment.json`. Use the [template](../templates/experiment/experiment.json) and [summary template](../templates/experiment/README.md). Keep the ID stable and use a distinct ID when historical round names were reused.

Required research metadata includes a title, completed status, date or an explicit uncertainty note, scope, summary, outcome, limitations, evidence, citations, and any published metrics. Each metric needs its meaning and provenance or evaluation scope. A completed negative or inconclusive experiment belongs in the archive.

Add only reviewed files from this allowlist:

- `experiment.json`: canonical metadata and aggregate metrics.
- `README.md`: question, method, result, interpretation, and limitations.
- `config.json`: sanitized research parameters; identify partial configurations explicitly.
- `evidence.md`: public evidence summary with source references and fingerprints.
- `metrics.json` or `results.json`: optional completed aggregate outputs.

Record provider citations and redistribution terms for any new data source. Never include scene-level records, coordinates, imagery, arrays, weights, raw logs, product code, deployment files, credentials, or private absolute paths. A successful automated check does not establish that arbitrary text or a derived dataset is safe to publish.

## 2. Import and update automatically

List **every** reviewed file explicitly:

```bash
python scripts/publish.py import ../research-review/new-experiment-id --files experiment.json README.md config.json evidence.md
```

The importer validates the completed bundle, adds its dated event to `registry/timeline.json`, and regenerates `TIMELINE.md` and `EXPERIMENTS.md`. It refuses an existing experiment ID or unsafe path. It does not overwrite an existing experiment. Failed validation must leave the published archive unchanged.

Figures and their small aggregate plotting tables require a separate, deliberate review in `figures/` and `results/`; the bundle importer does not copy arbitrary binaries or data folders. Include a reproducible plotting script and link the figure from the research summary once reviewed.

## 3. Check and review the release diff

```bash
python scripts/publish.py validate
python scripts/publish.py build
python scripts/publish.py check
python -m unittest discover -s tests
git diff --check
git diff --stat
```

Review the full Git diff for research-only scope, correct attribution, supported claims, private information, and data licensing. Ensure every numeric claim is attached to the right cohort and protocol. Review the figures visually. Commit and push only the reviewed changes; the script never pushes automatically.

## Timeline milestones and work in progress

Non-experiment milestones belong in `registry/timeline.json`. Include evidence and an honest date/date note. Run `build` after editing this registry; `check` fails when generated pages are stale. Unknown dates are shown separately rather than assigned an invented date.

An **IN PROGRESS** event is restricted to identity, date/status provenance, and scope. It must not contain summaries of outcomes, metric values, or links to unfinished result artifacts. When the study completes, review and import a completed bundle and update the old in-progress status record so it no longer implies active work. Do not leave simultaneous current and completed status claims.

## Provenance and citation

Use source-relative research paths rather than machine paths. Hash the exact source bytes. Only attach a commit as the source revision if that commit actually contains those bytes; untracked files need snapshot hashes without a false commit attribution. The curated public evidence file is what readers can access and cite.

Update [CITATION.cff](../CITATION.cff) for a new archive release date/version, keeping **Josiah Davis** as primary author and **Sargasso** as affiliation. Add other authors only for substantive research contributions. Do not create a DOI or suggest peer review that does not exist.

The CI workflow runs the publisher checks and tests on proposed changes. The public content boundary and original license are documented in [PROVENANCE.md](PROVENANCE.md).
