from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL1 = "https://www.google.com"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL1)

search_bar = driver.find_element(By.NAME, value="q")
search_bar.send_keys("python")