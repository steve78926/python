#coding:utf8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9090))
print "bind %s:%d" % ('127.0.0.1',9090)
while True:
    data, addr = s.recvfrom(1024)
    print 'data: %s from %s' % (data,addr)
    s.sendto('hello,%s' % data, addr)


