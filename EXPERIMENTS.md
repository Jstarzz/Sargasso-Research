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
| [Sub-kilometre feasibility Phase 1: currents-only hindcast on Putman GPS tracks](experiments/subkm-putman-currents-only-2026-09-20/experiment.json) | 2026-09-20 | negative | Retrospective drift hindcast of four natural Sargassum mat GPS tracks with reanalysis surface currents only, horizons 6, 12, 24 and 48 hours. |
| [Sub-kilometre feasibility Phase 4: adding wave Stokes drift](experiments/subkm-putman-stokes-2026-09-20/experiment.json) | 2026-09-20 | negative | Currents, fixed 3 percent windage and reanalysis surface Stokes drift versus the same run without Stokes drift, on identical cases. |
| [Sub-kilometre feasibility Phase 2: currents plus fixed windage sweep](experiments/subkm-putman-windage-sweep-2026-09-20/experiment.json) | 2026-09-20 | mixed | Prespecified sweep of 0, 1, 2 and 3 percent of reanalysis 10 m wind added to reanalysis currents, scored on the intersection of cases valid under all four coefficients. |
| [Sub-kilometre feasibility Phase 3: dependence-aware validation of the 3 percent windage finding](experiments/subkm-putman-windage-validation-2026-09-20/experiment.json) | 2026-09-20 | negative | Leave-one-track-out and purged forward-time validation of the windage coefficient chosen in the sweep. |
| [Model 2 windage calibration on Putman GPS mat tracks](experiments/m2-putman-windage-calibration-2026-09-27/experiment.json) | 2026-09-27 | positive | Wind-only and current-plus-wind drift endpoint errors for four natural Sargassum mat tracks, used to calibrate the windage coefficient. |
| [Model 1 R49 versus production ensemble on the official land-guarded test](experiments/m1-r49-official-landguard-test-2026-09-29/experiment.json) | 2026-09-29 | negative | Model 1 data-only R49 retrain compared with the R46+R47 mean-probability ensemble on the historical land-guarded test split. |
| [R49 SKN serving-mask evaluation against production](experiments/m1-r49-skn-serving-eval-2026-09-29/experiment.json) | 2026-09-29 | positive | Model 1 comparison of R49 with the production R46+R47 mean-probability ensemble on the SKN evaluation cohort under the serving land mask. |
| [Model 2 C3 recovery comparison](experiments/m2-c3-recovery-2026-09-29/experiment.json) | 2026-09-29 | mixed | Aggregate Model 2 recovery comparison of C3, C, and P on the previously exposed June-September 2026 cohort. |
| [Model 2 C3-OT: windage 0.04 with Sinkhorn and soft-Dice loss](experiments/m2-c3ot-sinkhorn-2026-09-29/experiment.json) | 2026-09-29 | negative | Model 2 residual-correction training variant compared with the C2w recipe on development folds. |
| [Model 3 island and coastal stretch recovery results](experiments/m3-recovery-island-stretch-2026-09-29/experiment.json) | 2026-09-29 | inconclusive | Aggregate Model 3 island and coastal stretch risk comparisons in the previously exposed June-September 2026 recovery cohort. |
| [Model 2 midpoint of current and wind physics: pre-registered drifter test](experiments/m2-midpoint-drifter-confirmation-2026-10-06/experiment.json) | 2026-10-06 | mixed | Parameter-free 50:50 midpoint of the current-coupled and wind-only 2 percent forecasts, scored on archived undrogued surface drifters. Drifters are an analogue, not Sargassum. |
| [Model 2 R18 neural correction: clean re-evaluation finds no benefit beyond a constant shift](experiments/m2-r18-clean-reevaluation-2026-10-06/experiment.json) | 2026-10-06 | negative | Model 2 R18 seed 11 learned correction versus physics and a constant-vector control on 19 held-out Sentinel-2 pairs, plus a footprint-aware pair benchmark. |
| [Model 3: no verified beach truth, so skill cannot be measured](experiments/m3-beach-truth-blocked-2026-10-11/experiment.json) | 2026-10-11 | inconclusive | Attempt to build a second Model 3 benchmark from data on disk for 17 accepted beach geometries in the St Kitts and Nevis study area. |
| [Model 1: would dropping R47 cost anything? Registered ensemble alternatives](experiments/m1-ensemble-alternatives-2026-10-12/experiment.json) | 2026-10-12 | negative | Registered non-inferiority test of R46 alone and R46+R49 against the production R46+R47 ensemble on the land-guarded test (173 scenes) and the SKN test (129 scenes). |
| [Model 2 GOES SST-pattern motion versus drifters: not supported](experiments/m2-goes-sst-drifter-validation-2026-10-12/experiment.json) | 2026-10-12 | negative | Retrospective co-motion check of GOES sea-surface-temperature pattern shifts against archived drifter six-hour displacements, under a frozen protocol. |
| [Model 2 coast-reach probabilities: calibrated on drifters](experiments/m2-crossing-probabilities-2026-10-16/experiment.json) | 2026-10-16 | positive | Probability that a drifting object crosses a stretch of line within a lead time, from a forecast track plus empirical error paths, tested across two historical periods. |
