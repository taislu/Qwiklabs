#! /usr/bin/env python3

#import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#os.environ['PATH'] += r"/Path_To_Selenium_driver"
driver = webdriver.Chrome()

url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver.get(url)
driver.implicitly_wait(5)

try:
  no_button = driver.find_element_by_class_name('at-cm-no-button')
  no_button.click()
  print("Clicked No Button on Dialog, No issues")
except Exception as e:
  print("Warning : " + str(e))

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

# send keyboard keys
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()

