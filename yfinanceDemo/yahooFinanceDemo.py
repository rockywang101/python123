'''
Created on 2020年5月5日

@author: rocky
'''
import requests
from bs4 import BeautifulSoup
stockId = "4205"
url = f"https://finance.yahoo.com/quote/{stockId}.TWO/history?p={stockId}.TWO&.tsrc=fin-srch"

r = requests.get(url)

with open("4205.html", "w", encoding="utf-8") as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, "html.parser")
elem = soup.find("span", {"class": "Trsdu(0.3s)"})
print(elem)
