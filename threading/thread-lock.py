#-*- encoding:utf8-*-
#link: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832360548a6491f20c62d427287739fcfa5d5be1f000
#desc： Lock
#date: 2016-11-8

import time, threading

balance = 0
lock = threading.Lock()

def run_thread(n):
    global balance
    for i in range(10000):
        try:
            lock.acquire()   #锁定下面两行代码段
            balance += n
            balance -= n
        finally:
            lock.release()  #修改共享变量变成，释放锁
            #print "balance=%d" % balance

def main():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print balance

if __name__ == '__main__':
    main()