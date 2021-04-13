# multithreading in python

from time import sleep
from threading import *

class thread1(Thread):
    def run(self):
        for i in range(5):
            print("hello world")
            sleep(1)

class thread2(Thread):
    def run(self):
        for i in range(5):
            print("hi everyone")
            sleep(1)

t1 = thread1()
t2 = thread2()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()

print("main thread execution")
