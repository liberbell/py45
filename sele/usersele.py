from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.safari.options import Options
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import datetime

URL1 = "https://www.google.com/search?q=python&oq=python&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGIAEGIoFMg4IARBFGCcYOxiABBiKBTIGCAIQRRg8MgYIAxBFGDwyBggEEEUYPDIGCAUQRRhBMgYIBhBFGEEyBggHEEUYQdIBCDM3MDNqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1"
URL2 = "https://www.google.com"


# driver = webdriver.Safari()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL2)

search_bar = driver.find_element(By.NAME, value="q")
search_bar.send_keys("python")

search_bar.submit()

csv_date = datetime.datetime.today().strftime(%Y%m%d)
csv_file_name = "google_python_" + csv_date + ".csv"

f = open(csv_file_name, "w", encoding="utf8", errors="ignore")
writer = csv.writer(f, lineterminator="\n")
csv_header = ["List No","Title", "URL"]
writer.writerow(csv_header)

ranking = 1
for elem_h3 in driver.find_elements(By.XPATH, value="//a/h3"):
    csv_list = []
    print(elem_h3.text)
    elem_a = elem_h3.find_element(by=By.XPATH, value="..")
    print(elem_a.get_attribute("href"))
    ranking += 1


driver.quit()