from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

driver=webdriver.Chrome(executable_path="D:\chromedriver")
driver.maximize_window()
# driver.minimize_window()
website='https://www.business-standard.com/topic/credit-card'
driver.get(website)

time.sleep(2)


driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)



page=driver.page_source
soup = bs(page, 'html.parser')

content=soup.find_all('div',class_='main-cont-left')
# print(content)
User=[]
Headlines=[]
Links=[]

# temp='https://www.business-standard.com/'

for i in content:
    data=i.h2.parent.parent
    print(data)
    # heading=i.h2
    # link=i.h2.parent.parent.parent
    try:
        for a in data:
            User.append(a)S
    except:
        User.append("Data not found")     

    # try:       
    #     for b in heading:
    #         Headlines.append(b)
    # except:
    #     Headlines.append("Data not found")     

    # try:       
    #     for c in link:
    #         Links.append(temp+c.get('href'))
    # except:
    #     Links.append("Data not found")   

# print(Links)             


# Taking help for link extract from https://github.com/ritiksh122/LearnScrapping/blob/main/Medium/main.py
Content=[]

# for k in Links:
#     driver.get(k)
#     result=driver.page_source
#     soup2=bs(result,'html.parser')
#     l=(soup2.section.find_all('div'))
#     emp=''
#     for i in l:
#         emp=emp + i.get_text()    
    
#     Content+=[emp]    
 
print(User)   

# df=pd.DataFrame({'User':User,'Headlines':Headlines,'Links':Links,'MainContent':Content})
# df.to_csv('medium_MachineLearning.csv',index=False)

