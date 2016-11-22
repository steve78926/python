#ccoding:utf8
import time, threading

def loop():
    print 'thread %s is running.。.' % threading.currentThread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s ' % (threading.currentThread().name, n)
        time.sleep(1)
    print 'thread %s end.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.currentThread().name
