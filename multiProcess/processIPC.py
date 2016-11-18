#coding:utf8

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in [x for x in range(100)]:
        print ('Put %s to queue....' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Proces to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print ('Get %s from queue' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


