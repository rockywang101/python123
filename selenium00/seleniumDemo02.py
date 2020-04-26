'''
Run Chrome quietly

Created on 2018年4月20日
@author: rocky.wang
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# 有沒有 executable_path 都可以，這行應該是給沒設 path 的人，或是想指定的人用的
# driver = webdriver.Chrome(options=options, executable_path="C:\\geckodriver\\geckodriver.exe")

driver.get("https://www.google.com/search?q=selenium")
soup = BeautifulSoup(driver.page_source, "html.parser")
for result in soup.find_all("div", {"class": "g"}):
    if (result.find("h3") != None):
        print(result.find("h3").text)

driver.close()
driver.quit()