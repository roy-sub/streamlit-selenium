import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager import ChromeType

@st.cache(allow_output_mutation=True)
def get_driver():
    service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

def get_text_from_url(url):
    driver = get_driver()
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    text = driver.find_element(By.TAG_NAME, 'body').text
    driver.quit()
    return text

st.title('Web Page Text Extractor')
url = st.text_input('Enter URL:', 'https://www.example.com')
if st.button('Extract Text'):
    try:
        text = get_text_from_url(url)
        st.text_area('Extracted Text:', value=text, height=200)
    except Exception as e:
        st.error(f'An error occurred: {e}')
