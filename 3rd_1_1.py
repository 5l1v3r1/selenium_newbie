#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

print "最大化浏览器"
driver.maximize_window()
#driver.quit()
