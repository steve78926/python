#coding:utf8
#desc: 递归输出当前目录下的子目录和文件
#author: me
import os
import time

def dirlist(pathname,level=1):
    if level == 1:
        print "%s" % pathname
    for d in os.listdir(pathname):
        time.sleep(1)
        print('%s|-- %s' %('|   '* (level-1),d))    #这一行控制树形的格式，level 控制输入 | 的数量，当前层级减1
        if os.path.isdir(os.path.join(pathname,d)):     #必须用os.path.join(pathname,d) 这个函数，否则无法进入第3层子目录
            dirlist(os.path.join(pathname,d),level+1)   #level 控制输入 | 的数量,每深入一层，| 数量加1

dirlist(".")