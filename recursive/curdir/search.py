#-*- encoding:utf8 -*-
#status: fail

import os

def scandir(startdir, target) :
    os.chdir(startdir)
    for obj in os.listdir(os.curdir) :
        if obj == target :
            print os.getcwd() + os.sep + obj
        if os.path.isdir(obj) :
            scandir(obj, target)
            os.chdir(os.pardir) #!!!

if __name__ == '__main__':
    listdir('.')
