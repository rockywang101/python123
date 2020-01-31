'''
demo thread wait for finish and get return value

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
            return name + " fail"
    
    return name + " success"
        

with concurrent.futures.ThreadPoolExecutor() as executor:
    futureA = executor.submit(doSomething, "A")
    futureB = executor.submit(doSomething, "B")
    futureC = executor.submit(doSomething, "C")
    returnA = futureA.result()
    returnB = futureB.result()
    returnC = futureC.result()
    print("-------------------")
    print(returnA)
    print(returnB)
    print(returnC)

print("completed")