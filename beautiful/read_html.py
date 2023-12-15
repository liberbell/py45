import pandas as pd
import requests


URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
data = pd.read_html(requests.get(URL, headers={'User-agent': 'Mozilla/5.0'}).text, header=0)

print(data[0].head())
print(data[0].tail())