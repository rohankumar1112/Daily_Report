from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

website ="https://www.bbc.com/news/business"
path ="D:\chromedriver"

driver =webdriver.Chrome(path)
driver.get(website)
driver.maximize_window()


Title =[]
Date =[]

data =driver.find_elements(By.XPATH,"//div[@id ='lx-stream']/div/ol/li/article/header/div/h3/a/span")
date =driver.find_elements(By.XPATH,"//div[@id='lx-stream']/div/ol/li/article/div/div/time/span")


for i in range(len(data)):
    Title.append(data[i].text)
    Date.append(date[i].text)

print(Title)
print(Date)

driver.quit()
