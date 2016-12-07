#coding: utf8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1',9090)
for data in ['mike','tom', 'john']:
    s.sendto(data,addr)
    print 'send data: %s' % data
    print s.recvfrom(1024)
s.close()
print 'close udp sock'