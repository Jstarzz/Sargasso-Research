# Model 1: would dropping R47 cost anything? Registered ensemble alternatives

## Question

Can R47 be dropped from the production ensemble without losing performance?

## Method

Candidates were registered before scoring and judged by a non-inferiority margin of -0.02 IoU on both test sets using a paired scene bootstrap.

## Result

Both candidates failed the margin on the land-guarded set.

## Interpretation

No ensemble change is supported by the home evidence.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Both test sets use automatic labels; the land-guarded test was reused for earlier selection.
- The re-evaluated production control (0.6232) does not reproduce the historical 0.6440 headline.
- On human labels R47 is the weakest member, which the home automatic labels do not show; independent human adjudication of home scenes is needed.
- R49 alone (0.5528 and 0.3903) and the three-checkpoint mean are descriptive, not promotion results.
