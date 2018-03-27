'''
Created on 2018年3月26日
@author: rocky.wang
'''
import time


print("%02d" %(5)) 
print("{:02}".format(8))
# example 
dateText = "{}/{:02}/{:02}".format(1998, 8, 12)
print(dateText)

dateText = "%s/%02d/%02d" %(1911, 5, 7)
print(dateText)

ttime = str(int(time.time()*100))
print(ttime)
