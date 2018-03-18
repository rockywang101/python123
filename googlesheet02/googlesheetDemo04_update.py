'''
Demo update sheet content

Created on 2018年3月18日
@author: Rocky
'''
from googlesheet02.googlesheetService import GooglesheetService

googlesheetService = GooglesheetService("1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw") # init service by spreadsheetId

rangeName = "工作表七" # ensure you have a sheet named it

row1 = ["stockd", "price", "amount"]
row2 = ["0050", 80.70, 2500]
row3 = ["2317", 90.70, 8500]
rowList = [row1, row2, row3]

googlesheetService.updateSheet(rangeName, rowList)

