# Model 2 windage calibration on Putman GPS mat tracks

## Question

Is the frozen windage coefficient of 0.005 appropriate for natural Sargassum mats?

## Method

Disjoint track segments were advected forward from each observed start with a windage sweep from 0.000 to 0.040, and endpoint great-circle error was compared across horizons, with leave-one-track-out selection.

## Result

Best wind-only windage was about 0.02 to 0.026; held-out median errors were lower than the frozen coefficient and persistence at 6, 24 and 48 hours.

## Interpretation

The frozen windage looks too low for mats. The sample is small, so treat the size of the effect as uncertain.

## Limitations

- Only four tracks near one region and season; segments within a track are correlated, so the effective sample is far smaller than the segment counts.
- Frozen and persistence rows are pooled, not leave-one-out.
- Daily-mean reanalysis currents limit the current-plus-wind variants.
- Endpoint distance on observed mat tracks is not map overlap and not coastal-arrival skill.
- This is a separate calibration study on the same four tracks. See the sub-kilometre feasibility records (subkm-putman-*) for the frozen-protocol hindcasts, where the best coefficient did not hold up forward in time.
