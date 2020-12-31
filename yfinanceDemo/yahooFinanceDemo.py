'''
Created on 2020年5月5日

@author: rocky
'''
import requests
from bs4 import BeautifulSoup
stockId = "2884"
#url = f"https://finance.yahoo.com/quote/{stockId}.TW/history?p={stockId}.TW&.tsrc=fin-srch"

url = f'https://finance.yahoo.com/quote/{stockId}.TW/'

r = requests.get(url)

with open(f"yahoo123.html", "w", encoding="utf-8") as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, "html.parser")
price = soup.find('span', {'data-reactid': '14'}).text
print(price)
