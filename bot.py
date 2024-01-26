from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://aparat.com/mehrabkb')

links = driver.find_elements(By.CSS_SELECTOR , 'a[class~="titled-link"]')
time.sleep(20)
target_links = []
print(links)
f = open("links.txt" , "w") 
for link in links:
    target_links.append(link.get_attribute("href"))
    f.write(link.get_attribute("href") + '\n')
f.close()
print(len(target_links))
