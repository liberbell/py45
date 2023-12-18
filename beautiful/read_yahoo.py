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

pickup_url = [elem.attrs["href"] for elem in elems]
print(pickup_url)

# for elem in elems:
#     # print(elem.span.string)
#     # print(elem.attrs["href"])
#     pickup_url = elem.attrs["href"]
#     pickup_response = requests.get(pickup_url)
#     print(pickup_response.text)
    # pickup_soup = BeautifulSoup(pickup_response, "html.parser")
    # print(pickup_response.attrs["href"])
    # print(pickup_response.span.string)
