'''
Created on 2018年3月14日
@author: rocky.wang
'''
import xlwt

# create workbook
wb = xlwt.Workbook()

sh = wb.add_sheet('A new sheet')

sh.write(0, 0, 'hello')
sh.write(1, 0, 'world')
sh.write(2, 0, 1234567)
sh.write(2, 1, '2017-04-10')

wb.save('xlwt_test.xlsx')
