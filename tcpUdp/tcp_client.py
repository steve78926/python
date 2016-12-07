#coding:utf8

import socket

host = '127.0.0.1'
port = 8080
bufsize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

for data in ['mike', 'tom', 'john']:
    sock.send(data)
    print sock.recv(1024)
sock.send('exit')
sock.close()
