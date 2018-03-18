'''
Created on 2018年3月18日
@author: Rocky
'''
from googlesheet02.googlesheetService import GooglesheetService

spreadsheetId = "1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw"

googlesheetService = GooglesheetService(spreadsheetId) # init service by spreadsheetId

title = "工作表七"

sheetId = googlesheetService.addSheet(title)
print(sheetId)

