'''

Created on 2018年4月20日
@author: rocky.wang
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Firefox()

driver.get("https://www.facebook.com/")

elem = driver.find_element_by_id("email")
elem.clear()
elem.send_keys("rockywang101@gmail.com")

elem = driver.find_element_by_id("pass")
elem.clear()
elem.send_keys(os.environ["MY_PASSWORD"])

elem.send_keys(Keys.RETURN)

time.sleep(5)

driver.get("https://www.facebook.com/greenbookstore/")


# while True:
#     
# #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     
#     print(driver.page_source)
#      
#     soup = BeautifulSoup(driver.page_source, "html.parser")
# 
#     print()    
#     time.sleep(60)
