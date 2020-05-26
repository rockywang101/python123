'''
解析網頁取得列表連結

Created on 2018年4月20日
@author: rocky.wang
'''

from bs4 import BeautifulSoup
    
# 取得文章列表
def parseTopicList():
    
    with open("topicList.html",  encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    elem = soup.find(id="full-width-tabpanel-1")
    divs = elem.find_all("div", {"class": "sc-eXNvrr fmDssR"})

    for div in divs:
        link = f'https://www.dreamplayer.tw{div.find("a").get("href")}'
        print(link)


if __name__ == "__main__":
    parseTopicList()

