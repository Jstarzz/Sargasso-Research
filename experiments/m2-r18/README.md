# Model 2 R18: Five-channel seed 11 selection

**Date:** 2026-05-30 · **Status:** COMPLETED · **Outcome:** positive

140 nominal two-day pairs; later records identify about 105 effective pairs. Selected from 20 seeds; exact 48-hour and more-than-10-km offshore scope.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.8486 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).

Additional horizon-gated diagnostic: median IoU 0.0403 physics versus 0.1195 corrected over 71 reused cases. Target-informed grids, historical timing and forcing-contract issues prevent confirmation or operational-skill interpretation.
