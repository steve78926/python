#-*- encoding:utf8 -*-

import os

def searchs(dirname):
    for d in os.listdir(dirname):
        if os.path.isdir(d):
            print d
            searchs(d)
        else:
            print "-" + d



if __name__ == '__main__':
    searchs('.')
