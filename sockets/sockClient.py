#encoding:utf8

import socket

host = '127.0.0.1'
port = 8000
bufsize = 1024

def Clinet():
    tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClientSock.connect((host,port))

    while True:
        data = raw_input("please input:")
        if data == "stopcli":
            break
        print "send data: %s" % data
        tcpClientSock.send(data)
        recvdata = tcpClientSock.recv(bufsize)
        print "receive data: %s..." % recvdata

    tcpClientSock.close()

if __name__ == '__main__':
    Clinet()