# R49 SKN serving-mask evaluation

## Question

How does R49 compare with the production R46+R47 mean-probability ensemble on the SKN evaluation cohort under the serving land mask?

## Method

We compare aggregate IoU on the same 129 paired scenes and report the paired-scene 95% interval. This record contains aggregate results only.

## Result

R49 IoU was 0.3903 and production IoU was 0.2148. The paired difference was +0.1755, with a 95% interval of [0.0928, 0.2500].

## Interpretation

R49 scored higher than the production ensemble on this evaluation cohort. The comparison does not change the selected production model or its serving scope.

## Limitations

The R49 validation split was used for model selection. The historical guarded-label IoU of 0.6440 is from a different cohort and metric, was test-tuned, and is not comparable to this SKN result or an unbiased serving estimate.
