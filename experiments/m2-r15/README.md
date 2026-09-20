# Model 2 R15: Sentinel-3 synthetic pixel proxies

**Date:** 2026-05-27 · **Status:** COMPLETED · **Outcome:** negative

5,000 one-day proxy pairs; 1,000 validation cases had zero median IoU for both physics and residual.

| Metric | Value | Scope |
|---|---:|---|
| validation_loss | 0.8122 | Recorded selection validation; Dice-family loss, lower is better |

## Interpretation

- Development evidence from repeatedly reused cohorts; not independent confirmation or live forecast skill.
- Historical horizon, observation, forcing and scoring contracts changed; numerical comparisons across records can be confounded.
- No restricted observations, case-level outcomes, weights or unfinished run metrics are released.

See [configuration](config.json), [machine-readable record](experiment.json), and [evidence](evidence.md).
