# -*- coding: utf-8 -*-
from selenium import webdriver
import os

driver = webdriver.Firefox()
##driver = webdriver.Chrome()
file_path = 'file:///E:/python/selenium_newbie/checkbox1.html'
print file_path
driver.get(file_path)

#选择页面上所有的tag name 为input的元素
inputs = driver.find_elements_by_tag_name('input')
print inputs
#然后从中过滤出type为checkbox的元素,单击勾选
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

#driver.quit()
