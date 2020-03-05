'''
demo thread wait for finish and get return value

Created on 2020年1月31日
@author: rocky
'''
from random import randint
from time import sleep
from multiprocessing.pool import ThreadPool

def doSomething(name):
    for i in range(3):
        n = randint(1, 3)
        sleep(n)
        print(f"{name}  {n}")
        if n == 2:
            return name + " fail" # 遇到 2 當 fail
    
    return name + " success"
        

pool = ThreadPool(processes=1)

async_resultA = pool.apply_async(doSomething, ('A',))
async_resultB = pool.apply_async(doSomething, ('B',))
async_resultC = pool.apply_async(doSomething, ('C',))


returnA = async_resultA.get()
returnB = async_resultB.get()
returnC = async_resultC.get()

print("-------------------")
print(returnA)
print(returnB)
print(returnC)

print("completed.")