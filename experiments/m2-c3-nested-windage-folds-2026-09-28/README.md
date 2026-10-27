# Model 2 C3: higher windage on leave-one-year-out development folds

## Question

Does retraining with corrected windage physics improve over the earlier recipe on honest development folds?

## Method

A recipe with windage 0.04 was trained and compared on leave-one-year-out folds against the windage 0.005 recipe and persistence.

## Result

Small positive gains over the old recipe and large gains over persistence on both folds.

## Interpretation

The gain over persistence is robust across settings; the gain over the old recipe is small and did not survive the later second look.

## Limitations

- Development folds only; not a confirmation and not a live forecast result.
- The later second look found no significant gain of C3 over C (+0.006, interval spanning zero) on an exposed cohort.
- In the separate sub-kilometre study the 3% windage coefficient did not hold up forward in time.
- Per-fold sample sizes and intervals are not retained in the public summary.
