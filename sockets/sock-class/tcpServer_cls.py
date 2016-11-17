#!/usr/local/bin/python2.7
#coding:utf8
#status: ok
'''
这个示例包含: socket，select, 根据客户端连接产生新的处理线程，日志模块,日志格式
'''

import socket,sys,time,logging,select
import threading

LOGFILE = 'server_access.log'
logging.basicConfig(filename = LOGFILE,
                    level= logging.INFO,
                    format='%(asctime)s %(levelname)s %(threadName)s %(message)s'
                    )

class Server(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 8000
        self.bufsize = 1024
        self.threads = []
        self.server = None

    def openSock(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error,(value,message):
            print "socket create fail: %s" % str(message)    #sock server端执行第2次就会造成address,port占用冲突,只能执行一次
            if self.server:
                self.server.close()
                sys.exit(1)

    def Server(self):
        self.openSock()
        input = [self.server]
        print "等待新的连接...."
        while True:
            inputready, outputready, exceptready = select.select(input, [], [])     #使用select
            for s in inputready:
                client, address = s.accept()
                print "接受新的连接，产生新的处理线程"
                t = handler(client, address)
                t.start()
                self.threads.append(t)

        for ch in self.threads:
            ch.join()

        self.server.close()

class handler(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.bufsize = 1024
        self.logger = logging.getLogger(str(self.client.getpeername()))

    def run(self):
        print "new connect come from ",self.address
        self.logger.info("新的连接来自 %s", str(self.address))
        while True:                                     #循环的目的是分多次接受客户端一次发来的数据，直到收到空数据,才断开当前客户端的连接
            recv_data = self.client.recv(self.bufsize)
            self.logger.info("接收数据: %s 从地址: %s" % (str(recv_data), self.client.getpeername()))
            print "recv_leng==%d" % len(recv_data)
            if not recv_data:                           #必须检查数据为空
                print "接收的数据为空"
                break                               #如果接收的数据为空，跳出当前循环，并关闭client处理线程
            time.sleep(3)
            send_data = 'hello, %s' % recv_data
            print "send_data==%s" % send_data
            self.client.send(send_data)
            print "数据已经发送给客户端"
        self.client.close()

if __name__ == "__main__":
    Server().Server()



