import requests
from bs4 import BeautifulSoup

URL = "https://www.yomiuri.co.jp/"
response = requests.get(URL)
print(response.status_code)