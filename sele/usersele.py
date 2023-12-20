from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.safari.options import Options
from selenium.webdriver.chrome.options import Options
from time import sleep

URL1 = "https://www.google.com/search?q=python&oq=python&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGIAEGIoFMg4IARBFGCcYOxiABBiKBTIGCAIQRRg8MgYIAxBFGDwyBggEEEUYPDIGCAUQRRhBMgYIBhBFGEEyBggHEEUYQdIBCDM3MDNqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1"
URL2 = "https://www.google.com"

driver = webdriver.Chrome()
# driver = webdriver.Safari()
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
driver.get(URL2)

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("python")

search_bar.submit()
driver.find_elements(By.XPATH, "//a/h3")

driver.quit()