import re
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def run_selenium(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Scroll Down

    query = "Curry houses in Oxford"
    
    divSideBar=driver.find_element(By.CSS_SELECTOR, f"div[aria-label='Results for {query}']")
    
    print("Scrolling Started")
    
    keepScrolling = True
    
    while(keepScrolling):
        
        divSideBar.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        
        divSideBar.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        
        html =driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
        
        if(html.find("You've reached the end of the list.")!=-1):
            keepScrolling=False
    
    print("Scrolling Completed")

    # Scrape

    elements = driver.find_elements(By.CLASS_NAME, "hfpxzc")
    
    sub_places =[]
    
    for element in elements:
        href = element.get_attribute("href")
        aria_label = element.get_attribute("aria-label")
        
        sub_place = {"title": aria_label, "href": href}
        sub_places.append(sub_place)

    return len(sub_places), sub_places
    
st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    num_entries, entries = run_selenium(url)
    st.write(num_entries)
    st.write(entries)
    
