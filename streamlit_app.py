import re
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def run_selenium(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    # Scroll Down

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    # Scrape

    elements = driver.find_elements(By.CLASS_NAME, "hfpxzc")
    
    sub_places =[]
    
    for element in elements:
        href = element.get_attribute("href")
        aria_label = element.get_attribute("aria-label")
        
        sub_place = {"title": aria_label, "href": href}
        sub_places.append(sub_place)

    time.sleep(2)
    driver.quite()

    return len(sub_places), sub_places
    
st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    num_entries, entries = run_selenium(url)
    st.write(num_entries)
    st.write(entries)
    
