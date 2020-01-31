'''
demo thread wait for finish, cannot get return value

Created on 2020年1月31日
@author: rocky
'''
from threading import Thread
from random import randint
from time import sleep

def doSomething(name):
    for i in range(3):
        n = randint(1, 3)
        sleep(n)
        print(f"{name}  {n} {i}")
        if i == 3:
            return "fail"
    
    return "success"
        

t1 = Thread(target=doSomething, args=("A",)) # age 10 只是亂傳，沒有兩個以上的參數會報錯
t2 = Thread(target=doSomething, args=("B",))
t3 = Thread(target=doSomething, args=("C",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("completed")