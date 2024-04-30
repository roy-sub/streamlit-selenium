import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_selenium(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    elements = driver.find_elements(By.CLASS_NAME, "hfpxzc")
    num_locations = len(elements)
    name_locations = []
    
    for element in elements:
        aria_label = element.get_attribute("aria-label")
        if aria_label:
            name_locations.append(aria_label)
    
    driver.quit()
    return num_locations, name_locations

st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    num_locations, name_locations = run_selenium(url)
    st.write(num_locations)
    st.write(name_locations) 
