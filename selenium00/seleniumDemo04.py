'''

Created on 2018年4月20日
@author: rocky.wang
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime

driver = webdriver.Firefox()

driver.get("https://www.facebook.com/lifeinvestment168/")

while True:
    
    print(driver.page_source)
     
    soup = BeautifulSoup(driver.page_source, "html.parser")

    print()    
    time.sleep(30)
