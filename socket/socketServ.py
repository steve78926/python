#!/usr/local/bin/python2.7
#coding:utf8

#desc
# 1. 建立一个server类,创建openSocket方法,在该方法中创建socket对象，绑定并监听
# 2. 在server类中建立run方法, 调用openSocket方法，建立input 列表，进入死循环
#    调用select方法，取得input数据，如果input里的数据是socket对象
#    则调用worker线程处理连接对象
# 3. 建立worker类,处理连接对象发送来的数据：记录日志，并返回原数据

# sock, addr = s.accept()
#select的原型为(rlist,wlist,xlist[,timeout]),其中rlist是等待读取的对象，wlist是等待写入的对象，xlist是等待异常的对象，
# 最后一个是可选对象，指定等待的时间，单位是s.  select()方法的返回值是准备好的对象的三元组，
# 若在timeout的时间内，没有对象准备好，那么返回值将是空的列表。


import socket,logging,select,threading,sys

logfile = "server.log"
logging.basicConfig(filename=logfile,level=logging.NOTSET)
class Serverproc(object):
    def __init__(self):
        self.host = ''
        self.port = 8000
        self.size = 1024
        self.Server = None
        self.backlog = 5
        self.threads = []

    def openSocket(self):
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.bind((self.host,self.port))
            self.server.listen(backlog=5)
        except socket.error,(value,message):
            if self.server:
                self.server.close()
                print "open socket fail: %s " % message
                sys.exit(1)

    def run(self):
        self.openSocket()
        input = [self.server,sys.stdin]
        running = 1
        while running:
            inputready,outputready,exceptready = select.select(input,[],[])

            for s in inputready:
                if s == self.server:
                    c = Client(self.server.accept())
                    c.start()
                    self.threads.append(c)
                elif s == sys.stdin:
                    running = 0

        #关闭所有的线程， 为什么要关闭所有的线程
        self.server.close()
        for t in self.threads:
            t.join()

class Client(threading.Thread):
    def __init__(self,(client,address)):
        super(Client,self).__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        self.logger = logging.getLogger(str(self.client.getpeername()))

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            if data:
                self.client.send(data)
            else:
                self.client.close()
                running = 0

if __name__ == "__main__":
    s = Serverproc()
    s.run()







