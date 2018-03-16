'''
Created on 2018年3月14日
@author: rocky.wang
'''

import xlrd


wb = xlrd.open_workbook("ad.xlsx")

row_data = wb.sheets()[0]

print("表單數量：", wb.nsheets)
print("表單名稱：", wb.sheet_names())

#獲取第一個目標表單
sheet_0 = wb.sheet_by_index(0)

print("表單 %s 共 %d 行 %d 列" % (sheet_0.name, sheet_0.nrows, sheet_0.ncols))

print ("第三行第三列:", sheet_0.cell_value(2, 2))

#直接輸出日期

date_value = xlrd.xldate_as_tuple(sheet_0.cell_value(2,2), wb.datemode)
date1 = xlrd.xldate.xldate_as_datetime(sheet_0.cell_value(2, 2), wb.datemode)

print (date_value)#元組
print (date1)#日期


for s in wb.sheets():
    print(s.name)
    for r in range(s.nrows):
        print (s.row(r))

