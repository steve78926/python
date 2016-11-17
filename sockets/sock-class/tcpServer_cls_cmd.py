#!/usr/local/bin/python2.7
#coding:utf8
#status: 未解决
'''
这个示例：socket, select, logging, threading
'''


import logging,commands
import sys
#from socket import socket
import socket,select
#from select import select
from threading import Thread

__author__ = 'songjh'

LOGFILE = "tcpServer.log"
logging.basicConfig(filename=LOGFILE,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(process)d %(message)s')

class tcpServer(object):
    def __init__(self):
        self.host = ''
        self.port = 8000
        self.Server = None
        self.threads = []

    def openSocket(self):
        try:
            self.Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.Server.bind((self.host,self.port))
            self.Server.listen(5)
        except socket.error,(value,message):
            if self.Server:
                print "create socket fail: %s" % message
                sys.exit(1)

    def tcpHandler(self):
        self.openSocket()
        input = [self.Server, sys.stdin]    #问题：这里加入sys.stdin, 45行就会报错: select.error: 10038  未解决
        running =1
        while running:
            print "等待新连接..."
            inputready, outputready, exceptready = select.select(input, [], [])
            for s in inputready:
                if s == self.Server:
                    client, address = s.accept()
                    t = requestHandler(client,address)
                    t.start()
                    self.threads.append(t)

        for th in self.threads:
            th.join()

        self.Server.close()
        print "Main tcpHandler thread has already exit"
        self.logger.info("Main tcpHandler thread has already exit")


class requestHandler(Thread):
    def __init__(self, client, address):
        Thread.__init__(self)
        self.client = client
        self.address = address
        self.bufsize = 4096
        self.logger = logging.getLogger(str(self.client.getpeername()))

    def run(self):
        print "新的连接来自 %s" % str(self.address)
        self.logger.info("new connect come from %s" % str(self.address))
        while True:
            recv_data = self.client.recv(self.bufsize)
            print "recv_data: %s " % str(recv_data)
            self.logger.info("recived data %s, from %s" % (str(recv_data),str(self.client.getpeername())))
            if not recv_data:
                print "recv data is null, the threader will exit"
                break
            elif recv_data == "stopserv":
                print "recive stopserv cmd, tcpServer will exit(100)"
                self.logger.info("recive stopserv cmd, tcpServer will exit(100)")
                sys.exit(100)
            status, output = commands.getstatusoutput(recv_data)
            print "command output: %s" % output
            print "command result send back to client "
            self.client.send(output)

        self.client.close()
        print "requestHandler thread has already exit"
        self.logger.info("requestHandler thread has already exit")

if __name__ == "__main__":
    tcpServer().tcpHandler()







