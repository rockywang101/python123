'''
Created on 2018年3月8日
@author: rocky.wang
'''

import datetime, csv

mp = {}
with open("holiday.csv", "r") as f1:
    for row in csv.reader(f1):
        print(row)
        mp[row[0]] = row[1]
print(mp) 

now = datetime.datetime.now()

final_day = datetime.datetime(2018, 12, 31)
print(final_day)

rowList = []
conti = True
while conti:
    now = now + datetime.timedelta(days=1)
    
    isWorkDay = 1
    # 六日
    if now.weekday() in (5, 6):
        if not mp.get(now.strftime('%Y/%m/%d')) == "1":
            isWorkDay = 0
    # 一到五
    else:
        if mp.get(now.strftime('%Y/%m/%d')) == "0":
            isWorkDay = 0
    
    rowList.append([now.strftime("%Y%m%d"), isWorkDay])
    
    if now.strftime("%Y%m%d") == '20181231':
        conti = False

with open("workdays.csv", "w", newline="\n") as f1:
    writer = csv.writer(f1)
    for row in rowList:
        writer.writerow(row)

with open("workdays.csv", "r") as f1:
    reader = csv.reader(f1)
    for row in reader:
        if row[1] == "0":
            print(row)
        
