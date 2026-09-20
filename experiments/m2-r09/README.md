# Model 2 R9: Add Stokes drift

**Date:** 2026-05-20 · **Status:** COMPLETED · **Outcome:** mixed

Validation loss improved but median hindcast overlap regressed; not promoted.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.8946 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
