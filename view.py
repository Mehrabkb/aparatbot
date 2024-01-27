from selenium import webdriver 
import time

driverList = []
def view():
    f = open("links.txt" , "r")
    count = 0 
    for line in f.readlines():
        driver = webdriver.Firefox()
        driver.get(line)
        driverList.append(driver)
        print(driverList)
        time.sleep(4)     
    f.close()

def closeAllDrivers():
    for d in driverList:
        d.close()

view()
time.sleep(600)
closeAllDrivers()
for i in range(1, 300):
    view()
    time.sleep(700)
    closeAllDrivers()