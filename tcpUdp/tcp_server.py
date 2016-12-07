#coding: utf8
import socket, threading

host = '127.0.0.1'
port = 8080
bufsize = 1024

def tcpHandler(cli, addr):
    print 'new connection from %s' % addr
    while True:
        data = cli.recv(bufsize)
        print 'data=%s' % data
        if data == 'exit' or not data:
            break
        cli.send('hello,%s' % data)
    print "exit handler loop"
    cli.close()
    print "close cli connect"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print 'waiting for connection....'

while True:
    cli, addr = sock.accept()
    t = threading.Thread(target=tcpHandler, args=(cli, addr))
    t.start()
    t.join()
print "exit main loop"
sock.close()