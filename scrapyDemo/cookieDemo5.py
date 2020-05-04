'''
selenium 透過 cookie 免登錄爬文

讀取 cookie，有效，但 facebook 仍然擋住要輸入密碼

Created on 2020年5月4日
@author: rocky
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import pickle


def main():
    
    
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print(cookies)
    driver.get("http://www.facebook.com")
    for cookie in cookies:
        print(cookie)
        cookie['expiry'] = int(cookie['expiry']) # 遇到 invalid argument: invalid 'expiry' 問題，裡面有浮點數，幫它轉成 int 
        driver.add_cookie(cookie)
    
    driver.get("http://www.facebook.com")    
    
    time.sleep(15)
    
    print("completed")


if __name__ == "__main__":
    main()