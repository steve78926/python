#-*- conding:utf8 -*-

import threading

product_list = []
cond = threading.Condition()

def producter():
    global product_list
    if cond.acquire():
        product_list.append("A")
        print "product_list= %s" % product_list
        cond.notify()
    cond.release()

def customer():
    global product_list
    if cond.acquire():
        if not product_list:
            print "now no date, %s wait to product data" % threading.currentThread().getName()
            cond.wait()
        rest = product_list.pop()
        print "%s get a %s" % (threading.currentThread().getName(),rest)
        print "product_list= %s" % product_list
        cond.release()

def main():
    print "main Thread start"

    plist = []
    clist = []
    for i in range(5):
        p = threading.Thread(target=producter)
        plist.append(p)

    for i in range(5):
        c = threading.Thread(target=customer)
        clist.append(c)

    for p,c in [plist,clist]:
        p.start()
        c.start()

    print "main Thread end"

if __name__ == '__main__':
    main()