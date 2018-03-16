'''
Read data from Google Sheet
 
Created on 2018年3月16日
@author: rocky.wang
'''
from googlesheet.googlesheetUtils import buildService

def main():
    
    service = buildService()

    spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"
    rangeName = "TEST"
    
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    for row in values:
        print(row)







if __name__ == '__main__':
    main()




