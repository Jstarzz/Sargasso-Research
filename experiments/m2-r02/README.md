# Model 2 R2: Smaller 10K-parameter correction

**Date:** 2026-05-20 · **Status:** COMPLETED · **Outcome:** positive

Base channels 16; smaller model improved development hindcast overlap.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.9325 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
