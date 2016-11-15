#coding:utf8

import threading, socket,select

host = '127.0.0.1'
port = 8000
bufsize = 1024



def openSock():
    tcpServSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServSock.bind((host,port))
    tcpServSock.listen(5)
    return tcpServSock

def Server():
    server = openSock()
    input = [server]
    while True:
        print "waiting for connect...\n"
        inpurready, outputready, exceptready = select.select(input, [], [])
        print "inputready=%s" % inpurready
        for s in inpurready:
            tcpCliSock, addr = s.accept()
            t = threading.Thread(target=Client, args=(tcpCliSock, addr))
            t.start()

def Client(tcpCliSock, address):
    print "new connect from" , address
    recv_data = tcpCliSock.recv(bufsize)
    print "recive date: %s" % recv_data
    send_data = "hello, %s" % recv_data
    tcpCliSock.send(send_data)

if __name__ == "__main__":
    Server()



