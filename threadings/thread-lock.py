#coding: utf8


import time, threading

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    start = time.time()
    for i in range(1000000):

        lock.acquire()
        try:
            change_it(n)
        finally:
          lock.release()
    end = time.time()                       #加锁与不加锁执行时间差10倍
    print "spend time: %f" % (end-start)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print balance