#coding:utf8
#status: fail

import threading
import time
qlist = []
con = threading.Condition()

def producter():
    global qlist
    if con.acquire():
        while True:
            if not qlist:
                print "当前没有商品，正在生产商品"
                qlist.append("A")
                print "已经生产商品A"

                con.notify()
                print qlist
                print "producter notifi..."
            print "product waitting..."
            con.wait()
            con.release()
            time.sleep(2)

def customer():
    global qlist
    print "customer start ..."
    if con.acquire():
        while True:
            if qlist is not None:
                print "qlist is true"
                qlist = None
                print "customer get %s" % qlist
                con.notify()
            con.wait()
            time.sleep(2)

def main():
    print "main thread start..."
    p = threading.Thread(target=producter,name="producter")
    c = threading.Thread(target=customer,name="customer")
    p.start()
    c.start()
    print "main thread end"

if __name__ == "__main__":
    main()