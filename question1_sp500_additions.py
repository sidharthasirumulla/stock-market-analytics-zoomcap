"""
Question 1: [Index] S&P 500 Stocks Added to the Index
Scrapes Wikipedia for S&P 500 company constituent additions and analyzes historical inclusion timeline.
"""
import pandas as pd
import requests

def run_q1():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print("Fetching table data from Wikipedia...")
    response = requests.get(url, headers=headers)
    tables = pd.read_html(response.text)
    df = tables[0]

    df['Date added'] = pd.to_datetime(df['Date added'], errors='coerce')
    df['Year added'] = df['Date added'].dt.year

    # Analysis starting from 2020
    df_2020 = df[df['Year added'] >= 2020]
    additions_by_year = df_2020['Year added'].value_counts().sort_index()

    print("\n=== S&P 500 Additions (2020 Onwards) ===")
    print(additions_by_year)
    
    highest_year = int(additions_by_year.idxmax())
    print(f"\n[ANSWER] Year with highest additions (2020+): {highest_year} ({additions_by_year.max()} additions)")

    # Additional metric: > 20 years in index
    cutoff_year = 2026 - 20
    long_standing = df[df['Year added'] < cutoff_year]
    print(f"[ANSWER] Current stocks added before {cutoff_year} (>20 yrs): {len(long_standing)}")

if __name__ == '__main__':
    run_q1()
