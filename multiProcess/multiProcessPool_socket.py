#!/usr/local/bin/python2.7
#coding:utf8
'''
该示例： 用进程池里的多个进程处理新连接
'''


__author__ = 'steve'
import socket,sys,select
from multiprocessing import Pool


class tcpServer(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 8000

    def openSocket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error, (value,message):
            if self.server:
                self.server.close()
                print "create socket fail: %s, socket exit" % message
                sys.exit(1)

    def connHander(self):
        print "wait for new connect..."
        self.openSocket()
        p = Pool(4)
        input = [self.server]
        print "pool create"
        while True:
            inputready, outputready, execptready = select.select(input, [], [])
            for s in inputready:
                client, address =s.accept()
                print "connect accept()"
                for i in range(5):
                    p.apply_async(reqHandler,args=(client, address))

                p.close()
                p.join()
        self.server.close()

class reqHandler(object):
    def __init__(self, client, address):
        self.client = client
        self.address = address
        self.bufsize = 1024

    def handler(self):
        print "new connect come from %s"  % str(self.address)
        while True:
            recv_data = self.client.recv(self.bufsize)
            if not recv_data:
                break
            send_data = 'hello, %s' % recv_data
            self.client.send(send_data)
            print "send_data has been send"

        self.client.close()

if __name__ == '__main__':
    tcps = tcpServer()
    tcps.connHander()
