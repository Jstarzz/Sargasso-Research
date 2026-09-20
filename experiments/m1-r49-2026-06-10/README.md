# Model 1 R49: Scratch training on guarded labels

**Date:** 2026-06-10 · **Status:** COMPLETED · **Outcome:** negative

Scratch training on guarded labels. Historical disposition: DISCARD .

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.2708 | Historical validation split; guarded labels only for R48/R49 |
| guarded_tta_test_iou | 0.5473 | TTA threshold 0.60 and land mask; discarded |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
