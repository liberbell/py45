from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

URL1 = "https://www.google.com"
URL2 = "https://www.google.com/imghp?hl=ja&tab=ri&authuser=0&ogbl"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# search_bar = driver.find_element(By.NAME, value="q")
# search_bar.send_keys("python")
# search_bar.submit()

error_flag = False
if error_flag is False:
    try:
        driver.get(URL2)
        search_bar = driver.find_element(By.NAME, value="q")
        search_bar.send_keys("python")
        search_bar.submit()
        sleep(2)

    except Exception:
        print("Somthing failed")
        error_flag = True

error_flag = False
if error_flag is False:
    try:
        scroll_count = 10
        try:
            all_images =[]
            for i in range(scroll_count):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                sleep(2)
                if i > 5:
                    break
        except Exception:
            print("Error with scrolling")
            error_flag = True

    except Exception:
        print("cant scroll")
        error_flag = True

sleep(3)
driver.quit()