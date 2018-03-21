'''
get Google Sheet all ranges data
 
Created on 2018年3月16日
@author: rocky.wang
'''
from __future__ import print_function

import json
from googlesheet.googlesheetUtils import buildService


def main():
    service = buildService()
    spreadsheetId = "1bydUUYVTxyyz2jxm3JRzIQkdElNthLHuQpzW6-DLVUk"
    
    ranges = [] # empty list means get all ranges data
    request = service.spreadsheets().get(spreadsheetId=spreadsheetId, ranges=ranges, includeGridData=False)
    response = request.execute()
    print(response)
    print("%s" %(json.dumps(response, indent=4)))


if __name__ == '__main__':
    main()