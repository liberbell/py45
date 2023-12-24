from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

URL1 = "https://www.google.com"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

search_bar = driver.find_element(By.NAME, value="q")
search_bar.send_keys("python")
search_bar.submit()

error_flag = False
if error_flag is False:
    try:
        driver.get(URL1)
        sleep(2)

    except Exception:
        print("Somthing failed")
        error_flag = True

error_flag = False
if error_flag is False:
    try:
        driver.get(URL1)
        sleep(2)

    except Exception:
        print("cant scroll")
        error_flag = True

# driver.quit()