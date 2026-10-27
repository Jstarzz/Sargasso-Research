# Model 2 coast-reach probabilities: calibrated on drifters

## Question

Can a track forecast be turned into calibrated crossing probabilities usable at 3 to 5 days?

## Method

Forecast tracks were combined with up to 2,000 real error paths from the other period, and Brier scores and reliability were compared against Gaussian, single-track and climatology baselines.

## Result

The ensemble was best in both directions and calibrated across the probability range.

## Interpretation

Most of the skill comes from having a calibrated spread at all. A live shadow board is the next test.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Historical undrogued surface drifters, not Sargassum mats; live calibration for Sargassum must be checked separately.
- Analysis fields stand in for forecasts, and both periods were used in earlier development, so this is cross-period rather than prospective.
- The gain over a simple Gaussian spread is small (about 3 to 7 percent lower Brier).
- Discrimination (AUC 0.92 to 0.99) is inflated by many easy distant segments; Brier skill is the meaningful measure.
- No land stopping is modelled.
