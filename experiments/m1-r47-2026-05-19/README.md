# Model 1 R47: May attempt; distinct from June rerun

**Date:** 2026-05-19 · **Status:** COMPLETED · **Outcome:** negative

May attempt; distinct from June rerun. Historical disposition: discard .

| Metric | Value | Scope |
|---|---:|---|
| validation_iou | 0.3474 | Historical validation split; guarded labels only for R48/R49 |
| test_iou | 0.5163 | Legacy unguarded selected-patch test protocol |

## Interpretation

- Historical development evidence; repeated test inspection and changing cohorts prevent an unbiased serving-performance claim.
- Configurations summarize the tested delta, not an independently executable training package.
- R47 appears in May and June with different outcomes; the selected checkpoint is the June record.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
