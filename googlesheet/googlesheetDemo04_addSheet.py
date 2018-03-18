'''
Demo add googlesheet

Created on 2018年3月13日
@author: Rocky
'''
from googlesheet.googlesheetUtils import buildService
import time, json

def main():
    service = buildService()
    spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"
    
    title = "sheetOf{}".format(time.time()) # random timestamp to avoid same name 
     
    body = {
      "requests": [
            {
                "addSheet": {
                    "properties": {
                        "title": title,
                        #optional
#                         "gridProperties": {
#                             "rowCount": 20,
#                             "columnCount": 8
#                         },
#                         "tabColor": {
#                             "red": 0.2,
#                             "green": 0.3,
#                             "blue": 0.4
#                         }
                    }
                }
            }
        ]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body=body)
    response = request.execute()
    
    print(response) # one line print
    print("%s" %(json.dumps(response, indent=4))) # format print
    print("New created sheetId => %s, title => %s" %(response["replies"][0]["addSheet"]["properties"]["sheetId"], response["replies"][0]["addSheet"]["properties"]["title"]))


if __name__ == '__main__':
    main()
