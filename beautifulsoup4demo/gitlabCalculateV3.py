'''
計算此次修正程式的程式碼增減行數 v2 - 貼上網址透過 selenium 自己執行

使用方法：
1. 複制網址
2. 執行 (selenium 去跑後續的)

因為這會關係到會不斷登入，且 V2 就蠻好用了，目前這版先不繼續寫下去

Created on 2020年4月29日
@author: rocky
'''
from bs4 import BeautifulSoup

with open("gitlab.html", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

trs = soup.find_all("tr", {"class": "line_holder old"})
removeLineCount = len(trs)
print(f"刪除行數: {removeLineCount}")
# for tr in trs:
#     td = tr.find_all("td")[2]
#     print(td.text) # print to debug if number is wrong

trs = soup.find_all("tr", {"class": "line_holder new"})
addLineCount = len(trs)
print(f"新簡行數: {addLineCount}")

clearLineCount = removeLineCount - addLineCount
print(f"精簡行數: {clearLineCount}")
