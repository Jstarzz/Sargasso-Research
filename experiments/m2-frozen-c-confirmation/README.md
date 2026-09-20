# Frozen C: reported 2024 nominal 48-hour confirmation

**Date:** 2026-09-10 · **Status:** COMPLETED · **Outcome:** positive

Approved post-confirmation assessment records 228 admitted SKN cases: C mean IoU 0.5152 versus persistence 0.4334; paired mean gain 0.0818 (18.9% relative), 190 wins, 3 ties, 35 losses. These are user-supplied final aggregate results, not independently re-audited for this public release.

| Metric | Value | Scope |
|---|---:|---|
| candidate_mean_iou | 0.5152 | 228 admitted 2024 SKN restricted-source daily-map cases |
| persistence_mean_iou | 0.4334 | Same admitted cases |
| paired_mean_iou_gain | 0.0818 | C minus persistence |
| wins | 190 | 228 admitted cases |
| ties | 3 | 228 admitted cases |
| losses | 35 | 228 admitted cases |
| primary_95_ci_low | 0.0655 | Whole 14-calendar-day percentile bootstrap; paired mean gain |
| primary_95_ci_high | 0.0977 | Whole 14-calendar-day percentile bootstrap; paired mean gain |

## Interpretation

- Reported by the project owner in the approved assessment; result CSV/JSON hashes and performance were not independently re-audited here.
- Restricted-source nominal 48-hour daily-map hindcast; daily product does not establish exact per-pixel 48-hour observation timing.
- Not live issue-time skill, beach-arrival probability, or residual improvement over physics alone.
- Different observation operator and checkpoint family from Sentinel-2/R18 serving research.
- 2025 remains closed; no restricted observations or protected outcome arrays were accessed or included.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
