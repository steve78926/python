#coding:utf8

import socket
import random, threading

host = '127.0.0.1'
port = 8000
bufsize = 1024

def client():
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect((host,port))
    rand_data = random.randint(1,1000)
    print "rand_data: %s" % rand_data
    tcpCliSock.send(str(rand_data))
    recv_data = tcpCliSock.recv(bufsize)
    print "recive data:", recv_data

def main():
    for i in range(10):
        t = threading.Thread(target=client)
        t.start()
        jt = t.join()
        print "jt=",jt

if __name__ == "__main__":
    main()
    print "threading end"


