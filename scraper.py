# imports we will be using
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import os
import pandas as pd

url = "http://www.in-n-out.com/locations"

browser = webdriver.Firefox()
browser.get(url)
browser.implicitly_wait(30)
browser.get(url)

python_button = browser.find_element_by_id('resultTabs') 
print(python_button)
# python_button.click()

#  soup = BeautifulSoup(browser.page_source, 'lxml')

# print(soup)
browser.quit()