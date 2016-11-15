#coding:utf8

import socket
import commands
import threading
from select import select

host = '127.0.0.1'
port = 8000
bufsize = 4096

def openSock():
    tcpServSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServSock.bind((host,port))
    tcpServSock.listen(5)
    return tcpServSock

def Server():
    server = openSock()
    input = [server]
    while True:
        print "waiting for connect..."
        inputready, outputready, exceptready = select(input, [], [])
        for s in inputready:
            cli, addr = s.accept()
            t = threading.Thread(target=Client, args=(cli,addr))
            t.start()
            t.join()

    server.close()

def Client(client, address):
    print "new connect from" , address
    cmd = client.recv(bufsize)
    if cmd:
        print "cmd is %s" % cmd
    status, output = commands.getstatusoutput(cmd)
    if not status:
        print "命令执行成功, 返回码:%d" % status
    else:
        print "命令执行失败, 返回码:%d" % status

    print "命令执行结果: %s" % output
    #client.send(str(status))
    client.send(output)

if __name__ == "__main__":
    Server()