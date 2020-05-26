'''
5pa

Created on 2020年5月4日
@author: rocky
'''
import browser_cookie3
import requests
from bs4 import BeautifulSoup

def fetch():
    
    cookies = browser_cookie3.firefox()
    
    url = 'http://www.5pa.com.tw/5pa/forum.php?mod=forumdisplay&fid=123'
    
    r = requests.get(url, cookies=cookies)
    
    with open("5pa.html", "w", encoding="utf-8") as f:
        f.write(r.text)
        
def fetchTopic():        
    
    cookies = browser_cookie3.firefox()    
    url = 'http://www.5pa.com.tw/5pa/forum.php?mod=viewthread&tid=3482&extra=page%3D1'
    
    r = requests.get(url, cookies=cookies)
    
    with open("5pa_3482.html", "w", encoding="utf-8") as f:
        f.write(r.text)

def parse():
    
    with open("5pa.html", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    tbodys = soup.find_all("tbody")
    i = 0
    for tbody in tbodys:
        th = tbody.find("tr").find('th')
        if th.text == '':
            continue

        title = th.find("span").text
        link = th.find("a").get("href")
        print(title, link)
        print("-------------")
        i = i + 1
    
#     for tr in trs:
#         print(tr.find("th"))

if __name__ == "__main__":
    fetch()
    
    fetchTopic()
#     fetch()
#     parse()
    
    
            
    
    
    print("completed")
