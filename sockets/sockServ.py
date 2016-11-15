#coding: UTF-8
import socket
import random

#另外一种则可返回状态与调用的shell命令的输出结果
# >>> import commands
# status, output = commands.getstatusoutput('ls -l')

host = ''
port = 8000
bufsize = 1024


def Server():


    while True:
        tcpservSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpservSock.bind((host,port))
        tcpservSock.listen(5)
        print "waiting connect from ...."
        tcpCliSock, addr = tcpservSock.accept()
        print "new connect from ", addr
        data = tcpCliSock.recv(bufsize)
        if data == "stopserv":
            break
        with open(data,"r") as f:
            retdata = f.read()
        print "retdata=",retdata
        senddata = retdata + str(int(random.random() * 100))
        print "send-data:",senddata
        tcpCliSock.send(senddata)

    tcpCliSock.close()
    tcpservSock.close()

if __name__ == "__main__":
    Server()



