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

pickup_urls = [elem.attrs["href"] for elem in elems]
# print(pickup_urls)

for pickup_url in pickup_urls:
    pickup_response = requests.get(pickup_url)
    pickup_soup = BeautifulSoup(pickup_response.text, "html.parser")

    pickup_elem = pickup_soup.find("p", class_="sc-eFIZSo knQvE")
    news_urls = pickup_elem.a.attrs["href"]
    # print(news_urls)
    news_response = requests.get(news_urls)
    news_soup = BeautifulSoup(news_response.text, "html.parser")
    # print(news_soup.title.text)

    detail_text = news_soup.find("article", id_="uamods")
    print(detail_text.header.h1.text)

#     <article id="uamods"><header><h1 class="sc-fnebDD bAGyCr">19日　九州は本格的に雪　各地で厳しい寒さ　北海道はなだれや落雪に
# for elem in elems:
#     # print(elem.span.string)
#     # print(elem.attrs["href"])
#     pickup_url = elem.attrs["href"]
#     pickup_response = requests.get(pickup_url)
#     print(pickup_response.text)
    # pickup_soup = BeautifulSoup(pickup_response, "html.parser")
    # print(pickup_response.attrs["href"])
    # print(pickup_response.span.string)
