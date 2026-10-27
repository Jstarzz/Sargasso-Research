# Model 2 R18 neural correction: clean re-evaluation finds no benefit beyond a constant shift

## Question

Does the R18 neural correction learn anything beyond a constant offset?

## Method

R18 and physics arms were scored on 19 held-out pairs, with a control that adds one constant vector to wind-only physics; a footprint-aware pair benchmark then scored arms only inside the area the later scene imaged.

## Result

R18 matched a constant shift; no benchmark arm separated from persistence.

## Interpretation

The R18 gain was mostly a footprint-driven east offset, not learned transport. Same-footprint observations are needed to train a learned correction.

## Limitations

- The source report is an untracked working-tree file; it is identified by SHA-256 only and has no source commit.
- Pair offsets track the differing image footprints of the two scenes: pooled correlation 0.77 between footprint offset and forecast residual, so cross-orbit pairs conflate footprint with transport.
- The planned common-footprint rescoring failed (timeout, then a crash) and its pre-registered criterion was never evaluated.
- The pair benchmark is underpowered: only about 20% of predicted mass lands in the observed strip.
- The only consistent signal is that east bias falls as windage rises toward 2 to 3 percent.
- This supersedes the archive records that describe R18 as a validated selection.
