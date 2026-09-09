"""
Question 3: [Index] S&P 500 Market Corrections Analysis
Calculates peak-to-trough drawdowns (>=5%) and duration percentiles for S&P 500 from 1950 to present.
"""
import pandas as pd
import numpy as np
import yfinance as yf

def run_q3():
    print("Downloading historical S&P 500 daily data (1950 to Present)...")
    sp500 = yf.download('^GSPC', start='1950-01-01')['Close']
    if isinstance(sp500, pd.DataFrame):
        sp500 = sp500.squeeze()

    # Calculate running cumulative peak (All-Time High)
    ath = sp500.cummax()
    drawdown = (sp500 - ath) / ath * 100

    # Filter for market corrections (drawdown >= 5%)
    is_corr = drawdown <= -5.0
    corr_groups = (~is_corr).cumsum()[is_corr]

    corrections = []
    for g_id, group in sp500.groupby(corr_groups):
        start_date = group.index[0]
        end_date = group.index[-1]
        max_dd = abs(drawdown.loc[group.index].min())
        dur_days = (end_date - start_date).days
        corrections.append({
            'start': start_date,
            'end': end_date,
            'max_drawdown_pct': max_dd,
            'duration_days': dur_days
        })

    df = pd.DataFrame(corrections)

    p25_dd, p50_dd, p75_dd = np.percentile(df['max_drawdown_pct'], [25, 50, 75])
    p25_dur, p50_dur, p75_dur = np.percentile(df['duration_days'], [25, 50, 75])

    print("\n=== S&P 500 Correction Analysis (Since 1950) ===")
    print(f"Total Corrections Identified (>= 5% DD): {len(df)}")
    print(f"[ANSWER] Median Drawdown (50th percentile): {p50_dd:.2f}%")
    print(f"Drawdown Percentiles (25th, 50th, 75th): {p25_dd:.2f}%, {p50_dd:.2f}%, {p75_dd:.2f}%")
    print(f"Duration Percentiles (25th, 50th, 75th): {p25_dur:.0f} days, {p50_dur:.0f} days, {p75_dur:.0f} days")

if __name__ == '__main__':
    run_q3()
