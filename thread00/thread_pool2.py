'''
demo thread wait for finish and get return value (raising Exception)

Created on 2020年1月31日
@author: rocky
'''
from random import randint
from time import sleep
import concurrent.futures

def doSomething(name):
    for i in range(3):
        n = randint(1, 3)
        sleep(n)
        print(f"{name}  {n}")
        if n == 2:
            raise Exception("ha ha")
#            return name + " fail" # 遇到 2 當 fail

    
    return name + " success"
        

with concurrent.futures.ThreadPoolExecutor() as executor:
    returnA = None
    returnB = None
    returnC = None
    try:
        futureA = executor.submit(doSomething, "A")
        futureB = executor.submit(doSomething, "B")
        futureC = executor.submit(doSomething, "C")
        returnA = futureA.result()
        returnB = futureB.result()
        returnC = futureC.result()
    except Exception as e:
        print("-------------------")
        print(returnA)
        print(returnB)
        print(returnC)

print("completed.")