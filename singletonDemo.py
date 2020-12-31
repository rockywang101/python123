'''
Singleton demo

Created on 2020年7月8日
@author: rocky
'''
import time

class SingleTonNew: 
    
    _instance = None 
    
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
        return cls._instance 
         
    def __init__(self, a, b): 
        self.a = a 
        self.b = b

st = set()
for i in range(1000):
    s = SingleTonNew(a=i*2, b=i)
    st.add(takeSomeTimeTasks))

# 當拿掉 __new__ 時，會發現其實產生的數量並不是 range 裡面的數字，可能只是 2 ~ 3 個而已
# 應該是 python 本身做的一些節約的機制吧
print(len(st))
