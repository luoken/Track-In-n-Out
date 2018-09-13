# imports we will be using
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import os
import pandas as pd
import requests

url = "http://www.in-n-out.com/locations"

# response = requests.get(url, timeout = 5)
# page_content = BeautifulSoup(response.content, "html.parser")
# print(page_content)

browser = webdriver.Firefox()
browser.get(url)
browser.implicitly_wait(30)
# browser.get(url)

python_button = browser.find_element_by_tag_name("iframe")
print(python_button('src'))
# python_button.click()

#  soup = BeautifulSoup(browser.page_source, 'lxml')

# print(soup)
browser.quit()