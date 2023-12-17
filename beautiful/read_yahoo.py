import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.yahoo.co.jp/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
