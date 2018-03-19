'''
Demo clear sheet content and update again

fomat clear will not be clear, example, if you set center of cell

Created on 2018年3月18日
@author: Rocky
'''
from googlesheet02.googlesheetService import GooglesheetService
import time

googlesheetService = GooglesheetService("1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw") # init service by spreadsheetId

rangeName = "工作表七" # ensure you have a sheet named it

rowList = googlesheetService.getValues(rangeName)

for row in rowList:
    print(row)

