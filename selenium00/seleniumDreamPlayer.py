'''
Run Chrome quietly

Created on 2018年4月20日
@author: rocky.wang
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import os
    
def main():
    options = Options()
#     options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    doLogin(driver)
    
    topicList = fetchTopicList(driver)
    
    html = ""
    for topic in topicList:
        print(topic)
        msgDataListResult = fetchTopicDetail(driver, topic)

        html = html + f"<h1>{topic[0]}留言</h1>"        
        for msgDataList in msgDataListResult:
            html = html + f"<div>"
            for msgData in msgDataList:
                html = html + f"<p class='who'>{msgData[0]} <span class='time'>{msgData[1]}</span></p>"
                html = html + f"<p class='content'>{msgData[3]}</p>"
            html = html + f"</div>\n"
            html = html + "<br/><br/><br/>"
    
    with open("resp.html", "w", encoding="utf-8") as f1:
        f1.write(html)    
            
    driver.close()
    driver.quit()
    
    print("completed")
    


def doLogin(driver):
    driver.get("https://www.dreamplayer.tw")
    
    elem = driver.find_element_by_class_name("sc-dliRfk")
    elem.click()
    time.sleep(2)
    
    elem = driver.find_element_by_name("email")
#     print(elem.get_attribute('innerHTML'))
#     print(elem.get_attribute('outerHTML'))
#     print(elem)
    elem.clear()
    time.sleep(1)
    elem.send_keys("rswin0050@gmail.com")
    elem = driver.find_element_by_name("password")
    elem.clear()
    elem.send_keys(os.environ["RSWIN0050_PASSWD"])
    elem.send_keys(Keys.RETURN)
    

# 取得文章列表
def fetchTopicList(driver):
    
    retList = []
    # 溫國信文章列表
    driver.get("https://www.dreamplayer.tw/projects/intro/102/subscription")

    pageDownToButtom(driver)
    
    with open("topicList.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    topicList = soup.find(id="list_sub").find_all("li")
    for topic in topicList:
        title = topic.find("p", {"class": "title"}).text
        link = topic.find("a").get("href")
        retList.append([title, link])
            
    return retList

#TODO: 不要 hard code 往下拉的次數
def pageDownToButtom(driver):
    body = driver.find_element_by_css_selector('body')
    
    for i in range(3):
        for j in range(8):
            body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        
    # 目前先這樣 hard code 次數，理想上是判斷往下後沒有新文章後再停止

def fetchTopicDetail(driver, url):
    title = url[0].replace("?", "")
#     if (os.path.isfile(f"data\{title}.html")):
#         print("file exist, testing using, return direct")
#         with open(f"data\{title}.html", encoding="utf-8") as f:
#             html = f.read()
#             return parseHtml(html)
    
    print(f"find message in url {title}")
    link = "https://www.dreamplayer.tw" + url[1]
    driver.get(link)

    pageDownToButtom(driver)
    
    # 寫入以備後續使用
    with open(f"data\{title}.html", "w", encoding="utf-8") as f1:
        f1.write(driver.page_source)
    
    print("sleep 3 seconds")
    time.sleep(3)
    
    return parseHtml(driver.page_source)
    
    
def parseHtml(html):
    
#     with open("tmp1.html", encoding="utf-8") as f1:
#         html = f1.read()
    
    soup = BeautifulSoup(html, "html.parser")
    liList = soup.find(id="rForm").find_all("li", recursive=False)
    
    msgDataListResult = []
    # 每一個回覆串
    for li in liList:
        rightZone = li.find("div", {"class": "rightZone"})
        msgDataList = parseRightZone(rightZone)
        msgDataListResult.append(msgDataList)
    
    return msgDataListResult

    
    # 單獨一個拿出來測試而已
#     li = liList[2]
#     rightZone = li.find("div", {"class": "rightZone"})
#      
#     msgDataList = parseRightZone(rightZone)
#     for msgData in msgDataList:
#         print(msgData)
    
    
        
def parseRightZone(rightZone):
    
    msgDataList = []
    
    time = rightZone.find("p", {"class", "who"}).find("span").text.strip()
    name = rightZone.find("p", {"class", "who"}).text.strip().replace(time, "").strip() # 如果要拆開，把 \n 變成 split
    msgId = rightZone.find_all("p", recursive=False)[1].get("id").replace("messageP", "")
    msgText = rightZone.find_all("p", recursive=False)[1].text
    
    msgDataList.append([name, time, msgId, msgText])
    
    layer2nd = rightZone.find("ul", {"class", "layer2nd"})
    for li in layer2nd.find_all("li"):
        # 預設第一個有個奇怪的隱藏起來的回覆，還有 "看更多回覆" 都會只有一個 Div
        if len(li.find_all("div")) == 1:
            continue
        innerRightZone = li.find("div", {"class": "rightZone"})
        time = innerRightZone.find("p", {"class", "who"}).find("span").text
        name = innerRightZone.find("p", {"class", "who"}).text.replace(time, "")
        msgId = innerRightZone.find_all("p", recursive=False)[1].get("id").replace("messageP", "")
        msgText = innerRightZone.find_all("p", recursive=False)[1].text
        msgDataList.append([name, time, msgId, msgText])
        
    return msgDataList
    


if __name__ == "__main__":
    main()
#     parseHtml("")

