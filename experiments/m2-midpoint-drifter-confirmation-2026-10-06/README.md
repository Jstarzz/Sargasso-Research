# Model 2 midpoint of current and wind physics: pre-registered drifter test

## Question

Is half-weighting the model current a robust improvement on tracks that played no part in finding it?

## Method

The midpoint arm was registered, then scored on 6,514 drifter cases against current plus 2 percent wind and wind-only 2 percent.

## Result

The midpoint won at every horizon, by growing margins at longer leads.

## Interpretation

This supports overweighting of the model current in the baseline, for drifters. It is not evidence of Sargassum skill.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Drifters are undrogued surface drifters, not floating Sargassum; mats move somewhat differently, and Sargassum GPS looks were NOT_CONFIRMED.
- Forcing is archived analysis fields standing in for forecasts.
- The same drifter product was used earlier in development of related arms; the midpoint itself was registered before scoring.
- The run was stopped at 6,400 of 6,514 cases and resumed with the script resume path, completing all 6,514.
