from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd


website ="https://www.nytimes.com/section/technology"
path ="D:\chromedriver"

driver =webdriver.Chrome(path)
driver.get(website)
driver.maximize_window()

content =driver.find_elements(By.CSS_SELECTOR,'li.css-112uytv')

headlines =[]
news =[]
date =[]
authors =[]

for items in content:
    # Headings
    headlines.append(items.find_element(By.CSS_SELECTOR,'.e15t083i0').text)

    #News
    news.append(items.find_element(By.CSS_SELECTOR,'a p.css-1pga48a').text)

    # Date
    date.append(items.find_element(By.CSS_SELECTOR,'div.css-e0xall').text)

    # Authors
    authors.append(items.find_element(By.CSS_SELECTOR,'.css-1n7hynb').text)

driver.quit()


# Import data to csv using pandas
df=pd.DataFrame({'Headlines':headlines,'News':news, 'Date':date, 'Authors':authors})
df.to_csv('data.csv',index=False)
print(df)
