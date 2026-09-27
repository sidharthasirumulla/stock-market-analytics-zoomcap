import gdown
import pandas as pd

def main():
    # 1. Download Parquet file
    file_id = "1grCTCzMZKY5sJRtdbLVCXg8JXA8VPyg-"
    gdown.download(f"https://drive.google.com/uc?id={file_id}", "data.parquet", quiet=False)
    
    # 2. Read dataset
    df = pd.read_parquet("data.parquet", engine="pyarrow")

    # 3. Filter strategy signals
    # RSI < 30 between 2000-01-01 and 2025-06-01
    df['Date'] = pd.to_datetime(df['Date'])
    filtered_df = df[
        (df['RSI'] < 30) & 
        (df['Date'] >= '2000-01-01') & 
        (df['Date'] <= '2025-06-01')
    ].copy()

    # 4. Profit Calculation
    # Net Income = 1000 * sum(growth_future_30d - 1)
    net_income = 1000 * (filtered_df['growth_future_30d'] - 1).sum()
    net_income_thousands = net_income / 1000.0

    print(f"Total Trades Triggered: {len(filtered_df)}")
    print(f"Total Net Income ($): ${net_income:,.2f}")
    print(f"Total Net Income ($ Thousands): ${net_income_thousands:,.2f}k")

if __name__ == '__main__':
    main()
