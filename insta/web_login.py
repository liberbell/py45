from selenium import webdriver
from time import sleep
import configparser
from selenium.webdriver.chrome.options import Options


config_txt = configparser.ConfigParser()
config_txt_path = "config.txt"
URL1 = "https://www.instagram.com/"

with open(config_txt_path, encoding='utf-8') as fp:
    config_txt.read_file(fp)

    read_default = config_txt['Login']
    user_id = read_default.get('User_id')
    password = read_default.get("Password")


chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL1)