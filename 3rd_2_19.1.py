#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

cookie = driver.get_cookies()

print cookie
driver.quit()
