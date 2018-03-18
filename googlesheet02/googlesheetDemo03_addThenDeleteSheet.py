'''
Demo add sheet and then delete it

Created on 2018年3月18日
@author: Rocky
'''
from googlesheet02.googlesheetService import GooglesheetService
import time

googlesheetService = GooglesheetService("1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw") # init service by spreadsheetId

sheetId = googlesheetService.addSheet("工作表七")

print("Add new sheetId %s, waiting 3 seconds then delete it" %(sheetId))
time.sleep(3)

googlesheetService.deleteSheet(sheetId)

