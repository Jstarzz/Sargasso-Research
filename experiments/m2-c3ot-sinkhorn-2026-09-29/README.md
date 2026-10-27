# Model 2 C3-OT: windage 0.04 with Sinkhorn and soft-Dice loss

## Question

Does an optimal-transport style distance loss improve the windage-corrected Model 2 recipe?

## Method

The C2w recipe was retrained with a Sinkhorn km-distance term and a heavier soft-Dice term, and compared on the 2022 and 2023 development folds.

## Result

IoU fell by 0.063 and 0.019 while median miss distance fell by 4.8 km and 1.8 km.

## Interpretation

The overlap loss outweighed the distance gain, so C3 without the Sinkhorn term remained the candidate.

## Limitations

- Development-fold evidence only; not a confirmation and not a live forecast result.
- Miss-distance gains traded off against overlap loss; the overlap metric governed the decision.
- Per-fold sample sizes and intervals are not retained in the public summary.
