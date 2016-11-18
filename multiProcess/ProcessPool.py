#!/usr/local/python2.7/bin/python2.7
#coding:utf8

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print("Run task %s (%s) ... " % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 300)
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end-start)))

if __name__ == '__main__':
    print ('Parent process %s ' % os.getpid())
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))

    print ('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')