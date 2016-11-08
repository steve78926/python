#-*- coding:utf8-*-
#s
import threading

alist = None
condition = threading.Condition()

def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()

        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()

def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()

        for i in alist:
            print i,

        condition.release()

def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()

test = threading.Thread(target=doSet,name='test')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')

test.start()
tprint.start()
tcreate.start()