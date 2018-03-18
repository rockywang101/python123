'''
Demo add googlesheet

Created on 2018年3月13日
@author: Rocky
'''
from googlesheet.googlesheetUtils import addSheet
import time

def main():
    spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"
    
    title = "sheetOf{}".format(time.time()) # random timestamp to avoid same name 
    
    sheetId = addSheet(spreadsheetId, title)
    
    print("New created sheetId => %s" %(sheetId))
    

if __name__ == '__main__':
    main()
