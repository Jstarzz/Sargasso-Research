# Model 1 R46: Remove pseudo-labels and expand exclusions

**Date:** 2026-05-19 · **Status:** COMPLETED · **Outcome:** positive

Remove pseudo-labels and expand exclusions. Historical disposition: KEPT .

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.3473 | Historical validation split; guarded labels only for R48/R49 |
| test_iou | 0.5161 | Legacy unguarded selected-patch test protocol |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
