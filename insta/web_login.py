from selenium import webdriver
from time import sleep
import configparser


config_txt = configparser.ConfigParser()
config_txt_path = "config.txt"

with open(config_txt_path, encoding='utf-8') as fp:
    config_txt.read_file(fp)

    read_default = config_txt['Login']
    user_id = read_default.get('User_id')
    password = read_default.get("Password")
