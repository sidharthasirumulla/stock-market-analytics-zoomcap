import io
import requests
import numpy as np
import pandas as pd

def main():
    # 1. Scrape data
    url = "https://www.iposcoop.com/ipos-recently-filed/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    resp = requests.get(url, headers=headers)
    tables = pd.read_html(io.StringIO(resp.text))
    df = tables[0]

    # Filter for Withdrawn
    df_withdrawn = df[df['Expected To Trade'] == 'Withdrawn'].copy()
    print(f"Total withdrawn entries: {len(df_withdrawn)}")

    # 2. Company Classification
    def classify(name):
        if not isinstance(name, str):
            return "Other"
        if "Technologies" in name:
            return "Technologies"
        elif any(k in name for k in ["Acquisition Corp", "Acquisition Corporation", "Corp"]):
            return "Acquisition Corp"
        elif any(k in name for k in ["Inc", "Incorporated"]):
            return "Inc."
        elif "Group" in name:
            return "Group"
        elif any(k in name for k in ["Ltd", "Limited"]):
            return "Limited"
        elif any(k in name for k in ["Holdings", "Holding"]):
            return "Holdings"
        return "Other"

    df_withdrawn['Company Type'] = df_withdrawn['Company'].apply(classify)

    # 3. Clean numeric fields
    def clean_num(val):
        if pd.isna(val) or str(val).strip() in ['-', '']:
            return np.nan
        val_str = str(val).replace('$', '').replace(',', '').strip()
        try:
            return float(val_str)
        except:
            return np.nan

    df_withdrawn['Price Low Num'] = df_withdrawn['Price Low'].apply(clean_num)
    df_withdrawn['Price High Num'] = df_withdrawn['Price High'].apply(clean_num)
    df_withdrawn['Avg_price'] = (df_withdrawn['Price Low Num'] + df_withdrawn['Price High Num']) / 2.0
    
    # Fill missing Avg_price if low/high missing individually
    df_withdrawn['Avg_price'] = df_withdrawn['Avg_price'].fillna(df_withdrawn['Price Low Num']).fillna(df_withdrawn['Price High Num'])

    df_withdrawn['Shares_num'] = df_withdrawn['Shares (millions)'].apply(clean_num)
    df_withdrawn['Est_vol_num'] = df_withdrawn['Est $ Vol (millions)'].apply(clean_num)

    # 4. Value Calculation
    df_withdrawn['Shares_offered_value'] = np.where(
        (df_withdrawn['Shares_num'].notna()) & (df_withdrawn['Avg_price'].notna()),
        df_withdrawn['Shares_num'] * df_withdrawn['Avg_price'],
        df_withdrawn['Est_vol_num']
    )

    # 5. Aggregation
    result = df_withdrawn.groupby('Company Type')['Shares_offered_value'].sum().sort_values(ascending=False)
    print("\n--- Total Withdrawn Value by Company Type ($ Millions) ---")
    print(result)

if __name__ == '__main__':
    main()
