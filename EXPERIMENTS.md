# Completed experiments

Historical research evidence; metrics are meaningful only within their stated scope and limitations.

| Experiment | Date | Outcome | Scope |
|---|---|---|---|
| [Model 1 R14 baseline](experiments/m1-r14-baseline/experiment.json) | Undated | inconclusive | Model 1 |
| [Model 1 R11: revert B0 and heavy augmentation](experiments/m1-r11-reversion/experiment.json) | 2026-04-18 | mixed | Model 1 |
| [Model 1 R15: Rotation augmentation](experiments/m1-r15-2026-04-18/experiment.json) | 2026-04-18 | negative | Model 1 |
| [Model 1 R19: Random resized crop](experiments/m1-r19-2026-04-18/experiment.json) | 2026-04-18 | negative | Model 1 |
| [Model 1 R16: BCE weight reduced to 0.3](experiments/m1-r16-2026-04-19/experiment.json) | 2026-04-19 | negative | Model 1 |
| [Model 1 R17: Learning rate reduced to 5e-5](experiments/m1-r17-2026-04-19/experiment.json) | 2026-04-19 | negative | Model 1 |
| [Model 1 R18: Learning rate raised to 3e-4](experiments/m1-r18-2026-04-19/experiment.json) | 2026-04-19 | negative | Model 1 |
| [Model 1 R20: Decoder dropout 0.2](experiments/m1-r20-2026-04-19/experiment.json) | 2026-04-19 | negative | Model 1 |
| [Model 1 R21: Tversky alpha/beta 0.2/0.8](experiments/m1-r21-2026-04-19/experiment.json) | 2026-04-19 | negative | Model 1 |
| [Model 1 R22: Positive-patch threshold reduced to 0.002](experiments/m1-r22-2026-04-20/experiment.json) | 2026-04-20 | positive | Model 1 |
| [Model 1 R23: Training extended to 60 epochs](experiments/m1-r23-2026-04-20/experiment.json) | 2026-04-20 | positive | Model 1 |
| [Model 1 R24: Dropout on expanded 60-epoch baseline](experiments/m1-r24-2026-04-20/experiment.json) | 2026-04-20 | negative | Model 1 |
| [Model 1 R25: EfficientNet-B2 encoder](experiments/m1-r25-2026-04-20/experiment.json) | 2026-04-20 | negative | Model 1 |
| [Model 1 R26: Rotation on expanded 60-epoch baseline](experiments/m1-r26-2026-04-20/experiment.json) | 2026-04-20 | positive | Model 1 |
| [Model 1 R35: Small MADOS addition](experiments/m1-r35-2026-04-20/experiment.json) | 2026-04-20 | negative | Model 1 |
| [Model 1 R28: Training extended to 90 epochs](experiments/m1-r28-2026-04-21/experiment.json) | 2026-04-21 | negative | Model 1 |
| [Model 1 R29: Positive-patch threshold reduced to 0.001](experiments/m1-r29-2026-04-21/experiment.json) | 2026-04-21 | negative | Model 1 |
| [Model 1 R30: Weight decay 1e-4; early strategy stop](experiments/m1-r30-2026-04-21/experiment.json) | 2026-04-21 | negative | Model 1 |
| [Model 1 R31: Five raw spectral bands instead of three indices](experiments/m1-r31-2026-04-21/experiment.json) | 2026-04-21 | negative | Model 1 |
| [Model 1 R33: Split investigation; historical stratification wording later corrected](experiments/m1-r33-2026-04-23/experiment.json) | 2026-04-23 | negative | Model 1 |
| [Model 1 R34: Weighted sampling](experiments/m1-r34-2026-04-23/experiment.json) | 2026-04-23 | negative | Model 1 |
| [Model 1 R36: MADOS removal and early stopping](experiments/m1-r36-2026-04-24/experiment.json) | 2026-04-24 | positive | Model 1 |
| [Model 1 R37: Repair of masked positive pixels](experiments/m1-r37-2026-04-24/experiment.json) | 2026-04-24 | positive | Model 1 |
| [Model 1 R38: Expanded dataset and positive weight 3.7](experiments/m1-r38-2026-04-27/experiment.json) | 2026-04-27 | positive | Model 1 |
| [Model 1 R39: Warm-restart/focal experiment](experiments/m1-r39-2026-04-28/experiment.json) | 2026-04-28 | negative | Model 1 |
| [Model 1 R39: Full-dataset smooth-cosine baseline](experiments/m1-r39-2026-05-11/experiment.json) | 2026-05-11 | positive | Model 1 |
| [Model 1 R42: Filtered 17,447-patch training set; warm resume](experiments/m1-r42-2026-05-15/experiment.json) | 2026-05-15 | positive | Model 1 |
| [Model 1 R43: Pseudo-label mixing 0.25 with conservative thresholds](experiments/m1-r43-2026-05-16/experiment.json) | 2026-05-16 | positive | Model 1 |
| [Model 1 R44: Exclude 28 low-label scenes](experiments/m1-r44-2026-05-17/experiment.json) | 2026-05-17 | positive | Model 1 |
| [Model 1 R45: Updated pseudo-labels and exclusions; extended warm resume](experiments/m1-r45-2026-05-17/experiment.json) | 2026-05-17 | negative | Model 1 |
| [Model 1 R46: Remove pseudo-labels and expand exclusions](experiments/m1-r46-2026-05-19/experiment.json) | 2026-05-19 | positive | Model 1 |
| [Model 1 R47: May attempt; distinct from June rerun](experiments/m1-r47-2026-05-19/experiment.json) | 2026-05-19 | negative | Model 1 |
| [Model 2 R1: Initial 38K-parameter residual CNN](experiments/m2-r01/experiment.json) | 2026-05-20 | mixed | Model 2 |
| [Model 2 R2: Smaller 10K-parameter correction](experiments/m2-r02/experiment.json) | 2026-05-20 | positive | Model 2 |
| [Model 2 R3: Flip augmentation](experiments/m2-r03/experiment.json) | 2026-05-20 | negative | Model 2 |
| [Model 2 R4: Wind-noise augmentation](experiments/m2-r04/experiment.json) | 2026-05-20 | negative | Model 2 |
| [Model 2 R5: 48-hour-only specialization](experiments/m2-r05/experiment.json) | 2026-05-20 | positive | Model 2 |
| [Model 2 R6: Mixed-horizon heavy regularization](experiments/m2-r06/experiment.json) | 2026-05-20 | mixed | Model 2 |
| [Model 2 R7: 48-hour specialization plus wind noise](experiments/m2-r07/experiment.json) | 2026-05-20 | positive | Model 2 |
| [Model 2 R8: Five-channel wind and current correction](experiments/m2-r08/experiment.json) | 2026-05-20 | positive | Model 2 |
| [Model 2 R9: Add Stokes drift](experiments/m2-r09/experiment.json) | 2026-05-20 | mixed | Model 2 |
| [Model 2 R10: Mixed horizons with horizon channel](experiments/m2-r10/experiment.json) | 2026-05-20 | negative | Model 2 |
| [Model 2 R11: Mixed training with two-day validation](experiments/m2-r11/experiment.json) | 2026-05-20 | negative | Model 2 |
| [Model 2 R12: Expanded pairs with horizon channel](experiments/m2-r12/experiment.json) | 2026-05-20 | negative | Model 2 |
| [Model 2 R13: Eight-channel Stokes/current/horizon model](experiments/m2-r13/experiment.json) | 2026-05-20 | negative | Model 2 |
| [Model 2 R14: Expanded two-day five-channel data](experiments/m2-r14/experiment.json) | 2026-05-24 | negative | Model 2 |
| [Model 2 R14b: Five-day correction attempt](experiments/m2-r14b/experiment.json) | 2026-05-24 | negative | Model 2 |
| [Model 2 R15: Sentinel-3 synthetic pixel proxies](experiments/m2-r15/experiment.json) | 2026-05-27 | negative | Model 2 |
| [Model 2 R16: Twenty-seed selection](experiments/m2-r16/experiment.json) | 2026-05-28 | positive | Model 2 |
| [Model 2 R17: Geographic expansion and lower windage](experiments/m2-r17/experiment.json) | 2026-05-29 | negative | Model 2 |
| [Model 2 R17b: Lower-windage seed sweep](experiments/m2-r17b/experiment.json) | 2026-05-30 | negative | Model 2 |
| [Model 2 R18: Five-channel seed 11 selection](experiments/m2-r18/experiment.json) | 2026-05-30 | positive | Model 2 |
| [Model 2 R19: Mix synthetic OLCI proxies with real detections](experiments/m2-r19/experiment.json) | 2026-05-30 | negative | Model 2 |
| [Model 2 R20: Real two- and three-day mixture](experiments/m2-r20/experiment.json) | 2026-05-31 | negative | Model 2 |
| [Model 1 R47: June rerun; distinct from May attempt](experiments/m1-r47-2026-06-07/experiment.json) | 2026-06-07 | positive | Model 1 |
| [Model 2 R21: Horizon-conditioned mixed training](experiments/m2-r21/experiment.json) | 2026-06-08 | negative | Model 2 |
| [Land-guarded detection benchmark](experiments/m1-landguard-benchmark/experiment.json) | 2026-06-10 | positive | Model 1 |
| [Model 1 R48: Warm resume on geometrically guarded labels](experiments/m1-r48-2026-06-10/experiment.json) | 2026-06-10 | mixed | Model 1 |
| [Model 1 R49: Scratch training on guarded labels](experiments/m1-r49-2026-06-10/experiment.json) | 2026-06-10 | negative | Model 1 |
| [Model 2 R22: Three-day specialist](experiments/m2-r22/experiment.json) | 2026-06-10 | negative | Model 2 |
| [Model 2 R23: Inference ensemble of R18 seeds](experiments/m2-r23/experiment.json) | 2026-06-10 | inconclusive | Model 2 |
| [Frozen C: reported 2024 nominal 48-hour confirmation](experiments/m2-frozen-c-confirmation/experiment.json) | 2026-09-10 | positive | Model 2 CERSAT |
