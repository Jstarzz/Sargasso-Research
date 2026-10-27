# Model 2 track-history correction on Caribbean drifters

## Question

If an object has been tracked for a day, can its recent forecast error be used to correct the next days?

## Method

Each case hindcast the last 24 h with the same recipe, measured the error, and added a fading fraction to the forecast. Settings were selected on one period and scored on the other.

## Result

About a fifth less miss at 48 h on drifters, robust to ending the window before issue, and still positive with moderately imprecise fixes.

## Interpretation

The correction is real on drifters, and the gain is local to the object own path. It needs a tracked object.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Drifter positions are an interpolated six-hourly product, so the position at issue time may be partly built from later fixes; the lagged-window check removes most of this but cannot separate leak from information decay.
- Drifters are undrogued surface drifters, not Sargassum, and the arms use analysis fields in place of forecasts.
- Gains shrink with imprecise fixes: about 14 to 19% at 2 km noise and 8 to 11% at 5 km with retuned settings.
- Borrowing the correction of nearby tracked objects for an untracked one is null (1 to 5% worse).
- Tracked-object correction on Sargassum-like suites did not confirm; see the separate record.
