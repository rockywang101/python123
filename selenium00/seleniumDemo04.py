'''

Created on 2018年4月20日
@author: rocky.wang
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def fetchToken():
        
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=options)
    
    print("開啟臉書")
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    print("進行登入")
    elem = driver.find_element_by_id("email")
    elem.clear()
    elem.send_keys("rockywang101@gmail.com")
    elem = driver.find_element_by_id("pass")
    elem.clear()
    elem.send_keys(os.environ["MY_PASSWORD"])
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    
    print("進入 API 頁面")
    driver.get("https://developers.facebook.com/tools/explorer")
    time.sleep(3)
    print("取得權杖")
    elem = driver.find_element_by_link_text("取得權杖")
    elem.click()
    time.sleep(1)
    print("取得用戶存取權杖")
    elem2 = driver.find_element_by_link_text("取得用戶存取權杖")
    elem2.click()
    time.sleep(1)
    print("取得存取權杖")
    elem3 = driver.find_element(By.XPATH, '//button[text()="取得存取權杖"]')
    elem3.click()
    time.sleep(3)
    
    inputList = driver.find_elements_by_class_name("_58al")
    token = inputList[2].get_attribute('value')
    print("取得 API Token: " + token)

    driver.close()
    return token

if __name__ == "__main__":
    token = fetchToken()
    
