'''
Created on 2018年5月21日
@author: rocky.wang
'''
import requests
from datetime import datetime
import json
import os

dt = datetime.now().strftime('%Y%m%d')
filename = f"daily_close_quotes_{dt}.json"


def main():
    
    js = readOrFetch()
    dataMap = {}
    for data in js['aaData'][90:100]:
        print(data)
        dataMap[data[0]] = data
        
    print(js['reportDate'])
    
def readOrFetch():
    if (os.path.isfile(filename)):
        print("file exist, read json data from file")
        with open(filename, encoding="utf-8") as f:
            js = json.load(f)
    else:
        print("file not exist, fetch from tpex website")
        js = fetchAndWriteToFile()
        
    return js
        
    # here if you want to print, don't need encode again, because file content is already utf-8
#     json_string = json.dumps(js, indent=4, ensure_ascii=False)
#     print(json_string)
    
def fetchAndWriteToFile():

    url = "http://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php"
    print(f"GET {url}")
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.3.2064119470.1586527709",
        "Host": "www.tpex.org.tw",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    }
    
    r = requests.get(url, headers=headers)
    js = r.json()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(js, f, indent=4, ensure_ascii=False)
    
    # print(r.json()) will print utf-8 word, but no formatted
    # if you want to pretty-print to console, you need to encode and decode
#     json_string = json.dumps(js, indent=4, ensure_ascii=False).encode("utf-8").decode()
#     print(json_string)
    return js
    

if __name__ == "__main__":
    main()    
