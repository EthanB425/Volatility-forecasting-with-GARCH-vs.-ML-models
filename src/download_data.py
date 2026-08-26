import yfinance as yf
import pandas as pd
import os

# --- Config ---
TICKERS = {
    "spx": "^GSPC",
    "stable": "KO",      # Coca-Cola — swap for any stable large-cap you prefer
    "tech": "NVDA",      # swap for your high-beta pick
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
    
    filepath = os.path.join(DATA_DIR, f"{name}.csv")
    df.to_csv(filepath)
    print(f"  Saved {len(df)} rows to {filepath}")

print("Done.")