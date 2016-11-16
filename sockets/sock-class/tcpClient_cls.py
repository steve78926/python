#coding:utf8

import socket
import random, threading

host = '127.0.0.1'
port = 8000
bufsize = 1024

def client():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect((host,port))

    for i in range(3):
        rand_data = random.choice(["abcde", "defakl", "ujikol", "qweafrf"])
        print "rand_data: |%s|" % rand_data
        tcpCliSock.send(rand_data)
        recv_data = tcpCliSock.recv(bufsize)
        print "recive data:", recv_data

    tcpCliSock.close()

if __name__ == "__main__":
    client()
    print "threading end"
