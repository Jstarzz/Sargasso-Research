# Model 2 R21: Horizon-conditioned mixed training

**Date:** 2026-06-08 · **Status:** COMPLETED · **Outcome:** negative

Six-channel, ten-seed experiment; none beat R18 and the best loss seed had poor hindcast overlap.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.867 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
