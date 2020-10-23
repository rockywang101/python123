'''
Created on 2018年3月29日
@author: rocky.wang
'''
from datetime import datetime
import time

now = datetime.now()

print(now)

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)


# get timestamp
now = time.time()
print(now)


def add():
    for i in range(5000000):
        i = i + 1

a = time.time()
begin = time.perf_counter() # 已是秒數表示，不用看 timestamp 看不是很懂過了幾秒
print(a)
print(begin) 
print('--------------------')

add()
b = time.time()
middle = time.perf_counter()
print(b-a)
print(middle-begin)

add()
c = time.time()
end = time.perf_counter()    
print(f'{c-b:0.4f}')
print(f'{end-middle:0.4f}')

