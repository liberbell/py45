from selenium import webdriver
from time import sleep
import configparser


config_txt = configparser.ConfigParser()
config_txt.read('config.txt', encoding='utf-8')