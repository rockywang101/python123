'''
crawl Proxy List from https://www.us-proxy.org/

tip: 網站上 proxy list 的資料會一直更新，取最新的應該是最有效的

Created on 2020年5月4日
@author: rocky
'''
import requests
from bs4 import BeautifulSoup
import csv

def fetch():

    r = requests.get("https://www.us-proxy.org/")
    soup = BeautifulSoup(r.text, "html.parser")
    
    # when debug, don't call everytime
#     with open("proxyList.html", "w", encoding="utf-8") as f:
#         f.write(r.text)
#     with open("proxyList.html", encoding="utf-8") as f:
#         soup = BeautifulSoup(f.read(), "html.parser")

    rowList = []
    rowList.append(["IP Address", "Port", "Code", "Country", "Anonymity", "Google", "Https", "Last Checked"])
    for tr in soup.find(id="proxylisttable").find("tbody").find_all("tr"):
        row = []
        for td in tr.find_all("td"):
            row.append(td.text)
        rowList.append(row)
    
    with open("proxyList.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerows(rowList)

    print(rowList[0])
    print(rowList[1])
    print(rowList[-1])
    print(f"proxy list: {len(rowList)}")
    print("completed")
    
if __name__ == "__main__":
    fetch()