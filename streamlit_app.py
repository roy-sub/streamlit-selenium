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

    # Wait for the entire page to be loaded
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))) 
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Log in']")))
    
    content = driver.page_source
    driver.quit()
    return content, username_input, password_input, login_button

st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    content, username_input, password_input, login_button = run_selenium(url)
    st.write(content)
    st.write(username_input)
    st.write(password_input)
    st.write(login_button)
    st.info('')
