"""
Question 2: [Macro] Indexes YTD (as of 21 August 2026)
Downloads global index closing price data from Yahoo Finance and compares YTD performance against S&P 500.
"""
import pandas as pd
import yfinance as yf

def run_q2():
    indices = {
        'United States (S&P 500)': '^GSPC',
        'China (Shanghai Composite)': '000001.SS',
        'Hong Kong (Hang Seng Index)': '^HSI',
        'Australia (S&P/ASX 200)': '^AXJO',
        'India (Nifty 50)': '^NSEI',
        'Canada (S&P/TSX Composite)': '^GSPTSE',
        'Germany (DAX)': '^GDAXI',
        'United Kingdom (FTSE 100)': '^FTSE',
        'Japan (Nikkei 225)': '^N225',
        'Mexico (IPC Mexico)': '^MXX',
        'Brazil (Ibovespa)': '^BVSP'
    }

    print("Downloading YTD pricing data for global stock market indices...")
    data = yf.download(list(indices.values()), start='2026-01-01', end='2026-08-22')['Close']

    first_day = data.ffill().bfill().iloc[0]
    last_day = data.ffill().bfill().iloc[-1]

    ytd_returns = ((last_day - first_day) / first_day) * 100

    ticker_map = {v: k for k, v in indices.items()}
    ytd_returns.index = [ticker_map.get(col, col) for col in ytd_returns.index]

    sp500_ret = ytd_returns['United States (S&P 500)']
    better_indexes = ytd_returns[ytd_returns > sp500_ret]

    print("\n=== YTD Performance Comparison (1 Jan 2026 - 21 Aug 2026) ===")
    for idx, val in ytd_returns.items():
        print(f"{idx:32s}: {val:6.2f}%")

    print(f"\nS&P 500 Return: {sp500_ret:.2f}%")
    print(f"[ANSWER] Number of indexes outperforming US (S&P 500): {len(better_indexes)}")

if __name__ == '__main__':
    run_q2()
