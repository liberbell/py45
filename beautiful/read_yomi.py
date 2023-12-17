import requests
from bs4 import BeautifulSoup

URL = "https://www.yomiuri.co.jp/"
response = requests.get(URL)
print(response.status_code)

print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(1) > div > h3 > a
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(3) > div > h3 > a
# body > div.home-2021-primary > div.home-2021-primary__main > div.headline > article:nth-child(6) > div > h3 > a