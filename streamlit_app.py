import os
import time
import json
import streamlit as st

os.chmod('chromedriver',0o755)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

PROXY = "proxy.soax.com:9000"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('proxy.soax.com'.format(PROXY))

# driver = webdriver.Chrome('chromedriver', options=chrome_options) 

path = shutil.which('chromedriver')
driver = webdriver.Chrome(options=chrome_options,service=path)

driver.get("https://www.instagram.com/accounts/login/")

page_title = driver.title

time.sleep(5)
driver.quit()

# Display the extracted content in Streamlit
st.title('Web Page Content Display')
st.write(f'Page Title: {page_title}')
