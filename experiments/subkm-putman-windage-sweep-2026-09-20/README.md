# Sub-kilometre feasibility Phase 2: currents plus fixed windage sweep

## Question

Does adding a fixed fraction of wind to the currents close the gap to simple baselines?

## Method

Currents were combined with 0, 1, 2 and 3 percent of hourly 10 m wind; all coefficients were scored on identical cases.

## Result

Median error fell monotonically with coefficient up to 3 percent, the largest value tried; the best value sits at the edge of the sweep.

## Interpretation

Windage is the dominant missing term, but the optimum is not bracketed and was chosen in-sample.

## Limitations

- All four tracks are one July-August 2018 deployment episode near Puerto Rico; rolling cases overlap heavily, so case counts are not independent samples.
- Forcing is retrospective reanalysis (daily-mean currents, hourly reanalysis wind), not an as-issued forecast.
- No 500 m or sub-kilometre positional skill and no St Kitts validation is claimed; final claims require another deployment.
- Provider track metadata has unresolved caveats, so no period is treated as confirmed.
- The best coefficient is selected in-sample on the same cases it is scored on; see the validation record, where it only partly held up.
- The sweep is a prespecified sensitivity analysis, not a fitted model.
