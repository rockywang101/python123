'''
Created on 2020年5月4日
@author: rocky
'''
import browser_cookie3
import requests

cookies = browser_cookie3.firefox()
for cookie in cookies:
    print(cookie)

url = 'http://www.5pa.com.tw/5pa/forum.php?mod=forumdisplay&fid=123'

r = requests.get(url, cookies=cookies)

with open("5pa.html", "w", encoding="utf-8") as f:
    f.write(r.text)


print("completed")
