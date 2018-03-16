'''
Created on 2018年3月13日
@author: Rocky
'''

from __future__ import print_function
from oauth2client import tools
from googlesheet.googlesheetUtils import buildService

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def main():
    
    service = buildService()

    spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"
     
#     body = {
#         "requests": [
#             {
#                 "addNamedRange": {
#                     "namedRange": {
#                         "namedRangeId" : "1234", 
#                         "name" : "Counts 2",
#                         "range": {
#                             "sheetId": 1324,
#                             "startRowIndex": 0,
#                             "endRowIndex": 3,
#                             "startColumnIndex": 0,
#                             "endColumnIndex": 5,
#                         },
#                     }
#                 }
#             }
#         ]
#     }
     
    body = {
      "requests": [
        {
          "addSheet": {
            "properties": {
              "title": "Deposits 2",
#               "gridProperties": {
#                 "rowCount": 20,
#                 "columnCount": 12
#               },
#               "tabColor": {
#                 "red": 0.2,
#                 "green": 0.3,
#                 "blue": 0.4
#               }
            }
          }
        }
      ]
    }
     
    request = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheetId, body = body)
    response = request.execute()
    
    print(response)


if __name__ == '__main__':
    main()