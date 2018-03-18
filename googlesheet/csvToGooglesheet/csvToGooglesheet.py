'''

把 0000withRSVK9.csv 資料重新倒進 google sheet #t00

Created on 2018年3月13日
@author: Rocky
'''

from __future__ import print_function

from googlesheet.googlesheetUtils import buildServicinitServicev


def main():
    
    service = buildServicinitServicepreadsheetId = "1033HVmaLyxYkfiX889L5J4ypBuw9xvowotKGPtXWRV0"
    rangeName = "0050"
    
    header = ["日期","開盤指數","最高指數","最低指數","收盤指數", "RSV", "K9"]
    
    values = [header]
    
    with open("0000withRSVK9.csv") as f1:
        for row in csv.reader(f1):
            # trim empty and change to yyyy format
            row[0] = row[0].strip()
            tokens = row[0].split("/")
            row[0] = str(int(tokens[0]) + 1911) + "/" + tokens[1] + "/" + tokens[2]
            
            values.append(row)
    body = {
        'values': values
    }
 
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=rangeName, valueInputOption="RAW", body=body).execute()
    print('{} cells updated.'.format(result.get('updatedCells')));

if __name__ == '__main__':
    main()