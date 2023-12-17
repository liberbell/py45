import requests
from bs4 import BeautifulSoup

URL = "https://www.yomiuri.co.jp/"
response = requests.get(URL)
# print(response.status_code)

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(1) > div > h3 > a
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(3) > div > h3 > a
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(6) > div > h3 > a

elems = soup.select("div.headline > article:nth-child(1) > div > h3 > a")
# print(elems[0])
# print(elems[0].contents[0])
# print(elems[0].attrs["href"])

elems = soup.select("div.headline")
# print(elems[0].prettify())
# print(type(elems[0]))

# print(elems[0].h3.a.string)
# print(elems[0].h3.a["href"])
# print(elems[0].li.next_sibling.next_sibling.h3.a.string)
# print(elems[0].article.next_sibling.next_sibling.h3.a.string)

for sibling in elems[0].article.next_sibling:
    print(sibling.h3.a.string)