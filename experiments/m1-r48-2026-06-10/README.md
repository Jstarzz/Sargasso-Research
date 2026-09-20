# Model 1 R48: Warm resume on geometrically guarded labels

**Date:** 2026-06-10 · **Status:** COMPLETED · **Outcome:** mixed

Warm resume on geometrically guarded labels. Historical disposition: KEPT as checkpoint, NOT promoted .

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.3363 | Historical validation split; guarded labels only for R48/R49 |
| guarded_tta_test_iou | 0.6287 | TTA threshold 0.60 and land mask; not promoted |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.
- Subsequent July repair showed residual inland contamination remained in its training labels.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
