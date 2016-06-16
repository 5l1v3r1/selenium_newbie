#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")

print "480*800"
driver.set_window_size(480, 800)
#driver.quit()
