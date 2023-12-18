import requests
from bs4 import BeautifulSoup
import time
import re

URL = "https://www.yahoo.co.jp/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

elems = soup.find_all("a")
# print(elems)

elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
# print(elems[0].span.string)
# print(elems[0].attrs["href"])

# print(elems[1].span.string)
# print(elems[1].attrs["href"])

for elem in elems:
    print(elem.span.string)
    print(elem.attrs["href"])