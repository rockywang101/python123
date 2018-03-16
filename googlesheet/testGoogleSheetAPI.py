'''
Created on 2018年3月13日
@author: Rocky
'''

from __future__ import print_function

from googlesheet.googlesheetUtils import buildService


def main():
    service = buildService()

    spreadsheetId = "1033HVmaLyxYkfiX889L5J4ypBuw9xvowotKGPtXWRV0"
    
    include_grid_data = False  # TODO: Update placeholder value.
    ranges = [] # empty list means all ranges
    request = service.spreadsheets().get(spreadsheetId=spreadsheetId, ranges=ranges, includeGridData=include_grid_data)
    response = request.execute()
    print(response)


#     rangeName = "T00"
#     
#     result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
#     values = result.get('values', [])
#  
#     for row in values:
#         print(row)


if __name__ == '__main__':
    main()