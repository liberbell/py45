from selenium import webdriver
from time import sleep

URL1 = "https://www.google.com/search?q=python&oq=python&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGIAEGIoFMg4IARBFGCcYOxiABBiKBTIGCAIQRRg8MgYIAxBFGDwyBggEEEUYPDIGCAUQRRhBMgYIBhBFGEEyBggHEEUYQdIBCDM3MDNqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1"

driver = webdriver.Chrome()
driver.get(URL1)