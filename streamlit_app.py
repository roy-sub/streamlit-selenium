import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_selenium(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    content = driver.page_source
    driver.quit()
    return content

st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    content = run_selenium(url)
    st.write(content)
