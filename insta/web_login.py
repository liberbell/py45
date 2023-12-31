from selenium import webdriver
from selenium.webdriver.common.by import By
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
    # print(user_id, password)


chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL1)

error_flag = False
try:
    username_input = driver.find_element(By.XPATH, value="//input[@aria-label='電話番号、ユーザーネーム、メールアドレス']")
    #<input aria-label="電話番号、ユーザーネーム、メールアドレス" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" class="_aa4b _add6 _ac4d _ap35" dir="" type="text" value="" name="username">
    username_input.send_keys(user_id)
    sleep(1)
    password_input = driver.find_element(By.XPATH, value="//input[@aria-label='パスワード']")
    password_input.send_keys(password)
    sleep(1)

    login_button = driver.find_element(By.XPATH, value="//button[@type='submit']")
    login_button.submit()
    sleep(1)
except Exception:
    error_flag = True
    print("User name or Password incorrect")

if error_flag is False:
    try:
        sleep(1)
        notnow_button = driver.find_element(By.XPATH, value="//button[text()='後で]")
        notnow_button.click()
    except Exception:
        pass