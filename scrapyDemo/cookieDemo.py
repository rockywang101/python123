'''
先在 Firefox 登錄過後，執行此程式，以 browser 打開 facebook.html 即可看到取得的是登入後的內容

關鍵是 python3 要用 browser_cookie3
 
Created on 2020年5月4日
@author: rocky
'''
import browser_cookie3
import requests

cookies = browser_cookie3.firefox()

url = 'https://www.facebook.com/'

r = requests.get(url, cookies=cookies)

with open("facebook.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("completed")
