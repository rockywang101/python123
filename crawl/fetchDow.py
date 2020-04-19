'''
Created on 2020年4月11日

@author: rocky
'''
import requests

from bs4 import BeautifulSoup
import time
import traceback

def main():
    text = "道瓊工業平均指數 "
    text = text + fetch("dow+jones+industrial+average")
    
    time.sleep(2)
    text = text + "\ns&p 500 "
    text = text + fetch("dow+jones+industrial+average")
    
    print(text)
    
    


def fetch(keyword):
    
#     url = "https://www.google.com/search?q=dow+jones+industrial+average&oq=dow&aqs=chrome.2.69i65j69i57j35i39j0l2j69i65l2j69i64.8659j0j7&sourceid=chrome&ie=UTF-8"
    url = "https://www.google.com/search?q=dow+jones+industrial+average"
    url = "https://www.google.com/search?q=s%26p500"
    url = "https://www.google.com/search?q=NASDAQ"
    url = "https://www.google.com/search?q=phlx+semiconductor"
    url = f"https://www.google.com/search?q={keyword}"
    
    print("GET " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    elem = soup.find("div", {"class", "BNeawe iBp4i AP7Wnd"}) # 裡面又包一樣的 
    price = elem.find("div", {"class", "BNeawe iBp4i AP7Wnd"}).text
    return price
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
#         lineTool.lineNotify(os.environ["LINE_TEST_TOKEN"], "crawlMoneydjETF 發生錯誤")
