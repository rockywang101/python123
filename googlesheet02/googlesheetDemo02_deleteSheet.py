'''
Demo delete sheet

Created on 2018年3月18日
@author: Rocky
'''
from googlesheet02.googlesheetService import GooglesheetService

googlehseetService = GooglesheetService("1CxCM_fOzFAySeg7pDs5g0SPCHOkxJFGQaisru3iC6Lw") # init service by spreadsheetId

sheetId = 318938055
googlehseetService.deleteSheet(sheetId)

