'''
Created on 2020年5月21日

@author: rocky
'''

import requests
from bs4 import BeautifulSoup
from googleService import GooglesheetService


     

def main():
    
    stockIdList = fetchMyStockIdList()


    url = 'https://histock.tw/stock/gift.aspx'
    r = requests.get(url)
    with open("souvenir.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    # 當你不想每次要重爬紀念品資料時，可以 mark 上面
    with open("souvenir.html", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
      
    count = 0
    table = soup.find(id="CPHB1_gvOld")
    for tr in table.find_all("tr", {"class": "searchrow"}):
        count += 1
        stockId = tr.find_all("td")[0].text.strip()
        stockName = tr.find_all("td")[1].text.strip()
        lastBuyDate = tr.find_all("td")[3].text.strip()
        souvenir = tr.find_all("td")[7].text.strip()
        
        if stockId in stockIdList:
            print(stockId, stockName, lastBuyDate, souvenir)


def fetchMyStockIdList():
    stockIdList = []
    googlesheetService = GooglesheetService("1F3cT6ltHQ7gOYxCPSrPJGvMpUt3b5mRJIMR0gJ5ITr8")
    rowList = googlesheetService.getValues("觀察清單")
    for row in rowList[1:500]:
        if len(row) != 0:
            stockIdList.append(row[0])
        
    return stockIdList



        
main()

