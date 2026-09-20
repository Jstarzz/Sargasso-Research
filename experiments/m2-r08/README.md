# Model 2 R8: Five-channel wind and current correction

**Date:** 2026-05-20 · **Status:** COMPLETED · **Outcome:** positive

32 base channels; physics probability, two wind and two current channels; development hindcast improved despite worse validation loss than R7.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.9104 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
