'''
計算此次修正程式的程式碼增減行數 - 手動將網頁原始碼貼到檔案裡

使用方法：
1. 把 commit 的網址右鍵 -> 檢示網頁原始碼  (記得如果有 Expand all 要先按)
2. 把原始碼貼到 gitlab.html 檔裡
3. 執行得到精簡行數

Created on 2020年4月29日
@author: rocky
'''
from bs4 import BeautifulSoup

with open("gitlab.html", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

trs = soup.find_all("tr", {"class": "line_holder old"})
removeLineCount = len(trs)
print(f"新增行數: {removeLineCount}")
# for tr in trs:
#     td = tr.find_all("td")[2]
#     print(td.text) # print to debug if number is wrong

trs = soup.find_all("tr", {"class": "line_holder new"})
addLineCount = len(trs)
print(f"刪除行數: {addLineCount}")
# for tr in trs:
#     td = tr.find_all("td")[2]
#     print(td.text)

clearLineCount = removeLineCount - addLineCount
print(f"精簡行數: {clearLineCount}")
