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
    
    query = "Curry houses in Oxford"
    driver.find_element(By.CSS_SELECTOR,f"div[aria-label='Results for {query}']") 

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

    return sub_places
    
st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    sub_places = run_selenium(url)
    st.write(sub_places)    
