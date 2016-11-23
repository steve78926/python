#status: no ok
#coding:utf8

import random, time,multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 发送任务的队列:
#task_queue = Queue.Queue()
task_queue = multiprocessing.Queue()
# 接收结果的队列:
#result_queue = Queue.Queue()
result_queue = multiprocessing.Queue()

def get_task_queue():
    return task_queue

def get_result_queue():
    return result_queue

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable = get_task_queue)
QueueManager.register('get_result_queue', callable = get_result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('127.0.0.1', 5000), authkey='abc')
# 启动Queue:
#manager.start()
# 获得通过网络访问的Queue对象:

def communicate():
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
# 关闭:
    manager.shutdown()

if __name__ == '__main__':
    freeze_support()
    manager.start()
    communicate()