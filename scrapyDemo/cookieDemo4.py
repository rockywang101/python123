'''
selenium 透過 cookie 免登錄爬文

寫入 cookie

Created on 2020年5月4日
@author: rocky
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pickle


def main():
    
    
#     cookies = browser_cookie3.chrome()
    
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    doLogin(driver)
    
    pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))
    
    print("completed")


def doLogin(driver):
    driver.get("https://www.facebook.com/")
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys("rockywang101@gmail.com")
    elem = driver.find_element_by_name("pass")
    elem.clear()
    elem.send_keys("yourpassword")
    elem.send_keys(Keys.RETURN)


if __name__ == "__main__":
    main()