# Data Engineering / Financial Analytics Cohort 2026 - Module 2 Homework

This repository contains python solution scripts for Module 2 Homework.

## File Structure
- `solution_q1.py`: Scrapes recently filed IPOs from IPO Scoop and aggregates withdrawn valuations by company type.
- `solution_q2.py`: Scrapes 2025 IPO pricings, downloads stock OHLCV data via `yfinance`, and calculates 252-day growth, annualized volatility, and median Sharpe ratio as of Sep 11, 2026.
- `solution_q3.py`: Evaluates a fixed months holding strategy (1 to 12 months) from the IPO date to find the optimal holding window.
- `solution_q4.py`: Executes a 25-year RSI < 30 oversold trading strategy using pre-computed indicators and calculates cumulative net profit.

## Requirements
```bash
pip install pandas numpy yfinance requests lxml pyarrow gdown
```

## Execution
Run each script independently:
```bash
python solution_q1.py
python solution_q2.py
python solution_q3.py
python solution_q4.py
```
