'''
Created on 2018年3月9日
@author: rocky.wang
'''
import os

def hello(token, ar1):
    pass



with open("c:\\users\\eit\\downloads\\3.20-21.txt") as f1:
    lines = f1.read().splitlines()
    
print(len(lines))

msg = ""
for line in lines:
    msg += line + ", "

print(msg)
    
        