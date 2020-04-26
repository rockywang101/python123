'''
這是之前幫 chuck 寫爬幣時的程式，不過現在打開已經會 404 了

Created on 2018年4月20日
@author: rocky.wang
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime

driver = webdriver.Chrome()

driver.get("https://www.huobi.pro/zh-hk/eth_btc/exchange/")

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")

    primaryPrice = soup.find("div", {"class": "mod_hd"}).find("span", {"class": "ticker_close"}).text
    
    now = datetime.datetime.now()
    print("{}  {}".format(now.strftime('%H:%M:%S'), primaryPrice))

    # fetch left block each currency price
    elemList = soup.find("div", {"class": "coin_table"}).find("div", {"class": "coin_list"}).findAll("dl", {"action": "gourl"})
    cnt = 0
    for em in elemList:
        cnt += 1
        if cnt > 3:
            continue
        currency = em.find("div", {"class": "coin_unit"}).find("em", {"class": "base_currency"}).text
        price = em.find("span", {"price": "price"}).text
        colorBuy = em.find("span", {"rate": "rate"}).text 
        # find("span", {"class": "color-buy"}) 會找不到，不知道是不是 - 造成的

        print("{}\t{}\t{}".format(currency, price, colorBuy))
        
    print()    
    time.sleep(5)
