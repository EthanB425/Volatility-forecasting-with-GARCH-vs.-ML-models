import yfinance as yf
import pandas as pd
import os

TICKERS = {
    "spx": "^GSPC",
    "stable": "KO",
    "tech": "NVDA",
    "btc": "BTC-USD",
}

START = "2017-01-01"
END = "2025-01-01"
DATA_DIR = "data"

os.makedirs(DATA_DIR, exist_ok=True)

for name, ticker in TICKERS.items():
    print(f"Downloading {name} ({ticker})...")
    df = yf.download(ticker, start=START, end=END, auto_adjust=True)

    if df.empty:
        print(f"  WARNING: no data returned for {ticker}")
        continue

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    filepath = os.path.join(DATA_DIR, f"{name}.csv")
    df.to_csv(filepath)
    print(f"  Saved {len(df)} rows to {filepath}")

print("Done.")