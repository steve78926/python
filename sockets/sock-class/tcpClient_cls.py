#coding:utf8

import socket
import random, threading

host = '127.0.0.1'
port = 8000
bufsize = 1024

def client():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect((host,port))

    for i in range(300):
        #rand_data = raw_input(">")
        rand_data = str(random.randint(1,2)) + random.choice(["A123456789BCDE"]) #总是发送空数据, 空数据可能是回车或者换行符，因此，服务端必须检查data是否为空
        print "rand_data: |%s|" % rand_data
        tcpCliSock.send(rand_data)
        print "randata have been send"
        recv_data = tcpCliSock.recv(bufsize)
        print "recive data:", recv_data

    tcpCliSock.close()

if __name__ == "__main__":
    client()
    print "threading end"
