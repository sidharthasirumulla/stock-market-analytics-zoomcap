# Module 4 Homework (2026 Cohort) - How to solve each question

Notebook with the code edits: `Module_04_Homework_2026_solution.ipynb`.
Rule: for every question start from a fresh copy of `[2026]_Module_04_Colab_Trading_Simulations.ipynb`, apply only that question's edits, and run all cells.

> Note: I did not have the course notebook or dataset, so I could not execute anything. The numeric answers below must be read from your own run.

## Q1 - Less features is more
1. Before `pd.get_dummies()`, remove `ticker` and `month_wom` from `CATEGORICAL`.
2. Check `df_with_dummies[NUMERICAL+DUMMIES].info()`: 301 features before, 208 after.
3. Run the whole notebook, go to the end (after the bubble chart) and read the CAGR of `pred10_rf_best_rule_55`. It should be slightly above 1.1195. Pick the closest option.

## Q2 - Second-best Random Forest rule (< 5 trades/day)
1. Use the Q1 notebook. Switch `y_pred_test` to `rf_best.predict_proba(X_test)` and re-run the TPR/FPR cells (precision goes up and TP+FP goes down as the threshold rises).
2. Add the predictors for thresholds 0.56 to 0.64 with `(y_pred_all_class1_array >= t).astype(int)` (watch for name collisions with the existing `pred11_rf_best_rule_65`).
3. Re-run the simulation and in `df_sim1_results` keep rules with avg. trades/day < 5. The one with the highest CAGR (close to 1.12) is the second-best model. Its threshold is the answer. The options 0.56, 0.57 and 0.58 are the plausible ones, because 0.54 is outside the 0.55-0.65 range.

## Q3 - Redefine the target
1. Fresh copy of the original notebook.
2. Set `is_positive_growth_30d_future = (growth_future_30d > 1.022)`. Confirm that class 1 is about 50%.
3. Run all, then in the simulation results find `pred5_clf_10` and read its number of trades.

## Q4 - Ideal strategy (suggested answer)
"Each day, use the Random Forest probability and only consider predictions above 0.65. Take the 3 most confident ones and split my available cash equally between them, instead of a fixed $100 on every positive prediction. If nothing passes the threshold, I stay in cash. This cuts the number of trades (lower costs and effort), concentrates money where precision is highest, and limits risk by capping each position at one third of the budget. To reduce risk further I would add a stop-loss, avoid more than one position per ticker at a time, and confirm that the second model (logistic/NN) also agrees before entering. I would test it by back-testing on the test period and comparing CAGR, trades per day and max drawdown against the baseline."
