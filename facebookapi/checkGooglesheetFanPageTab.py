'''
檢查粉絲頁列表，建立尚未建立的 sheet

Created on 2018年3月19日
@author: rocky.wang
'''
from googlesheet02.googlesheetService import GooglesheetService
import requests
import json

# always effective
token = "EAABb6vxMesIBAISKgjO7L9kVIqESpB5B4ZCIKdlz7DBSSit2E09FkL9NIf6bUx5GsO7tXDFobtC4YfZAZCNldDZANJ7SsEPFEClEB5RlEie7hvvLymjVgzxXgwqbx7MZBfNZCeycTTK0zZB6sWMrbtIx0IQPbevQhAI6Y0c1xorqgZDZD"

googlesheetService = GooglesheetService("1bydUUYVTxyyz2jxm3JRzIQkdElNthLHuQpzW6-DLVUk") # init service by spreadsheetId

def main():
    
    rowList = googlesheetService.getValues("粉絲頁列表")
    
    checkTab(rowList)
     
    googlesheetService.updateSheet("粉絲頁列表", rowList)
        
def checkTab(rowList):
    
    for row in rowList:
        if len(row) > 1:
            continue
    
        print(row[0])
    
        id = row[0].split("/")[-2]
        # 處理像是「XXXX-OOOO-1616764821902568」，很搞怪的前面有中文，只有後面的「1616764821902568」是 id
        if "-" in id:
            id = id.split("-")[-1]

        fields = "id, name"
        url = 'https://graph.facebook.com/v2.10/{}?fields={}&access_token={}'.format(id, fields, token)
 
        response = requests.get(url)
        js = json.loads(response.text)
        
        googlesheetService.addSheet(js["name"])
        row.append(id)
        row.append(js["name"])
    
        
if __name__ == "__main__":
    main()