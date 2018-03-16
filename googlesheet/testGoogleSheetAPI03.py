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

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def main():
    
    service = buildService()


    # The spreadsheet to apply the updates to.
    spreadsheet_id = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"  # TODO: Update placeholder value.
     
    batch_update_spreadsheet_request_body = {
        # A list of updates to apply to the spreadsheet.
        # Requests will be applied in the order they are specified.
        # If any request is not valid, no requests will be applied.
     
        "requests": [
            {
              "deleteSheet": {
                "sheetId": 600863499
              }
            }
        ]
     
        # TODO: Add desired entries to the request body.
    }
     
    request = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet_id, body = batch_update_spreadsheet_request_body)
    response = request.execute()
    
    
    # create a untitle new sheet, everything is default value
#     spreadsheet_body = {
#         # TODO: Add desired entries to the request body.
#     }
#     
#     request = service.spreadsheets().create(body=spreadsheet_body)
#     response = request.execute()
    
    # TODO: Change code below to process the `response` dict:
    print(response)

#     values = [
#         [1, 3, "ABC"],
#         [2, 4, "Rox"]
#     ]
#     
#     body = {
#         'values': values
#     }
# 
#     spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"
#     rangeName = "TEST"
# 
#     result = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range=rangeName, valueInputOption="RAW", body=body).execute()
#     print('{0} cells updated.'.format(result.get('updatedCells')));


if __name__ == '__main__':
    main()