# Sub-kilometre feasibility Phase 1: currents-only hindcast on Putman GPS tracks

## Question

Can GLORYS surface currents alone transport a floating mat better than simple baselines?

## Method

A single particle was integrated with RK4 at 1 h steps from each rolling case start under a frozen protocol (v1.0.0, hash-bound before any forcing was downloaded).

## Result

Currents-only error was larger than persistence and causal velocity at all four horizons.

## Interpretation

Daily-mean currents alone do not explain mat motion at these scales; wind-driven slip must be added.

## Limitations

- All four tracks are one July-August 2018 deployment episode near Puerto Rico; rolling cases overlap heavily, so case counts are not independent samples.
- Forcing is retrospective reanalysis (daily-mean currents, hourly reanalysis wind), not an as-issued forecast.
- No 500 m or sub-kilometre positional skill and no St Kitts validation is claimed; final claims require another deployment.
- Provider track metadata has unresolved caveats, so no period is treated as confirmed.
- No confidence interval is reported; matched pairs numbered 203, 198, 190 and 176 at the four horizons before land-mask exclusions.
