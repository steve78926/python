#coding:utf8

import socket
import threading

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
        except socket.error:
            print "socket create fail"   #sock server端执行第2次就会造成冲突,只能执行一次

        while True:
            print "wait for connect..."
            client, address = self.server.accept()
            print "new connect come from ", address
            while True:
                retdata = client.recv(2048)
                print "recv data:%s" % retdata
                if retdata == "stop":
                    break
                elif not retdata:
                    print "recv data null"
                    break       #必须检查 retdata 是否为空，如果为空，必须中断当前循环
                send_data = "helloss" + retdata
                print "send_data=",send_data
                client.send(send_data)
            client.close()
        self.server.close()

if __name__ == "__main__":
    Server().openSock()



