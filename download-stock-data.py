import yfinance as yf
import pandas as pd

tickers = {
    "PayPal": "PYPL",
    "Visa": "V",
    "Mastercard": "MA",
    "JP Morgan": "JPM",
    "Bank of America": "BAC"
}

data = []

for company, ticker in tickers.items():
    df = yf.download(ticker, start="2019-01-01", progress=False)
    df.reset_index(inplace=True)
    df["Company"] = company
    data.append(df)

final_df = pd.concat(data)
final_df.to_csv("fintech_stock_data.csv", index=False)

print("✅ Data successfully downloaded and saved as fintech_stock_data.csv")