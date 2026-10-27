# Model 2 on raw GPS trackers inside Sargassum mats (Barbados and Jamaica)

## Question

Does the Model 2 improvement hold on real Sargassum mats tracked by GPS, not just drifters?

## Method

Hourly raw fixes from trackers inside mats were scored with settings frozen beforehand, for untracked and tracked correction arms at several horizons.

## Result

Confirmed at 24 and 48 h on both sites, not confirmed at 6 h on Barbados.

## Interpretation

This is the strongest evidence yet that the gains transfer to real mats, but it rests on few trackers.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Five trackers in one season and one area, plus one tracker off Jamaica; intervals resample tracker-days and are optimistic.
- Forcing is reanalysis currents; no forecast fields.
- It disagrees with the 2018 Puerto Rico mats, where a related blend family was worse than the cached baseline.
- On Jamaica the extra 1% wind mattered (-21% for the wind-added recipe against -12% for the current-only one).
