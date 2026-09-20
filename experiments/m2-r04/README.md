# Model 2 R4: Wind-noise augmentation

**Date:** 2026-05-20 · **Status:** COMPLETED · **Outcome:** negative

Superseded by horizon specialization. Original prose incorrectly called 0.9343 better than 0.9325; lower loss makes it worse.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.9343 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
