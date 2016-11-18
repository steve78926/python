#!/usr/loca/bin/python2.7
#encoding:utf8
#status: ok

import socket,sys,time
from threading import Thread

class tcpClient(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.host = '192.168.152.128'
        self.port = 8000
        self.bufsize = 4096
        self.client = None

    def run(self):
        try:
            self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
        except socket.error,(value,message):
            if self.client:
                print "client create fail: %s, application will exit(1)" % str(message)
                sys.exit(1)

        while True:
            send_data = raw_input("input command:")
            if send_data == 'stopcli':
                print "client application exit(1) after 3 second..."
                time.sleep(3)
                sys.exit(1)
            self.client.send(send_data)
            print "command has already been send"
            cmdoutput = self.client.recv(self.bufsize)
            print "command output:%s" % str(cmdoutput)

        self.client.close()

if __name__ == "__main__":
    t = tcpClient()
    t.start()
    t.join()