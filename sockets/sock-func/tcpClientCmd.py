#coding:utf8
#desc: 客户端向tcp server服务端发送命令，并获得命令执行的结果。对端文件：tcpServerCmd.py
#问题: 一次连接只能完成一个命令的执行，客户端若要发第二条命令，就需要重新启动.
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