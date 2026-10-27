# Model 2 track-history correction on Sargassum-like suites: not confirmed

## Question

Do the drifter-fitted track-history settings carry over to Sargassum-relevant tracks?

## Method

Settings were frozen and registered, then scored on three suites at 24 and 48 h.

## Result

No suite confirmed at 48 h, and two were worse than the uncorrected forecast.

## Interpretation

The drifter gain does not automatically transfer to mats. The Barbados and Jamaica GPS record shows a case where it does.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Settings were frozen from the open-Caribbean drifter fits; a shorter fade or lower strength is untested and must be chosen without reusing these suites.
- The GPS suite is four tracks over 18 days in one season, scored many times before, and its interpolated positions may leak later fixes.
- These suites have now been looked at and cannot serve as clean holdouts for retuning.
