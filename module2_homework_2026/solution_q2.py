import io
import requests
import numpy as np
import pandas as pd
import yfinance as yf

def main():
    # 1. Scrape 2025 Pricings
    url = "https://www.iposcoop.com/2025-pricings/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    resp = requests.get(url, headers=headers)
    df = pd.read_html(io.StringIO(resp.text))[0]

    # 2. Filter before Sep 1, 2025 & return != 0%
    df['Offer Date Parsed'] = pd.to_datetime(df['Offer Date'], errors='coerce')
    filtered = df[
        (df['Offer Date Parsed'] < '2025-09-01') & 
        (df['1st Day Return'] != '0.00%') & 
        (df['1st Day Return'] != '0%')
    ].copy()

    tickers = filtered['Symbol'].dropna().str.strip().tolist()
    print(f"Filtered Tickers Count: {len(tickers)}")

    # 3. Download stock data via yfinance
    data = yf.download(tickers, start="2025-01-01", end="2026-09-12", group_by='ticker')

    stocks_list = []
    for ticker in tickers:
        try:
            if len(tickers) == 1:
                df_t = data.copy()
            else:
                if ticker not in data.columns.levels[0]:
                    continue
                df_t = data[ticker].copy()
            
            df_t = df_t.dropna(how='all')
            if df_t.empty or 'Close' not in df_t.columns:
                continue

            df_t['Ticker'] = ticker
            # Feature Engineering
            df_t['growth_252d'] = df_t['Close'] / df_t['Close'].shift(252)
            df_t['volatility'] = df_t['Close'].rolling(30).std() * np.sqrt(252)
            df_t['Sharpe'] = (df_t['growth_252d'] - 0.05) / df_t['volatility']
            
            stocks_list.append(df_t)
        except Exception:
            continue

    stocks_df = pd.concat(stocks_list)

    # 4. Analysis as of 2026-09-11
    sep_11_data = stocks_df.loc[stocks_df.index == '2026-09-11']
    stats = sep_11_data[['growth_252d', 'volatility', 'Sharpe']].describe()

    print("\n--- Stats as of 2026-09-11 ---")
    print(stats)
    print(f"\nMedian Sharpe Ratio: {sep_11_data['Sharpe'].median():.4f}")

if __name__ == '__main__':
    main()
