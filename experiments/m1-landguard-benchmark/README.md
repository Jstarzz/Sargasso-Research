# Land-guarded detection benchmark

**Date:** 2026-06-10 · **Status:** COMPLETED · **Outcome:** positive

Land-guarded labels plus masked R46/R47 ensemble and four-pass TTA at 0.60 yielded recorded IoU 0.6440; unmasked inference on guarded labels yielded 0.4692. Selection and threshold tuning reused test evidence.

| Metric | Value | Scope |
|---|---:|---|
| guarded_masked_iou | 0.644 | Historical selected-patch test; 5,000 patches, reported 173 scenes |
| guarded_unmasked_iou | 0.4692 | Same recorded guarded-label comparison |
| inland_positive_fraction | 0.351 | Original test-label positives at least 100 m inland |

## Interpretation

- Historical selected-patch/test-tuned result, not unbiased serving accuracy.
- Exact original guarded image/label/mask/probability package is unavailable; public release cannot independently replay 0.6440.
- Gold review was prediction-exposed and must not be called independent corroboration.
- 173 versus 174 scenes in historical records remains unresolved.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
