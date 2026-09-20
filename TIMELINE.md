# Research timeline

Generated from curated public records. Unknown dates are explicitly marked. IN PROGRESS entries describe scope only.

## Dated milestones

### 2026-03-28 — Initial research design

**COMPLETED** · Model 1

Historical PROJECT revision table dates initial design to March 28; earliest surviving Git commit is March 30. Design date is documentary, not a commit timestamp.


**Provenance**

- Historical PROJECT revision table dates initial design to March 28; earliest surviving Git commit is March 30. Design date is documentary, not a commit timestamp.; Source label: `PROJECT.md` (private historical source; provenance only); SHA-256: `22c1e757bf4d7f44e8c731b211046428f4060490970c7fa022f9f7121b0fe999`; Source commit: `940cd3f`

### 2026-03-30 — Earliest retained project commit

**COMPLETED** · Model 1

Git history begins at 2321bc6; no earlier experiment results are established by this release.


**Provenance**

- Git history begins at 2321bc6; no earlier experiment results are established by this release.; Source label: `PROJECT.md` (private historical source; provenance only); SHA-256: `cdea4094158b4fae082ed1668db341ef26a668e24e3f1d6ecf9828c546c66d1a`; Source commit: `2321bc6`

### 2026-04-12 — Spectral preprocessing generation

**COMPLETED** · Model 1

Preprocessing introduced band handling, floating-algae indices, cloud masks and patches; numerical-stability fixes followed.


**Provenance**

- Preprocessing introduced band handling, floating-algae indices, cloud masks and patches; numerical-stability fixes followed.; Source label: `PROJECT.md` (private historical source; provenance only); SHA-256: `055c6d74395cfe2a33e6218b5b367e8ffc0d69a38ca50879a1a7e7977eeb40c1`; Source commit: `7c224c3`

### 2026-04-13 — Three-index EfficientNet-B3 lineage

**COMPLETED** · Model 1

FAI-only/older prototype descriptions gave way to FAI, AFAI and NDWI inputs with EfficientNet-B3. Older parallel lineages were later retired.


**Provenance**

- FAI-only/older prototype descriptions gave way to FAI, AFAI and NDWI inputs with EfficientNet-B3. Older parallel lineages were later retired.; Source label: `PROJECT.md` (private historical source; provenance only); SHA-256: `7b232d671e16b6aaadbc0491cdb1ed4ef157d607cf36214293c7b1364504c2a5`; Source commit: `236a743`

### 2026-04-17 — Early diagnostics and normalization redesign

**COMPLETED** · Model 1

Git records BCE/Tversky stabilization, train-only normalization, percentile clipping replacing z-scores, encoder freeze diagnostics, and a B0 regularization trial. Individual R1–R10 numbering cannot be reconstructed confidently from retained summaries.


**Provenance**

- Git records BCE/Tversky stabilization, train-only normalization, percentile clipping replacing z-scores, encoder freeze diagnostics, and a B0 regularization trial. Individual R1–R10 numbering cannot be reconstructed confidently from retained summaries.; Source label: `PROJECT.md` (private historical source; provenance only); SHA-256: `5c75a2bfec43c43c80c51b98fdc1a2b69413f3ec25688e3f67010017fee5e4d6`; Source commit: `b163e60`

### 2026-04-18 — Model 1 R11: revert B0 and heavy augmentation

**COMPLETED** · Model 1

Historical PROJECT revision 7 and commit 940cd3f explicitly record R11 returning to B3 and flips with weight decay 0.0005. No authenticated final metric is transcribed.

- [Model 1 R11: revert B0 and heavy augmentation](experiments/m1-r11-reversion/experiment.json)

**Provenance**

- Historical PROJECT revision 7 and commit 940cd3f explicitly record R11 returning to B3 and flips with weight decay 0.0005. No authenticated final metric is transcribed.; Source label: `PROJECT.md` (private historical source; provenance only); SHA-256: `22c1e757bf4d7f44e8c731b211046428f4060490970c7fa022f9f7121b0fe999`; Source commit: `940cd3f`

### 2026-04-18 — Model 1 R15: Rotation augmentation

**COMPLETED** · Model 1

Rotation augmentation. Historical disposition: reverted.

- [Model 1 R15: Rotation augmentation](experiments/m1-r15-2026-04-18/experiment.json)

**Provenance**

- Rotation augmentation. Historical disposition: reverted.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-18 — Model 1 R19: Random resized crop

**COMPLETED** · Model 1

Random resized crop. Historical disposition: reverted.

- [Model 1 R19: Random resized crop](experiments/m1-r19-2026-04-18/experiment.json)

**Provenance**

- Random resized crop. Historical disposition: reverted.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-19 — Model 1 R16: BCE weight reduced to 0.3

**COMPLETED** · Model 1

BCE weight reduced to 0.3. Historical disposition: discard.

- [Model 1 R16: BCE weight reduced to 0.3](experiments/m1-r16-2026-04-19/experiment.json)

**Provenance**

- BCE weight reduced to 0.3. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-19 — Model 1 R17: Learning rate reduced to 5e-5

**COMPLETED** · Model 1

Learning rate reduced to 5e-5. Historical disposition: reverted.

- [Model 1 R17: Learning rate reduced to 5e-5](experiments/m1-r17-2026-04-19/experiment.json)

**Provenance**

- Learning rate reduced to 5e-5. Historical disposition: reverted.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-19 — Model 1 R18: Learning rate raised to 3e-4

**COMPLETED** · Model 1

Learning rate raised to 3e-4. Historical disposition: discard.

- [Model 1 R18: Learning rate raised to 3e-4](experiments/m1-r18-2026-04-19/experiment.json)

**Provenance**

- Learning rate raised to 3e-4. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-19 — Model 1 R20: Decoder dropout 0.2

**COMPLETED** · Model 1

Decoder dropout 0.2. Historical disposition: discard.

- [Model 1 R20: Decoder dropout 0.2](experiments/m1-r20-2026-04-19/experiment.json)

**Provenance**

- Decoder dropout 0.2. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-19 — Model 1 R21: Tversky alpha/beta 0.2/0.8

**COMPLETED** · Model 1

Tversky alpha/beta 0.2/0.8. Historical disposition: discard.

- [Model 1 R21: Tversky alpha/beta 0.2/0.8](experiments/m1-r21-2026-04-19/experiment.json)

**Provenance**

- Tversky alpha/beta 0.2/0.8. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-20 — Model 1 R22: Positive-patch threshold reduced to 0.002

**COMPLETED** · Model 1

Positive-patch threshold reduced to 0.002. Historical disposition: kept.

- [Model 1 R22: Positive-patch threshold reduced to 0.002](experiments/m1-r22-2026-04-20/experiment.json)

**Provenance**

- Positive-patch threshold reduced to 0.002. Historical disposition: kept.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-20 — Model 1 R23: Training extended to 60 epochs

**COMPLETED** · Model 1

Training extended to 60 epochs. Historical disposition: KEPT .

- [Model 1 R23: Training extended to 60 epochs](experiments/m1-r23-2026-04-20/experiment.json)

**Provenance**

- Training extended to 60 epochs. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-20 — Model 1 R24: Dropout on expanded 60-epoch baseline

**COMPLETED** · Model 1

Dropout on expanded 60-epoch baseline. Historical disposition: discard.

- [Model 1 R24: Dropout on expanded 60-epoch baseline](experiments/m1-r24-2026-04-20/experiment.json)

**Provenance**

- Dropout on expanded 60-epoch baseline. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-20 — Model 1 R25: EfficientNet-B2 encoder

**COMPLETED** · Model 1

EfficientNet-B2 encoder. Historical disposition: discard.

- [Model 1 R25: EfficientNet-B2 encoder](experiments/m1-r25-2026-04-20/experiment.json)

**Provenance**

- EfficientNet-B2 encoder. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-20 — Model 1 R26: Rotation on expanded 60-epoch baseline

**COMPLETED** · Model 1

Rotation on expanded 60-epoch baseline. Historical disposition: KEPT .

- [Model 1 R26: Rotation on expanded 60-epoch baseline](experiments/m1-r26-2026-04-20/experiment.json)

**Provenance**

- Rotation on expanded 60-epoch baseline. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-20 — Model 1 R35: Small MADOS addition

**COMPLETED** · Model 1

Small MADOS addition. Historical disposition: discard.

- [Model 1 R35: Small MADOS addition](experiments/m1-r35-2026-04-20/experiment.json)

**Provenance**

- Small MADOS addition. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-21 — Model 1 R28: Training extended to 90 epochs

**COMPLETED** · Model 1

Training extended to 90 epochs. Historical disposition: discard.

- [Model 1 R28: Training extended to 90 epochs](experiments/m1-r28-2026-04-21/experiment.json)

**Provenance**

- Training extended to 90 epochs. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-21 — Model 1 R29: Positive-patch threshold reduced to 0.001

**COMPLETED** · Model 1

Positive-patch threshold reduced to 0.001. Historical disposition: discard.

- [Model 1 R29: Positive-patch threshold reduced to 0.001](experiments/m1-r29-2026-04-21/experiment.json)

**Provenance**

- Positive-patch threshold reduced to 0.001. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-21 — Model 1 R30: Weight decay 1e-4; early strategy stop

**COMPLETED** · Model 1

Weight decay 1e-4; early strategy stop. Stopped before intended training completion; partial metrics deliberately withheld.

- [Model 1 R30: Weight decay 1e-4; early strategy stop](experiments/m1-r30-2026-04-21/experiment.json)

**Provenance**

- Weight decay 1e-4; early strategy stop. Stopped before intended training completion; partial metrics deliberately withheld.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-21 — Model 1 R31: Five raw spectral bands instead of three indices

**COMPLETED** · Model 1

Five raw spectral bands instead of three indices. Historical disposition: discard.

- [Model 1 R31: Five raw spectral bands instead of three indices](experiments/m1-r31-2026-04-21/experiment.json)

**Provenance**

- Five raw spectral bands instead of three indices. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-23 — Model 1 R33: Split investigation; historical stratification wording later corrected

**COMPLETED** · Model 1

Split investigation; historical stratification wording later corrected. Historical disposition: discard.

- [Model 1 R33: Split investigation; historical stratification wording later corrected](experiments/m1-r33-2026-04-23/experiment.json)

**Provenance**

- Split investigation; historical stratification wording later corrected. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-23 — Model 1 R34: Weighted sampling

**COMPLETED** · Model 1

Weighted sampling. Historical disposition: discard.

- [Model 1 R34: Weighted sampling](experiments/m1-r34-2026-04-23/experiment.json)

**Provenance**

- Weighted sampling. Historical disposition: discard.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-24 — Model 1 R36: MADOS removal and early stopping

**COMPLETED** · Model 1

MADOS removal and early stopping. Historical disposition: kept early stopping logic; investigation ongoing.

- [Model 1 R36: MADOS removal and early stopping](experiments/m1-r36-2026-04-24/experiment.json)

**Provenance**

- MADOS removal and early stopping. Historical disposition: kept early stopping logic; investigation ongoing.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-24 — Model 1 R37: Repair of masked positive pixels

**COMPLETED** · Model 1

Repair of masked positive pixels. Historical disposition: KEPT .

- [Model 1 R37: Repair of masked positive pixels](experiments/m1-r37-2026-04-24/experiment.json)

**Provenance**

- Repair of masked positive pixels. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-24 — Positive pixels erased by water masking

**COMPLETED** · Model 1

Investigation reported 99.3% of sargassum-labeled pixels had been made NaN. Preserving floating-algae candidates before strict water masking restored learnable positives; R37 followed.


**Provenance**

- Investigation reported 99.3% of sargassum-labeled pixels had been made NaN. Preserving floating-algae candidates before strict water masking restored learnable positives; R37 followed.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-25 — Data-generation Phase 2 Run 1

**COMPLETED** · Research data pipeline

An initial data-generation run was interrupted by detached-process/logging issues. It was not a training experiment; incomplete processing counts and projections are deliberately withheld.


**Provenance**

- An initial data-generation run was interrupted by detached-process/logging issues. It was not a training experiment; incomplete processing counts and projections are deliberately withheld.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-26 — Refine the water-mask repair

**COMPLETED** · Model 1

Expanded mask was later reverted at the patch-water gate; adaptive thresholding retained recovery of algae outside strict water classification. This supersedes the initial April 24 implementation description.


**Provenance**

- Expanded mask was later reverted at the patch-water gate; adaptive thresholding retained recovery of algae outside strict water classification. This supersedes the initial April 24 implementation description.; Source label: `CLAUDE.md` (private historical source; provenance only); SHA-256: `f42447e49f9145da5dd508d5c9a3c1c91e52738fa165a910d4d34f09103c4e32`; Source commit: `4e8f35582323e52de597b484cc64c04e96dbba2a`

### 2026-04-27 — Model 1 R38: Expanded dataset and positive weight 3.7

**COMPLETED** · Model 1

Expanded dataset and positive weight 3.7. Historical disposition: KEPT .

- [Model 1 R38: Expanded dataset and positive weight 3.7](experiments/m1-r38-2026-04-27/experiment.json)

**Provenance**

- Expanded dataset and positive weight 3.7. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-04-28 — Model 1 R39: Warm-restart/focal experiment

**COMPLETED** · Model 1

Warm-restart/focal experiment. Historical disposition: discard scheduler, KEEP focal_gamma.

- [Model 1 R39: Warm-restart/focal experiment](experiments/m1-r39-2026-04-28/experiment.json)

**Provenance**

- Warm-restart/focal experiment. Historical disposition: discard scheduler, KEEP focal_gamma.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-11 — Model 1 R39: Full-dataset smooth-cosine baseline

**COMPLETED** · Model 1

Full-dataset smooth-cosine baseline. Historical disposition: KEPT.

- [Model 1 R39: Full-dataset smooth-cosine baseline](experiments/m1-r39-2026-05-11/experiment.json)

**Provenance**

- Full-dataset smooth-cosine baseline. Historical disposition: KEPT.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-12 — Triage normalization parity

**COMPLETED** · Model 1

Triage was corrected to use the training percentile normalization. Earlier visual diagnostics may have used a mismatched input transformation.


**Provenance**

- Triage was corrected to use the training percentile normalization. Earlier visual diagnostics may have used a mismatched input transformation.; Source label: `CLAUDE.md` (private historical source; provenance only); SHA-256: `f42447e49f9145da5dd508d5c9a3c1c91e52738fa165a910d4d34f09103c4e32`; Source commit: `4e8f35582323e52de597b484cc64c04e96dbba2a`

### 2026-05-15 — Model 1 R42: Filtered 17,447-patch training set; warm resume

**COMPLETED** · Model 1

Filtered 17,447-patch training set; warm resume. Historical disposition: KEPT.

- [Model 1 R42: Filtered 17,447-patch training set; warm resume](experiments/m1-r42-2026-05-15/experiment.json)

**Provenance**

- Filtered 17,447-patch training set; warm resume. Historical disposition: KEPT.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-16 — Model 1 R43: Pseudo-label mixing 0.25 with conservative thresholds

**COMPLETED** · Model 1

Pseudo-label mixing 0.25 with conservative thresholds. Historical disposition: KEPT .

- [Model 1 R43: Pseudo-label mixing 0.25 with conservative thresholds](experiments/m1-r43-2026-05-16/experiment.json)

**Provenance**

- Pseudo-label mixing 0.25 with conservative thresholds. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-16 — Per-scene evaluation correction

**COMPLETED** · Model 1

Evaluation CSV changed from batch-level rows to true scene-level tracking; historical count was 173 scenes. Later split audit found 174, an unresolved historical artifact discrepancy.


**Provenance**

- Evaluation CSV changed from batch-level rows to true scene-level tracking; historical count was 173 scenes. Later split audit found 174, an unresolved historical artifact discrepancy.; Source label: `CLAUDE.md` (private historical source; provenance only); SHA-256: `f42447e49f9145da5dd508d5c9a3c1c91e52738fa165a910d4d34f09103c4e32`; Source commit: `4e8f35582323e52de597b484cc64c04e96dbba2a`

### 2026-05-17 — Model 1 R44: Exclude 28 low-label scenes

**COMPLETED** · Model 1

Exclude 28 low-label scenes. Historical disposition: KEPT .

- [Model 1 R44: Exclude 28 low-label scenes](experiments/m1-r44-2026-05-17/experiment.json)

**Provenance**

- Exclude 28 low-label scenes. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-17 — Model 1 R45: Updated pseudo-labels and exclusions; extended warm resume

**COMPLETED** · Model 1

Updated pseudo-labels and exclusions; extended warm resume. Historical disposition: discard .

- [Model 1 R45: Updated pseudo-labels and exclusions; extended warm resume](experiments/m1-r45-2026-05-17/experiment.json)

**Provenance**

- Updated pseudo-labels and exclusions; extended warm resume. Historical disposition: discard .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-17 — Physics generation 1: centroid matching

**COMPLETED** · Model 2

Wind-only Lagrangian advection and windage sweeps established a centroid-distance baseline; raw current and Stokes additions did not consistently improve this protocol.


**Provenance**

- Wind-only Lagrangian advection and windage sweeps established a centroid-distance baseline; raw current and Stokes additions did not consistently improve this protocol.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-18 — Physics generation 2: constrained matching

**COMPLETED** · Model 2

Size-weighted one-to-one assignment replaced nearest-neighbor matching, reducing many-to-one optimism. Its distance metrics are not directly interchangeable with raster IoU.


**Provenance**

- Size-weighted one-to-one assignment replaced nearest-neighbor matching, reducing many-to-one optimism. Its distance metrics are not directly interchangeable with raster IoU.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-19 — AFAI coastal-overlap evaluation

**COMPLETED** · Model 2

Satellite AFAI coastal-overlap evaluation expanded from 120 scorable pairs to 193 after recovering small-blob source coverage. Recorded full-coverage recall was 126/193 (65.3%). This is satellite proxy overlap with broad spatial tolerance, not verified beach-arrival recall or calibrated warning accuracy.


**Provenance**

- Satellite AFAI coastal-overlap evaluation expanded from 120 scorable pairs to 193 after recovering small-blob source coverage. Recorded full-coverage recall was 126/193 (65.3%). This is satellite proxy overlap with broad spatial tolerance, not verified beach-arrival recall or calibrated warning accuracy.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-19 — Model 1 R46: Remove pseudo-labels and expand exclusions

**COMPLETED** · Model 1

Remove pseudo-labels and expand exclusions. Historical disposition: KEPT .

- [Model 1 R46: Remove pseudo-labels and expand exclusions](experiments/m1-r46-2026-05-19/experiment.json)

**Provenance**

- Remove pseudo-labels and expand exclusions. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-19 — Model 1 R47: May attempt; distinct from June rerun

**COMPLETED** · Model 1

May attempt; distinct from June rerun. Historical disposition: discard .

- [Model 1 R47: May attempt; distinct from June rerun](experiments/m1-r47-2026-05-19/experiment.json)

**Provenance**

- Scene exclusion warm resume; distinct from earlier same-number run. Historical disposition: discard .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-19 — Physics generation 3: raster overlap

**COMPLETED** · Model 2

Pixel-seeded particles and KDE overlap became the spatial metric; minimum-bandwidth repair changed proxy recall substantially. Coastal detection proxies are not independent beach-arrival truth.


**Provenance**

- Pixel-seeded particles and KDE overlap became the spatial metric; minimum-bandwidth repair changed proxy recall substantially. Coastal detection proxies are not independent beach-arrival truth.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R1: Initial 38K-parameter residual CNN

**COMPLETED** · Model 2

159 train / 39 validation pairs; small validation Dice improvement but overfit.

- [Model 2 R1: Initial 38K-parameter residual CNN](experiments/m2-r01/experiment.json)

**Provenance**

- 159 train / 39 validation pairs; small validation Dice improvement but overfit.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R2: Smaller 10K-parameter correction

**COMPLETED** · Model 2

Base channels 16; smaller model improved development hindcast overlap.

- [Model 2 R2: Smaller 10K-parameter correction](experiments/m2-r02/experiment.json)

**Provenance**

- Base channels 16; smaller model improved development hindcast overlap.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R3: Flip augmentation

**COMPLETED** · Model 2

Sign-corrected flips underperformed; geographic wind symmetry assumption was unsuitable.

- [Model 2 R3: Flip augmentation](experiments/m2-r03/experiment.json)

**Provenance**

- Sign-corrected flips underperformed; geographic wind symmetry assumption was unsuitable.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R4: Wind-noise augmentation

**COMPLETED** · Model 2

Superseded by horizon specialization. Original prose incorrectly called 0.9343 better than 0.9325; lower loss makes it worse.

- [Model 2 R4: Wind-noise augmentation](experiments/m2-r04/experiment.json)

**Provenance**

- Superseded by horizon specialization. Original prose incorrectly called 0.9343 better than 0.9325; lower loss makes it worse.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R5: 48-hour-only specialization

**COMPLETED** · Model 2

95 training / 18 validation pairs; restrict correction to two-day horizon.

- [Model 2 R5: 48-hour-only specialization](experiments/m2-r05/experiment.json)

**Provenance**

- 95 training / 18 validation pairs; restrict correction to two-day horizon.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R6: Mixed-horizon heavy regularization

**COMPLETED** · Model 2

Intended three-day-only run actually admitted all horizons up to three days; did not replace specialized correction.

- [Model 2 R6: Mixed-horizon heavy regularization](experiments/m2-r06/experiment.json)

**Provenance**

- Intended three-day-only run actually admitted all horizons up to three days; did not replace specialized correction.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R7: 48-hour specialization plus wind noise

**COMPLETED** · Model 2

Development gains motivated subsequent current-channel experiment.

- [Model 2 R7: 48-hour specialization plus wind noise](experiments/m2-r07/experiment.json)

**Provenance**

- Development gains motivated subsequent current-channel experiment.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R8: Five-channel wind and current correction

**COMPLETED** · Model 2

32 base channels; physics probability, two wind and two current channels; development hindcast improved despite worse validation loss than R7.

- [Model 2 R8: Five-channel wind and current correction](experiments/m2-r08/experiment.json)

**Provenance**

- 32 base channels; physics probability, two wind and two current channels; development hindcast improved despite worse validation loss than R7.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R9: Add Stokes drift

**COMPLETED** · Model 2

Validation loss improved but median hindcast overlap regressed; not promoted.

- [Model 2 R9: Add Stokes drift](experiments/m2-r09/experiment.json)

**Provenance**

- Validation loss improved but median hindcast overlap regressed; not promoted.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R10: Mixed horizons with horizon channel

**COMPLETED** · Model 2

Early checkpoint and poor hindcast results; completed result supersedes historical TRAINING entry.

- [Model 2 R10: Mixed horizons with horizon channel](experiments/m2-r10/experiment.json)

**Provenance**

- Early checkpoint and poor hindcast results; completed result supersedes historical TRAINING entry.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R11: Mixed training with two-day validation

**COMPLETED** · Model 2

Lower validation loss failed to translate to hindcast skill; completed result supersedes TRAINING entry.

- [Model 2 R11: Mixed training with two-day validation](experiments/m2-r11/experiment.json)

**Provenance**

- Lower validation loss failed to translate to hindcast skill; completed result supersedes TRAINING entry.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R12: Expanded pairs with horizon channel

**COMPLETED** · Model 2

Expanded 116-pair source cohort did not improve end-to-end overlap.

- [Model 2 R12: Expanded pairs with horizon channel](experiments/m2-r12/experiment.json)

**Provenance**

- Expanded 116-pair source cohort did not improve end-to-end overlap.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-20 — Model 2 R13: Eight-channel Stokes/current/horizon model

**COMPLETED** · Model 2

Best validation loss among early runs but median overlap degraded; illustrates objective mismatch.

- [Model 2 R13: Eight-channel Stokes/current/horizon model](experiments/m2-r13/experiment.json)

**Provenance**

- Best validation loss among early runs but median overlap degraded; illustrates objective mismatch.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-21 — Early Model 2 selection and coastal-risk separation

**COMPLETED** · Model 2

R8 was declared the selected correction after early negative ablations; neural correction hurt coastal proxy recall, motivating physics-based coastal-risk assessment. Later R16 and R18 selections superseded this declaration; it is not the current final model.


**Provenance**

- R8 was declared the selected correction after early negative ablations; neural correction hurt coastal proxy recall, motivating physics-based coastal-risk assessment. Later R16 and R18 selections superseded this declaration; it is not the current final model.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-24 — Model 2 R14: Expanded two-day five-channel data

**COMPLETED** · Model 2

Hindcast mean 0.134 and median 0.092 below recorded R8 comparison; cohorts differ.

- [Model 2 R14: Expanded two-day five-channel data](experiments/m2-r14/experiment.json)

**Provenance**

- Hindcast mean 0.134 and median 0.092 below recorded R8 comparison; cohorts differ.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-24 — Model 2 R14b: Five-day correction attempt

**COMPLETED** · Model 2

400 detected pairs; near-unit loss at first selected epoch; no evidence supporting learned five-day correction.

- [Model 2 R14b: Five-day correction attempt](experiments/m2-r14b/experiment.json)

**Provenance**

- 400 detected pairs; near-unit loss at first selected epoch; no evidence supporting learned five-day correction.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-25 — Cloud-adjusted acquisition lesson

**COMPLETED** · Model 2

A raw catalogue pair-count gate greatly overstated usable two-day pairs. Pilot produced six detected pairs against a planned 60-pair gate; later dry-season acquisition improved yield.


**Provenance**

- A raw catalogue pair-count gate greatly overstated usable two-day pairs. Pilot produced six detected pairs against a planned 60-pair gate; later dry-season acquisition improved yield.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-27 — Model 2 R15: Sentinel-3 synthetic pixel proxies

**COMPLETED** · Model 2

5,000 one-day proxy pairs; 1,000 validation cases had zero median IoU for both physics and residual.

- [Model 2 R15: Sentinel-3 synthetic pixel proxies](experiments/m2-r15/experiment.json)

**Provenance**

- 5,000 one-day proxy pairs; 1,000 validation cases had zero median IoU for both physics and residual.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-28 — Model 2 R16: Twenty-seed selection

**COMPLETED** · Model 2

Seed 1 selected; no independent confirmation because hindcast set was reused for selection.

- [Model 2 R16: Twenty-seed selection](experiments/m2-r16/experiment.json)

**Provenance**

- Seed 1 selected; no independent confirmation because hindcast set was reused for selection.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-29 — Model 2 R17: Geographic expansion and lower windage

**COMPLETED** · Model 2

255-pair cohort; all initial seeds net-negative; added sparse pairs degraded validation.

- [Model 2 R17: Geographic expansion and lower windage](experiments/m2-r17/experiment.json)

**Provenance**

- 255-pair cohort; all initial seeds net-negative; added sparse pairs degraded validation.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-30 — Model 2 R17b: Lower-windage seed sweep

**COMPLETED** · Model 2

May 29 five-channel sweep and May 30 eight-channel top-seed assessment share the R17b label; retain this ambiguity. Neither displaced prior selection.

- [Model 2 R17b: Lower-windage seed sweep](experiments/m2-r17b/experiment.json)

**Provenance**

- May 29 five-channel sweep and May 30 eight-channel top-seed assessment share the R17b label; retain this ambiguity. Neither displaced prior selection.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-30 — Model 2 R18: Five-channel seed 11 selection

**COMPLETED** · Model 2

140 nominal two-day pairs; later records identify about 105 effective pairs. Selected from 20 seeds; exact 48-hour and more-than-10-km offshore scope.

- [Model 2 R18: Five-channel seed 11 selection](experiments/m2-r18/experiment.json)

**Provenance**

- 140 nominal two-day pairs; later records identify about 105 effective pairs. Selected from 20 seeds; exact 48-hour and more-than-10-km offshore scope.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-30 — Model 2 R19: Mix synthetic OLCI proxies with real detections

**COMPLETED** · Model 2

200 proxy pairs added to 140 nominal real pairs; selected seeds failed to improve the evaluation pairs.

- [Model 2 R19: Mix synthetic OLCI proxies with real detections](experiments/m2-r19/experiment.json)

**Provenance**

- 200 proxy pairs added to 140 nominal real pairs; selected seeds failed to improve the evaluation pairs.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-05-31 — Model 2 R20: Real two- and three-day mixture

**COMPLETED** · Model 2

202 real pairs; 105 two-day and 97 three-day; mixed training degraded hindcast performance.

- [Model 2 R20: Real two- and three-day mixture](experiments/m2-r20/experiment.json)

**Provenance**

- 202 real pairs; 105 two-day and 97 three-day; mixed training degraded hindcast performance.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-07 — Model 1 R47: June rerun; distinct from May attempt

**COMPLETED** · Model 1

June rerun; distinct from May attempt. Historical disposition: KEPT .

- [Model 1 R47: June rerun; distinct from May attempt](experiments/m1-r47-2026-06-07/experiment.json)

**Provenance**

- Scene exclusion warm resume; distinct from earlier same-number run. Historical disposition: KEPT .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-08 — Model 2 R21: Horizon-conditioned mixed training

**COMPLETED** · Model 2

Six-channel, ten-seed experiment; none beat R18 and the best loss seed had poor hindcast overlap.

- [Model 2 R21: Horizon-conditioned mixed training](experiments/m2-r21/experiment.json)

**Provenance**

- Six-channel, ten-seed experiment; none beat R18 and the best loss seed had poor hindcast overlap.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-09 — 48-hour benefit and 72-hour degradation separated

**COMPLETED** · Model 2

Horizon-stratified R18 diagnostics led to an exact two-day correction gate. These results were later classified as development evidence, not confirmation.


**Provenance**

- Horizon-stratified R18 diagnostics led to an exact two-day correction gate. These results were later classified as development evidence, not confirmation.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-09 — Two-detector ensemble and four-pass TTA selected

**COMPLETED** · Model 1

R46/R47 mean probabilities with four flip passes and threshold 0.60 selected after test sweeps. Legacy-label score must not be compared directly with guarded-label scores.


**Provenance**

- R46/R47 mean probabilities with four flip passes and threshold 0.60 selected after test sweeps. Legacy-label score must not be compared directly with guarded-label scores.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-10 — Prediction-exposed gold review

**COMPLETED** · Model 1

Fifty selected scenes were reviewed; 28 were retained for the early gold subset. Reviewers saw predictions; later audit explicitly rejected independence and population-performance claims.


**Provenance**

- Fifty selected scenes were reviewed; 28 were retained for the early gold subset. Reviewers saw predictions; later audit explicitly rejected independence and population-performance claims.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-10 — Land-guarded detection benchmark

**COMPLETED** · Model 1

Land-guarded labels plus masked R46/R47 ensemble and four-pass TTA at 0.60 yielded recorded IoU 0.6440; unmasked inference on guarded labels yielded 0.4692. Selection and threshold tuning reused test evidence.

- [Land-guarded detection benchmark](experiments/m1-landguard-benchmark/experiment.json)

**Provenance**

- Land-guarded labels plus masked R46/R47 ensemble and four-pass TTA at 0.60 yielded recorded IoU 0.6440; unmasked inference on guarded labels yielded 0.4692. Selection and threshold tuning reused test evidence.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-10 — Model 1 R48: Warm resume on geometrically guarded labels

**COMPLETED** · Model 1

Warm resume on geometrically guarded labels. Historical disposition: KEPT as checkpoint, NOT promoted .

- [Model 1 R48: Warm resume on geometrically guarded labels](experiments/m1-r48-2026-06-10/experiment.json)

**Provenance**

- Warm resume on geometrically guarded labels. Historical disposition: KEPT as checkpoint, NOT promoted .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-10 — Model 1 R49: Scratch training on guarded labels

**COMPLETED** · Model 1

Scratch training on guarded labels. Historical disposition: DISCARD .

- [Model 1 R49: Scratch training on guarded labels](experiments/m1-r49-2026-06-10/experiment.json)

**Provenance**

- Scratch training on guarded labels. Historical disposition: DISCARD .; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-10 — Model 2 R22: Three-day specialist

**COMPLETED** · Model 2

97 three-day training pairs; 88 evaluable hindcasts; apparent gain not significant, so physics-only retained.

- [Model 2 R22: Three-day specialist](experiments/m2-r22/experiment.json)

**Provenance**

- 97 three-day training pairs; 88 evaluable hindcasts; apparent gain not significant, so physics-only retained.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-06-10 — Model 2 R23: Inference ensemble of R18 seeds

**COMPLETED** · Model 2

Three-seed median 0.1349 versus single 0.1195 on 71 reused cases; interval crossed zero; not promoted.

- [Model 2 R23: Inference ensemble of R18 seeds](experiments/m2-r23/experiment.json)

**Provenance**

- Three-seed median 0.1349 versus single 0.1195 on 71 reused cases; interval crossed zero; not promoted.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### 2026-07-26 — Residual label-content drift repair

**COMPLETED** · Model 1

Twenty-four scenes had failed an earlier content round-trip check. Geometric repair of saved patches removed 9,727 inland positives from 18 train/validation scenes; test headline unchanged. R48 predates this repair.


**Provenance**

- Twenty-four scenes had failed an earlier content round-trip check. Geometric repair of saved patches removed 9,727 inland positives from 18 train/validation scenes; test headline unchanged. R48 predates this repair.; Source label: `docs/playbook.md` (private historical source; provenance only); SHA-256: `807a42ededaa3873c3f350693f781e9635b73217cdefcea67d963361e90462a5`; Source commit: `14ef21556cb7548694e3bf79db7d8d516c3fdd11`

### 2026-07-29 — Scientific/runtime contract review

**COMPLETED** · All models

Review documented normalization, horizon, coastal gating and risk-publication requirements. Engineering implementation is separate from evidence of operational forecast skill.


**Provenance**

- Review documented normalization, horizon, coastal gating and risk-publication requirements. Engineering implementation is separate from evidence of operational forecast skill.; Source label: `docs/architecture-review-2026-07-29.md` (private historical source; provenance only); SHA-256: `a1bb3b6bd6b07a1a8c220fdd3217aa70f2fe82193415ded9927c2769b21af26f`; Source commit: `4c73abeceeb25adce3638031a0b73d8626b33852`

### 2026-08-08 — Land-guard and historical replay caveats

**COMPLETED** · Model 1

Missing coastline asset could allow label generation without guard. Historical stored masks and strict-threshold scores were not equivalent by assumption to dynamic inference.


**Provenance**

- Missing coastline asset could allow label generation without guard. Historical stored masks and strict-threshold scores were not equivalent by assumption to dynamic inference.; Source label: `docs/playbook.md` (private historical source; provenance only); SHA-256: `807a42ededaa3873c3f350693f781e9635b73217cdefcea67d963361e90462a5`; Source commit: `14ef21556cb7548694e3bf79db7d8d516c3fdd11`

### 2026-08-08 — Model 3 v1 remains provisional

**COMPLETED** · Model 3

Model 3 v1 retained as provisional 48-hour physics-relative-density bands. Its calibration cohort selected future detections and target-date locations; it cannot establish independent beaching probabilities, negative base rate or operational coverage.


**Provenance**

- Model 3 v1 retained as provisional 48-hour physics-relative-density bands. Its calibration cohort selected future detections and target-date locations; it cannot establish independent beaching probabilities, negative base rate or operational coverage.; Source label: `docs/decisions/model3-v1-provisional.md` (private historical source; provenance only); SHA-256: `5caf7e174efc36168d1ccb2439de63226ae4498eac796ec96d76378d28f75eec`

### 2026-09-02 — Chronological holdout correction

**COMPLETED** · Model 1

Audit corrected year-stratified wording: scene-sorted splits are chronological, with no scene overlap. Historical R33 interpretations must be read with this correction.


**Provenance**

- Audit corrected year-stratified wording: scene-sorted splits are chronological, with no scene overlap. Historical R33 interpretations must be read with this correction.; Source label: `CLAUDE.md` (private historical source; provenance only); SHA-256: `f42447e49f9145da5dd508d5c9a3c1c91e52738fa165a910d4d34f09103c4e32`; Source commit: `4e8f35582323e52de597b484cc64c04e96dbba2a`

### 2026-09-05 — Claim/evidence register supersedes historical headlines

**COMPLETED** · All models

M1 0.6440 is selected-patch/test-tuned; gold subset is non-independent; R18 is diagnostic with unresolved historical contracts; Model 3 is provisional, not beaching probability.


**Provenance**

- M1 0.6440 is selected-patch/test-tuned; gold subset is non-independent; R18 is diagnostic with unresolved historical contracts; Model 3 is provisional, not beaching probability.; Source label: `docs/claim-evidence-register.md` (private historical source; provenance only); SHA-256: `f6945bda193c6af3577e32fa423feaa4191dc94d8e93d56708344be4fede1447`

### 2026-09-06 — CERSAT publication audit: no-go

**COMPLETED** · Model 2 CERSAT

Audit found temporal-support, observation-representation, missingness and block-bootstrap issues. Early results were not accepted as confirmation; no protected outcome contents are republished.


**Provenance**

- Audit found temporal-support, observation-representation, missingness and block-bootstrap issues. Early results were not accepted as confirmation; no protected outcome contents are republished.; Source label: `docs/model2-publication-review-2026-09-06.md` (private historical source; provenance only); SHA-256: `a7378af1fa29ee088e922ee25df86548c78086e34c0a60afd71f3623de4a51d6`

### 2026-09-07 — CERSAT repair audit: incomplete

**COMPLETED** · Model 2 CERSAT

Repaired development evidence superseded earlier point estimates, but incomplete provenance, controls and inference/statistical handling kept confirmation closed. 2024 proposed for once-only confirmation and 2025 reserved.


**Provenance**

- Repaired development evidence superseded earlier point estimates, but incomplete provenance, controls and inference/statistical handling kept confirmation closed. 2024 proposed for once-only confirmation and 2025 reserved.; Source label: `docs/model2-repair-review-2026-09-07.md` (private historical source; provenance only); SHA-256: `397cfe78cf4f33a930fff261674473d70e383a9f6d9a06862bf33b21241a2ba9`

### 2026-09-08 — CERSAT final-readiness audit

**COMPLETED** · Model 2 CERSAT

Further score-blind review preserved a frozen train-2021/select-2022 design and confirmation controls; readiness is not a forecast-performance result.


**Provenance**

- Further score-blind review preserved a frozen train-2021/select-2022 design and confirmation controls; readiness is not a forecast-performance result.; Source label: `docs/model2-final-readiness-review-2026-09-08.md` (private historical source; provenance only); SHA-256: `d08ddc0e9d23857c7a9f42ed0ed18a930b46b0bc33ac95f0ef366eeefe99aa9b`

### 2026-09-09 — CERSAT V3: execution defects block confirmation

**COMPLETED** · Model 2 CERSAT

Review identified an unwired actual frozen-C entry point and raw masks thresholded before invalid-value checks. Required repairs preceded any confirmation.


**Provenance**

- Review identified an unwired actual frozen-C entry point and raw masks thresholded before invalid-value checks. Required repairs preceded any confirmation.; Source label: `docs/model2-v3-independent-go-review-2026-09-09.md` (private historical source; provenance only); SHA-256: `0243967687c00c444370c977b9c8d677aa52956820c5f7baeddff29280c1be9a`

### 2026-09-10 — CERSAT V4: score-blind readiness approved

**COMPLETED** · Model 2 CERSAT

Independent review closed runner and raw-mask defects, verified payload hashes and exact ensemble, and authorized one frozen confirmation; the review itself did not inspect performance.


**Provenance**

- Independent review closed runner and raw-mask defects, verified payload hashes and exact ensemble, and authorized one frozen confirmation; the review itself did not inspect performance.; Source label: `docs/model2-v4-independent-go-review-2026-09-10.md` (private historical source; provenance only); SHA-256: `2dc6fae220dd532512f43789f2941f951ae682a50440304a223a3a1afcd11908`

### 2026-09-10 — Frozen C: reported 2024 nominal 48-hour confirmation

**COMPLETED** · Model 2 CERSAT

Approved post-confirmation assessment records 228 admitted SKN cases: C mean IoU 0.5152 versus persistence 0.4334; paired mean gain 0.0818 (18.9% relative), 190 wins, 3 ties, 35 losses. These are user-supplied final aggregate results, not independently re-audited for this public release.

- [Frozen C: reported 2024 nominal 48-hour confirmation](experiments/m2-frozen-c-confirmation/experiment.json)

**Provenance**

- Approved post-confirmation assessment records 228 admitted SKN cases: C mean IoU 0.5152 versus persistence 0.4334; paired mean gain 0.0818 (18.9% relative), 190 wins, 3 ties, 35 losses. These are user-supplied final aggregate results, not independently re-audited for this public release.; Source label: `docs/post-confirmation-production-assessment-2026-09-10.md` (private historical source; provenance only); SHA-256: `ee80a61a62a28680afbe515fc6779d4d95200d565bcde37c9a95cf09005eb289`

### 2026-09-19 — Research status at release preparation

**COMPLETED** · All models

Current handoff preserves frozen C and R46/R47 and R18 selections. No new training completion or seven-day forecast skill is asserted. User confirms no active training; the separately identified Putman feasibility study is the current research in progress.


**Provenance**

- Current handoff preserves frozen C and R46/R47 and R18 selections. Current active research status additionally uses the separately disclosed owner declaration.; Source label: `docs/handoff.md` (private historical source; provenance only); SHA-256: `c40fdaf827f7d74f30f393280be8c16a88493b7e4f7f3f1b696fd8e3751b8b23`; Source commit: `f4b47afee0c60a821dd067fdf97948f8a6c936af`

### 2026-09-19 — Putman GPS / physics sub-kilometre feasibility, Phase 1 — IN PROGRESS

**IN PROGRESS** · Currents-only retrospective hindcast using real 2018 GLORYS and frozen Putman rolling GPS cases for St Kitts feasibility. User confirms a background worker is running; no outcomes or unfinished metrics published. No model training is active.

## Undated records

These records have no established date. Their placement here implies no chronological order relative to dated milestones.

### Undated (Exact experiment date not established in retained records; positioned by documented lineage.) — Missing and reused round identifiers

**COMPLETED** · Model 1

No standalone completed records were found for Model 1 R12, R13, R27, R32 or R41. R40 appears as a plan; the subsequent full-data run is labeled R39. R39 and R47 labels are reused. These gaps are not invented experiments or proof of ongoing training.


**Provenance**

- No standalone completed records were found for Model 1 R12, R13, R27, R32 or R41. R40 appears as a plan; the subsequent full-data run is labeled R39. R39 and R47 labels are reused. These gaps are not invented experiments or proof of ongoing training.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`

### Undated (Exact experiment date not established in retained records; positioned by documented lineage.) — Model 1 R14 baseline

**COMPLETED** · Model 1

Baseline recorded at the start of the tuning log; B3, three-index inputs, BCE/Tversky, positive weight 10, percentile normalization and 30 epochs.

- [Model 1 R14 baseline](experiments/m1-r14-baseline/experiment.json)

**Provenance**

- Baseline recorded at the start of the tuning log; B3, three-index inputs, BCE/Tversky, positive weight 10, percentile normalization and 30 epochs.; Source label: `docs/tuning-log.md` (private historical source; provenance only); SHA-256: `4749574ff988a133852c44a58889c8f8373682f84cba95e76df7da87b8e63829`; Source commit: `e833e4b2164a28879b7fef8408e52c5734cc6b5e`
