#coding:utf8
#date :2016-11-12

import logging

logfile = "test.log"
logging.basicConfig(filename=logfile,level=logging.ERROR,)
logging.debug("this is test log file")
logging.error('error')

logger1 = logging.getLogger("package.module1")   #派生出第1个日志对象,对应线程1
logger2= logging.getLogger("package.module2")   #派生出第2个日志对象，对应线程2

logger1.warning("this message come from modul1 ")
logger2.warning("this message come from modul2")

try:
    with open(logfile,"r+") as f:
        print f.read()
except:
    print "read file error"


