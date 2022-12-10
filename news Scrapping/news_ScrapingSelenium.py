from selenium import webdriver
import time
from selenium.webdriver.common.by import By

website ="https://www.nytimes.com/section/technology"
path ="D:\chromedriver"

driver =webdriver.Chrome(path)
driver.get(website)
driver.maximize_window()


content =driver.find_elements(By.CSS_SELECTOR,'li.css-112uytv')
for items in content:
    # Headings
    headlines =items.find_element(By.CSS_SELECTOR,'.e15t083i0')
    print(headlines.text)

    #News
    news =items.find_element(By.CSS_SELECTOR,'a p.css-1pga48a')
    print(news.text)

    # Date
    date =items.find_element(By.CSS_SELECTOR,'div.css-e0xall')
    print(date.text)

    # Authors
    authors =items.find_element(By.CSS_SELECTOR,'.css-1n7hynb')
    print(authors.text)



driver.quit()