#-*- encoding:utf8-*-
#link: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832845200f6513494f0c64bd882f25818a0281e80000
#desc: thread local
#date: 2016-11-8

import threading

local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.currentThread().name)

def process_thread(name):
    local_school.student = name
    process_student()

def main():
    t1 = threading.Thread(target= process_thread, args=('Alice',),name='Thread-A')
    t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
