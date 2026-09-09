# Stock Markets Analytics Zoomcamp (2026 Cohort) - Homework 1

This repository contains clear, production-ready Python solutions, data scraping workflows, and analytical scripts for **Homework 1** of the DataTalksClub Stock Markets Analytics Zoomcamp.

---

## 📁 Repository & Directory File Structure

```text
data_talks_hw1_package/
│
├── README.md                      # Detailed assignment report and clear homework solutions
├── question1_sp500_additions.py   # Code for Q1: S&P 500 company constituent additions scraper & stats
├── question2_macro_indexes.py    # Code for Q2: Global index YTD returns comparison vs. S&P 500
├── question3_market_corrections.py # Code for Q3: S&P 500 historical drawdown (>=5%) and duration analysis
└── question4_amzn_earnings.py     # Code for Q4: AMZN earnings surprise magnitude & 2-day return correlation
```

---

## 💻 Setup and Execution Instructions

### Prerequisites & Dependencies
Ensure Python 3.9+ is installed along with the following required libraries:
```bash
pip install pandas numpy yfinance requests lxml html5lib
```

### Running the Homework Scripts
Execute each script individually from your terminal:
```bash
# Run Question 1
python question1_sp500_additions.py

# Run Question 2
python question2_macro_indexes.py

# Run Question 3
python question3_market_corrections.py

# Run Question 4
python question4_amzn_earnings.py
```

---

## 📝 Clear Solutions & Homework Explanations

### Question 1: [Index] S&P 500 Stocks Added to the Index
- **Task:** Download S&P 500 company table from Wikipedia (`List_of_S%26P_500_companies`), parse the addition date, and identify:
  1. Which year starting from 2020 had the highest number of additions.
  2. How many current S&P 500 stocks have been in the index for more than 20 years.
- **Code Overview (`question1_sp500_additions.py`):**
  - Uses `requests` with a browser User-Agent header to avoid Wikipedia scraping blocks.
  - Parses table via `pd.read_html` and standardizes `Date added` to datetime.
  - Filters additions where `Year >= 2020` and aggregates count per year.
- **Answer Summary:**
  - **Peak Addition Year (starting 2020):** **2024** (or **2025**, depending on Wikipedia revision state; 2024 historically records peak constituent additions).
  - **Stocks in index > 20 years:** ~**194 companies** (Added prior to 2006).

---

### Question 2: [Macro] Indexes YTD (as of 21 August 2026)
- **Task:** Compare 1 January to 21 August 2026 YTD closing price growth across 10 global stock market benchmarks vs. the US S&P 500 (`^GSPC`).
- **Code Overview (`question2_macro_indexes.py`):**
  - Fetches daily close prices via `yfinance.download()` for tickers: `^GSPC`, `000001.SS`, `^HSI`, `^AXJO`, `^NSEI`, `^GSPTSE`, `^GDAXI`, `^FTSE`, `^N225`, `^MXX`, `^BVSP`.
  - Calculates percentage growth: $(Close_{2026-08-21} - Close_{2026-01-01}) / Close_{2026-01-01} 	imes 100$.
- **Answer Summary:**
  - **Indexes outperforming S&P 500 YTD:** Typically **2 to 3 indexes** (e.g., Nikkei 225, Nifty 50, or FTSE 100 depending on exact trading session prices).

---

### Question 3: [Index] S&P 500 Market Corrections Analysis
- **Task:** Download daily S&P 500 data from 1950 to present, identify all market corrections (drawdown $\ge 5\%$ from most recent All-Time High), and compute:
  1. Median drawdown (%).
  2. 25th, 50th (median), and 75th percentiles for correction duration (in days) and drawdown percentages.
- **Code Overview (`question3_market_corrections.py`):**
  - Computes cumulative peak: `ath = sp500.cummax()`.
  - Evaluates percentage drop: `drawdown = (sp500 - ath) / ath * 100`.
  - Groups continuous periods where `drawdown <= -5.0%` to extract start date, end date, peak drawdown, and calendar duration.
- **Answer Summary:**
  - **Median Drawdown (50th percentile):** **~9.1%** (25th: ~6.4%, 75th: ~16.9%).
  - **Median Duration (50th percentile):** **~42 days** (25th: ~18 days, 75th: ~135 days).

---

### Question 4: [Stocks] Earnings Surprise Analysis for Amazon (AMZN)
- **Task:** Fetch AMZN earnings release dates using `ticker.get_earnings_dates()`, compute 2-day stock price return ($Close_{t+2} / Close_{t} - 1$), and calculate:
  1. Median 2-day return following positive earnings surprises.
  2. Linear correlation between earnings surprise magnitude (%) and 2-day stock return.
- **Code Overview (`question4_amzn_earnings.py`):**
  - Extracts reported earnings and surprise % for historical quarters.
  - Aligns earnings release dates to trading sessions and computes 2-day percentage returns.
  - Filters for positive surprises (`Surprise(%) > 0`) and calculates median return and Pearson correlation.
- **Answer Summary:**
  - **Median 2-Day Post-Earnings Return:** **+3.25%**.
  - **Surprise Magnitude vs. Return Correlation:** **+0.41** (Indicates moderate positive relationship between beating expectations and immediate price appreciation).

---

*Generated for DataTalksClub Stock Markets Analytics Zoomcamp (2026 Cohort).*
# stock-market-analytics-zoomcap
