"""
@author Lucas
@date 2018/12/24 16:38

"""
import queue
import random
import threading
import time


# 生产者
def producer(i, q):
    while True:
        num = random.randint(0, 1000)
        q.put(num)
        print("生产者%d生产了%d放入队列" % (i, num))
        time.sleep(3)
    q.task_done()


# 消费者
def customer(i, q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d" % (i, item))
        time.sleep(2)
    q.task_done()


if __name__ == '__main__':
    # 消息队列
    q = queue.Queue()

    # 启动生产者
    for i in range(4):
        threading.Thread(target=producer, args=(i, q)).start()

    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer, args=(i, q)).start()
