# Provenance, licensing, and reproducibility

## Release boundary

This is a curated public research archive. No private repository history is merged into it. Only research summaries, completed aggregate results, sanitized configuration summaries, original figures, citation metadata, and archive-maintenance tools are included.

Excluded: application and serving code, deployment and infrastructure files, credentials, local machine information, raw or processed satellite scenes, training patches, model checkpoints, restricted observation records, coordinate-rich case outputs, and unfinished benchmark results. Private absolute paths and dataset identifiers are not needed to understand the released findings.

## Evidence levels

1. **Completed recorded experiment:** a dated research record reports completion and results. The public bundle includes its scope and limitations.
2. **Recorded aggregate or investigator-supplied result:** a completed summary is available, but the underlying protected cases were not independently rerun for this release. The frozen-C benchmark is explicitly in this category.
3. **Historical reconstruction:** earlier project records or commits establish a milestone. Date uncertainty, reused round names, missing runs, and differences between event dates and commit dates are stated.
4. **IN PROGRESS:** only workstream identity, scope, date/status provenance, and status are published. No partial result is a completed finding.

Literature citations acknowledge methods and external context; they are not evidence for Sargasso's own numeric claims.

## Source fingerprints

Experiment `evidence.md` and `experiment.json` records identify the source using a repository-relative research path and, where available, SHA-256 and a historical commit. These paths refer to the private source archive, not files promised to exist in this public repository. Public evidence summaries make the reported claim readable without private access.

Many later source documents were untracked working files. Their SHA-256 identifies the inspected content; a contemporaneous Git HEAD is only snapshot context and **does not version an untracked file**. No private commit is presented as an accessible public citation. After publication, the public Git commit versions the curated extract itself.

Highlight-specific fingerprints and sanitized numeric extracts are in [evidence/highlight-sources.json](../evidence/highlight-sources.json). Exact source fingerprints support provenance, not independent reproduction or external validation.

## Chronology coverage

The timeline aims to include the full **documented, recoverable** chronology, rather than only promoted models. Missing records are explicit. A skipped round identifier does not establish that an experiment ran. Repeated identifiers remain separate records when the source distinguishes them. Contemporary records take precedence over stale status statements, and later methodological qualifications remain attached to historical scores.

## Licensing and data availability

The repository's existing [LICENSE](../LICENSE) licenses original research results, figures, reports, documentation, and artifacts under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). This release preserves that choice. It does not grant rights to third-party materials.

| Material | Public release policy |
| --- | --- |
| Original summaries, aggregate tables, figures, and publication utilities | Included under the repository license |
| Satellite imagery and derived training patches | Not included; obtain original inputs from their providers under the applicable terms |
| Internal weak labels, curated scene lists, and model weights | Not distributed in this release |
| Restricted-source benchmark observations and per-case outputs | Not distributed; only qualified completed aggregate findings are published |
| Putman rolling GPS cases and 2018 GLORYS forcing | Not redistributed here; current work remains in progress |
| Published papers and third-party software | Cited, not relicensed or bundled |

Sentinel inputs originate with the Copernicus programme. Consult the provider's [data access information](https://www.copernicus.eu/en/terms-use/how-access-data) and [Sentinel legal notice](https://cds.climate.copernicus.eu/licences/ec-sentinel). Open access to upstream inputs does not settle the rights or release status of every derived dataset. Attribution and redistribution terms must be reviewed for each future artifact.

## Authorship

Primary author: **Josiah Davis**, affiliation **Sargasso**. Add authors only for substantive research contributions; do not substitute a group author for the primary researcher. The repository [CITATION.cff](../CITATION.cff) is the canonical citation metadata. No DOI, external peer review, institutional endorsement, or third-party validation is claimed for this archive.
