#coding:utf8

import socket,threading

host = '127.0.0.1'
port = 8000
bufsize = 4096
running = 1

def Client():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect((host,port))

    while running:
        cmd = raw_input("cmd:>")
        if cmd == "exitout":
            break
        tcpCliSock.send(cmd)
        retdata = tcpCliSock.recv(bufsize)
        print "返回结果：", retdata
    tcpCliSock.close()

if __name__ == "__main__":
    Client()