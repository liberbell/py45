import pandas as pd
import requests
from datetime import datetime as dt
import matplotlib.pyplot as plt


URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
data = pd.read_html(requests.get(URL, headers={'User-agent': 'Mozilla/5.0'}).text, header=0)

# print(data[0].head())


data[0]["Adj Close**"] = pd.to_numeric(data[0]["Adj Close**"], errors="coerce")
# print(data[0].tail())

data[0].dropna(inplace=True)
# print(data[0].tail())

data[0]["Date2"] = [dt.strptime(i, "%b %d, %Y") for i in data[0]["Date"]]
# print(data[0]["Date2"].head())
# print(data[0].head())

data[0].set_index("Date2", inplace=True)
# print(data[0].head())
# print(data[0]["Adj Close**"].dtype)

data[0]["Adj Close**"].plot(title="AAPL stock price", grid=True)
plt.plot(data[0]["Adj Close**"], label="AAPL stock price")
plt.legend()
plt.show()

data[0].to_csv("AAPL_stock_price.csv")