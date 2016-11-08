#coding:utf8
#status: fail
#time : 2016-11-8 11:33 status: ok

import threading
import time
import random

con = threading.Condition()
qlist = []

def producter():
    global qlist
    if con.acquire():
        while True:
            if not qlist:
                print "当前没有商品，正在生产商品"
                p = int(random.random() * 1000)
                qlist.append(p)
                time.sleep(1)
                print "已经生产商品: %d" % p

                con.notify()
                print "通知商品已经生产"

            con.wait()
            time.sleep(2)

def customer():
    global qlist
    if con.acquire():
        while True:
            if qlist:
                print "库里有商品"
                ret = qlist.pop()
                print "顾客得到商品： %s" % ret
                print "商品库状态：%s" % qlist
                con.notify()
            con.wait()
            time.sleep(2)

def main():
    print "main thread start..."
    p = threading.Thread(target=producter,name="producter")
    c = threading.Thread(target=customer,name="customer")
    p.start()
    c.start()
    p.join()
    c.join()
    print "main thread end"

if __name__ == "__main__":
    main()