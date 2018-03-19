'''
Demo fetch Facebook FanPage data

Created on 2018年3月19日
@author: rocky.wang
'''
from googlesheet02.googlesheetService import GooglesheetService

'''
Created on 2018年3月13日
@author: rocky.wang
'''
import requests
import json


token = "EAABb6vxMesIBAISKgjO7L9kVIqESpB5B4ZCIKdlz7DBSSit2E09FkL9NIf6bUx5GsO7tXDFobtC4YfZAZCNldDZANJ7SsEPFEClEB5RlEie7hvvLymjVgzxXgwqbx7MZBfNZCeycTTK0zZB6sWMrbtIx0IQPbevQhAI6Y0c1xorqgZDZD"

sheetService = GooglesheetService("1bydUUYVTxyyz2jxm3JRzIQkdElNthLHuQpzW6-DLVUk")


def fetchPostPictures(postId):
    fields = "attachments"
    url = 'https://graph.facebook.com/v2.10/{}?fields={}&access_token={}'.format(postId, fields, token)
    response = requests.get(url)
    js = json.loads(response.text)
    print(js)
    picUrlList = []
    for data in js["attachments"]["data"][0]["subattachments"]["data"]:
        picUrlList.append(data["media"]["image"]["src"])
    return picUrlList


def main():
    
    rowList = sheetService.getValues("粉絲頁列表")
    for row in rowList:
        fanPageId = row[1]
        rangeName = row[2]
        fetchFanPage(fanPageId, rangeName)

def fetchFanPage(fanPageId, rangeName):
    
    # 取已經寫入過的 post id
    existPostIds = getExistPostIds(rangeName)
    # 取前 25 筆貼文
    rowList = crawlFanpageData(fanPageId)
    # 過濾剩下沒寫入過的貼文
    rowList = [row for row in rowList if not row[0] in existPostIds]

    # 寫入 google sheet
    sheetService.appendSheet(rangeName, rowList)
    
    
def crawlFanpageData(fanPageId):
    
    fields = "id, name, posts{id,name,message,created_time,permalink_url}"
    url = 'https://graph.facebook.com/v2.10/{}?fields={}&access_token={}'.format(fanPageId, fields, token)
    print("GET %s" %(url))
    js = json.loads(requests.get(url).text)
    print(js)
    
    rowList = [["ID", "Message", "Time", "Notify", "PostUrl"]]
    for data in js["posts"]["data"]:
        print(data)
        if data.get("message", "") == "":
            print("empty, put some value")
            data["message"] =  "分享了 " + data["name"] + " 的資料" 
                                
        rowList.append([data["id"], data['message'], data["created_time"], "Not Yet", data["permalink_url"]])
    
    return rowList
    
    
def getExistPostIds(rangeName):
    sheetRows = sheetService.getValues(rangeName)
    existPostIds = []
    for row in sheetRows:
        existPostIds.append(row[0])
    return existPostIds



if __name__ == "__main__":
    main()
