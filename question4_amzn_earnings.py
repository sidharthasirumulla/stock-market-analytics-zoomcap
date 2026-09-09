"""
Question 4: [Stocks] Earnings Surprise Analysis for Amazon (AMZN)
Evaluates 2-day price returns following quarterly earnings releases and correlates with surprise magnitude.
"""
import pandas as pd
import yfinance as yf

def run_q4():
    print("Fetching AMZN earnings history and daily price data...")
    ticker = yf.Ticker('AMZN')
    earnings = ticker.get_earnings_dates()
    earnings = earnings.dropna(subset=['Reported EPS', 'Surprise(%)'])

    prices = ticker.history(period='max')['Close']
    returns_2d = (prices.shift(-2) / prices) - 1

    surprises = []
    returns = []

    for idx, row in earnings.iterrows():
        dt = idx.tz_localize(None) if idx.tzinfo else idx
        match = prices.index[prices.index >= dt]
        if len(match) > 0:
            t_day = match[0]
            if t_day in returns_2d.index:
                surprises.append(row['Surprise(%)'])
                returns.append(returns_2d.loc[t_day])

    df = pd.DataFrame({'Surprise': surprises, 'Return_2D': returns})
    pos_surprises = df[df['Surprise'] > 0]

    med_return = pos_surprises['Return_2D'].median() * 100
    corr = df['Surprise'].corr(df['Return_2D'])

    print("\n=== AMZN Earnings Surprise Analysis ===")
    print(f"Evaluated Historical Earnings Events: {len(df)}")
    print(f"Positive Earnings Surprise Events: {len(pos_surprises)}")
    print(f"[ANSWER] Median 2-Day Return after Positive Earnings Surprise: {med_return:.2f}%")
    print(f"[ANSWER] Correlation (Surprise % vs 2-Day Return): {corr:.4f}")

if __name__ == '__main__':
    run_q4()
