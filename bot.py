from selenium import webdriver 
from selenium.webdriver.common.by import By
import time



driver = webdriver.Firefox()
driver.get('https://aparat.com/mehrabkb')

links = driver.find_elements(By.CSS_SELECTOR , 'a[class~="titled-link"]')
time.sleep(20)
target_links = []
for link in links:
    target_links.append(link.get_attribute("href"))
print(len(target_links))
