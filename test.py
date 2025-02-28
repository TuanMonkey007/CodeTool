#write a program to test selenium 
import requests 
from time import time 
from selenium import webdriver

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://www.google.com/")   
print(driver.title)     
driver.close()      
driver.quit()
