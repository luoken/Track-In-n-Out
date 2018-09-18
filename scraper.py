# imports we will be using
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import os
import pandas as pd
import requests

url = "http://www.in-n-out.com/locations"

browser = webdriver.Firefox()
browser.implicitly_wait(30)
browser.get(url)
innoutiframelink = browser.find_element_by_tag_name("iframe").get_attribute('src')

print(innoutiframelink)

innoutDriver = webdriver.Firefox()
innoutDriver.implicitly_wait(30)
innoutDriver.get(innoutiframelink)
innoutDriver.implicitly_wait(100)

iframeClicker = innoutDriver.find_element_by_id('tabAll')
iframeClicker.click()
iframeClicker = innoutDriver.find_element_by_id('tabAll')
iframeClicker.click()

soup = BeautifulSoup(innoutDriver.page_source, 'lxml')

# print(soup)


data=[]
x = 0
for store in soup.find_all('div', id='results'):
    data.append(store)

print("data")
for d in data:
    print(d)
    print('\n')


#  soup = BeautifulSoup(browser.page_source, 'lxml')

# print(soup)
# browser.quit()
# innoutDriver.quit()