# Model 1 R43: Pseudo-label mixing 0.25 with conservative thresholds

**Date:** 2026-05-16 · **Status:** COMPLETED · **Outcome:** positive

Pseudo-label mixing 0.25 with conservative thresholds. Historical disposition: KEPT .

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.3451 | Historical validation split; guarded labels only for R48/R49 |
| test_iou | 0.5039 | Legacy unguarded selected-patch test protocol |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
