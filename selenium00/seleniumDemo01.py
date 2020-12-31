'''
Demo how to use selenium to open python website

1. download geckodriver.exe from https://github.com/mozilla/geckodriver/releases
2. put it in a folder
3. add this folder into your PATH  
4. remember to restart eclipse
5. run ! 

20200426 try firefox
Unable to find a matching set of capabilities

so i change to using Chrome

我在 windows 的 Path 裡有多設定一個 C:\selenium_driver

see your chrome version
chrome://settings/help

and download one match your version
https://chromedriver.chromium.org/downloads

Created on 2018年4月20日
@author: rocky.wang
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
driver.quit()

print('comp')
