#coding:utf8
#desc: 类方式实现
import threading,random,time

mqlist = []
con = threading.Condition()

class Producter(threading.Thread):
    def run(self):
        global mqlist
        if con.acquire():
            while True:
                if not mqlist:
                    print "无库存,%s正在生产商品" % threading.currentThread().getName()
                    po = int(random.random() * 100 )
                    mqlist.append(po)
                    print "商品已经生产，ID：%d " % po

                    con.notify()
                    print "商品生成完成，正在通知顾客购买"

                con.wait()
                time.sleep(1)

class Customer(threading.Thread):
    def run(self):
        global mqlist
        if con.acquire():
            while True:
                if mqlist:
                    po = mqlist.pop()
                    print "顾客:%s 购买了商品，ID:%d" % (threading.currentThread().getName(),po)

                    con.notify()
                    print mqlist
                    print "库存空，正在通知生产"

                con.wait()
                time.sleep(1)

def main():
    Producter().start()
    Customer().start()

if __name__ == "__main__":
    main()

