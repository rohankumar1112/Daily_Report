from selenium import webdriver
from selenium.webdriver.common.by import By
import time


website ="https://economictimes.indiatimes.com/topic/websites"

driver =webdriver.Chrome(executable_path="D:\chromedriver")
driver.maximize_window()
driver.get(website)
time.sleep(5)

Headlines =[]

data =driver.find_elements(By.XPATH,'//*[@id="all"]/div')
# title     =driver.find_elements(By.XPATH,'//*[@id="scrollableDiv"]/div/div/div/a/div/div/p')


# for d in data:
for d in data:
    # d =data[i]
    try:
        Headlines.append(data[d].text)
    except:  
        Headlines.append("not_found_text")

print(Headlines)  

driver.quit()