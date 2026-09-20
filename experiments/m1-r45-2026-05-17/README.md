# Model 1 R45: Updated pseudo-labels and exclusions; extended warm resume

**Date:** 2026-05-17 · **Status:** COMPLETED · **Outcome:** negative

Updated pseudo-labels and exclusions; extended warm resume. Historical disposition: discard .

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.3469 | Historical validation split; guarded labels only for R48/R49 |
| test_iou | 0.511 | Legacy unguarded selected-patch test protocol |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
