# Model 2 surface current product comparison on Caribbean drifters

## Question

Does an observation-based surface current product transport drifters better than the model current?

## Method

Eleven recipes on 2,423 drifter cases were scored with held-out drifters for fitted arms, including a forecast-capable form.

## Result

The observation-based current product was far closer to drifter motion.

## Interpretation

A large gain on drifters, not transferred to the four Sargassum GPS mats tested. Mat response to wind may differ from drifters.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Drifters are not Sargassum; on the Puerto Rico GPS mats the recipe tied (medians 12.07/22.52 vs 11.73/22.38 km at 24/48 h) and had a worse 90th percentile.
- Forecast mode uses analysis wind in place of forecast wind, which is optimistic.
- Fitted arms used a 5-fold split by drifter, but the product comparison is exposed development evidence.
- Adding 2% wind to a surface model current made drifters worse, consistent with double counting wind-driven flow; the finding that the model current is overweighted reproduces the half-weight result from GPS tracks.
