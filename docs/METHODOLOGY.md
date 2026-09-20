# Methodology and interpretation

## Detection

Sargasso's detection research explores multispectral segmentation with U-Net-family models and EfficientNet encoders. The historical selected detector combines R46 and R47 probabilities with four-pass test-time augmentation and a 0.60 decision threshold. The timeline records the progression through sampling, loss, training, label-cleaning, and ensemble experiments.

The architectural foundations are [Ronneberger, Fischer, and Brox (2015)](https://arxiv.org/abs/1505.04597) and [Tan and Le (2019)](https://arxiv.org/abs/1905.11946). Sargassum remote-sensing context includes [Wang and Hu (2021)](https://doi.org/10.1016/j.rse.2021.112631). Citing these methods does not imply that their reported performance applies to Sargasso.

Historical supervision includes automatically generated Sentinel-2-derived weak labels based on the Floating Algae Index ([Hu, 2009](https://doi.org/10.1016/j.rse.2009.05.012)), water masking, and local cleaning. The coastline audit changed the interpretation of earlier evaluations: geographic contradictions in the labels cannot be treated as reliable independent truth. Configuration summaries report only what the corresponding source establishes; undocumented defaults are not reconstructed as fact.

## Drift and residual corrections

The research separates a physics drift baseline from learned residual correction. Historical R18 selection evidence supports a restricted **48-hour, more-than-10-km-offshore** scope; it does not validate correction at the coast or at longer horizons. Subsequent daily-map research uses its own protocols and must not inherit the scope or score of an earlier experiment by name alone.

Changing the horizon, current/wind inputs, label representation, target definition, or cohort creates a materially different evaluation. Retrospective forcing and issue-time forecast forcing must be identified separately. Historical hindcast results do not establish operational forecast skill with information available at issuance.

## Coastal risk

The coastal-risk track derives and calibrates risk scores from physics forecast rasters. A score is not automatically a posterior probability of beaching. Without the corresponding outcome-validation evidence, neither probabilistic calibration nor beach-level performance should be inferred from the existence of a calibration artifact.

## Metrics

- **Intersection over Union (IoU):** intersection of prediction and reference divided by their union. It measures spatial overlap, not pixel accuracy or probability calibration.
- **Paired difference:** compare two methods on the same admitted cases before averaging the differences.
- **Relative improvement:** divide a difference in mean scores by the baseline mean; keep distinct from an absolute IoU or percentage-point change.
- **Win fraction:** number of positive paired differences divided by the case count; this is not classification accuracy.
- **Block-bootstrap interval:** preserve the stated temporal block length when reporting the recorded uncertainty estimate. The published interval concerns the paired mean gain.

The archive does not invent undocumented empty-mask conventions, sampling rules, optimizer settings, or trial counts. Such gaps appear in the experiment limitations and provenance records.

## Evaluation discipline

Chronological splits, non-overlapping scene groups, training-only normalization, and inference/training parity are part of the recorded research progression. Their adoption and fixes matter: old scores are not silently upgraded to satisfy later protocols. Historical selected-patch or test-tuned results retain those labels even after the implementation changes.

Completed negative results remain visible. A failed experiment can be a completed research result; a still-running experiment cannot. Current Putman/GLORYS work appears only as **IN PROGRESS**, with no interim metrics or inferred outcome.

## What can be reproduced here?

Readers can regenerate the archive, audit its internal citations and source fingerprints, recreate the aggregate plots, and inspect released configuration summaries. Reproducing the original model training or protected-data evaluation requires materials outside this release. A source hash identifies an exact source snapshot; it is not evidence that the underlying scientific claim has been independently verified.

See [provenance and licensing](PROVENANCE.md), [results](RESULTS.md), and [references](REFERENCES.md).
