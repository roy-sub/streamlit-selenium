import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType

def get_driver(options):
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

def get_text_from_url(url):
    
    options = Options()
    options.add_argument("--disable-gpu")
    # Comment out the following line to run in non-headless mode
    options.add_argument("--headless")

    driver = get_driver(options)
    driver.get(url)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    text = driver.find_element(By.TAG_NAME, 'body').text
    
    driver.quit()
    return text

st.title('Web Page Text Extractor')
url = st.text_input('Enter URL:', '')
if st.button('Extract Text'):
    try:
        text = get_text_from_url(url)
        st.text_area('Extracted Text:', value=text, height=200)
    except Exception as e:
        st.error(f'An error occurred: {e}')
