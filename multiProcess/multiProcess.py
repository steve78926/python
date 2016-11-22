#coding:utf8

from multiprocessing import Process
import os,time

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
    time.sleep(60)

if __name__ == '__main__':
    print 'Paraent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end'