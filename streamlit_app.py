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

    # 2. Scrape Average Rating

    avg_rating_element = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'F7nice')]//span[contains(@aria-hidden, 'true')]")
    avg_rating = avg_rating_element.text 
    
    # 3. Scrape Total Number of ratings
    
    total_reviews_element = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'F7nice')]//span[contains(@aria-label, 'reviews')]")
    total_number_of_reviews = total_reviews_element.text
    total_number_of_reviews = total_number_of_reviews.replace('(', '').replace(')', '') 
    
    # 4. Scrape Description
    
    try:
        text_element = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'PYvSYb')]")
        description = text_element.text
    except NoSuchElementException:
        description = ""
    
    # 5. Scrape Service Options
    
    service_option_elements = driver.find_element(by=By.XPATH, value="//div[@class='E0DTEd']//div[contains(@class, 'LTs0Rc')]//div[@aria-hidden='true']")
    service_options = [option.text for option in service_option_elements] 
    
    # 6. Scrape Address
    
    address_button = driver.find_element_by_css_selector('button[aria-label^="Address"]')
    address = address_button.get_attribute('aria-label').split(': ')[1]
    
    # 7. Scrape Open Hours
    
    open_hours = driver.find_element_by_css_selector('.t39EBf.GUrTXd').get_attribute('aria-label')
    
    # 8. Scrape Website Link
    
    website = driver.find_element_by_css_selector('a[aria-label^="Website"]')
    website_link = website.get_attribute('href')
    
    # 9. Scrape Phone Number
    
    phone_button = driver.find_element_by_css_selector('button[aria-label^="Phone"]')
    phone_button_text = phone_button.text
    phone_number = phone_button_text.split('\n')[-1]
    
    # 10. Scrape Reviews
    
    reviews = []
    
    review_elements = driver.find_elements_by_css_selector('.DUGVrf [jslog*="track:click"]')
    review_texts = [element.get_attribute('aria-label') for element in review_elements]
    
    for review_text in review_texts:
        review_text = re.search('"([^"]*)"', review_text).group(1)
        reviews.append(review_text)
    
    review_elements = driver.find_elements_by_css_selector('.wiI7pd')
    review_texts = [element.text for element in review_elements]
    
    for review_text in review_texts:
        reviews.append(review_text)

    return avg_rating, total_number_of_reviews, description, service_options, service_options, address, open_hours, website_link, phone_number, reviews

st.title('Simple Web Scraping with Selenium and Streamlit')
url = st.text_input('Enter a website URL:')
if st.button('Scrape'):
    st.info('Scraping the website...')
    avg_rating, total_number_of_reviews, description, service_options, address, open_hours, website_link, phone_number, reviews = run_selenium(url)
    st.write(avg_rating)
    st.write(total_number_of_reviews)
    st.write(description)
    st.write(service_options)
    st.write(address)
    st.write(open_hours)
    st.write(website_link)
    st.write(phone_number)
    st.write(reviews)
