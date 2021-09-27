#! /usr/bin/env python3

#import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#os.environ['PATH'] += r"/Path_To_Selenium_driver"
driver = webdriver.Chrome()

url = "https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"
driver.get(url)

# Only need to call implicity_wait one time, then
# Once set, the implicit wait is set for the life of the WebDriver object.
driver.implicitly_wait(10)   # wait up to 10 seconds

element1 = driver.find_element_by_id('downloadButton')
element1.click()

# Explicit Waits
#WebDriverWait(driver, 30).until(
#  EC.text_to_be_present_in_element(
#    (By.CLASS_NAME, 'progress-label'), 'Complete!'
#  )
#)

try:
  xpath2 = '//button[text()="Close"]'
  element2 = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, xpath2))
  )
  print(element2.text)
  element2.click()
except Exception as e:
  print("ERROR : " + str(e))
