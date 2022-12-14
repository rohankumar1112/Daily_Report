from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import pandas as pd
import pyautogui 
import time

driver=webdriver.Chrome(executable_path="D:\chromedriver")
driver.maximize_window()
# driver.minimize_window()
website='https://medium.com/'
driver.get(website)

time.sleep(2)
Programming =driver.find_element(By.XPATH,'//*[@id="root"]//div/aside/div/div/div/a/div/div/p')

Programming.click()
# pyautogui.hotkey('ctrl', '/')
pyautogui.hotkey('ctrl', 'l')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

# p =driver.page_source
# soup = bs(p, 'html.parser')


time.sleep(5)
print(a)

'''
content =soup.find_all('div',class_='ae cx')

# XPATH(Programming) ://*[@id="root"]/div/div[4]/div[3]/div[1]/div/div/aside/div/div[1]/div[2]/a[1]/div/div/p

Headlines =[]
Author =[]
Date =[]
Links =[]


for i in content:
    headlines =i.h2
    authors =i.h4
    date =i.span.strings
    link =i.h4.parent.parent.parent.parent

    for a in headlines:
        Headlines.append(a)
    for b in  authors:
        Author.append(b) 
    for c in date:
        Date.append(c)  
    for d in link:
        Links.append(d.get('href'))       

print(len(Headlines))
print(len(Author))
print(len(Links))
print(len(Date))

df=pd.DataFrame({'Headlines':Headlines,'Author':Author,'Date':Date,'Links':Links})
df.to_csv('mediumFirstPage.csv',index=False)
'''