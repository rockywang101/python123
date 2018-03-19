'''
fetch fanPageData on google sheet and notify

Created on 2018年3月19日
@author: rocky.wang
'''
from googlesheet02.googlesheetService import GooglesheetService
import lineTool
import os

sheetService = GooglesheetService("1bydUUYVTxyyz2jxm3JRzIQkdElNthLHuQpzW6-DLVUk")


def main():
    
    rangeName = "華倫存股 穩中求勝"

    rowList = sheetService.getValues(rangeName)
    # filter not notify topics
    notifyRowList = [row for row in rowList if row[3] != "OK"]

    rowListToMessage(notifyRowList, rangeName)
    
    # update notify status
    for row in rowList:
        row[3] = "OK"
    
    rowList = sheetService.updateSheet(rangeName, rowList)

def rowListToMessage(rowList, rangeName):
    
    message = ""
    for row in rowList:
        dt = row[2][0:10] + " " + row[2][11:16]
        message += "------------------------------------------\n[%s] [%s]\n------------------------------------------\n" %(rangeName, dt)
        message += row[1] + "\n原文連結: " + row[4] + "\n\n"

    print(message)
    
    lineTool.lineNotify(os.environ["LINE_TEST_TOKEN"], message)

if __name__ == "__main__":
    main()
