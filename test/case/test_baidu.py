import os
import time
from selenium import webdriver
from utils.config import DRIVER_PATH
from selenium.webdriver.common.by import By

URL = "http://www.baidu.com"
driver_path = DRIVER_PATH + '\chromedriver.exe'

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium 灰蓝')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
time.sleep(3)
driver.quit()
