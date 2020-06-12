'''
pip3 install pyquery

Created on 2020年5月4日
@author: rocky
'''
import requests
from pyquery import PyQuery
from bs4 import BeautifulSoup
from PIL import Image

def fetch():

#     url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=1256'
#     headers = {
#         "User-Agent" : "Chrome/31.0.1650.63"
#     }
#     r = requests.get(url, headers=headers)
#     r.encoding = 'utf-8'
#     
#     with open('1256.html', 'w', encoding='utf-8') as f:
#         f.write(r.text)
#     d = PyQuery(r.text)
    
    with open('1256.html', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    with open('1256.html', encoding='utf-8') as f:
        d = PyQuery(f.read())
        
    # 無法理解 pyquery 怎麼取值
#     for tr in d('#divFinDetail tr').items():
#         for td in tr('td'):
#             print(td.items())

    # 前兩行是 header 所以從 [2:] 開始
    for tr in soup.find(id='divFinDetail').find_all('tr')[2:]:
        tds = tr.find_all('td') 
        year = tds[0].text
        afterAmount = int(float(tds[11].text) * 100) # 稅後淨利
        
        
        print(year, afterAmount)

    
if __name__ == "__main__":
    fetch()