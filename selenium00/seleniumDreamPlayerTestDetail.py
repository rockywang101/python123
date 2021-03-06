'''
Run Chrome quietly

Created on 2018年4月20日
@author: rocky.wang
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import os
    
def fetch():
    options = Options()
    driver = webdriver.Chrome(options=options)
    
    doLogin(driver)
    
    print("wait 10")
    time.sleep(10)
    
    driver.get('https://www.dreamplayer.tw/projects/intro/102/intro')
    
    time.sleep(3)
    
    driver.get("https://www.dreamplayer.tw/projects/102/articles/7343")
    time.sleep(5)
    pageDownToButtom(driver)
    with open("7343.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)    
            
    driver.close()
    driver.quit()
    
def parse():
    with open("7343.html", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    elem = soup.find("div", {"class": "cAecGH"})
    
#     print(elem.prettify())
    
    with open("7343pure.html", "w", encoding="utf-8") as f:
        print(str(elem))
        f.write(str(elem))
    

def doLogin(driver):
    driver.get("https://www.dreamplayer.tw")
    
    elem = driver.find_element_by_class_name("sc-dliRfk")
    elem.click()
    time.sleep(2)
    
    elem = driver.find_element_by_name("email")
    elem.clear()
    time.sleep(1)
    elem.send_keys("rswin0050@gmail.com")
    elem = driver.find_element_by_name("password")
    elem.clear()
    time.sleep(1)
    elem.send_keys(os.environ["RSWIN0050_PASSWD"])

#     elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_class_name("sc-hEsumM")
    elem.click()
    print("login end")
    
    
def pageDownToButtom(driver):
    body = driver.find_element_by_css_selector('body')
    
    for i in range(2):
        for j in range(8):
            body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
    

if __name__ == "__main__":
#     fetch()
    parse()

