# Model 1 R42: Filtered 17,447-patch training set; warm resume

**Date:** 2026-05-15 · **Status:** COMPLETED · **Outcome:** positive

Filtered 17,447-patch training set; warm resume. Historical disposition: KEPT.

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.3228 | Historical validation split; guarded labels only for R48/R49 |
| test_iou | 0.474 | Legacy unguarded selected-patch test protocol |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
