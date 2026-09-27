import io
import requests
import numpy as np
import pandas as pd
import yfinance as yf

def main():
    # Load and filter 2025 IPO data (same as Q2)
    url = "https://www.iposcoop.com/2025-pricings/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    resp = requests.get(url, headers=headers)
    df = pd.read_html(io.StringIO(resp.text))[0]

    df['Offer Date Parsed'] = pd.to_datetime(df['Offer Date'], errors='coerce')
    filtered = df[(df['Offer Date Parsed'] < '2025-09-01')].copy()
    tickers = filtered['Symbol'].dropna().str.strip().tolist()

    data = yf.download(tickers, start="2025-01-01", end="2026-09-12", group_by='ticker')

    processed_tickers = []
    for ticker in tickers:
        try:
            if ticker not in data.columns.levels[0]:
                continue
            df_t = data[ticker].dropna(how='all').copy()
            if df_t.empty or 'Close' not in df_t.columns:
                continue

            # Calculate 1 to 12 months growth (21 to 252 trading days)
            for m in range(1, 13):
                days = m * 21
                df_t[f'future_growth_{m}_m'] = df_t['Close'].shift(-days) / df_t['Close']
            
            df_t['Ticker'] = ticker
            df_t = df_t.reset_index()
            processed_tickers.append(df_t)
        except Exception:
            continue

    full_df = pd.concat(processed_tickers, ignore_index=True)

    # Find first trading day per ticker
    min_dates = full_df.groupby('Ticker')['Date'].min().reset_index()
    ipo_entry_points = pd.merge(min_dates, full_df, on=['Ticker', 'Date'], how='inner')

    # Analyze median growth across months
    growth_cols = [f'future_growth_{m}_m' for m in range(1, 13)]
    medians = ipo_entry_points[growth_cols].median()

    print("--- Median Growth by Holding Month ---")
    print(medians)

    best_month = medians.idxmax()
    best_value = medians.max()
    print(f"\nOptimal Holding Horizon: {best_month} with Median Growth of {best_value:.4f}")

if __name__ == '__main__':
    main()
