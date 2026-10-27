# Model 1 R49 versus production ensemble on the official land-guarded test

## Question

How did the September R49 retrain compare with the production ensemble on the historical official test split?

## Method

Both detectors were evaluated with four-pass flip TTA at threshold 0.60, with and without the serving land mask.

## Result

Masked IoU was 0.5527 for R49 and 0.6232 for the ensemble; unmasked IoU was 0.5519 and 0.5229.

## Interpretation

R49 is ahead on the SKN cohort but behind on the historical official test. This disagreement is why it was not promoted.

## Limitations

- The official test split was reused for earlier selection and threshold tuning; it is not an unbiased serving estimate.
- Read together with the SKN serving evaluation, where R49 was ahead on a different cohort; neither cohort alone supports a promotion decision.
- The gap between the re-evaluated ensemble (0.6232) and the historical 0.6440 is not reconciled in the retained records.
- R49 was not promoted; the selected production models and serving scope are unchanged.
- This is the September 2026 data-only R49; it is distinct from the June 2026 R49 run of the same name.
