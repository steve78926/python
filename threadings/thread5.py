# encoding: UTF-8
import threading
import time

# 商品
product = []
# 条件变量
con = threading.Condition()

# 生产者方法
def produce():
    global product
    if con.acquire():
        while True:
            if not product:
                print '生产者正在生产商品  '
                product.append("A")
                print "商品库：%s" % product

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)

# 消费者方法
def consume():
    global product
    if con.acquire():
        while True:
            if product:
                print '消费者购买商品'
                ret = product.pop()
                print "消费者得到商品:%s" % ret
                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            print "消费者等待商品..."
            con.wait()
            time.sleep(2)

p1 = threading.Thread(target=produce,name="producter1")
p2 = threading.Thread(target=produce,name="producter2")
c1 = threading.Thread(target=consume,name="customer1")
c2 = threading.Thread(target=consume,name="customer2")
c2.start()
c1.start()
p1.start()
p2.start()