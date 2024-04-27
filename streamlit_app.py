import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_selenium(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Wait for the entire page to be loaded
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    content = driver.page_source
    driver.quit()
    return content, username

st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    content, username = run_selenium(url)
    st.write(content)
    st.write(username)
