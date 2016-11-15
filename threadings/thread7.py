#-*-encoding:utf8 -*-
#link: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832360548a6491f20c62d427287739fcfa5d5be1f000

import time,threading

def loop():
    print '%s is running..' % threading.currentThread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.currentThread().name, n)
    print 'thread %s end.' % threading.currentThread().name


def main():
    print 'thread %s is running...' % threading.currentThread().name
    t = threading.Thread(target=loop,name='LoopThread')
    t.start()
    t.join()
    print 'thread %s end..' % threading.currentThread().name

if __name__ == "__main__":
    main()