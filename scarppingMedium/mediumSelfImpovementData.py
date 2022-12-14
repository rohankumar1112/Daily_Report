from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

driver=webdriver.Chrome(executable_path="D:\chromedriver")
driver.maximize_window()
# driver.minimize_window()
website='https://medium.com/tag/self-improvement'

driver.get(website)

time.sleep(2)

for i in range(15):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)


page=driver.page_source
soup = bs(page, 'html.parser')

content=soup.find_all('article',class_='meteredContent')

User=[]
Headlines=[]
Links=[]

temp='https://medium.com'

for i in content:
    data=i.p.strings
    heading=i.h2.strings
    link=i.h2.parent.parent.parent
    try:
        for a in data:
            User.append(a)
    except:
        User.append("Data not found")     

    try:       
        for b in heading:
            Headlines.append(b)
    except:
        Headlines.append("Data not found")     

    try:       
        for c in link:
            Links.append(temp+c.get('href'))
    except:
        Links.append("Data not found")        


# Taking help for link extract from https://github.com/ritiksh122/LearnScrapping/blob/main/Medium/main.py
Content=[]

for k in Links:
    driver.get(k)
    result=driver.page_source
    soup2=bs(result,'html.parser')
    l=(soup2.section.find_all('div'))
    emp=''
    for i in l:
        emp=emp + i.get_text()    
    
    Content+=[emp]    
    

df=pd.DataFrame({'User':User,'Headlines':Headlines,'Links':Links,'MainContent':Content})
df.to_csv('medium_Self-Improvement.csv',index=False)


