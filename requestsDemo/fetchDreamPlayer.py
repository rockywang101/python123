'''

我想要測試一下是不是不用登入，就可以拿全部

Created on 2020年5月4日
@author: rocky
'''
import requests
from bs4 import BeautifulSoup
import csv

def fetch():

    data = {"pN": 1, "pA": 3, "tag": "", "id": "20191228105151825691"}

    r = requests.post("https://www.dreamplayer.tw/DreamPlayer/ajaxMoreSubs.do", data=data)
    
#     soup = BeautifulSoup(r.text, "html.parser")

    print(r.text)
    
    with open("topicListTest1.html", "w", encoding="utf-8") as f:
        f.write(r.text)

#     with open("proxyList.html", encoding="utf-8") as f:
#         soup = BeautifulSoup(f.read(), "html.parser")

if __name__ == "__main__":
    fetch()