'''
Demo delete a googlesheet

Created on 2018年3月13日
@author: Rocky
'''
from googlesheet.googlesheetUtils import buildService

def main():
    service = buildService()
    spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"
    
    sheetId = 1640883652
     
    body = {
        "requests": [
            {
              "deleteSheet": {
                "sheetId": sheetId
              }
            }
        ]
    }
     
    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body=body)
    response = request.execute()
    print(response)

if __name__ == '__main__':
    main()