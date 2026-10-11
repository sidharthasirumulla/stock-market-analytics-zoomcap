# Module 3 Homework – Answers

> **Important:** Q1–Q4 depend on the course dataset (`module3_dataset.csv`), which could not be downloaded where the notebook was first run. The outputs saved in `module3_homework.ipynb` come from a synthetic stand-in, so they do **not** match the answer options. Run the notebook in Colab (Runtime → Run all), then fill in the table below from the real printed outputs.

## How to answer

| # | Notebook line to read | Real output (fill in) | Pick the closest option |
|---|-----------------------|-----------------------|--------------------------|
| 1 | `Answer Q1 - Highest absolute correlation` | ______ | 0.015 / 0.025 / 0.035 / 0.045 |
| 2 | `Answer Q2 - Best new precision` | ______ | 0.558 / 0.568 / 0.578 / 0.588 / 0.598 |
| 3 | `Answer Q3 - Records in TEST where only pred5 is correct` | ______ | 271 / 571 / 1171 / 1571 |
| 4 | `Answer Q4 - Optimal depth` | ______ | 4 / 6 / 8 / 12 |

Homework options are usually approximate, so choose the option nearest to your computed value.

Sanity check for the synthetic run (not real answers): it gave 0.021, 0.551, 58 and depth 1, none of which match the options, which confirms those outputs can't be submitted.

## Question 5 (exploratory): What data is missing?

**Additional indicators / data sources**

1. **Market microstructure & sentiment**
   - Options-market indicators: implied-volatility skew, put/call ratio, VIX term structure.
   - News and earnings-call sentiment scores (e.g., LLM-derived) from headlines and transcripts.
2. **Global macro & liquidity**
   - Central bank balance sheets (Fed WALCL, ECB, RBI).
   - 10Y–2Y yield-spread momentum and real rates (TIPS yield).

**Reasoning:** Macro variables like DGS10 and FEDFUNDS move slowly and describe the broad regime, while technical indicators capture price momentum. Options-implied expectations and liquidity measures bridge the gap between long-term macro trends and the 30-day prediction horizon.
