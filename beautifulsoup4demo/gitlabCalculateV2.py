'''
計算此次修正程式的程式碼增減行數 v2 - 從 Windows 剪貼簿將 gitlab 取得複制的 gitlab 原始碼

使用方法：
1. 把 commit 的網址右鍵 -> 檢示網頁原始碼
2. ctrl + A -> ctrl + C  (全選，複制)
3. 執行此程式得到精簡行數

第一次需安裝
pip3 install pyperclip

Created on 2020年4月29日
@author: rocky
'''
from bs4 import BeautifulSoup
import pyperclip

html = pyperclip.paste();
soup = BeautifulSoup(html, "html.parser")

title = soup.find("h3", {"class": "commit-title"}).text.strip()
print(title)

link = soup.find("div", {"class": "inline-parallel-buttons"}).find("a").get("href")
link = "https://gitlab.etzone.net" + link.replace("&w=1", "").replace("?w=1", "") # 有展開全部時是 &w=1 沒有時是 ?w=1
print(link) 

trs = soup.find_all("tr", {"class": "line_holder old"})
removeLineCount = len(trs)
print(f"刪除行數: {removeLineCount}")
# for tr in trs:
#     td = tr.find_all("td")[2]
#     print(td.text) # print to debug if number is wrong
 
trs = soup.find_all("tr", {"class": "line_holder new"})
addLineCount = len(trs)
print(f"新增行數: {addLineCount}")
 
print(f"精簡行數: {removeLineCount - addLineCount}")