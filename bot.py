from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://aparat.com/mehrabkb')

# this function to get elements by css selector 
def getElementsByCssSelector(selector=""):
    return driver.find_elements(By.CSS_SELECTOR , selector)
# this function to scroll page with counter and default counter = 3
def scrollPage(counter = 3):
    for i in range(0 , counter):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(6)

# this function get links and write to txt file 
def writeLinksInTxtFile(links):
    f = open("links.txt" , "w")
    for link in links : 
        f.write(link.get_attribute("href") + '\n')
    f.close()    

scrollPage(5)
links = getElementsByCssSelector('a[class~="titled-link"]')
writeLinksInTxtFile(links)

