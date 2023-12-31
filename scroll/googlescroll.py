from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import os
import shutil

URL1 = "https://www.google.com"
URL2 = "https://www.google.com/imghp?hl=ja&tab=ri&authuser=0&ogbl"

PATH = "/photo"

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
        scroll_count = 4
        try:
            all_images = []
            for i in range(scroll_count):
                soup = BeautifulSoup(driver.page_source, "html.parser")
                for image in soup.find_all("img"):
                    all_images.append(image)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                sleep(2)
                if i > 3:
                    break

            all_images = list(dict.fromkeys(all_images))
            for index, image in enumerate(all_images):
                print("Image index: " + str(index))
                print("Image src: " + image["src"])
            
        except Exception as err:
            print("error: ", err)
            print("Error with scolling")
            error_flag = False

    except Exception:
        print("cant scroll")
        error_flag = True

if error_flag is False:
    for index, image in enumerate(all_images):
        filename = "image_" + str(index) + ".jpg"
        image_path = os.path.join(PATH, filename)
        print(image)

        image_link = image["data-src"]
        # url_ptn = re.compile(r"^(https)://")
        # res = url_ptn.match(image_link)
        # print(res)
        # if res:
        #     response = requests.get(image_link, stream=True)


sleep(3)
driver.quit()